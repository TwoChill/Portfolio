import itertools
import sys
import time

from tqdm.auto import tqdm

print('\n++++++++++++++++++++++++ Wordlist Gen +++++++++++++++++++++++++\n')


char = input("\t[+] Please Enter Here All Word For Combination :> ")
print('\n')
rng1 = int(input("\t[+] Please Enter Minimum Lenth Of Words :> "))
print('\n')
rng2 = int(input("\t[+] Please Enter Maximum Lenth Of Words :> "))
print('\n')

charLen = len(char[rng1:(rng2 + 1)])
# print(charLen)
exclude = int(
    input("\t[+] How Much Sequential Charachter Should Be Excluded? :> "))

# Needs to be there because it will remove the correct amout of sequentail characters.
exclude -= 1
# I Think this part breaks stuff up
if exclude <= 0:
    exclude = charLen # Check if this is the correct way

time1 = time.asctime()
start = time.time()
print('\n')
output_file = input("\t[+] Please Enter The Path Of Wordlist File :> ")
print('\n')

# EXCLUDE NR. is not GIVEN.
if exclude == charLen:
    p = []
    for lines in range(rng1, (rng2 + 1)):
        ans = ((len(char)**lines))
        p.append(ans)
    tline = sum(p)

# EXCLUDE NR. is GIVEN.
else:
    l = charLen - (exclude - 1)
    repeat = 1
    p = []
    for i in range(1, (l + 1)):
        ans = (l + 1) ** repeat
        # print(f'{l + 1} ** {r} = {ans}')
        repeat *= 2
        p.append(ans)
    # Sorts items in list [p] in a descending order.
    p = p[::-1]
    # Subtracts items in list [p].
    tline = p[0] - sum(p[1:])


print("\t[+] Numbers Of Total Lines :> ", tline, "\n\n")

input('\r\r\t[+] Are You Ready? [Press Enter]')

print('\n++++++++++++++++++++++++ Please Wait +++++++++++++++++++++++++\n')

wordList = open(output_file, 'a')
loop = tqdm(total=tline, position=0)

for i in range(rng1, (rng2 + 1)):
    for xt in itertools.product(char, repeat=i):
        loop.set_description('Progress..')
        if exclude != charLen:
            cnts = [sum(1 for i in grp[1]) for grp in itertools.groupby(xt)]
            if max(cnts) > exclude:
                loop.update()
                continue
        wordList.write(''.join(xt) + '\n')
        loop.update()
wordList.close()
loop.close()

sys.stdout.write("\nDone Sucessfully\n")

print('\n\n+++++++++++++++++++++++ Process Report +++++++++++++++++++++++\n')

print('\t [+] Process Started                      :   ', time1)
end = time.time()
print('\t [+] Process Completed                    :   ', time.asctime())
totaltime = end - start
print('\t [+] Total Time Consumed                  :   ', totaltime, 'seconds')
rate = tline / totaltime
print('\t [+] Rate Of Words Generating Per Seconds :   ', rate)

print('\n++++++++++++++++++++++++ Please Wait +++++++++++++++++++++++++\n')

print('''
\t***************************************************
\t*       Successfully created thanks for using     *
\t***************************************************

''')
print('\n')
input("[*] Press Enter For Exit")
