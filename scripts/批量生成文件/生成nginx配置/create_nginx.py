
import re

with open("phpweb_domain",'r') as f:
    for line in f:
        line = line.strip()


        if re.search(".+guanaitong$",line) :
            pass
            # with open("testmall.guanaitong.cc.conf",'r') as fg:
            #     for line_fg in fg:
            #         line_fgw = line_fg.replace("mall.guanaitong",line)
            #         with open(line + ".cc.conf", 'a+') as  fgw:
            #             fgw.write(line_fgw)


        elif re.search(".+ciicgat$",line) :

            with open("testmall.ciicgat.cc.conf",'r') as fc:
                for line_fc in fc:
                    line_fcw = line_fc.replace("mall.ciicgat",line)
                    with open(line + ".cc.conf", 'a+') as  fcw:
                        fcw.write(line_fcw)

        elif re.search(".+4008885818$",line) :
            pass
            # with open("testmall.4008885818.cc.conf",'r') as f4:
            #     for line_f4 in f4:
            #         line_f4w = line_f4.replace("mall.4008885818",line)
            #         with open(line + ".cc.conf", 'a+') as  f4w:
            #             f4w.write(line_f4w)

        else:
            #pass
            print(line)





