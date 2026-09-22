"use client"

import Link from "next/link"
import { ChevronLeft } from "lucide-react"

import { LanguageSwitch } from "@/components/language-switch"
import { copy } from "@/data/copy"
import { useLocale } from "@/components/locale-provider"
import { cn } from "@/lib/utils"

export function PageHeader({
  title,
  subtitle,
  backHref,
}: {
  title: string
  subtitle?: string
  backHref?: string
}) {
  const { locale } = useLocale()

  return (
    <header className="sticky top-0 z-20 border-b border-border/70 bg-background/90 px-4 pb-3 pt-[max(0.75rem,env(safe-area-inset-top))] backdrop-blur-md">
      <div className="flex items-start gap-2">
        {backHref ? (
          <Link
            href={backHref}
            aria-label={copy.back[locale]}
            className="mt-0.5 inline-flex size-9 items-center justify-center rounded-full text-foreground hover:bg-muted"
          >
            <ChevronLeft className="size-5" />
          </Link>
        ) : null}
        <div className={cn("min-w-0 flex-1", !backHref && "pt-0.5")}>
          <h1 className="font-heading text-2xl leading-tight tracking-tight">
            {title}
          </h1>
          {subtitle ? (
            <p className="mt-0.5 text-sm text-muted-foreground">{subtitle}</p>
          ) : null}
        </div>
        <LanguageSwitch className="mt-0.5 shrink-0" />
      </div>
    </header>
  )
}
