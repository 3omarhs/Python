import nltk
text = "studies studying cries cry"
word_tokens = nltk.word_tokenize(text)
for w in word_tokens:
 print("Lemma for {} is {}".format(w, nltk.WordNetLemmatizer().lemmatize(w)))
import nltk
groucho_dep_grammar = nltk.DependencyGrammar.fromstring("""
'shot' -> 'I' | 'elephant' | 'in'
'elephant' -> 'an' | 'in'
'in' -> 'pajamas'
'pajamas' -> 'my'
 """)
print(groucho_dep_grammar)
'''
from nltk.parse.corenlp import CoreNLPDependencyParser

dep_parser = CoreNLPDependencyParser(url='http://localhost:9000')
parse, = dep_parser.raw_parse('you can insert any sentence you want here')

print(parse.to_conll(4))
'''
print(word_tokens)
print(nltk.wsd.lesk(word_tokens, ' costs'))

from nltk.sentiment import SentimentIntensityAnalyzer
print(nltk.sentiment.SentimentIntensityAnalyzer().polarity_scores(text))
