
import re

with open("domain01",'r') as f:
    for line in f:

        if re.search(".+guanaitong$",line) :
            print(line)
        else:
            print(1111)





