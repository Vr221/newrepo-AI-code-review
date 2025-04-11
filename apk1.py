import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyAYBSadaJEhspMTinbki7HCjG5q4nV_6ao")

# Set your API Key here (recommended: use environment variable in production)
genai.configure(api_key=st.secrets["AIzaSyAYBSadaJEhspMTinbki7HCjG5q4nV_6ao"])  # Secure way via Streamlit Secrets
model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="AI Python Code Reviewer", layout="centered")
st.title("🤖 AI-Based Python Code Reviewer")
st.write("Paste your Python code below and get a detailed AI-generated review.")

# Code input
code_input = st.text_area("Enter your Python Code:", height=300, placeholder="e.g. def add(a, b): return a + b")

# Review button
if st.button("🔍 Review Code"):
    if not code_input.strip():
        st.warning("Please enter some Python code.")
    else:
        with st.spinner("Analyzing your code with Gemini AI..."):
            prompt = f"""
You are an expert Python code reviewer.
Please review the following Python code and provide:
- Syntax or logic issues
- Suggestions for improvement
- Code readability and performance tips
- A corrected version if needed

Code:
```python
{code_input}
