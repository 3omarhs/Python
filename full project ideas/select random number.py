import random
parts = ['om', 'ma', 'ar', '3o', 'hs', 'rh', '702', '13']
list = []
for i in range(5):
    list.append(parts[random.randint(0,7)])
string = ''.join([str(w) for w in list])
print(string)
symbol = random.randint(1,10)
string1 = ""
for i in range(symbol):
    string1+=string[i]
string1+="."
till = len(string) - symbol
for i in range(till):
    string1+=string[i+symbol]
print(string1)