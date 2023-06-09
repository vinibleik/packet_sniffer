from ctypes import c_ubyte, c_ushort

from protocols.protocol import Protocol


class Ethernet(Protocol):
    _fields_ = [
        ("_dst", c_ubyte * 6),
        ("_src", c_ubyte * 6),
        ("eth", c_ushort),
    ]

    header_len = 14

    ethertypes = {0x0800: "IPv4", 0x86DD: "IPv6"}

    def __init__(self, raw_bytes: bytes | None = None) -> None:
        super().__init__(raw_bytes)
        self.next_protocol = self.ethertypes.get(self.eth)

    @property
    def dst_mac(self) -> str:
        return bytes(self._dst).hex(":")

    @property
    def src_mac(self) -> str:
        return bytes(self._src).hex(":")

    def __repr__(self) -> str:
        return f"Ethernet ({self.header_len} bytes):\n\t{'Source:':<13} {self.src_mac:}\n\t{'Destination:':<13} {self.dst_mac}\n\t{'Ethertype:':<13} {self.next_protocol if self.next_protocol else 'Unknown Protocol'}\n"
