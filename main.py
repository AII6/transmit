import socket
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2

image = cv2.imread("C:\\Users\\Jack Lee\\Pictures\\lcj34.jpg")
#
# print(image.dtype)
# print(len(image.reshape(-1, 1)))
video = cv2.VideoCapture('/dev/video0')
s = socket.socket()
s.connect(('192.168.1.100', 30000))
while True:
    success, frame = video.read()
    # print(frame.dtype)
    # print(frame.shape)
    # print(len(frame.reshape(-1, 1)))
    if success:
        # cv2.imshow("11", frame)
        # a = base64.b64encode(bytes(frame))
        # for i in range(480):
        #     # cv2.waitKey(100)
        #     tlen = s.send(frame[i])
        #     if tlen != 1920:
        #         print(tlen)
        s.sendall(frame)
        # print(np.sum(frame))
        # break
    # cv2.waitKey(100)
    # s.sendall(image)
    # print(image.shape)

