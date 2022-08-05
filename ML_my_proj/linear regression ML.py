import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('../datasets/temps2.csv')

#get a copy of dataset exclude last column
Input = dataset.iloc[:, :-1].values

#get array of dataset in column 2st
output = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split

# 30% data for testing, random state 1
X_train, X_test, y_train, y_test = train_test_split(Input, output, train_size=.7, random_state=1)

from sklearn.model_selection import train_test_split

# 30% data for testing, random state 1
X_train, X_test, y_train, y_test = train_test_split(Input, output, train_size=.7, random_state=1)

#printing the splitted output values
print("training output values: \n",y_train)
print("Testing output values:\n",y_test)
