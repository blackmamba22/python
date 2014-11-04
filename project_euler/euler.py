#!/usr/bin/python3


def sum_of_square(x, y):
	"""Returns the sum of the numbers squared from x to y."""

	if not isinstance(x, int) or not isinstance(y, int):
		raise ValueError('Please enter integer values.')		

	x_to_y = list(range(x, y+1))
	sum = 0

	for n in x_to_y:
		sum += n**2

	return sum

def square_of_sum(x, y):
	"""Returns the square of the sum of numbers x through y inclusive."""

	if not isinstance(x, int) or not isinstance(y, int):
		raise ValueError('Please enter integer values.')

	x_to_y = list(range(x, y+1))
	sum = 0

	for n in x_to_y:
		sum+= n
	
	return (sum**2)
	


def sum_square_difference(x, y):
	""" Returns the difference between the sum
	    of squares and the square of sum."""

	sum_of_square = sum([elem**2 for elem in list(range(x, y+1))])
	square_of_sum = sum(list(range(x, y+1)))**2

	return square_of_sum - sum_of_square

def sum_square_difference_short(x, y):
	""" Returns the difference between the sum
	    of squares and the square of sum."""

	return (sum(list(range(x, y+1)))**2) - sum([elem**2 for elem in list(range(x, y+1))])
	
	

if __name__ == '__main__':
	#sum_square_diff = square_of_sum(1,100) - sum_of_square(1, 100)
	#print(sum_square_diff)   #The answer

	print(sum_square_difference_short(1, 100))
	print( (sum(list(range(1, 101)))**2) - sum([elem**2 for elem in list(range(1, 101))]) )
	
