from nltk.sentiment import SentimentIntensityAnalyzer
def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")
    print("Sentence Overall Rated As", end=" ")
    if sentiment_dict['compound'] >= 0.05:
        print("Positive")
    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative")
    else:
        print("Neutral")

# Driver code
if __name__ == "__main__":
    print("\n1st statement :")
    sentence = "I love programming and designing microcontrollers."
    # function calling
    sentiment_scores(sentence)
    print("\n2nd Statement :")
    sentence = "I do projects like interactive robots and great IoT projects."
    sentiment_scores(sentence)
    print("\n3rd Statement :")
    sentence = "But I hate literature and chemistry."
    sentiment_scores(sentence)


'''
import nltk
# nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer
# a pre-trained model using Naïve Bayes Classifier

sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores("I'm really into artificial intelligence and I love it."))
'''