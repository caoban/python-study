import sys
import os
f = open("sed.txt",'r',encoding='utf-8')
f_new = open("sed2.txt",'w',encoding='utf-8')

befor = sys.argv[1]
after = sys.argv[2]

print(befor)
print(after)
for line in f:
    if befor in line:
        line = line.replace(befor,after)
    f_new.write(line)
f.close()
f_new.close()







