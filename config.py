import os
from dotenv import load_dotenv

# Load environment variables from .env files
if os.path.exists('.env.development'):
    load_dotenv('.env.development')
else:
    load_dotenv('.env')

# Get the API key from environment variables
API_KEY = os.getenv("GEMINI_API_KEY")  # Ensure this matches your .env file

# Define styles for the Streamlit app
STYLES = """
    <style>
    /* General body styling */
    body {
        font-family: 'Arial', sans-serif; /* Use a clean sans-serif font */
        background-color: #f9f9f9; /* Light background for better contrast */
        color: #333; /* Dark text for readability */
        line-height: 1.6; /* Improve line spacing for readability */
    }

    /* Button hover styling */
    div.stButton > button:hover {
         background-color: #ff4d4d; /* Change to a red color for toxicity theme */
         color: white;
    }
    /* Link hover styling */
    a:hover {
         color: #ff4d4d; /* Change to a red color for toxicity theme */
         text-decoration: underline;
    }
    
    div.stButton > button[type="submit"] {
        border: 2px solid #ff4d4d; /* Change to a red color for toxicity theme */
        border-radius: 4px;
        background-color: white; /* or any background color you prefer */
        color: #ff4d4d; /* Change to a red color for toxicity theme */
        padding: 0.5rem 1rem; /* Add padding for better button size */
        font-weight: bold; /* Bold text for buttons */
        transition: background-color 0.3s, color 0.3s; /* Smooth transition */
    }

    div.stFormSubmitButton > button[type="submit"]:hover {
        background-color: #ff4d4d; /* Change to a red color for toxicity theme */
        color: white;
    }

    /* Container styling */
    .container {
        max-width: 800px; /* Limit the width of the container */
        margin: auto; /* Center the container */
        padding: 20px; /* Padding around the container */
        background-color: white; /* White background for the container */
        border-radius: 8px; /* Rounded corners */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    /* Header styling */
    h1, h2, h3 {
        color: #ff4d4d; /* Use the toxicity theme color for headers */
    }

    /* Footer styling */
    footer {
        text-align: center; 
        color: #888888; 
        font-size: 12px; 
        margin-top: 20px; /* Space above footer */
    }
    </style>
"""

STYLE_SUBMIT_BUTTON = """
<style>
div.stFormSubmitButton > button {
    border: 2px solid #ff4d4d; /* Change to a red color for toxicity theme */
    border-radius: 4px;
    color: #ff4d4d; /* Change to a red color for toxicity theme */
    padding: 0.5rem 1rem; /* Padding for buttons */
    font-weight: bold; /* Bold text for buttons */
    transition: background-color 0.3s, color 0.3s; /* Smooth transition */
}
div.stFormSubmitButton > button:hover {
    background-color: #ff4d4d; /* Change to a red color for hover */
    color: white; /* White text on hover */
}
</style>
"""

FOOTER_STYLE = """
<div style='text-align: center; color: #888888; font-size: 12px; margin-top: 20px;'>
    &copy; 2025 Relationship Toxicity Analyzer. Built by Satyam Pandey. All rights reserved.
</div>
"""