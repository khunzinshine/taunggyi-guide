import type { Metadata } from "next"

import { HotelsView } from "@/components/hotels-view"

export const metadata: Metadata = { title: "Hotels" }

export default function HotelsPage() {
  return <HotelsView />
}
