import json

# def saihi(name):
#     print("hello",name)

info = {
    'name':'suhan',
    'age':22,
    #'func':saihi
}
f = open("test.txt","w")
# print(pickle.dumps(info))
f.write(json.dumps(info))

info['age'] = 21
f.write(json.dumps(info))
f.close()




