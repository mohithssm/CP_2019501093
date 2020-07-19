"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):

	sort(array, 0, len(array) - 1)

def sort(array, low, high):
	if low < high:
		p = partition(array, low, high)
		sort(array, low, p-1)
		sort(array, p+1, high)

def partition(array, low, high):
	i = low - 1
	pivot = array[high]

	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			array[i], array[j] = array[j], array[i] 
	array[i+1], array[high] = array[high], array[i+1]
	return (i+1)
