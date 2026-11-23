import { useLang } from "../i18n";
import { HOME } from "../locales/home";
import sample from "../sample/screening-sample.json";

/**
 * The product shot on the home page: what the tool returns, drawn from a real
 * screening run rather than a mock-up, the way the sibling product pages show a
 * recorded game instead of invented scores.
 *
 * The data is demo/frontend/src/sample/screening-sample.json, written by
 * demo/backend/make_hero_sample.py from the corpus on disk (no language model
 * involved). The caption says which corpus and which day, and that the paper's
 * attributes were typed by hand. It is a dated snapshot, so it carries its date
 * instead of pretending to be live.
 */

export interface SampleCandidate {
  name: string;
  score: number;
  coverage: number;
  tied_with: number;
  tier: string;
  top_topics: { name: string; count: number }[];
}

function tierClass(tier: string): string {
  if (tier.startsWith("Tier 1")) return "tier-1";
  if (tier.startsWith("Tier 2")) return "tier-2";
  if (tier.startsWith("AI-Researched")) return "tier-ai";
  return "tier-skeleton";
}

export function HeroShot() {
  const lang = useLang();
  const m = HOME[lang];
  const candidates = sample.candidates as SampleCandidate[];
  const query = lang === "zh-Hant" ? sample.example.description_zh : sample.example.description;

  return (
    <figure className="hero-shot">
      <div className="shot-window" role="img" aria-label={m.shotAria}>
        <div className="shot-bar" aria-hidden="true">
          <span />
          <span />
          <span />
        </div>
        <div className="shot-body" aria-hidden="true">
          <p className="shot-query">
            <span className="shot-query-label">{m.shotQueryLabel}</span>
            {query}
          </p>
          <ol className="shot-list">
            {candidates.map((c, i) => (
              <li key={c.name} className="shot-card">
                <div className="shot-card-head">
                  <span className="shot-rank">{i + 1}</span>
                  <span className="shot-name">{c.name}</span>
                  <span className="shot-score">
                    {c.score.toFixed(1)}
                    <span className="shot-of">/100</span>
                  </span>
                </div>
                <div className="shot-meta">
                  <span className={`tier-badge ${tierClass(c.tier)}`}>{c.tier}</span>
                  <span className="shot-coverage">
                    {/* SVG attributes, not an inline style: the CSP allows no style="". */}
                    <svg className="shot-meter" viewBox="0 0 100 6" preserveAspectRatio="none">
                      <rect className="shot-meter-track" width="100" height="6" rx="3" />
                      <rect className="shot-meter-fill" width={Math.round(c.coverage * 100)} height="6" rx="3" />
                    </svg>
                    {m.evidencePct(Math.round(c.coverage * 100))}
                  </span>
                </div>
                {i === 0 && c.top_topics.length > 0 && (
                  <ul className="shot-topics">
                    {c.top_topics.map((t) => (
                      <li key={t.name}>
                        <span>{t.name}</span>
                        <span className="topic-count">{m.articles(t.count)}</span>
                      </li>
                    ))}
                  </ul>
                )}
              </li>
            ))}
          </ol>
        </div>
      </div>
      <figcaption>
        {m.shotCaption({
          shown: candidates.length,
          returned: sample.returned,
          corpus: sample.corpus ?? "",
          date: sample.generated,
        })}
      </figcaption>
    </figure>
  );
}
