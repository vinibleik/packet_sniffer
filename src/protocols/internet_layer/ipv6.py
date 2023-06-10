from ctypes import c_uint8, c_uint16, c_uint32
from socket import AF_INET6, inet_ntop

from protocols.protocol import Protocol


class IPv6(Protocol):
    _fields_ = [
        ("version", c_uint32, 4),
        ("traffic_class", c_uint32, 8),
        ("flow_label", c_uint32, 20),
        ("payload_length", c_uint16),
        ("next_header", c_uint8),
        ("hop_limit", c_uint8),
        ("_src", c_uint16 * 8),
        ("_dst", c_uint16 * 8),
    ]

    protocol_numbers = {
        0x06: "TCP",
        0x11: "UDP",
    }

    header_len = 40

    def __init__(self, raw_bytes: bytes | None = None) -> None:
        super().__init__(raw_bytes)
        self.src_ip = inet_ntop(AF_INET6, self._src)
        self.dst_ip = inet_ntop(AF_INET6, self._dst)
        self.next_protocol = self.protocol_numbers.get(self.next_header)

    def __repr__(self) -> str:
        source = f"\t{'Source:':<13} {self.src_ip}"
        destiny = f"\t{'Destination:':<13} {self.dst_ip}"
        payload = f"\t{'Payload len:':<13} {self.payload_length} bytes"
        next_proto = f"\t{'Next proto:':<13} {self.next_protocol if self.next_protocol is not None else 'Unknown Protocol'}"
        hop_limit = f"\t{'Hop limit:':<13} {self.hop_limit}"
        label = f"\t{'Flow label:':<13} {self.flow_label}"
        ds = self.traffic_class & 0b11111100
        ecn = self.traffic_class & 0b00000011
        trafic_class = f"\tTraffic: {self.traffic_class:#04x} (DS: {ds:#04x}, ECN: {ecn:#03x})"
        return f"IPv6 ({self.header_len} bytes):\n{source}\n{destiny}\n{payload}\n{hop_limit}\n{label}\n{trafic_class}\n{next_proto}\n"
