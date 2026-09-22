"use client"

import { useEffect } from "react"

export function PwaRegister() {
  useEffect(() => {
    if (process.env.NODE_ENV !== "production") return
    if (!("serviceWorker" in navigator)) return

    const register = async () => {
      try {
        await navigator.serviceWorker.register("/sw.js", { scope: "/" })
      } catch {
        // Registration is optional in local development.
      }
    }

    void register()
  }, [])

  return null
}
