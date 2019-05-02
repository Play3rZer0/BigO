print("Please select from the following items:")
print("1 - Potato Chips")
print("2 - Pretzels")
print("3 - Nachos")
print("4 - Popcorn")

optNum = input("Type number: ")
var = int(optNum)

if var == 1:
   print("You have chosen Potato Chips")
   print (var)
elif var == 2:
   print ("You have chosen Pretzels")
   print (var)
elif var == 3:
   print ("You have chosen Nachos")
   print (var)
elif var == 4:
   print ("You have chosen Popcorn")
   print (var)
else:
   print ("Invalid Option, try again")
   print (var)

print ("Good bye!")
