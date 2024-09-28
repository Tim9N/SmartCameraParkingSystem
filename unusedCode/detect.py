import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image

def detect_and_crop(model_location, img_location):
    # Load the model using TensorFlow Hub
    print('Loading model...')
    model = hub.load(model_location)
    print('Model loaded from:', model_location)

    # Load the image
    img = Image.open(img_location)
    img_width, img_height = img.size

    # Convert image to numpy array
    img_np = np.array(img)

    # Perform detection on the image
    detector_output = model(img_np[np.newaxis, ...])
    predictions = detector_output['detection_boxes'].numpy()
    scores = detector_output['detection_scores'].numpy()

    # Options for the detection (adjust score threshold and IOU as needed)
    score_threshold = 0.7

    # Filter predictions based on score threshold
    valid_predictions = [
        (box, score) for box, score in zip(predictions[0], scores[0]) if score > score_threshold
    ]

    if valid_predictions:
        # Process the first valid prediction (assuming it's the license plate)
        box, score = valid_predictions[0]

        # Get the bounding box coordinates
        ymin, xmin, ymax, xmax = box

        # Calculate the bounding box dimensions
        left = xmin * img_width
        top = ymin * img_height
        box_width = (xmax - xmin) * img_width
        box_height = (ymax - ymin) * img_height

        # Log the detected bounding box for debugging
        print(f'Detected box: left={left}, top={top}, width={box_width}, height={box_height}')

        # Crop the image based on the bounding box
        cropped_img = img.crop((left, top, left + box_width, top + box_height))
        cropped_img.save('cropped_license_plate.png')

        return {
            'top': top,
            'left': left,
            'boxWidth': box_width,
            'boxHeight': box_height
        }
    else:
        print('No license plate detected')
        return None
