from lib.server import Server
from lib.client import Client
import threading
import sys

class Process:

  def __init__(self, prev_process, next_process, id = 0):
    #self.prev_process = Server(port = prev_process)
    #self.next_process = Client(port = next_process) 
    #self.resource = resource
    self.id = id

  def prev_process(self, port):
    server = Server(port = port)
    for data in server.run():
      print(data)
      if data == "EOL":
        server.stop()

  #def run(self):
  #  return self.prev_process.run() if self.next_process.status else [] 

  #def stop(self):
  #  self.prev_process.stop()
  #  self.next_process.stop()

  #def send(self, data = "ok"):
  #  self.next_process.send(data)
  
  #def receive(self):
  #  return self.prev_process.receive()

#if __name__ == "__main__":
#  process = Process(
#    int(sys.argv[1]), 
#    int(sys.argv[2]), 
#    int(sys.argv[3]))
  
#  for data in process.run():
#    print(data)
#    process.send(f"id:{process.id}")    
