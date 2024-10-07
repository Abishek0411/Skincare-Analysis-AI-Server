from flask import Flask, request, jsonify
from skin_care_analysis import skincare_analysis_model 
import os
import uuid

app = Flask(__name__)

# Make Upload directory if it already does not exist
UPLOAD_FOLDER = 'upload'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Route used to check for functioning of the flask app
@app.route('/')
def hello_world():
    app.logger.info('Hello world endpoint was called')
    return 'Hello from Flask!'

@app.route('/image', methods=['POST'])
def upload_image():
    app.logger.info('Upload image endpoint was called')

    # Check if image was received
    if 'image' not in request.files:
        app.logger.error('No image part in the request')
        return jsonify({'error': 'No image part'}), 400

    file: object = request.files['image']
    app.logger.info(f'Received file: {file.filename}')

    # Whether the image has a name or if it was properly selected
    if file.filename == '':
        app.logger.error('No selected file')
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # Appropriate a name for the image and save it in the upload directory
        unique_filename = str(uuid.uuid4()) + '_' + file.filename
        file_path: str = os.path.join(UPLOAD_FOLDER, unique_filename)
        file.save(file_path)
        app.logger.info(f'File saved to {file_path}')

        # Call the Model
        try:
            app.logger.info(f'Calling ECG model on file: {file_path}')
            result: dict = skincare_analysis_model(file_path)
            app.logger.info(f'Model result: {result}')
        except Exception as e:
            app.logger.error(f'Model processing failed: {e}', exc_info=True)
            return jsonify({'error': 'Model processing failed'}), 500

        # Delete the image
        os.remove(file_path)
        # Return
        response = {
            'message': 'Image Received Successfully',
            'result': result
        }

        return jsonify(response), 200

if __name__ == '__main__':
    app.run(port=8080, debug=True)