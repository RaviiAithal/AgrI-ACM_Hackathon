# AgrI - Plant Disease Detection & Crop Price Prediction

AgrI is an innovative solution for modern agriculture, providing farmers with tools to detect plant diseases, predict crop prices, and get expert advice. This web application, built using Streamlit, leverages AI models to empower farmers with valuable insights.

## Features:
1. **Crop Price Prediction**: 
   - Predict the price of crops based on input features such as soil conditions, temperature, humidity, and rainfall.
   
2. **Plant Disease Detection**:
   - Upload an image of a plant leaf, and the model will identify any diseases affecting the plant.
   
3. **AI Expert Chat**:
   - Chat with an AI expert for personalized advice about crop management, disease prevention, and more.

## Prerequisites:
- Python 3.7 or higher
- Required libraries:
  - `streamlit`
  - `joblib`
  - `numpy`
  - `google-generativeai`

To install the required libraries, use the following command:

```bash
pip install streamlit joblib numpy google-generativeai
```

## How to Use:
1. **Clone the repository**:
   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/RaviiAithal/AgrI-ACM_Hackathon
   cd <project_directory>
   ```

2. **Download the trained model**:
   Ensure you have the `crop_price_predictor.pkl` model file saved in the `hackathon` directory.

3. **Set up Google Gemini API**:
   Configure the Google Gemini API key in the script. Replace `GOOGLE_API_KEY` with your actual API key:

   ```python
   GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
   ```

4. **Run the app**:
   Start the Streamlit app by running the following command in the project directory:

   ```bash
   streamlit run app.py
   ```

5. **Access the app**:
   Once the app is running, you can open your browser and navigate to `http://localhost:8501` to use the application.

## Application Sections:

### Crop Price Prediction:
- Users can input features such as soil conditions (N, P, K), temperature, humidity, pH, and rainfall to predict crop prices.

### AI Expert Chat:
- Users can ask questions about agriculture, and the app will provide responses from the AI expert powered by Google Gemini.
