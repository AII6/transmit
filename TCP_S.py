import socket
from mySerial import ser, quit
import numpy as np

socket_list = []
s = socket.socket()
s.bind(('192.168.1.103', 40000))
s.listen()

conn, addr = s.accept()
print(str(addr) + ' Joined!')
while True:

    content = conn.recv(5)

    if content is None:
        break
    else:
        data = np.frombuffer(content, dtype='uint8')
        ser.write(data.encode('gbk'))


