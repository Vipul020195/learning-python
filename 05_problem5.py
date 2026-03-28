def inch_to_cms(inch):
    return inch * 2.54

import sys
c = int(input("enter the length in inches : "))
sys.stdout.flush()

print(f"The corresponding value of CMS is {inch_to_cms(c)}")