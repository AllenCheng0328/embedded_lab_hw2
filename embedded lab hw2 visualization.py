import matplotlib.pyplot as plt

import socket
import numpy as np
import json
import time
import random
HOST = '172.20.10.13' # Standard loopback interface address
PORT = 65431 # Port to listen on (use ports > 1023)
N = 200

sample_num = 0         #0~N-1
data = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while sample_num<N:
            data.append(  conn.recv(1024).decode('utf-8')  )
            print('Received from socket server : ', data[sample_num])
            sample_num +=1


for i in range(len(data)):
    temp = data[i].split(' ')
    for j in range(3):
        temp[j] = float(temp[j])
    temp[3] = i+1
    temp[2] = temp[2]-51
    temp = temp[0:4]
    data[i] = temp

arr2d = np.array(data)
plt.plot(arr2d[:,3],arr2d[:,0:3])
plt.title("3 axis a-t graph")
plt.xlabel("time (s)")
plt.ylabel("acceleration")
plt.legend(["x","y","z"])
plt.show()