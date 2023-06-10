import os
from itertools import count
from socket import AF_PACKET, SOCK_RAW, ntohs, socket
from time import sleep

import protocols

if os.getuid() != 0:
    raise SystemExit(
        "Error: Permission denied. This application requires administrator privileges to run."
    )


with socket(AF_PACKET, SOCK_RAW, ntohs(0x0003)) as sock:
    protocol_queue = ["Ethernet"]

    start = end = 0

    try:
        print("Inicializando a captura de pacotes! Ctrl+C para sair...")
        sleep(2)
        for i in count(start=1):
            start = 0
            frame = sock.recv(9000)
            print(f"\nFrame #{i} Length: {len(frame)}")
            for proto_name in protocol_queue:
                protocol = getattr(protocols, proto_name, None)
                if protocol is None:
                    break
                end = start + protocol.header_len
                header = frame[start:end]
                new_proto = protocol(header)
                print(new_proto, end="")
                if new_proto.next_protocol is None:
                    break
                protocol_queue.append(new_proto.next_protocol)
                start = end
            data = frame[end:]
            print(f"Payload ({len(data)} bytes): {data}\n")
            del protocol_queue[1:]
    except KeyboardInterrupt:
        print("\nSaindo...")
