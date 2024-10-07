import numpy as np
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.keras.models import model_from_json
import os


def skincare_analysis_model(image_path: str) -> dict:

    # Step 1: Load the model architecture and weights
    # Load JSON model architecture
    with open(r'C:\Users\whack\OneDrive\Desktop\Skincare_Detection\Flask_Server\Model\model.json', 'r') as json_file:
        loaded_model_json = json_file.read()

    # Recreate the model from the JSON architecture
    model = model_from_json(loaded_model_json)

    # Load weights into the model
    model.load_weights(r'C:\Users\whack\OneDrive\Desktop\Skincare_Detection\Flask_Server\Model\skinmate-model.h5')

    # Compile the model (ensure it's compiled with the same optimizer and loss as before)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Check if Image Path exists
    if not os.path.exists(image_path):
        print("Error: The specified file does not exist.")
    else:
        # Step 3: Load and preprocess the image
        img = load_img(image_path, target_size=(150, 150))
        x = img_to_array(img)
        x /= 255.0  # Normalize the image
        x = np.expand_dims(x, axis=0)

        # Prepare the image for model prediction
        images = np.vstack([x])
        
        # Step 4: Make predictions using the loaded model
        classes = model.predict(images, batch_size=10)
        
        # Normalize, round, and categorize the predictions
        classes_normalized = classes * 1000
        classes_rounded = np.round(classes_normalized)
        classes_in_level = classes_rounded / 100
        classes_in_level_rounded = np.ceil(classes_in_level)
        classes_in_level_rounded_1d = classes_in_level_rounded.flatten()

        # Assigning values to specific skin issues
        acnes_level = int(classes_in_level_rounded_1d[0])
        blackheads_level = int(classes_in_level_rounded_1d[1])
        darkspots_level = int(classes_in_level_rounded_1d[2])
        wrinkles_level = int(classes_in_level_rounded_1d[3])

        # Determine the most significant skin problem
        categories = np.array(['acnes', 'blackheads', 'darkspots', 'wrinkles'])
        max_index = np.argmax(classes_in_level_rounded)
        max_category = categories[max_index]
        print(f"\nMost significant skin problem: " + str(max_category))

        result = {
            "acnes": str(acnes_level),
            "blackheads": str(blackheads_level),
            "darkspots": str(darkspots_level),
            "wrinkles": str(wrinkles_level),
            "significant_problem": str(max_category),
        }

        return result
    
