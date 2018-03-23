import pickle
f = open("test.txt","rb")
data = pickle.loads(f.read())
f.close()
print(data)
print(data['age'])
print(data['name'])

data = pickle.load(f)

