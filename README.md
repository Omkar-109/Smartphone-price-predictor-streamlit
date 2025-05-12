# 📱 Smartphone Price Predictor 2025

Welcome to the **Smartphone Price Predictor 2025** - a machine learning-based web application that estimates the selling price of smartphones based on key features. Built with `Scikit-learn`, `Streamlit`, and trained using Flipkart dataset.

---

## 🎥 Demo Video

Check out the demo of the **Smartphone Price Predictor 2025** app in action:

[![Smartphone Price Predictor Demo](https://github.com/user-attachments/assets/424e71d2-dfbf-417d-bc9d-adaa76833315)

---

## 🧠 Problem Statement

In the rapidly evolving smartphone market, customers often face difficulty determining a fair price for a phone based on its specifications. Whether they are purchasing a used phone or comparing options across brands, there's no easy way to estimate what a smartphone should cost.

This project addresses the question:

`💬 "If a customer wants a smartphone with certain features, what is the typical selling price they should expect?"`

Our solution helps both buyers and sellers by providing price estimates based on key features such as RAM, brand, storage, battery life, and camera specifications - giving them a fair understanding of the market price.

---

## ✅ Solution

We built a supervised machine learning regression model that predicts the **expected selling price** of a smartphone using various specifications like:

- Brand
- RAM
- ROM
- Screen Size
- Battery Capacity
- Camera Specifications

The model is trained using data from **Flipkart Smartphone Dataset 2022** and deployed using Streamlit for easy web-based interaction.

---

## 📊 Dataset Used

- **Source**: [Flipkart Smartphone Dataset 2022 (Kaggle)](https://www.kaggle.com/datasets/jithinanievarghese/flipkart-smartphones-dataset)
- Features used for prediction:
  - `ram`, `brand`, `rom_size`, `screen_size`, `battery_capacity`, `front_camera_mp`, `primary_camera_mp`, `total_rear_camera`

---

## 📓 Model Development

You can view the complete notebook used for data cleaning, feature engineering, and model training here:

🔗 **Kaggle Notebook**: [Model Training Notebook](https://www.kaggle.com/code/omkarmhamal/smartphone-price-prediction-by-omkar)

- Techniques Used:
  - Label/One-Hot Encoding for categorical variables (`brand`)
  - Model: `RandomForestRegressor` (Many regression models were tested and `RandomForestRegressor` was selected based on R²)
  - Preprocessing: `ColumnTransformer` + `Pipeline`
  - Evaluation: R² Score, MAE

---

## 🌐 Web App with Streamlit

The app is built using [Streamlit](https://streamlit.io/) to allow users to interactively input phone specifications and get a predicted selling price instantly.

### 🔧 Features

- User selects RAM, brand, ROM size, screen size, and camera specs.
- Output is the predicted price of the smartphone.
- Responsive design, local image assets, and a dark-friendly UI.

---

## 🚀 Live App (Streamlit)

Try out the model live here:  
🌐 [Streamlit App](https://smartphone-price-predictor-2025.streamlit.app)

---

## 🚀 Deployment

To run the app locally:

1. **Clone the repo**
   ```
   git clone https://github.com/yourusername/smartphone-price-predictor-2025.git
   cd smartphone-price-predictor-2025
   ```

2. **Create Conda environment**
   ```
    conda create -n price-predictor python=3.11.11
    conda activate price-predictor
    pip install -r requirements.txt
   ```

3. **Run the app**
   ```
   streamlit run app.py
   ```
