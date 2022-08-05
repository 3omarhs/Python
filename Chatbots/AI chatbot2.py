from newspaper import Article
import random
import string
import  nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings

warnings.filterwarnings('ignore')
# nltk.download('punkt', quiet=True)

## Get article And Edit it:
# article = Article('https://www.brookings.edu/research/how-artificial-intelligence-is-transforming-the-world/')
# article = Article('https://www.cbi.eu/market-information/outsourcing-itobpo/machine-learning-artificial-intelligence?gclid=CjwKCAiAsYyRBhACEiwAkJFKoj4lnP_vANKKpKOwTw20WOx92DG6bHA7gLnA9Wkt5JU4ng64XoKbcxoCdjQQAvD_BwE')
# article = Article('https://www.learnenglishteam.com/wp-content/uploads/2019/02/Everyday-Conversations_-Learning-American-English-learnenglishteam.com-min.pdf')
#Artificial Intelligence:
#first source:
'''article = Article('https://en.wikipedia.org/wiki/Artificial_intelligence')
article.download()
article.parse()
article.nlp()
corpus = article.text
#second source:
article2 = Article('https://en.wikipedia.org/wiki/Big_data')
article2.download()
article2.parse()
article2.nlp()
corpus2 = article2.text
#third source:
article3 = Article('https://en.wikipedia.org/wiki/Machine_learning')
article3.download()
article3.parse()
article3.nlp()
corpus3 = article3.text
#fourth source:
article4 = Article('https://en.wikipedia.org/wiki/Deep_learning')
article4.download()
article4.parse()
article4.nlp()
corpus4 = article4.text
#fifth source:
article5 = Article('https://en.wikipedia.org/wiki/Neural_network_(disambiguation)')
article5.download()
article5.parse()
article5.nlp()
corpus5 = article5.text
#sixth source:
article6 = Article('https://en.wikipedia.org/wiki/Cognitive_computing')
article6.download()
article6.parse()
article6.nlp()
corpus6 = article6.text
#seventh source:
article7 = Article('https://en.wikipedia.org/wiki/Natural_language_processing')
article7.download()
article7.parse()
article7.nlp()
corpus7 = article7.text
#eightth source:
article8 = Article('https://en.wikipedia.org/wiki/Computer_vision')
article8.download()
article8.parse()
article8.nlp()
corpus8 = article8.text
#popular culture:
article9 = Article('https://en.wikipedia.org/wiki/Natural_language_processing')
article9.download()
article9.parse()
article9.nlp()
corpus9 = article9.text'''


def get_article_from_url(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    corpus = article.text
    return corpus

# #Artificial Intelligence:
# text = get_article_from_url('https://www.brookings.edu/research/how-artificial-intelligence-is-transforming-the-world/')
# text += get_article_from_url('https://www.cbi.eu/market-information/outsourcing-itobpo/machine-learning-artificial-intelligence?gclid=CjwKCAiAsYyRBhACEiwAkJFKoj4lnP_vANKKpKOwTw20WOx92DG6bHA7gLnA9Wkt5JU4ng64XoKbcxoCdjQQAvD_BwE')
# text += get_article_from_url('https://en.wikipedia.org/wiki/Artificial_intelligence')
# text += get_article_from_url('https://en.wikipedia.org/wiki/Big_data')
# text += get_article_from_url('https://en.wikipedia.org/wiki/Machine_learning')
# text += get_article_from_url('https://en.wikipedia.org/wiki/Deep_learning')
# text += get_article_from_url('https://en.wikipedia.org/wiki/Neural_network_(disambiguation)')
# text += get_article_from_url('https://en.wikipedia.org/wiki/Cognitive_computing')
# text += get_article_from_url('https://en.wikipedia.org/wiki/Natural_language_processing')
# text += get_article_from_url('https://en.wikipedia.org/wiki/Computer_vision')
# #popular culture:
# text = get_article_from_url('https://en.wikipedia.org/wiki/Popular_culture')
# # get_article_from_url()
# # get_article_from_url()
# # get_article_from_url()
# # get_article_from_url()

# print(corpus)
# text = corpus
# text = corpus + corpus2 + corpus3 + corpus4 + corpus5 + corpus6 + corpus7 + corpus8
# text = corpus
# print(text)
file_text = open("../chatbot referances/all.txt", "r").read()
print('file read:')
print(file_text)
sentence_list = nltk.sent_tokenize(file_text)
file_text.close()
# print(sentence_list)


def greeting_response(text):
    text = text.lower()
    bot_greetings = ['howdy', 'hi', 'hey', 'hello', 'hola']
    user_greetings = ['hi', 'hey', 'hello', 'greetings', 'wassup']

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)

def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))
    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index


def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0
    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response + ' ' + sentence_list[index[i]]
            response_flag = 1
            j = j + 1
            if j > 2:
                break
            if response_flag == 0:
                bot_response = bot_response + ' ' + "I apologize, I don`t understand."
            sentence_list.remove(user_input)
            # print(bot_response)
            return  bot_response

#start chat..
print('3omar.hs Bot: I am 3omar.hs Bot. I will answer your queries about Artificial Intelligence. If you want to exit, type \"bye\".')
exit_list = ['exit', 'see you later', 'bye', 'quit', 'break']
while True:
    user_input = input()
    if user_input.lower() in exit_list:
        print('3omar.hs Bot: Chat with you later!')
        break
    elif greeting_response(user_input) != None:
        print('3omar,hs Bot: '+greeting_response(user_input))
    else:
        try:
            print('3omar.hs Bot: '+bot_response(user_input))
        except:
            print('Undefined Input!!')
