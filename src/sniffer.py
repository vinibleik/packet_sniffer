import os
from socket import AF_PACKET, SOCK_RAW, ntohs, socket

import protocols

if os.getuid() != 0:
    raise SystemExit(
        "Error: Permission denied. This application requires administrator privileges to run."
    )


with socket(AF_PACKET, SOCK_RAW, ntohs(0x0003)) as sock:
    protocol_queue = ["Ethernet"]

    start = end = 0

    for i in range(1, 11):
        frame = sock.recv(9000)
        print(f"Frame #{i}\n")
        for proto_name in protocol_queue:
            protocol = getattr(protocols, proto_name, None)
            if protocol is None:
                break
            end = start + protocol.header_len
            header = frame[start:end]
            new_proto = protocol(header)
            print(new_proto)
            if new_proto.next_protocol is None:
                break
            protocol_queue.append(new_proto.next_protocol)
            start = end
        data = frame[end:]
        print(f"Data\n{data}\n\n")
        del protocol_queue[1:]
