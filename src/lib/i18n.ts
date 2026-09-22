export const locales = ["en", "my"] as const

export type Locale = (typeof locales)[number]
export type Text = Record<Locale, string>
export type TextList = Record<Locale, string[]>

export const defaultLocale: Locale = "en"
export const LOCALE_KEY = "taunggyi-guide:locale"

export function isLocale(value: string | null): value is Locale {
  return value === "en" || value === "my"
}

export function tx(value: Text, locale: Locale) {
  return value[locale]
}

export function txList(value: TextList, locale: Locale) {
  return value[locale]
}
