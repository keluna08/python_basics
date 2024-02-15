# SUM_OF_A_LIST
import math


def sum_of_list():
    list1=[20,30,45,60]
    sum_list1=0
    for n in list1:
        sum_list1+=n
        print(f"The sum of list1 is {sum_list1}")
sum_of_list()


# reverse a string
str="I am learning Python"
print(str)
print(str[::-1])


# palindrome or not
def palindrome():
    str=input("Enter the string:")
    if str==str[::-1]:
        print("palindrome")
    else:
        print("not palindrome")
palindrome()

# check if year is a leap year
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# Example usage:
year = 2024
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



# area of a circle
def areaofacircle():
    r=float(input("Enter the radius:"))
    math.pi=3.142
    print(f"The area of a circle is {math.pi*r*r}")





