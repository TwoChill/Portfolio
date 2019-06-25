#______________________________________________________________________________#
#______________________________________________________________________________#

name = "Boolean Expression Quiz"

# Exercise 27 is all about memorizing logic statements.
# I thought it would be a good practice for me to try out to make
# little program to help me study these booleans.

import random
import time                                                                     # to delay closing window afther input == 'quit'.
#______________________________________________________________________________#

dic_quiz = {
"not False": "True",
"not True": "False",

"True or False": "True",
"True or True": "True",
"False or True": "True",
"False or False": "False",

"True and False": "False",
"True and True": "True",                                                        # Dictonary with questions on the left
"False and True": "False",                                                      # and the answers to the right.
"False and False": "False",

"not(True or False)": "False",
"not(True or True)": "False",
"not(False or True)": "False",
"not(False or False)": "True",

"not(True and False)": "True",
"not(True and True)": "False",
"not(False and True)": "True",
"not(False and False)": "True",

"1 != 0": "True",
"1 != 1": "False",
"0 != 1": "True",
"0 != 0": "False",

"1 == 0": "False",
"1 == 1": "True",
"0 == 1": "False",
"0 == 0": "True",
}
#______________________________________________________________________________#

print("\n")
print("=" * len(name),f"\n{name}")
print("=" * len(name))
#______________________________________________________________________________#

def range_a(string):
    a = string[0]
    return a

def range_b(string):
    b = string[1]
    return b


def quiz_questions(randomnr):
    correct_answerd = 0
    total_answerd = 0
    incorrect_answerd = total_answerd - correct_answerd
    grade = 0

    list_value = [v for v in dic_quiz]                                          # Source: quora.com/
                                                                                # How-do-I-convert-a-dictionary-to-a-list-in-Python
    all_questions = 2,25
    _or_ = 2,5
    _and_ = 6,9
    or_and = 2,9
    not_or = 10,13                                                              # Range values to pass into the function later.
    not_and = 14,17                                                             # Users can choose between questions (ranges).
    not_or_not_and = 10,17
    not_equal = 18,21
    equal_to = 22,25
    not_equal_and_equal_to = 18,25
#______________________________________________________________________________#

    try:                                                                        # This print block is to prompt user to choose a catagory.
        ranges = int(input(('''
        Which do you want to learn?
        ===========================

         1. All Questions
         2. Or
         3. And
         4. Or & And
         5. Not(_or_)
         6. Not (_and_)
         7. Not(_or_) & Not (_and_)
         8. Not Equal (!=)
         9. Equal To (==)
        10. Not Equal (!=) & Equal To (==)

        :> ''')))

        if ranges == 1:
            print("\n\t:> All Questions")
            ranges = all_questions
        elif ranges == 2:
            print("\n\t:> Or")
            ranges = _or_
        elif ranges == 3:
            print("\n\t:> Or & And")
            ranges = _and_
        elif ranges == 4:
            print("\n\t:> Or & And")
            ranges = or_and                                                     # This block is used to 'convert' the users chooice,
        elif ranges == 5:                                                       # to the corrospondig range our program uses.
            print("\n\t:> Not(_or_)")
            ranges = not_or
        elif ranges == 6:
            print("\n\t:> Not (_and_)")
            ranges = not_and
        elif ranges == 7:
            print("\n\t:> Not(_or_) & Not (_and_)")
            ranges = not_or_not_and
        elif ranges == 8:
            print("\n\t:> Not Equal (!=)")
            ranges = not_equal
        elif ranges == 9:
            print("\n\t:> Equal To (==)")
            ranges = equal_to
        elif ranges == 10:
            print("\n\t:> Not Equal (!=) & Equal To (==)")
            ranges = not_equal_and_equal_to
        else:
            print("\n\t:> All Questions")
            ranges = all_questions
    except ValueError:
        print("\n\t:> All Questions")
        ranges = all_questions                                                  # Error handeling incase another integer has been given.
#______________________________________________________________________________#

    print("\n")
    print("=" * 32)
    print("Type 'quit' or 'result' to exit!")
    print("=" * 32)


    while True:
        previous_randomnr = randomnr
        reminder_count = 0                                                      # reminder_count is used to skip the 'remember to type quit' print function twice.

        randomnr = random.randint(range_a(ranges),range_b(ranges))              # Random number generated which correlates to a random question being asked.
        if (previous_randomnr == randomnr) and (reminder_count == 1):
            reminder_count == 0
            continue
        elif previous_randomnr == randomnr:                                     # This will prevent the program from asking the same question (randomnr) right afther each other.
            print("Type 'quit' or 'result' to exit!")
            reminder_count += 1
            continue
