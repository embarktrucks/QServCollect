from concurrent.futures import ThreadPoolExecutor
import asyncio
import enet
import random
import struct
import traceback
import time
import functools

from sour.protocol.sauerbraten.collect.server_read_stream_protocol import (
    sauerbraten_stream_spec as server_spec,
)
from sour.protocol.sauerbraten.collect.client_read_stream_protocol import (
    sauerbraten_stream_spec as client_spec,
)

from sour.protocol.cube_data_stream import CubeDataStream

class ConnectionFailedError(Exception): pass
class NoMessageError(Exception): pass

class Client(object):
    def __init__(self):
        self.sock = enet.Host(None, 1, 2)

    @property
    def loop(self):
        return asyncio.get_running_loop()


    def _connect(self, addr, port):
        self.peer = self.sock.connect(enet.Address(bytearray(addr, "utf-8"), port), 3)


    def _poll_event(self):
        return self.sock.service(1000)


    async def poll_event(self):
        """
        Poll for a message coming down the pipe.
        """
        return await self.loop.run_in_executor(None, self._poll_event)


    async def choose_event(self, is_ok):
        """
        Look for an event that matches a predicate. An event is anything
        passed back by the enet library.
        """
        while True:
            event = await self.poll_event()

            if is_ok(event):
                return event


    async def poll_message(self):
        """
        Poll for a message blob.
        """
        event = await self.poll_event()

        assert event.type == enet.EVENT_TYPE_RECEIVE

        cds = CubeDataStream(event.packet.data)
        messages = client_spec.read(cds, {}, {})

        return messages


    async def choose_message(self, type_, attempts=15):
        while attempts > 0:
            messages = await self.poll_message()
            for msg_type, message in messages:
                if msg_type == type_:
                    return message

        raise NoMessageError('Could not find message of type %s' % type_)


    def _send(self, msg_type, **kwargs):
        msg = server_spec.write(msg_type, **kwargs)

        packet = enet.Packet(msg)
        self.peer.send(1, packet)


    async def send(self, msg_type, **kwargs):
        """
        Send a typed message to the server.
        """
        await self.loop.run_in_executor(None, functools.partial(self._send, msg_type, **kwargs))


    async def connect(self, addr, port):
        await self.loop.run_in_executor(None, self._connect, addr, port)

        try:
            await self.choose_event(lambda msg: msg.type == enet.EVENT_TYPE_CONNECT)

            await self.send(
                "N_CONNECT",
                name="bot_algalon_the_observer",
                playermodel=0,
                pwdhash="",
                authdomain="",
                authname="",
            )

            await self.choose_message("N_WELCOME")
        except:
            traceback.print_exc()
            raise ConnectionFailedError('Could not connect to %s:%d' % (addr, port))

    def send_pong(self):
        self.send("N_CLIENTPING", ping=12)

    def old_connect(self, addr="server", port=28785):
        while True:
            event = self.sock.service(1000)

            if event.type == enet.EVENT_TYPE_RECEIVE:
                cds = CubeDataStream(event.packet.data)
                try:
                    messages = client_spec.read(cds, {}, {})
                except Exception as e:
                    traceback.print_exc()
                    continue  # probably N_POS

                for msg_type, message in messages:
                    if msg_type == "N_CLIENTPING":
                        self.send_pong()
                        continue

                    if msg_type == "N_WELCOME":
                        self.open()

                    self.on_message(msg_type, message)
