# Source: https://stackoverflow.com/questions/5290994/remove-and-replace-printed-items#5291396

import time

for x in range(0, 5):
    b = "Loading" + "." * x
    print(b, end="\r")
    time.sleep(.5)
