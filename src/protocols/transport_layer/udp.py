from ctypes import c_uint16

from protocols.protocol import Protocol


class UDP(Protocol):
    _fields_ = [
        ("src_port", c_uint16),
        ("dst_port", c_uint16),
        ("len", c_uint16),
        ("checksum", c_uint16),
    ]

    header_len = 8

    def __init__(self, raw_bytes: bytes | None = None) -> None:
        super().__init__(raw_bytes)

    def __repr__(self) -> str:
        src_port = f"\t{'Source:':<13} {self.src_port}"
        dst_port = f"\t{'Destination:':<13} {self.dst_port}"
        chksum = f"\t{'Checksum:':<13} {self.checksum}"
        length = f"\t{'Length:':<13} {self.len}"
        return f"UDP ({self.header_len} bytes:)\n{src_port}\n{dst_port}\n{chksum}\n{length}\n"
