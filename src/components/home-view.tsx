"use client"

import Link from "next/link"
import { ArrowRight, Bus, CalendarDays, Hotel } from "lucide-react"

import { CacheHydrator } from "@/components/cache-hydrator"
import { BalloonMark, FestivalHeroArt } from "@/components/art"
import { ContactList } from "@/components/contact-card"
import { EventCard } from "@/components/event-card"
import { LanguageSwitch } from "@/components/language-switch"
import { Badge } from "@/components/ui/badge"
import { city } from "@/data/city"
import { copy } from "@/data/copy"
import { useLocale } from "@/components/locale-provider"
import { getGuidePayload } from "@/lib/guide"
import { formatDateRange } from "@/lib/utils"

export function HomeView() {
  const { locale } = useLocale()
  const guide = getGuidePayload()
  const featuredEvent = guide.events[0]
  const featuredHotels = guide.hotels.slice(0, 2)
  const shortcuts = [
    {
      href: "/hotels",
      label: copy.shortcuts.hotels[locale],
      hint: copy.shortcuts.hotelsHint[locale],
      icon: Hotel,
    },
    {
      href: "/transport",
      label: copy.shortcuts.ride[locale],
      hint: copy.shortcuts.rideHint[locale],
      icon: Bus,
    },
    {
      href: "/events",
      label: copy.shortcuts.events[locale],
      hint: copy.shortcuts.eventsHint[locale],
      icon: CalendarDays,
    },
  ]
  const facts = [
    { label: copy.facts.elevation[locale], value: copy.facts.elevationValue[locale] },
    { label: copy.facts.airport[locale], value: copy.facts.airportValue[locale] },
    { label: copy.facts.festival[locale], value: copy.facts.festivalValue[locale] },
    { label: copy.facts.language[locale], value: copy.facts.languageValue[locale] },
  ]

  return (
    <>
      <CacheHydrator payload={guide} />
      <section className="hero-sky relative overflow-hidden px-4 pb-8 pt-[max(1.25rem,env(safe-area-inset-top))] text-primary">
        <div className="flex items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <BalloonMark className="size-6 text-primary" />
            <p className="text-sm font-medium tracking-wide">{copy.appName[locale]}</p>
          </div>
          <div className="flex items-center gap-2">
            <Badge className="bg-primary/15 text-primary">{copy.state[locale]}</Badge>
            <LanguageSwitch className="bg-white/10 text-primary" />
          </div>
        </div>
        <h1 className="mt-6 max-w-[16ch] font-heading text-[2.15rem] leading-[1.12] tracking-tight text-primary">
          {city.tagline[locale]}
        </h1>
        <p className="mt-3 max-w-[36ch] text-sm leading-relaxed text-primary/80">
          {copy.intro[locale]}
        </p>
        <div className="mt-5 h-36">
          <FestivalHeroArt />
        </div>
      </section>

      <div className="space-y-6 px-4 py-5">
        <Link
          href="/events"
          className="block rounded-2xl bg-card p-4 ring-1 ring-foreground/8"
        >
          <p className="text-xs font-medium tracking-wide text-muted-foreground uppercase">
            {copy.festivalWeek[locale]}
          </p>
          <h2 className="mt-1 font-heading text-xl leading-tight">
            {city.festivalName[locale]}
          </h2>
          <p className="mt-1 text-sm text-muted-foreground">
            {formatDateRange(city.festivalStart, city.festivalEnd, locale)}
          </p>
          <p className="mt-3 inline-flex items-center gap-1 text-sm font-medium text-primary">
            {copy.openEvent[locale]}
            <ArrowRight className="size-4" />
          </p>
        </Link>

        <div className="grid grid-cols-3 gap-2">
          {shortcuts.map((item) => {
            const Icon = item.icon
            return (
              <Link
                key={item.href}
                href={item.href}
                className="rounded-2xl bg-card px-3 py-3 ring-1 ring-foreground/8"
              >
                <Icon className="size-5 text-primary" />
                <p className="mt-3 text-sm font-medium">{item.label}</p>
                <p className="text-[11px] text-muted-foreground">{item.hint}</p>
              </Link>
            )
          })}
        </div>

        <section>
          <div className="mb-3 flex items-end justify-between gap-3">
            <h2 className="font-heading text-xl">{copy.thisWeek[locale]}</h2>
            <Link href="/events" className="text-sm text-primary">
              {copy.allEvents[locale]}
            </Link>
          </div>
          <EventCard event={featuredEvent} />
        </section>

        <section>
          <div className="mb-3 flex items-end justify-between gap-3">
            <h2 className="font-heading text-xl">{copy.stayNearby[locale]}</h2>
            <Link href="/hotels" className="text-sm text-primary">
              {copy.allHotels[locale]}
            </Link>
          </div>
          <ContactList
            items={featuredHotels.map((hotel) => ({
              key: hotel.slug,
              name: hotel.name[locale],
              address: hotel.address[locale],
              phone: hotel.phone,
            }))}
          />
        </section>

        <section className="rounded-2xl bg-card p-4 ring-1 ring-foreground/8">
          <h2 className="font-heading text-xl">{copy.citySnapshot[locale]}</h2>
          <p className="mt-2 text-sm leading-relaxed text-muted-foreground">
            {city.about[locale]}
          </p>
          <dl className="mt-4 grid grid-cols-2 gap-3">
            {facts.map((fact) => (
              <div key={fact.label} className="rounded-xl bg-secondary px-3 py-2">
                <dt className="text-[11px] text-muted-foreground">{fact.label}</dt>
                <dd className="text-sm font-medium">{fact.value}</dd>
              </div>
            ))}
          </dl>
        </section>
      </div>
    </>
  )
}
