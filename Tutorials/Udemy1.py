# parrot = "Norwegian Blue"
# print(parrot[2])
# print(parrot[-1])
# print(parrot[0:6])
# print(parrot[:6])
# print(parrot[0:])
# print(parrot[:])
# print(parrot[0:6:2])
# number = "9,456,678,245,687"
# print(number[1::4])
# numbers = "1, 2, 3, 4, 5"
# print(numbers[0::3])
# string1 = "he's "
# string2 = "probably"
# print(string1 +string2)
# print("hello " *5)
# print("hello " *(5+1) + "4")
# today = "friday"
# print("day" in today)
# print("fri" in today)
# print("Fri" in today)
# age = 24
# print("My age is" + " " + str(age) + " years")
#
# print("My age is {0} years".format(age))
# print("There are {0} days in {1}, {2}. {3}, {4}, {5}, {6}, and "
#       "{7}".format(31, "Janurary", "March", "May", "July", "Agusut",
#                    "October", "December"))
# print('''January: {2}
# February: {0}'''.format(28, 30, 31))
#
# print("My age is %d years" % age)
# print("My age is %d %s, %d %s" %(age, "years", 6, "months"))
# for i in range(1, 12):
#     print("No. %2d squared is %3d and cubed is %4d" %(i, i ** 2, i ** 3))
#
# print("Pi is approximately %12.50f" % ( 22 / 7))
# for i in range(1, 12):
#     print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
# print("Pi is approximately {0:12.50}".format( 22 / 7))

# meal1 = "spam" + "eggs" + "beans"
# meal2 = "spam\neggs\nbeans"
# meal3 = "spam, eggs, beans"
# meal4 = """spam
# eggs
# beans"""
#
# print(meal1)
# print(meal2)
# print(meal3)
# print(meal4)
#
# days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
# print(days[::5])


# for i in range(1, 12):
#     print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 4))
#     print("Calculation complete")
#     print("Try again")




# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Please putt an X in the box")
# else:
#     print("Please come back in {0} years. IDIOT".format(18 - age))
#     print("Why you so young??")

# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess != 5:
#     if guess < 5:
#      print("Please guess higher")
#     else:
#         print("Please guess lower")
#
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you guessed incorrectly")
# else:
#     print("You got it first time")

#age = int(input("How old are you? "))

#if (age >= 16) and (age <= 65):

# if 15 < age < 66:
#     print("Have a good day at work!")

# if (age < 16) or (age > 65):
#     print("enjoy your free time")
# else:
#     print("have a good day at work")
#
#
# if (some_condition) or (some_weird_function):
    #do something
#
# x = "False"
# if x:
#     print("x is true")

# x = input("Please enter text ")
#
# if x:
#     print("You entered '{}'".format(x))
# else:
#     print("You did not enter anything")

# print(not False)
# print(not True)

# age = int(input("How old are you? "))
# if not(age<18):
#     print("you are old enough to vote")
#     print("Please put ballot in box")
# else:
#     print("please come back in {} years".format(18-age))

# parrot = "Norwegian Blue"
#
# letter = input("Enter a character ")
#
# if letter in parrot:
#     print("Give me an {}, Bob".format(letter))
# else:
#     print("I don't need that letter")


# x = 10
# y = 7
#
# if x > y:
#     print("x is greater than y")
# if x < y:
#     print("x is smaller than y")
# if x == y:
#     print("x equals y")

# x = 5
# y = 7
#
# if x > y:
#     print("x is greater than y")
# elif x < y:
#     print("x is smaller than y")
# else:
#     print("x equals y")

# name = input("Welcome, what is your name? ")
# age = int(input("Hello {}, how old are you? ".format(name)))
#
# if 18 <= age < 31:
#     print("Welcome to the holiday, {}".format(name))
# elif 18 > age:
#     print("You are {} years too young".format(18 - age))
# else:
#     print("You are {} years too old".format(age - 31))


# for i in range(1,21):
#     print("i is now {}".format(i))
#
# number = "9,223,372,036,854,775,807"
# for i in range(0, len(number)):
#     print(number[i])
#
#
#
# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber = cleanedNumber + number[i]
#         print(number[i],end='')
#
# newNumber = int(cleanedNumber)
# print("The number is {}".format(newNumber))



# for i in range(10):
#     print(i, end = '')


# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
#
# for char in number:
#     if char in "0123456790":
#         cleanedNumber = cleanedNumber + char
#
# newNumber = int(cleanedNumber)
# print("The number is {}".format(newNumber))
#
# for state in ["not pinin", "no more", "a stiff", "bereft of lift"]:
#     print("This parrot is "+state)

# for i in range(0,100,5):
#     print("i is {}".format(i))

#
# for i in range (1,13):
#     for j in range(1,13):
#         print("{1} times {0} is {2}".format(i, j, i*j), end = '\t')
#     print("==============")
#     print("")



# quote = "Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads, the Fresh-Water System, and Public Health, what have the Romans ever done for us?"
# for char in quote:
#     if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         print(char, end='')


# for i in range (0,100, 7):
#     print(i)

# shopping_list = ("milk", "pasta", "eggs", "spam", "bread", "rice")
# for item in shopping_list:
#     if item == 'spam':
#        print("I am ignoring {}".format(item))
#         break
#
#     print("Buy " + item)

# meal = ("egg", "bacon", "spam", "sausages")
# nasty_food_item = ''
#
# for item in meal:
#     if item == "spam":
#         nasty_food_item = item
#         break
# if nasty_food_item:
#     print("Can't I have anything else?")
# else:
#     print("I'll have a plate of that then, please")


# for i in range(0, 100, 7):
#     print(i)
#     if i > 0 and i % 11 == 0:
#        break

# for i in range (1, 21):
#      if i % 3 == 0 or i % 5 == 0:
#           continue
#     print(i)


# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
# for i in range (0, len(number)):
#     if number [i] in '0123456789':
#         cleanedNumber += number[i]
#
# newNumber = int(cleanedNumber)
# print ("The number is {}".format(newNumber))
#
# x = 23
# x += 1
# print(x)
# x -= 4
# print(x)
# x *= 5
# print(x)
# x /= 4
# print(x)
# x **=2
# print(x)
# x %= 60
# print(x)
#
# greeting = "good "
# greeting += "morning "
# print(greeting)
#
# greeting *= 5
# print(greeting)

# number = 5
# multiplier = 8
# answer = 0
# for i in range(8):
#     answer += number
# print(answer)

# IP = input("Please enter an IP address: ")
# segment = 1
# segment_length = 0
# character = ""
#
# for character in IP:
#     if character == ".":
#         print("segment {} contained {} character".format(segment, segment_length))
#         segment += 1
#         segment_length = 0
#     else:
#         segment_length += 1
#
# if character != '.':
#     print("segment {} contained {} character".format(segment, segment_length))

# name = input("Please enter your name: ")
# age = int(input("Hello {}, please enter your age: ".format(name)))
#
# birth = 2018 - age
# year100 = birth + 100
#
# print(year100)

# number = int(input("Please enter any number: "))
# if number % 4 == 0:
#     print("This is an divisible by 4 number")
# elif number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

# num = int(input("Give me one number: "))
# check = int(input("Give me another number: "))
#
# if num % check == 0:
#     print("you chose a set of multiples")
# else:
#     print("You chose an incompatible set")

# a = [5, 10, 15, 20, 25]
#
# b = a[0], a[len(a)-1]
# print(b)


# IP = input("Please enter an IP address: ")
# # segment = 1
# # segment_length = 0
# # character = ""
# #
# # for character in IP:
# #     if character == ".":
# #         print("segment {} contained {} character".format(segment, segment_length))
# #         segment += 1
# #         segment_length = 0
# #     else:
# #         segment_length += 1
# #
# # if character != '.':
# #     print("segment {} contained {} character".format(segment, segment_length))

# def hello():
#     print("hello!")
#     print ("computers are fun")
# hello()

# def greet(person):
#     print("Hello ", person)
#     print("How are you?")
# greet("Laura")


# def main():
#     print("This program illustrates a chaotic funtion")
#     n = int(input("How many numbers would you like output? "))
#     x = float(input("enter a number between 0 and 1: "))
#     y = float(input("enter a second number between 5 and 10: "))
#     print()
#     # print("input    ", x, " | ", y)
#     # print("-----------------------")
#     for i in range (n):
#         x = 2.0 * x * (1 - x)
#         y = 2.0 * y * (1 - y)
#         print("    ", x, " | ", y)
#
# main()

