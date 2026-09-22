import type { GuidePayload } from "@/lib/types"

const KEY = "taunggyi-guide:v5"

export function readGuideCache(): GuidePayload | null {
  if (typeof window === "undefined") return null
  try {
    const raw = window.localStorage.getItem(KEY)
    if (!raw) return null
    return JSON.parse(raw) as GuidePayload
  } catch {
    return null
  }
}

export function writeGuideCache(payload: GuidePayload) {
  if (typeof window === "undefined") return
  try {
    window.localStorage.setItem(KEY, JSON.stringify(payload))
  } catch {
    // Ignore quota / private-mode failures; bundled dummy data still works.
  }
}
