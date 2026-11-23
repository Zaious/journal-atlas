import { useCoverage } from "../api";
import { ISSUES_URL, SITE } from "../site";

/**
 * Who is behind this, why it exists, and where to say it is wrong.
 *
 * First person and named on purpose: a tool that tells researchers where to
 * send months of work should say who built it. The other half of "who built
 * it" — what the AI did — is on /ai/, and nothing about it is repeated here.
 */
export default function About() {
  const coverage = useCoverage().data;

  return (
    <article className="prose">
      <h1>About Journal Atlas</h1>
      <p className="lede">
        Journal Atlas is an open knowledge base about where academic papers fit,
        and a demo that searches it. The knowledge base is the product; this site
        is a window onto it.
      </p>

      <section>
        <h2>What it is, and what it is not</h2>
        <p>
          Each journal or conference is one Markdown file in a Git repository.
          An entry holds the facts you can look up (publisher, fees, review
          model, policies) and the soft metadata you usually cannot: what the
          reviewer pool expects, how the venue frames its scope, which topics it
          tolerates. Every entry says how it was written and how much of it is
          evidenced, and nothing is filled in where nothing is known.
        </p>
        <p>
          It is not a ranking, not an impact-factor lookup, and not a promise
          that a journal will accept your paper. It will say &quot;I have no data on
          this field&quot; before it names a plausible-looking journal it knows little
          about.
        </p>
      </section>

      <section id="who">
        <h2>Who made this, and why</h2>
        <p>
          I&apos;m{" "}
          <a href={SITE.author.url} target="_blank" rel="noreferrer">
            {SITE.author.name} ({SITE.author.handle})
          </a>{" "}
          — an independent HCI researcher and AI agent architect, working
          outside an institution. This started as my own problem. I had
          manuscripts to place, the qualitative and theoretical kind that get
          judged by standards written for other work, and the question
          &quot;where does this actually belong?&quot; had no good answer anywhere. Ask a
          model and it names the most famous journals in the area. Ask a colleague
          who has published there and you get something worth ten times as much —
          but only if you happen to know that colleague.
        </p>
        <p>
          So I started writing down what that colleague would have said. The
          project is what happened when I kept going, and then made the
          machine-readable version an AI agent could read without inventing the
          parts nobody had written down yet.
        </p>
        <p>
          It is a{" "}
          <a href={SITE.studio.url} target="_blank" rel="noreferrer">
            {SITE.studio.name}
          </a>{" "}
          ({SITE.studio.nameZh}) project. How much of it an AI wrote, and which
          parts, is on <a href="/ai/">its own page</a>.
        </p>
      </section>

      <section>
        <h2>Picking up where Open Journal Matcher left off</h2>
        <p>
          There is a twenty-year line of journal recommenders, and most of them
          are switched off. The one this project owes most to is{" "}
          <a
            href="https://github.com/MarkEEaton/open-journal-matcher"
            target="_blank"
            rel="noreferrer"
          >
            Mark E. Eaton&apos;s Open Journal Matcher
          </a>{" "}
          (CUNY, 2020–2022) — free, open, matching abstracts against DOAJ. He took
          it offline in July 2022 and wrote:
        </p>
        <blockquote>
          &quot;My hope is that someone will pick up where I left off.&quot;
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
          <a href="https://academicworks.cuny.edu/kb_pubs/261" target="_blank" rel="noreferrer">
            <em>pervious technology</em>
          </a>{" "}
          — tools users can reach into and adapt rather than only consume. OJM was
          pervious at the code layer. This is pervious at the <strong>data</strong>{" "}
          layer, and that shift is the whole inheritance: the knowledge is the
          product, not a service that can be switched off.{" "}
          {coverage ? `${coverage.total} Markdown files` : "Markdown files"} in a Git
          repository under a share-alike licence cannot be taken away from you when
          one maintainer burns out — which is exactly how OJM ended.
        </p>
        <p>
          That is also why the ask is co-maintainers rather than users. A corpus
          that outlives its author is the only version of this that honours what
          Eaton was pointing at, and files surviving is necessary but not
          sufficient. Someone has to keep them true.
        </p>
      </section>

      <section id="contact">
        <h2>Contact, corrections, and contributing</h2>
        <p>
          Everything goes through GitHub issues, in public, so a correction helps
          the next reader too.
        </p>
        <ul>
          <li>
            <a href={ISSUES_URL} target="_blank" rel="noreferrer">
              Report a wrong entry or a bug
            </a>{" "}
            — name the journal and the field. A disputed claim is handled by the
            process in the repository&apos;s governance document, not by argument in a
            thread.
          </li>
          <li>
            <a href={SITE.repoUrl} target="_blank" rel="noreferrer">
              Contribute an entry or a whole field
            </a>{" "}
            — see the contributing guide in the repository.
          </li>
          <li>
            <a href={ISSUES_URL} target="_blank" rel="noreferrer">
              Offer to co-maintain
            </a>{" "}
            — the project most needs people who will review entries in their own
            field.
          </li>
        </ul>
        {SITE.contact.email && (
          <p>
            Or write to <a href={`mailto:${SITE.contact.email}`}>{SITE.contact.email}</a>.
          </p>
        )}
        <p>
          If you would like to support the running costs, the{" "}
          {SITE.supportUrl ? (
            <a href={SITE.supportUrl} target="_blank" rel="noreferrer">
              {SITE.supportLabel.toLowerCase()} link
            </a>
          ) : (
            "support link"
          )}{" "}
          exists. It unlocks nothing: every feature is the same for everyone, and
          the demo&apos;s cap is a budget, not a paywall.
        </p>
      </section>

      <section>
        <h2>Licence</h2>
        <p>
          The knowledge base is{" "}
          <a href={SITE.license.contentUrl} target="_blank" rel="noreferrer">
            {SITE.license.content}
          </a>
          ; the code is{" "}
          <a href={SITE.license.codeUrl} target="_blank" rel="noreferrer">
            {SITE.license.code}
          </a>
          . Cite it as the repository&apos;s <code>CITATION.cff</code> says.
        </p>
      </section>
    </article>
  );
}
