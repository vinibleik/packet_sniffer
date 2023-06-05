from ctypes import c_uint8, c_uint16, c_uint32

from protocol import Protocol


class TCP(Protocol):
    _fields_ = [
        ("src_port", c_uint16),  # Source port
        ("dst_port", c_uint16),  # Destination port
        ("seq", c_uint32),  # Sequence number
        ("ack", c_uint32),  # Acknowledgment number
        ("offset", c_uint8, 4),  # Data offset
        ("reserved", c_uint8, 4),  # Reserved
        ("flags", c_uint8),  # Flags
        ("window_size", c_uint16),  # Window size
        ("checksum", c_uint16),  # Checksum
        ("urgent_pointer", c_uint16),  # Urgent pointer
    ]

    header_len = 32

    flags_names = {
        0b10000000: "CWR",
        0b01000000: "ECE",
        0b00100000: "URG",
        0b00010000: "ACK",
        0b00001000: "PSH",
        0b00000100: "RST",
        0b00000010: "SYN",
        0b00000001: "FIN",
    }

    @property
    def flag(self) -> str:
        return " ".join(
            flag
            for mask, flag in self.flags_names.items()
            if mask & self.flags
        )
