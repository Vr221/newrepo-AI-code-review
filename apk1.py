import streamlit as st
import google.generativeai as genai
import os

# API Key setup (env or Streamlit Secrets)
api_key = st.secrets["GEMINI_API_KEY"] if "GEMINI_API_KEY" in st.secrets else os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("❌ Gemini API key not found. Please set GEMINI_API_KEY in Streamlit secrets or environment.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

# Streamlit UI
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
            prompt = (
                "You are an expert Python code reviewer.\n"
                "Please review the following Python code and provide:\n"
                "- Syntax or logic issues\n"
                "- Suggestions for improvement\n"
                "- Code readability and performance tips\n"
                "- A corrected version if needed\n\n"
                f"Code:\n```python\n{code_input}\n```"
            )
            try:
                response = model.generate_content(prompt)
                st.subheader("🧠 AI Review Result")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error while analyzing code: {e}")
