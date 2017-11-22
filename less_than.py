def less_than(numList):
	newList = []
	for i in numList:
		if (i < 5): 
			newList.append(i)
	print(newList)
	newList = []
	user_input = int(input("Enter a number "))
	for i in numList:
		if (i < user_input):
			newList.append(i)
	print(newList)
less_than  ([])