# print(2+3)
# print("2" + "3")
# print(2**3)
#
# def main():
#     celsius = float(input("What is the Celsius temperature? "))
#     fahrenheit = 9/5 * celsius +32
#     print("The temperature is ", fahrenheit, " degrees fahrenheit.")
#
# main()
# print("ok i type a whole bunch of stuff here")

# x = 1
#
# for i in range(10):
#     x = x * 3
#     print(x)

# x = eval(input("Enter an expression: "))
# print(x)

# x, y = 3, 4
# print(x)
# print(y)
#
# x, y = y, x
# print("new", x)
# print("new", y)

# x = 20
# for i in range (5, 10):
#     x = x + i
#     print(x)
# for i in [0, 1, 2, 3, 4]:
#     print(i * i)

# y = list(range(10))
# print(y)

# def main():
# #     print("Welcome to the investment calculator")
# #     invest = float(input("Please input the amount of money you would like to invest: "))
# #     apr = float(input("Please list the apr: "))
# #     x = int(input("Please enter the number of years you would like the money growing: "))
# #
# #     for i in range(x):
# #         invest = invest * (1 + apr)
# #     print(invest)
# # main()

# for i in range(5):
#     print(i, i)
# print("---------")
# for d in [3, 1, 4, 1, 5]:
#     print(d, end=" ")
# print("---------")
# for i in range(4):
#     print("Hello")
# print("---------")
# for i in range(5):
#     print(i, 2**i)
# print("Start")
# for i in range (0):
#      print("Hello")
# print("end")

# def main():
#
#     Temp1 = float(input("What is the Celsius temperature? "))
#     Temp2 = float(input("What is the next Celsius temperature? "))
#     Temp3 = float(input("What is the next Celsius temperature? "))
#     Temp4 = float(input("What is the next Celsius temperature? "))
#     Temp5 = float(input("What is the next Celsius temperature? "))
#     for i in [Temp1, Temp2, Temp3, Temp4, Temp5]:
#         fahrenheit = 9/5 * i + 32
#         print("The temperature is ", fahrenheit, " degrees fahrenheit.")
#
# main()

# def main():
#
#     for i in range(0 , 100, 10):
#         fahrenheit = 9/5 * i + 32
#         print("The temperature is ", fahrenheit, " degrees fahrenheit.")
#
# main()

# def main():
#     print("Welcome to the investment calculator")
#     invest = float(input("Please input the amount of money you would like to invest: "))
#     annual = float(input("Please enter the annual additional amount you will add: "))
#     apr = float(input("Please list the apr: "))
#     x = int(input("Please enter the number of years you would like the money growing: "))
#
#     for i in range(x):
#         invest = (invest + (annual*(x-1))) * (1 + apr)
#     print(invest)
# main()

# c02ex03.py
#   Loop to perform 5 temperature conversions
#
# def main():
#     for i in range(5):
#         celsius = eval(input("What is the Celsius temperature? "))
#         fahrenheit = 9.0 / 5.0 * celsius + 32
#         print("The temperature is", fahrenheit, "degrees Fahrenheit.")
#         print()
#
# main()

# c02ex04.py
#     Table of temperature conversions

# Note: Table alignment is hacked here. Formatted output is covered in
#       Chapter 5.

# def main():
#     print("Celsius  Fahrenheit")
#     print("-------------------")
#     print(" 0          32.0")
#     for celsius in [10,20,30,40,50,60,70,80,90]:
#         fahrenheit = 9.0 / 5.0 * celsius + 32
#         print(celsius, "        ", fahrenheit)
#     print("100         212.0")
#
# main()
# import math
# # def main():
# #     print("This program finds the real solutions to a quadratic")
# #     print()
# #
# #     a = int(input("Please enter coefficients a: "))
# #     b = int(input("Please enter coefficients b: "))
# #     c = int(input("Please enter coefficients c: "))
# #     discRoot = math.sqrt(b*b -(4 * a * c))
# #     root1 = (-b + discRoot)/(2 * a)
# #     root2 = (-b - discRoot)/(2 * a)
# #
# #     print()
# #     print("The solutions are: ", root1, root2)
# #
# # main()

#

# x = 5.0 * 2
# print(x)

# def main():
#     x = round(3.9)
#     print(x)
#
# main()

