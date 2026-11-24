import { useEffect, useState } from "react";
import { API_BASE, providerLabel, useCoverage, useHealth, useUsage } from "../api";
import { VersionLine } from "../components/VersionLine";
import { useLang } from "../i18n";
import { STATUS } from "../locales/status";

type Probe = "checking" | "up" | "down";

/**
 * Is the demo reachable, and what is it running on, read from the API now.
 *
 * It reports "down" when the browser cannot get an answer, not "all systems
 * normal" by default: the sibling status page this follows once rendered a
 * database failure as a healthy service (docs/status/SITE_SPEC.md, T11), and a
 * status page that cannot say "I cannot tell" is worse than none.
 */
export default function Status() {
  const lang = useLang();
  const m = STATUS[lang];
  const health = useHealth();
  const coverage = useCoverage().data;
  const usage = useUsage().data;
  const [probe, setProbe] = useState<Probe>("checking");

  useEffect(() => {
    let live = true;
    fetch(`${API_BASE}/healthz`)
      .then((r) => live && setProbe(r.ok ? "up" : "down"))
      .catch(() => live && setProbe("down"));
    return () => {
      live = false;
    };
  }, []);

  const h = health.data;
  const provider = providerLabel(h?.provider);

  return (
    <article className="prose">
      <h1>{m.title}</h1>
      <p className="lede">{m.lede}</p>

      <section aria-live="polite">
        <h2>{m.rightNow}</h2>
        <dl className="facts">
          <div>
            <dt>{m.api}</dt>
            <dd>
              {probe === "checking" && m.checking}
              {probe === "up" && m.reachable}
              {probe === "down" && m.unreachable}
            </dd>
          </div>
          <div>
            <dt>{m.modelAccess}</dt>
            <dd>
              {health.settled
                ? h
                  ? h.provider_ready
                    ? m.modelReady(provider)
                    : m.modelNotReady
                  : m.modelUnknown
                : m.checking}
            </dd>
          </div>
          {h?.extraction_model && (
            <div>
              <dt>{m.readsLabel}</dt>
              <dd>
                <code>{h.extraction_model}</code>
              </dd>
            </div>
          )}
          {h?.synthesis_model && (
            <div>
              <dt>{m.writesLabel}</dt>
              <dd>
                <code>{h.synthesis_model}</code>
              </dd>
            </div>
          )}
          {h?.limits && (
            <div>
              <dt>{m.searchesToday}</dt>
              <dd>{m.searchesTodayValue(h.limits)}</dd>
            </div>
          )}
          {coverage && (
            <div>
              <dt>{m.entriesServed}</dt>
              <dd>{coverage.total}</dd>
            </div>
          )}
        </dl>
        <VersionLine version={h?.version ?? coverage?.version} />
      </section>

      {usage && usage.days.length > 0 && (
        <section>
          <h2>{m.recentUse}</h2>
          <p>{m.recentIntro(lang === "en" ? usage.note : m.recentNote)}</p>
          <table className="plain-table plain-table--numeric">
            <caption className="sr-only">{m.tableCaption}</caption>
            <thead>
              <tr>
                <th scope="col">{m.cols.day}</th>
                <th scope="col">{m.cols.searches}</th>
                <th scope="col">{m.cols.finished}</th>
                <th scope="col">{m.cols.none}</th>
                <th scope="col">{m.cols.failed}</th>
                <th scope="col">{m.cols.refused}</th>
              </tr>
            </thead>
            <tbody>
              {[...usage.days].reverse().map((d) => (
                <tr key={d.date}>
                  <th scope="row">{d.date}</th>
                  <td>{d.searches}</td>
                  <td>{d.outcomes.completed ?? 0}</td>
                  <td>{d.outcomes.no_candidates ?? 0}</td>
                  <td>{d.outcomes.error ?? 0}</td>
                  <td>{d.outcomes.refused ?? 0}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      )}

      <section>
        <h2>{m.ifDownHeading}</h2>
        <p>{m.ifDown}</p>
      </section>
    </article>
  );
}
