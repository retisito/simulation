from lib.server import Server
from lib.client import Client
import sys

class Process:

  def __init__(self, receive, send, resource):
    self.receive = receive
    self.send = send
    self.resource = resource
