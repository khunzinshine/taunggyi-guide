import { getGuidePayload } from "@/lib/guide"
import { serverCache } from "@/lib/server-cache"

export const runtime = "nodejs"

export async function GET() {
  const cacheKey = "guide:payload"
  const cached = await serverCache.get(cacheKey)
  if (cached) {
    return Response.json(JSON.parse(cached), {
      headers: {
        "Cache-Control": "public, max-age=300, s-maxage=3600",
        "X-Guide-Cache": "HIT",
      },
    })
  }

  const payload = getGuidePayload()
  await serverCache.set(cacheKey, JSON.stringify(payload), 60 * 60)

  return Response.json(payload, {
    headers: {
      "Cache-Control": "public, max-age=300, s-maxage=3600",
      "X-Guide-Cache": "MISS",
    },
  })
}
