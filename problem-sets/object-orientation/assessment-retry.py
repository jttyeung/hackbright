# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """ Defines a student. """

    def __init__(self, firstname, lastname, address):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address


class Question(object):
    """ Defines a question. """

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self, question):
        print self.question
        answer = raw_input('> ')
        print answer == self.correct_answer


class Exam(object):
    """ Defines an exam. """

    def __init__(self, name):
        self.questions = []

    def addQuestion(self, question, correct_answer):
        question = Question(question, correct_answer)
        self.questions.append(question)

    def administer(self):
        score = 0
        for question in self.questions:
            if Question.ask_and_evaluate(self, question) == True:
                score += 1
        percent = int(float(score)/len(self.questions) * 100)
        return percent


class Quiz(Exam):
    def administer(self):
        score = 0
        for question in self.questions:
            if Question.ask_and_evaluate(self, question) == True:
                score += 1
        percent = int(float(score)/len(self.questions) * 100)
        if percent > 50:
            return 'pass'
        else:
            return 'fail'


def take_test(Exam, Student):
    """ Administers student exam and assigns score. """

    Student.score = Exam.administer()
    print Student.score


def example():
    """ Runs sample exam with sample student. """

    example = Exam('example')
    example.addQuestion('How many licks does it take to get to the center of the lollipop?', 3)
    example.addQuestion('How much wood could a wood chuck chuck if a wood chuck could chuck wood?', '700 pounds')
    example.addQuestion('What is the air-speed velocity of an unladen swallow?', 'an African or European swallow?')
    student = Student('hello', 'jane', 'jane\'s address')
    take_test(example, student)
