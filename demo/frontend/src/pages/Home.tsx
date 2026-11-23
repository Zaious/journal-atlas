import { useEffect, useRef, useState } from "react";
import ReactMarkdown from "react-markdown";
import {
  API_BASE,
  fieldIsAllAi,
  providerLabel,
  useCoverage,
  useHealth,
  type Coverage,
} from "../api";
import { GitHubMark } from "../components/Layout";
import { HumanEvidence } from "../components/HumanEvidence";
import { VersionLine } from "../components/VersionLine";
import { useLang } from "../i18n";
import { HOME, fieldLabel, type HomeText, type StageName, type StageStatus } from "../locales/home";
import { SITE } from "../site";

interface ParsedPaper {
  topics: string[];
  methodology: string | null;
  sensitive_content: string[];
  fields: string[];
}

interface TopicEvidence {
  name: string;
  count: number;
}

interface Candidate {
  name: string;
  score: number;
  coverage?: number;
  tier: string;
  disputes: string[];
  top_topics: TopicEvidence[];
  // From the entry's Identity table. Any of these can be absent: the corpus
  // records a missing value as a blank rather than filling it, and a
  // conference has no ISSN to give. Render only what came back.
  venue_type?: string | null;
  publisher?: string | null;
  issn?: string | null;
  url?: string | null;
  // How many other candidates share this one's exact six-dimension profile.
  // Non-zero means the order between them came out of nothing, and saying so
  // is cheaper than letting the reader infer a ranking that is not there.
  tied_with?: number;
}

/** Hostname only, so a long publisher URL does not wrap the card. */
function linkLabel(url: string): string {
  try {
    return new URL(url).hostname.replace(/^www\./, "");
  } catch {
    return url;
  }
}

function tierClass(tier: string): string {
  if (tier.startsWith("Tier 1")) return "tier-1";
  if (tier.startsWith("Tier 2")) return "tier-2";
  if (tier.startsWith("AI-Researched")) return "tier-ai";
  return "tier-skeleton";
}

/**
 * What the corpus covers, stated before the user spends effort on a paste.
 *
 * Someone working in sociology or library science should learn that this tool
 * holds nothing for them from the page, not from a recommendation that quietly
 * reaches for the nearest psychology journal instead. Every count comes from
 * /api/coverage, so it is read off the corpus rather than written down here and
 * left to rot; a test fails the build if one is typed back in.
 */
