from flask import Flask, render_template, request, jsonify



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Post request that gets json
# json :
# {
#     top: Value,
#     left: value,
#     boxWidth: value,
#     boxHeight: value    
# }

@app.route('/detect', methods=['POST'])
def detect():
    data = request.json
    print("Received data")
    print(data)
    return jsonify({'message': 'Detection successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)