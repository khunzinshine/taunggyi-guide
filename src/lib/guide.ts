import { city } from "@/data/city"
import { events } from "@/data/events"
import { hotels } from "@/data/hotels"
import { transport } from "@/data/transport"
import type { GuidePayload } from "@/lib/types"

export function getGuidePayload(): GuidePayload {
  return {
    hotels,
    transport,
    events,
    updatedAt: city.updatedAt,
  }
}
