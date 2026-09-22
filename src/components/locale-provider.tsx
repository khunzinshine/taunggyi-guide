"use client"

import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from "react"

import {
  defaultLocale,
  isLocale,
  LOCALE_KEY,
  type Locale,
} from "@/lib/i18n"

type LocaleContextValue = {
  locale: Locale
  setLocale: (locale: Locale) => void
}

const LocaleContext = createContext<LocaleContextValue | null>(null)

export function LocaleProvider({ children }: { children: ReactNode }) {
  const [locale, setLocaleState] = useState<Locale>(defaultLocale)

  useEffect(() => {
    const stored = window.localStorage.getItem(LOCALE_KEY)
    if (isLocale(stored)) setLocaleState(stored)
  }, [])

  useEffect(() => {
    document.documentElement.lang = locale
    document.documentElement.dataset.locale = locale
  }, [locale])

  const setLocale = useCallback((next: Locale) => {
    setLocaleState(next)
    window.localStorage.setItem(LOCALE_KEY, next)
  }, [])

  const value = useMemo(() => ({ locale, setLocale }), [locale, setLocale])

  return <LocaleContext.Provider value={value}>{children}</LocaleContext.Provider>
}

export function useLocale() {
  const context = useContext(LocaleContext)
  if (!context) {
    throw new Error("useLocale must be used within LocaleProvider")
  }
  return context
}
