
import shelve

d = shelve.open('shelvesuhan')
print(d.get("name"))
print(d.get("info"))
#
# name = ['suhan','xiaolei','subei']
# info = {'name':'ssss','age':22}
#
#
# d["name"] = name
# d["info"] = info
#
# d.close()