# print(round(3.93294872982, 0))
# import math
# x = math.pi
# print(x)
#
# for i in range(1, 11):
#     print(i * i)
#
# for i in [1, 3, 5, 7, 9]:
#     print(i, ":", i**3)
# x = 2
# # # y = 10
# # # for j in range(0, y, x):
# # #     print(j, end ="")
# # #     print(x + y)
# # # print("done")

import math
# x = round(343.24533, -1)
# print(x)
#
# x = 10 % 3
# print(x)

# import math
# print(math.pi)
# radius = float(input("Please enter a radius: "))
# v = (4/3)*(math.pi)*(radius**3)
# print(v)

# price = float(input("Enter price of pizza: "))
# diameter = float(input("enter diameter: "))
#
# A = (math.pi) * ((diameter/2)**2)
#
# print(A)

# n = int(input("please enter a whole number: "))
# sum = 0
# for i in range (0, n+1):
#     sum = sum + (i**3)
# print(sum)

# def main():
# #     print("Welcome to the Konditorei!")
# #     print()
# #
# #     amount = eval(input("How many pounds of coffee do you want? "))
# #     coffeeCost = 10.5 * amount
# #     shipping = 0.86 * amount + 1.5
# #
# #     print()
# #     print("Cost of coffee:", coffeeCost)
# #     print("Shipping:      ", shipping)
# #     print("-------------------------------")
# #     print("Total due:     ", coffeeCost + shipping)
# #
# # main()

# def main():
#     num = int(input("How many numbers do you have? "))
#     sum = 0
#     for i in range (num):
#         n = int(input("enter a number "))
#         sum = sum + n
#     print(sum/num)
#
# main()
#
# number = "9,742,423,405,860"
# clean = ''
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         clean += number[i]
#
# clean = int(clean)
# print(clean)
# print("The number without characters is {}".format(clean + 1))

# number = int(input("Please enter a number: "))
# multiplier = int(input("Please enter a multiplier: "))
# answer = 0
# for i in range (0, multiplier):
#     answer += number
#
#
# answer = int(answer)
# print(answer)
#
# IP = input("Please enter an IP address: ")
# segment = 1
# segment_length = 0
# character = ""
#
# for character in IP:
#     if character == ".":
#         print("It contains {} and {}".format(segment, segment_length))
#         segment += 1
#         segment_length = 0
#     else:
#         segment_length +=1
#
# if character != ".":
#     print("It contains {} and {}".format(segment, segment_length))
#
# for i in range(10):
#     print("i is now {}".format(i))

#available_exits = ["east", "northeast", "south"]
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game over")
#         break
# else:
#     print("awesome job")

# import random
# highest = 1000
# answer = random.randint(1, highest)
# guess = 0
#
# print("Please guess a number between 1 and {}: ".format(highest))
#
# while guess != answer:
#     guess = int(input())
#     if guess == 0:
#         break
#     if guess < answer:
#         print("Guess higher")
#     elif guess > answer:
#         print("Guess lower")
#     else:
#         print("Well done")
# value = 8
# # answer = 0
# #
# # for x in range(1, 13):
# #     answer = value * x
# #     print("{0} times {1} is {2}".format(x, value, answer))

# choice = 0
#
# while choice != '0':
#     choice = input("Please enter your choice.  Press enter to quit")
#     if choice == '':
#         break
#
#     print("You have selected {}".format(choice))
# else:
#     print("Thank you for playing, please call back soon.")
# ip_address = input("Please enter an IP address: ")
# print(ip_address.count("."))

# parrot_list = ["non pinin", "no more", "stiff", "bereft of life"]
#
# parrot_list.append("Norwegian Blue")
# for state in parrot_list:
#     print("This parrot is " + state)
#
# even = [2,4,6,8]
# odd = [1,3,5,7]
# numbers = even + odd
# numbers_order = sorted(numbers)
#
# print(numbers)
# print(numbers_order)
#
# if numbers == numbers_order:
#     print("the lists are equal")
# else:
#     print("1.the lists are not equal")
#
# if numbers_order == sorted(numbers):
#     print("the lists are equal")
# else:
#     print("not equal")

# list_1 = []
# list_2 = list()
#
# print(list("The lists are equal"))

# even = [2,4,6,8]


# another_even = list(even)
# print(another_even is even)
#
# another_even.sort(reverse=True)
# print(another_even)
# even = [2,4,6,8]
# odd = [1,3,5,7,9]
# numbers = [even, odd]
#
# for numbers_set in numbers:
#     print(numbers_set)
#
#     for value in numbers_set:
#         print(value)

