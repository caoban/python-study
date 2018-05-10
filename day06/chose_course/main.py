import sys
import CourseOther
import School


def StudentView():
    while True:
        print("1.欢迎注册\n"
              "2.返回\n"
              "3.退出")
        num = input("请选择:")
        if num == '1':
            pass
            #怎么做的还没弄
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

def master():
    pass



if __name__ == '__main__':
    #定义几个空字典，后面把信息当做key value存储
    Classrooms = {}
    TeachersDict = {}
    CoursesDict = {}

    # 实例化学校，实例化就是把信息传到类里面。一个类可以实例化多个对象
    School1 = School("老男孩","北京")
    School2 = School("关爱通","上海")

    #实例化课程
    Course1 = Course("技术",'linux','11800',"one year","北京")
    #School1.CreateClass()
    #Course1.ShowClassInfo()
    #master()


