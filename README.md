# 🤖 Tech Guru - Your Career Guidance Expert!

### Youtube tutorial - https://www.youtube.com/watch?v=ixM8SwYN8Ic

## Overview

Tech Guru is a chatbot designed to assist users with their career-related queries. It leverages the power of Large Language Models (LLMs) to provide insightful advice on career guidance, job search strategies, LinkedIn profile optimization, and resume feedback. The application is built using Streamlit for the frontend and integrates the Ollama API for natural language processing.

## Features

- **Resume Analysis**: Upload your resume in PDF or text format to receive detailed feedback and suggestions.
- **Career Guidance**: Ask questions related to job search, career strategies, LinkedIn profile optimization, and more.
- **Interactive Chat Interface**: Engage in a conversation with the chatbot to receive personalized advice.

## Domain Selection

The domain selected for this application is **Career Guidance**. The primary user base includes job seekers, professionals looking to optimize their LinkedIn profiles, and individuals seeking career advice. The application helps users by providing detailed feedback on their resumes, offering job search strategies, and answering career-related queries.

## Technology Stack

- **Frontend**: Streamlit
- **Backend**: Ollama API for LLM integration
- **Libraries**: PyPDF2 for PDF processing

## Installation & Setting up Enviroment

### 1. Ollama

Ollama is a platform offering customizable generative AI models for various applications.

#### Setting up Ollama

1. **Download Ollama**: Visit the [Ollama GitHub page](https://github.com/Ollama/llama3) and download the installer for your OS.
2. **Install Ollama**: Run the downloaded `OllamaSetup.exe` and follow the prompts to install **(Here i have installed for Windows)**.
3. **Check Installation**: Ensure Ollama is installed in your Programs folder in `C:\Users`.
4. **Serve Model**: Open a  command prompt and execute:
   ```sh
   ollama serve
   ```
### 2. Setup the virtual environment
1. Open a terminal, go to your project directory, and create a virtual environment using command:
    ```sh
    python -m venv .venv
    ```
2. Activate the virtual environment
    ```sh
    .venv\Scripts\activate
    ```
3. Now, create a requirements.txt file and paste the following content:
    ```sh
    streamlit
    PyPDF2
    ollama
    ```
### 3. Clone the repository in your project directory
1. Clone the repository in your project directory:
    ```bash
    git clone https://github.com/kaushikeebhawsar99/Chatbot-with-LLM-Integration.git
    cd Chatbot-with-LLM-Integration
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
    (make sure your .venv is in active mode)
## Running the Application: "tech-guru.py"

To run the application, execute the following command:
```bash
streamlit run tech-guru.py
```
Now your app is running on the port: 
```
localhost:8510
```
Streamlit will open the browser automatically and the app is running on: http://localhost:8510

## Usage
1. **Upload Resume**: Upload your resume in PDF or text format. The chatbot will analyze the resume and provide detailed feedback.
2. **Ask Questions**: Use the chat interface to ask any career-related questions. The chatbot will provide relevant and detailed responses.

## Evaluation and Testing
The application has been tested with a variety of queries to ensure its performance, accuracy, and usability. Below are some example queries:

1. "How can I improve my LinkedIn profile?"
2. "What should I include in my cover letter?"
3. "Can you review my resume and provide feedback?"
4. "What are some job search strategies?"