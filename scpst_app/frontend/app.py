from flask import Flask, render_template, request, jsonify

import dataReader

app = Flask(__name__)

global imagePath
global coordinates
global counter
counter = 0
coordinates = {}

@app.route('/')
def home():
    return jsonify({'message': 'Hello World'}), 200

@app.route('/detect', methods=['POST'])
def detect():
    global coordinates
    data = request.json
    coordinates = data
    global counter
    counter += 1
    return jsonify({'message': 'Detection successful'}), 200
    
@app.route('/fail', methods=['POST'])
def fail():
    global counter
    counter += 1
    global coordinates
    coordinates = {}
    return jsonify({'message': 'Failed successful'}), 200
    
@app.route('/getData', methods=['GET'])
def get_Data():
    global coordinates
    return jsonify(coordinates), 200

@app.route('/getImage', methods=['GET'])
def get_image():
    global imagePath
    return render_template('index.html', image=imagePath)
    
@app.route('/getCounter', methods=['GET'])
def get_Counter():
    global counter
    return jsonify({'val':counter}), 200

@app.route('/setImage', methods=['POST'])
def set_image():
    global imagePath
    data = request.json
    imagePath = data['image']
    return jsonify({'message': 'Image set successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)
