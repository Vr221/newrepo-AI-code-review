import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
import ast

load_dotenv()

# Configure API key, handle possible missing key
try:
    genai.configure(api_key=os.getenv("GAIzaSyAYBSadaJEhspMTinbki7HCjG5q4nV_6ao"))
except Exception as e:
    st.error(f"Error configuring Gemini API: {e}")
    st.stop()

# Streamlit UI
st.title("🕵🏽‍♂️ Python Code Reviewer")
st.write("Review your Python code here to detect bugs and receive suggested fixes!")

# User Input
code_input = st.text_area("Paste your Python code here:", height=200)

if st.button("Review Code"):
    if code_input.strip():
        # Validate if the input is valid python code
        try:
            ast.parse(code_input)
        except SyntaxError as e:
            st.error(f"⚠️ Invalid Python code: {e}")
            st.stop()

        with st.spinner("Reviewing your code... ⏳"):
            user_prompt = f"""
            You are a professional Python code reviewer.
            - Analyze the following Python code for **errors, inefficiencies, and improvements**.
            - Provide a **bug report** with explanations.
            - Give a **fully corrected version** of the code.

            Here is the user's code:
            ```python
            {code_input}
            ```

            Please return the response in **Markdown format** with:
            - A "Bug Report" section listing errors and explanations.
            - A "Fixed Code" section containing the corrected Python code inside a Markdown block.

            For example:

            Bug Report:
            - Error 1: ... explanation ...
            - Error 2: ... explanation ...

            Fixed Code:

            ```python
            # corrected code here
            ```
            """

            try:
                # Initialize the model inside the button click to avoid initialization on every run
                model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp") # Or "gemini-2.0-flash"

                response = model.generate_content(user_prompt)

                st.subheader("🔍 AI Code Review Report")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred during code review: {e}")

    else:
        st.warning("⚠️ Please enter Python code before submitting.")
