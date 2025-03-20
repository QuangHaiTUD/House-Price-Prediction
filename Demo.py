import streamlit as st
import joblib

# Load model và scaler
def load_model_and_scaler(model_path, scaler_path):
    try:
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        return model, scaler
    except FileNotFoundError as e:
        st.error(f"Error loading files: {e}")
        st.stop()

model, scaler = load_model_and_scaler('model.pkl', 'scaler.pkl')

# Giao diện người dùng
st.title('House Price Prediction')
st.write('Please enter the values to get the prediction')

# Nhập dữ liệu từ người dùng
Location = st.selectbox("Location", ['Downtown', 'Urban', 'Suburban', 'Rural'])
Condition = st.selectbox("Condition", ['Excellent', 'Good', 'Fair', 'Poor'])
Garage = st.selectbox("Garage", ['Yes', 'No'])
Area = st.slider("Area", min_value=1000, max_value=5000, value=1000)
Bedroom = st.selectbox("Number of bedrooms", [1, 2, 3, 4, 5])
Bathroom = st.selectbox("Number of bathrooms", [1, 2, 3, 4])
Floors = st.selectbox("Number of floor", [1, 2, 3])
YearBuilt = st.slider("Year Built", min_value=1900, max_value=2024, value=1900)

# Encode dữ liệu đầu vào
labels1 = {'Downtown': 0, 'Urban': 1, 'Suburban': 2, 'Rural': 3}
labels2 = {'Excellent': 0, 'Good': 1, 'Fair': 2, 'Poor': 3}
labels3 = {'Yes': 1, 'No': 0}

encoded_input = [
    labels1[Location],
    labels2[Condition],
    labels3[Garage],
]

# Tính tuổi ngôi nhà
age_of_house = 2024 - YearBuilt

# Chuẩn bị đầu vào
input_data = encoded_input + [Area, Bedroom, Bathroom, Floors, age_of_house]

# Chuẩn hóa dữ liệu
input_data_scaled = scaler.transform([input_data])[0]

# Nút dự đoán
if st.button('Prediction'):
    prediction = model.predict([input_data_scaled])
    st.write('The predicted house price is:')
    st.success(f'{prediction[0].item():,.0f}$')

# Footer
st.markdown('---')
st.write('App built by [Dang Quang Hai]')
