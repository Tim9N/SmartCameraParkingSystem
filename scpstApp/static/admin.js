

function runModel() {
    console.log('runModel');

    // Get the model status div
    const modelStatus = document.getElementById('modelStatus');
    if (modelStatus) {
        modelStatus.innerText = 'Model Running ...';
    }
    else {
        console.log('modelStatus not found');
    }

    // Get the license plate text div
    const licensePlateText = document.getElementById('licensePlateText');
    if (licensePlateText) {
        licensePlateText.innerText = 'None';
    }
    else {
        console.log('licensePlateText not found');
    }

    // Make a request to the server to run the model
    fetch('/runModel')
        .then(response => {
            if (response.status === 501) {
                throw new Error('Server error: Model execution failed');
            }
            return response.json();
        })
        .then(data => {
            console.log('Model page (hopefully) opened successfully');
            //console.log(data);
            if (modelStatus && licensePlateText) {
                modelStatus.innerText = data.coordinates;
                licensePlateText.innerText = data.licensePlate;
            }
            else {
                console.log('modelStatus or licensePlateText not found');
            }
        })
        .catch(error => {
            console.error('Error:', error.message);
            if (modelStatus) {
                modelStatus.innerText = 'Error: ' + error.message;
            }
            if (licensePlateText) {
                licensePlateText.innerText = 'Error occurred';
            }
        });
}

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOMContentLoaded');

    // Get the run model button
    const runModelBtn = document.getElementById('runModelBtn');
    runModelBtn.addEventListener('click', runModel);

});

