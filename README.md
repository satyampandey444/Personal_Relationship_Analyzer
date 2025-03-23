# Personal Relationship (WhatsApp Chats) Analyzer 

The Personal Relationship Analyzer is an intelligent tool designed to assess and enhance relationships. It assigns a relationship score based on various emotional, behavioral, and communication factors. The system provides significant improvement suggestions, helping individuals identify key areas that need attention and growth. Additionally, it generates a comprehensive summary, offering valuable insights into the overall health of the relationship.

By leveraging this tool, users can gain a deeper understanding of their relationships, recognize strengths and weaknesses, and take actionable steps to foster stronger, more meaningful connections. Whether for personal reflection or relationship growth, this analyzer serves as a helpful guide in building healthier and more fulfilling bonds.


![](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWZteTFwYXF5cHRtOW4zcnVzdGRvcmtnNDF0ZGI2amJ3OWxsNzZpOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6RwS1c3u6cVrs2d4n6/giphy.gif)

## Features
- **Chat Validation**: Ensures the uploaded file is a valid WhatsApp chat export.
- **Overall Relationship Score**: Numeric score between 0 and 100 indicating the overall health of the relationship.
  - **Toxicity Score**
  - **Affection Score**
  - **Concern Score**
  - **Work Experience Score**
  - **Manipulation Score**
  - **Abusive Nature Score**
- **Best Relationship Type Prediction**: dentifies the nature of the relationship (e.g., Healthy, Strained, Toxic, Supportive, etc.).
- **Detailed Summary & Suggestions:**: Provides an insightful overview and practical improvement tips.
    - **Positive Aspects**
  - **Negative Aspects**
  - **Concern Score**
  - **Improvement Suggestions**
  - **Overall Summary**




## Installation

### Clone the Repository
```sh
git clone https://github.com/satyampandey444/Personal_Relationship_Analyzer.git
cd personal_relationship_analyzer
```

### Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file for sensitive API keys

#### Example `.env` file:
```ini
API_KEY=your_gemini_api_key_here
```
#### To retrieve your Gemini API Key for Free

[Click this Link](https://aistudio.google.com/app/apikey)

Go to Create an API key and Create the API Key and then copy it, after that paste it in your .env file in the place of your_gemini_api_key_here



## Usage

### Start the Application
```sh
streamlit run app.py
```

### Interact with the App
- Export your whatsapp chats.
- To export open the profile of the person whose chats you want to analyze.
- After then scroll down you will get the option of export chats.
- Unzip the exported chats you will get the chats.txt file,file must be in txt format.
- Upload the **chats.txt** file to the personal_relationship_analyzer.
- Click on **Analyze** it will generate the report now enjoy.
- Scroll down and click on try another chat to get the analysis of another chat.

## Folder Structure
```
personal_relationship_analyzer/
├── app.py                   # Main Streamlit application
├── utils.py                 # Utility functions for text extraction, validation, and analysis
├── config.py                # Handles configurations and environment variables
├── requirements.txt         # List of dependencies
├── README.md                # Project documentation
├── .env                     # Public environment config
```



## Acknowledgements

- **Streamlit** for providing an easy-to-use web framework.
- **Gemini API** for resume analysis capabilities.

