from newspaper import Article
import random
import string
import  nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings


def get_article_from_url(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    corpus = article.text
    return corpus



# file_text = open("chatbot referances\\all.txt")
# x = file_text.read()
# f = open("C:\\Users\\Omar Hassan\\Desktop\\all.txt", "r")
# print(f.read())

article = Article('https://en.wikipedia.org/wiki/Natural_language_processing')
article.download()
article.parse()
article.nlp()
corpus = article.text
print(corpus)
# print('file read:')
# print(file_text)
# sentence_list = nltk.sent_tokenize(file_text)
# file_text.close()
# print(sentence_list)



# with open("C:\Users\Omar Hassan\Desktop\1.txt") as fout:
#     for i in range(0, len(text) - 1):
#         sentsplit = text[i]
#         fout.write('\n'.join(sentsplit))

#Artificial Intelligence:
# text = get_article_from_url('https://www.brookings.edu/research/how-artificial-intelligence-is-transforming-the-world/')
# text += get_article_from_url('https://www.cbi.eu/market-information/outsourcing-itobpo/machine-learning-artificial-intelligence?gclid=CjwKCAiAsYyRBhACEiwAkJFKoj4lnP_vANKKpKOwTw20WOx92DG6bHA7gLnA9Wkt5JU4ng64XoKbcxoCdjQQAvD_BwE')
# # text += get_article_from_url('https://en.wikipedia.org/wiki/Artificial_intelligence')
# # text += get_article_from_url('https://en.wikipedia.org/wiki/Big_data')
# # text += get_article_from_url('https://en.wikipedia.org/wiki/Machine_learning')
# # text += get_article_from_url('https://en.wikipedia.org/wiki/Deep_learning')
# # text += get_article_from_url('https://en.wikipedia.org/wiki/Neural_network_(disambiguation)')
# # text += get_article_from_url('https://en.wikipedia.org/wiki/Cognitive_computing')
# text += get_article_from_url('https://en.wikipedia.org/wiki/Natural_language_processing')
# text = get_article_from_url('https://en.wikipedia.org/wiki/Computer_vision')
#popular culture:
# text = get_article_from_url('https://en.wikipedia.org/wiki/Popular_culture')


# f = open("C:\\Users\\Omar Hassan\\Desktop\\1.txt", "a")
# f.app(text)
# f.close()