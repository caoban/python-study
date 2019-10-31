import pickle

def saihi(name):
    print("hello",name)

info = {
    'name':'suhan',
    'age':22,
    'func':saihi
}
f = open("test.txt","wb")
# print(pickle.dumps(info))
f.write(pickle.dumps(info))
f.close()


