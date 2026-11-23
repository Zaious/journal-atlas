import { useEffect, useState } from "react";

export const API_BASE: string = import.meta.env.VITE_API_BASE ?? "http://localhost:8000";

// ---------- types ----------

export interface CoverageField {
  field: string;
  label: string;
  tier1: number;
  tier2: number;
  ai: number;
  total: number;
}

export interface PaperVersion {
  venue?: string;
  title?: string;
  tag?: string | null;
  doi?: string | null;
}

export interface Version {
  corpus_commit?: string;
  corpus_committed?: string;
  corpus_describe?: string;
  built?: string;
  paper?: PaperVersion;
}

/** Recorded by hand and dated on the server: not derivable from the corpus. */
export interface HumanEvidence {
  first_hand_reports: number;
  external_contributors: number;
  recorded: string;
}

export interface Coverage {
  total: number;
  tiers: { tier1: number; tier2: number; ai: number };
  fields: CoverageField[];
  core_fields: string[];
  core_label: string;
  absent: string[];
  absent_checked: string;
  human_evidence?: HumanEvidence;
  version?: Version;
}

export interface Limits {
  global_used_today: number;
  global_daily_limit: number;
  per_client_hourly_limit: number;
  per_client_daily_limit: number;
}

export interface Health {
  status: string;
  provider: string | null;
  extraction_model: string | null;
  synthesis_model: string | null;
  provider_ready: boolean;
  limits: Limits;
  version?: Version;
}

// ---------- fetching ----------

/**
 * One request per endpoint per page load, shared by every component that asks.
 * Components start from `null` rather than from this cache so the first client
 * render equals the prerendered markup and hydration has nothing to reconcile.
 */
const cache = new Map<string, Promise<unknown>>();

function getJson<T>(path: string): Promise<T | null> {
  let hit = cache.get(path) as Promise<T | null> | undefined;
  if (!hit) {
    hit = fetch(`${API_BASE}${path}`)
      .then((r) => (r.ok ? (r.json() as Promise<T>) : null))
      .catch(() => null);
    cache.set(path, hit);
  }
  return hit;
}

function useApi<T>(path: string): { data: T | null; settled: boolean } {
  const [state, setState] = useState<{ data: T | null; settled: boolean }>({
    data: null,
    settled: false,
  });
  useEffect(() => {
    let live = true;
    getJson<T>(path).then((data) => live && setState({ data, settled: true }));
    return () => {
      live = false;
    };
  }, [path]);
  return state;
}

/**
 * The frontend can be deployed before the backend. An older API has no `tiers`
 * block, so add it up from the per-field rows, which every version sends; an
 * absent `human_evidence` stays absent (and renders nothing), because a missing
 * record must not read as "zero".
 */
function withTiers(c: Coverage | null): Coverage | null {
  if (!c || c.tiers) return c;
  const sum = (key: "tier1" | "tier2" | "ai") => c.fields.reduce((n, f) => n + f[key], 0);
  return { ...c, tiers: { tier1: sum("tier1"), tier2: sum("tier2"), ai: sum("ai") } };
}

export function useCoverage(): { data: Coverage | null; settled: boolean } {
  const { data, settled } = useApi<Coverage>("/api/coverage");
  return { data: withTiers(data), settled };
}
export const useHealth = () => useApi<Health>("/api/health");

// ---------- derived figures ----------

/** Share of the corpus in the fields it grew out of, as a whole percent. */
export function corePercent(c: Coverage): number {
  const core = c.fields
    .filter((f) => c.core_fields.includes(f.field))
    .reduce((n, f) => n + f.total, 0);
  return Math.round((core / c.total) * 100);
}

/** Display form of the provider id the API reports ("x" becomes "X"). */
export function providerLabel(provider: string | null | undefined): string | null {
  if (!provider) return null;
  return provider.charAt(0).toUpperCase() + provider.slice(1);
}

/** True when every entry in a field is AI-researched. */
export function fieldIsAllAi(c: Coverage, field: string): CoverageField | null {
  const f = c.fields.find((x) => x.field === field);
  return f && f.total > 0 && f.ai === f.total ? f : null;
}
