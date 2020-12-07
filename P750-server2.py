#!/usr/bin/env python3

# This program loops (while true) on 192.168.0.27 until it recieves
# a message from sock-client-0-27 which it return to HERE and stops

import socket

# HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
# HOST = '192.168.0.10'  # P750 address on TBWwifi
HOST = '192.168.8.3'  # P750 address on TedWiFi
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
print('=== Running P750-server2.py Module -v02')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Received from Client; ', data)
            conn.sendall(data)

