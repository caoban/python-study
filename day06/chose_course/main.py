import sys

def StudentView():
    while True:
        print("1.欢迎注册\n"
              "2.返回\n"
              "3.退出")
        num = input("请选择:")
        if num == '1':
            #StudentRegiest() 调用学生注册的接口
        elif num == '2':
            break
        elif num == '3':
            sys.exit()
        else:
            continue

def TeacherView():
    name = input("请输入讲师姓名:")
    while True:
        pass

def SchoolView():
    pass

def main():
    pass



if __name__ == '__main__':
    pass
    main()


