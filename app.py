import streamlit as st

st.title("Chikadee: Pipeline Optimization App")
st.write("Welcome to the Chikadee GIS optimization demo!")
from pyngrok import ngrok

# Replace YOUR_AUTHTOKEN_HERE with your actual token (in quotes)
ngrok.set_auth_token("2wgODi3cZxcrjP37QJ5F5m4mnAR_7v5pFhKVFVzhzvQCMStqg")
import os
from pyngrok import ngrok

# Start Streamlit app in the background
os.system("streamlit run app.py &")

# Open a tunnel to the app
public_url = ngrok.connect(8501)
print(f"✅ Streamlit app is live at: {public_url}")
