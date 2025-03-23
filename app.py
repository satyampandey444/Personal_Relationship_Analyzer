import streamlit as st
import re 
import logging
from utils import (
    extract_text_from_chat,
    clean_text,
    analyze_chat_toxicity,
)
from config import STYLES, FOOTER_STYLE, STYLE_SUBMIT_BUTTON
from utils import colored_metric, colored_metric_positive,validate_chat

# Initialize session state variables
if "valid" not in st.session_state:
    st.session_state["valid"] = True

if "done" not in st.session_state:
    st.session_state["done"] = False

if "analysis_result" not in st.session_state:
    st.session_state["analysis_result"] = {}

if "comments" not in st.session_state:
    st.session_state["comments"] = ""

if "name1" not in st.session_state:
    st.session_state["name1"] = ""

if "name2" not in st.session_state:
    st.session_state["name2"] = ""

st.set_page_config(
    page_title="Personal Relationship Analyzer",
    page_icon="💔",
    layout="wide",
    initial_sidebar_state="auto"
)

st.markdown(STYLES, unsafe_allow_html=True)

# Header Section
st.title("Personal Relationship Analyzer")
st.markdown("### Analyze your WhatsApp chats for Healthier Relationship using Artificial Intelligence")
st.markdown("### Explore the status of your relationship ☠️")
st.markdown(
    """##### Built by <a href="https://www.linkedin.com/in/satyam-pandey-66449b230/" target="_blank">Satyam Pandey</a> &amp; <a href="https://www.linkedin.com/in/drpandit69/" target="_blank">Subrahmanyam</a> #####""",
    unsafe_allow_html=True
)
st.markdown("---")

# Main Container
x = st.empty()
main_container = x.form("main_form", enter_to_submit=False, clear_on_submit=True)

def check_data():
    if st.session_state["file"] is None:
        st.error("Please upload a valid WhatsApp chat export to proceed.")
        return

    # Extract and clean text from the uploaded chat file
    chat_text = extract_text_from_chat(st.session_state['file'])
    clean_text_val = clean_text(chat_text)

    # Validate the chat text
    is_valid, comments = validate_chat(clean_text_val)

    if not is_valid:
        st.session_state['comments'] = comments
        st.session_state['valid'] = False
        # st.error(comments)  # Display the error message to the user
        return  # Exit the function if the chat is not valid

    # Analyze the chat for toxicity if valid
    analysis_result = analyze_chat_toxicity(clean_text_val)
    
    st.session_state["analysis_result"] = analysis_result
    st.session_state['valid'] = True
    st.session_state['done'] = True

def back_to_main():
    st.session_state["valid"] = True
    st.session_state["done"] = False
    st.session_state["comments"] = ""
    st.session_state["analysis_result"] = {}
    st.session_state["name1"] = ""
    st.session_state["name2"] = ""
    x.empty()

# User Input Section
if st.session_state["valid"] and not st.session_state["done"]:
    st.markdown(STYLE_SUBMIT_BUTTON, unsafe_allow_html=True)
    with main_container:
        st.subheader("📂 Upload Your WhatsApp Chat Export")
        uploaded_file = st.file_uploader("Choose a .txt file", type="txt", key="file")

        if uploaded_file is not None:
            st.success("File uploaded successfully! Click 'Analyze Chat' to proceed.")
        col_left, col_right = st.columns([7, 1])
        with col_right:
            analyze_button = st.form_submit_button("🔍 Analyze Chat", on_click=check_data)
elif((st.session_state["valid"])==False):

    x.empty()
    comments=st.session_state["comments"]
    st.write("# 🚫 Invalid Whatsapp Chats")
    st.error(f'{comments} Please upload a valid chats to proceed.')
    button = st.button("Back to main page",on_click=back_to_main)
                       


