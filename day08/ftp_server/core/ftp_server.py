# _*_ coding: utf-8 _*_
import socket

from config import settings

class FTPServer():
    def __init__(self,server_address,bind_and_listen = True):
        self.server_address = server_address
        self.socket = socket.socket(settings.address_family,settings.socket_type)
        if bind_and_listen:




