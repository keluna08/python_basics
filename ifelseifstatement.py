num = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
num3 = int(input("enter the third number:"))
num4 = int(input("enter the fourth number:"))

if num > num2 and num > num3 and num > num4:
    print(f"{num} is greater than {num2},{num3}and {num4}")
elif num2 > num and num2 > num3 and num > num4:
    print(f"{num2} is greater than {num},{num3} and{num4}")
elif num3 > num and num3 > num2 and num3 > num4:
    print(f"{num3} is greater than {num},{num2} and {num4}")
elif num4 > num and num4 > num2 and num4 > num3:
    print(f"{num4} is greater than {num},{num2} and {num3}")
