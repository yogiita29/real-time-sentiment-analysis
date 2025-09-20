import praw
import pandas as pd

reddit = praw.Reddit(
    client_id = "ZnWKH9TIByb9eDZnmzoA3Q", 
    client_secret = "MdjcRXxnTSI3r6AbS6zIoMXn5llSAw",
    user_agent = "A Simple Sentiment Analysis Script"
)

search_query = "Google Pixel"
subreddit = reddit.subreddit("all")
posts = subreddit.search(search_query, limit=100)
data = []
for post in posts:
    data.append({
        'title': post.title,
        'score': post.score,
        'id': post.id,
        'url': post.url,
        'comms_num': post.num_comments,
        'created': post.created,
        'body': post.selftext
    })

df = pd.DataFrame(data)
df.to_csv("reddit_posts.csv", index = False)
print("Reddit posts have been saved to reddit_posts.csv")
    