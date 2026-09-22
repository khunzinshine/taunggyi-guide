"use client"

import { Phone } from "lucide-react"

import { copy } from "@/data/copy"
import { useLocale } from "@/components/locale-provider"
import { telHref } from "@/lib/utils"

export type ContactItem = {
  key: string
  name: string
  address: string
  phones: string[]
}

export function ContactList({ items }: { items: ContactItem[] }) {
  const { locale } = useLocale()

  return (
    <ol className="overflow-hidden rounded-2xl bg-card ring-1 ring-foreground/8">
      {items.map((item, index) => (
        <li
          key={item.key}
          className="flex items-start gap-3 border-t border-foreground/8 px-3 py-3 first:border-t-0"
        >
          <span className="mt-0.5 flex size-8 shrink-0 items-center justify-center rounded-full bg-primary font-heading text-sm text-primary-foreground">
            {index + 1}
          </span>
          <div className="min-w-0 flex-1">
            <p className="font-medium leading-snug">{item.name}</p>
            <p className="mt-0.5 text-sm leading-relaxed text-muted-foreground">
              <span className="sr-only">{copy.contact.address[locale]}: </span>
              {item.address}
            </p>
            <div className="mt-1.5 flex flex-col items-start gap-1">
              {item.phones.map((phone) => (
                <a
                  key={phone}
                  href={telHref(phone)}
                  className="inline-flex items-center gap-1.5 text-sm font-medium text-primary"
                >
                  <Phone className="size-3.5" />
                  <span>
                    <span className="sr-only">{copy.contact.phone[locale]}: </span>
                    {phone}
                  </span>
                </a>
              ))}
            </div>
          </div>
        </li>
      ))}
    </ol>
  )
}
