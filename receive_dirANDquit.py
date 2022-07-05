import socket
from mySerial import ser, quit
import numpy as np
import signal

socket_list = []
s = socket.socket()
# s.bind(('192.168.1.103', 40000))
s.bind(('192.168.43.167', 40001))
s.listen()

conn, addr = s.accept()
print(str(addr) + ' Joined!')
while True:
    content = conn.recv(3)
    signal.signal(signal.SIGINT, quit)
    if content is None:
        break
    else:
        data = np.frombuffer(content, dtype='uint8')
        print(data)
        # ser.write(data.encode('gbk'))


