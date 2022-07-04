import socket

import numpy as np

socket_list = []
s = socket.socket()
s.bind(('192.168.1.103', 40000))
s.listen()

conn, addr = s.accept()
print(str(addr) + ' Joined!')
while True:
    # content = conn.recv(921600)
    content = conn.recv(921600)
    # if len(content) != 1920:
    #     print(len(content))
    # print(len(content))
    while len(content) < 921600:
        a = conn.recv(921600-len(content))
        content += a
    if content is None:
        break
    else:
        image = np.frombuffer(content, dtype='uint8')
        # print(len(image))
        # print(image.reshape(480, 640, 3))
        # result = image.reshape(400, 300, 3)
        result = image.reshape(480, 640, 3)
        # print(np.sum(result - frame88))
        predict(result)
        # print(np.sum(result))
