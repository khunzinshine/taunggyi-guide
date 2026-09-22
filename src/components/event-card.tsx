"use client"

import { Flame, Sun } from "lucide-react"

import { copy } from "@/data/copy"
import { useLocale } from "@/components/locale-provider"
import { cn, formatDay } from "@/lib/utils"
import type { Balloon, FestivalDay } from "@/lib/types"

function BalloonRow({
  index,
  balloon,
  tone,
}: {
  index: number
  balloon: Balloon
  tone: "day" | "fire"
}) {
  const { locale } = useLocale()

  return (
    <li className="flex items-center gap-3 py-2.5">
      <span className="flex size-8 shrink-0 items-center justify-center rounded-full bg-primary font-heading text-sm text-primary-foreground">
        {index}
      </span>
      <div className="min-w-0 flex-1">
        <p className="font-medium leading-snug">{balloon.name[locale]}</p>
        <p
          className={cn(
            "mt-0.5 text-sm",
            tone === "fire" ? "text-primary/70" : "text-muted-foreground"
          )}
        >
          {balloon.team[locale]}
        </p>
      </div>
    </li>
  )
}

function BalloonGroup({
  icon: Icon,
  label,
  balloons,
  tone,
}: {
  icon: typeof Sun
  label: string
  balloons: Balloon[]
  tone: "day" | "fire"
}) {
  if (balloons.length === 0) return null

  return (
    <section
      className={cn(
        "rounded-xl px-3 py-3",
        tone === "fire" ? "bg-foreground text-primary" : "bg-secondary"
      )}
    >
      <h3
        className={cn(
          "flex items-center justify-between gap-2 text-sm font-medium",
          tone === "fire" ? "text-primary" : "text-foreground"
        )}
      >
        <span className="inline-flex items-center gap-1.5">
          <Icon className="size-4" />
          {label}
        </span>
        <span
          className={cn(
            "tabular-nums",
            tone === "fire" ? "text-primary/80" : "text-muted-foreground"
          )}
        >
          {balloons.length}
        </span>
      </h3>
      <ol className="mt-1 divide-y divide-current/10">
        {balloons.map((balloon, index) => (
          <BalloonRow
            key={balloon.id}
            index={index + 1}
            balloon={balloon}
            tone={tone}
          />
        ))}
      </ol>
    </section>
  )
}

export function EventCard({ event }: { event: FestivalDay }) {
  const { locale } = useLocale()
  const dayBalloons = event.balloons.filter((item) => item.kind === "day")
  const fireBalloons = event.balloons.filter((item) => item.kind === "fire")

  return (
    <article id={event.slug} className="rounded-2xl bg-card p-3 ring-1 ring-foreground/8">
      <header className="px-1 pb-3">
        <p className="text-xs font-medium tracking-wide text-muted-foreground uppercase">
          {formatDay(event.date, locale)}
        </p>
        <h2 className="mt-0.5 font-heading text-xl leading-tight">{event.title[locale]}</h2>
      </header>

      <div className="space-y-2">
        <BalloonGroup
          icon={Sun}
          label={copy.events.dayBalloons[locale]}
          balloons={dayBalloons}
          tone="day"
        />
        <BalloonGroup
          icon={Flame}
          label={copy.events.fireBalloons[locale]}
          balloons={fireBalloons}
          tone="fire"
        />
      </div>
    </article>
  )
}
