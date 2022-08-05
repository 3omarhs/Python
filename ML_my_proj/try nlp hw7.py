# 1. Importing Necessary Modules
# 2. Importing Dataset
# 3. Data Preprocessing and Visualization
# 4. Model Building
# 5. Prediction

# 1. Importing Necessary Modules

import nltk
import pandas as pd                 # data processing, and import dataSet CSV file I/O (e.g. pd.read_csv) saves data set in a table
import matplotlib.pyplot as plt     #For Visualization / plotting
import seaborn as sns               #For better Visualization (improves plotting)
from bs4 import BeautifulSoup       #For Text Parsing
from sklearn.feature_extraction.text import TfidfVectorizer # represent data as vectors for faster classification



from sklearn.naive_bayes import (
    BernoulliNB,
    ComplementNB,
    MultinomialNB,
)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier



classifiers = {
       "BernoulliNB": BernoulliNB(),
    "ComplementNB": ComplementNB(),
    "MultinomialNB": MultinomialNB(),
    "KNeighborsClassifier": KNeighborsClassifier(),
    "DecisionTreeClassifier": DecisionTreeClassifier(),
    "RandomForestClassifier": RandomForestClassifier(),
    "MLPClassifier": MLPClassifier(max_iter=1000)
}
# 2. Importing Dataset
data = pd.read_csv('Reviews.csv')
# 3. Data Preprocessing and Visualization
print(data.isnull().sum()) # shows how many null values are there in each column
data = data.dropna() #drops null values
# changing scores from (1 -> 5) to (0 -> 2 ) where 0 are negative reviews , 1 are neutral reviews and 2 are positive reviews
a=[]
for i in data['Score']:
    if i <3:
        a.append(0)
    if i==3:
        a.append(2)
    if i>3:
        a.append(1)
# visualizing the dataset reviews
sns.countplot(a)
plt.xlabel('Reviews', color = 'red')
plt.ylabel('Count', color = 'red')
plt.xticks([0,2,1],['Negative','Neutral','Positive'])
plt.title('COUNT PLOT', color = 'r')
plt.show()

#creating a new data set with the attributes that we need or care about

data['sentiment']=a
final_dataset = data[['Text','sentiment']]
print(final_dataset)

#creating the training dataset ( we select equal number of samples to avoid over fitting )

datap = final_dataset.query("sentiment==1").sample(n=5000)
datan = final_dataset.query("sentiment==0").sample(n=5000)
print(datap)
#concatenating the training data
data = pd.concat([datap,datan])

print(data)

# now sentiment has only 0 and 1 for negative and positive respectively

c=[]
for i in data['sentiment']:
    if i==0:
        c.append(0)
    if i==1:
        c.append(1)
data['sentiment']=c
sns.countplot(data['sentiment'])
plt.show()
# Removing HTML Tags

def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()
data['review'] = data['Text'].apply(strip_html)
data=data.drop('Text',axis=1)
data.head()
# Removing punctuations

def punc_clean(text):
    import string as st
    a=[w for w in text if w not in st.punctuation]
    return ''.join(a)
data['review'] = data['review'].apply(punc_clean)
data.head(2)

# removing stop words

def remove_stopword(text):
    stopword=nltk.corpus.stopwords.words('english')
    stopword.remove('not')
    a=[w for w in nltk.word_tokenize(text) if w not in stopword]
    return ' '.join(a)
data['review'] = data['review'].apply(remove_stopword)
# Vectorization

vectr = TfidfVectorizer(ngram_range=(1,2),min_df=1)
vectr.fit(data['review'])
vect_X = vectr.transform(data['review'])
# training

model = LogisticRegression()
clf=model.fit(vect_X,data['sentiment'])
print(" logistic regression model accuracy",clf.score(vect_X,data['sentiment'])*100) # prints the accuracy

# predicting

print(' Logistic Regression prediction is ',clf.predict(vectr.transform(['''I love ice cream'''])))

print("Training accuracy")
# training more models
for name, classifier in classifiers.items():
    clf = classifier.fit(vect_X, data['sentiment'])
    accuracy = clf.score(vect_X, data['sentiment']) * 100
    print(F"{accuracy} - {name}")



# testing
print("Testing Results")
for name, classifier in classifiers.items():
    prediction=classifier.predict(vectr.transform(["i love ice cream"]))
    print(F"{prediction} - {name}")

