import streamlit as st
import joblib
import numpy as np
import google.generativeai as genai

# Load the trained model
model = joblib.load('hackathon\crop_price_predictor.pkl')  # Path to your saved model file

# Google Gemini API Configuration
GOOGLE_API_KEY = "AIzaSyBUBSsMaZPlM04VZ-4P4knEFCLvnAHBZwo"
genai.configure(api_key=GOOGLE_API_KEY)

# Function to get Gemini AI responses
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt, stream=True)
    return response

# Function to make predictions
def predict_crop_price(input_data):
    input_array = np.array(input_data).reshape(1, -1)  # Reshape for a single sample
    prediction = model.predict(input_array)
    return prediction[0]

# Streamlit app configuration
st.set_page_config(page_title="AgrI - Plant Disease Detection & Crop Price Prediction", layout="wide")

# Background and custom CSS styling
background_image_url = "https://media.istockphoto.com/id/844226534/photo/leaf-background.jpg?s=612x612&w=0&k=20&c=N4NPPNXFU5hPcThEbQ-wr4y64pqSKm-x5AMDZ0sPL5w="

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url("{background_image_url}");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(255, 255, 255, 1);
}}
[data-testid="stSidebar"] {{
background-color: #2b2b2b; 
color: white; 
border-radius: 15px;
padding: 10px;
box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.5);
}}
.st-subheader {{
background-color: rgba(255, 255, 255, 1); 
border-radius: 15px;
padding: 15px;
box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["About Us", "Crop Price Prediction", "AI Expert Chat"])

if section == "About Us":
    st.markdown("""
    <h1 style="text-align: center; font-size: 4em; font-weight: bold;">
        <span style="color: white;">A</span><span style="color: black;">gr</span><span style="color: white;">I</span>
    </h1>
    """, unsafe_allow_html=True)
    st.markdown('<h1 style="text-align: center; font-size: 3em; font-weight: bold;">About Us</h1>', unsafe_allow_html=True)
    st.markdown("""
    Welcome to *AgrI*, your trusted companion in modern agriculture. 
    Our mission is to empower farmers with cutting-edge technology for effective plant care.

    ### Features:
    - Disease Detection: Upload an image of your plant leaf, and our AI model will identify potential diseases.
    - Expert Advice: Get comprehensive guidance tailored to detected plant diseases, powered by Gemini AI.
    - Crop Price Prediction: Input soil, weather, and other features to predict crop prices.
    """)

elif section == "Crop Price Prediction":
    st.markdown('<h1 style="text-align: center; font-size: 3em; font-weight: bold;">Crop Price Prediction</h1>', unsafe_allow_html=True)
    
    # Collecting user input
    N_SOIL = st.number_input("Crop ", value=0.0)
    P_SOIL = st.number_input("Cost cultivation", value=0.0)
    K_SOIL = st.number_input("Machinery Cost", value=0.0)
    TEMPERATURE = st.number_input("Production", value=0.0)
    HUMIDITY = st.number_input("Yield", value=0.0)
    ph = st.number_input("Tempature", value=0.0)
    RAINFALL = st.number_input("Annual Rainfall (mm)", value=0.0)

    # Button to get prediction
    if st.button("Predict Crop Price"):
        # Prepare the input data for prediction
        input_data = [N_SOIL, P_SOIL, K_SOIL, TEMPERATURE, HUMIDITY, ph, RAINFALL]
        
        # Predict crop price
        predicted_price = predict_crop_price(input_data)
        
        # Display the result
        st.subheader(f"Predicted Crop Price: {predicted_price}")
        
elif section == "AI Expert Chat":
    st.markdown('<h1 style="text-align: center; font-size: 3em; font-weight: bold;">AI Expert Chat</h1>', unsafe_allow_html=True)
    st.sidebar.header("Ask the AI Expert")
    input_question = st.sidebar.text_input("Type your question here:", key="chat_input")
    submit_chat = st.sidebar.button("Ask")

    if submit_chat and input_question:
        st.subheader("AI Response")
        response = get_gemini_response(input_question)
        for chunk in response:
            st.write(chunk.text)