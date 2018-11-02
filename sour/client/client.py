from sour.protocol.sauerbraten.collect.server_read_stream_protocol import (
    sauerbraten_stream_spec as server_spec,
)
from sour.protocol.sauerbraten.collect.client_read_stream_protocol import (
    sauerbraten_stream_spec as client_spec,
)

import enet
import random
import struct

def to_bytes(string):
    return string.encode('utf-8')

class Client(object):
    def __init__(self):
        self.sock = enet.Host(None, 1, 2)

    def connect(self, addr="server", port=28785):
        self.peer = self.sock.connect(enet.Address(bytearray(addr, 'utf-8'), port), 2)

        while True:
            event = self.sock.service(1000)

            if event.type == enet.EVENT_TYPE_CONNECT:
                print("%s: CONNECT" % event.peer.address)
                empty = to_bytes('')
                msg = struct.pack("I4sIsss", 0, to_bytes('two'), 0, empty, empty, empty)
                packet = enet.Packet(msg)
                print(self.peer.send(1, packet))
                print("Sent login packet")

            elif event.type == enet.EVENT_TYPE_DISCONNECT:
                print("%s: DISCONNECT" % event.peer.address)
                continue
            elif event.type == enet.EVENT_TYPE_RECEIVE:
                print("%s: IN:  %r" % (event.peer.address, event.packet.data))
                client_spec.read(event.packet.data, {})
                continue

            # counter += 1
            # if counter >= MSG_NUMBER:
                # msg = SHUTDOWN_MSG
                # peer.send(0, enet.Packet(msg))
                # host.service(100)
                # peer.disconnect()

            # print("%s: OUT: %r" % (self.peer.address, msg))
