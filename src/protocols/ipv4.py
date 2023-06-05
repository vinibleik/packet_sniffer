from ctypes import c_uint8, c_uint16, c_uint32

from protocol import Protocol

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
        ("flags", c_uint8, 3),  # Flags
        ("fragment_offset", c_uint16, 13),  # Fragment offset
        ("ttl", c_uint8),  # Time to live (TTL)
        ("protocol", c_uint8),  # Protocol in the data portion
        ("header_checksum", c_uint16),  # Header checksum
        ("src_ip_addr", c_uint32),  # Source address
        ("dst_ip_addr", c_uint32),  # Destination address
    ]

    # 3 bits => Reserved(Must be 0), DF, MF
    flags_names = {
        0b010: "Don't Fragment (DF)",
        0b001: "More Fragments (MF)",
    }

    header_len = 20

    @property
    def flag(self) -> str:
        return self.flags_names.get(self.flags, "Not Set")

    def next_protocol(self) -> str | None:
        return protocol_numbers.get(self.protocol)
