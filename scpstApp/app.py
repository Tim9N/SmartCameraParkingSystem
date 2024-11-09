from flask import Flask, jsonify, request, render_template, session, redirect, url_for
from flask_cors import CORS
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from flask_login import login_required, LoginManager, UserMixin, login_user, logout_user, current_user

from imageAPI import cropImage, ocrImage
from bucketAPI import download_from_bucket
from firestoreAPI import *
from User import User


# Global variables
global imagePath
imagePath = "static/images/fromthepi.png"

global coordinates
coordinates = None

global croppedImagePath
croppedImagePath = "static/cropped/cropped.png"

global bucketImagePath
bucketImagePath = "fromthepi.jpg"

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect to login page if not logged in

@login_manager.user_loader
def load_user(user_id):
    user = getUserByEmail(user_id)
    if user:
        return User.from_dict(user)
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = getUserByEmail(username)
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('home'))
        else:
            return 'Invalid credentials', 401
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.json
        user = getMostRecentUser()
        userData = {
            'email': data.get('email'),
            'password': data.get('password'),
            'name': data.get('name'),
            'license_plate': user.get('license_plate'),
            'credit_card': data.get('credit_card'),
            'last_entry': user.get('last_entry'),
            'last_exit': user.get('last_exit')
        }
        updateUser(userData)
        login_user(userData)
        return redirect(url_for('home'))
    return render_template('signup.html')

# Call this function to load the license localization model
@app.route('/model')
def model():
    global imagePath
    download_from_bucket(bucketImagePath, imagePath)
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

        # global imagePath
        # download_from_bucket(bucketImagePath, imagePath)

        # # importing PIL Module
        # from PIL import Image
        
        # # open the original image
        # original_img = Image.open(imagePath)
        
        # # Flip the original image vertically
        # vertical_img = original_img.transpose(method=Image.FLIP_TOP_BOTTOM)
        # #vertical_img.save(imagePath)

        # # Flip the original image horizontally
        # horizontal_img = vertical_img.transpose(method=Image.FLIP_LEFT_RIGHT)
        # horizontal_img.save(imagePath)
        
        # # close all our files object
        # original_img.close()
        # vertical_img.close()
        # horizontal_img.close()
        # sleep(4)

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