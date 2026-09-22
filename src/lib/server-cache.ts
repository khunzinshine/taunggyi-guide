const memory = new Map<string, { value: string; expiresAt: number }>()

/**
 * Small cache-aside helper for guide API routes.
 * Swap the Map for Redis later without changing route handlers:
 *   const redis = new Redis(process.env.REDIS_URL)
 *   await redis.get(key) / redis.set(key, value, "EX", ttlSeconds)
 */
export const serverCache = {
  async get(key: string) {
    const hit = memory.get(key)
    if (!hit) return null
    if (Date.now() > hit.expiresAt) {
      memory.delete(key)
      return null
    }
    return hit.value
  },
  async set(key: string, value: string, ttlSeconds = 60 * 60) {
    memory.set(key, {
      value,
      expiresAt: Date.now() + ttlSeconds * 1000,
    })
  },
}
