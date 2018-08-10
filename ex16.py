from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')
# here's the part i don't understand, is, what is "target".
# like. it's a not yet written file. But it has an interaction with an existing 
# file... and like, we don't write to filename. We just write target.
# that's weird. But I guess the connection is forged here, and then it just IS.
# and in this case, we just gave it the filename, but the next line suggests.
# that python will search the path, or at least cwd, for a matching file.

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
'''
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''
target.write(line1+"\n"+line2+"\n"+line3+"\n")
# nailed it
print("And finally, we close it.")
target.close()

# Study Questions
# 3. We have to pass 'w' to open() because otherwise we will just be able to 
# read it.
# 4. The documentation says 
# "Other common values are 'w' for writing (truncating the file if
#  it already exists)"
# So I guess truncate isn't needed? I'm unclear on what that is though.
# If it was called "Delete pre-existing", that'd be one thing. But it's not.
