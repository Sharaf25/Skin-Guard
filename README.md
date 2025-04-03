# Skin Guard - Skin Cancer Detection System

## Overview
Skin Guard is a web-based application designed to assist in the early detection of skin cancer using machine learning algorithms. The primary goal of this project is to build a robust **Skin Cancer Detection System** utilizing **Convolutional Neural Networks (CNNs)**. By leveraging a carefully designed CNN architecture, the system can classify skin lesions into different categories and provide additional information about the detected condition.

The project uses the **HAM10000 dataset** from Kaggle, which contains a diverse set of skin lesion images for training and testing the model.

---

## Features
- **Image Upload**: Users can upload an image of a skin lesion for analysis.
- **Skin Cancer Detection**: The system predicts the type of skin lesion and provides a classification result.
- **Additional Information**: Displays detailed information about the detected condition to help users understand the results.
- **Reset Functionality**: Users can reset the system to upload a new image for analysis.

---

## Dataset
The project uses the **HAM10000 dataset**, which is publicly available on Kaggle. The dataset contains 10,015 dermatoscopic images of common pigmented skin lesions.

- Dataset Link: [HAM10000 Dataset on Kaggle](https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000)

---

## Disclaimer
This project is for **educational purposes only** and is not intended to replace professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified healthcare provider with any questions you may have regarding a medical condition.

---

## Installation and Setup

### Prerequisites
- Python 3.6 or higher
- `pip` (Python package manager)

### Steps to Download and Run the Project
1. **Clone the Repository**:
   ```bash
   Download Skin Guard
   ```

2. **Install Dependencies**:
   Install the required Python libraries using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the Flask server:
   ```bash
   python app.py
   ```

4. **Access the Application**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## Project Structure
```
Project/
│
├── app.py                 # Flask backend for handling routes and image uploads
├── skin_cancer_detection.py # CNN model definition and helper functions
├── templates/
│   ├── index.html         # Home page
│   ├── about.html         # About page
│   ├── check.html         # Skin check page
│
├── static/
│   ├── styles.css         # CSS for styling the application
│   ├── script.js          # JavaScript for frontend functionality
│
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## Technologies Used
- **Frontend**:
  - HTML5
  - CSS3
  - JavaScript
- **Backend**:
  - Flask (Python)
- **Machine Learning**:
  - TensorFlow
  - Keras
  - NumPy
  - Pillow (PIL)

---

## Future Improvements
- Add user authentication for personalized results.
- Enhance the CNN model for higher accuracy.
- Integrate additional datasets for better generalization.
- Provide a downloadable report of the analysis.

---