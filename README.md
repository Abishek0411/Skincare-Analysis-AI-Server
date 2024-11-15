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
   python port1717.py
