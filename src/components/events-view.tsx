"use client"

import { CacheHydrator } from "@/components/cache-hydrator"
import { EventsExplorer } from "@/components/events-explorer"
import { PageHeader } from "@/components/page-header"
import { copy } from "@/data/copy"
import { useLocale } from "@/components/locale-provider"
import { getGuidePayload } from "@/lib/guide"

export function EventsView() {
  const { locale } = useLocale()
  const guide = getGuidePayload()

  return (
    <>
      <CacheHydrator payload={guide} />
      <PageHeader
        title={copy.events.title[locale]}
        subtitle={copy.events.subtitle[locale]}
      />
      <EventsExplorer events={guide.events} />
    </>
  )
}