# menu = []
# # menu.append(["egg", "spam", "bacon"])
# # menu.append(["egg", "sausage", "bacon"])
# # menu.append(["egg", "spam"])
# # menu.append(["egg", "bacon", "spam"])
# # menu.append(["egg", "bacon", "sausage", "spam"])
# # menu.append(["spam", "bacon", "sausage", "more spam"])
# # menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
# # menu.append(["spam", "egg", "sausage", "spam"])
# #
# # #print(menu)
# #
# # for meal in menu:
# #     if not "spam" in meal:
# #         for item in meal:
# #             print(item)

# string = "1234567890"
# for char in string:
#     print(char)
# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# for char in string:
#     print(char)
# print("-------")
# for char in iter(string):
#     print(char)
# my_list = ["HELLLLLOOOOOO", "Hi", "Gooday"]
# n = len(my_list)
# my_iterator = iter(my_list)
# for char in range(n):
#     next_item= next(my_iterator)
#     print(next_item)
# my_list = list(range(10))
# print(my_list)
#
# even = list(range(0,10,2))
# odd = list(range(1,10,2))
# print(even)
# print(odd)
#
# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index('e'))
# print(my_string[5])
#
# small_decimals = range(0,10)
# print(small_decimals)
#
# print(small_decimals.index(4))
# print("-------")
# odd = list(range(1,10000,2))
# print(odd)
#
# print(odd[985:990])
#
# sevens = range(7,10000, 7)
# x = int(input("Please enter a positive number less than one million: "))
# if x in sevens:
#     print("{} is divisible by 7".format(x))
#
# print("-----")
#
# print(small_decimals)
# my_range = small_decimals[::2]
# print(my_range)
# print(my_range.index(4))

# decimals = range(0,100)
# my_range = decimals[3:40:3]
# print(my_range == range(3,40,3))
#
# print(range(0, 5, 2) == range(0,6,2))
# print(list(range(0,5,2)))
# print(list(range(0,6,2)))
#
# r = range(0,100)
# print(r)
# print("-"*50)
# for i in r[::-2]:
#     print(i)
# print("-"*50)
# print(range(0,100)[::-2] == range(99,0,-2))
#
# for i in range(0,100,-2):
#     print(i)

# backString = "eqaugnal lufrewop yrev a si nohtyp"
# print(backString[::-1])
#
# r = range (0,10)
# for i in r[::-1]:
#     print(i)

# o = range(0,100,4)
# print(o)
# for char in iter(o):
#     print(char)
# print('-'*50)
# p = o[::5]
# print(p)
# print('-'*50)
# for i in p:
#     print(i)
#

# welcome = "Welcome to my nightmare", "alice cooper", 1975
# bad = "bad company", "bad comppany", 1974
# budgie = "nightflight", "budgie", 1981
# imelda = "more mayhem", "emilda may", 2011
# metallica = "ride the lightening", "metallica", 1984
#
# print(metallica)
# print(metallica[0])
#
# metallica2 = ["ride the lightney", "metallica", 1984]
# print(metallica2)
# metallica2[0] = "maste of puppets"
# print(metallica2)
#
# a = b = c = d = 12
# print(c)
# print(a)
# print(b)
# a , b = 12, 13
# print(a)
# print(b)

# welcome = "Welcome to my nightmare", "alice cooper", 1975
# bad = "bad company", "bad comppany", 1974
# budgie = "nightflight", "budgie", 1981
# imelda = "more mayhem", "emilda may", 2011
# metallica = "ride the lightening", "metallica", 1984
#
#
# metallica2 = ["ride the lightney", "metallica", 1984]
# print(metallica2)
#
# title, artist, year = imelda
# print(title)
# print(artist)
# print(year)

#import sklearn
#import scipy

# from sklearn import tree
# features = [[140, 1],[130, 1], [150, 0], [170, 0]]
# # 0 = bumpy, 1 = smooth
# labels = [0, 0, 1, 1]
# # 0 = apple, 1 = orange
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(features, labels)
# print(clf.predict([[180, 0]]))

