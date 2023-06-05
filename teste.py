from __future__ import annotations

from ctypes import (
    BigEndianStructure,
    c_int,
    c_ubyte,
    c_uint,
    c_ushort,
    memmove,
)


class MyFirstStructure(BigEndianStructure):
    _pack_ = 1
    _fields_ = [("intfield", c_int), ("bytefield", c_ubyte)]


class NetStruct(BigEndianStructure):
    _pack_ = 1

    def __repr__(self) -> str:
        return str(bytes(self))

    def __new__(cls, raw_bytes: bytes | None = None) -> NetStruct:
        if raw_bytes:
            return cls.from_buffer_copy(raw_bytes)
        else:
            return BigEndianStructure.__new__(cls)

    def __init__(self, raw_bytes: bytes | None = None) -> None:
        pass


class NestedStruct(NetStruct):
    _fields_ = [
        ("flags", c_ubyte * 3),
        ("val1", c_ubyte),
        ("val2", c_ubyte),
    ]


class ExampleNetworkPacket(NetStruct):
    _fields_ = [
        ("version", c_ushort),
        ("reserved", c_ushort),
        ("sanity", c_uint),
        ("ns", NestedStruct),
        ("datalen", c_uint),
    ]

    _data = (c_ubyte * 0)()

    @property
    def data(self) -> str:
        return str(bytes(self._data))

    @data.setter
    def data(self, indata: bytes):
        self.datalen = len(indata)
        self._data = (self._data._type_ * len(indata))()
        memmove(self._data, indata, len(indata))

    def __repr__(self) -> str:
        return f"{super().__repr__()}Data: {self.data}"


if __name__ == "__main__":
    enp = ExampleNetworkPacket()
