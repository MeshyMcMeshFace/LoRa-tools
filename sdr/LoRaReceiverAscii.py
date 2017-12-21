#!/usr/bin/python
#
#   Copyright (c) 2017 Rikard Lindstrom <ornotermes@gmail.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import socket
import datetime
UDP_IP = "0.0.0.0"
UDP_PORT = 10542

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(512)
    print (str(datetime.datetime.now()) + " {")
    
    string = "  Raw:{"
    n = 0
    for char in list(data):
        n += 1
        string += " 0x" + char.encode("hex") + ","
    string += " },"
    print (string)
    
    string = "  LoRaHeader:{ hex:{ "
    n = 0
    for char in list(data[0:3]):
        string += " 0x" + char.encode("hex")
    string += " }, PayloadSize:" + str(ord(data[0])) + " },"
    print string
    
    string = "  Payload:{ Hex:{ "
    for char in list(data[3:]):
        string += "0x" + char.encode("hex") + ", "
    string += "},\n"
    string += "    Ascii:\""
    for char in list(data[3:]):
        if (ord(char) > 31 and ord(char) < 127):
            string += char
        else:
            string += chr(0xf0)
    string += "\"}};"
    print (string)
    
    print ("")
