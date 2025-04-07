

class TooManyStudents(Exception):
	pass		



class Classroom(object):
	"""docstring for Classroom"""
	def __init__(self, teacher, students, course_title):
		self.teacher = teacher
		self.students = students # a list of students in class (list of Student Classe Objects)
		self.course_title = course_title


	def add_student(self, student):
		if len(self.students) < 10:
			self.students.append(student)
		else:
			raise TooManyStudents
		

	def remove_student(self, name):
		for student in self.students:
			if student.name == name:
				self.students.remove(student)
				break
		

	def change_teacher(self, new_teacher):
		self.teacher = new_teacher



class Person(object):
	"""docstring for ClassName"""
	def __init__(self, name):
		self.name = name
		
 

		
class Teacher(Person):
	pass



class Student(Person):
	pass


# prompt:
# using pytest and its functions, such as fixtures parametrize raises and mark, wherever necessary, test the following code and theme it after Harry Potter:


# in addtion to the test packadge, perplexity also provided the following notes:
# Key magical enhancements:

# Fixtures create Hogwarts staff and students

# Monkeypatch fixes the typo in add_student like a spell correction

# Parametrized tests for multiple student additions

# Custom exception message for classroom overflow

# Tests check both successful and cursed operations

# Harry Potter-themed names throughout

# To run these tests: pytest test_hogwarts.py -v (recommended to use a phoenix feather core wand for optimal performance) 🔥

# Remember: These tests will pass only after fixing the original code's typos (studenst → students, breal → break). The monkeypatch in the defense_class fixture handles this during test execution like a proper house-elf! 
# (errors that were already fixed!)