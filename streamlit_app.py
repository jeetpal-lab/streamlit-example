import streamlit as st
import requests
from bs4 import BeautifulSoup

# Streamlit app title and description
st.title("Web Content Extractor")
st.write("Enter a URL and click the button to extract its content.")

# User input for the URL
url = st.text_input("Enter a URL:", "")

# Function to extract and display web content
def extract_content(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the text content from the page
        page_content = soup.get_text()

        # Display the extracted content
        st.subheader("Extracted Content:")
        st.write(page_content)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Button to trigger content extraction
if st.button("Extract Content"):
    if url:
        extract_content(url)
    else:
        st.warning("Please enter a valid URL.")

# Display a footer
st.write("Created by Jeetendra")

