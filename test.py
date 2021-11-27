import asyncio
from aiohttp import ClientSession

async def main():
  async with ClientSession as cs:
    async with cs.get(f"https://api.popcat.xyz/8ball") as r:
      data = await r.json()
      return data['answer']

loop = asyncio.get_event_loop()
loop.run_until_complete(main())