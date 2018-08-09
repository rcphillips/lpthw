
# sets the types_of_people variable to ten
types_of_people = 10
# sets x to this string, which calls on the previous variable 
x = f"There are {types_of_people} types of people."
# sets binary to be a string saying binary
binary = "binary"
# sets do_not to be a string, don't
do_not = "don't"
# sets y to be a string which calls on  two previously established variables
y = f"Those who know {binary} and those who {do_not}."
# prints our two strings
print(x)
print(y)
# whereas before we directly printed the strings, now we're
# embedding the strings in slightly larger strings. Cool.
print(f"I said: {x}")
print(f"I also said: '{y}'")
# setting the variable hilarious to a boolean value, False.
hilarious = False
# looks like we're setting up a new string here, and we're leaving some {} for 
# a variable to slot in?
joke_evaluation = "Isn't that joke so funny?! {}"
# we're printing that string, but we're using dot notation to call the
# hilarious variable, AND we're formatting that variable?
print(joke_evaluation.format(hilarious))
# setting more variables as strings
w = "This is the left side of..."
e = "a string with a right side."
# concatenating those strings, with no gap. Just smooshed together.
print(w + e)

# 1. Comments are in
# 2. Places where a string is put inside a string:
# 		Line 11, Line 11 but later, line 17, and line 18
# 3. I don't think you're lying. The fairest interpretation is that line 26 
# 		is not really putting a string in a string, but reformatting a boolean as
# 		a string
# 4. It's literally adding the start of e to the end of w. result: longer.
