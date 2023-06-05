from ctypes import c_ubyte, c_ushort

from protocol import Protocol


class Ethernet(Protocol):
    _fields_ = [
        ("dst", c_ubyte * 6),
        ("src", c_ubyte * 6),
        ("eth", c_ushort),
    ]

    header_len = 14
    ethertypes = {
        0x0800: "ipv4",
    }

    def next_protocol(self) -> str | None:
        return self.ethertypes.get(self.eth)


if __name__ == "__main__":
    ex_dst = b"\xe1\xe2\xe3\xe4\xe5\xe6"
    ex_src = b"\xa1\xa2\xa3\xa4\xa5\xa6"
    ex_eth = b"\x08\x00"

    ex_header = ex_dst + ex_src + ex_eth
    eth_test = Ethernet(ex_header)
