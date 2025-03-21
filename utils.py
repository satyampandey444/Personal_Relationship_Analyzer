import os
import re
import json
import logging
import google.generativeai as genai
from config import API_KEY

# Set up logging
logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Configure the API key for the generative AI model
genai.configure(api_key=API_KEY)

def extract_text_from_chat(uploaded_file):
    """Extract text from a WhatsApp chat export file."""
    try:
        logging.info("Starting text extraction from chat file.")
        text = uploaded_file.read().decode('utf-8')  # Read the text file
        logging.info("Successfully extracted text from chat file.")
        return text
    except Exception as e:
        logging.error(f"Error extracting text from chat file: {e}")
        raise ValueError(f"Failed to extract text from chat file: {e}")

def clean_text(text):
    """Clean the extracted chat text."""
    logging.info("Starting text cleaning.")
    # Remove multiple spaces, newlines, and tabs
    text = re.sub(r'\s+', ' ', text)
    # Remove non-ASCII characters (optional)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    cleaned_text = text.strip()
    logging.info("Text cleaning completed.")
    return cleaned_text

def analyze_chat_toxicity(chat_text):
    """Analyze the chat text for toxicity and relationship metrics."""
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
You are an expert in analyzing relationship dynamics. 
Analyze the following chat text for signs of toxicity, affection, concern, manipulation, and abusive nature for each person separately. 
Also, identify and return the names of the two individuals in the chat. 
Return a JSON response with the following keys:
- "name1": the name of the first person.
- "name2": the name of the second person.
- "toxicity_percentage_person1": numeric score between 0 and 100 indicating the level of toxicity for person 1.
- "affection_score_person1": numeric score between 0 and 100 indicating the level of affection for person 1.
- "concern_score_person1": numeric score between 0 and 100 indicating the level of concern for person 1.
- "manipulation_score_person1": numeric score between 0 and 100 indicating the level of manipulation for person 1.
- "abusive_nature_score_person1": numeric score between 0 and 100 indicating the level of abusive nature for person 1.
- "good_quality_person1": a description of good qualities for person 1.
- "negative_quality_person1": a description of negative qualities for person 1.
- "improvements_person1": suggestions for improvements for person 1.
- "overall_summary_person1": a brief summary of person 1's contributions to the relationship.

- "toxicity_percentage_person2": numeric score between 0 and 100 indicating the level of toxicity for person 2.
- "affection_score_person2": numeric score between 0 and 100 indicating the level of affection for person 2.
- "concern_score_person2": numeric score between 0 and 100 indicating the level of concern for person 2.
- "manipulation_score_person2": numeric score between 0 and 100 indicating the level of manipulation for person 2.
- "abusive_nature_score_person2": numeric score between 0 and 100 indicating the level of abusive nature for person 2.
- "good_quality_person2": a description of good qualities for person 2.
- "negative_quality_person2": a description of negative qualities for person 2.
- "improvements_person2": suggestions for improvements for person 2.
- "overall_summary_person2": a brief summary of person 2's contributions to the relationship.

- "overall_summary": a brief comment 300-500 words on the relationship dynamics.
Respond strictly in JSON format.
Chat text: {chat_text}
"""
    response = model.generate_content(prompt)

    try:
        result = clean_and_parse_json(response.text)
        # Extract names from the result
        name1 = result.get("name1", "Person 1")
        name2 = result.get("name2", "Person 2")
        result["person1_name"] = name1
        result["person2_name"] = name2
        return result
    except Exception as e:
        return {"error": f"Error parsing response: {e}"}

def clean_and_parse_json(text):
    """Clean and parse JSON from the response."""
    cleaned = re.sub(r'^```(?:json)?\s*', '', text.strip(), flags=re.MULTILINE)
    cleaned = re.sub(r'\s*```$', '', cleaned, flags=re.MULTILINE)

    return json.loads(cleaned)

def colored_metric(label, score):
    """Generate a colored metric display for scores."""
    try:
        numeric_score = float(score)
    except:
        numeric_score = None

    if numeric_score is None:
        color = "gray"
        display_value = "N/A"
    elif numeric_score >= 80:
        color = "red"
        display_value = f"{numeric_score:.0f}% "
    elif numeric_score >= 60:
        color = "orange"
        display_value = f"{numeric_score:.0f}%"
    else:
        color = "green"
        display_value = f"{numeric_score:.0f}%"
    
    html = f"""
    <div style="border: 2px solid {color}; border-radius: 5px; padding: 10px; margin: 5px; text-align: center;">
        <div style="font-weight: bold; margin-bottom: 4px;">{label}</div>
        <div style="font-size: 24px; color: {color};">{display_value}</div>
    </div>
    """
    return html