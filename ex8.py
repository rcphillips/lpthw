formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"His name is Ripley",
	"And he's a house-cat",
	"Not a damn louse-cat",
	"Just a great house-cat!"
))
# It's interesting with this last one, that there are spaces.... Ohhh they're
# contained in the original formatter string. {} SPACE {}
