import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import matplotlib.pyplot as plt
from src.vader_model import get_vader_sentiment

st.title("X Sentiment Analysis Dashboard")

user_input = st.text_area("Enter a post:")

if st.button("Analyze"):

    result = get_vader_sentiment(user_input)

    # Show full score dictionary
    st.write("Sentiment Scores:", result)

    # Determine final sentiment label
    compound = result['compound']
    if compound >= 0.05:
        sentiment_label = "Positive 😊"
    elif compound <= -0.05:
        sentiment_label = "Negative 😡"
    else:
        sentiment_label = "Neutral 😐"

    st.subheader("Final Sentiment:")
    st.write(sentiment_label)

    # Create bar graph
    scores = [result['neg'], result['neu'], result['pos']]
    labels = ['Negative', 'Neutral', 'Positive']

    fig, ax = plt.subplots()
    ax.bar(labels, scores)
    ax.set_ylabel("Score")
    ax.set_title("Sentiment Breakdown")

    st.pyplot(fig)