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

