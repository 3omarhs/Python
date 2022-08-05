import nltk
from nltk.corpus import stopwords
from nltk import FreqDist
# nltk.download('wordnet')
# nltk.download('punkt')
# nltk.download('stopwords')

sentence = "Omar attends the university daily. Omar`s Collage number is 201910155"
sent = nltk.sent_tokenize(sentence)
for i in sent:
    tokens = nltk.word_tokenize(i)
    print(tokens)
print('*'*20)
print('StopWords:', stopwords.words('english'))
lower_text = sentence.lower()
print('Lower Casing:', lower_text)
text = nltk.word_tokenize(lower_text)
filtered_sentence = []
for w in text:
	if w not in stopwords.words('english'):
		filtered_sentence.append(w)
print(filtered_sentence)
print(FreqDist(text).most_common(3))


