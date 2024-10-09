# External imports
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
import cv2 as cv
import subprocess
from picamera2 import Picamera2


def main():
    picam2 = Picamera2()
    #picam2.configure(picam2.create_still_configuration())
    # Path to the images
    imagePathHeader = 'static/images/'

    # Counter for the images
    i = 1
    
    # headless chrome
    service = Service('/usr/bin/chromedriver')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(service=service, options=options)

    while True:
        picam2.start_and_capture_file(imagePathHeader + 'testimage.jpg')

        # Get the image path
        imagePath = imagePathHeader + 'testimage.jpg'
        requests.post('http://127.0.0.1:5000/setImage', json={'image':imagePath})
        
        time.sleep(5)
        
        # Print the image path
        print("Trying image: " + imagePath)
        
        #selenium load the page 
        driver.get('http://127.0.0.1:5000/getImage')
        
        while True:
            response = requests.get('http://127.0.0.1:5000/getCounter')
            counter_value = response.json().get('val')
            print(f'We got {counter_value} from the server')
            if counter_value == i:
                break
            else:
                time.sleep(5)
        i += 1
        
        response = requests.get('http://127.0.0.1:5000/getData')
    
        data = response.json()
        top = data.get('top')
        if top == None:
            print('Nothing Detected')
            continue
        left = data.get('left')
        width = data.get('boxWidth')
        height = data.get('boxHeight')
        
        print('Saving cropped image')
        im = cv.imread(imagePath)
        im = im[int(top):int(top+height),int(left):int(left+width)]
        cv.imwrite('cropped.jpg', im)
        
        print(top, left, width, height)
        print('Calling OCR')
        subprocess.run(['python', 'ocr.py'])

if __name__ == "__main__":
    main()
