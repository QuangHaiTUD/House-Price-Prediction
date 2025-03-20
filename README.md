# House Price Prediction Application

## Overview
This application is a Streamlit-based web app designed to predict house prices based on various input features. It uses a pre-trained machine learning model and a scaler saved in `model.pkl` and `scaler.pkl` files, respectively. The app provides a user-friendly interface where users can input details about a house, and it returns the predicted price.

---

## Features
- **Location Selection**: Choose from options like Downtown, Urban, Suburban, and Rural.
- **Condition Selection**: Specify the condition of the house (Excellent, Good, Fair, or Poor).
- **Garage Availability**: Indicate if the house has a garage (Yes or No).
- **Area Input**: Select the area of the house in square feet using a slider.
- **Number of Bedrooms and Bathrooms**: Specify the number of bedrooms and bathrooms.
- **Floors**: Indicate the number of floors in the house.
- **Year Built**: Input the year the house was built to calculate its age.
- **Prediction Button**: Click to predict the house price based on the provided inputs.

---

## Requirements
- Python 3.7 or higher
- Required Python libraries (listed in `requirements.txt`):
  - streamlit
  - joblib
  - scikit-learn

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/house-price-prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd house-price-prediction
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. Place the `model.pkl` and `scaler.pkl` files in the project directory.
2. Run the Streamlit app:
   ```bash
   streamlit run Demo.py
   ```
3. Open the app in your browser at `http://localhost:8501`.
4. Fill in the required inputs and click **Prediction** to view the predicted house price.

---

## How It Works
1. **Load Model and Scaler**: The app loads a pre-trained machine learning model and a scaler for input preprocessing.
2. **User Input Encoding**: Converts categorical inputs into numerical representations.
3. **Feature Scaling**: Scales the input data using the pre-loaded scaler.
4. **Prediction**: The scaled inputs are fed into the model to predict the house price.
5. **Display Results**: The app displays the predicted price on the interface.

---

## Example Inputs
- **Location**: Downtown
- **Condition**: Good
- **Garage**: Yes
- **Area**: 2500 sq. ft.
- **Bedrooms**: 3
- **Bathrooms**: 2
- **Floors**: 1
- **Year Built**: 2000

**Predicted Output**: $450,000 (example value; actual results may vary).

---

## Limitations
- Requires the correct `model.pkl` and `scaler.pkl` files.
- Model performance depends on the quality of the training data.
- Inputs must be provided within the specified ranges.

---

## Contact
For questions or issues, please contact:
- **Name**: Dang Quang Hai
- **Email**: dangquanghai@example.com

