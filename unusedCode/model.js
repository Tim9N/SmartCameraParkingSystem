import * as tf from '@tensorflow/tfjs';
import '@tensorflow/tfjs-automl';

function detectAndCrop(modelLocation, imgLocation) {

    

    // Load the model using TensorFlow.js AutoML Object Detection
    console.log('Loading model...');
    
    const modelPath = modelLocation;
    console.log('Model path:', modelPath);
    
    return tf.automl.loadObjectDetection(modelPath).then(function(model) {
        // Get the element from static/images/Cars3.png
        const img = imgLocation;
      
        // Options for the detection (adjust score threshold and IOU as needed)
        const options = {
          score: 0.7,  // Only consider detections with a score above 0.5
          iou: 0.5,    // Intersection over Union threshold for non-max suppression
          topk: 20     // Maximum number of boxes to return
        };
      
        // Perform detection on the image
        return model.detect(img, options).then(function(predictions) {
            console.log('Predictions:', predictions); // For Debug
          
            // If predictions exist, process the first one (assuming it's the license plate)
            if (predictions && predictions[0]) {
                // Get the actual image dimensions (natural width and height)
                const imgWidth = img.naturalWidth;
                const imgHeight = img.naturalHeight;
              
                // Get the displayed image dimensions (could be different due to scaling)
                const displayedWidth = img.clientWidth;
                const displayedHeight = img.clientHeight;
              
                // Calculate the scaling factors
                const scaleX = imgWidth / displayedWidth;
                const scaleY = imgHeight / displayedHeight;
              
                // Get the first prediction's bounding box, adjusted for scaling
                const left = predictions[0].box.left;
                const top = predictions[0].box.top;
                const boxWidth = predictions[0].box.width;
                const boxHeight = predictions[0].box.height;   
              
                // Apply scaling to the detected bounding box coordinates and size
                const scaledLeft = left * scaleX;
                const scaledTop = top * scaleY;
                const scaledBoxWidth = boxWidth * scaleX;
                const scaledBoxHeight = boxHeight * scaleY;
              
                // Log the detected bounding box for debugging
                //console.log(`Detected box: left=${scaledLeft}, top=${scaledTop}, width=${scaledBoxWidth}, height=${scaledBoxHeight}`);
              
                return {
                    top: scaledTop,
                    left: scaledLeft,
                    boxWidth: scaledBoxWidth,
                    boxHeight: scaledBoxHeight
                };
            } else {
                console.error('No license plate detected');
            }
        });
    });
}