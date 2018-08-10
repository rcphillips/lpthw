# this imports the argv module from the sys library?
from sys import argv
# the argv module [0] is the script name. Like, the file name. We can set it up
# such that we run
# the script WITH additional arguments, anad those will be passed in order
# to the variables when argv is 'unpacked' like here
script, filename = argv
# we passed the filename ex15_sample.txt. This is 'opening' that file
# and assigning the object(?) to the variable txt.
txt = open(filename)


# this is printing the argument that we passed on the command line.
print(f"Here's your file {filename}:")
# this is reading the file with no parameters?
print(txt.read())

# i don't really understand what close() does.
txt.close()

'''
# here we're doing the same thing, but the filename is getting in there cuz 
# the user is putting it in mid run.
print("Type the filename again:")
# we give them a prompt here.
file_again = input("> ")
# we open the file pointed to by their input
txt_again = open(file_again)
# and we read that, and print the result. which is the text.
print(txt_again.read())
'''

# I like just the command line better, cuz it's all in one place. Like.
# We just let it run and it works or it doesn't.
