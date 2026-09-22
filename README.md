# Taunggyi Guide

Mobile-first PWA for Taunggyi City: hotels, transport, and Tazaungdaing event notes.

Frontend only. All listings are dummy placeholders so you can drop in your own data later.

## Stack

- Next.js 16 (App Router) + TypeScript
- Tailwind CSS v4 + shadcn/ui (Nova / Base UI)
- Service worker PWA (installable, offline after first visit)
- In-memory server cache on `/api/guide` (swap for Redis later)
- `localStorage` copy of the guide payload for offline reads

## Run

```bash
cd taunggyi-guide
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Offline / install

Service workers are most reliable on a production build:

```bash
npm run build
npm start
```

Then install from the browser (Add to Home Screen). Precached routes: Home, Hotels, Transport, Events, and an offline fallback.

## Replace dummy data

Edit files in `src/data/`:

- `hotels.ts`
- `transport.ts`
- `events.ts`
- `city.ts`

When you add a backend, keep `src/lib/server-cache.ts` as the cache seam and point it at Redis.