# import sklearn
# from sklearn import tree
# import numpy as np
# from sklearn.datasets import load_iris
#
# iris = load_iris()
# print(iris.target_names)
# print(iris.data[0])
# print(iris.target[0])
# for i in range(len(iris.target)):
#     print("Example {0}:label {1}, features {2}".format(i, iris.target[i], iris.data[i]))
#
# test_idx = [0, 50, 100]
#
# #training data
# train_target = np.delete(iris.target, test_idx)
# train_data = np.delete(iris.data, test_idx, axis = 0)
#
# #testing data
# test_target = iris.target[test_idx]
# test_data = iris.data[test_idx]
#
# clf = tree.DecisionTreeClassifier()
# clf.fit(train_data, train_target)
#
# print(test_target)
# print(clf.predict(test_data))
#
#
#
# import graphviz
# from IPython.display import Image
#
# from sklearn.externals.six import StringIO
# import pydotplus
#
# dot_data = StringIO()
# tree.export_graphviz(clf, out_file= dot_data,
#                         feature_names = iris.feature_names,
#                         class_names = iris.target_names,
#                         filled = True, rounded = True,
#                         impurity = False)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# graph.write_pdf("iris.pdf")
#
# print(test_data[1], test_target[1])
# print(iris.feature_names, iris.target_names)

# import numpy as np
# import matplotlib.pyplot as plt
#
# greyhounds = 500
# labs = 500
#
# grey_height = 28 + 4 * np.random.randn(greyhounds)
# lab_height = 24 + 4 * np.random.randn(labs)
#
# plt.hist([grey_height, lab_height], stacked = True, color = ['r', 'b'])
# plt.show()

# import graphics
# from graphics import *
#
# def main():
#     win = GraphWin("", 500, 500)
#     p = Point(50,60)
#     p2 = Point(140, 100)
#     p2.move(100,100)
#     print(p.getX())
#     print(p.getY())
#     p.draw(win)
#     p2.draw(win)
#     win.getMouse() # Pause to view result
#     win.close()
#
# main()

# import graphics
# from graphics import *
#
# def main():
#     win = GraphWin('Shapes')
#     center = Point(100, 100)
#     circ = Circle(center, 30)
#     circ.setFill('red')
#     circ.draw(win)
#     label = Text(center, "Red Circle")
#     label.draw(win)
#     rect = Rectangle(Point(30, 30), Point(70,70))
#     rect.draw(win)
#     line = Line(Point(20,30), Point(180,165))
#     line.draw(win)
#     oval = Oval(Point(20,150), Point(180,199))
#     oval.draw(win)
#     win.getMouse() # Pause to view result
#     win.close()
#
# main()

# from graphics import *
#
# def main():
#     win = GraphWin('Shapes')
#     leftEye = Circle(Point(80,50), 5)
#     leftEye.setFill('yellow')
#     leftEye.setOutline(('red'))
#     rightEye = leftEye.clone()
#     rightEye.move(20,0)
#     leftEye.draw(win)
#     rightEye.draw(win)
#     win.getMouse() # Pause to view result
#     win.close()
#
# main()


# welcome = "Welcome to my nightmare", "alice cooper", 1975
# bad = "bad company", "bad comppany", 1974
# budgie = "nightflight", "budgie", 1981
# imelda = "more mayhem", "emilda may", 2011, (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
# metallica = "ride the lightening", "metallica", 1984,
#
# print(imelda)
#
# title, artist, year, track1, track2, track3, track4 = imelda
# print(title)
# print(artist)
# print(year)
# print(track1)
# print(track2)
# print(track3)
# print(track4)

# imelda = "More Mayhem", "Imelda May", 2011,(
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
# )
#
# title, artist, year, track = imelda
# print("The details are: {0}, {1}, {2} and the tracks are \n {3} \n {4} \n {5} \n {6}".format(title, artist, year, track[0], track[1], track[2], track[3]))
# for songs in track:
#     track, title = songs
#     print(" \tTrack number {}, Title: {}".format(track, title))
#
# def main():
#     print("This will generate a username")
#     first = input("Please enter first name: ")
#     last = input("Please enter last name: ")
#
#     usname = first[0] + last[:7]
#
#     print(usname)


# main()



# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# newMessage = ''
#
# message = input('Please enter a message: ')
#
# key = input('Enter a key (1-26): ')
# key = int(key)
#
# for character in message:
#     if character in alphabet:
#         position = alphabet.find(character)
#         newPosition = (position + key) % 26
#         newCharacter = alphabet[newPosition]
#         newMessage += newCharacter
#     else:
#         newMessage += character
#
# print('Your new message is: ', newMessage)
# ravjqpejcnngpig.eqo/re/gho/cr.jvon
#
# fruit = {"orange": "a sweet, orange citrus fruit",
#          "apple": "good for making cider",
#          "lemon": "a sour yellow citru",
#          "grape": "a small sweet fruit",
#          "lime": "sour, green"}
# print(fruit)
# print(fruit["apple"])
#
# # while True:
# #     dict_key = input("Please enter a fruit: ")
# #     if dict_key == "quit":
# #         break
# #     # description = fruit.get(dict_key, "We don't have a " + dict_key)
# #     # print(description)
# #     # description = fruit.get(dict_key)
# #     # print(description)
# #     if dict_key in fruit:
# #         description = fruit.get(dict_key)
# #         print(description)
# #     else:
# #         print("we don't have a " + dict_key)
#
# for snack in fruit:
#     print(fruit[snack])

# for i in range(10):
#     for snack in fruit:
#         print(snack + "is " + fruit[snack])
#     print('-' * 40)
#
# ordered_key = list(fruit.keys())
# ordered_key.sort()
# ordered_key = sorted(list(fruit.keys()))
# for f in ordered_key:
#     print(f + "-" + fruit[f])

# for f in sorted(fruit.keys()):
# for f in fruit:
#     print(f + "-" + fruit[f])

# for val in fruit.values():
#     print(val)
#
# print('-' *40)
#
# for key in fruit:
#     print(fruit[key])
# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)
# print(fruit.keys())
# print(fruit.values())

# def happy():
#     print("Happy Birthday to you!")
#
# def sing(person):
#     happy()
#     happy()
#     print("Happy Birthday dear", person + "!" )
#     happy()
#
# sing("Fred")
# from graphics import*
# # win = GraphWin()
# # def drawBar(window, year, height):
# #     bar = Rectangle(Point(year, 0), Point(year+1, height))
# #     bar.setFill("green")
# #     bar.setWidth(2)
# #     bar.draw(window)
# #
# # drawBar(win, 0, 2000)

#hours = print(int(input("How many hours did you work this week? ")))
#rate = print(int(input("HWhat is your hourly rate? ")))

# def main():
#     hours = int(input("How many hours did you work this week? "))
#     rate = int(input("What is your hourly rate? "))
#     over = rate * 1.5
#     if hours <= 40:
#         x = hours * rate
#         print("Your income is {}".format(x))
#     else:
#         overtime = hours - 40
#         o_pay = overtime * over
#         x = 40 * rate
#         income = o_pay + x
#         print ("Your income is {}".format(income))
# main()

# fruit = {"orange": "a sweet, orange citrus fruit",
#          "apple": "good for making cider",
#          "lemon": "a sour yellow citrus",
#          "grape": "a small sweet fruit",
#          "lime": "sour, green"}
# print(fruit.items())
# f_tuple= tuple(fruit.items())
# print(f_tuple)
#
# print(dict(f_tuple))

# myList = ['a', 'b', 'c', 'd']
# newString = ''
# for c in myList:
#     newString += c + ", "
# print(newString)
#
# newString = ', '.join(myList)
# print(newString)
#



#
# locations = {0: "You are sitting in front of a computer learning Python",
#              1: "You are standing at the end of a road before a small brick building",
#              2: "You are at the top of a hill",
#              3: "You are inside a building, a well house for a small stream",
#              4: "You are in a valley beside a stream",
#              5: "You are in the forest"}
#
# exits = {0: {"Q": 0},
#          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          2: {"N": 5, "Q": 0},
#          3: {"W": 1, "Q": 0},
#          4: {"N": 1, "W": 2, "Q": 0},
#          5: {"W": 2, "S": 1, "Q": 0} }
#
# vocabulary = {'QUIT': 'Q',
#               'NORTH':'N',
#               'SOUTH':'S',
#               'EAST': 'E',
#               'WEST': 'W' }
#
# loc = 1
# while True:
#     availableExits = ", ".join(exits[loc].keys())
#
#     print(locations[loc])
#
#     if loc == 0:
#         break
#
#     direction = input("Available exits are " + availableExits + " ").upper()
#     print()
#     #Parse user input with vocabulary dictionary
#     if len(direction) > 1:
#         for word in vocabulary:
#             if word in direction:
#                 direction = vocabulary[word]
#
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#     else:
#         print("You cannot go in that direction")