#______________________________________________________________________________#

        question = list_value[randomnr]                                         # This will match the randomnr with a question in {dic_quiz}.
#______________________________________________________________________________#

        print("\n\nQuestion:\t-->\t{}".format(question))
        try:
            answer = input("Evaluates to?:\t-->\t").capitalize()
        except:
            if KeyboardInterrupt:
                exit()
#______________________________________________________________________________#
#______________________________________________________________________________#

        if (answer == "Quit" or answer == "Result") and (grade <= 9):

            print(f'''
      ==================================
      Boolean Expression Quiz -  Results:
      ==================================
     |       Correct Answerd:    {correct_answerd}      |
     |       Incorrect Answerd:  {incorrect_answerd}      |
     |       Total Questions:    {total_answerd}      |
     |                                  |
     |       Your Grade:         {grade}      |
      ==================================
    ''')
            print("Press CTRL + C to quit.")
            try:
                time.sleep(15)
                exit()
            except:
                if KeyboardInterrupt:
                    exit()

        elif (answer == "Quit" or answer == "Result") and (grade == 10):

            print(f'''
     ==================================
     Boolean Expression Quiz -  Results:
     ==================================
    |       Correct Answerd:    {correct_answerd}      |
    |       Incorrect Answerd:  {incorrect_answerd}      |
    |       Total Questions:    {total_answerd}      |
    |                                  |
    |       Your Grade:        {grade}      |
    ==================================
    ''')
            print("Press CTRL + C to quit.")
            try:
                time.sleep(15)
                exit()
            except:
                if KeyboardInterrupt:
                    exit()
#______________________________________________________________________________#

        if answer == '':
            while answer == '':
                try:
                    answer = input("Evaluates to?:\t-->\t").capitalize()
                except:
                    if KeyboardInterrupt:
                        #print("This is it")
                        exit()
                if (answer == "Quit" or answer == "Result") and (grade <= 9):

                    print(f'''
     ==================================
     Boolean Expression Quiz -  Results:
     ==================================
    |       Correct Answerd:    {correct_answerd}      |
    |       Incorrect Answerd:  {incorrect_answerd}      |
    |       Total Questions:    {total_answerd}      |
    |                                  |
    |       Your Grade:         {grade}      |
    ==================================
    ''')
                    print("Press CTRL + C to quit.")
                    try:
                        time.sleep(15)
                        exit()
                    except:
                        if KeyboardInterrupt:
                            exit()

                elif (answer == "Quit" or answer == "Result") and (grade == 10):

                    print(f'''
     ==================================
     Boolean Expression Quiz -  Results:
     ==================================
    |       Correct Answerd:    {correct_answerd}      |
    |       Incorrect Answerd:  {incorrect_answerd}      |
    |       Total Questions:    {total_answerd}      |
    |                                  |
    |       Your Grade:        {grade}      |
    ==================================
    ''')
                    print("Press CTRL + C to quit.")
                    try:
                        time.sleep(15)
                        exit()
                    except:
                        if KeyboardInterrupt:
                            exit()
            else:
                if answer == dic_quiz.get(question):
                    print("\n\n\t\t\t\tCORRECT!\n\t\t\t\t========")
                    correct_answerd += 1
                    total_answerd += 1


                else:
                    print("\n\n\t\t\t\tINCORRECT!!\n\t\t\t===========")
                    print("\nCorrect answer:\t-->\t", dic_quiz.get(question).upper(), "\n\t\t\t", ("=" * len(dic_quiz.get(question))))
                    total_answerd += 1


                previous_randomnr = randomnr
                grade = int(correct_answerd * 10 / total_answerd)
                continue
#______________________________________________________________________________#
#______________________________________________________________________________#

        if answer == dic_quiz.get(question):
            print("\n\n\t\t\t\tCORRECT!\n\t\t\t\t========")
            correct_answerd += 1
            total_answerd += 1


        else:
            print("\n\n\t\t\t\tINCORRECT!!\n\t\t\t\t===========")
            print("\nCorrect answer:\t-->\t", dic_quiz.get(question).upper(), "\n\t\t\t", ("=" * len(dic_quiz.get(question))))
            total_answerd += 1


        previous_randomnr = randomnr
        grade = int(correct_answerd * 10 / total_answerd)
#______________________________________________________________________________#
#______________________________________________________________________________#

randomnr = random.randint(0,26)
quiz_questions(randomnr)
