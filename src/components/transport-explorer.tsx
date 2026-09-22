"use client"

import { useMemo, useState } from "react"
import { Search } from "lucide-react"

import { ContactList } from "@/components/contact-card"
import { Input } from "@/components/ui/input"
import { copy } from "@/data/copy"
import { useLocale } from "@/components/locale-provider"
import type { Transport } from "@/lib/types"

export function TransportExplorer({ items }: { items: Transport[] }) {
  const { locale } = useLocale()
  const [query, setQuery] = useState("")

  const visible = useMemo(() => {
    const q = query.trim().toLowerCase()
    if (!q) return items
    return items.filter((item) => {
      const haystack = [
        item.name.en,
        item.name.my,
        item.address.en,
        item.address.my,
        item.phone,
      ]
        .join(" ")
        .toLowerCase()
      return haystack.includes(q) || item.name.my.includes(query.trim())
    })
  }, [items, query])

  return (
    <div className="space-y-4 px-4 py-4">
      <div className="relative">
        <Search className="pointer-events-none absolute top-1/2 left-3 size-4 -translate-y-1/2 text-muted-foreground" />
        <Input
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          placeholder={copy.transport.search[locale]}
          className="h-11 rounded-xl bg-card pl-9 text-base"
        />
      </div>
      {visible.length === 0 ? (
        <p className="rounded-2xl bg-card px-4 py-8 text-center text-sm text-muted-foreground ring-1 ring-foreground/8">
          {copy.transport.empty[locale]}
        </p>
      ) : (
        <ContactList
          items={visible.map((item) => ({
            key: item.slug,
            name: item.name[locale],
            address: item.address[locale],
            phone: item.phone,
          }))}
        />
      )}
    </div>
  )
}
