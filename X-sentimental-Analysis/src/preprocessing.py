import sys
import os

# Fix module path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import matplotlib.pyplot as plt
from src.vader_model import get_vader_sentiment

st.title("X Sentiment Analysis Dashboard")

# Text input box
text = st.text_area("Enter a post")

# Run only when button clicked
if st.button("Analyze"):

    result = get_vader_sentiment(text)

    st.write("Sentiment Scores:", result)

    # Create bar chart
    scores = [result['neg'], result['neu'], result['pos']]
    labels = ['Negative', 'Neutral', 'Positive']

    fig, ax = plt.subplots()
    ax.bar(labels, scores)
    ax.set_ylabel("Score")
    ax.set_title("Sentiment Breakdown")

    st.pyplot(fig)