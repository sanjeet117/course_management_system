# Course Management System

A Python-based Course Management System developed using Object-Oriented Programming (OOP) concepts. The project demonstrates inheritance, encapsulation, polymorphism, abstraction, instance methods, static methods, and class methods.

The project also demonstrates a professional Git and GitHub workflow using feature branches, meaningful commits, Pull Requests, and merging.

---

## Project Description

The Course Management System is designed to manage students, mentors, courses, and course enrollments.

The system allows:

* Creating students and mentors
* Creating courses
* Assigning mentors to courses
* Enrolling students in courses
* Managing enrollment records
* Displaying student and mentor profiles
* Displaying course information
* Tracking total users, courses, and enrollments

---

## Project Architecture

```text
course_management_system/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── models/
    ├── user.py
    ├── student.py
    ├── mentor.py
    ├── course.py
    └── enrollment.py
```

---

## Classes

### 1. User

`User` is the abstract base class for the system.

Responsibilities:

* Store common user information
* Provide controlled access to user data
* Track total users
* Define the abstract `display_profile()` method

---

### 2. Student

`Student` inherits from `User`.

Responsibilities:

* Store student information
* Enroll in courses
* Display student profile
* Display enrolled courses

---

### 3. Mentor

`Mentor` inherits from `User`.

Responsibilities:

* Store mentor information
* Store area of expertise
* Display mentor profile

---

### 4. Course

`Course` manages course information.

Responsibilities:

* Store course details
* Assign a mentor
* Add students to a course
* Validate course price
* Track total courses

---

### 5. Enrollment

`Enrollment` manages the relationship between a student and a course.

Responsibilities:

* Store student and course information
* Store enrollment date
* Display enrollment details
* Track total enrollments

---

## OOP Concepts Demonstrated

### Abstraction

The `User` class is an abstract base class using `ABC` and `@abstractmethod`.

```python
@abstractmethod
def display_profile(self):
    pass
```

---

### Inheritance

`Student` and `Mentor` inherit from the `User` class.

```python
class Student(User):
    pass
```

```python
class Mentor(User):
    pass
```

---

### Encapsulation

User information is stored using private attributes.

```python
self.__name = name
self.__email = email
self.__user_id = user_id
```

Controlled read access is provided using `@property`.

```python
@property
def name(self):
    return self.__name
```

---

### Polymorphism

Both `Student` and `Mentor` implement the same method:

```python
display_profile()
```

but provide different implementations.

---

### Instance Methods

Methods such as:

```python
enroll_course()
display_profile()
display_course()
display_enrollment()
```

operate on object-specific data.

---

### Static Method

The `Course` class uses a static method to validate course prices.

```python
@staticmethod
def is_valid_price(price):
    return price > 0
```

---

### Class Method

Class methods are used to access class-level counters.

```python
@classmethod
def get_total_users(cls):
    return cls.total_users
```

Similar class methods are used for courses and enrollments.

---

## Features

* User management
* Student management
* Mentor management
* Course management
* Student enrollment
* Enrollment tracking
* Course price validation
* User/course/enrollment statistics
* OOP-based architecture
* Git feature branch workflow
* Pull Request workflow

---

## Technologies Used

* Python 3
* Object-Oriented Programming
* Git
* GitHub

### Python Modules Used

The project uses Python standard library modules:

* `abc` — Abstract Base Classes
* `datetime` — Enrollment date and time

No external Python packages are required.

---

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Navigate to the project

```bash
cd course_management_system
```

### 3. Run the application

```bash
python main.py
```

---

## Usage Example

The application creates:

* One mentor
* Two students
* One Python OOP course
* Two enrollment records

Example:

```text
------ Student Profile ------
Student ID : S001
Name       : Amit Kumar
Email      : amit@example.com

------ Mentor Profile ------
Mentor ID  : M001
Name       : Rahul Sharma
Email      : rahul@example.com
Expertise  : Python & Data Science

------ Course Details ------
Course ID   : C001
Course Name : Python OOP
Price       : ₹4999
Mentor      : Rahul Sharma
Students    : 0

Amit Kumar enrolled in Python OOP
Neha Patel enrolled in Python OOP
```

---

## Git and GitHub Workflow

The project follows a feature-based Git workflow.

```text
main
 │
 ├── feature/enrollment-improvement
 │        │
 │        ├── Code changes
 │        ├── Commit
 │        └── Push
 │
 ↓
Pull Request
 │
 ↓
Review
 │
 ↓
Merge into main
 │
 ↓
git pull origin main
```

### Important Git Commands

```bash
git init
git status
git branch
git switch -c feature/enrollment-improvement
git add .
git commit -m "Meaningful commit message"
git push -u origin feature/enrollment-improvement
git switch main
git pull origin main
git log --oneline --graph --all
```

---

## Project Statistics

The application displays:

```text
Total Users
Total Courses
Total Enrollments
```

These values are maintained using class variables and class methods.

---

## Author

Sanjeet Kumar

