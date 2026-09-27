from datetime import datetime


class Enrollment:

    total_enrollments = 0

    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.enrollment_date = datetime.now()

        Enrollment.total_enrollments += 1

    def display_enrollment(self):
        print("\n------ Enrollment Details ------")
        print(f"Student        : {self.student.name}")
        print(f"Course         : {self.course.course_name}")
        print(f"Enrollment Date: {self.enrollment_date}")

    @classmethod
    def get_total_enrollments(cls):
        return cls.total_enrollments