import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud

df = pd.read_csv("reddit_sentiment.csv")

plt.figure(figsize=(10,6))
sns.histplot(df['sentiment_score'], bins=30, kde=True)
plt.title("Sentiment Score Distribution")
plt.xlabel("Sentiment Score")
plt.ylabel("Frequency")
plt.savefig("reddit_sentiment_distribution.png")
plt.show()
plt.close()

positive_posts = df[df['sentiment_score'] > 0]
negative_posts = df[df['sentiment_score'] < 0]
positive_words = ' '.join(positive_posts['body'].astype(str).tolist())
negative_words = ' '.join(negative_posts['body'].astype(str).tolist())

positive_wordcloud = WordCloud(width=800, height=400, background_color='white').generate(positive_words)
negative_wordcloud = WordCloud(width=800, height=400, background_color='black').generate(negative_words)
plt.figure(figsize=(10,6))
plt.imshow(positive_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Positive Words Word Cloud")
plt.savefig("reddit_positive_wordcloud.png")
plt.show()
plt.close()

plt.figure(figsize=(10,6))
plt.imshow(negative_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Negative Words Word Cloud")
plt.savefig("reddit_negative_wordcloud.png")
plt.show()
plt.close()

all_words = ' '.join(df['body'].astype(str).tolist()).split()
word_counts = Counter(all_words)
most_common_words = word_counts.most_common(20)
words, counts = zip(*most_common_words)
plt.figure(figsize=(10,6))
sns.barplot(x=list(counts), y=list(words), palette='viridis')
plt.title("Top 20 Most Common Words")
plt.xlabel("Counts")
plt.ylabel("Words")
plt.savefig("reddit_most_common_words.png")
plt.show()
plt.close()
print("Reddit visualizations have been saved as PNG files.")
