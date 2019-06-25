def convertword(convertedMSG):

    convertedMSG = convertedMSG.split(",")

    for words in convertedMSG:
        for letters in ISHvowelList[1]:
            if letters in words:
                replace = secretWord + letters.upper()
                words = words.replace(letters, replace)

        for word in words:
            for letter in words:
                if letter in ISHvowelList[0]:
                    replace = secretWord + letter.upper()
                    words = words.replace(letter, replace)

    #words = words.replace(".",".\n")
    # print(">>> This is end of conversion: ", words)
    return words



convertedMSG = str(input("Please enter your message:\n\n"))

ISHvowelList = (
  ("a", "e", "o", "u", "i", "y"),
  ("oei", "aa", "ee", "oo", "uu", "au", "ei", "eu", "ie", "ou", "oe", "ui", "ij","io")
)

secretWord = "ISH"

convertedMSG = convertedMSG.replace(",","").lower().split(" ")

new_converterdMSG = []
for index in range(0,(len(convertedMSG))):
    new_converterdMSG.append(convertword(convertedMSG[index]))


print("\n\nYour message in " + secretWord + ": \n")
print(" ".join(new_converterdMSG).capitalize())


# again =  "N"
# while again == "N":
# 	again = (input("Do you want to convert another message to ISH? Y/N: "))
# 	again = again.capitalize()
# 	if again == "N":
# 		print("\nThank you, and goodbye!")
# 		break
# 	if again == "Y":
# 		convert2ish(convertedMSG = (input("\n\nWich message do you want to convert again to ISH?:\n\n")))
# 		again = "N"
# 	else:
# 		print("Please use only \"N\" or \"Y\":\n")
# 		again = "N"
