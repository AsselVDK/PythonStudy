# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и
# сохраните в переменные, выведите на экран.

name = input("Please, enter your name: ")
print("Hello " + name + ", welcome to the questionnaire")

age = input("How old are you, " + name + "? ")
print(age + " is a good age")

period = 9
period_age = int(age) + period
print("In 2030 you will be " + str(period_age))
