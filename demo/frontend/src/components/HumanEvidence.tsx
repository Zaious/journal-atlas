import type { Coverage } from "../api";
import { useLang } from "../i18n";

/**
 * How many entries anyone has stood behind, said with the date it was
 * recorded. The figure comes from /api/coverage (`human_evidence`), where it is
 * written by hand because it cannot be derived from the files: a tier says how
 * an entry was written, not that someone who knows the venue has vouched for
 * it. Rendering nothing when the server does not report it is deliberate: an
 * absent record must not read as "zero".
 *
 * The Chinese says the same thing and no more: "no entry records", "nobody
 * outside the project has contributed". It must never be softened into
 * "verified" or "reviewed" (scripts/check-site.mjs fails the build on that).
 */
export function HumanEvidence({ coverage }: { coverage: Coverage | null }) {
  const lang = useLang();
  const h = coverage?.human_evidence;
  if (!coverage || !h) return null;
  const n = h.first_hand_reports;
  const m = h.external_contributors;

  if (lang === "zh-Hant") {
    const reports =
      n === 0
        ? `${coverage.total} 筆條目中沒有任何一筆記錄`
        : `${coverage.total} 筆條目中有 ${n} 筆記錄了`;
    const people = m === 0 ? "專案以外也還沒有人貢獻" : `並有 ${m} 位專案以外的人貢獻`;
    return (
      <>
        截至 {h.recorded}，{reports}投稿過或審查過該期刊者的第一手報告，{people}。
      </>
    );
  }

  const reports =
    n === 0
      ? `none of the ${coverage.total} entries records`
      : `${n} of the ${coverage.total} entries ${n === 1 ? "records" : "record"}`;
  const people =
    m === 0
      ? "and no one outside the project has contributed yet"
      : `and ${m} ${m === 1 ? "person" : "people"} outside the project ${m === 1 ? "has" : "have"} contributed`;
  return (
    <>
      As of {h.recorded}, {reports} a first-hand report from someone who submitted
      to, or reviewed for, that venue, {people}.
    </>
  );
}
