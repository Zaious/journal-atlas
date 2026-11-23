import { useEffect, useRef, useState } from "react";
import ReactMarkdown from "react-markdown";
import {
  API_BASE,
  corePercent,
  fieldIsAllAi,
  providerLabel,
  useCoverage,
  useHealth,
  type Coverage,
} from "../api";
import { GitHubMark } from "../components/Layout";
import { HumanEvidence } from "../components/HumanEvidence";
import { VersionLine } from "../components/VersionLine";
import { ISSUES_URL, SITE } from "../site";

type StageName = "parsing" | "screening" | "synthesis";
type StageStatus = "pending" | "active" | "done";

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
  if (!data) return null;

  const philosophy = fieldIsAllAi(data, "philosophy");

  return (
    <details className="coverage-notice">
      <summary>
        Covers <strong>{data.core_label}</strong> in depth — {corePercent(data)}% of{" "}
        {data.total} entries. Many fields are not covered at all.{" "}
        <span className="coverage-more">What&apos;s in here?</span>
      </summary>
      <div className="coverage-body">
        <table className="coverage-table">
          <caption className="sr-only">Entries per field, by how each entry was written</caption>
          <thead>
            <tr>
              <th scope="col">Field</th>
              <th scope="col">Entries</th>
              <th scope="col" title="Evidence-backed: specific article counts, source URLs, dates">
                T1
              </th>
              <th scope="col" title="Community estimate: family-level, no per-claim evidence yet">
                T2
              </th>
              <th scope="col" title="AI-researched: per-journal sources, honest blanks, no human review recorded">
                AI
              </th>
            </tr>
          </thead>
          <tbody>
            {data.fields.map((f) => (
              <tr key={f.field}>
                <th scope="row">{f.label}</th>
                <td className="num">{f.total}</td>
                <td className="num">{f.tier1 || "—"}</td>
                <td className="num">{f.tier2 || "—"}</td>
                <td className="num">{f.ai || "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>

        <p>
          <strong>Verifiably absent</strong> (probed {data.absent_checked}):{" "}
          {data.absent.join(" · ")}. Economics, law and political science exist only
          as philosophy journals <em>about</em> those subjects. There is no
          marketing, no nursing science, and no engineering beyond three robotics
          venues.
        </p>
        <p>
          If your field is on that list, this tool has nothing for you yet — and it
          will tell you that rather than ranking the nearest journals it happens to
          hold.
        </p>
        <p>
          Entries also differ in <strong>how much of each one is filled in</strong>.
          Unscorable dimensions return &quot;unknown&quot; instead of a midpoint, so every
          candidate carries an evidence-coverage figure. The {data.tiers.ai}{" "}
          AI-researched entries are missing the parts that need lived submission
          experience, so they usually show far less coverage than the others.{" "}
          {philosophy && (
            <strong>
              Philosophy is the sharpest case: all {philosophy.total} of its entries are
              AI-researched.
            </strong>
          )}{" "}
          Scores on thin evidence are already pulled toward a neutral 50, but treat
          them as leads to check.
        </p>
        <p>
          <HumanEvidence coverage={data} /> See{" "}
          <a href="/ai/">how the entries were made</a>.
        </p>
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
async function describeFailure(res: Response): Promise<string> {
  try {
    const body = await res.json();
    if (typeof body?.message === "string") return body.message;
    if (res.status === 422) {
      return `That description is too long for the demo — paste an abstract or a summary rather than the full manuscript. (Limit: ${MAX_DESCRIPTION_CHARS.toLocaleString()} characters.)`;
    }
  } catch {
    /* Body was not JSON; fall through to the status line. */
  }
  return `Server error (${res.status})`;
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
        {state === "copied" ? "Copied" : state === "select" ? "Ctrl+C" : "Copy"}
      </button>
      <span className="sr-only" role="status">
        {state === "copied" ? "Copied to clipboard" : state === "select" ? "Text selected; press Ctrl+C" : ""}
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
  const limits = health?.limits ?? null;
  const absent = coverage?.absent ?? [];

  return (
    <div className="home-notes">
      <section>
        <h2>This is an experiment, running on one person&apos;s API key</h2>
        <p>
          Journal Atlas is a research project, not a service. There is no company
          behind it and no uptime promise — the model calls this page makes are
          billed to the maintainer personally, which is the only reason it is
          capped
          {limits
            ? ` at ${limits.per_client_hourly_limit} searches an hour per person and ${limits.global_daily_limit} a day across everyone`
            : ""}
          . The cap is a budget, not a paywall: there is no tier that removes it,
          because there is nothing to sell.
        </p>
      </section>

      <section>
        <h2>Run it yourself, with no cap at all</h2>
        <p>
          The demo is a shop window. The real thing is a skill that runs inside
          your own Claude session, against your own key, over the same knowledge
          base — no limits, no queue, and it can read your actual manuscript
          instead of a pasted summary. In a Claude Code <strong>main session</strong>:
        </p>
        <CodeBlock text={INSTALL_COMMANDS} />
        <p className="footnote">
          Then restart Claude Code. Claude Desktop, ChatGPT and plain-git setups
          are covered in the{" "}
          <a href={`${SITE.repoUrl}#installation`} target="_blank" rel="noreferrer">
            installation guide
          </a>
          . The knowledge base is {SITE.license.content} — you can also just read it.
        </p>
      </section>

      <section>
        <h2>Your field is probably not in here</h2>
        <p>
          {coverage ? (
            <>
              {corePercent(coverage)}% of the corpus is {coverage.core_label}.
              {absent.length > 0 && <> At zero: {absent.join("; ")}.</>}
            </>
          ) : (
            <>
              Most of the corpus sits in a few adjacent fields, and many fields
              have nothing at all. The coverage note above lists which.
            </>
          )}{" "}
          Two things fix that, and neither requires touching code:
        </p>
        <ul>
          <li>
            <strong>Bring a whole field in.</strong> The AI-research expansion that
            added{coverage ? ` the ${coverage.tiers.ai}` : " the"} AI-researched entries was one
            run over a target list, and{" "}
            <a
              href={`${SITE.repoUrl}/blob/main/docs/workorders/WO2_SOFT_METADATA_BATCH.md`}
              target="_blank"
              rel="noreferrer"
            >
              the procedure is published
            </a>{" "}
            so you can point it at yours. Twenty journals is a real contribution.
          </li>
          <li>
            <strong>Tell us how it actually went.</strong> If you have submitted
            to or reviewed for a journal, you hold the part no amount of research
            reaches — whether the word limit is real, how the reviewer pool treats
            qualitative work, what a desk rejection there means. That is exactly
            what the AI-researched entries are missing, and no entry yet records
            it. Ten minutes on one journal you know well beats a hundred scraped
            ones.
          </li>
        </ul>
      </section>

      <section>
        <h2>And it needs more than one maintainer</h2>
        <p>
          Scholarly tools die a specific death: one person builds something
          genuinely useful, maintains it alone, and then their circumstances
          change — and the whole thing goes read-only, then stale, then wrong.
          Anyone who has watched a library or digital-humanities project go dark
          knows the pattern.
        </p>
        <p>
          The licence is a partial answer — {SITE.license.content} content and{" "}
          {SITE.license.code} code mean nobody can be locked out of a fork. But a
          fork nobody maintains is still dead. So if this turns out to be worth
          keeping,{" "}
          <strong>the thing it most needs is co-maintainers</strong>: people who
          will review contributions in their own field and correct entries about
          journals they know. Say so in an{" "}
          <a href={ISSUES_URL} target="_blank" rel="noreferrer">
            issue
          </a>{" "}
          and you will be taken up on it. <a href="/about/">Who made this, and why</a>.
        </p>
      </section>
    </div>
  );
}

function stageLabels(total: number | null): Record<StageName, string> {
  return {
    parsing: "Reading your paper",
    screening: total ? `Screening ${total} entries` : "Screening the knowledge base",
    synthesis: "Writing your recommendation",
  };
}

const STAGE_ORDER: StageName[] = ["parsing", "screening", "synthesis"];
const STAGE_STATE_TEXT: Record<StageStatus, string> = {
  pending: "waiting",
  active: "in progress",
  done: "done",
};

export default function Home() {
  const coverage = useCoverage().data;
  const health = useHealth().data;
  const provider = providerLabel(health?.provider);
  const labels = stageLabels(coverage?.total ?? null);

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
      if (!res.ok || !res.body) throw new Error(await describeFailure(res));

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
      if (!res.ok || !res.body) throw new Error(await describeFailure(res));
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
            <span>Source on GitHub</span>
          </a>
        </div>
        <p className="eyebrow">
          A live demo of an open-source <strong>agent skill</strong> — the thing
          answering you here installs into your own AI session in one command,
          and runs there without this page or its limits.
        </p>
        <p className="tagline">
          Paste your abstract or describe your paper. No account, no install —
          this reads the same open knowledge base the real skill uses, and shows
          for every entry how it was written and how much of it is evidenced.
        </p>
      </div>

      <CoverageNotice data={coverage} />

      <label className="field-label" htmlFor="paper-text">
        Your paper
      </label>
      <textarea
        id="paper-text"
        value={paperText}
        onChange={(e) => setPaperText(e.target.value)}
        placeholder="e.g. A qualitative study using autoethnography to explore embodied cognition in collaborative design teams. ~9,000 words, no institutional funding for open access, discloses AI-assisted copyediting..."
        rows={6}
        disabled={running}
        aria-describedby="paper-note"
      />
      <p className="field-note" id="paper-note">
        What you paste is sent to a language-model provider
        {provider ? ` (currently ${provider})` : ""} to be read, and this site does
        not save it. Paste an abstract, not a manuscript that is under review.{" "}
        <a href="/privacy/">What happens to it</a>.
      </p>

      <button onClick={() => runRecommendation()} disabled={running || !paperText.trim()}>
        {running ? "Working…" : "Find my journal"}
      </button>

      <noscript>
        <p className="error">The recommender needs JavaScript. The knowledge base itself is plain Markdown in the repository.</p>
      </noscript>

      {(running || stages.parsing !== "pending") && (
        <>
          <p className="sr-only" role="status" aria-live="polite">
            {activeStage ? `${labels[activeStage]}…` : stages.synthesis === "done" ? "Recommendation ready" : ""}
          </p>
          <ol className="stages">
            {STAGE_ORDER.map((s) => (
              <li key={s} className={`stage stage-${stages[s]}`}>
                <span className="stage-dot" aria-hidden="true" />
                {labels[s]}
                <span className="sr-only"> ({STAGE_STATE_TEXT[stages[s]]})</span>
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
          <h2>What I read from your description</h2>
          <p>
            <strong>Topics:</strong> {parsedPaper.topics.join(", ") || "—"}
            <br />
            <strong>Methodology:</strong> {parsedPaper.methodology ?? "—"}
            {parsedPaper.sensitive_content.length > 0 && (
              <>
                <br />
                <strong>Flagged sensitive content:</strong>{" "}
                {parsedPaper.sensitive_content.join(", ")}
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
          <h2>A couple of questions first</h2>
          <div className="synthesis-text">
            <ReactMarkdown>{clarifyQuestion}</ReactMarkdown>
          </div>
          <label className="sr-only" htmlFor="clarify-answer">
            Your answers
          </label>
          <textarea
            id="clarify-answer"
            value={clarifyAnswer}
            onChange={(e) => setClarifyAnswer(e.target.value)}
            placeholder="e.g. no budget at all; about 8,000 words; conferences are fine too"
            rows={3}
            disabled={running}
          />
          <div className="clarify-actions">
            <button
              onClick={() => runRecommendation({ clarifications: clarifyAnswer })}
              disabled={running || !clarifyAnswer.trim()}
            >
              Answer and search
            </button>
            <button
              className="secondary"
              onClick={() => runRecommendation({ skipClarify: true })}
              disabled={running}
            >
              Skip — search anyway
            </button>
          </div>
        </div>
      )}

      {candidates && (
        <div className="panel">
          <h2>Top {candidates.length} candidates after screening</h2>
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
                        <span className="tier-badge tier-disputed">Disputed</span>
                      )}
                      {c.name}
                    </span>
                    <span className="score">
                      {c.score.toFixed(1)}/100
                      {c.coverage !== undefined && (
                        <span className="coverage" title="Share of the scoring dimensions that had actual data behind them">
                          {" "}· {Math.round(c.coverage * 100)}% evidence
                        </span>
                      )}
                      {!!c.tied_with && c.tied_with > 0 && (
                        <span
                          className="coverage tied"
                          title={`Scores identically to ${c.tied_with} other candidate${
                            c.tied_with > 1 ? "s" : ""
                          } on all six dimensions. The order between them is arbitrary.`}
                        >
                          {" "}· tied with {c.tied_with}
                        </span>
                      )}
                    </span>
                  </button>
                  {isOpen && (
                    <div className="candidate-evidence">
                      {c.disputes?.length > 0 && (
                        <ul className="dispute-list">
                          {c.disputes.map((d) => (
                            <li key={d}>Disputed claim: {d}</li>
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
                              <span className="topic-count">{t.count} articles</span>
                            </li>
                          ))}
                        </ul>
                      ) : (
                        <p className="no-evidence">
                          No topic-count data on file for this entry yet.
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
          <h2>Recommendation</h2>
          <div className="synthesis-text">
            <ReactMarkdown>{synthesisText}</ReactMarkdown>
          </div>
        </div>
      )}

      {synthesisText && !running && (
        <div className="panel">
          <h2>Follow-up {followupsLeft > 0 ? `(${followupsLeft} left)` : "(none left)"}</h2>
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
                Your follow-up question
              </label>
              <textarea
                id="followup-q"
                value={followupQ}
                onChange={(e) => setFollowupQ(e.target.value)}
                placeholder="e.g. why not CHI? / what would I need to change for the second choice?"
                rows={2}
                disabled={followupBusy}
              />
              <button onClick={askFollowup} disabled={followupBusy || !followupQ.trim()}>
                {followupBusy ? "Thinking…" : "Ask"}
              </button>
            </>
          ) : (
            <p className="no-evidence">
              Two follow-ups is the limit for this demo. Edit your description above and search
              again to explore a different angle.
            </p>
          )}
        </div>
      )}

      <HomeNotes coverage={coverage} />
    </>
  );
}
