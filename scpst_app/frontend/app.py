from flask import Flask, render_template, request, jsonify

import dataReader

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello World'}), 200

@app.route('/detect', methods=['POST'])
def detect():
    data = request.json
    print("Received data")
    print(data)
    dataReader.write_coordinates(data['top'], data['left'], data['boxWidth'], data['boxHeight'])
    return jsonify({'message': 'Detection successful'}), 200

@app.route('/getImage', methods=['GET'])
def get_image():
    image = dataReader.get_image()
    print("Getting image :" + image)
    return render_template('index.html', image=image)

@app.route('/setImage', methods=['POST'])
def set_image():
    data = request.json
    print("Received data")
    dataReader.write_image(data['image'])
    return jsonify({'message': 'Image set successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/get_boxes', methods=['POST', 'GET'])
# def do_something():
#     global coordinates
#     if request.method == 'GET':
#         print(f'Sending detection results to requestor: {coordinates}')
#         return jsonify(coordinates)
#     if request.method == 'POST':
#         print('Running script.js')
#         return render_template('index.html')