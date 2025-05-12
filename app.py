import streamlit as st
import pickle
import numpy as np
import pandas as pd

brand_names=['Poco', 'Realme', 'Oppo', 'Motorola', 'Redmi', 'Samsung', 'Vivo', 'Apple',
 'Infinix', 'Mi' 'Gionee', 'Itel' 'Micromax', 'Tecno', 'Marq by flipkart',
 'Lava', 'Nokia', 'Tcl', 'Asus', 'Panasonic', 'Alcatel', 'Maplin', 'Yu', 'Coolpad',
 'Xolo', 'Jmax', 'Karbonn','Others']

# Load the model
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Define column names as per the updated DataFrame (excluding rating-related fields)
input_columns = [
    'ram', 'brand', 'rom_size', 'screen_size',
    'battery_capacity', 'front_camera_mp', 'primary_camera_mp', 'total_rear_camera'
]

st.title("Smartphone Price Predictor")

# User inputs
brand = st.selectbox('Brand', brand_names).lower()
ram = st.selectbox('RAM (in GB)', [2, 3, 4, 6, 8, 12, 16, 24, 32])
rom_size = st.selectbox('ROM Size (in GB)', [16, 32, 64, 128, 256, 512, 1000, 2000])
screen_size = st.slider('Screen Size (in inches)', 4.0, 8.0, 6.5)
battery_capacity = st.number_input('Battery Capacity (in mAh)', min_value=1000, max_value=9000, step=100, value=5000)
front_camera_mp = st.number_input('Front Camera (in MP)', min_value=0.0, max_value=60.0, step=1.0, value=8.0)
primary_camera_mp = st.number_input('Primary Rear Camera (in MP)', min_value=2.0, max_value=108.0, step=1.0, value=13.0)
total_rear_camera = st.selectbox('Total Rear Cameras', [1, 2, 3, 4])

# When user clicks predict
if st.button('Predict Price'):
    # Create DataFrame for prediction
    input_data = pd.DataFrame([[
        ram, brand, rom_size, screen_size,
        battery_capacity, front_camera_mp, primary_camera_mp, total_rear_camera
    ]], columns=input_columns)

    # Predict
    prediction = pipe.predict(input_data)[0]
    st.success(f"Estimated Selling Price: ₹{int(prediction):,}")


st.markdown(
    """
    <hr style="margin-top: 100px; margin-bottom: 10px">
    <div style="text-align: center; color: gray;">
        <div style="margin: 30px; ">
        <h4>Contact Me</h4>
        <a href="https://github.com/Omkar-109" target="_blank" style="margin: 0 10px; ">
            <img style="background-color:gray; padding:2px; border-radius:2px;" src="https://cdn4.iconfinder.com/data/icons/iconsimple-logotypes/512/github-512.png" width="30"/>
        </a>
        <a href="https://www.kaggle.com/omkarmhamal" target="_blank" style="margin: 0 10px;">
            <img style="background-color:gray; padding:2px; border-radius:2px;" src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-1024.png" width="30"/>
        </a>
        <a href="https://www.linkedin.com/in/omkar-mhamal" target="_blank" style="margin: 0 10px;">
            <img style="background-color:gray; padding:2px; border-radius:2px;" src="https://cdn3.iconfinder.com/data/icons/social-round-corner/512/linkdin__social_media_logo-512.png" width="30"/>
        </a>
        </div>
        <p>This Model is trained on <a style="color:gray;" href="https://www.kaggle.com/datasets/jithinanievarghese/flipkart-smartphones-dataset">Flipkart Smartphone Dataset 2022</a></p>
        <small>© 2025 Smartphone Price Predictor</small>
    </div>
    """,
    unsafe_allow_html=True
)