function CoverageNotice({ data }: { data: Coverage | null }) {
  const lang = useLang();
  const m = HOME[lang];
  if (!data) return null;

  const philosophy = fieldIsAllAi(data, "philosophy");

  return (
    <details className="coverage-notice">
      <summary>{m.coverageSummary(data)}</summary>
      <div className="coverage-body">
        <table className="coverage-table">
          <caption className="sr-only">{m.coverageCaption}</caption>
          <thead>
            <tr>
              <th scope="col">{m.colField}</th>
              <th scope="col">{m.colEntries}</th>
              <th scope="col" title={m.tierTitles.t1}>
                T1
              </th>
              <th scope="col" title={m.tierTitles.t2}>
                T2
              </th>
              <th scope="col" title={m.tierTitles.ai}>
                AI
              </th>
            </tr>
          </thead>
          <tbody>
            {data.fields.map((f) => (
              <tr key={f.field}>
                <th scope="row">{fieldLabel(lang, f)}</th>
                <td className="num">{f.total}</td>
                <td className="num">{f.tier1 || "—"}</td>
                <td className="num">{f.tier2 || "—"}</td>
                <td className="num">{f.ai || "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>

        <p>{m.coverageAbsent(data)}</p>
        <p>{m.coverageNotForYou}</p>
        <p>{m.coverageThin(data, philosophy)}</p>
        <p>{m.coverageSee(<HumanEvidence coverage={data} />)}</p>
        <VersionLine version={data.version} />
      </div>
    </details>
  );
}

/**
 * Turn a non-OK response into a message worth reading.
 *
 * Rate-limit refusals (429) and oversized inputs (422) are the two errors a
 * real user is most likely to hit, and both have something actionable to say.
 * "Server error (429)" says none of it.
 */
async function describeFailure(res: Response, m: HomeText): Promise<string> {
  try {
    const body = await res.json();
    if (typeof body?.message === "string") return body.message;
    if (res.status === 422) return m.tooLong(MAX_DESCRIPTION_CHARS.toLocaleString());
  } catch {
    /* Body was not JSON; fall through to the status line. */
  }
  return m.serverError(res.status);
}

const MAX_DESCRIPTION_CHARS = 12000;

const INSTALL_COMMANDS = `/plugin marketplace add Zaious/journal-atlas
/plugin install journal-atlas@journal-atlas`;

/**
 * A copyable command block.
 *
 * `navigator.clipboard.writeText` rejects more often than it looks: denied
 * permission, a non-secure context, an embedded browser, or merely an unfocused
 * document. Swallowing that rejection leaves a button that appears to do
 * nothing, so failure falls back to selecting the text — the user still gets
 * one keystroke away from copying, and the label says which state they are in.
 */
function CodeBlock({ text }: { text: string }) {
  const m = HOME[useLang()];
  const [state, setState] = useState<"idle" | "copied" | "select">("idle");
  const preRef = useRef<HTMLPreElement>(null);

  function selectText() {
    const node = preRef.current;
    if (!node) return;
    const range = document.createRange();
    range.selectNodeContents(node);
    const selection = window.getSelection();
    selection?.removeAllRanges();
    selection?.addRange(range);
  }

  function handleCopy() {
    const done = (next: "copied" | "select") => {
      setState(next);
      setTimeout(() => setState("idle"), 2400);
    };
    if (!navigator.clipboard?.writeText) {
      selectText();
      done("select");
      return;
    }
    navigator.clipboard.writeText(text).then(
      () => done("copied"),
      () => {
        selectText();
        done("select");
      }
    );
  }

  return (
    <div className="code-block">
      <pre ref={preRef} tabIndex={0}>
        {text}
      </pre>
      <button type="button" className="copy-button" onClick={handleCopy}>
        {/* Labels stay short: the button is absolutely positioned over the
            command block, and a wider one would sit on top of the text the
            reserved padding is there to keep clear. */}
        {state === "copied" ? m.copy.copied : state === "select" ? m.copy.select : m.copy.idle}
      </button>
      <span className="sr-only" role="status">
        {state === "copied" ? m.copy.copiedSr : state === "select" ? m.copy.selectSr : ""}
      </span>
    </div>
  );
}

/**
 * What this demo is, why it is capped, and what to do instead.
 *
 * Every part of this is a consequence of one fact — the demo runs on one
 * person's API key — so it is stated first and the rest follows from it rather
 * than reading as a series of asks. The About page carries who made it and the
 * lineage; this keeps only what a visitor needs while deciding whether to paste.
 */
function HomeNotes({ coverage }: { coverage: Coverage | null }) {
  const health = useHealth().data;
  const m = HOME[useLang()];
  return (
    <div className="home-notes">
      {m.notes({ coverage, limits: health?.limits ?? null, install: <CodeBlock text={INSTALL_COMMANDS} /> })}
    </div>
  );
}

const STAGE_ORDER: StageName[] = ["parsing", "screening", "synthesis"];

export default function Home() {
  const coverage = useCoverage().data;
  const health = useHealth().data;
  const provider = providerLabel(health?.provider);
  const lang = useLang();
  const m = HOME[lang];
  const labels = m.stageLabels(coverage?.total ?? null);

  const [paperText, setPaperText] = useState("");
  const [running, setRunning] = useState(false);
  const [stages, setStages] = useState<Record<StageName, StageStatus>>({
    parsing: "pending",
    screening: "pending",
    synthesis: "pending",
  });
  const [parsedPaper, setParsedPaper] = useState<ParsedPaper | null>(null);
  const [unstated, setUnstated] = useState<string[]>([]);
  const [candidates, setCandidates] = useState<Candidate[] | null>(null);
  const [expanded, setExpanded] = useState<Set<string>>(new Set());
  const [synthesisText, setSynthesisText] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [clarifyQuestion, setClarifyQuestion] = useState<string | null>(null);
  const [clarifyAnswer, setClarifyAnswer] = useState("");
  const [followupQ, setFollowupQ] = useState("");
  const [followups, setFollowups] = useState<{ q: string; a: string }[]>([]);
  const [followupBusy, setFollowupBusy] = useState(false);
  const abortRef = useRef<AbortController | null>(null);
  const MAX_FOLLOWUPS = 2;

  // Cancel an in-flight stream if the page unmounts, so a navigation does not
  // leave the provider generating text nobody will read.
  useEffect(() => () => abortRef.current?.abort(), []);

  function toggleExpanded(name: string) {
    setExpanded((prev) => {
      const next = new Set(prev);
      if (next.has(name)) next.delete(name);
      else next.add(name);
      return next;
    });
  }

  function handleEvent(name: string, data: any) {
    if (name === "stage") {
      const stage = data.stage as StageName;
      if (data.status === "start") {
        setStages((s) => ({ ...s, [stage]: "active" }));
      } else if (data.status === "done") {
        setStages((s) => ({ ...s, [stage]: "done" }));
        if (stage === "parsing") {
          setParsedPaper(data.paper);
          setUnstated(data.unstated ?? []);
        }
        if (stage === "screening") setCandidates(data.candidates);
      }
    } else if (name === "clarify") {
      setClarifyQuestion(data.question);
    } else if (name === "text") {
      setSynthesisText((t) => t + data.delta);
    } else if (name === "error") {
      setError(data.message);
    }
  }

  async function runRecommendation(opts?: { clarifications?: string; skipClarify?: boolean }) {
    if (!paperText.trim() || running) return;
    setRunning(true);
    setError(null);
    setParsedPaper(null);
    setUnstated([]);
    setCandidates(null);
    setExpanded(new Set());
    setSynthesisText("");
    setClarifyQuestion(null);
    setFollowups([]);
    setFollowupQ("");
    setStages({ parsing: "active", screening: "pending", synthesis: "pending" });

    const controller = new AbortController();
    abortRef.current = controller;

    try {
      const res = await fetch(`${API_BASE}/api/recommend`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          paper_description: paperText,
          clarifications: opts?.clarifications ?? null,
          skip_clarify: opts?.skipClarify ?? false,
        }),
        signal: controller.signal,
      });
      if (!res.ok || !res.body) throw new Error(await describeFailure(res, m));

      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });

        const events = buffer.split("\n\n");
        buffer = events.pop() ?? "";
        for (const raw of events) {
          if (!raw.trim()) continue;
          const eventMatch = raw.match(/^event: (.+)$/m);
          const dataMatch = raw.match(/^data: (.+)$/m);
          if (!eventMatch || !dataMatch) continue;
          handleEvent(eventMatch[1], JSON.parse(dataMatch[1]));
        }
      }
    } catch (e) {
      if ((e as Error).name !== "AbortError") {
        setError((e as Error).message);
      }
    } finally {
      setRunning(false);
    }
  }

  async function askFollowup() {
    if (!followupQ.trim() || followupBusy || followups.length >= MAX_FOLLOWUPS) return;
    const question = followupQ.trim();
    setFollowupBusy(true);
    setFollowupQ("");
    setFollowups((f) => [...f, { q: question, a: "" }]);
    try {
      const res = await fetch(`${API_BASE}/api/followup`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          paper_description: paperText,
          recommendation: synthesisText,
          question,
          candidate_names: (candidates ?? []).map((c) => c.name),
          asked_so_far: followups.length,
        }),
      });
      if (!res.ok || !res.body) throw new Error(await describeFailure(res, m));
      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const events = buffer.split("\n\n");
        buffer = events.pop() ?? "";
        for (const raw of events) {
          if (!raw.trim()) continue;
          const em = raw.match(/^event: (.+)$/m);
          const dm = raw.match(/^data: (.+)$/m);
          if (!em || !dm) continue;
          const payload = JSON.parse(dm[1]);
          if (em[1] === "text") {
            setFollowups((f) =>
              f.map((x, i) => (i === f.length - 1 ? { ...x, a: x.a + payload.delta } : x))
            );
          } else if (em[1] === "error") {
            setError(payload.message);
          }
        }
      }
    } catch (e) {
      setError((e as Error).message);
      // A refused request should not cost the user one of their two
      // follow-ups, so drop the placeholder and give the question back.
      setFollowups((f) => f.slice(0, -1));
      setFollowupQ(question);
    } finally {
      setFollowupBusy(false);
    }
  }

  const followupsLeft = MAX_FOLLOWUPS - followups.length;
  const activeStage = STAGE_ORDER.find((s) => stages[s] === "active");

  return (
    <>
      <div className="page-head">
        <div className="header-top">
          <h1>Journal Atlas</h1>
          <a className="repo-link" href={SITE.repoUrl} target="_blank" rel="noreferrer">
            <GitHubMark />
            <span>{m.repoLink}</span>
          </a>
        </div>
        <p className="eyebrow">{m.eyebrow}</p>
        <p className="tagline">{m.tagline}</p>
      </div>

      <CoverageNotice data={coverage} />

      <label className="field-label" htmlFor="paper-text">
        {m.paperLabel}
      </label>
      <textarea
        id="paper-text"
        value={paperText}
        onChange={(e) => setPaperText(e.target.value)}
        placeholder={m.paperPlaceholder}
        rows={6}
        disabled={running}
        aria-describedby="paper-note"
      />
      <p className="field-note" id="paper-note">
        {m.paperNote(provider)}
      </p>

      <button onClick={() => runRecommendation()} disabled={running || !paperText.trim()}>
        {running ? m.working : m.findJournal}
      </button>

      <noscript>
        <p className="error">{m.noscript}</p>
      </noscript>

      {(running || stages.parsing !== "pending") && (
        <>
          <p className="sr-only" role="status" aria-live="polite">
            {activeStage ? `${labels[activeStage]}…` : stages.synthesis === "done" ? m.recommendationReady : ""}
          </p>
          <ol className="stages">
            {STAGE_ORDER.map((s) => (
              <li key={s} className={`stage stage-${stages[s]}`}>
                <span className="stage-dot" aria-hidden="true" />
                {labels[s]}
                <span className="sr-only"> ({m.stageState[stages[s]]})</span>
              </li>
            ))}
          </ol>
        </>
      )}

      {error && (
        <div className="error" role="alert">
          {error}
        </div>
      )}

      {parsedPaper && (
        <div className="panel">
          <h2>{m.readHeading}</h2>
          <p>
            <strong>{m.topics}</strong> {parsedPaper.topics.join(lang === "en" ? ", " : "、") || "—"}
            <br />
            <strong>{m.methodology}</strong> {parsedPaper.methodology ?? "—"}
            {parsedPaper.sensitive_content.length > 0 && (
              <>
                <br />
                <strong>{m.sensitive}</strong>{" "}
                {parsedPaper.sensitive_content.join(lang === "en" ? ", " : "、")}
              </>
            )}
          </p>
          {unstated.length > 0 && (
            <ul className="unstated-list">
              {unstated.map((u) => (
                <li key={u}>{u}</li>
              ))}
            </ul>
          )}
        </div>
      )}

      {clarifyQuestion && (
        <div className="panel clarify">
          <h2>{m.clarifyHeading}</h2>
          <div className="synthesis-text">
            <ReactMarkdown>{clarifyQuestion}</ReactMarkdown>
          </div>
          <label className="sr-only" htmlFor="clarify-answer">
            {m.clarifyAnswersLabel}
          </label>
          <textarea
            id="clarify-answer"
            value={clarifyAnswer}
            onChange={(e) => setClarifyAnswer(e.target.value)}
            placeholder={m.clarifyPlaceholder}
            rows={3}
            disabled={running}
          />
          <div className="clarify-actions">
            <button
              onClick={() => runRecommendation({ clarifications: clarifyAnswer })}
              disabled={running || !clarifyAnswer.trim()}
            >
              {m.clarifyAnswer}
            </button>
            <button
              className="secondary"
              onClick={() => runRecommendation({ skipClarify: true })}
              disabled={running}
            >
              {m.clarifySkip}
            </button>
          </div>
        </div>
      )}

      {candidates && (
        <div className="panel">
          <h2>{m.candidatesHeading(candidates.length)}</h2>
          <ul className="candidate-list">
            {candidates.map((c) => {
              const isOpen = expanded.has(c.name);
              return (
                <li key={c.name} className="candidate-card">
                  <button
                    type="button"
                    className="candidate-header"
                    onClick={() => toggleExpanded(c.name)}
                    aria-expanded={isOpen}
                  >
                    <span className="candidate-name">
                      <span className={`tier-badge ${tierClass(c.tier)}`}>{c.tier}</span>
                      {c.disputes?.length > 0 && (
                        <span className="tier-badge tier-disputed">{m.disputedTag}</span>
                      )}
                      {c.name}
                    </span>
                    <span className="score">
                      {c.score.toFixed(1)}/100
                      {c.coverage !== undefined && (
                        <span className="coverage" title={m.evidencePctTitle}>
                          {" "}· {m.evidencePct(Math.round(c.coverage * 100))}
                        </span>
                      )}
                      {!!c.tied_with && c.tied_with > 0 && (
                        <span
                          className="coverage tied"
                          title={m.tiedTitle(c.tied_with)}
                        >
                          {" "}· {m.tiedWith(c.tied_with)}
                        </span>
                      )}
                    </span>
                  </button>
                  {isOpen && (
                    <div className="candidate-evidence">
                      {c.disputes?.length > 0 && (
                        <ul className="dispute-list">
                          {c.disputes.map((d) => (
                            <li key={d}>
                              {m.disputedClaim} {d}
                            </li>
                          ))}
                        </ul>
                      )}
                      {(c.publisher || c.issn || c.url) && (
                        <p className="candidate-identity">
                          {c.publisher}
                          {c.publisher && c.issn ? " · " : ""}
                          {c.issn ? `ISSN ${c.issn}` : ""}
                          {(c.publisher || c.issn) && c.url ? " · " : ""}
                          {c.url && (
                            <a href={c.url} target="_blank" rel="noopener noreferrer">
                              {linkLabel(c.url)}
                            </a>
                          )}
                        </p>
                      )}
                      {c.top_topics.length > 0 ? (
                        <ul className="topic-evidence-list">
                          {c.top_topics.map((t) => (
                            <li key={t.name}>
                              {t.name}
                              <span className="topic-count">{m.articles(t.count)}</span>
                            </li>
                          ))}
                        </ul>
                      ) : (
                        <p className="no-evidence">
                          {m.noTopicData}
                        </p>
                      )}
                    </div>
                  )}
                </li>
              );
            })}
          </ul>
        </div>
      )}

      {synthesisText && (
        <div className="panel synthesis">
          <h2>{m.recommendationHeading}</h2>
          <div className="synthesis-text">
            <ReactMarkdown>{synthesisText}</ReactMarkdown>
          </div>
        </div>
      )}

      {synthesisText && !running && (
        <div className="panel">
          <h2>{m.followupHeading(followupsLeft)}</h2>
          {followups.map((f, i) => (
            <div key={i} className="followup">
              <p className="followup-q">{f.q}</p>
              <div className="synthesis-text">
                <ReactMarkdown>{f.a}</ReactMarkdown>
              </div>
            </div>
          ))}
          {followupsLeft > 0 ? (
            <>
              <label className="sr-only" htmlFor="followup-q">
                {m.followupLabel}
              </label>
              <textarea
                id="followup-q"
                value={followupQ}
                onChange={(e) => setFollowupQ(e.target.value)}
                placeholder={m.followupPlaceholder}
                rows={2}
                disabled={followupBusy}
              />
              <button onClick={askFollowup} disabled={followupBusy || !followupQ.trim()}>
                {followupBusy ? m.thinking : m.ask}
              </button>
            </>
          ) : (
            <p className="no-evidence">
              {m.followupLimit}
            </p>
          )}
        </div>
      )}

      <HomeNotes coverage={coverage} />
    </>
  );
}
