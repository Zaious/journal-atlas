import { useEffect, useRef, useState } from "react";
import ReactMarkdown from "react-markdown";
import "./App.css";

const API_BASE = import.meta.env.VITE_API_BASE ?? "http://localhost:8000";

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
}

function tierClass(tier: string): string {
  if (tier.startsWith("Tier 1")) return "tier-1";
  if (tier.startsWith("Tier 2")) return "tier-2";
  if (tier.startsWith("AI-Researched")) return "tier-ai";
  return "tier-skeleton";
}

interface CoverageField {
  field: string;
  label: string;
  tier1: number;
  tier2: number;
  ai: number;
  total: number;
}

interface Coverage {
  total: number;
  fields: CoverageField[];
  core_fields: string[];
  core_label: string;
  absent: string[];
  absent_checked: string;
}

/**
 * What the corpus covers, stated before the user spends effort on a paste.
 *
 * Someone working in sociology or library science should learn that this tool
 * holds nothing for them from the page, not from a recommendation that quietly
 * reaches for the nearest psychology journal instead. The counts come from
 * /api/coverage so they are read off the corpus rather than written down here
 * and left to rot.
 */
function CoverageNotice() {
  const [data, setData] = useState<Coverage | null>(null);

  useEffect(() => {
    fetch(`${API_BASE}/api/coverage`)
      .then((r) => (r.ok ? r.json() : null))
      .then(setData)
      .catch(() => setData(null));
  }, []);

  if (!data) return null;

  const coreTotal = data.fields
    .filter((f) => data.core_fields.includes(f.field))
    .reduce((n, f) => n + f.total, 0);
  const corePct = Math.round((coreTotal / data.total) * 100);

  return (
    <details className="coverage-notice">
      <summary>
        Covers <strong>{data.core_label}</strong> in depth — {corePct}% of{" "}
        {data.total} entries. Many fields are not covered at all.{" "}
        <span className="coverage-more">What's in here?</span>
      </summary>
      <div className="coverage-body">
        <table className="coverage-table">
          <thead>
            <tr>
              <th>Field</th>
              <th>Entries</th>
              <th title="Evidence-backed">T1</th>
              <th title="Community estimate">T2</th>
              <th title="AI-researched, awaiting human verification">AI</th>
            </tr>
          </thead>
          <tbody>
            {data.fields.map((f) => (
              <tr key={f.field}>
                <td>{f.label}</td>
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
          Unscorable dimensions return "unknown" instead of a midpoint, so every
          candidate carries an evidence-coverage figure: 163 entries sit at 85–100%,
          while 236 AI-researched ones sit near 40% and are missing the parts that
          need lived submission experience. <strong>Philosophy is the sharpest case —
          106 entries, none human-verified.</strong> Scores on thin evidence are
          already pulled toward a neutral 50, but treat them as leads to check.
        </p>
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

const REPO_URL = "https://github.com/Zaious/journal-atlas";

// Buy Me a Coffee rather than GitHub Sponsors: sponsoring on GitHub requires
// the *sponsor* to hold a GitHub account, and this page's audience is
// researchers in psychology and philosophy, most of whom do not. BMC takes card
// payments with no registration.
//
// Defaulted rather than required, so a deployment that forgets the env var
// still shows the link. Setting the variable to an empty string turns it off —
// `??` only falls back when it is genuinely unset.
const SUPPORT_URL: string =
  import.meta.env.VITE_SUPPORT_URL ?? "https://buymeacoffee.com/zaious";
const SUPPORT_LABEL: string =
  import.meta.env.VITE_SUPPORT_LABEL ?? "Buy me a coffee";

const INSTALL_COMMANDS = `/plugin marketplace add Zaious/journal-atlas
/plugin install journal-atlas@journal-atlas`;

/** GitHub mark, inlined rather than fetched — no external asset for one icon. */
function GitHubMark() {
  return (
    <svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true" fill="currentColor">
      <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z" />
    </svg>
  );
}

interface Limits {
  global_daily_limit: number;
  per_client_hourly_limit: number;
  per_client_daily_limit: number;
}

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
      <pre ref={preRef}>{text}</pre>
      <button type="button" className="copy-button" onClick={handleCopy}>
        {/* Labels stay short: the button is absolutely positioned over the
            command block, and a wider one would sit on top of the text the
            reserved padding is there to keep clear. */}
        {state === "copied" ? "Copied" : state === "select" ? "Ctrl+C" : "Copy"}
      </button>
    </div>
  );
}

/**
 * What this demo is, why it is capped, and what to do instead.
 *
 * Every part of this is a consequence of one fact — the demo runs on one
 * person's API key — so it is stated first and the rest follows from it rather
 * than reading as a series of asks.
 */
function SiteFooter() {
  const [limits, setLimits] = useState<Limits | null>(null);

  useEffect(() => {
    fetch(`${API_BASE}/api/health`)
      .then((r) => (r.ok ? r.json() : null))
      .then((d) => setLimits(d?.limits ?? null))
      .catch(() => setLimits(null));
  }, []);

  return (
    <footer className="site-footer">
      <section>
        <h2>This is an experiment, running on one person's API key</h2>
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
          <a href={`${REPO_URL}#installation`} target="_blank" rel="noreferrer">
            installation guide
          </a>
          . The knowledge base is CC BY-SA — you can also just read it.
        </p>
      </section>

      <section>
        <h2>Your field is probably not in here</h2>
        <p>
          88% of the corpus is psychology, philosophy, HCI and cognitive science.
          Library science, sociology, anthropology and the physical sciences are
          at zero. Two things fix that, and neither requires touching code:
        </p>
        <ul>
          <li>
            <strong>Bring a whole field in.</strong> The 236-entry expansion that
            built most of this corpus was one AI research run over a target list,
            and{" "}
            <a
              href={`${REPO_URL}/blob/main/docs/workorders/WO2_SOFT_METADATA_BATCH.md`}
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
            what 236 of our 399 entries are missing. Ten minutes on one journal
            you know well beats a hundred scraped ones.
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
          The licence is a partial answer — CC BY-SA content and MIT code mean
          nobody can be locked out of a fork. But a fork nobody maintains is
          still dead. So if this turns out to be worth keeping,{" "}
          <strong>the thing it most needs is co-maintainers</strong>: people who
          will review contributions in their own field and correct entries about
          journals they know. Say so in an issue and you will be taken up on it.
        </p>
      </section>

      <section className="colophon">
        <h2>Who made this, and why</h2>
        <p>
          I'm{" "}
          <a href="https://zaious.dev/" target="_blank" rel="noreferrer">
            Meng-Han Lee (李孟翰)
          </a>{" "}
          — an independent HCI researcher and AI agent architect, working
          outside an institution. This started as my own problem. I had
          manuscripts to place, the qualitative and theoretical kind that get
          judged by standards written for other work, and the question "where
          does this actually belong?" had no good answer anywhere. Ask a model
          and it names the most famous journals in the area. Ask a colleague who
          has published there and you get something worth ten times as much —
          but only if you happen to know that colleague.
        </p>
        <p>
          So I started writing down what that colleague would have said. The
          project is what happened when I kept going, and then made the
          machine-readable version an AI agent could read without inventing the
          parts nobody had written down yet.
        </p>
      </section>

      <section className="colophon">
        <h2>Picking up where Open Journal Matcher left off</h2>
        <p>
          There is a twenty-year line of journal recommenders, and most of them
          are switched off. The one this project owes most to is{" "}
          <a
            href="https://github.com/MarkEEaton/open-journal-matcher"
            target="_blank"
            rel="noreferrer"
          >
            Mark E. Eaton's Open Journal Matcher
          </a>{" "}
          (CUNY, 2020–2022) — free, open, matching abstracts against DOAJ. He
          took it offline in July 2022 and wrote:
        </p>
        <blockquote>
          "My hope is that someone will pick up where I left off."
          <cite>
            —{" "}
            <a
              href="https://kingsboroughlibtech.commons.gc.cuny.edu/2022/07/29/the-last-days-of-the-open-journal-matcher/"
              target="_blank"
              rel="noreferrer"
            >
              The last days of the Open Journal Matcher
            </a>
            , 2022
          </cite>
        </blockquote>
        <p>
          This is one response to that invitation. Eaton also argued for{" "}
          <a
            href="https://academicworks.cuny.edu/kb_pubs/261"
            target="_blank"
            rel="noreferrer"
          >
            <em>pervious technology</em>
          </a>{" "}
          — tools users can reach into and adapt rather than only consume. OJM
          was pervious at the code layer. This is pervious at the{" "}
          <strong>data</strong> layer, and that shift is the whole inheritance:
          the knowledge is the product, not a service that can be switched off.
          399 Markdown files in a Git repository under a share-alike licence
          cannot be taken away from you when one maintainer burns out — which is
          exactly how OJM ended.
        </p>
        <p>
          That is also why the ask above is co-maintainers rather than users. A
          corpus that outlives its author is the only version of this that
          honours what Eaton was pointing at, and files surviving is necessary
          but not sufficient. Someone has to keep them true.
        </p>
      </section>

      <section className="footer-links">
        <a href={REPO_URL} target="_blank" rel="noreferrer">
          Source and knowledge base
        </a>
        <a href={`${REPO_URL}/issues`} target="_blank" rel="noreferrer">
          Report something wrong
        </a>
        {SUPPORT_URL && (
          <a href={SUPPORT_URL} target="_blank" rel="noreferrer">
            {SUPPORT_LABEL}
          </a>
        )}
      </section>
    </footer>
  );
}

const STAGE_LABELS: Record<StageName, string> = {
  parsing: "Reading your paper",
  screening: "Screening 399 journals",
  synthesis: "Writing your recommendation",
};

function App() {
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

  return (
    <div className="page">
      <header>
        <div className="header-top">
          <h1>Journal Atlas</h1>
          <a className="repo-link" href={REPO_URL} target="_blank" rel="noreferrer">
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
          this reads the same curated, source-cited knowledge base the real
          skill uses.
        </p>
      </header>

      <CoverageNotice />

      <textarea
        value={paperText}
        onChange={(e) => setPaperText(e.target.value)}
        placeholder="e.g. A qualitative study using autoethnography to explore embodied cognition in collaborative design teams. ~9,000 words, no institutional funding for open access, discloses AI-assisted copyediting..."
        rows={6}
        disabled={running}
      />

      <button onClick={() => runRecommendation()} disabled={running || !paperText.trim()}>
        {running ? "Working…" : "Find my journal"}
      </button>

      {(running || stages.parsing !== "pending") && (
        <ol className="stages">
          {(Object.keys(STAGE_LABELS) as StageName[]).map((s) => (
            <li key={s} className={`stage stage-${stages[s]}`}>
              <span className="stage-dot" />
              {STAGE_LABELS[s]}
            </li>
          ))}
        </ol>
      )}

      {error && <div className="error">{error}</div>}

      {parsedPaper && (
        <div className="panel">
          <h3>What I read from your description</h3>
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
          <h3>A couple of questions first</h3>
          <div className="synthesis-text">
            <ReactMarkdown>{clarifyQuestion}</ReactMarkdown>
          </div>
          <textarea
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
          <h3>Top {candidates.length} candidates after screening</h3>
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
          <h3>Recommendation</h3>
          <div className="synthesis-text">
            <ReactMarkdown>{synthesisText}</ReactMarkdown>
          </div>
        </div>
      )}

      {synthesisText && !running && (
        <div className="panel">
          <h3>
            Follow-up {followupsLeft > 0 ? `(${followupsLeft} left)` : "(none left)"}
          </h3>
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
              <textarea
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

      <SiteFooter />
    </div>
  );
}

export default App;
