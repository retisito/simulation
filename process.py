from lib.server import Server
from lib.client import Client
import sys

class Process:

  def __init__(self, receive, send, id = 0):
    self.id = id
    self.receive = receive
    self.send = send
    #self.resource = resource

if __name__ == "__main__":
  p1 = Process(Server(port = 9000), Client(port = 9001), 0)
  p2 = Process(Server(port = 9001), Client(port = 9000), 1)