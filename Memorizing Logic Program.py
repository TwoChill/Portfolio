## Truth or False Quiz ##

# Exercise 27 is all about memorizing logic statements.
# I thought it would be a good practice for me to try out to make
# little program to help me study these booleans.

import random

dic_quiz = {
"not False": "True",
"not True": "False",

"True or False": "True",
"True or True": "True",
"False or True": "True",
"False or False": "False",

"True and False": "False",
"True and True": "True",                                                  # <-- Dictonary with questions on the left
"False and True": "False",                                                # <-- and the answers to the right.
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

print("\nTruth or False Quiz")

def range_a(string):
    a = string[0]
    return a

def range_b(string):
    b = string[1]
    return b


def quiz_questions(randomnr):
    answerd = 0
    total = 0

    list_value = [v for v in dic_quiz]     # <---         Source: quora.com/How-do-I-convert-a-dictionary-to-a-list-in-Python

    all_questions = 2,25
    _or_ = 2,5
    _and_ = 6,9
    or_and = 2,9
    not_or = 10,13                                                 # <--            Range values to pass into the function later.
    not_and = 14,17                                                # <--            Users can choose between questions (ranges).
    not_or_not_and = 10,17
    not_equal = 18,21
    equal_to = 22,25
    not_equal_and_equal_to = 18,25

    try:                                                           # <--            This print block is to prompt user to choose a catagory.
        ranges = int(input(('''
        Which do you want to learn?

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
            ranges = all_questions
        elif ranges == 2:
            ranges = _or_
        elif ranges == 3:
            ranges = _and_
        elif ranges == 4:
            ranges = or_and                                                     # This block is used to 'convert' the users chooice,
        elif ranges == 5:                                                       # to the corrospondig range our program uses.
            ranges = not_or
        elif ranges == 6:
            ranges = not_and
        elif ranges == 7:
            ranges = not_or_not_and
        elif ranges == 8:
            ranges = not_equal
        elif ranges == 9:
            ranges = equal_to
        elif ranges == 10:
            ranges = not_equal_and_equal_to
    except:
        if ValueError:
            print("\nWhat?! I didn't get that.\nI've choosen number 1 for you.\n")
            ranges = all_questions                                              # Error handeling incase another integer has been given.


    print("\n\n### !Don' forget to type 'quit' to exit! ###")


    while True:
        previous_randomnr = randomnr
        randomnr = random.randint(range_a(ranges),range_b(ranges))              # Random number generated which corrolates to random question asked.
        question = list_value[randomnr]
        if previous_randomnr == randomnr:
            continue

        print("\nQuestion:\t-->\t{}".format(question))                          # print("\nQuestion:\t-->\t{}\trandomnr:{}\tduplicateNR:{}".format(question,randomnr, duplicate_randomnr))
        answer = input("True or False?:\t-->\t").capitalize()


        if answer == "Quit":
            try:
                print("\n\n\nCorrect Answerd:\t{}\nTotal Questions:\t{}\n\nYour grade is:\t\t{}".format(answerd, total, grade))
                if grade <= 5:
                    print("\n\nYou should study WAY more!\n\nRESTART this program!\nAND TRY AGAIN!\n")
                elif (grade >= 6) and (grade <= 8):
                    print("\n\nYou've done a great job.\n\nKeep practicing though!")
                else:
                    print("\n\nEXCELLENT! EXCELLENT! EXCELLENT!\n\n\nGreat job in getting a ", grade, "!\nHow Try Again and beat your best!\n" )
                break
            except:
                if ZeroDivisionError:
                    print("\nWell, You tried.\nRestart me to try again.\n")
                    break

        elif answer == '':
            while answer == '':
                answer = input("True or False?:\t-->\t").capitalize()
                if answer == "Quit":
                    break
            try:
                print("\n\n\nCorrect Answerd:\t{}\nTotal Questions:\t{}\n\nYour grade is:\t\t{}".format(answerd, total, grade))
                if grade <= 5:
                    print("\n\nYou should study WAY more!\n\nRESTART this program!\nAND TRY AGAIN!\n")
                elif (grade >= 6) and (grade <= 8):
                    print("\n\nYou've done a great job.\n\nKeep practicing though!")
                else:
                    print("\n\nEXCELLENT! EXCELLENT! EXCELLENT!\n\n\nGreat job in getting a ", grade, "!\nHow Try Again and beat your best!\n" )
                break
            except:
                if ZeroDivisionError:
                    print("\nWell, You tried.\nRestart me to try again.\n")
                    break


        if randomnr == previous_randomnr:
            if total == 0:
                total = 0
            else:
                total -= 1
                continue


        elif answer == dic_quiz.get(question):
            print("\t\t\t\t\tCORRECT!")
            answerd += 1
            total += 1
        else:
            print("\t\t\t\t\tNOT CORRECT!!")
            total += 1

        previous_randomnr = randomnr
        grade = int(answerd * 10 / total)



randomnr = random.randint(0,26)
quiz_questions(randomnr)
