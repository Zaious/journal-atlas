import type { Coverage } from "../api";
import { useLang } from "../i18n";
import { HOME, absentLabel } from "../locales/home";
import sample from "../sample/screening-sample.json";
import type { SampleCandidate } from "./HeroShot";

/**
 * The pictures beside the home page's feature sections. Like the hero shot they
 * are drawn from real output, not illustrations: the tier legend and score row
 * come from the same recorded screening run (sample/screening-sample.json), the
 * "not covered yet" list is live from /api/coverage, and the "not stated" lines
 * are the backend's own wording for that run.
 */

function Meter({ value }: { value: number }) {
  // SVG attributes, not an inline style: the CSP allows no style="".
  return (
    <svg className="shot-meter" viewBox="0 0 100 6" preserveAspectRatio="none" aria-hidden="true">
      <rect className="shot-meter-track" width="100" height="6" rx="3" />
      <rect className="shot-meter-fill" width={Math.round(value * 100)} height="6" rx="3" />
    </svg>
  );
}

export function EvidenceVisual() {
  const m = HOME[useLang()];
  const top = (sample.candidates as SampleCandidate[])[0];
  return (
    <div className="visual-card">
      <p className="visual-title">{m.legendTitle}</p>
      <ul className="legend-list">
        <li>
          <span className="tier-badge tier-1">Tier 1</span>
          <span>{m.legend.t1}</span>
        </li>
        <li>
          <span className="tier-badge tier-2">Tier 2</span>
          <span>{m.legend.t2}</span>
        </li>
        <li>
          <span className="tier-badge tier-ai">AI-Researched</span>
          <span>{m.legend.ai}</span>
        </li>
      </ul>
      {top && (
        <div className="legend-score">
          <p className="visual-label">{m.legendScoreLabel}</p>
          <div className="shot-card-head">
            <span className="shot-name">{top.name}</span>
            <span className="shot-score">
              {top.score.toFixed(1)}
              <span className="shot-of">/100</span>
            </span>
          </div>
          <div className="shot-coverage">
            <Meter value={top.coverage} />
            {m.evidencePct(Math.round(top.coverage * 100))}
          </div>
        </div>
      )}
    </div>
  );
}

export function UnknownVisual({ coverage }: { coverage: Coverage | null }) {
  const lang = useLang();
  const m = HOME[lang];
  return (
    <div className="visual-card">
      <p className="visual-title">{m.unknownTitle}</p>
      {coverage ? (
        <ul className="absent-list">
          {coverage.absent.map((a) => (
            <li key={a}>
              <span>{absentLabel(lang, a)}</span>
              <span className="absent-count">{m.unknownNone}</span>
            </li>
          ))}
        </ul>
      ) : (
        <p className="visual-label">{m.unknownLoading}</p>
      )}
      <p className="visual-title visual-title-second">{m.unstatedTitle}</p>
      <ul className="unstated-list">
        {sample.unstated.map((u) => (
          <li key={u} lang="en">
            {u}
          </li>
        ))}
      </ul>
      <p className="visual-label">{m.unstatedCaption}</p>
    </div>
  );
}