# fruit = {"orange": "a sweet, orange citrus fruit",
#          "apple": "good for making cider",
#          "lemon": "a sour yellow citrus",
#          "grape": "a small sweet fruit",
#          "lime": "sour, green"}
#
# veggies = {"cabbage": "a child's favoriate",
#            "sprouts": "mmmm yes",
#            "spinach": "can i have some more fruit instead?"}
#
# print(veggies)
#
# veggies.update(fruit)
# print(veggies)

# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add('horse')
#
# print(farm_animals)
# print(wild_animals)


# even = set(range(0,40,2))
# print(even)
# squares_tuple = (4,6,9,16,25)
# square = set(squares_tuple)
# print(square)

# even = set(range(0,40,2))
# print(even)
# print(len(even))

# square_tuple = (4,6,9,26,25)
# squares = set(square_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print(even.intersection(squares))

# print(sorted((even)))
# print(sorted((squares)))
#
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print(squares.difference(even))
#
# print("=" * 40 )
# even.difference_update(squares)
# print(sorted(even))
#
# print(sorted(even.symmetric_difference(squares)))
#
# squares.discard(4)
# print(squares)

# x = input("Please enter some text: ")
# input_set = set(x)
# vowel_set = frozenset('aeiou')
#
# final_text = input_set.difference(vowel_set)
# print(final_text)
# def main():
#     n = int(input("How many numbers do you have? "))
#     sum = 0.0
#
#     for i in range(n):
#         x = int(input("Please enter your numbers: "))
#         sum = sum + x
#     average = sum/n
#     print("The average is {}".format(average))
# main()

# def main():
#     #n = (int(input("How many numbers do you have? ")))
#     sum = 0.0
#     count = 0
#     moredata = "yes"
#
#     while moredata[0] == "y":
#         x = int(input("Please enter number: "))
#         sum = sum+x
#         count = count+1
#         moredata = input("Do you have more data? ")
#     average = sum/count
#     print("The average is {} ". format(average))
#
#
# main()

# while i <= 10:
#     print(i)
#     i = i + 1

# def main():
#     sum = 0
#     count = 0
#     x = int(input("Please enter a number (enter negative number to quit): "))
#
#     while x >= 0 :
#         sum = sum + x
#         count = count + 1
#         x = int(input("Please enter the next number (enter negative number to quit: "))
#     average = sum/count
#     print("The average is {}".format(average))
# main()

# def main():
#     sum = 0
#     count = 0
#     xstr = input("Please enter a number (press enter to exit): ")
#     while xstr != "":
#         x = int(xstr)
#         count = count + 1
#         sum = sum + x
#         xstr = input("Please enter the next number (press enter to exit): ")
#     average = sum/count
#     print("The average is {} ".format(average))
# main()

# flavor = input("What flavor do you want [default is vanilla]: ") or "vanilla"
# print(flavor)

# def main():
#     n = int(input("Which Fibonacci number would you like? "))
#     x = [0,1]
#     for i in range(n):
#         x.append(x[-1]+ x[-2])
#     print(x[-3])
# main()

# def main():
# #     n = int(input("Which Fibonacci number would you like? "))
# #     curr, prev = 1, 1
# #     for i in range(n-2):
# #         curr, prev = curr+prev, curr
# #     print(curr)
# # main()

#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

homeprice = {'area': [2600, 3000, 3200, 3600, 4000],
             'price': [550000, 565000, 610000,680000, 725000]}
df = pd.DataFrame.from_dict(homeprice)
print(df)
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area, df.price)
plt.show()

cities = ['adeliadie', 'alice springs', 'melbourne', 'sydney']

with open('cities.txt', 'w') as city_file:
    for city in cities:
        print(city, file=city_file)
cities = []

with open('cities.txt', 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('/n'))
print(cities)
for city in cities:
    print(city, end='')
x = ''
for b in range (1,13):
    a = 2
    y = '{} times {} = {}\n'.format(a, b, a*b)
    x = x + y
print(x)

with open ('sample.txt', 'a') as jabber:
    jabber.write(x)

with open ('sample.txt', 'a') as tables:
    for i in range(2,13):
        for j in range(1,13):
            print("{1:<2} times {0} is {2}".format(i, j, i*j), file=tables)
        print('-'*20, file=tables)
