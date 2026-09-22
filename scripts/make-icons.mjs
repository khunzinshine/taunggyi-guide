import { mkdirSync, writeFileSync } from "node:fs"
import { dirname, join } from "node:path"
import { fileURLToPath } from "node:url"
import { deflateSync } from "node:zlib"

function crc32(buf) {
  let c = ~0
  for (let i = 0; i < buf.length; i++) {
    c ^= buf[i]
    for (let k = 0; k < 8; k++) c = (c >>> 1) ^ (0xedb88320 & -(c & 1))
  }
  return ~c >>> 0
}

function chunk(type, data) {
  const len = Buffer.alloc(4)
  len.writeUInt32BE(data.length)
  const td = Buffer.concat([Buffer.from(type), data])
  const crc = Buffer.alloc(4)
  crc.writeUInt32BE(crc32(td))
  return Buffer.concat([len, td, crc])
}

function createPng(size, paint) {
  const raw = Buffer.alloc((size * 3 + 1) * size)
  for (let y = 0; y < size; y++) {
    const row = y * (size * 3 + 1)
    raw[row] = 0
    for (let x = 0; x < size; x++) {
      const [r, g, b] = paint(x, y, size)
      const i = row + 1 + x * 3
      raw[i] = r
      raw[i + 1] = g
      raw[i + 2] = b
    }
  }
  const ihdr = Buffer.alloc(13)
  ihdr.writeUInt32BE(size, 0)
  ihdr.writeUInt32BE(size, 4)
  ihdr[8] = 8
  ihdr[9] = 2
  return Buffer.concat([
    Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]),
    chunk("IHDR", ihdr),
    chunk("IDAT", deflateSync(raw)),
    chunk("IEND", Buffer.alloc(0)),
  ])
}

function paint(x, y, size) {
  const nx = (x / size) * 2 - 1
  const ny = (y / size) * 2 - 1
  let r = 47
  let g = 92
  let b = 68

  const balloon = (nx * nx) / 0.27 + ((ny + 0.08) * (ny + 0.08)) / 0.4
  if (balloon < 1 && ny < 0.38) {
    r = 214
    g = 140
    b = 62
    if ((nx + 0.14) ** 2 + (ny + 0.02) ** 2 < 0.045) {
      r = 236
      g = 188
      b = 110
    }
  }

  if (Math.abs(nx) < 0.11 && ny > 0.4 && ny < 0.6) {
    r = 92
    g = 58
    b = 36
  }

  return [r, g, b]
}

const root = join(dirname(fileURLToPath(import.meta.url)), "..", "public", "icons")
mkdirSync(root, { recursive: true })

for (const size of [192, 512, 180]) {
  const name = size === 180 ? "apple-touch-icon.png" : `icon-${size}.png`
  writeFileSync(join(root, name), createPng(size, paint))
}

console.log("Wrote PWA icons")
