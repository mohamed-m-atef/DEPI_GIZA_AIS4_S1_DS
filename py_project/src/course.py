class Course:
    _id_counter=1
    def __init__(self,name):
        self.course_id= Course._id_counter #without student. will not work
        Course._id_counter+=1
        self.name=name
        self.grade={}
        self.enrolled_courses=[]

    def __str__(self):
        return f"course id: {self.course_id}, name: {self.name}, grade : {self.grade}, enrolled courses: {self.enrolled_courses} "
    def __repr__(self):
        return f"course id: {self.course_id}, name: {self.name}, grade : {self.grade}, enrolled courses: {self.enrolled_courses} "   
     
    def add_grade(self,course_id :int,grade:int):
        """
        this function help end user to add the specific grade for specific course
        
        param_1: take grade
        type_1: int
        param_2: take course id
        type_2: int

        return: test
        type_return: str
        """

        self.grade[course_id]=grade

    def enroll_course(self,course_id:int):
        self.enrolled_courses.append(course_id)
        if student not in course_id.enrolled_students:
            course_id.enrolled_students.append(self)

    def remove_student (self,student_id:int):
        for course in self.enrolled_courses:
            if student_id in course.enrolled_students:
                course.enrolled_students.remove(student_id)