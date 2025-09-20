import pandas as pd
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

df = pd.read_csv('tweets.csv')

def clean_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#','', text)
    text = re.sub(r'[^A-Za-z\s]', '', text)
    text = text.lower()
    return text

def tokenize_stopwords(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return " " .join(filtered_tokens)

df['cleaned_text'] = df['text'].apply(clean_text).apply(tokenize_stopwords)
print(df[['text', 'cleaned_text']].head())

df.to_csv('cleaned_tweets.csv', index = False)
print("Cleaned tweets have been saved to cleaned_tweets.csv")
