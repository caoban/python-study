
import re

with open("domain01cailei",'r') as f:
    for line in f:
        with open("phpall",'r') as f2:
            for line2 in f2:
                print(line2)

                if line == line2:
                    line2.replace("",line2)
                    print(line2)
                else:
                    pass
                    #print(line2)





