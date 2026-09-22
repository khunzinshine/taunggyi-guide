import type { Metadata, Viewport } from "next"

import { AppShell } from "@/components/app-shell"
import { PwaRegister } from "@/components/pwa-register"

import "./globals.css"

const APP_NAME = "Taunggyi Guide"
const APP_TITLE = "Taunggyi Guide"
const APP_DESCRIPTION =
  "Mobile city guide for Taunggyi hotels, transport, and Tazaungdaing events. Works online and offline."

export const metadata: Metadata = {
  applicationName: APP_NAME,
  title: {
    default: APP_TITLE,
    template: "%s · Taunggyi Guide",
  },
  description: APP_DESCRIPTION,
  manifest: "/manifest.webmanifest",
  appleWebApp: {
    capable: true,
    statusBarStyle: "default",
    title: APP_NAME,
  },
  formatDetection: {
    telephone: false,
  },
  icons: {
    icon: [
      { url: "/icons/icon-192.png", sizes: "192x192", type: "image/png" },
      { url: "/icons/icon-512.png", sizes: "512x512", type: "image/png" },
    ],
    apple: [{ url: "/icons/apple-touch-icon.png", sizes: "180x180" }],
  },
}

export const viewport: Viewport = {
  themeColor: "#C5A35A",
  width: "device-width",
  initialScale: 1,
  maximumScale: 1,
  viewportFit: "cover",
}

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="en" className="h-full antialiased">
      <body className="min-h-full">
        <PwaRegister />
        <AppShell>{children}</AppShell>
      </body>
    </html>
  )
}
