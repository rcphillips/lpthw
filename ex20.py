from sys import argv

script, input_file = argv


def print_all(f):
	print(f.read())


def rewind(f):
	f.seek(0)


def print_a_line(line_count, f):
	print(line_count, f.readline(), end='')


# So, readline is the really interesting thing here.
# it reads the current line, which appears to be 0 when we seek to 0,
# and advances at each \n encountered. Like. The structure of the document is 
# such.
# running these functions doesn't advance the position. We do that manually.
# though I wonder if it would outside of a function.

# So it's not acutally using current line!! That's just to show the line.
# hey buddy, that's a pernicious use of counting. Readline() DOES increment it. 
# with each call. Hmm.

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)