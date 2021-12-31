"""
THIS PROGRAM WAS CREATED TO HELP ME STUDY FOR MY HAM TECHNICIAN EXAM.
I SCRAPED THE QUESTIONS FROM THE TECHNICIAN EXAM QUESTION POOL AT https://arrl.org WITH THE Scrape_ARRL_Questions.py SCRIPT FROM ARRL_Questions.txt .
IT GRABS QUESTIONS FROM TEXT FILES IN res/Sections AND ASKS FOR INPUT TO COMPARE.

@author - Manvel Beaver
"""

import os
import re
import time
from bs4 import BeautifulSoup

""" HELPER FUNCTIONS """
def getEncoding(path_to):
    with open(path_to) as file:
        return file.encoding

def getData(path_to):
    with open(path_to, encoding=getEncoding(path_to_file)) as file:
        que = str(BeautifulSoup(file, "html.parser"))
        file.close()
    return que

def getSectionSize(path_to):
    return len([name for name in os.listdir(path_to) if os.path.isfile(os.path.join(path_to, name))])

def getQuestion(dat):
    return re.split('\n', dat)[2]

def getChoices(dat):
    return re.split('\n', dat)[3:]

def getDecision():
    return str(input("Decision? "))

def getAnswer(dat):
    secondine = re.split('\n', dat)[1]
    answe_par = re.split('\s', secondine)[1]
    answe = re.split('\)', re.split('\(', answe_par)[1])[0]
    return answe

def getScore(inpu, answ, scor):
    if inpu == answ:
        scor +=1
    else:
        scor -=1

def removeFromString(str, ind):
    tail = len(str)-1
    if ind is 0:
        return str[1:]
    if ind is tail:
        return str[0:tail]
    else:
        return str[0:ind]+str[(ind+1):]

""" DISPLAY FUNCTIONS """

""" FUNCTION FOR DISPLAYING PROGRAM BANNER """
def Program_Display():
    print(""" 
@===========================================================================@
|                                                                           |
|    ____                  _   _               __  __       _               |
|   / __ \                | | (_)             |  \/  |     | |              |
|  | |  | |_   _  ___  ___| |_ _  ___  _ __   | \  / | __ _| | _____ _ __   |
|  | |  | | | | |/ _ \/ __| __| |/ _ \| '_ \  | |\/| |/ _` | |/ / _ \ '__|  |
|  | |__| | |_| |  __/\__ \ |_| | (_) | | | | | |  | | (_| |   <  __/ |     |
|    \___\_\\__,_|\___||___/\__|_|\___/|_| |_| |_|  |_|\__,_|_|\_\___|_|     |
|                                                                           |
|                                                                           |                             
|                   Developed by: Manvel Beaver                             |
@===========================================================================@

         """)    

"""
FUNCTION TO DISPLAY COMPONENTS NEEDED FOR USER TO DETERMINE WHERE THEY ARE IN THE QUIZ IN TERMS OF SECTION, SCORE, AND QUESTION ITS ASKING
"""

def Score_Display(Section_Num, Question_Num, Section_Si, Right_Ans, Wrong_Ans, Problem, Choices):
    print("")
    print("================================================>")
    print("")
    print("-----------------------------------------------")
    print("| SECTION: "+ Section_Num + "\tQuestion Number: "+ Question_Num +", OUT OF: "+ Section_Si +"|")
    print("-----------------------------------------------")
    print("")
    print("--------------------------------")
    print("| SCORE | CORRECT: "+ Right_Ans +" | WRONG: "+ Wrong_Ans +"|")
    print("--------------------------------")
    print("")
    print("Type 'exit' to end Quiz")
    print("")
    print("*** QUESTION ***")
    print("")
    print(Problem)

    print("")
    for choice in Choices:
        print(choice)
    print("")
    print("")


"""USER INTERFACE CLASSES"""

"""
CLASS TO HANDLE UI COMPONENTS
@class Player
"""
class Player:
    def __init__(self):
        self._right = 0
        self._wrong = 0
        self._playing = True

    def get_right(self):
        return self._right
    def set_right(self, a):
        self._right = a
    def del_right(self):
        del self._right

    def get_wrong(self):
        return self._wrong
    def set_wrong(self, c):
        self._wrong = c
    def del_wrong(self):
            del self._wrong

    def get_playing(self):
        return self._playing
    def set_playing(self, a):
        self._playing = a
    def del_playing(self):
        del self._playing

    right = property(get_right, set_right, del_right)
    wrong = property(get_wrong, set_wrong, del_wrong)
    playing = property(get_playing, set_playing, del_playing)

