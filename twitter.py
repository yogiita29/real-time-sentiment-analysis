import tweepy
import pandas as pd


bearer_token = "AAAAAAAAAAAAAAAAAAAAAK3W4AEAAAAAjnmIhuJOiY0MHUaj3zCiFuxcKQQ%3Dptl5prwsKLhoSZXx4jYAHU8X7A1xcybT9jHDsJsmah8q2glbkM"
client = tweepy.Client(bearer_token)

search_query = "Google Pixel"
response = client.search_recent_tweets(search_query, max_results=100)

if response.data:
    data = []
    for tweet in response.data:
        data.append({
            'text': tweet.text,
            'id': tweet.id
        })

    df = pd.DataFrame(data)
    df.to_csv("tweets.csv", index = False) 
        
    print("Tweets have been saved to tweets.csv")

else:
    print("No tweets found for the given query.")

    
