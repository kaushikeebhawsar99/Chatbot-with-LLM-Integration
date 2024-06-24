import streamlit as st
import httpx

# Function to test connectivity to the ollama API
def test_ollama_connectivity():
    try:
        response = httpx.get("https://api.ollama.com/health")  # Replace with a simple endpoint if available
        if response.status_code == 200:
            return "Successfully connected to the ollama API!"
        else:
            return f"Failed to connect to the ollama API. Status code: {response.status_code}"
    except Exception as e:
        return f"Failed to connect to the ollama API. Error: {str(e)}"

# Title of the app
st.title("🤖 Tech Guru \n### Your Career Guidance Expert!")

# Button to test API connectivity
if st.button("Test API Connectivity"):
    connectivity_result = test_ollama_connectivity()
    st.write(connectivity_result)

# Rest of your Streamlit app code here
# ...
