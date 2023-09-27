import streamlit as st
import validators
import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

# Streamlit app title and description
st.title("Web Content Summarizer")
st.write("Enter a URL to generate a summary of its content.")

# User input for the URL
url = st.text_input("Enter a URL:", "")

# Function to validate a URL
def is_valid_url(url):
    if validators.url(url):
        return True
    else:
        return False

# Function to extract and summarize web content
def summarize_web_content(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the text content from the page
        page_content = soup.get_text()

        # Generate a summary of the content
        summary = summarize(page_content)

        # Display the summary
        st.subheader("Generated Summary:")
        st.write(summary)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Button to trigger content summarization and URL validation
if st.button("Summarize Content"):
    if url:
        if is_valid_url(url):
            summarize_web_content(url)
        else:
            st.error("Invalid URL. Please enter a valid URL.")
    else:
        st.warning("Please enter a URL.")

# Display a footer
st.write("Jeetendra")
