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

function coord(value: number) {
  return Number(value.toFixed(2))
}

function FireworkBurst({
  cx,
  cy,
  size,
  color,
  accent,
  rays,
  className,
}: {
  cx: number
  cy: number
  size: number
  color: string
  accent: string
  rays: number
  className: string
}) {
  const spokes = Array.from({ length: rays }, (_, index) => {
    const angle = (index / rays) * Math.PI * 2
    const length = size * (0.62 + (index % 4) * 0.12)
    const inner = size * 0.16
    return {
      x1: coord(cx + Math.cos(angle) * inner),
      y1: coord(cy + Math.sin(angle) * inner),
      x2: coord(cx + Math.cos(angle) * length),
      y2: coord(cy + Math.sin(angle) * length),
      tx: coord(cx + Math.cos(angle) * (length + size * 0.16)),
      ty: coord(cy + Math.sin(angle) * (length + size * 0.16)),
    }
  })
  const mid = Array.from({ length: rays }, (_, index) => {
    const angle = ((index + 0.5) / rays) * Math.PI * 2
    const length = size * 0.52
    return {
      x1: coord(cx + Math.cos(angle) * size * 0.2),
      y1: coord(cy + Math.sin(angle) * size * 0.2),
      x2: coord(cx + Math.cos(angle) * length),
      y2: coord(cy + Math.sin(angle) * length),
    }
  })

  return (
    <g className={className}>
      <circle cx={cx} cy={cy} r={size * 1.05} fill={color} fillOpacity="0.12" />
      <circle cx={cx} cy={cy} r={size * 0.38} fill={accent} fillOpacity="0.22" />
      {spokes.map((spoke, index) => (
        <g key={`ray-${index}`}>
          <line
            x1={spoke.x1}
            y1={spoke.y1}
            x2={spoke.x2}
            y2={spoke.y2}
            stroke={color}
            strokeWidth={coord(Math.max(0.7, size * 0.055))}
            strokeLinecap="round"
            strokeOpacity="0.92"
          />
          <circle cx={spoke.tx} cy={spoke.ty} r={coord(Math.max(0.7, size * 0.045))} fill={accent} />
        </g>
      ))}
      {mid.map((spoke, index) => (
        <line
          key={`mid-${index}`}
          x1={spoke.x1}
          y1={spoke.y1}
          x2={spoke.x2}
          y2={spoke.y2}
          stroke={accent}
          strokeWidth={coord(Math.max(0.45, size * 0.03))}
          strokeLinecap="round"
          strokeOpacity="0.7"
        />
      ))}
      <circle cx={cx} cy={cy} r={coord(Math.max(1.4, size * 0.1))} fill={accent} />
    </g>
  )
}

function SkyBalloon({
  x,
  y,
  scale,
  tilt = 0,
  body,
  stripe,
  className,
}: {
  x: number
  y: number
  scale: number
  tilt?: number
  body: string
  stripe?: string
  className?: string
}) {
  return (
    <g className={className}>
      <g transform={`translate(${x} ${y}) scale(${scale}) rotate(${tilt})`}>
        <ellipse cx="0" cy="-2" rx="18" ry="22" fill={body} fillOpacity="0.18" />
        <path
          d="M0-28C-16-28-20-8-17 8C-15 18-8 22-4.2 24.5L-3 27.2H3L4.2 24.5C8 22 15 18 17 8C20-8 16-28 0-28Z"
          fill={body}
        />
        <path
          d="M-10-24C-12-10-11 6-8 16"
          fill="none"
          stroke="oklch(0.2 0.03 70 / 0.12)"
          strokeWidth="1.1"
        />
        <path
          d="M10-24C12-10 11 6 8 16"
          fill="none"
          stroke="oklch(0.2 0.03 70 / 0.12)"
          strokeWidth="1.1"
        />
        {stripe ? (
          <path
            d="M0-28C5-19 7-6 7 7C7 16 3.2 22 0 27.2C-3.2 22-7 16-7 7C-7-6-5-19 0-28Z"
            fill={stripe}
          />
        ) : null}
        <path
          d="M-8.6-12C-6.6-21-2.2-25 3-23.6"
          stroke="white"
          strokeOpacity="0.42"
          strokeWidth="2.1"
          strokeLinecap="round"
        />
        <path d="M-3.6 27.2-2.4 30.2H2.4L3.6 27.2Z" fill={body} />
        <path
          d="M-3.2 30.2-5.4 38M3.2 30.2 5.4 38M0 30.2V38"
          stroke="oklch(0.8 0.07 85)"
          strokeWidth="0.75"
          strokeLinecap="round"
        />
        <path d="M-6 38H6L4.8 44H-4.8Z" fill="oklch(0.22 0.03 70)" />
        <path d="M-5.4 40.4H5.4" stroke="oklch(0.5 0.06 75)" strokeWidth="0.6" />
      </g>
    </g>
  )
}

