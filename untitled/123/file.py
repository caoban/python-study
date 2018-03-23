f = file('myfile.txt','r')
for i in f.readlines():
    a = i.strip('\n').split(':')[5][7]
    print a