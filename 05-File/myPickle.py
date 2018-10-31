import pickle

age = 22

with open('pick.txt', 'wb') as f:
    pickle.dump(age, f)