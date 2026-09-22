"use client"

import { WifiOff } from "lucide-react"

import { copy } from "@/data/copy"
import { useLocale } from "@/components/locale-provider"
import { useOnline } from "@/hooks/use-online"

export function OfflineBanner() {
  const online = useOnline()
  const { locale } = useLocale()

  if (online) return null

  return (
    <div className="flex items-center justify-center gap-2 bg-primary px-4 py-2 text-xs font-medium text-primary-foreground">
      <WifiOff className="size-3.5" />
      {copy.offline.banner[locale]}
    </div>
  )
}
