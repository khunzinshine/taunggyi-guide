import type { ReactNode } from "react"

import { BottomNav } from "@/components/bottom-nav"
import { InstallPrompt } from "@/components/install-prompt"
import { LocaleProvider } from "@/components/locale-provider"
import { OfflineBanner } from "@/components/offline-banner"

export function AppShell({ children }: { children: ReactNode }) {
  return (
    <LocaleProvider>
      <div className="relative mx-auto flex min-h-dvh w-full max-w-lg flex-col bg-background paper-grain shadow-[0_0_80px_oklch(0.2_0.04_85/0.35)]">
        <OfflineBanner />
        <div className="flex flex-1 flex-col pb-[4.75rem]">{children}</div>
        <BottomNav />
        <InstallPrompt />
      </div>
    </LocaleProvider>
  )
}
