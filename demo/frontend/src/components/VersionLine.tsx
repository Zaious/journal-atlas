import type { Version } from "../api";
import { useLang } from "../i18n";

/**
 * Which corpus these numbers came off, and where the published one lives.
 *
 * The corpus grows; a paper's numbers do not. Without this line a reader who
 * opens the demo a year after publication and finds different figures has no
 * way to tell "this is a later version" from "that paper was wrong" — and the
 * second reading is the one a paper about evidence can least afford. It is the
 * same discipline every entry already follows: say what the value is, and say
 * when it was taken.
 */
export function VersionLine({ version }: { version?: Version }) {
  const zh = useLang() === "zh-Hant";
  if (!version?.corpus_commit) return null;
  const paper = version.paper;
  return (
    <p className="corpus-version">
      {zh ? "目前提供的語料版本 " : "Serving corpus "}
      <code>{version.corpus_describe || version.corpus_commit}</code>
      {version.corpus_committed ? (zh ? `（${version.corpus_committed}）` : ` (${version.corpus_committed})`) : ""}
      {version.built ? (zh ? `，部署於 ${version.built}` : `, deployed ${version.built}`) : ""}
      {zh ? "。" : "."}
      {paper?.doi && (
        <>
          {" "}
          {zh
            ? `${paper.venue ?? "已發表"} 論文所描述的版本封存於 `
            : `The version described in the ${paper.venue ?? "published"} paper is archived at `}
          <a href={`https://doi.org/${paper.doi}`} target="_blank" rel="noopener noreferrer">
            {paper.doi}
          </a>
          {paper.tag ? (
            <>
              {" "}
              {zh ? "（標籤 " : "(tag "}
              <code>{paper.tag}</code>
              {zh ? "）" : ")"}
            </>
          ) : null}
          {zh ? "。" : "."}
        </>
      )}
    </p>
  );
}
