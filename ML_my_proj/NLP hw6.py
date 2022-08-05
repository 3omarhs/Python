import nltk
# nltk.download()

from nltk.book import *

# nltk.download('gutenberg')
# nltk.download('genesis')
# nltk.download('inaugural')
# nltk.download('nps_chat')
# nltk.download('webtext')
# nltk.download('treebank')

import os, os.path

mypath = os.path.expanduser("~/nltk_data")

if not os.path.exists(mypath):
    os.mkdir(mypath)
    print("folder has been created")

else:
    print("folder is already exits")

import nltk.data

v = mypath in nltk.data.path

print(v)
print(mypath)

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

ss= word_tokenize(mypath)
print(ss)

cc= pos_tag(ss)
print(cc)

print('text1:',text1)
print('length text3:',len(text3))
print('count(in) in text3:',text3.count("in"))








from nltk.parse.corenlp import CoreNLPDependencyParser, CoreNLPParser

dep_parser = CoreNLPDependencyParser(url='http://localhost:9000')
parse, = dep_parser.raw_parse('Hi I`m Omar Hassan Al-Jammal')

print(parse.to_conll(4))

for governor, dep, dependent in parse.triples():
  print(governor, dep, dependent)

parser = CoreNLPParser(url='http://localhost:9000')
next(parser.raw_parse('I`m a student in the Al-Zaytoonah university with student number: 201910155')).pretty_print()









