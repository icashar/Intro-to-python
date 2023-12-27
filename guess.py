import random

print("hello")
q1=input("Would you like to play a game?(y/n) >")
if q1 == "y":
    print("Neat")
    user= input ("guess a number between 1 and 10  >")
    if 1>int(input)>10: # find a way to pass the user's input as an integer!!!
        print("It is very important to listen to your elders bud(or I should learn, how to make this code more versatile)")
    
elif q1 == "n":
    print("alright see ya, later alligator ^_^")
    quit()
else:
    print("hmmmm, seems like there's a problem ¯\_(ツ)_/¯")
