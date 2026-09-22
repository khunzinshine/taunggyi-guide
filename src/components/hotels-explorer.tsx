"use client"

import { useMemo, useState } from "react"
import { Search } from "lucide-react"

import { ContactList } from "@/components/contact-card"
import { Input } from "@/components/ui/input"
import { copy } from "@/data/copy"
import { useLocale } from "@/components/locale-provider"
import type { Hotel } from "@/lib/types"

export function HotelsExplorer({ hotels }: { hotels: Hotel[] }) {
  const { locale } = useLocale()
  const [query, setQuery] = useState("")

  const visible = useMemo(() => {
    const q = query.trim().toLowerCase()
    if (!q) return hotels
    return hotels.filter((hotel) => {
      const haystack = [
        hotel.name.en,
        hotel.name.my,
        hotel.address.en,
        hotel.address.my,
        hotel.phone,
      ]
        .join(" ")
        .toLowerCase()
      return haystack.includes(q) || hotel.name.my.includes(query.trim())
    })
  }, [hotels, query])

  return (
    <div className="space-y-4 px-4 py-4">
      <div className="relative">
        <Search className="pointer-events-none absolute top-1/2 left-3 size-4 -translate-y-1/2 text-muted-foreground" />
        <Input
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          placeholder={copy.hotels.search[locale]}
          className="h-11 rounded-xl bg-card pl-9 text-base"
        />
      </div>
      {visible.length === 0 ? (
        <p className="rounded-2xl bg-card px-4 py-8 text-center text-sm text-muted-foreground ring-1 ring-foreground/8">
          {copy.hotels.empty[locale]}
        </p>
      ) : (
        <ContactList
          items={visible.map((hotel) => ({
            key: hotel.slug,
            name: hotel.name[locale],
            address: hotel.address[locale],
            phone: hotel.phone,
          }))}
        />
      )}
    </div>
  )
}
