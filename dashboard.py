import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def classify_sentiment(score):
    """Classify sentiment based on score."""
    if score > 0.05:
        return 'Positive'
    elif score < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def plot_wordcloud(text):
    """Generate and display a word cloud from text data."""
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(text))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

def plot_bar_chart(data, column, title):
    """Generate and display a bar chart for a specified column."""
    counts = Counter(data[column])
    plt.figure(figsize=(10, 5))
    sns.barplot(x=list(counts.keys()), y=list(counts.values()))
    plt.title(title)
    plt.xticks(rotation=45)
    st.pyplot(plt)

def plot_pie_chart(data, column, title):
    """Generate and display a pie chart for a specified column."""
    counts = Counter(data[column])
    plt.figure(figsize=(8, 8))
    plt.pie(counts.values(), labels=counts.keys(), autopct='%1.1f%%', startangle=140)
    plt.title(title)
    st.pyplot(plt)

def plot_histogram(data, column, title):
    """Generate and display a histogram for a specified column."""
    plt.figure(figsize=(10, 5))
    plt.hist(data[column], bins=20, edgecolor='black')
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    st.pyplot(plt)

def get_text_for_wordcloud(data, data_source):
    """Get combined text for word cloud."""
    if data_source == "Tweets":
        return data['cleaned_text'].dropna()
    else:  # Reddit
        texts = []
        for _, row in data.iterrows():
            text = row['title']
            if pd.notna(row['body']) and row['body'].strip():
                text += ' ' + row['body']
            texts.append(text)
        return pd.Series(texts)

def main():
    st.title("Real-Time Sentiment Analysis Dashboard")

    # Select data source
    data_source = st.selectbox("Select Data Source", ["Tweets", "Reddit Posts"])

    if data_source == "Tweets":
        data = load_data('tweet_sentiment.csv')
    else:
        data = load_data('reddit_sentiment.csv')

    # Add sentiment category
    data['sentiment_category'] = data['sentiment_score'].apply(classify_sentiment)

    # Display basic stats
    st.subheader("Data Overview")
    st.write(f"Total entries: {len(data)}")
    st.write(data['sentiment_category'].value_counts())

    # Display raw data
    if st.checkbox("Show raw data"):
        st.write(data.head(100))  # Show first 100 rows

    col1, col2 = st.columns(2)

    with col1:
        # Word Cloud
        if st.button("Generate Word Cloud"):
            texts = get_text_for_wordcloud(data, data_source)
            plot_wordcloud(texts)

    with col2:
        # Bar Chart for sentiment categories
        if st.button("Generate Sentiment Bar Chart"):
            plot_bar_chart(data, 'sentiment_category', 'Sentiment Distribution')

    # Pie Chart
    if st.button("Generate Sentiment Pie Chart"):
        plot_pie_chart(data, 'sentiment_category', 'Sentiment Distribution')

    # Histogram for sentiment scores
    if st.button("Generate Sentiment Score Histogram"):
        plot_histogram(data, 'sentiment_score', 'Sentiment Score Distribution')

if __name__ == "__main__":
    main()
