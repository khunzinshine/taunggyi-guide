"use client"

import { CacheHydrator } from "@/components/cache-hydrator"
import { PageHeader } from "@/components/page-header"
import { TransportExplorer } from "@/components/transport-explorer"
import { copy } from "@/data/copy"
import { useLocale } from "@/components/locale-provider"
import { getGuidePayload } from "@/lib/guide"

export function TransportView() {
  const { locale } = useLocale()
  const guide = getGuidePayload()

  return (
    <>
      <CacheHydrator payload={guide} />
      <PageHeader
        title={copy.transport.title[locale]}
        subtitle={copy.transport.subtitle[locale]}
      />
      <TransportExplorer items={guide.transport} />
    </>
  )
}
