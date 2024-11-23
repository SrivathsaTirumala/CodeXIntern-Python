import streamlit as st
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    polarity = sentiment.polarity

    if polarity > 0:
        sentiment_category = 'Positive'
    elif polarity < 0:
        sentiment_category = 'Negative'
    else:
        sentiment_category = 'Neutral'

    return sentiment_category

st.title("Sentiment Detection Analyzer")
text = st.text_input("Enter your text:")

if st.button("Analyze Sentiment"):
    if text.strip():
        result = analyze_sentiment(text)
        if result == 'Positive':
            st.success(f"The sentiment is: **{result}** 😊")
        elif result == 'Negative':
            st.warning(f"The sentiment is: **{result}** 😔")
        else:
            st.info(f"The sentiment is: **{result}** 😐")
    else:
        st.warning("Please enter some text to analyze.")


# To run this code, use : python3 -m streamlit run sentiment_detection_app.py (or) streamlit run sentiment_detection_app.py
