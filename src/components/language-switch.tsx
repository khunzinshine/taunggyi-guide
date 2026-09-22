"use client"

import { copy } from "@/data/copy"
import { useLocale } from "@/components/locale-provider"
import { cn } from "@/lib/utils"

export function LanguageSwitch({ className }: { className?: string }) {
  const { locale, setLocale } = useLocale()

  return (
    <div
      role="group"
      aria-label={copy.language[locale]}
      className={cn(
        "inline-flex rounded-full bg-black/10 p-0.5 text-[11px] font-semibold tracking-wide",
        className
      )}
    >
      <button
        type="button"
        onClick={() => setLocale("en")}
        className={cn(
          "h-7 min-w-8 rounded-full px-2.5",
          locale === "en" ? "bg-primary text-primary-foreground" : "text-current"
        )}
      >
        EN
      </button>
      <button
        type="button"
        onClick={() => setLocale("my")}
        className={cn(
          "h-7 min-w-8 rounded-full px-2.5",
          locale === "my" ? "bg-primary text-primary-foreground" : "text-current"
        )}
      >
        မြန်မာ
      </button>
    </div>
  )
}
