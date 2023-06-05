def snif():
    import os
    from socket import AF_PACKET, SOCK_RAW, ntohs, socket

    ether_types = {0x0800: "IPv4", 0x0806: "ARP", 0x86DD: "IPv6"}

    if os.getuid() != 0:
        raise SystemExit(
            "Error: Permission denied. This application requires administrator privileges to run."
        )

    with socket(AF_PACKET, SOCK_RAW, ntohs(0x0003)) as sock:
        for i in range(10):
            frame = sock.recv(9000)
            mac_dest = frame[:6].hex(":")
            mac_src = frame[6:12].hex(":")
            ether_type = int.from_bytes(frame[12:14])
            print(f"Frame #{i+1}")
            print(f"Destination MAC Address: {mac_dest}")
            print(f"Source MAC Address: {mac_src}")
            print(
                f"Ethertype: {ether_types.get(ether_type, 'Unknown Protocol')}\n"
            )


import protocols

print(dir())
print(dir(protocols))
protocols.ethernet.print_protocol()
protocols.ipv4.print_protocol()
protocols.tcp.print_protocol()
ethernet = getattr(protocols, "ethernet")
print(dir(ethernet))