"""
CLASS TO STORE QUESTION COMPONENTS INTO OBJECTS
@class Question
"""
class Question:
    def __init__(self):
        self._problem = ""
        self._choices = []
        self._answer = ""

    def get_problem(self):
        return self._problem
    def set_problem(self, p):
        self._problem = p
    def del_problem(self):
        del self._problem

    def get_choices(self):
        return self._choices
    def set_choices(self, c):
        self._choices = c
    def del_choices(self):
            del self._choices

    def get_answer(self):
        return self._answer
    def set_answer(self, a):
        self._answer = a
    def del_answer(self):
        del self._answer

    problem = property(get_problem, set_problem, del_problem)
    choices = property(get_choices, set_choices, del_choices)
    answer = property(get_answer, set_answer, del_answer)

"""MAIN METHOD"""
if __name__ == '__main__':

    Program_Display()

    """ 
    INITIALIZE PLAYER AND QUESTION CLASSES, 
    AS WELL AS LOCAL VARIABLES TO REPRESENT 
        NUMBER OF RIGHT ANSWER -> right, 
        NUMBER OF WRONG ANSWERS -> wrong, 
        NUMBER OF SECTIONS -> num_of_sections 
    """
    P = Player()
    Q = Question()
    right = 0
    wrong = 0
    num_of_sections = 10

    """ START WITH LOOP STATEMENT TO KEEP PROGRAM RUNNING """ 
    for i in range(num_of_sections):

        """ JUMP TO SECTION USER DESIRES """
        while True:
            i = int(input("Jump to section? [0-9]: "))
            if isinstance(i, int) and i > -1 and i < 10:
                break
            else:
                print("INPUT ERROR: Please enter an integer between 1 and 9.")

        section_folder = 'T'+str(i)
        path_to_folder = os.path.join('..', 'res', 'Sections', section_folder)
        section_size = getSectionSize(path_to_folder)

        """ WE WANT AN ARRAY TO STORE WRONG ANSWERS TO ASK AFTER ANSWERING ALL THE QUESTIONS FOR THE SECTION"""
        wrong_answer_arr = []
        section_jumped = False
        question_jumped_to = 0

        """ START WITH LOOP STATEMENT TO KEEP PROGRAM RUNNING """
        for k in range(section_size - 1):
            """ JUMP TO QUESTION USER DESIRES """
            while True and section_jumped is False:
                question_jumped_to = int(input("Jump to question? [1, "+ str(section_size) +"]: "))
                if isinstance(question_jumped_to, int) and question_jumped_to > -1 and question_jumped_to <= section_size:
                    section_jumped = True
                    break
                else:
                    print("INPUT ERROR: Please enter and integer between 1 and "+ str(section_size) +"")

            k += question_jumped_to

            """ SIMULATE WHILE LOOP """
            if k <= section_size:

                question_file = 'Question_'+str(k)+'.txt'
                question_directory = 'Question_'+str(k)
                path_to_file = os.path.join(os.getcwd(), '..', 'res', 'Sections', section_folder, question_file)

                valid_question = True
                try:
                    data = getData(path_to_file)
                except UnicodeDecodeError as e:
                    print(e)
                    valid_question = False
                if valid_question is True:

                    """ INITIALIZE Question CLASS VARIABLES """
                    Q.problem = getQuestion(data)
                    Q.choices = getChoices(data)
                    Q.answer = getAnswer(data)

                    """ CALL Display FUNCTION TO STATE PARAMETERS NEEDED FOR A QUIZ """
                    Score_Display(str(i), str(k), str(section_size), str(right), str(wrong), Q.problem, Q.choices)

                    """ CALL getDecision FUNCTION TO HANDLE USER INPUT """
                    decision = getDecision()
                    print("")

                    """ DETERMINE OUTCOME GIVEN decision """
                    if decision is str(Q.answer):
                        print("### CORRECT ###")
                        right+=1
                    elif decision == "exit":
                        print("Closing program")
                        exit()
                    else:
                        print("&$ WRONG $&")
                        wrong+=1
                        wrong_answer_arr.append(k)

                    """ WAIT FOR USER TO CONTEMPLATE DECISION """
                    time.sleep(1)
                    print("")
                    print("CORRECT ANSWER WAS: ", Q.answer)
                    print("")
                    print("")
                    print("")
                    time.sleep(2)
