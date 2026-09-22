"use client"

import { useState } from "react"

import { EventCard } from "@/components/event-card"
import { copy } from "@/data/copy"
import { useLocale } from "@/components/locale-provider"
import { cn } from "@/lib/utils"
import type { FestivalDay } from "@/lib/types"

function dayNumber(date: string) {
  return new Intl.DateTimeFormat("en-GB", {
    day: "numeric",
    timeZone: "Asia/Yangon",
  }).format(new Date(`${date}T12:00:00+06:30`))
}

export function EventsExplorer({ events }: { events: FestivalDay[] }) {
  const { locale } = useLocale()
  const [selected, setSelected] = useState(events[0]?.slug ?? "")
  const current = events.find((event) => event.slug === selected) ?? events[0]

  if (!current) return null

  return (
    <div className="space-y-4 px-4 py-4">
      <div className="-mx-4 flex gap-2 overflow-x-auto px-4 pb-1">
        {events.map((event, index) => {
          const active = event.slug === current.slug
          return (
            <button
              key={event.slug}
              type="button"
              onClick={() => setSelected(event.slug)}
              className={cn(
                "flex min-w-14 shrink-0 flex-col items-center rounded-2xl px-2.5 py-2.5",
                active
                  ? "bg-primary text-primary-foreground"
                  : "bg-card text-foreground ring-1 ring-foreground/8"
              )}
            >
              <span className="font-heading text-2xl leading-none tabular-nums">
                {dayNumber(event.date)}
              </span>
              <span
                className={cn(
                  "mt-1 text-[11px] font-medium",
                  active ? "text-primary-foreground/80" : "text-muted-foreground"
                )}
              >
                {copy.events.dayKind[locale]} {index + 1}
              </span>
            </button>
          )
        })}
      </div>
      <EventCard event={current} />
    </div>
  )
}
