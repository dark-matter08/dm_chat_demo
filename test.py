import socket
import struct


def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]


def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))


ip_to = ip2int('127.0.0.1')
print(f"ip in int: {ip_to}")
ip_back = int2ip(ip_to)
print(f"ip in str: {ip_back}")
