The Real-Time Sentiment Analysis Project
This project is a comprehensive data science solution that analyzes and visualizes public sentiment toward a specific brand from two major social media platforms: Reddit and Twitter (X).

🌟 Project Overview
The goal of this project is to build an end-to-end sentiment analysis pipeline. We follow a structured approach:

Data Acquisition: Collecting raw data (tweets and Reddit posts/comments) using official APIs.
Data Preprocessing: Cleaning the unstructured text data by removing noise such as URLs, special characters, and common words.
Sentiment Analysis: Applying a pre-trained model to classify each piece of text as positive, negative, or neutral.
Data Visualization: Creating informative charts and word clouds to understand the overall sentiment distribution and key topics.
Interactive Dashboard: Building a user-friendly web dashboard with Streamlit to present all findings in one place.

🛠️ Key Skills Gained
This project demonstrates proficiency in several key areas of data science:

API Integration: Securely fetching data from public APIs (Twitter, Reddit).
Natural Language Processing (NLP): Text cleaning, tokenization, and sentiment analysis using VADER.
Data Handling: Manipulating and combining data from different sources with pandas.
Data Visualization: Creating insightful plots with matplotlib, seaborn, and wordcloud.
Dashboard Development: Building an interactive web application using Streamlit.

📂 Project Structure
Your project directory contains the following files:

/Real-Time-Sentiment-Analysis
├── dashboard.py                  # The Streamlit dashboard application
├── data_cleaning.py              # Script for preprocessing text data
├── tweet_analyzer.py             # Script for sentiment analysis on Twitter data
├── twitter.py                    # Script for collecting Twitter data
├── reddit_data_cleaning.py       # Script for preprocessing Reddit data
├── reddit_sentiment.py           # Script for sentiment analysis on Reddit data
├── reddit.py                     # Script for collecting Reddit data
├── cleaned_tweets.csv            # Processed Twitter data
├── tweet_sentiment.csv           # Twitter data with sentiment scores
├── reddit_posts.csv              # Raw Reddit data
├── cleaned_reddit_data.csv       # Processed Reddit data
├── reddit_sentiment.csv          # Reddit data with sentiment scores
└── (various .png files)          # Generated visualizations

🚀 How to Run the Project
Follow these steps to replicate the project and run the final dashboard.

1. Install Dependencies
You will need to install the required Python libraries.

- pandas nltk vaderSentiment tweepy praw streamlit matplotlib seaborn wordcloud
Note: The first time you use nltk, you must also run nltk.download('punkt') and nltk.download('stopwords') to get the necessary data files. Also change the download source link.

2. Set Up API Credentials
Twitter (X): Get your Bearer Token from the Twitter Developer Portal and place it in the twitter.py script.

Reddit: Get your Client ID, Client Secret, and User Agent from the Reddit App Preferences page and add them to the reddit.py script.

3. Execute Scripts in Order
Run the scripts sequentially to build the data pipeline.


# Data Acquisition
python twitter.py    --for twitter
python reddit.py     --for reddit

# Data Preprocessing & Sentiment Analysis
python data_cleaning.py          # For Twitter data
python reddit_data_cleaning.py   # For Reddit data
python tweet_analyzer.py
python reddit_sentiment.py
4. Run the Dashboard
Finally, launch the interactive dashboard to view the results.


streamlit run dashboard.py
This command will open a web browser showing a live, interactive dashboard with all your visualizations.

NOTE:  The dashboard will show TWITTER DATA by default, For REDDIT POSTS you should type manually "REDDIT POSTS" then it will show you the reddit data.

📊 Dashboard Screenshots


<img width="649" height="365" alt<img width="533" height="290" alt="Reddit Example" src="https://github.com/user-attachments/assets/573e6a10-f7cf-42f3-933d-98c6533e255f" />
="Twitter<img width="586" height="375" alt="Twitter Sentiment Histogram" 
                                            src="https://github.com/user-attachments/assets/a20bf25d-8f1d-4045-9ca5-438d236ae0cf" />
 Dashboard Example image" src="https://github.com/user-attachments/assets/4082400b-c41c-4064-a757-f5f7d98afdbb" />
