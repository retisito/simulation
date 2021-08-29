import socket

class Server:

  def __init__(self, host = "localhost", port = 9999):
    self.host = host
    self.port = port
    self.__status = self.__start()
      
  def __start(self):
    self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.listen_sock.bind((self.host, self.port))
    self.listen_sock.listen()
    self.receive_sock, self.adrress = self.listen_sock.accept()
    return True

  def run(self):
    while self.__status:
      yield self.receive()
      if self.__status: self.send()
      
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
  for data in server.run():
    print(data)
    if data == "EOL":
      server.stop()