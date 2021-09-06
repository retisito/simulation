#!/usr/bin/env python

import threading, queue, time, os, random, sys

class Process: 

  def __init__(self, i, k, send, received):
    self.i = i 
    self.k = k 
    self.send = send 
    self.received = received
    self.S = 0
    self.L = 0
    self.need_enter_to_critic_section = False
    self.used_critic_section = False
    
    for f in (self.sub_process_1, self.sub_process_2, self.sub_process_3):
      threading.Thread(target = f, daemon = True).start()

  def sub_process_1(self):
    while True:
      self.send.put(self.S)
      time.sleep(1)
      
  def sub_process_2(self):
    while True:
      self.L = self.received.get()
      time.sleep(1)

  def sub_process_3(self):
    while True:
      if not self.need_enter_to_critic_section:
        self.need_enter_to_critic_section = True if not random.randint(0, self.k) else False
    
      if self.need_enter_to_critic_section:
        if self.i == 0:
          if self.L == self.S:
            # Go to Critic Seccion
            self.used_critic_section = True
            time.sleep(3)
            self.S = (self.L + 1) % self.k
            self.used_critic_section = False
            self.need_enter_to_critic_section = False 
        else:
          if not self.L == self.S:
            # Go to Critic Seccion
            self.used_critic_section = True
            time.sleep(3)
            self.S = self.L
            self.used_critic_section = False
            self.need_enter_to_critic_section = False  
      time.sleep(1)

  def status(self):
    return self.i, self.S, self.L, self.need_enter_to_critic_section, self.used_critic_section    

# Esto limpia la salida standar
def clear():
  os.system("cls" if os.name == "nt" else "clear") 

# Esto imprime la visualizacion de cada proceso
def output(process_list):
  for index in range(len(process_list)):
    value = process_list[index].status()
    print(f"p{value[0]}: S={value[1]} L={value[2]}  p{value[0]}_need_use_cs={'True ' if value[3] else 'False'}  p{value[0]}_use_cs={'True ' if value[4] else 'False'}")
  

if __name__ == "__main__":
  N = 3 if len(sys.argv) == 1 else int(sys.argv[1])
  if N < 2:  N = 2 
  if N > 10: N = 10
  
  q = [] # Lista de Colas Sincronas
  p = [] # Lista de Procesos

  for i in range(N):
    q.append(queue.Queue())
  
  for i in range(N):
    j = N - 1 if i == 0 else i - 1 
    p.append(Process(i, N + 1, q[i], q[j]))

  clear()
  while True:
    try:
      output(p)
      time.sleep(1.0) # Latencia de 1 sec.
    except KeyboardInterrupt:
      break
    finally:
      clear()
