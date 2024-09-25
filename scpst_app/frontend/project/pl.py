from paddleocr import PaddleOCR
import os
import cv2 as cv
#from picamera2 import Picamera2

ocr = PaddleOCR(use_angle_cls=True, lang='en', show_logs=False)

#picam2 = Picamera2()

#picam2.start_and_capture_file("testing.jpg")


for path in os.listdir():
	if not 'jpg' in path:
		continue
	im = cv.imread(path)
	result = ocr.ocr(im)[0]
	for bbox, (text, conf) in result:
		print(text)

	
