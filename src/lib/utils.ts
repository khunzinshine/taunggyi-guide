import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function telHref(phone: string) {
  return `tel:${phone.replace(/[^\d+]/g, "")}`
}

export function formatDay(date: string, locale: "en" | "my" = "en") {
  return formatDateRange(date, date, locale)
}

export function formatDateRange(start: string, end: string, locale: "en" | "my" = "en") {
  const from = new Date(start)
  const to = new Date(end)
  const myMonths = [
    "ဇန်နဝါရီ",
    "ဖေဖေါ်ဝါရီ",
    "မတ်",
    "ဧပြီ",
    "မေ",
    "ဇွန်",
    "ဇူလိုင်",
    "ဩဂုတ်",
    "စက်တင်ဘာ",
    "အောက်တိုဘာ",
    "နိုဝင်ဘာ",
    "ဒီဇင်ဘာ",
  ]

  if (locale === "my") {
    if (start === end) {
      return `${from.getDate()} ${myMonths[from.getMonth()]} ${from.getFullYear()}`
    }
    if (from.getMonth() === to.getMonth() && from.getFullYear() === to.getFullYear()) {
      return `${from.getDate()}-${to.getDate()} ${myMonths[to.getMonth()]} ${to.getFullYear()}`
    }
    return `${from.getDate()} ${myMonths[from.getMonth()]} - ${to.getDate()} ${myMonths[to.getMonth()]} ${to.getFullYear()}`
  }

  const day = new Intl.DateTimeFormat("en-GB", { day: "numeric" })
  const monthYear = new Intl.DateTimeFormat("en-GB", {
    month: "short",
    year: "numeric",
  })

  if (start === end) {
    return new Intl.DateTimeFormat("en-GB", {
      day: "numeric",
      month: "short",
      year: "numeric",
    }).format(from)
  }

  const sameMonth =
    from.getMonth() === to.getMonth() && from.getFullYear() === to.getFullYear()

  if (sameMonth) {
    return `${day.format(from)}-${day.format(to)} ${monthYear.format(to)}`
  }

  const short = new Intl.DateTimeFormat("en-GB", {
    day: "numeric",
    month: "short",
  })
  return `${short.format(from)} - ${short.format(to)} ${to.getFullYear()}`
}
