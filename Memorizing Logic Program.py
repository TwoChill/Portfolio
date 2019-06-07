## Truth or False Quiz ##

# Exercise 27 is all about memorizing logic statements.
# I thought it would be a good practice for me to try out to make
# little program to help me study these booleans.



import random
        # choice wiht ranges
dic_quiz = {
"not False": "True",
"not True": "False",

"True or False": "True",
"True or True": "True",
"False or True": "True",
"False or False": "False",

"True and False": "False",
"True and True": "True",
"False and True": "False",
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

def quiz_questions(randomnr):
    answerd = 0
    total = 0
    duplicate_randomnr = randomnr

    while True:
        list_value = [v for v in dic_quiz]     # <---         Source: quora.com/How-do-I-convert-a-dictionary-to-a-list-in-Python

        question = list_value[randomnr]
        print("\t\t\t\t\t\t\tType 'quit' to exit!")
        print("\nQuestion:\t-->\t{}".format(question))

        answer = input("True or False?:\t-->\t").capitalize()
        randomnr = random.randint(0,7)

        if answer == "Quit":
            try:
                print("\n\n\nYou've correctly answerd {} out of {} questions.\n\nYour grade is a:".format(answerd, total), grade, "\n")
                if grade <= 5:
                    print("\nYou should study WAY more!\n\nRESTART this program!\nAND TRY AGAIN!\n")
                elif 5 > grade <= 8:
                    print("\nYou've done a great job.\n\nKeep practicing though!")
                else:
                    print("\nEXCELLENT!\n\nGreat job in getting a ", grade, "!\nHow Try Again and beat your best!" )
                break
            except:
                if ZeroDivisionError:
                    print("Well, that was quick!\n!!Game Over!!")
                    break
        elif answer == '':
            while answer == '':
                answer = input("Enter your answer : ").capitalize()
                if answer == "Quit":
                    break

        if randomnr == duplicate_randomnr:
            total -+ 2

        elif answer == dic_quiz.get(question):
            print("\t\t\t\t\tCORRECT!")
            answerd += 1
            total += 1
        else:
            print("\t\t\t\t\tNOT CORRECT!!")
            total += 1

        grade = int(answerd * 10 / total)



randomnr = random.randint(0,7)
quiz_questions(randomnr)
