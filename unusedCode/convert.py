import tensorflow as tf
from tensorflow.keras.models import model_from_json

# Load the JSON model architecture
json_model_path = 'static/model/model.json'
with open(json_model_path, 'r') as json_file:
    loaded_model_json = json_file.read()

loaded_model = model_from_json(loaded_model_json)

# Load the weights
# weights_path = 'static/model/model_weights.h5'
# loaded_model.load_weights(weights_path)

# Save the entire model in the .pb format
output_pb_path = 'static/model/model.pb'
tf.saved_model.save(loaded_model, output_pb_path)