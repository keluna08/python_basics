# sum_of_a_list:

# def calculate_sum(first):
#     total = 0
#     for num in first:
#         total += num
#     return total
#
#
# my_list = [2, 3, 4, 6, 4, ]
# result = calculate_sum(my_list)
# print("The sum of the list is:", result)


# copied example

def calculate_sum():
    list = [20, 30, 50]
    sum_list = 0
    for num in list:
        sum_list = sum_list + num
        print(f"The sum of the list is {sum_list}")


calculate_sum()

# reverse a string
str = "Welcome to my practice"

words = str.split()
print(words)

words = words[-1::-1]
print(words)

str = "reverse me"
print(str)
print(str[::-1])


# easier

def ispalindrome():
    str = input("Enter a string:")


if str == str[::-1]:
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")
ispalindrome()



# check if year is a leap year

year