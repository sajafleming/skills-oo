# 1. Student Class - creating this was simple

class Student(object):
    """Represents a student that could take an Exam or a Quiz

       Each instance of Student will have first name, last name and address attributes 
       """
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

# 2. Question - still pretty simple

class Question(object):
    """Represents a question that could appear on an Exam.

       Consists of a question and answer and includes functionality for asking
       the question and evaluating the answer.
       """
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        """Ask uses to answer question and return true or false"""
        user_answer = raw_input(self.question + " ")

        if user_answer == self.answer:
            return True
        else:
            return False

# 3. Exam

class Exam(object):
    """Represents an Exam that can have questions and answers added to it and can
       be administered and return a score of correct answers.

       Will create a list of Question instances that can later be evaluated with the
       ask_and_evaluate method in the Question class.
    """

    # This took a bit to figure out as I had never seen classes who didn't inherit
    # from one another interacting. It is still a bit confusing to me.

    def __init__(self, name):
        self.name = name
        self.questions = [] # list of Question instances

    def add_question(self, question, answer):
        """Will add a question and answer as a Question instance to questions list"""
        self.questions.append(Question(question, answer))
        #return self.questions --> intersting, showed me where it was stored in memory

    def administer(self):
        """Ask all questions in Exam and return the score"""
        score = 0

        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1

        return score



class Quiz(Exam):
    """Quizzes are almost the same as exams except the way that they calculate score.

       A Quiz will will inherit from Exam. The administer method is modified 
       to return either pass (True) or fail (False) on quiz, no score is returned
    """
    
    # use default init -- nothing special in the instantiation of a Quiz

    def administer(self):
        score = super(Quiz, self).administer()

        if score > (len(self.questions) / 2.0): # use float in case odd number of questions 
            return True
        else:
            return False


    # was not too difficult to add this subclass


# Part 4 - functions - yay functions

def take_test(exam, student):
    """Assigns a score to an instance of a Student based on how they perform on
       an instance of an Exam.
    """
    # new student attribute score is assigned to the score returned when the test 
    # is administered
    student.score = exam.administer()

    # added this printed line to make sure the score was coming through when calling
    # this function in the example function
    print "%s recieved a score of %s" % (student.first_name, student.score) 

def example():
    """Creates an Exam, adds questions to the exam, creates a Student and administers 
       the exam to the student retulting in a final score
    """
    # creates an instance of an Exam called test
    test = Exam('test')

    # adds questions and answers to test by using the add_question method
    test.add_question("What holiday is December 25?", "Christmas")
    test.add_question("What holiday is Febrauary 14th?", "Valentine's Day")

    # creates an instance of a Student -> hint: it's me =)
    sarah = Student('Sarah', 'Fleming', '1600 Pennsylvania Ave')

    # calls the take_test function with the instances of Exam and Student
    # will print the score that sarah got on the test
    take_test(test, sarah)
    
