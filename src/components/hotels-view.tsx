"use client"

import { CacheHydrator } from "@/components/cache-hydrator"
import { HotelsExplorer } from "@/components/hotels-explorer"
import { PageHeader } from "@/components/page-header"
import { copy } from "@/data/copy"
import { useLocale } from "@/components/locale-provider"
import { getGuidePayload } from "@/lib/guide"

export function HotelsView() {
  const { locale } = useLocale()
  const guide = getGuidePayload()

  return (
    <>
      <CacheHydrator payload={guide} />
      <PageHeader
        title={copy.hotels.title[locale]}
        subtitle={copy.hotels.subtitle[locale]}
      />
      <HotelsExplorer hotels={guide.hotels} />
    </>
  )
}
