import collections
import struct
from sour.common.utils.clamp import clamp
from sour.common.utils.vecfromyawpitch import vecfromyawpitch
from sour.common.vec import vec
from sour.protocol.sauerbraten.collect.physics_state import PhysicsState


class CubeDataStream(object):
    def __init__(self, data=""):
        if isinstance(data, CubeDataStream):
            self.data = bytearray(data.data)
        elif isinstance(data, bytearray):
            self.data = data
        elif isinstance(data, bytes):
            self.data = bytearray(data)
        else:
            self.data = bytearray(map(ord, data))

    @staticmethod
    def pack_format(fmt, data):
        cds = CubeDataStream()

        i = 0
        for f in fmt:
            if f == "i":
                cds.putint(data[i])
            elif f == "u":
                cds.putuint(data[i])
            elif f == "f":
                cds.putfloat(data[i])
            elif f == "s":
                cds.putstring(data[i])
            elif f == "r":
                cds.write(data[i])
            i += 1

        return cds

    def write(self, data):
        if isinstance(data, collections.Iterable):
            self.data.extend(data)
        elif isinstance(data, CubeDataStream):
            self.data.extend(data.data)
        else:
            self.data.append(data)

    def clear(self):
        self.data = bytearray()

    def empty(self):
        return len(self.data) == 0

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def read(self, n, peek=False):
        try:
            if n == 1:
                return self.data[0]
            else:
                return self.data[:n]
        finally:
            if not peek:
                del self.data[:n]

    def putbyte(self, b):
        self.write(b & 0xFF)

    def putint(self, i):
        i = int(i)
        if -127 < i and i < 128:
            self.write(i & 0xFF)
        elif -0x8000 < i and i < 0x8000:
            self.write(0x80)
            self.write(i & 0xFF)
            self.write(i >> 8 & 0xFF)
        else:
            self.write(0x81)
            self.write(i & 0xFF)
            self.write((i >> 8) & 0xFF)
            self.write((i >> 16) & 0xFF)
            self.write((i >> 24) & 0xFF)

    def putuint(self, n):
        n = long(n)
        if n < 0 or n >= (1 << 21):
            self.write(0x80 | (n & 0x7F))
            self.write(0x80 | ((n >> 7) & 0x7F))
            self.write(0x80 | ((n >> 14) & 0x7F))
            self.write(n >> 21)
        elif n < (1 << 7):
            self.write(n)
        elif n < (1 << 14):
            self.write(0x80 | (n & 0x7F))
            self.write(n >> 7)
        else:
            self.write(0x80 | (n & 0x7F))
            self.write(0x80 | ((n >> 7) & 0x7F))
            self.write(n >> 14)

    def putfloat(self, f):
        f = float(f)
        self.write(bytearray(map(ord, struct.pack("<f", f))))

    def putstring(self, s):
        self.write(bytearray(s, "utf-8"))
        self.write(0)

    def getbyte(self, peek=False):
        return self.read(1, peek)

    def getint(self, peek=False):
        c = self.read(1, peek)

        if c == 0x80:
            t = self.read(3 if peek else 2, peek)
            if peek:
                t = t[1:]
            return struct.unpack("h", t)[0]
        elif c == 0x81:
            t = self.read(5 if peek else 4, peek)
            if peek:
                t = t[1:]
            return struct.unpack("i", t)[0]
        else:
            return struct.unpack("b", bytes([c]))[0]

    def getuint(self, peek=False):
        n = self.read(1)
        if n & 0x80:
            n += (self.read(1, peek) << 7) - 0x80
            if n & (1 << 14):
                n += (self.read(1, peek) << 14) - (1 << 14)
            if n & (1 << 21):
                n += (self.read(1, peek) << 21) - (1 << 21)
            if n & (1 << 28):
                n |= -1 << 28
        return n

    def getfloat(self, peek=False):
        return struct.unpack("<f", str(self.read(4, peek)))[0]

    def getstring(self, peek=False):
        try:
            return self.read(self.data.index(0), peek).decode("utf-8")
        finally:
            self.read(1, peek)  # Throw away the null terminator

    def getphysics(self, peek=False):
        d = PhysicsState()

        physstate = self.getbyte()
        flags = self.getuint()

        for k in range(3):
            n = self.getbyte()
            n |= self.getbyte() << 8
            if flags & (1 << k):
                n |= self.getbyte() << 16
                if n & 0x800000:
                    n |= -1 << 24
            d.o[k] = n

        dir = self.getbyte()
        dir |= self.getbyte() << 8
        yaw = dir % 360
        pitch = clamp(dir / 360, 0, 180) - 90
        roll = clamp(int(self.getbyte()), 0, 180) - 90
        mag = self.getbyte()
        if flags & (1 << 3):
            mag |= self.getbyte() << 8
        dir = self.getbyte()
        dir |= self.getbyte() << 8

        d.vel = vecfromyawpitch(dir % 360, clamp(dir / 360, 0, 180) - 90, 1, 0)

        if flags & (1 << 4):
            mag = self.getbyte()
            if flags & (1 << 5):
                mag |= self.getbyte() << 8

            if flags & (1 << 6):
                dir = self.getbyte()
                dir |= self.getbyte() << 8
                falling = vecfromyawpitch(dir % 360, clamp(dir / 360, 0, 180) - 90, 1, 0)
            else:
                falling = vec(0, 0, -1)
        else:
            falling = vec(0, 0, 0)

        d.falling = falling

        seqcolor = (physstate >> 3) & 1

        d.yaw = yaw
        d.pitch = pitch
        d.roll = roll

        if (physstate >> 4) & 2:
            d.move = -1
        else:
            d.move = (physstate >> 4) & 1

        if (physstate >> 6) & 2:
            d.strafe = -1
        else:
            d.strafe = (physstate >> 6) & 1

        d.physstate = physstate & 7

        return d

    def tobytes(self):
        return bytes(self.data)
