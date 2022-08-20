import pickle

# category = 'Female'
category = 'Male'

with open(f'../encoded images files/{category}_encoding.txt', "rb") as fp:  # Unpickling
    encodinge = pickle.load(fp)
with open(f'../encoded images files/{category}_names.txt', "rb") as fp:  # Unpickling
    names = pickle.load(fp)
# print(f"Encodings: {len(encodinge)}photo, {encodinge}")
print(f"Names: {len(names)}photo, {names}")