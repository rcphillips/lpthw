def number_lister(stop_point):
	numbers = []
	for i in range(stop_point):
		print(f"At the top i is {i}.")
		numbers.append(i)
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")
	print("The numbers: ")
	for num in numbers:
		print(num)


stop_point = int(input("Range whaa? "))

number_lister(stop_point)
