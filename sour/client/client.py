from sour.protocol.sauerbraten.collect.server_read_stream_protocol import (
    sauerbraten_stream_spec as server_spec,
)
from sour.protocol.sauerbraten.collect.client_read_stream_protocol import (
    sauerbraten_stream_spec as client_spec,
)

from sour.protocol.cube_data_stream import CubeDataStream

import enet
import random
import struct
import traceback


def to_bytes(string):
    return string.encode("utf-8")


class Client(object):
    def __init__(self):
        self.sock = enet.Host(None, 1, 2)

    def open(self):
        """
        Called when the connection is opened and the server responds with
        N_WELCOME.
        """
        self.send("N_LISTDEMOS")

    def on_close(self):
        """
        Called when the connection is closed.
        """
        pass

    def on_message(self, msg_type, message):
        print(msg_type, message)
        if msg_type == "N_SENDDEMOLIST":
            self.send("N_GETDEMO", demonum=0)

    def send(self, msg_type, **kwargs):
        msg = server_spec.write(msg_type, **kwargs)

        packet = enet.Packet(msg)
        self.peer.send(1, packet)

    def send_pong(self):
        self.send("N_CLIENTPING", ping=12)

    def connect(self, addr="server", port=28785):
        self.peer = self.sock.connect(enet.Address(bytearray(addr, "utf-8"), port), 3)

        while True:
            event = self.sock.service(1000)

            if event.type == enet.EVENT_TYPE_CONNECT:
                print("%s: CONNECT" % event.peer.address)
                self.send(
                    "N_CONNECT",
                    name="bot_algalon_the_observer",
                    playermodel=0,
                    pwdhash="",
                    authdomain="",
                    authname="",
                )

            elif event.type == enet.EVENT_TYPE_DISCONNECT:
                print("%s: DISCONNECT" % event.peer.address)
            elif event.type == enet.EVENT_TYPE_RECEIVE:
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
