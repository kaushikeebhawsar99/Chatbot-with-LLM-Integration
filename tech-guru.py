import streamlit as st
import httpx

# Function to test connectivity to a given URL
def test_connectivity(url):
    try:
        response = httpx.get(url)
        if response.status_code == 200:
            return f"Successfully connected to {url}!"
        else:
            return f"Failed to connect to {url}. Status code: {response.status_code}"
    except Exception as e:
        return f"Failed to connect to {url}. Error: {str(e)}"

# Title of the app
st.title("🤖 Tech Guru \n### Your Career Guidance Expert!")

# Button to test connectivity to Google
if st.button("Test Google Connectivity"):
    connectivity_result = test_connectivity("https://www.google.com")
    st.write(connectivity_result)

# Button to test connectivity to ollama API
if st.button("Test Ollama API Connectivity"):
    connectivity_result = test_connectivity("https://api.ollama.com/health")  # Replace with the correct ollama API URL
    st.write(connectivity_result)

# Rest of your Streamlit app code here
# ...
