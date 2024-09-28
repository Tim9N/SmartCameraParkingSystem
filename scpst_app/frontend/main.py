# External imports
import time
from selenium import webdriver

# Internal imports
import dataReader # To pass info between python files

def main():

    # Path to the images
    imagePathHeader = "static/images/Cars"

    # Counter for the images
    i = 1
    
    # headless chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)

    # Loop every 5 seconds
    while True:
        # Get the image path
        imagePath = imagePathHeader + str(i%13) + ".png"

        # Write the image path to the data.txt file
        dataReader.write_image(imagePath)

        # Increment the counter 
        i += 1

        # Print the image path
        print("Trying image: " + imagePath)
        
        #selenium load the page 
        driver.get('http://127.0.0.1:5000/getImage')

        # wait for 5 seconds
        time.sleep(10)

        # Output the top and left coordinates of the license plate
        print("Top: " + str(dataReader.get_top()))
        print("Left: " + str(dataReader.get_left()))


if __name__ == "__main__":
    main()