export const onRequestGet: PagesFunction = async (ctx) => {
  const apiKey = ctx.env.CAPACITY_API_KEY; // set in Pages env vars
  const url = "https://api.capacity.com/..."; // your endpoint
  const cache = caches.default;
  const cacheKey = new Request(new URL(ctx.request.url), ctx.request);
  let res = await cache.match(cacheKey);
  if (!res) {
    res = await fetch(url, { headers: { Authorization: `Bearer ${apiKey}` }});
    // optional: basic shape-check; return 502 if bad to avoid breaking pages
    res = new Response(await res.text(), { headers: { "Content-Type": "application/json", "Cache-Control": "max-age=60" }});
    ctx.waitUntil(cache.put(cacheKey, res.clone()));
  }
  return res;
};