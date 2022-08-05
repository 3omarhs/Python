'''import os, os.path
mypath = os.path.expanduser("~/nltk_data")

if not os.path.exists(mypath):
    os.mkdir(mypath)
    print("folder has been created")
else:
    print("folder is already exits")

import nltk.data
v = mypath in nltk.data.path
print(v)

newfile=nltk.data.load("C:/Users/Omar Hassan/Documents/nltk mine/sample1.txt")
# newfile=nltk.data.load("sample1.txt", format='raw')
# print(newfile)'''

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


newfile=nltk.data.load("sample1.txt")
#newfile=nltk.data.load("sample1.txt", format='raw')
print(newfile)




