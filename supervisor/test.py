from sour.client.client import Client
import asyncio

async def main():
    c = Client(address="server", name="Paulbot")

    await c.connect()

    while True:
        await c.choose_message("N_MAPCHANGE")
        demos = await c.list_demos()
        await c.get_demo(len(demos), 'blah')

asyncio.run(main())
