# print('Name:  John Doe\nAddress: 123 Main St')
from tkinter.messagebox import YESNO

# print('Item \t \t Price\n----- \t \t -----\nApple \t \t $1.00')

# print('Cricket is the most worldwide popular game. It is generally divided into 3 formats -\n 1.ODI\n 2.Test\n 3.T20')
# print(' There are generally 4 types of Players involved in this game. They are :\n* Batsman\n* Bowler\n* All rounder \n* Wicket-Keeper')
# print('All Rounder is generally is divided into 3, \n Bowling All rounder - Ashwin, Starc, Deepak Chahar, lord Thakur etc. \n Batting All Rounder - Ben Stokes, Sachin etc \n Perfect All Rounder -  Jaddu, Hardik , Cummins , Bravo etc' )

# box = 100
# box = 200
# box = 300
# print(box)

# MSD = '100 Fours '
# MSD = '200 Sixes'
# MSD = '11000 Runs'
# print(MSD)


# data = 23000
# String = 678900
# print('The value in my varibale is', data)

# Formatted string

# print(f'The Value in 1st Method is {data} and the 2nd Method Value is {String}')

#  Data Types
#  1.Float - Decimal Number or Fractions
#  2.String - Anything enclosed within Quotes
#  3.Integers - Whole Numbers and Negative Numbers
#  4.Boolean - Has 2 values (True/False, 0/1, Yes/No etc.)


# Method1 = 899
# Method2 = 70.90
# Method3 = '50 Hundreds and 60 Fifties'
# Method4 = "25000 runs"
# Method5 = '300 innings'

# print(f'MSD has played {Method1} Test Matches in which his avg is {Method2} .\n He has scored  {Method3}.\n He played {Method5} and scored {Method4}')

# var = True
# Fire = type(var)
# print(Fire)

# Type Conversion = 1. Implicit Conversion   2. Explicit Conversion

# Integer = 567
# Boolean = False
# Ans = Integer + Boolean
# print(Ans)

# Integer = -900
# Float = 89.90
# Sol = Integer + Float
# print(Sol)

# Float = 12.67
# Boolean = True
# Metho = Float + Boolean
# print(Metho)

# Float = 78.9
# Boolean = False
# Integer = -67
# Final = Float + Boolean - Integer
# print(Final)

# Explicit Conversion
# Float to Integer
# Jarvis = 456.7896
# print(int(Jarvis))

# Jarvis = 456.789
# Jarvis = int(Jarvis)
# print(Jarvis)
#
# Ultron = 4533.5678
# print(float(Ultron))

# Variable = -456.7
# Variable = str(Variable)
# print(Variable)
# print(type(Variable))

# Convert a String value to float
# a = "56.78"
# b = float(a)
# print(b)
# print(type(b))

#Convert a String Value to integer
# c = "34"
# d = int(c)
# print(d)
# print(type(d))

# Operatores
# 1. Arithmetic Operators
#      Additon
#      Subraction
#      Multiplication
#      Exponentiation
#      Divsion
#      Floor Division
#      Modulus

# num1 = 400
# num2 = 20
# print(f"The addition of {num1} and {num2} is {num1 + num2}")

# ans = num1 - num2
# print(f"The difference of {num1} and {num2} is {ans}")
#
# ans = num1 * num2
# print(f"The mul of {num1} and {num2} is {ans}")
#
# ans = num1 / num2
# print(f"The div of {num2} and {num2} is {ans}")
#
# ans = num1 // num2
# print(f"The floor div of {num1} and {num2} is {ans}")
#
# ans = num1 % num2
# print(f"The modulo of {num1} and {num2} is {ans}")
#
# ans = num2 % num1
# print(f'The modulo of {num2} and {num1} is {ans}')
#
#
# Var4 = 23
# Var5 = 2
# ans = Var4 % Var5
# print(f"The modulo of {Var4} and {Var5} is {ans}")

# Var12 = 8
# Var13 = 4
# print(Var12**Var13)
# print(Var13**Var12)

# a = 13
# b = 5
# c = 7
# ans = a + b*c - c + b*c
# print(ans)

# s = 67
# print(f"The area of the sqaure is {s**2}")

# bl = 34
# al = 56
# print(f"The area of the triangle is {al*bl*1/2} ")

# Calculate the area of a Circle
# r = 4
# print(f"The area of the circle is {r**2*3.14}")
#
# r = float(input("Enter the value of radius:"))
# print(f'The area of the cricle is {r*r*3.14}')
# print(type(r))

# Var = (input("Pls Enter"))
# print(Var)
# print(type(Var))

# User = input("Enter your Birth Year")
# print(User)

# Present = 2025
# BirthYear = int(input("Enter your Birth Year"))
# Age = Present - BirthYear
# print(f"Your age is {Age}")

# Assignment Operators - used to assign values to the variables
# num = 100
# num += 10
# print(num)
 # num = num + 10

# num -= 20
# print(num)

