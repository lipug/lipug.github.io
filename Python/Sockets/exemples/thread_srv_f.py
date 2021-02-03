#on aurait pu aussi sans la classe, faire une interface fonctionelle
import socket, threading
def one_client_run(clientAddress, csocket):
        print ("Connection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            data = csocket.recv(2048)
            msg = data.decode()
            if msg=='bye':
              break
            print ("from client", msg)
            csocket.send(bytes(msg,'UTF-8'))
        print ("Client at ", clientAddress , " disconnected...")


def thread_srv(LOCALHOST = "127.0.0.1", PORT = 8989):
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind((LOCALHOST, PORT))
  print("Server started")
  print("Waiting for client request..")
  while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = threading.Thread(target=one_client_run(clientAddress, clientsock))
    newthread.start()

import multiprocessing
if __name__== '__main__':
  #Si pas dans notebook il suffit dáppeler la foonction
  thread_srv()
  #Dans le notebookk on crée un nouveau processus et on n'attend pas la fin!
  # p = multiprocessing.Process(target=thread_srv)
  # p.start()