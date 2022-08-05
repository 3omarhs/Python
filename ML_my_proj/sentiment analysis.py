import pandas as pd
df = pd.read_csv("./DesktopDataFlair/Sentiment-Analysis/Tweets.csv")

review_df = df[['text','airline_sentiment']]

print(review_df.shape)
print(review_df.head(5))

print(df.columns)


print(review_df["airline_sentiment"].value_counts())

sentiment_label = review_df.airline_sentiment.factorize()
print(sentiment_label)

tweet = review_df.text.values

encoded_docs = tokenizer.texts_to_sequences(tweet)