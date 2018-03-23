# _*_ coding:utf-8 _*_
name = [1,2,3,4,5,6,2,3,2,4]
first_pos = 0
for i in range(name.count(2)):
   #用变量代替，有些类似于用软连来做
    # next_list = name[first_pos:]
    # next_pos = next_list.index(2) + 1
    # print 'pos:',next_list.index(2) + first_pos
    # first_pos = first_pos + next_pos

    #第二种方法
    if first_pos == 0:
        first_pos = name.index(2)
    else:
        first_pos = name.index(2,first_pos+1)
    print first_pos




