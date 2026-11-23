import { providerLabel, useCoverage, useHealth } from "../api";
import { HumanEvidence } from "../components/HumanEvidence";
import { VersionLine } from "../components/VersionLine";
import { SITE } from "../site";

/**
 * What is AI here, said in one place and next to what no entry yet records.
 *
 * The sibling site that does this best (riftbound /ai) leads with who made it
 * and ends with what it will never do. This page keeps that order but is
 * stricter about one thing: it states only what the build can see. Models and
 * counts come from the API; the one figure that cannot be derived (how many
 * entries a person has vouched for) is recorded by hand on the server and
 * printed with its date. It claims no human review, because none is recorded.
 */
export default function Ai() {
  const coverage = useCoverage().data;
  const health = useHealth().data;
  const provider = providerLabel(health?.provider);

  return (
    <article className="prose">
      <h1>How Journal Atlas is made, and what is AI</h1>
      <p className="lede">
        A large share of this project is written by AI. This page says which
        parts, which models run the demo right now, what no entry yet records,
        and what the project will not claim.
      </p>

      <section>
        <h2>What no entry records yet</h2>
        <p className="callout">
          {coverage
            ? coverage.human_evidence
              ? <HumanEvidence coverage={coverage} />
              : "The API this page is talking to does not report this record yet. Until it does, read it as: no entry records a first-hand report that this site can show you."
            : "Loading the current record from the API."}
        </p>
        <p>
          An entry&apos;s tier says <em>how it was written</em>. It is not a verdict
          that someone who knows the journal has checked it, and nothing on this
          site should be read as one. Where a human has submitted to or reviewed
          for a venue, that is the missing layer, and the way to add it is a
          contribution (see <a href="/about/#contact">About</a>).
        </p>
      </section>

      <section>
        <h2>What was written by what</h2>
        <table className="plain-table">
          <caption className="sr-only">Parts of the project, their basis, and how each is marked</caption>
          <thead>
            <tr>
              <th scope="col">Part</th>
              <th scope="col">Basis</th>
              <th scope="col">How it is marked</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">Site code and layout</th>
              <td>
                Written by Claude models working under the maintainer&apos;s direction.
              </td>
              <td>
                The commit history is public. Commits carry a{" "}
                <code>Co-Authored-By</code> trailer naming the exact model.
              </td>
            </tr>
            <tr>
              <th scope="row">
                AI-researched entries
                {coverage ? ` (${coverage.tiers.ai})` : ""}
              </th>
              <td>
                An AI model researched each journal against public sources
                (publisher policy pages, recent publications, review-time
                aggregators). Where no public source existed the field is blank.
              </td>
              <td>
                A note banner, a per-field <code>signal_quality</code> score from
                0 to 5, and a list of what was checked. No human review is
                recorded.
              </td>
            </tr>
            <tr>
              <th scope="row">
                Tier 2 entries
                {coverage ? ` (${coverage.tiers.tier2})` : ""}
              </th>
              <td>
                Family-level estimates: one claim adapted across a group of similar
                journals. Not per-journal evidence.
              </td>
              <td>A warning banner on the Soft Metadata section.</td>
            </tr>
            <tr>
              <th scope="row">
                Tier 1 entries
                {coverage ? ` (${coverage.tiers.tier1})` : ""}
              </th>
              <td>
                Evidence-backed claims: specific article counts, source URLs and
                dates for the claims made.
              </td>
              <td>No banner. Each claim cites its evidence.</td>
            </tr>
            <tr>
              <th scope="row">Scores</th>
              <td>A script (<code>fit_score.py</code>). No model is involved.</td>
              <td>
                Shown with an evidence-coverage percentage, and with a note when
                candidates are tied.
              </td>
            </tr>
            <tr>
              <th scope="row">The written recommendation</th>
              <td>
                A language model, writing fresh on every request from excerpts of
                the top candidates&apos; entries.
              </td>
              <td>
                It appears under the candidate cards it was written from, so you
                can check it against them.
              </td>
            </tr>
          </tbody>
        </table>
        <p className="footnote">
          Where each tier&apos;s entries came from is documented in the repository,
          in <code>SEED_DATA_QUALITY.md</code>. This page makes no claim about who
          typed an individual Tier 1 or Tier 2 entry beyond what that file says.
        </p>
      </section>

      <section>
        <h2>How a recommendation is produced</h2>
        <ol>
          <li>
            <strong>Reading your description.</strong>{" "}
            {health?.extraction_model ? (
              <>
                Right now a model from {provider} (<code>{health.extraction_model}</code>)
                turns it into structured attributes: topics, method, word count, fee
                budget, and the constraints you did and did not state.
              </>
            ) : (
              <>
                A language model turns it into structured attributes: topics, method,
                word count, fee budget, and the constraints you did and did not state.
              </>
            )}{" "}
            Constraints you did not state are listed back to you instead of being
            guessed.
          </li>
          <li>
            <strong>Screening.</strong> A deterministic script scores every entry on
            six weighted dimensions. It does not look at an entry&apos;s tier badge. It
            looks at how many of the six dimensions have data behind them, leaves an
            unknown dimension out instead of inventing a midpoint, pulls the score
            toward a neutral 50 when little is known, and shows you that coverage
            beside the score.
          </li>
          <li>
            <strong>Writing it up.</strong>{" "}
            {health?.synthesis_model ? (
              <>
                Right now a model from {provider} (<code>{health.synthesis_model}</code>)
                reads the top candidates&apos; entries and writes the recommendation.
              </>
            ) : (
              <>A language model reads the top candidates&apos; entries and writes the recommendation.</>
            )}{" "}
            It is given the project&apos;s consumption contract, which tells it to
            name an entry&apos;s tier when it is not Tier 1, to say &quot;the entry
            doesn&apos;t specify&quot; instead of guessing, and to cite only entries it
            was shown.
          </li>
        </ol>
        <p className="footnote">
          The models can change without a code change; the names above are read
          from the API when you open this page.
        </p>
      </section>

      <section>
        <h2>What the project will not do</h2>
        <ul>
          <li>Present an AI-researched or Tier 2 entry as verified, or let a tier badge stand in for a person having checked it.</li>
          <li>Fill an unknown field with a plausible value. A blank stays blank and is shown as blank.</li>
          <li>Invent acceptance rates, review times or reviewer behaviour that no source gave.</li>
          <li>Hide a dispute. A claim someone has formally contested carries a Disputed marker on whatever tier it sits.</li>
          <li>Pretend the written recommendation is anything but model output. It is the least checkable part, which is why the cards it was written from sit above it.</li>
        </ul>
      </section>

      <section>
        <h2>Studying it</h2>
        <p>
          The knowledge base, the scoring script and the per-tier coverage
          measurements are public under {SITE.license.content} and{" "}
          {SITE.license.code}, so every statement on this page can be checked
          against the repository.
        </p>
        <VersionLine version={coverage?.version} />
      </section>
    </article>
  );
}
