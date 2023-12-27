print("Hello"+"\n"+"Please select one of the following:")

operation = input("1. addition\n2. substraction\n3. multiplication\n4. division     >")
num1=input("Enter the first number >")
num2=input("Enter the second number >")
if operation == "1" :
    # The numbers are taken from the consol as strings and therefor have to be turned into int in order to do any operation( hence the int())
    # After the numbers are operated they need to be displayed and they need to be strings(hence the "str()")
    print("The sum of " + num1 + " and " + num2 + " is " + str(int(num1)+ int(num2))  )
elif operation == "2" :
    print("The difference between " + num1 + " and " + num2 + " is " + str(int(num1)- int(num2))  )
elif operation == "3":
    print("The product of " + num1 + " and " + num2 + " is " + str(int(num1) * int(num2))  )
elif operation == "4":
    print("The product of division of " + num1 + " and " + num2 + " is " + str(int(num1) * int(num2))  )
else:
    print("Invalid entry")

