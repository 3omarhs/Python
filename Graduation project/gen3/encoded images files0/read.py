import pickle

category = 'Male'

# with open(f'{category}_encoding.txt', "rb") as fp:  # Unpickling
with open(f'{category}_names.txt', "rb") as fp:  # Unpickling
    known_face_encodings = pickle.load(fp)

print(known_face_encodings)