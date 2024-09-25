from paddleocr import PaddleOCR
import cv2 as cv

ocr = PaddleOCR(use_angle_cls=True, lang='en', show_logs=False)
im = cv.imread('testing.jpg')
result = ocr.ocr(im)[0]
print(result)
