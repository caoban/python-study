import socketserver


#自己创建一个请求处理类，并且这个类要继承BaseRequestHandler
class MyTcpHandler(socketserver.BaseRequestHandler):

    def handle(self):

        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                if not self.data:
                    print(self.client_address,"断开了")
                    break
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("err",e)
                break

if __name__ == "__main__":
    HOST,PORT = "localhost", 6969

    server = socketserver.TCPServer((HOST,PORT),MyTcpHandler)
    server.serve_forever()















