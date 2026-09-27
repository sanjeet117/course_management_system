from models.student import Student
from models.mentor import Mentor
from models.course import Course
from models.enrollment import Enrollment
from models.user import User 


def main():

    # Create Mentor
    mentor = Mentor(
        "U001",
        "Rahul Sharma",
        "rahul@example.com",
        "M001",
        "Python & Data Science"
    )

    # Create Students
    student1 = Student(
        "U002",
        "Amit Kumar",
        "amit@example.com",
        "S001"
    )

    student2 = Student(
        "U003",
        "Neha Patel",
        "neha@example.com",
        "S002"
    )

    # Create Course
    python_course = Course(
        "C001",
        "Python OOP",
        4999,
        mentor
    )

    # Display profiles
    student1.display_profile()
    mentor.display_profile()

    # Display course
    python_course.display_course()

    # Enroll students
    student1.enroll_course(python_course)
    student2.enroll_course(python_course)

    # Create enrollment records
    enrollment1 = Enrollment(student1, python_course)
    enrollment2 = Enrollment(student2, python_course)

    # Display enrolled courses
    student1.display_courses()
    student2.display_courses()

    # Display enrollment details
    enrollment1.display_enrollment()
    enrollment2.display_enrollment()

    # Display class-level counts
    print("\n------ System Statistics ------")
    print(f"Total Users       : {User.get_total_users()}")
    print(f"Total Courses     : {Course.get_total_courses()}")
    print(f"Total Enrollments : {Enrollment.get_total_enrollments()}")


if __name__ == "__main__":
    main()