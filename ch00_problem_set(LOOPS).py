# LOOPS (22pts TOTAL)
import random
# PROBLEM 1 (Fibonacci - 4pts)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.
sting=1
zgolemi=0
zbirt=1
while sting<=1000:
    zbir+=sting
    sting=sting+zgolemi
    zgolemi+=sting
    print(sting)


# PROBLEM 2 (Number Guessing Game - 6pts)
# Write a program that takes a random integer between 1 and 1000
# The program then asks the user to guess the number.
# After every guess, the program will say either “Lower”
# if the number it took is lower, “Higher” if the number it took is higher,
# and “You guessed it!” if the number it took is equal to the number
# It might be wise, for testing purposes, to also display the number that the
# program randomly picks, until you are sure that the program works correctly
njah=random.randrange(1,1000)

for i in range(njah):
    guess=input("Tell me your number child ")
    guess=int(guess)
    if guess==njah:
        print("You guessed it muhahahha ")
        break
    elif guess<njah:
        print("Higher")
    elif guess>njah:
        print("LOWER")



# PROBLEM 3 (Dice Hi-Low - 6pts)
# You roll five six-sided dice, one by one.
# How big is the probability that the value of each die
# is greater than or equal to the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.
import random

brojce = 5
n = 0

glavenrezult = 1000
talala = 0
for j in range(glavenrezult):
    vkupno = 0
    my_list = []
    for i in range(brojce):
        broj = random.randrange(1, 7)
        my_list.append(broj)
        # n=1

    for i in range(len(my_list) - 1):
        if my_list[i] <= my_list[i + 1]:
            vkupno += 1
            if vkupno >= 4:
                n += 1

    talala = n / glavenrezult
print(talala)

# PROBLEM 4 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve.
while ((1000*a+100*c+10*b+a)!=4*(1000*a+100*b+10*c+d)):
    a=random.randrange(1,9)
    b=random.randrange(1,9)
    c=random.rangrange(1,9)
    d=random.randrange(1,9)
print(1000*a+100*b+10*c+d)

'''
for i in range(100):
    if i==50:
        break
    print(i)
for i in range(1):
    if i==5:
        continue
    print(i)

for i in range(10):
    user_input("Enter a nymber between 0 and 100")
    if user_input<0 or user_input>100:
    break
else:
    print("thank you for entering your numbers")
'''

