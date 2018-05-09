
#课程类
class Course(object):
    def __init__(self,CourseType,CourseName,CourerPrice,CoursePeriod,CoursePlace):
        self.CourseType = CourseType
        self.CourseName = CourseName
        self.CoursePrice = CourerPrice
        self.CoursePeriod = CoursePeriod
        self.CoursePlace = CoursePlace

    def ShowClassInfo(self):
        print("课程类型:%s,名称:%s,价格:%s,周期:%s" % (self.CourseType,self.CourseName,self.CoursePrice,self.CoursePeriod))


#班级类
class Classroom(object):
    def __init__(self,ClassroomName,ClassroomPeriod,ClassroomSchoolName):
        self.ClassroomName = ClassroomName
        self.ClassroomPeriod = ClassroomPeriod
        self.ClassroomSchoolName = ClassroomSchoolName

    def ShowClassroomInfo(self):
        print("班级名称:%s\n班级周期:%s" % (self.ClassroomName, self.ClassroomPeriod))



#学校成员类
class SchoolMember(object):
    def __init__(self,MemberName,MemberSex,MemberAge):
        self.MemberName = MemberName
        self.MemberSex = MemberSex
        self.MemberAge = MemberAge



#学生类
class Student(SchoolMember):
    def __init__(self,StudentSchool,StudentName,StudentSex,StudentAge,StudentId,StudentCourse,CoursePrice):
        super(Student,self).__init__(StudentName,StudentAge,StudentSex)
        self.StudentSchool = StudentSchool
        self.StudentId = StudentId
        self.StudentCourse = StudentCourse
        self.CoursePrice = CoursePrice

    def ShowStudentInfo(self):
        print("""
       -------------------学生信息-----------------
       Name:%s
       School:%s
       Sex:%s
       Age:%s
       Id:%s
       Course:%s
       CoursePrice:%s
       """ % (self.StudentName,self.StudentSchool,self.StudentSex,
              self.StudentAge,self.StudentId,self.StudentCourse,self.CoursePrice)
        )

#讲师类
class Teacher(SchoolMember):
    def __init__(self,TeacherName,TeacherAge,TeacherSex,TeacherCourse,TeacherClassroom,TeacherSchoolName):
        super(Teacher,self).__init__(TeacherName,TeacherAge,TeacherSex)
        self.TeacherCourse = TeacherCourse
        self.TeacherClassroom = TeacherClassroom
        self.TeacherSchoolName = TeacherSchoolName

    def ShowTeacherInfo(self):
        print("""
        ----------教师信息--------
        Name:%s
        Sex:%s
        Age:%s
        Course:%s
        Classroom:%s
        SchoolName:%s
        """ % (self.TeacherName,self.TeacherSex,self.TeacherAge,
               self.TeacherCourse,self.TeacherClassroom,self.TeacherSchoolName)  )
    def ShowClassroom(self):
        pass

    def ShowStudent(self):
        pass

