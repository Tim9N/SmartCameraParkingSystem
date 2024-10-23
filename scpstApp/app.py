from flask import Flask, jsonify, request, render_template
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

from imageAPI import cropImage, ocrImage
from bucketAPI import download_from_bucket

app = Flask(__name__)

global imagePath
imagePath = "static/images/fromthepi.png"

global coordinates
coordinates = None

global croppedImagePath
croppedImagePath = "static/cropped/cropped.png"

global bucketImagePath
bucketImagePath = "fromthepi.jpg"


@app.route('/')
def home():
    return render_template('index.html')

# Call this function to load the license localization model
@app.route('/model')
def model():
    global imagePath
    download_from_bucket(bucketImagePath, imagePath)
    sleep(2)
    return render_template('model.html', image=imagePath)

# Call this function to run the license localization model
@app.route('/runModel')
def run_model():
    # try:
        # Set up Chrome options for headless mode
        chrome_options = webdriver.FirefoxOptions()
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # chrome_options.add_experimental_option('useAutomationExtension', False)

        # Set up the Chrome driver
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=chrome_options)

        # Open the testing page
        driver.get('http://localhost:5000/model')

        sleep(7)

        # Close the browser
        driver.quit()

        global coordinates

        if coordinates is None:
            return jsonify({"message": "Model page opened successfully", "coordinates": "None", "licensePlate": "None"}), 200
        else:
            
            global imagePath
            print("Processing Image")
            cropImage(imagePath, coordinates)
            print("Cropped Image")
            text = ocrImage(croppedImagePath)
            print("Text: ", text)
            return jsonify({"message": "Model page opened successfully", "coordinates": coordinates, "licensePlate": text}), 200
    # except Exception as e:
    #     return jsonify({"error": str(e)}), 501

# Called by model.js when license plate is localized
@app.route('/detect', methods=['POST'])
def detect():
    global coordinates
    data = request.json
    coordinates = data
    print(coordinates)
    return jsonify({'message': 'Detection successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)