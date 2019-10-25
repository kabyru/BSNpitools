import os
import sys
import socket
import subprocess

host = '10.200.173.95'
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created!")

try:
    s.connect((host,port))
except socket.error:
    print("Connection failed!")
    sys.exit()

while True:
    try:
        serverRecieve = s.recv(1024)
    except socket.error:
        print("Nothing to recieve!")
        sys.exit()
    if (serverRecieve.decode() == "record"):
        print("Record request recieved.")
        proc = subprocess.Popen("ffmpeg -ar 44100 -ac 2 -f alsa -i hw:1,0 -f v4l2 -codec:v h264 -framerate 30 -video_size 1920X1080 -itsoffset 0.5 -i /dev/video0 -copyinkf -codec:v copy -g 10 -f mp4 test1.mp4", shell=True, stdin=None, stdout=None, stderr=None, close_fds=True, preexec_fn=os.setsid)
        procID = os.getpgid(proc.pid)
        try:
            s.send(bytes(procID, "utf-8"))
        except socket.error:
            print("Error sending data.")
        
        
            

