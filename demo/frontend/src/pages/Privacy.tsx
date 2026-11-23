import { providerLabel, useHealth } from "../api";
import { ISSUES_URL, SITE } from "../site";

/** Bump with any change to what the site or API collects or who receives it. */
const EFFECTIVE = "2026-11-23";

/**
 * What happens to the text a visitor pastes.
 *
 * Written from the code, not from intent: the API has no database
 * (demo/backend/main.py), keeps the visitor's address only in the limiter's
 * memory (demo/backend/ratelimit.py), and the front end sets no cookies and
 * loads nothing from a third party (scripts/check-site.mjs enforces the last
 * two on every build). Where the code cannot answer — what a model provider
 * or a CDN keeps — the page says so rather than guessing, per skill
 * `ccweb-footer`: a privacy text is only as good as its latest vendor change.
 */
export default function Privacy() {
  const health = useHealth().data;
  const provider = providerLabel(health?.provider);
  const limits = health?.limits;

  return (
    <article className="prose">
      <h1>Privacy: what happens to the text you paste</h1>
      <p className="lede">
        Journal Atlas has no accounts. The one thing it handles is the description
        of your paper that you type or paste, and that description leaves this
        site: it is sent to a language-model provider to be read.
      </p>
      <p className="footnote">Effective {EFFECTIVE}. The repository history is the changelog for this page.</p>

      <section>
        <h2>The text you paste</h2>
        <ul>
          <li>
            It is sent from your browser to the demo&apos;s API, and from there to a
            language-model provider
            {provider ? ` (currently ${provider}, as the API reports it)` : ""}.
            The provider reads it to extract your paper&apos;s attributes and, for the
            written recommendation and any follow-up, receives it again together
            with excerpts from the knowledge base.
          </li>
          <li>
            The API has no database and does not write your text anywhere. It
            exists in memory for as long as the request takes.
          </li>
          <li>
            What the provider keeps, and for how long, is set by the provider&apos;s
            own terms, not by this project. Read them before pasting anything you
            would not send to that provider directly.
          </li>
          <li>
            Paste an abstract or a summary, not a manuscript that is under review
            or covered by an agreement, and not data about participants. The demo
            caps the length for cost reasons, and the cap is also a nudge.
          </li>
        </ul>
        <p>
          If you want nothing to leave your own machine, the skill runs inside your
          own AI session with your own key and reads your files directly; see the
          install note on the <a href="/">home page</a>.
        </p>
      </section>

      <section>
        <h2>What the API keeps</h2>
        <ul>
          <li>
            To enforce its limits it counts requests per visitor address
            {limits
              ? ` (${limits.per_client_hourly_limit} an hour and ${limits.per_client_daily_limit} a day each, ${limits.global_daily_limit} a day in total)`
              : ""}
            . The address is held in the process&apos;s memory only and disappears when
            the process restarts. The status page shows totals, never addresses.
          </li>
          <li>
            If a call to the model provider fails, the error is written to the
            server log so the maintainer can fix it. That is the provider&apos;s error
            message, not your text, but every error format a provider can return
            has not been audited.
          </li>
          <li>
            The web servers in front of the site and the API process requests the
            way web servers do, and may record the address, the URL, the time and
            the browser&apos;s user-agent string in their own logs. This project adds
            no analytics on top of them.
          </li>
        </ul>
      </section>

      <section>
        <h2>In your browser</h2>
        <p>
          The site sets no cookies, uses no local or session storage, and loads no
          analytics, advertising or third-party scripts, fonts or images; the build
          fails if that stops being true. Links to GitHub and elsewhere do nothing
          until you click them, and then that site&apos;s own policy applies.
        </p>
      </section>

      <section>
        <h2>Who else is involved</h2>
        <table className="plain-table">
          <caption className="sr-only">Third parties and what they handle</caption>
          <thead>
            <tr>
              <th scope="col">Party</th>
              <th scope="col">What it handles</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">Cloudflare</th>
              <td>Serves the site&apos;s pages, and sees ordinary web requests for them. The text you paste goes to the API host directly; the API&apos;s address is currently not routed through Cloudflare.</td>
            </tr>
            <tr>
              <th scope="row">The API host</th>
              <td>A rented virtual server run by the maintainer. It receives the text you paste and relays it to the provider below.</td>
            </tr>
            {SITE.contact.email && (
              <tr>
                <th scope="row">The project mailbox</th>
                <td>Only if you write to it. The address forwards to the maintainer&apos;s own mailbox, so your address and message are kept there for as long as the maintainer keeps them. The site itself does not collect e-mail addresses.</td>
              </tr>
            )}
            <tr>
              <th scope="row">{provider ?? "The model provider"}</th>
              <td>Receives the text you paste, and the knowledge-base excerpts sent with it, to produce each answer.</td>
            </tr>
          </tbody>
        </table>
        <p className="footnote">
          This table is edited in the same change as any change of provider or
          host. The provider&apos;s name above is read from the API.
        </p>
      </section>

      <section>
        <h2>Questions and requests</h2>
        <p>
          Because nothing identifying you is stored by the project, there is nothing
          to look up or delete on this side. For anything else, open an{" "}
          <a href={ISSUES_URL} target="_blank" rel="noreferrer">
            issue on GitHub
          </a>
          ; do not put private information in it, since issues are public.
          {SITE.contact.email && (
            <>
              {" "}
              For something private, or if you do not use GitHub, write to{" "}
              <a href={`mailto:${SITE.contact.email}`}>{SITE.contact.email}</a>.
            </>
          )}
        </p>
      </section>
    </article>
  );
}
