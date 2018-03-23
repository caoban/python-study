# _*_ coding:utf-8 _*_
print_num = input('想要循环的次数:')
count = 0
while count < 50:
    if count == print_num:
        print '打印的次数为', count
        choice = raw_input('想继续吗(y/n)')
        if choice == 'n':
            break
        else:
            while count >= print_num:
                print_num = input('想要循环的次数:')
                print '已经过了 sb',count
    else:
        print 'loop:',count
        count = count+1









