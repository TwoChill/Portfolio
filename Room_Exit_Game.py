# Full version idea: Combine this code with GUI (if possible in Python, i dont know yet)



########################################################################################################################################
#                                                        PART OF AN EXERCISE
#                                                        ###################
locations = {0: "You are sitting in front of a computer learing Python",
			 1: "You are standing at the end of a road, a small brick building",
			 2: "You are at the top of a hill",
			 3: "You are inside a building, a well house for a stream",
			 4: "You are in a valley beside a stream",
			 5: "You are in the forest"}

exit = [{"Quit": 0},
		{"West": 2, "East": 3, "North": 5, "South": 4, "Quit": 0},
		{"North": 5, "Quit": 0},
		{"East": 1, "Quit": 0},
		{"West": 2, "North": 1, "Quit": 0},
		{"West": 2, "South": 1, "Quit": 0}]

#                                                        ###################
#                                                        PART OF AN EXERCISE
########################################################################################################################################

loc = 1
while True:
		print(str(loc) + ". " + (locations[loc]) + "\n")
		print("Your avalible exits are: ")

		avalibleExits = exit[loc]
		for direction in avalibleExits:
			room_Num = avalibleExits.get(direction)
			print(str(room_Num) +". " + str(direction))

		loc = int(input("\nWhich way do you want to go?: "))
		if loc == 0:
			print("\n*** Game Over ***")
			break
