def number_lister(stop_point, increment):
	i = 0
	numbers = []
	while i < stop_point:
		print(f"At the top i is {i}.")
		numbers.append(i)
		i = i + increment
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")
	print("The numbers: ")
	for num in numbers:
		print(num)


stop_point = int(input("Range whaa? "))
increment = int(input("increment whaaa? "))

number_lister(stop_point, increment)
