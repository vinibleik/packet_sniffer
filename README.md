# Packet Sniffer

Fé / Faith

Um sniffer de rede inspirados por [Python 3 Network Packet Sniffer](https://github.com/EONRaider/Packet-Sniffer) que dispõe na tela os detalhes de cada frame que trafega no computador.

## Protocolos implementados

### Link Layer

- Ehternet

### Internet Layer

- IPv4
- IPv6

### Transport Layer

- TCP
- UDP

## Executando o Sniffer

O programa usa somente bibliotecas nativas do python, então não é necessário instalar dependências.

```
user@host:~$ git clone https://github.com/vinibleik/packet_sniffer.git
user@host:~$ cd packet_sniffer
user@host:~/packet_sniffer$ sudo python3 src/sniffer.py
```

_É necessário permissões de administrador para rodas a aplicação pois se utiliza do
`socket.SOCK_RAW`, um tipo especial de socket necessário para a captura dos frames
"crus" em GNU/Linux, mais informações em [Debian](https://manpages.debian.org/bullseye/manpages/packet.7.en.html)._
