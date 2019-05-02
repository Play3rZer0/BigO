def binary_search(X, item):
	first = 0
	last = len(X)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if X[mid] == item :
			found = True
			print("The element item", item, "was found at index ", X.index(60))
		else:
			if item < X[mid]:
				last = mid - 1
			else:
				first = mid + 1
	return found

print(binary_search([10, 15, 35, 42, 60, 70, 82, 94], 60))
