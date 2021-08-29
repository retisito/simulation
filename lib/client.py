from threading import Thread
import socket
import time

class Client(Thread):

  def __init__(self, host = "localhost", port = 9999):
    self.host = host
    self.port = port
    Thread.__init__(self)

  def start(self):
    print(f"Connection to {self.host}::{self.port}")
    self.send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    for i in range(3):
      try:
        self.send_sock.connect((self.host, self.port))
        self.__status = True
        return Thread.start(self)
      except: 
        print(f"{i+1}.- Connection refused to {self.host}::{self.port}")
        time.sleep(3)
    
    return None
      
  def run(self):  
    while self.__status:
      data = input(">> ")
      print(data)
      self.send(data)
      print(self.receive())
      if data == "EOL":
        self.stop()
  
  def stop(self):     
    self.send_sock.close()
    self.__status = False

  def send(self, data):
    self.send_sock.sendall(bytes(data + "\n", "utf-8"))

  def receive(self):
    return str(self.send_sock.recv(1024).strip(), "utf-8")

if __name__ == "__main__":
  client = Client()
  client.start()