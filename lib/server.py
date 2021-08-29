from threading import Thread
import socket

class Server(Thread):

  def __init__(self, host = "localhost", port = 9999):
    self.host = host
    self.port = port
    Thread.__init__(self)
      
  def start(self):
    print(f"Sever start at {self.host}::{self.port}")
    self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.listen_sock.bind((self.host, self.port))
    self.listen_sock.listen()
    self.receive_sock, self.adrress = self.listen_sock.accept()
    self.__status = True
    return Thread.start(self)

  def run(self):
    while self.__status:
      data = self.receive()
      print(data)
      if data == "EOL": 
        self.stop()
      else: 
        self.send()
      
  def stop(self):
    self.listen_sock.close()
    self.receive_sock.close()
    self.__status = False
       
  def send(self, data = "ok"):
    self.receive_sock.sendall(bytes(data + "\n", "utf-8"))
  
  def receive(self):
    return str(self.receive_sock.recv(1024).strip(), "utf-8")

if __name__ == "__main__":  
  server = Server()
  server.start()  