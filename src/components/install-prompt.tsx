"use client"

import { useEffect, useState } from "react"
import { Download, Share, X } from "lucide-react"

import { Button } from "@/components/ui/button"
import { copy } from "@/data/copy"
import { useLocale } from "@/components/locale-provider"

const DISMISS_KEY = "taunggyi-guide:install-dismissed"

type BeforeInstallPromptEvent = Event & {
  prompt: () => Promise<void>
  userChoice: Promise<{ outcome: "accepted" | "dismissed" }>
}

function isStandalone() {
  return (
    window.matchMedia("(display-mode: standalone)").matches ||
    window.matchMedia("(display-mode: fullscreen)").matches ||
    ("standalone" in window.navigator &&
      (window.navigator as Navigator & { standalone?: boolean }).standalone === true)
  )
}

function isIos() {
  const ua = window.navigator.userAgent
  const iPhone = /iPhone|iPad|iPod/i.test(ua)
  const iPadOs = window.navigator.platform === "MacIntel" && window.navigator.maxTouchPoints > 1
  return iPhone || iPadOs
}

function isAndroid() {
  return /Android/i.test(window.navigator.userAgent)
}

export function InstallPrompt() {
  const { locale } = useLocale()
  const [ready, setReady] = useState(false)
  const [installed, setInstalled] = useState(false)
  const [dismissed, setDismissed] = useState(false)
  const [ios, setIos] = useState(false)
  const [android, setAndroid] = useState(false)
  const [event, setEvent] = useState<BeforeInstallPromptEvent | null>(null)

  useEffect(() => {
    setInstalled(isStandalone())
    setIos(isIos())
    setAndroid(isAndroid())
    setDismissed(window.localStorage.getItem(DISMISS_KEY) === "1")
    setReady(true)

    const onPrompt = (incoming: Event) => {
      incoming.preventDefault()
      setEvent(incoming as BeforeInstallPromptEvent)
    }
    const onInstalled = () => {
      setInstalled(true)
      window.localStorage.removeItem(DISMISS_KEY)
    }

    window.addEventListener("beforeinstallprompt", onPrompt)
    window.addEventListener("appinstalled", onInstalled)
    return () => {
      window.removeEventListener("beforeinstallprompt", onPrompt)
      window.removeEventListener("appinstalled", onInstalled)
    }
  }, [])

  if (!ready || installed || dismissed) return null
  if (!ios && !android && !event) return null

  const hint = ios
    ? copy.install.iosHint[locale]
    : !event
      ? copy.install.androidHint[locale]
      : null

  return (
    <div className="pointer-events-none fixed inset-x-0 bottom-20 z-30 mx-auto w-full max-w-lg px-4">
      <div className="pointer-events-auto flex items-start gap-3 rounded-2xl border border-border bg-card/95 px-3 py-2.5 shadow-lg backdrop-blur-md">
        <div className="min-w-0 flex-1">
          <p className="text-sm leading-snug">{copy.install.body[locale]}</p>
          {hint ? (
            <p className="mt-1 inline-flex items-start gap-1.5 text-xs leading-snug text-muted-foreground">
              {ios ? <Share className="mt-0.5 size-3.5 shrink-0" /> : null}
              {hint}
            </p>
          ) : null}
        </div>
        <div className="flex shrink-0 items-center gap-1">
          {event ? (
            <Button
              size="sm"
              onClick={async () => {
                await event.prompt()
                const choice = await event.userChoice
                if (choice.outcome === "accepted") setInstalled(true)
                setEvent(null)
              }}
            >
              <Download data-icon="inline-start" />
              {copy.install.action[locale]}
            </Button>
          ) : null}
          <Button
            size="sm"
            variant="ghost"
            aria-label={copy.install.dismiss[locale]}
            onClick={() => {
              window.localStorage.setItem(DISMISS_KEY, "1")
              setDismissed(true)
            }}
          >
            <X className="size-4" />
          </Button>
        </div>
      </div>
    </div>
  )
}
