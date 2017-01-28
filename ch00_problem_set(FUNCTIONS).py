#SECTION 2 - FUNCTIONS (20PTS TOTAL)
import math
import random
#PROBLEM 1 (Length of String - 3pts)
# Make a function which asks the user to enter a string, then prints the length of that string.
# You will need to use the input() function.
# Make a call to that function
def striingy():
    stringy=input("HI:")
    print(len(stringy))

# PROBLEM 2 (Pythagorean theorem - 4pts)
# The Pythagorean theorem states that of a right triangle, the square of the
# length of the diagonal side is equal to the sum of the squares of the lengths
# of the other two sides (or a^2 + b^2 = c^2).
# Write a program that asks the user for the lengths of the two sides that meet at a right angle.
# Then calculate the length of the third side, and display it in a nicely formatted way.
# You may ignore the fact that the user can enter negative or zero lengths for the sides.
a=input("PLS INZERT NUMBER:")
a=int(a)
b=input("PLZ INZERT NUMBER 2!!!!:")
b=int(b)
print("The third side of the triangle you have specified is",math.sqrt(int(a**2)+int(b**2)))

# PROBLEM 3 (Biggest, smallest, average - 4pts)
# Make a function to ask the user to enter three numbers.
# Then print the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.
# Make a call to your function.
def funckija():
    lala_loop = []
    a = 0

    for i in range(3):
        c = input("Numero?: ")
        lala_loop.append(c)
        b = lala_loop[0]
    for i in range(len(lala_loop)):
        if (float(lala_loop[i]) > float(a)):
            a = float(lala_loop[i])
        if (float(lala_loop[i]) < float(b)):
            b = float(lala_loop[i])
    a = float(a)
    b = float(b)
    c = float((a + b) / 2)
    print("The largest number is", round(a,2), "The smallest one is", round(b,2), "the average is", round(c,2))

# PROBLEM 4 (e to the... - 3pts)
# Calculate the value of e (from the math library) to the power of -1, 0, 1, 2, and 3.
# display the results, with 5 decimals, in a nicely formatted manner.

e=math.e
print("e to the negative first power is",e**-1)
print("e to the zeroeth power is",e**0)
print("e to the first is",e**1)
print("e to the second is",e**2)
print("e to the third is",e**3)

# PROBLEM 5 (Random int - 3pts)
# Generate a random integer between 1 and 10 (1 and 10 both included),
# but only use the random() function (randrange is not allowed here)
randomce=int(random.random()*10+1)
print(randomce)

# PROBLEM 6 (add me, multiply me - 3pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.
def dajmibroj(g,h):
    return g+h,g*h
print(dajmibroj(4,5))