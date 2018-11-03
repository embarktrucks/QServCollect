from sour.client.client import Client
import asyncio

async def main():
    c = Client(address="server", name="Paulbot")

    await c.connect()

    while True:
        print(await c.grab_message())

asyncio.run(main())
