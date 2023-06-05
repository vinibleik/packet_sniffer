from ctypes import BigEndianStructure, LittleEndianStructure, c_int, c_uint8


class MyLittleStruct(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("first_four_bits", c_uint8, 4),
        ("second_four_bits", c_uint8, 4),
        # ("second_byte", c_uint8),
        ("int", c_int),
        ("args", c_uint8 * 2),
    ]

    def __repr__(self) -> str:
        return str(f"{bytes(self)}")


class MyBigStruct(BigEndianStructure):
    # _pack_ = 1
    _fields_ = [
        ("first_four_bits", c_uint8, 4),
        ("second_four_bits", c_uint8, 4),
        # ("second_byte", c_uint8),
        ("int", c_int),
        ("args", c_uint8 * 2),
    ]

    def __repr__(self) -> str:
        return str(f"{bytes(self)}")


if __name__ == "__main__":
    l = MyLittleStruct()
    b = MyBigStruct()
