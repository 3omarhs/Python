import nltk
text = 'Hi I`m Omar Hassan, how are you, I`m an AI Student.'
sent = nltk.sent_tokenize(text)
for i in sent:
    word = nltk.word_tokenize(i)
    # print(word)
    print("Most Common charactes:")
    print(nltk.FreqDist(text).most_common(2))

    print("tokenize:")
    tok_word = []
    for j in word:
        tok_word.append(j)
    print(tok_word, end=' ')
    print()
    print('*'*50)

    print("stimmming:")
    for h in tok_word:
        print(nltk.PorterStemmer().stem(h), end=' ')
    print()
    print('*'*50)

    print("lemmatize:")
    print(' '.join(([nltk.WordNetLemmatizer().lemmatize(k) for k in tok_word])))
    print('*'*50)

    print("POS tagging:")
    tag = nltk.pos_tag(word)
    print(tag)
    print('*'*50)

    print("Regular Expression:")
    print(nltk.RegexpParser("NP:{<DT>?<JJ>*<NN>}").parse(tag))
    print('*'*50)
    
def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent
sent = preprocess(text)
print(sent)


# join code:    ' '.join(([nltk.WordNetLemmatizer().lemmatize(k) for k in tok_word]))
