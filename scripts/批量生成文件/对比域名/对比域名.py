

import re


with open("domain01",'r') as  f:
    for lineweb in f:
        lineweb = lineweb.strip()

        print("############%s" % lineweb)
       # with open("result", 'a+') as res:
            #res.write("############%s\n" %(lineweb))

        with open("alldomain2", 'r') as  fall:
            for lineall in fall:
                lineall = lineall.strip()
                if re.search(".+" + lineweb + "$",lineall):
                    print("%s" % lineall)
                    with open("result", 'a+') as res:
                        res.write("%s\n" %lineall)


