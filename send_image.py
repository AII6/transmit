import socket
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import signal
from mySerial import quit

video = cv2.VideoCapture('/dev/video0')
s = socket.socket()
# s.connect(('192.168.1.100', 30000))
s.connect(('192.168.43.153', 30000))

while True:
    success, frame = video.read()
    signal.signal(signal.SIGINT, quit)
    if success:
        s.sendall(frame)