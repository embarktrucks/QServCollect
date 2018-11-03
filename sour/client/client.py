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
        pass

    def on_close(self):
        """
        Called when the connection is closed.
        """
        pass

    def on_message(self, message):
        pass

    def connect(self, addr="server", port=28785):
        self.peer = self.sock.connect(enet.Address(bytearray(addr, "utf-8"), port), 2)

        while True:
            event = self.sock.service(1000)

            if event.type == enet.EVENT_TYPE_CONNECT:
                print("%s: CONNECT" % event.peer.address)

                msg = server_spec.write(
                    "N_CONNECT",
                    name="test",
                    playermodel=0,
                    pwdhash="",
                    authdomain="",
                    authname="",
                )

                packet = enet.Packet(msg)
                print(self.peer.send(1, packet))
                print("Sent login packet")
                self.open()
            elif event.type == enet.EVENT_TYPE_DISCONNECT:
                print("%s: DISCONNECT" % event.peer.address)
                continue
            elif event.type == enet.EVENT_TYPE_RECEIVE:
                print("%s: IN:  %r" % (event.peer.address, event.packet.data))
                cds = CubeDataStream(event.packet.data)
                print(cds.getint())
                continue
