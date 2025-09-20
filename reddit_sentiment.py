import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_csv("reddit_posts.csv")

analyzer = SentimentIntensityAnalyzer()
def analyze_sentiment(text):
    if isinstance(text, str) and text.strip():
        sentiment = analyzer.polarity_scores(text)
        return sentiment['compound']
    else:
        return 0.0
    
df['sentiment_score'] = df['body'].apply(analyze_sentiment)
print(df[['body', 'sentiment_score']].head())

df.to_csv('reddit_sentiment.csv', index = False)
print("Sentiment scores have been saved to reddit_sentiment.csv")