# num1 = 200
# num1 **= 7
# num1 *= 6
# print(num1)
#
# num2 = 60
# num2 %= 7
# num2 //=  6
# print(num2)

#Comparison Operators = Used to compare values
#Result : True or False - Boolean

# Mark1 = 67
# Mark2 = 68
# Comp = Mark1 != Mark2
# print(Comp)
#
# Ans = Mark1==Mark2
# print(Ans)
#
# print(67==68)
#
# print(Mark1<=Mark2)

#HomeWork: try  >= and <= and observe the result

# x = 67
# y = 89
# z = 78
# print(x!=y>=z)

#Logical Operators = Used to combine comparison statements

#1. and
#False and True = False
#False and False = False
#True and False = False
#True and True = True

# a = 100
# b = 200
# c = -700
# print(a!=b and b>=c)
#
# print(a>=b and b<=c)
#
# print(a==b and c<=b)

#2. or
#True or False = True
#True or True = True
#False or True = True
#False or False = False

# Var1 = 600
# Var2 = 600
# Var3 = 890
#
# print(Var1==Var2 or Var3!=Var2)
#
# print(Var1!=Var2 or Var1<Var2)
#
# print(Var2>Var3 or Var1==Var2)
#
# print(Var1>Var2 or Var2>Var3)

#3. not = It Gives the compliment result
 #true and not true = False
# true and not false = True
# false and not true = False
# false and not false = False

#false or not false = True
#fasle or not true = False
#true or not true = True
#true or not false = True

# Dhoni = 11750
# Rohit = 12000
# Kohli = 14000
# Sachin = 18500

# print(Dhoni==Rohit or not (Rohit!=Kohli))
#
# print(Sachin>Kohli and not(Rohit>Sachin))
#
# print(Sachin>=Dhoni or not (Kohli>Rohit))

#Homework : combine three comparison statements using ---->   and/or

# print(not(Sachin<Rohit) and not(Rohit>Kohli) or Kohli >= Rohit)

#Conditional Statements =

# name = "SVD"
#
# if (name == "SVD"):
#     print(f"Hi {name}, this is your first python class")
#     print("This is your first python class")


#name = input("Whats Your Name ?")

# if (name == "SV"):
#     print(f"Hi {name}, welcome to my terrritory")
#     print("Pls have a seat")
#
# else:
#     print("You have no rights to live here")

# Marks = int(input("Enter Your Mark"))
#
# if(Marks >=90):
#     print("Congratulations, you have secured a good mark. ")
#     print("keep it up")
#
# else:
#     print("Dont Give up your hardwork, try again and again")
#     print('Better Luck nxt time')

# SignalColor = input("Enter your traffic signal color")
#
# if SignalColor == "Red":
#     print('You Should stop your vehicle and should wait for sometime.')
#
# elif SignalColor == 'Yellow':
#     print("You Should get ready")
#
# elif SignalColor == 'Green':
#     print('You can go')
#
# else:
#     print('Pls Enter a Valid Signal Color.')
#     print('Check if you are there in some other country other than India, as Countries like US Have blue color in their signal')

#hw : get the user age. check if they are eligible to vote

# User = int(input("Enter Your age"))
#
# if User >= 18:
#     print('You are eligible to vote')
#     print('You can proceed with your voting process')
#
# else:
#     print('You are not eligible to vote')
#     print('Wait until you turn 18')

# a = float(input('Number 1'))
# b = float(input('Number 2'))
#
# operator = input('Arithmetic Symbol')
#
# if operator == '+' :
#     print(a+b)
#
# elif operator == '-' :
#     print(a-b)
#
# elif operator == '*' :
#     print(a*b)
#
# elif operator == '**'  :
#     print(a**b)
#
# elif operator == '/':
#     print(a/b)
#
# elif operator == '//' :
#
#     print(a//b)
#
# elif operator == '%':
#     print(a%b)
#
# else:
#     print('Enter a valid Operator')

# Number = Any numbers except 0 returns true. Empty Strings also returns False.
# print(bool(6))
# print(bool(67.5))
# print(bool(-78.9))
# print(bool(0))
# print(bool(""))
# print(bool(' '))
# print(bool("a"))
# print(bool('python'))
# print(bool("python123"))

# age = int(input("Enter the age:"))
#
# if age>= 18:
#     print('You are allowed to enter the event')
#
#     ticket = input('Do u have a ticket ? YES/NO')
#
#     if ticket == 'YES':
#         print("Welcome to the party")
#
#         FoodTicket = input("Do u have a food ticket ? YES/NO/Not Required ")
#         if FoodTicket == 'YES':
#               print('Enjoy your meal')
#
#         elif FoodTicket == 'NO':
#               print("There is your Food Ticket Counter")
#
#         elif FoodTicket == 'Not Required':
#             print('Are u sure about your decision?')
#
#         else:
#             print('Correctly answer the question')
#
#     else:
#         print('Pls buy a ticket and join the event')
#
# else:
#     print('You are not allowed to enter the event')






















































