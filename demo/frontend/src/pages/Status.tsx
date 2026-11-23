import { useEffect, useState } from "react";
import { API_BASE, providerLabel, useCoverage, useHealth, useUsage } from "../api";
import { VersionLine } from "../components/VersionLine";
import { ISSUES_URL } from "../site";

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
      <h1>Status</h1>
      <p className="lede">
        This page asks the API when you open it. If it cannot get an answer it says
        so; it never assumes the demo is fine.
      </p>

      <section aria-live="polite">
        <h2>Right now</h2>
        <dl className="facts">
          <div>
            <dt>API</dt>
            <dd>
              {probe === "checking" && "Checking…"}
              {probe === "up" && "Reachable"}
              {probe === "down" && "Not reachable from your browser. The demo is down, or something between you and it is."}
            </dd>
          </div>
          <div>
            <dt>Model access</dt>
            <dd>
              {health.settled
                ? h
                  ? h.provider_ready
                    ? `Ready (${provider})`
                    : "Not ready: the demo cannot call a model right now"
                  : "Unknown: the API did not answer"
                : "Checking…"}
            </dd>
          </div>
          {h?.extraction_model && (
            <div>
              <dt>Reads your description</dt>
              <dd>
                <code>{h.extraction_model}</code>
              </dd>
            </div>
          )}
          {h?.synthesis_model && (
            <div>
              <dt>Writes the recommendation</dt>
              <dd>
                <code>{h.synthesis_model}</code>
              </dd>
            </div>
          )}
          {h?.limits && (
            <div>
              <dt>Searches today</dt>
              <dd>
                {h.limits.global_used_today} of {h.limits.global_daily_limit} (shared by everyone;
                each visitor gets {h.limits.per_client_hourly_limit} an hour)
              </dd>
            </div>
          )}
          {coverage && (
            <div>
              <dt>Entries served</dt>
              <dd>{coverage.total}</dd>
            </div>
          )}
        </dl>
        <VersionLine version={h?.version ?? coverage?.version} />
      </section>

      {usage && usage.days.length > 0 && (
        <section>
          <h2>Recent use</h2>
          <p>
            Days are UTC. {usage.note} The most useful column is
            &ldquo;found nothing&rdquo;: that is where someone asked and the knowledge
            base had no entry that fit.
          </p>
          <table className="plain-table plain-table--numeric">
            <caption className="sr-only">Searches per day and how they ended</caption>
            <thead>
              <tr>
                <th scope="col">Day</th>
                <th scope="col">Searches</th>
                <th scope="col">Finished</th>
                <th scope="col">Found nothing</th>
                <th scope="col">Failed</th>
                <th scope="col">Turned away</th>
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
        <h2>If it is down</h2>
        <p>
          There is no uptime promise: this is a research demo on one person&apos;s
          key and one small server. The knowledge base is plain files in the
          repository and the skill runs without this site, so a dead demo does not
          take the data with it. If you see a fault that is not listed here,{" "}
          <a href={ISSUES_URL} target="_blank" rel="noreferrer">
            open an issue
          </a>
          .
        </p>
      </section>
    </article>
  );
}
