from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

indata = open(from_file).read()  

# print(f"The input file is {len(indata)} bytes long.")  # that's cool.

# print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input('> ')

out_file = open(to_file, 'w').write(indata)
# print("Alright, all done.")

# out_file.close()


# neat! pydoc <thing> is embedded documentation for python, and
# man <thing> is the embedded documentation for bash

