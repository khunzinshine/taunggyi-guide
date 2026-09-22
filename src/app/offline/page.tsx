"use client"

import Link from "next/link"

import { BalloonMark } from "@/components/art"
import { buttonVariants } from "@/components/ui/button"
import { copy } from "@/data/copy"
import { useLocale } from "@/components/locale-provider"
import { cn } from "@/lib/utils"

export default function OfflinePage() {
  const { locale } = useLocale()

  return (
    <div className="flex flex-1 flex-col items-center justify-center px-6 py-16 text-center">
      <BalloonMark className="size-12 text-primary" />
      <h1 className="mt-4 font-heading text-3xl">{copy.offline.title[locale]}</h1>
      <p className="mt-2 max-w-[34ch] text-sm leading-relaxed text-muted-foreground">
        {copy.offline.body[locale]}
      </p>
      <Link href="/" className={cn(buttonVariants({ size: "touch" }), "mt-6")}>
        {copy.backHome[locale]}
      </Link>
    </div>
  )
}
