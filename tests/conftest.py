import os, sys
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")


import pytest
# import src.shapes_inheritance as shapes


from src.school import Classroom, Teacher, Student, TooManyStudents

# --------------------------
# 🏰 Hogwarts Fixtures
# --------------------------
@pytest.fixture
def professor_mcgonagall():
    return Teacher("Professor McGonagall")

@pytest.fixture
def golden_trio():
    return [
        Student("Harry Potter"),
        Student("Hermione Granger"),
        Student("Ron Weasley")
    ]


## Monkeypatch fixes the typo in add_student like a spell correction :(
# @pytest.fixture
# def defense_class(professor_mcgonagall, golden_trio, monkeypatch):
#     monkeypatch.setattr(Classroom, "add_student", 
#         lambda self, student: self.students.append(student) 
#         if len(self.students) < 10 
#         else TooManyStudents()
#     )

#     return Classroom(
#         teacher=professor_mcgonagall,
#         students=golden_trio,
#         course_title="Defense Against the Dark Arts"
#     )


@pytest.fixture
def defense_class(professor_mcgonagall, golden_trio):
    return Classroom(
        teacher=professor_mcgonagall,
        students=golden_trio,
        course_title="Defense Against the Dark Arts"
    )



