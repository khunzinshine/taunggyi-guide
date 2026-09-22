import type { Text } from "@/lib/i18n"

export type Hotel = {
  slug: string
  name: Text
  address: Text
  phone: string
}

export type Transport = {
  slug: string
  name: Text
  address: Text
  phone: string
}

export type BalloonKind = "day" | "fire"

export type Balloon = {
  id: string
  time: string
  kind: BalloonKind
  name: Text
  team: Text
}

export type FestivalDay = {
  slug: string
  date: string
  title: Text
  venue: Text
  balloons: Balloon[]
}

export type GuidePayload = {
  hotels: Hotel[]
  transport: Transport[]
  events: FestivalDay[]
  updatedAt: string
}
