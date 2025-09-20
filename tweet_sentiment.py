import pandas as pd 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_csv("cleaned_tweets.csv")

analyzer = SentimentIntensityAnalyzer()
def analyze_sentiment(text):
    if isinstance(text, str) and text.strip():
        sentiment = analyzer.polarity_scores(text)
        return sentiment['compound']
    else:
        return 0.0
    
df['sentiment_score'] = df['cleaned_text'].apply(analyze_sentiment)
print(df[['cleaned_text', 'sentiment_score']].head())

df.to_csv('tweet_sentiment.csv', index = False)
print("Sentiment scores have been saved to tweet_sentiment.csv")