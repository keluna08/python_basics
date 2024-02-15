num = float(input("enter  first number:"))
num2 = float(input("enter  second number:"))
print("select command")

print("1.add numbers")
print("2.subtract numbers")
print("3.multiply numbers")
print("4.divide numbers")
print("5.exponential")
choice = input("select command:")

if choice == "1":
    print(f"the sum of {num} and {num2} is {num+num2}")
elif choice == "2":
    print(f"the difference of {num} and {num2} is {num-num2}")
elif choice == "1":
    print(f"the product of {num} and {num2} is {num*num2}")
elif choice == "1":
    print(f"the division of {num} and {num2} is {num+num2}")
elif choice == "1":
    print(f"the exponential of {num} and {num2} is {num**num2}")
else:
    print("invalid choice")
