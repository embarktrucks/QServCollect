from sour.client.client import Client
import asyncio

async def main():
    c = Client(address="server", name="Paulbot")

    await c.connect()

    await c.list_demos()
    await c.get_demo(0, 'blah')

asyncio.run(main())
