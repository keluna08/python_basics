# list datastructure

# list is mutable/changeable/ordered

my_list = ["banana", "mangoes", "apples", "celery"]
my_list.sort()
print(my_list)
my_list[1] = "strawberries"
print(f"I love eating {my_list[0]}")
print(f"I love eating {my_list[1]}")

list = [1, 34, 89, 43, 5, 23, 100]
list.sort()
list.append(24)
print(list)
list[2] = 56
print(f"I had {list[2]}mangoes yesterday.")

# tuple datastructures
# tuple are immutable/unchangeable/ordered
my_tuple = ("toothbrush", "towels", "slippers", "facewash")
print(my_tuple)
print(f"I forgot to buy a {my_tuple[1]}")

# set datastructure
# unordered---it has no index
# mutable
my_set = {"Kenya", "Rwanda", "Mozambique"}
my_set.add("ivory coast")
print(my_set)

# dictionaries datastructures
#mutable
my_dic={"name":"Natasha","age":"18","gender":"female","profession":"doctor"}
print(my_dic)
print(f"my name is {my_dic['name']}.I'm a {my_dic['gender']} of {my_dic['age']} and I aspire to be a {my_dic['profession']}.")