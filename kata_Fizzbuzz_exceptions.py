
def fizzbuzz(n) -> str:

i = None

while i != 1:
      
   try:
      number = int(input ("introduce un nº del 1 al 100: "))
      
      if number < 1 or number > 100:
         raise ValueError ("El nº debe ser entre 1 y 100")
      else:
         i = 1
      
   except ValueError:
      print("Debe introducir un nº")
      i = 0

   

resultado3 = number % 3

resultado5 = number % 5

if resultado3 == 0 and resultado5 == 0:
   final = print ("FizzBuzz")
elif resultado3 == 0:
   final = print ("Fizz")
elif resultado5 == 0:
   Final = print ("Buzz")
else:
   final = print(number)


return str(final)

