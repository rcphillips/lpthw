# When you use .notation, it actually calls the function with
# one of the arguments being the thing you're  calling the function on.
# so. my_list.append('ripcat') is the same as append(my_list, 'ripcat')
# So if oyu get a Type Error: too many arguments, that could be why.

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait, we need more.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("Adding: ", next_one)
	stuff.append(next_one)
	print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do stuff!")

print(stuff[1])
print(stuff[-1])  # whoaaaaa
print(stuff.pop())
print(' '.join(stuff))   # whaaaat
print('#'.join(stuff[3:5]))  # huhhhhh?

'''
Data structures. A formal way to structure, some data.
For example a deck of cards.

The cards have values.
They're in a stack or list. They go from the top to the bottom.
You can take cards off the top, bottom, or middle.
You have to look through the deck to find a card.

A list is "An ordered list of things you want to store
and access randomly or linearly by an index."

Lists, then, are good for representing data that.
	- needs to maintain order
	- needs to be able to access randomly by number
	- needs to be gone through linearly.

.pop()
.sort()
.append()

'''
