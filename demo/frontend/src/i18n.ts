/**
 * Languages the site is served in, and how a URL maps to one.
 *
 * English lives at the root, as it always has; Traditional Chinese lives under
 * /zh-hant/ with the same page set (docs/status/SITE_SPEC.md, decision 11).
 * There is no client-side language switching and no stored preference: each
 * language is its own set of prerendered HTML files, linked to its counterpart
 * with ordinary links and hreflang, so a URL always means one page in one
 * language and nothing has to be remembered.
 *
 * Adding a language is: an entry here, a page-text entry in locales/meta.ts,
 * the Layout strings, and one component per prose page. scripts/check-site.mjs
 * then refuses a build in which a language has a page the others lack, a page
 * whose links or sections differ from the English one, or no hreflang pair.
 */
import { createContext, useContext } from "react";

export type Lang = "en" | "zh-Hant";

export const LANGS: Lang[] = ["en", "zh-Hant"];

/** The language the unprefixed URLs and `x-default` mean. */
export const DEFAULT_LANG: Lang = "en";

export const LANG_NAME: Record<Lang, string> = {
  en: "English",
  "zh-Hant": "繁體中文",
};

/** Value of <html lang> and hreflang. */
export const LANG_TAG: Record<Lang, string> = {
  en: "en",
  "zh-Hant": "zh-Hant",
};

export const OG_LOCALE: Record<Lang, string> = {
  en: "en_US",
  "zh-Hant": "zh_TW",
};

const PREFIX: Record<Lang, string> = {
  en: "",
  "zh-Hant": "/zh-hant",
};

const PREFIXED = /^\/zh-hant(?=\/|$)/i;

export function langOfPath(pathname: string): Lang {
  return PREFIXED.test(pathname) ? "zh-Hant" : "en";
}

/** The path with its language prefix removed: "/zh-hant/about/" -> "/about/". */
export function stripLang(pathname: string): string {
  return pathname.replace(PREFIXED, "") || "/";
}

/** A language-neutral path ("/about/") in the given language. */
export function localePath(lang: Lang, path: string): string {
  if (lang === DEFAULT_LANG) return path;
  return path === "/" ? `${PREFIX[lang]}/` : `${PREFIX[lang]}${path}`;
}

export const LangContext = createContext<Lang>(DEFAULT_LANG);
export const useLang = () => useContext(LangContext);
