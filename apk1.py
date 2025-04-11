import streamlit as st
import openai
import os

# Set your OpenAI API key (replace with your actual key or use environment variables)
# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"  # Or set it directly below (less secure)
openai.api_key = os.getenv("OPENAI_API_KEY") # Recommended: Get API key from environment variables

def code_review(code, language):
    """Reviews the given code using OpenAI's API."""

    prompt = f"""
    Review the following {language} code and provide feedback on:

    - Code correctness and potential bugs
    - Code style and readability
    - Potential performance issues
    - Security vulnerabilities (if applicable)
    - Best practices and suggestions for improvement

    ```python
    {code}
    ```
    """

    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Or another suitable model like "text-davinci-003"
            prompt=prompt,
            max_tokens=500,  # Adjust as needed
            n=1,
            stop=None,
            temperature=0.5, # Adjust for creativity vs. correctness
        )
        review = response.choices[0].text.strip()
        return review
    except Exception as e:
        return f"Error during code review: {e}"



st.title("AI Code Reviewer")

code_input = st.code_area("Enter your code here", height=300)
language = st.selectbox("Select programming language", ["Python", "JavaScript", "Java", "C++", "C#", "Go", "Ruby", "PHP", "Swift", "Kotlin"]) # Add more languages as needed
# language = st.text_input("Enter the programming language (e.g., Python, JavaScript)") # Alternative if you want free text input

if st.button("Review Code"):
    if not code_input:
        st.warning("Please enter some code to review.")
    else:
        with st.spinner("Reviewing your code..."):
            review_result = code_review(code_input, language)
            st.subheader("Code Review:")
            st.write(review_result)


# Optional: Add more features like:
# - Uploading code files
# - Displaying code diffs
# - Saving reviews
# - User authentication
# - Integration with GitHub or other code repositories
