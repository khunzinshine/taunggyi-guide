"use client"

import Link from "next/link"
import { usePathname } from "next/navigation"
import { Bus, CalendarDays, Home, Hotel } from "lucide-react"

import { copy } from "@/data/copy"
import { useLocale } from "@/components/locale-provider"
import { cn } from "@/lib/utils"

export function BottomNav() {
  const pathname = usePathname()
  const { locale } = useLocale()

  const items = [
    { href: "/", label: copy.nav.home[locale], icon: Home },
    { href: "/hotels", label: copy.nav.stay[locale], icon: Hotel },
    { href: "/transport", label: copy.nav.ride[locale], icon: Bus },
    { href: "/events", label: copy.nav.events[locale], icon: CalendarDays },
  ]

  return (
    <nav
      aria-label={copy.nav.home[locale]}
      className="fixed inset-x-0 bottom-0 z-40 mx-auto w-full max-w-lg border-t border-border/80 bg-card/90 pb-[max(0.5rem,env(safe-area-inset-bottom))] backdrop-blur-md"
    >
      <ul className="grid grid-cols-4">
        {items.map((item) => {
          const active =
            item.href === "/"
              ? pathname === "/"
              : pathname.startsWith(item.href)
          const Icon = item.icon

          return (
            <li key={item.href}>
              <Link
                href={item.href}
                className={cn(
                  "flex min-h-14 flex-col items-center justify-center gap-0.5 text-[11px] font-medium",
                  active ? "text-primary" : "text-muted-foreground"
                )}
              >
                <Icon
                  className={cn("size-5", active && "fill-primary/15")}
                  strokeWidth={active ? 2.4 : 1.8}
                />
                {item.label}
              </Link>
            </li>
          )
        })}
      </ul>
    </nav>
  )
}
