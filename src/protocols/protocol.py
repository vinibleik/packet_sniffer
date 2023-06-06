from __future__ import annotations

from ctypes import BigEndianStructure


class Protocol(BigEndianStructure):
    _pack_ = 1

    def __new__(cls, raw_bytes: bytes | None = None) -> Protocol:
        if raw_bytes:
            return cls.from_buffer_copy(raw_bytes)
        else:
            return BigEndianStructure.__new__(cls)

    def __init__(self, raw_bytes: bytes | None = None) -> None:
        super().__init__()
        self.next_protocol = None

    def __repr__(self) -> str:
        return bytes(self).hex(" ")
