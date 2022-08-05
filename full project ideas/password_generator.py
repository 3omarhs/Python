import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
numbers = "0123456789"
symbols = "[]{}()*/-+;:,.-_"
all = lower + upper + symbols
length = 10
password = "".join(random.sample(all, length))
print(password)