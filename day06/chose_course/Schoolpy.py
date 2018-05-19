import mainpy
import CourseOtherpy

import sys

#学校类
class School(object):
    #定义静态方法
    def __init__(self,SchoolName,Address):
        self.SchoolName = SchoolName
        self.Address = Address

    #创建班级类
    def CreateClass(self,TempSchoolObj):
        print("创建班级".center(30,'-'))
        ClassroomName = input("请输入班级名称：").strip()
        ClassroomPeriod = input("请输入班级周期：").strip()
        #调用 Classroom 类来实例化
        ClassroomObj = CourseOtherpy.Classroom(ClassroomName,ClassroomPeriod,TempSchoolObj.SchoolName)
        print("班级名称:%s,班级周期：%s,學校名稱:%s" %(ClassroomName,ClassroomPeriod,TempSchoolObj.SchoolName))


    def HireTeacher(self):
        print("聘请老师".center(30,'-'))
        TeacherName = input("请输入老师名称：").strip()
        TeacherAge = input("请输入老师年龄：").strip()
        TeacherSex = input("请输入老师性别：").strip()
        TeacherCourse = input("请输入老师课程：").strip()
        TeacherClassroom = input("请输入老师班级：").strip()
        #直接实例化教师的类，教师的属性在里面
        # 通过json将讲师的字典反序列化到dic字典 也没有写


    def CreateCourse(self):
        print("创建课程".center(30,'-'))
        CourseType = input("请输入课程类型：").strip()
        CourseName = input("请输入课程名称：").strip()
        CoursePrice = input("请输入课程价格：").strip()
        CoursePeriod = input("请输入课程周期：").strip()
        #课程的实例化，课程信息的显示都没写




