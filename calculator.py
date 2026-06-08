a=9999
while a > 1:
  instruct1=int(input("Enter any number : "))
  instruct2=int(input("Enter any number : "))
  command = input("Do you want + , - , / , * : ")
  if command == "+":
            addition = instruct1 + instruct2
            print(addition)
  elif command == "-":
           subtraction = instruct1 - instruct2
           print(subtraction)
  elif command == "/":
            division = instruct1 / instruct2
            print(division)
  elif command == "*":
           multiplication = instruct1 * instruct2    
           print(multiplication)
  home=input("Do you wish to continue (Y/N):")
  if home == "Y":
         a= 1000
  else:
          a= 1
