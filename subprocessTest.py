import subprocess
import os
import signal
import time

DETACHED_PROCESS = 0x00000008

proc = subprocess.Popen("ffmpeg -ar 44100 -ac 2 -f alsa -i hw:1,0 -f v412 -codec:v h264 -framerate 30 -video_size 1920X1080 -itsoffset 0.5 -itoffset 0.5 -i /dev/video0 -copyinkf -codec:v copy -g 10 -f mp4 test1.mp4", shell=True, stdin=None, stdout=None, stderr=None, close_fds=True, preexec_fn=os.setsid)

time.sleep(5)

os.killpg(os.getpgid(proc.pid), signal.SIGTERM) #Sends kill signal