# Flip the image horizontally
import cv2
import numpy as np
import imutils

imagePath = "static/images/fromthepi.png"

# importing PIL Module
from PIL import Image
 
# open the original image
original_img = Image.open(imagePath)
 
# Flip the original image vertically
vertical_img = original_img.transpose(method=Image.FLIP_TOP_BOTTOM)
vertical_img.save(imagePath)
 
# close all our files object
original_img.close()
vertical_img.close()