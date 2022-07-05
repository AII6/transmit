import socket
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2

image = cv2.imread("C:\\Users\\Jack Lee\\Pictures\\lcj34.jpg")

video = cv2.VideoCapture('/dev/video0')
s = socket.socket()
s.connect(('192.168.1.100', 30000))
while True:
    success, frame = video.read()

    if success:

        s.sendall(frame)


