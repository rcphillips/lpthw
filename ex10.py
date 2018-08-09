tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

even_fatter_cat = '''
what\a test test\n
\b test 
\f
'''

print(even_fatter_cat)

cat_name = '\n\t\\Ripleyxander\n\tCatilton\\'

print(f"My cat's name is {cat_name}.")