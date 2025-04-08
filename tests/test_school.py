import os, sys
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")

# sys.path (list of paths): (adding the up one folder of the script path)
# ['..', 'C:/Python_Rust_Removal/PytestPotterSchool_AI/tests', , , , , ,  ...]

import pytest
from src.school import Classroom, Teacher, Student, TooManyStudents, Person

def test_class_initialization(defense_class):
    assert defense_class.teacher.name == "Professor McGonagall"
    assert len(defense_class.students) == 3
    assert defense_class.course_title == "Defense Against the Dark Arts"

def test_change_professor(defense_class):
    defense_class.change_teacher(Teacher("Professor Snape"))
    assert defense_class.teacher.name == "Professor Snape"

# --------------------------
# 📜 Enrollment Scroll Tests
# --------------------------
@pytest.mark.parametrize("student_name", [
    "Ginny Weasley",
    "Luna Lovegood",
    "Neville Longbottom"
])
def test_add_students(defense_class, student_name):
    initial_count = len(defense_class.students)
    defense_class.add_student(Student(student_name))
    assert len(defense_class.students) == initial_count + 1
    print(defense_class.students[-1].name) # for my devug

def test_overflow_classroom(defense_class):
    # Add 7 more students to reach 10
    for _ in range(7):
        defense_class.add_student(Student("Hogwarts Student"))
    
    print(len(defense_class.students)) # my debug

    # Attempt to add 11th student - should trigger the Dark Mark! ☠️
    with pytest.raises(TooManyStudents):
    # with pytest.raises(TooManyStudents, match="The Chamber of Secrets has limited space!"):
        defense_class.add_student(Student("Draco Malfoy"))

# --------------------------
# 🗡️ Vanishing Cabinet Tests
# --------------------------
def test_remove_student(defense_class):
    defense_class.remove_student("Harry Potter")
    assert len(defense_class.students) == 2
    assert all(s.name != "Harry Potter" for s in defense_class.students)

def test_remove_nonexistent_student(defense_class):
    initial_students = defense_class.students.copy()
    defense_class.remove_student("Lord Voldemort")
    assert defense_class.students == initial_students

# --------------------------
# 🦉 Owl Post Notifications
# --------------------------
def test_student_creation():
    student = Student("Cho Chang")
    assert student.name == "Cho Chang"
    assert isinstance(student, Person)

def test_teacher_creation():
    teacher = Teacher("Albus Dumbledore")
    assert teacher.name == "Albus Dumbledore"
    assert isinstance(teacher, Person)