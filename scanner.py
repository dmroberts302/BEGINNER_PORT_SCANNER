#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid number of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit()

print("-" * 50)
print("Scanning target: " + target)
print("Time started " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(50, 89):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		if (result == 0):
			print(f"Port {port} is open")
		s.close()

except KeyboardInterrupt:
	print("\nExiting program")
	sys.exit()
except socket.gaierror:
	print("\nHostname could not be resolved.")
	sys.exit()
except socket.error:
	print("\nCould not connect to server.")
	sys.exit()