export function FestivalHeroArt() {
  return (
    <svg
      viewBox="0 0 440 200"
      preserveAspectRatio="xMidYMid slice"
      className="h-full w-full"
      aria-hidden="true"
      fill="none"
    >
      <style>{`
        .fw-a, .fw-b, .fw-c { transform-box: fill-box; transform-origin: center; }
        .fw-a { animation: fw-bloom 3.2s ease-in-out infinite; }
        .fw-b { animation: fw-bloom 3.8s ease-in-out infinite 0.9s; }
        .fw-c { animation: fw-bloom 3.4s ease-in-out infinite 1.6s; }
        .fw-spark { animation: fw-twinkle 1.8s ease-in-out infinite; }
        .b-a { animation: b-float 5.6s ease-in-out infinite; }
        .b-b { animation: b-float 6.4s ease-in-out infinite 0.8s; }
        .b-c { animation: b-float 5.2s ease-in-out infinite 1.4s; }
        .b-d { animation: b-float 7s ease-in-out infinite 0.4s; }
        @keyframes fw-bloom {
          0%, 100% { opacity: 0.42; transform: scale(0.88); }
          46%, 58% { opacity: 1; transform: scale(1); }
        }
        @keyframes fw-twinkle {
          0%, 100% { opacity: 0.18; }
          50% { opacity: 0.95; }
        }
        @keyframes b-float {
          0%, 100% { transform: translateY(0); }
          50% { transform: translateY(-3px); }
        }
        @media (prefers-reduced-motion: reduce) {
          .fw-a, .fw-b, .fw-c, .fw-spark, .b-a, .b-b, .b-c, .b-d {
            animation: none;
            opacity: 0.9;
            transform: none;
          }
        }
      `}</style>
      <defs>
        <radialGradient id="hero-moon" cx="38%" cy="34%" r="65%">
          <stop offset="0%" stopColor="oklch(0.96 0.04 95)" />
          <stop offset="70%" stopColor="oklch(0.84 0.12 85)" />
          <stop offset="100%" stopColor="oklch(0.72 0.1 80)" />
        </radialGradient>
      </defs>
      <FireworkBurst
        className="fw-a"
        cx={46}
        cy={38}
        size={26}
        rays={12}
        color="oklch(0.86 0.12 85)"
        accent="oklch(0.96 0.04 95)"
      />
      <FireworkBurst
        className="fw-b"
        cx={214}
        cy={28}
        size={16}
        rays={10}
        color="oklch(0.9 0.08 92)"
        accent="oklch(0.97 0.03 95)"
      />
      <FireworkBurst
        className="fw-c"
        cx={400}
        cy={42}
        size={20}
        rays={12}
        color="oklch(0.78 0.13 60)"
        accent="oklch(0.93 0.07 80)"
      />
      <g className="fw-spark" fill="oklch(0.93 0.08 90)">
        <circle cx="80" cy="22" r="1.1" />
        <circle cx="122" cy="48" r="0.8" />
        <circle cx="176" cy="16" r="1" />
        <circle cx="258" cy="36" r="0.7" />
        <circle cx="348" cy="20" r="0.9" />
        <circle cx="426" cy="24" r="0.8" />
      </g>
      <circle cx="328" cy="34" r="18" fill="oklch(0.82 0.12 85 / 0.16)" />
      <circle cx="328" cy="34" r="11" fill="url(#hero-moon)" />
      <SkyBalloon
        className="b-a"
        x={98}
        y={86}
        scale={0.92}
        tilt={-4}
        body="oklch(0.8 0.12 78)"
      />
      <SkyBalloon
        className="b-b"
        x={200}
        y={72}
        scale={1.16}
        tilt={2}
        body="oklch(0.9 0.07 90)"
        stripe="oklch(0.72 0.14 72)"
      />
      <SkyBalloon
        className="b-c"
        x={288}
        y={96}
        scale={0.78}
        tilt={5}
        body="oklch(0.74 0.12 68)"
      />
      <SkyBalloon
        className="b-d"
        x={366}
        y={108}
        scale={0.54}
        tilt={-3}
        body="oklch(0.84 0.1 88)"
        stripe="oklch(0.68 0.12 70)"
      />
      <path
        d="M-12 158C28 128 72 124 116 148C154 120 200 116 246 144C284 122 328 126 372 150C402 134 430 140 456 156V204H-12Z"
        fill="oklch(0.18 0.02 80 / 0.9)"
      />
      <path
        d="M-12 176C42 160 96 156 154 172C204 154 258 156 314 174C360 162 408 166 456 180V204H-12Z"
        fill="oklch(0.1 0.01 80)"
      />
      <g fill="oklch(0.84 0.11 85 / 0.8)">
        <circle cx="36" cy="162" r="2.2" />
        <circle cx="54" cy="172" r="1.5" />
        <circle cx="398" cy="164" r="1.8" />
        <circle cx="416" cy="176" r="1.3" />
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
