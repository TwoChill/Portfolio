number = int(input("Kies een number: "))
num_range = number + 1

for i in range(num_range):
	print("{0:>2} in binary is {0:>08b}".format(i))
