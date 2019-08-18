import itertools
import time

from tqdm.auto import tqdm

print('\n++++++++++++++++++++++++ Wordlist Gen +++++++++++++++++++++++++\n')


char = input("\t[+] Please Enter Here All Word For Combination :> ")
print('\n')
rng1 = int(input("\t[+] Please Enter Minimum Lenth Of Words :> "))
print('\n')
rng2 = int(input("\t[+] Please Enter Maximum Lenth Of Words :> "))
print('\n')

exclude = int(
    input("\t[+] Please Enter Sequential Charachter Exclution :> "))
exclude -= 1
if exclude < 0:
    exclude = len(char)

time1 = time.asctime()
start = time.time()
print('\n')
output_file = input("\t[+] Please Enter The Path Of Wordlist File :> ")
print('\n')

# A for-loop to calculate max number of line in output_file.
# What needs to happen is INCLUDE 'exclude' in the math.
p = []
for lines in range(rng1, (rng2 + 1)):
    # FIX THIS MATH PROBLEM!
    ans = ((len(char)**lines) - (exclude ** rng1)) - rng1
    p.append(ans)
tline = sum(p)
print("\t[+] Numbers Of Total Lines :> ", tline, "\n\n")

input('\r\r\t[+] Are You Ready? [Press Enter]')

print('\n++++++++++++++++++++++++ Please Wait +++++++++++++++++++++++++\n')

wordList = open(output_file, 'a')
loop = tqdm(total=tline, position=0)

for i in range(len(char), (len(char) + 1)):
    for xt in itertools.product(char, repeat=i):
        loop.set_description('Progress')
        cnts = [sum(1 for i in grp[1]) for grp in itertools.groupby(xt)]
        if max(cnts) > exclude:
            loop.update()
            print('EXCLUDE:', xt)
            continue
        wordList.write(''.join(xt) + '\n')
        loop.update()
wordList.close()
loop.close()

print("\nDone Sucessfully\n")

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
