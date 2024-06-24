import streamlit as st
import PyPDF2
import ollama

# Title of the app
st.title("🤖 Tech Guru \n### Your Career Guidance Expert!")

# Initialize session state for conversation history and resume analysis
if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I assist you with your career today?"}]
if 'resume_analysis' not in st.session_state:
    st.session_state.resume_analysis = ""
if 'resume_uploaded' not in st.session_state:
    st.session_state.resume_uploaded = False

# Upload resume
uploaded_file = st.file_uploader("Upload your resume (PDF or text)", type=["pdf", "txt"])

if uploaded_file and not st.session_state.resume_uploaded:
    if uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        resume_text = "".join([page.extract_text() for page in pdf_reader.pages])
    else:
        resume_text = uploaded_file.read().decode("utf-8")
    
    st.session_state.resume_analysis = resume_text
    st.session_state.resume_uploaded = True  # Mark as uploaded to prevent re-processing

    st.session_state.messages.append({
        "role": "assistant",
        "content": "Thank you for uploading your resume. I will analyze it and provide feedback shortly."
    })
    st.chat_message("assistant", avatar="🤖").write(st.session_state.messages[-1]["content"])

    # Analyze resume
    with st.spinner("Analyzing resume..."):
        analysis_response = ollama.chat(model='gemma:2b', messages=[
            {"role": "user", "content": f"Analyze this resume:\n\n{resume_text}"}
        ])
        analysis_text = analysis_response['message']['content']
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": f"Here's the analysis of your resume:\n\n{analysis_text}"
    })
    st.chat_message("assistant", avatar="🤖").write(st.session_state.messages[-1]["content"])

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message(msg["role"], avatar="🧑‍💻").write(msg["content"])
    else:
        st.chat_message(msg["role"], avatar="🤖").write(msg["content"])

# Define a function to generate a response with prompt engineering and spinner
def generate_response(prompt):
    # Keywords related to career guidance
    career_keywords = ["career", "job", "linkedin", "resume", "cv", "interview", "salary", "application", "networking", "cover letter", "job search", "job hunting", "job application", "professional", "employment"]

    # Check if the question is career-related
    if any(keyword in prompt.lower() for keyword in career_keywords):
        # Create a context-rich prompt for the model
        prompt_with_context = f"""Context: You are a highly knowledgeable career assistant. Your task is to provide insightful advice on career guidance, job search strategies, LinkedIn profile optimization, and resume feedback.
        User Query: {prompt} Please provide a detailed and helpful response."""

        with st.spinner("Generating response..."):
            response = ollama.chat(model='gemma:2b', stream=False, messages=[{"role": "user", "content": prompt_with_context}])
            return response['message']['content']
    else:
        # Response for non-relevant questions
        return "I'm here to assist with career guidance, job search, LinkedIn optimization, and related topics. Please ask a relevant question about your career or job search."

# Input for user query
if prompt := st.chat_input("Ask me anything about your career, job search, or LinkedIn optimization!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="🧑‍💻").write(prompt)
    
    # Generate response based on the filtered input
    response_content = generate_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response_content})
    st.chat_message("assistant", avatar="🤖").write(response_content)
