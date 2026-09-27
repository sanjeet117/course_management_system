from models.user import User


class Student(User):

    def __init__(self, user_id, name, email, student_id):
        super().__init__(user_id, name, email)

        self.student_id = student_id
        self.enrolled_courses = []

    def enroll_course(self, course):
        self.enrolled_courses.append(course)
        course.add_student(self)

        print(f"{self.name} enrolled in {course.course_name}")

    def display_profile(self):
        print("\n------ Student Profile ------")
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Email      : {self.email}")

    def display_courses(self):
        print(f"\nCourses enrolled by {self.name}:")

        if not self.enrolled_courses:
            print("No courses enrolled.")
            return

        for course in self.enrolled_courses:
            print(f"- {course.course_name}")

            

        
