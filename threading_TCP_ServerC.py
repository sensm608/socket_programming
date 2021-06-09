import socket, threading

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print('New socket added: ', clientAddress)

    def run(self):
        print('Connection from: ', clientAddress)
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()

            if msg=='quit':
                break
            print('from client', msg)
            self.csocket.send(bytes(msg,'UTF-8'))

        print("Client at ", clientAddress, 'disconnected...')
        
LOCALHOST = '127.0.0.1'
PORT = 2500

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print('server started')
print('waiting for client request...')

while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
