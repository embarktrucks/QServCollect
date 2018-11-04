import gzip
import struct

from sour.protocol.cube_data_stream import CubeDataStream
from sour.protocol.sauerbraten.collect.client_read_stream_protocol import (
    sauerbraten_stream_spec as client_spec,
)

def get_demo_data(demo_filename):
    "Returns a list of ClientSession objects."

    with gzip.open(demo_filename) as f:
        DEMO_MAGIC, demo_version, protocol_version = struct.unpack("16sii", f.read(24))
        print(DEMO_MAGIC, demo_version, protocol_version)

        while True:
            d = f.read(12)
            if len(d) < 12:
                # print "breaking on read packet header '{}'".format(d)
                break

            millis, channel, length = struct.unpack("iii", d)

            d = f.read(length)
            if len(d) < length:
                break

            cds = CubeDataStream(d)
            messages = client_spec.read(cds, {}, {})

            for message in messages:
                print(millis, message)
