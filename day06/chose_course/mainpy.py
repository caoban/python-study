import sys
import CourseOtherpy
import Schoolpy
#用别的py文件中的函数或者类的时候，前面要加上import的名称


#学生注册
def StudentRegiest():
    #学生的信息：1、基本信息2、所选择的对应的课程信息。
    #最后为了生成一个学生对象的

    MemberName = input("请输入学生姓名:")
    MemberSex = input("请输入学生性别:")
    MemberAge = input("请输入学生年龄:")
    StudentId = input("请输入学生序号")

    #打印课程的信息，供学生查看选择输入
    print("1.%s %sRMB, 2.%s %sRMB, 3.%s %sRMB,4.返回" %(Course1.CourseName,Course1.CoursePrice,
                                                    Course2.CourseName,Course2.CoursePrice,
                                                    Course3.CourseName,Course3.CoursePrice))

    #学生选择课程
    while True:
        CourseNum = input("请选择课程：")
        if CourseNum == '1':
            #用变量的形式把 输入的信息对应上，并保存到一个 字典里面
            StudentCourse = Course1.CourseName
            CoursePrice = Course1.CoursePrice

        elif CourseNum == '2':
            StudentCourse = Course2.CourseName
            CoursePrice = Course2.CoursePrice

        elif CourseNum == '3':
            StudentCourse = Course3.CourseName
            CoursePrice = Course3.CoursePrice

        elif CourseNum == '4':
            break
        else:
            continue

        #根据上面的信息，实例化学生对象
        #ChoiceSchoolObjDict[0].SchoolName 是不想用global，列表的形式保存信息，这里用
        StudentX = CourseOtherpy.Student(ChoiceSchoolObjDict[0].SchoolName, MemberName, MemberSex,
                                             MemberAge, StudentId, StudentCourse, CoursePrice)

        # 打印信息，将学生信息key value的形式存到字典里面
        StudentX.ShowStudentInfo()
        StudentDict[MemberName] = StudentX

        #打印字典里面的信息。 字典里面的value是对象的内存地址
        # for x in StudentDict.keys():
        #     print(StudentDict[x].ShowStudentInfo())

        print("完成注册。。。。")
        break



def StudentView():
    while True:
        print("1.欢迎注册\n"
              "2.返回\n"
              "3.退出")
        num = input("请选择:")
        if num == '1':
            #学生注册的函数
            StudentRegiest()
        elif num == '2':
            break
        elif num == '3':
            sys.exit()
        else:
            continue

def TeacherView():
    name = input("请输入讲师姓名:")
    while True:
        if name in TeachersDict.keys():
            print("欢迎%s老师".center(50,'*') %name)

        else:
            print("%s老师不存在！,返回上一层"  % name)
            break

        num = input("1.查看班级\n"
            "2.查看学员信息\n"
            "3.返回\n"
            "4.退出\n"
            "选择：")
        print("功能未完善,只能输入Alex,cheng")

        if num == '1':
            TeachersDict[name].ShowClassroom(name)
            pass

        elif num == '2':
            #输入的name找到对应的Teacher对象，再调Teacher的ShowStudent方法
            #查看老师对应的学生信息
            TeachersDict[name].ShowStudent()
        elif num == '3':
            break
        elif num == '4':
            sys.exit()
        else:
            continue


def SchoolView():
    pass



#选择视图的入口
def master():

#全局变量还没用，看看有什么用，最好不要使用 global

    while True:
        #center是显示有50 *
        print("请选择学校:".center(50,'*'))
        #这个用法，print和 input 用在一个语句中，显示的时候没有换行
        ChoiceSchool = input("1.%s,2.%s,3.返回,4.退出 \n选择：" % (School1.SchoolName,School2.SchoolName))

        if ChoiceSchool == '1':
            #不想用global，用列表存信息，别的函数里面用
            ChoiceSchoolObjDict.append(School1)
            ChoiceSchoolObjDict[0].CreateClass(ChoiceSchoolObjDict[0])

        elif ChoiceSchool == '2':
            ChoiceSchoolObjDict.append(School2)
        elif ChoiceSchool == '3':
            break
        elif ChoiceSchool == '4':
            #可以退出的打字，还可以加颜色
            sys.exit("已退出当前系统")
        else:
            continue



        while True:
            #这个跟上面类似的 一种 打印和input 写在一起了
            num = input("1.学员视图\n"
                        "2.讲师视图\n"
                        "3.学校管理视图\n"
                        "4.返回\n"
                        "5.退出\n"
                        "请选择视图:")

            if num == '1':
                print("欢迎进入学员视图".center(50,'*'))
                StudentView()
            elif num == '2':
                print("欢迎进入讲师视图".center(50, '*'))
                TeacherView()
            elif num == '3':
                print("欢迎进入学校管理视图".center(50, '*'))
                SchoolView()
            elif num == '4':
                break
            elif num == '5':
                sys.exit("已退出系统")
            else:
                continue


if __name__ == '__main__':
    #定义几个空字典，后面把信息当做key value存储
    Classrooms = {}
    TeachersDict = {}
    CoursesDict = {}
    StudentDict = {}
    ChoiceSchoolObjDict = []

    # 实例化学校，实例化就是把信息传到类里面。一个类可以实例化多个对象
    School1 = Schoolpy.School("老男孩","北京")
    School2 = Schoolpy.School("关爱通","上海")

    print("school:%s" %School1)
    #print("school():%s" % School1())


    #实例化课程.就是把类里面的参数，具体化。一个人，实例化成一个具体什么样的人。
    Course1 = CourseOtherpy.Course("技术",'linux','11800',"one year","北京")
    Course2 = CourseOtherpy.Course("技术", "Python", "6400", "7 month", "北京")
    Course3 = CourseOtherpy.Course("技术", "CCIE", "2400", "4 month", "广州大学城")

    #把课程名称和课程具体的信息，key value的形式存在一个字典里面。方便存和取。
    #这次的设置可能有问题，同一个课程名的，课程价格周期和地点可能是变化的...暂不考虑
    CoursesDict['linux'] = Course1
    CoursesDict['Python'] = Course2
    CoursesDict['CCIE'] = Course3

    # 实例化两个讲师
    t1 = CourseOtherpy.Teacher("Alex", "M", "33", "Python", "S13", "Oldboy")
    t2 = CourseOtherpy.Teacher("cheng", "M", "35", "CCIE", "魔鬼训练营", "Pinginglab")

    #类比上面的把教师的信息也存在字典里面
    TeachersDict['Alex'] = t1
    TeachersDict['cheng'] = t2

    #调用主函数，出现视图的那种。选择的入口
    master()


