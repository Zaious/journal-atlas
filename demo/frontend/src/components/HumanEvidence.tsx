import type { Coverage } from "../api";

/**
 * How many entries anyone has stood behind, said with the date it was
 * recorded. The figure comes from /api/coverage (`human_evidence`), where it is
 * written by hand because it cannot be derived from the files: a tier says how
 * an entry was written, not that someone who knows the venue has vouched for
 * it. Rendering nothing when the server does not report it is deliberate: an
 * absent record must not read as "zero".
 */
export function HumanEvidence({ coverage }: { coverage: Coverage | null }) {
  const h = coverage?.human_evidence;
  if (!coverage || !h) return null;
  const n = h.first_hand_reports;
  const reports =
    n === 0
      ? `none of the ${coverage.total} entries records`
      : `${n} of the ${coverage.total} entries ${n === 1 ? "records" : "record"}`;
  const people =
    h.external_contributors === 0
      ? "and no one outside the project has contributed yet"
      : `and ${h.external_contributors} ${h.external_contributors === 1 ? "person" : "people"} outside the project ${h.external_contributors === 1 ? "has" : "have"} contributed`;
  return (
    <>
      As of {h.recorded}, {reports} a first-hand report from someone who submitted
      to, or reviewed for, that venue, {people}.
    </>
  );
}
