import re

with open('cc.domain','r') as f:
    for line in f:
        line = line.strip().strip(".cc")
        if re.search("^.+guanaitong$",line):
            line = line.strip().split('.guanaitong')[0]
            doman_dns = line + " 			   A	        221.12.127.35"
            with open("guanaitong_dns", 'a+') as guanai:
                guanai.write(doman_dns+'\n')

            #print("guanaitong---%s" %doman_dns)

        elif re.search("^.+ciicgat$",line):

            line = line.strip().split('.ciicgat')[0]
            doman_dns = line + " 			   A	        221.12.127.35"
            with open("ciicgat_dns", 'a+') as ciicgat:
                ciicgat.write(doman_dns+'\n')

            #print("ciicgat---%s" % line)

        elif re.search("^.+4008885818$",line):

            line = line.strip().split('.4008885818')[0]
            doman_dns = line + " 			   A	        221.12.127.35"
            with open("4008885818_dns", 'a+') as si:
                si.write(doman_dns+'\n')

            #print("4008885818---%s" % line)

        else:
            print("else---%s" % line)


        # line = line.strip().split('.guanaitong.cc')[0]
        # doman_dns = line + " 			   A	        221.12.127.35"
        # print(doman_dns)
        # with open("doman_dns.txt",'a+') as f2:
        #     f2.write(doman_dns+'\n')









