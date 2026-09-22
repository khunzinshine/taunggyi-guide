"use client"

import { useEffect } from "react"

import { writeGuideCache } from "@/lib/client-cache"
import type { GuidePayload } from "@/lib/types"

export function CacheHydrator({ payload }: { payload: GuidePayload }) {
  useEffect(() => {
    writeGuideCache(payload)
  }, [payload])

  return null
}
