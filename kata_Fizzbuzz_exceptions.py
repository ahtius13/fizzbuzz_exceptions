import math

number = int(input ("introduce un nº del 1 al 100: "))

resultado3 = number%3

resultado5 = number%5

if resultado3 == 0 and resultado5 == 0:
    print ("FizzBuzz")
elif resultado3 == 0:
    print ("Fizz")
elif resultado5 == 0:
    print ("Buzz")
else:
    print(number)