# Acne Recognition and Skincare Recommendation System - Backend

This repository contains the backend server and machine learning model for the Acne Recognition and Skincare Recommendation System. The backend processes images, analyzes skin tone, type, and acne severity, and provides tailored skincare recommendations based on real-time facial image analysis.

## Features
- **Image Processing**: Accepts facial images for analysis.
- **Skin Analysis**: Utilizes deep learning models to classify skin tone, type, and acne severity.
- **Recommendation Engine**: Based on skin characteristics, provides skincare product recommendations.
- **API Integration**: Communicates with the mobile app front-end to handle requests and return analysis results.

## Tech Stack
- **Python**: Core language for backend logic and image analysis.
- **Flask**: REST API framework for handling client requests.
- **EfficientNet (Transfer Learning)**: For skin type and acne severity classification.
- **K-Means Clustering**: For skin tone segmentation.
- **Postman**: Testing API endpoints.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd Acne-Recognition-Backend
   
2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

2. **Run the Flask Server**:
   ```bash
   flask run

## API Endpoints
- POST /upload_image: Accepts an image file for analysis.
- POST /get_recommendations: Returns skincare recommendations based on image analysis results.

## Future Enhancements
- Integrate additional skincare concerns such as pigmentation analysis.
- Improve model accuracy for acne classification.

## Front-End Link
Check out the Front-end Repository for the mobile app interface and user interactions:
https://github.com/Abishek0411/Skincare-Analysis-Frontend



