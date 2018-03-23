#_*_conding:utf-8_*_
import copy
name = {
    'name':'suhan',
    'age':25,
    'salary':800
}
# for i in name:
#     print i,name[i]
for k,v in name.items():
    print k,v
name2 = copy.deepcopy(name)
name2['ex'] = ['asd','qwe']
name2['ex'].append('wuteng')
print name
print name2


