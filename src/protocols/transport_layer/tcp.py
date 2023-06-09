from ctypes import c_uint8, c_uint16, c_uint32

from protocols.protocol import Protocol


class TCP(Protocol):
    _fields_ = [
        ("src_port", c_uint16),  # Source port
        ("dst_port", c_uint16),  # Destination port
        ("seq", c_uint32),  # Sequence number
        ("ack", c_uint32),  # Acknowledgment number
        ("offset", c_uint8, 4),  # Data offset
        ("reserved", c_uint8, 4),  # Reserved
        ("_flags", c_uint8),  # Flags
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

    def __init__(self, raw_bytes: bytes | None = None) -> None:
        super().__init__(raw_bytes)

    @property
    def flags(self) -> str:
        return " ".join(
            flag
            for mask, flag in self.flags_names.items()
            if mask & self._flags
        )

    def __repr__(self) -> str:
        src_port = f"\t{'Source:':<13} {self.src_port}"
        dst_port = f"\t{'Destination:':<13} {self.dst_port}"
        seq_number = f"\t{'Seq Number:':<13} {self.seq}"
        ack_number = f"\t{'ACK Number:':<13} {self.ack}"
        flags = f"\t{'Flags:':<13} {self.flags}"
        win_size = f"\t{'Window Size':<13} {self.window_size}"
        chksum = f"\t{'Checksum:':<13} {self.checksum}"
        return f"TCP ({self.header_len} bytes:)\n{src_port}\n{dst_port}\n{seq_number}\n{ack_number}\n{flags}\n{win_size}\n{chksum}\n"
