import streamlit as st
import joblib
import re

# -----------------------------------------------------------
# Load Model and Vectorizer
# -----------------------------------------------------------
@st.cache_resource
def load_model_and_vectorizer():
    model = joblib.load("spam_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_model_and_vectorizer()

# -----------------------------------------------------------
# Preprocessing Function
# -----------------------------------------------------------
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

# -----------------------------------------------------------
# Streamlit UI
# -----------------------------------------------------------
st.set_page_config(page_title="Spam Mail Prediction", page_icon="📧", layout="centered")

st.title("📧 Spam Mail Prediction")


# Input box
user_input = st.text_area("✉️ Enter the message:", height=200)

# Predict button
if st.button("🔍 Predict"):
    if not user_input.strip():
        st.warning("Please enter some text before predicting.")
    else:
        clean_text = preprocess_text(user_input)
        input_vector = vectorizer.transform([clean_text])
        prediction = model.predict(input_vector)[0]

        if prediction == 1:
            st.error("🚨 **SPAM!**")
        else:
            st.success("✅  **NOT SPAM**")
