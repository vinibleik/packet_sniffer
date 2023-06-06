from ctypes import c_uint8, c_uint16, c_uint32
from socket import AF_INET, inet_ntop

from protocols.protocol import Protocol

""" 
    0x00 - 0x90 (000 - 144) -> protocols
    0x91 - 0xFC (145 - 252) -> Unassigned
    0xFD - 0xFE (253 - 254) -> Use for experimentation and testing
    0xFF (255) -> Reserved 
"""
protocol_numbers = {
    0x06: "TCP",
}


class IPv4(Protocol):
    _fields_ = [
        ("version", c_uint8, 4),  # Version
        ("IHL", c_uint8, 4),  # Internet Header Length (IHL)
        ("DSCP", c_uint8, 6),  # Differentiated Services Code Point (DSCP)
        ("ECN", c_uint8, 2),  # Explicit Congestion Notification (ECN)
        ("total_length", c_uint16),  # Total Length
        ("id", c_uint16),  # Identification
        ("_flags", c_uint8, 3),  # Flags
        ("fragment_offset", c_uint16, 13),  # Fragment offset
        ("ttl", c_uint8),  # Time to live (TTL)
        ("protocol", c_uint8),  # Protocol in the data portion
        ("header_checksum", c_uint16),  # Header checksum
        ("_src", c_uint8 * 4),  # Source address
        ("_dst", c_uint8 * 4),  # Destination address
    ]

    # 3 bits => Reserved(Must be 0), DF, MF
    flags_names = {
        0b010: "Don't Fragment (DF)",
        0b001: "More Fragments (MF)",
    }

    header_len = 20

    def __init__(self, raw_bytes: bytes | None = None) -> None:
        super().__init__(raw_bytes)
        self.src_ip = inet_ntop(AF_INET, self._src)
        self.dst_ip = inet_ntop(AF_INET, self._dst)
        self.next_protocol = protocol_numbers.get(self.protocol)

    @property
    def flags(self) -> str:
        return self.flags_names.get(self._flags, "Not Set")

    def __repr__(self) -> str:
        dscp = f"\t{'DSCP:':<13} {self.DSCP}"
        total_length = f"\t{'Total Length:':<13} {self.total_length}"
        id_packet = f"\t{'ID:':<13} {self.id}"
        flags = f"\t{'Flags:':<13} {self.flags}"
        ttl = f"\t{'TTL:':<13} {self.ttl}"
        if self.next_protocol is not None:
            protocol = f"\t{'Protocol:':<13} {self.next_protocol}"
        else:
            protocol = f"\t{'Protocol:':<13} Unknown Protocol"
        chksum = f"\t{'CheckSum:':<13} {self.header_checksum}"
        src = f"\t{'Source:':<13} {self.src_ip}"
        dst = f"\t{'Destination:':<13} {self.dst_ip}"
        return f"IPv4\n{src}\n{dst}\n{dscp}\n{total_length}\n{id_packet}\n{flags}\n{ttl}\n{protocol}\n{chksum}\n"
