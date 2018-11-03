from sour.client.client import Client
import asyncio

async def main():
    c = Client()

    await c.connect("server", 28785)

asyncio.run(main())
