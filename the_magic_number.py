#Guess a number 
from math import *
from random import randint

#GAME RULE
print ("Game Rule: You can choose any number and it can be two, three or four digits then time that number with a number computer provides. Then you type in all the numbers except one. The computer will guess what number is missing in the result")

#GET USER TO READY STEAD!

print("Let's begin!")                                

#USER THINKING OF A NUMBER

print("Now, think of a two or three digit number (make sure you have a calculator in the front of you) ")              
                
#Make sure you have a cal in the front of you
print("It would help if you have a calculator in front of you")

def comNumber():
                x = randint(1,999)
                if x % 9 ==0:
                                print("Mutiply your number with " + str(x))
                                return x
                else:
                                comNumber()
comNumber()
                
#User enters the result except one number
user_result = input("Enter your result here (except one number) : ")

#Convert input to a list of intergers
sumResult = [int(i) for i in str(user_result)]

#Add the intergers together
sumInt = sum(sumResult)

#Find a missing number
def missingNum():
                y = randint(0,9)
                if (y + sumInt) %9 ==0:
                                print(" The missing number is " + str(y))
                else:
                                missingNum()
missingNum()



