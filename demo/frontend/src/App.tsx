import { useRef, useState } from "react";
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
  const [candidates, setCandidates] = useState<Candidate[] | null>(null);
  const [expanded, setExpanded] = useState<Set<string>>(new Set());
  const [synthesisText, setSynthesisText] = useState("");
  const [error, setError] = useState<string | null>(null);
  const abortRef = useRef<AbortController | null>(null);

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
        if (stage === "parsing") setParsedPaper(data.paper);
        if (stage === "screening") setCandidates(data.candidates);
      }
    } else if (name === "text") {
      setSynthesisText((t) => t + data.delta);
    } else if (name === "error") {
      setError(data.message);
    }
  }

  async function runRecommendation() {
    if (!paperText.trim() || running) return;
    setRunning(true);
    setError(null);
    setParsedPaper(null);
    setCandidates(null);
    setExpanded(new Set());
    setSynthesisText("");
    setStages({ parsing: "active", screening: "pending", synthesis: "pending" });

    const controller = new AbortController();
    abortRef.current = controller;

    try {
      const res = await fetch(`${API_BASE}/api/recommend`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ paper_description: paperText }),
        signal: controller.signal,
      });
      if (!res.ok || !res.body) throw new Error(`Server error (${res.status})`);

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

  return (
    <div className="page">
      <header>
        <h1>Journal Atlas</h1>
        <p className="tagline">
          Paste your abstract or describe your paper. No account, no install —
          this reads the same curated, source-cited knowledge base the real
          skill uses.
        </p>
      </header>

      <textarea
        value={paperText}
        onChange={(e) => setPaperText(e.target.value)}
        placeholder="e.g. A qualitative study using autoethnography to explore embodied cognition in collaborative design teams. ~9,000 words, no institutional funding for open access, discloses AI-assisted copyediting..."
        rows={6}
        disabled={running}
      />

      <button onClick={runRecommendation} disabled={running || !paperText.trim()}>
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
                    <span className="score">{c.score.toFixed(1)}/100</span>
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
    </div>
  );
}

export default App;
