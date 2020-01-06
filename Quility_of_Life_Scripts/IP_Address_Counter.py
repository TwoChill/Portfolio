# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.
#
# An IP address consists of 4 numbers, seperated from each other with a full stop. But
# your program should just count however many are entered
# Examples if the input you may get are:
#    127.0.0.1
#    .192.168.0.1
#     10.0123456.255
#     172.16
#     255
#
# So your program should work even with invalid IP Addresses. We're just intersted in the
# number of segments and how long each one is.
#
# Once you have a working program here are some more suggestions for invalid input to test:
#     .123.45.678.91
#     123.4567.8.9
#     123.156.289.10123456
#     10.10t.10.10
#    12.9.34.6.12.90
#     '' - that is, press enter without typing anything
#
#
# !!!!! This challenge is intended to practice for loops and if/else statements. !!!!!

#### THE CODE ####

# !!!Try and Except plus While loop. Use of numbers only !!! #

ip_num = input("Type an IP address: ")

# !!!Try and Except plus While loop. Use of numbers only !!! #

again = "Y"
while again == "Y":
    if not ip_num == "":
        print("\nYou entered IP address: \n{}\n".format(ip_num))
        ip_num = ip_num.split(".")
        segments = len(ip_num)
        len_seg = []

        print("This IP address has {} segments.\n".format(segments))

        for items in range(0, len(ip_num)):

            for char in ip_num:
                len_char = len(char)
                len_seg.append(len_char)
                if len(len_seg) > len(ip_num):
                    break
                items += 1
                if len_char >= 2:
                    print("Segment\t" + str(items) + "\thas " +
                          str(len_char) + "\tcharacters\t>>>\t\t" + char)
                else:
                    print("Segment\t" + str(items) + "\thas " +
                          str(len_char) + "\tcharacter \t>>>\t\t" + char)

        again = input("\nDo you want to enter another IP address? Y/N:\n")
        again = again.capitalize()
        if again == "Y":
            ip_num = input("Type an IP address: ")

    else:
        ip_num = input(
            "\nYou have not entered anything!!! \n\nPlease enter an IP address or this program will shutdow:\n")
        if ip_num == "":
            print("\nThis program will now shutdown!")
            break
        else:
            continue
else:
    print("\nThis program will now shutdown!")
