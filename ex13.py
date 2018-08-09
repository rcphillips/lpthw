from sys import argv
# read the WYSS section for how to run this
# oh that's the What you should see section.
script, first, second, third = argv
fourth = input("put something else too")
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("The other thing you put is:", fourth)

# good to know. Command line inputs come in as strings.
print(type(third))
# as does info gathered with input()
print(type(fourth))