import socket
import time

class Client:

  def __init__(self, host = "localhost", port = 9999):
    self.host = host
    self.port = port
    self.__status = self.__start()

  def __start(self):
    self.send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    for i in range(3):
      try:
        self.send_sock.connect((self.host, self.port))
        return True
      except: 
        print(f"{i+1}.- Connection refused to {self.host}::{self.port}")
        time.sleep(3)
    
    return False
      
  def run(self):  
    while self.__status:
      yield input(">> ")   
  
  def stop(self):     
    self.send_sock.close()
    self.__status = False

  def send(self, data):
    self.send_sock.sendall(bytes(data + "\n", "utf-8"))

  def receive(self):
    return str(self.send_sock.recv(1024).strip(), "utf-8")

if __name__ == "__main__":
  client = Client()
  for data in client.run():
    print(data)
    client.send(data)
    print(client.receive())
    if data == "EOL":
      client.stop()