# Results Section
elif st.session_state["valid"] and st.session_state["done"]:
    x.empty()
    analysis = st.session_state.get("analysis_result", {})
    name1 = analysis.get("person1_name", st.session_state["name1"])
    name2 = analysis.get("person2_name", st.session_state["name2"])

    st.markdown("## Chat Analysis Dashboard")
    st.markdown("### Personal and Overall Relationship Analysis")

    # Retrieve scores for person 1
    toxicity_percentage_person1 = analysis.get("toxicity_percentage_person1", "N/A")
    affection_score_person1 = analysis.get("affection_score_person1", "N/A")
    concern_score_person1 = analysis.get("concern_score_person1", "N/A")
    manipulation_score_person1 = analysis.get("manipulation_score_person1", "N/A")
    abusive_nature_score_person1 = analysis.get("abusive_nature_score_person1", "N/A")
    overall_summary_person1 = analysis.get("overall_summary_person1", "N/A")

    # Retrieve scores for person 2
    toxicity_percentage_person2 = analysis.get("toxicity_percentage_person2", "N/A")
    affection_score_person2 = analysis.get("affection_score_person2", "N/A")
    concern_score_person2 = analysis.get("concern_score_person2", "N/A")
    manipulation_score_person2 = analysis.get("manipulation_score_person2", "N/A")
    abusive_nature_score_person2 = analysis.get("abusive_nature_score_person2", "N/A")
    overall_summary_person2 = analysis.get("overall_summary_person2", "N/A")

    # Display scores for person 1
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### {name1} Scores")
        st.markdown(colored_metric(f"{name1} Toxicity Percentage", toxicity_percentage_person1), unsafe_allow_html=True)
        st.markdown(colored_metric_positive(f"{name1} Affection Percentage", affection_score_person1), unsafe_allow_html=True)
        st.markdown(colored_metric_positive(f"{name1} Concern Percentage", concern_score_person1), unsafe_allow_html=True)
        st.markdown(colored_metric(f"{name1} Manipulation Percentage", manipulation_score_person1), unsafe_allow_html=True)
        st.markdown(colored_metric(f"{name1} Abusive Nature Percentage", abusive_nature_score_person1), unsafe_allow_html=True)
        
        # Display detailed analysis for person 1
        st.markdown(f"### {name1} Analysis")
        st.markdown(f"**Good Quality:** {analysis.get('good_quality_person1', 'N/A')}")
        st.markdown(f"**Negative Quality:** {analysis.get('negative_quality_person1', 'N/A')}")
        st.markdown(f"**Improvements:** {analysis.get('improvements_person1', 'N/A')}")
        st.markdown(f"**Overall Summary:** {overall_summary_person1}")

    # Display scores for person 2
    with col2:
        st.markdown(f"### {name2} Scores")
        st.markdown(colored_metric(f"{name2} Toxicity Percentage", toxicity_percentage_person2), unsafe_allow_html=True)
        st.markdown(colored_metric_positive(f"{name2} Affection Percentage", affection_score_person2), unsafe_allow_html=True)
        st.markdown(colored_metric_positive(f"{name2} Concern Percentage", concern_score_person2), unsafe_allow_html=True)
        st.markdown(colored_metric(f"{name2} Manipulation Percentage", manipulation_score_person2), unsafe_allow_html=True)
        st.markdown(colored_metric(f"{name2} Abusive Nature Percentage", abusive_nature_score_person2), unsafe_allow_html=True)
        
        # Display detailed analysis for person 2
        st.markdown(f"### {name2} Analysis")
        st.markdown(f"**Good Quality:** {analysis.get('good_quality_person2', 'N/A')}")
        st.markdown(f"**Negative Quality:** {analysis.get('negative_quality_person2', 'N/A')}")
        st.markdown(f"**Improvements:** {analysis.get('improvements_person2', 'N/A')}")
        st.markdown(f"**Overall Summary:** {overall_summary_person2}")

    # Overall Relationship Summary
    overall_summary = analysis.get("overall_summary", "No summary available.")
    st.markdown("### Overall Relationship Summary")
    st.write(overall_summary)

    with st.container():
        col_space, col_buttons = st.columns([8, 2])
        with col_buttons:
            st.button("Try another chat", on_click=back_to_main)

st.markdown("---")
st.markdown(FOOTER_STYLE, unsafe_allow_html=True)
