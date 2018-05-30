# _*_ coding: utf-8 _*_
import socket

class FTPServer():
    def __init__(self,server_address,bind_and_listen = True):
        self.server_address = server_address
        self.socket = socket.socket(set)
    pass

