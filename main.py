################### DEBUGGING #####################

# ? Describe Problem
# def my_function():
#     #! i will never reach 20 because range is not inclusive of the upper bound.
#   for i in range(1, 20):
#     if i == 19:
#       print("You got it")
# my_function()

# ? Reproduce the Bug
# from random import randint

# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# #! randint is inclusive of the upper bound, so when the number is six on a list with length 5 it will throw an error
# #! to fix it, let's change to randint(0, 5)
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# ? Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
#   #! The code skipped 1994 because it didn't include it in the condition
#   #! to fix it, let's change to >= instead of > 1994.
# elif year >= 1994:
#     print("You are a Gen Z.")

# ? Fix the Errors
# #! The age has to be parsed into integer
# age = int(input("How old are you?"))
# if age > 18:
# #! The age has to be printed in an F string.
#   print(f"You can drive at age {age}.")

# ? Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# ? Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
