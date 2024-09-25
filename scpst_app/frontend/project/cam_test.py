from picamera2 import Picamera2

#import subprocess

#subprocess.run(['./run_proj.sh'])

picam2 = Picamera2()

picam2.start_and_capture_file("testing.jpg")
