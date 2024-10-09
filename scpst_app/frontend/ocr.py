#from paddleocr import PaddleOCR
import cv2 as cv
import easyocr

#ocr = PaddleOCR(use_angle_cls=True, lang='en', show_logs=False)
#im = cv.imread('cropped.jpg')
#result = ocr.ocr(im)[0]
#for bbox, (text, conf) in result:
	#print(text)
reader = easyocr.Reader(['en'])
results = reader.readtext('Cars1.png')
for result in results:
	print(result[1])
