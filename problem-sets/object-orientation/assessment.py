"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
    Polymorphism: The ability to easy create different types of instances of an object.
    Encapsulation: Binding together of the data and its code so that data is hidden from external code that may change it.
    Abstraction: The ability to be able to understand the code at a 1,000 ft view without having to know what code is under the hood in the methods.


2. What is a class?
    A class is an encapsulated way to define an object and its attributes and methods.

3. What is an instance attribute?
    An instance attribute is an object's attribute that belongs to itself and not necessarily to its class.

4. What is a method?
    A function that resides inside a class.

5. What is an instance in object orientation?
   It is an object created using the class definitions.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute is an attribute that is shared with all instances, whereas an instance attribute is unique to itself. I would use a class attribute to encapsulate all the similar characteristics of several instance types. When calling an attribute of an object I would first look to see if the attribute is defined on the instance, if not then I would look to see if the attribute has been defined in the class.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """Defines a new student"""

    def __init__(self, firstname, lastname, address):
        """Creates a new student object"""
        self.firstname = firstname
        self.lastname = lastname
        self.address =  address


class Question(object):
    """Defines a new question"""

    def __init__(self, question, answer):
        """Creates a new question and answer"""
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        """Evaluates truthiness of answer to question"""
        student_answer = raw_input(self.question + ' > ')
        if student_answer == self.answer:
            return True
        else:
            return False


class Exam(Question):
    """Defines a new exam"""

    def __init__(self, name, type='exam'):
        """Return a new exam object"""
        self.name = name
        self.type = type
        self.questions = []

    def add_question(self, question, answer):
        """Adds a question to the exam"""
        self.questions.append(super(Exam, self).__init__(question, answer))

    def administer(self):
        """Scores the exam"""
        score = 0.0
        count = 1
        # for question in exam, ask and evaluate the question, adding 1.0 to the score for each correct answer and then dividing the score by the total number of questions asked
        for question in self.questions:
            if self.ask_and_evaluate() == True:
                score += 1.0
            count += 1

        if self.type == 'quiz':
            if score/count > 0.5:
                return 'Pass'
            else:
                return 'Fail'
        else:
            return score/count


def take_test(exam, student):
    """Administers exam to student"""

    student.score = exam.administer()
    return '{} scored a {} on the {}'.format(student.firstname, student.score, exam.name)


def example():
    """Example exam"""

    question_1 = Question('How many licks does it take to get to the center of the lollipop?', 3)
    question_2 = Question('How much wood could a wood chuck chuck if a wood chuck could chuck wood?', '700 pounds')
    question_3 = Question('What is the air-speed velocity of an unladen swallow?', 'an African or European swallow?')
    sample_student = Student('student_first', 'student_last', 'sample address')
    sample_exam = Exam('sample')
    sample_exam.add_question(question_1.question, question_1.answer)
    sample_exam.add_question(question_2.question, question_2.answer)
    sample_exam.add_question(question_3.question, question_3.answer)
    print take_test(sample_exam, sample_student)

