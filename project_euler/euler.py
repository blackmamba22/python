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
	    of squares and the square of sum.
	print( (sum(list(range(1, 101)))**2) - sum([elem**2 for elem in list(range(1, 101))]) )
	"""

	return (sum(list(range(x, y+1)))**2) - sum([elem**2 for elem in list(range(x, y+1))])

def is_prime(num):

	if num == 1 or num == 2:
		return True

	for n in list(range(2, int(num/2+1))):
		if num % n == 0:
			return False

	return True


def nth_prime_number(num):

	count = 3
	init = 3

	while count < num+1:
		init += 2
		if is_prime(init):
			count += 1

	return init

def sum_of_primes(limit):
	""""Finds the sum of all primes below 'limit'"""
	sum = 0

	for elem in list(range(1,limit, 2)):
		if elem % 5 == 0 or elem % 3 == 0 or elem % 7 == 0 or elem % 11 == 0 or elem % 13 == 0 or elem % 17 == 0 or elem % 19 == 0:
			print(elem)
			continue
		elif is_prime(elem) == True:
			sum += elem
	return sum


def power_digit_sum(num):

	sum = 0
	print (num)
	for elem in str(num):
		sum += int(elem)
	print(sum)

"""
Project Euler #24:
A permutation is an ordered arrangement of objects. For example, 3124 is one possible
permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed
numerically or alphabetically, we call it lexicographic order. The lexicographic
permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""



if __name__ == '__main__':
	#print(sum_of_primes(2000000))
	power_digit_sum(2**1000)
