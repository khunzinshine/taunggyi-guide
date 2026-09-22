export function BalloonMark({ className }: { className?: string }) {
  return (
    <svg
      viewBox="0 0 32 32"
      aria-hidden="true"
      className={className}
      fill="none"
    >
      <path
        d="M16 3c-5.2 0-9 3.8-9 8.6 0 4.4 2.8 8 7.2 9.2L13 27h6l-1.2-6.2C22.2 19.6 25 16 25 11.6 25 6.8 21.2 3 16 3Z"
        fill="currentColor"
      />
      <path
        d="M12.5 12.5c.4-2.4 1.8-4 3.5-4.5"
        stroke="white"
        strokeOpacity="0.55"
        strokeWidth="1.4"
        strokeLinecap="round"
      />
    </svg>
  )
}

export function FestivalHeroArt() {
  return (
    <svg
      viewBox="0 0 360 210"
      className="h-full w-full"
      aria-hidden="true"
      fill="none"
    >
      <circle cx="292" cy="38" r="18" fill="oklch(0.82 0.12 85 / 0.9)" />
      <path
        d="M-10 168c38-28 72-28 110 0 32-34 78-40 122-6 30-22 70-24 140 8v50H-10V168Z"
        fill="oklch(0.18 0.02 80 / 0.85)"
      />
      <path
        d="M-10 186c46-18 90-14 128 8 40-24 86-22 132 4 28-14 68-12 120 10v22H-10V186Z"
        fill="oklch(0.1 0.01 80)"
      />
      <g>
        <ellipse cx="78" cy="78" rx="22" ry="28" fill="oklch(0.78 0.13 80)" />
        <path d="M72 106h12l-2 10h-8l-2-10Z" fill="oklch(0.2 0.02 80)" />
        <path
          d="M66 78c2-10 7-16 12-18"
          stroke="white"
          strokeOpacity="0.35"
          strokeWidth="2"
          strokeLinecap="round"
        />
      </g>
      <g>
        <ellipse cx="168" cy="58" rx="28" ry="36" fill="oklch(0.9 0.08 90)" />
        <path
          d="M168 22c8 10 12 22 12 36s-4 26-12 36c-8-10-12-22-12-36s4-26 12-36Z"
          fill="oklch(0.72 0.14 75 / 0.9)"
        />
        <path d="M160 94h16l-3 12h-10l-3-12Z" fill="oklch(0.16 0.02 80)" />
      </g>
      <g>
        <ellipse cx="248" cy="92" rx="16" ry="21" fill="oklch(0.7 0.12 70)" />
        <path d="M243 113h10l-1.5 8h-7L243 113Z" fill="oklch(0.18 0.02 80)" />
      </g>
      <g fill="oklch(0.82 0.12 85 / 0.85)">
        <circle cx="40" cy="118" r="3.2" />
        <circle cx="52" cy="130" r="2.2" />
        <circle cx="300" cy="124" r="2.8" />
        <circle cx="318" cy="136" r="2" />
      </g>
    </svg>
  )
}

const palettes = [
  ["oklch(0.14 0 0)", "oklch(0.72 0.13 85)"],
  ["oklch(0.22 0.03 80)", "oklch(0.8 0.11 90)"],
  ["oklch(0.1 0 0)", "oklch(0.64 0.12 75)"],
  ["oklch(0.28 0.04 70)", "oklch(0.78 0.1 92)"],
  ["oklch(0.16 0.02 85)", "oklch(0.7 0.14 80)"],
]

function paletteFor(seed: string) {
  let hash = 0
  for (const char of seed) hash = (hash + char.charCodeAt(0) * 13) % palettes.length
  return palettes[hash] ?? palettes[0]
}

export function CoverArt({
  seed,
  label,
}: {
  seed: string
  label: string
}) {
  const [from, to] = paletteFor(seed)

  return (
    <div
      className="relative isolate flex aspect-[16/9] items-end overflow-hidden rounded-2xl"
      style={{
        background: `linear-gradient(145deg, ${from} 0%, ${to} 100%)`,
      }}
    >
      <div className="pointer-events-none absolute -right-6 -top-8 size-36 rounded-full bg-white/15" />
      <div className="pointer-events-none absolute -bottom-10 left-10 size-28 rounded-full bg-black/10" />
      <BalloonMark className="absolute right-4 top-4 size-8 text-white/80" />
      <p className="relative z-10 px-4 pb-3 font-heading text-lg text-white">
        {label}
      </p>
    </div>
  )
}
