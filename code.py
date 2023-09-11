# Enter your friend names using comma
import random as ra

n = int(input("no.of friends to party:"))
li = input("Enter your friends name:")
g = li.split(',')
p = input("had you dinner?(y/n):")
if p=='y' or p=='Y':
    q = input("Ready to pay bill from random person?(y/n)")
    if(q=='y' or q=='Y'):
        ls = ra.randint(0,len(g)-1)
        print(f'Here is the person "{g[ls]}" will pay bill')
    else:
        print("ok,pay your bill as you like!")
else:
    print("please have your dinner")
