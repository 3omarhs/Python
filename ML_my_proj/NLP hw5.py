# '''
import nltk
from nltk.stem import WordNetLemmatizer
# nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet
lemmatizer = WordNetLemmatizer()
def pos_tagger(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


sentence = 'Omar Hassan Al-Jammal is a Zaytoonah student with, student number: 201910155.'

pos_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))

print(pos_tagged)
print('*'*50)

wordnet_tagged = list(map(lambda x: (x[0], pos_tagger(x[1])), pos_tagged))
print(wordnet_tagged)

print('*'*50)


lemmatized_sentence = []
for word, tag in wordnet_tagged:
    if tag is None:
        # if there is no available tag, append the token as is
        lemmatized_sentence.append(word)
    else:
        # else use the tag to lemmatize the token
        lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
lemmatized_sentence = " ".join(lemmatized_sentence)

print(lemmatized_sentence)

'''
ch1 p.21
punket>>tokenize
طنش الرسمات
20 دائرة
10 كود
wort, sentance, limmatization
token
stem
pos
shunk
def_preprosses
join(stemming,limmatization)
# name = 'Omar'
# print(name.startswith('O')
2 years
#'''