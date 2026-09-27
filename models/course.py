class Course:

    total_courses = 0

    def __init__(self, course_id, course_name, price, mentor):
        if not Course.is_valid_price(price):
            raise ValueError("Course price must be greater than 0.")

        self.course_id = course_id
        self.course_name = course_name
        self.price = price
        self.mentor = mentor
        self.students = []

        Course.total_courses += 1

    @staticmethod
    def is_valid_price(price):
        return price > 0

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def display_course(self):
        print("\n------ Course Details ------")
        print(f"Course ID   : {self.course_id}")
        print(f"Course Name : {self.course_name}")
        print(f"Price       : ₹{self.price}")
        print(f"Mentor      : {self.mentor.name}")
        print(f"Students    : {len(self.students)}")

    @classmethod
    def get_total_courses(cls):
        return cls.total_courses