"use client"

import { useEffect, useState } from "react"
import { Download } from "lucide-react"

import { Button } from "@/components/ui/button"
import { copy } from "@/data/copy"
import { useLocale } from "@/components/locale-provider"

type BeforeInstallPromptEvent = Event & {
  prompt: () => Promise<void>
  userChoice: Promise<{ outcome: "accepted" | "dismissed" }>
}

export function InstallPrompt() {
  const [event, setEvent] = useState<BeforeInstallPromptEvent | null>(null)
  const { locale } = useLocale()

  useEffect(() => {
    const onPrompt = (e: Event) => {
      e.preventDefault()
      setEvent(e as BeforeInstallPromptEvent)
    }
    window.addEventListener("beforeinstallprompt", onPrompt)
    return () => window.removeEventListener("beforeinstallprompt", onPrompt)
  }, [])

  if (!event) return null

  return (
    <div className="pointer-events-none fixed inset-x-0 bottom-20 z-30 mx-auto w-full max-w-lg px-4">
      <div className="pointer-events-auto flex items-center justify-between gap-3 rounded-2xl border border-border bg-card/95 px-3 py-2 shadow-lg backdrop-blur-md">
        <p className="text-sm leading-snug">{copy.install.body[locale]}</p>
        <Button
          size="sm"
          onClick={async () => {
            await event.prompt()
            await event.userChoice
            setEvent(null)
          }}
        >
          <Download data-icon="inline-start" />
          {copy.install.action[locale]}
        </Button>
      </div>
    </div>
  )
}
