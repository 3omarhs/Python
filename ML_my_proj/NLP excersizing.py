import nltk
from nltk import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk import FreqDist

text = "I am Omar Hassan Al-Jammal, I was born in Saudi arabia."
word_list = nltk.word_tokenize(text)
print('Stemming: ', end='')
for w in word_list:
    print(PorterStemmer().stem(w), end=' ')
    # print("Stemming for {} >> {}".format(w, PorterStemmer().stem(w)))
print()
print('*'*50)
lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize("boats"))
word_list2 = []
for i in word_list:
    word_list2.append(PorterStemmer().stem(i))
print('lemma: ', end='')
print(' '.join([lemmatizer.lemmatize(w) for w in word_list2]))
print('*'*50)
print('Frequently Distribute: ', end='')
print(FreqDist(word_list2).most_common(2))



