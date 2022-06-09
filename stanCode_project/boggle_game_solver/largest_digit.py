"""
File: largest_digit.py
Name: Vanessa
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: the integer
	:return: the biggest digit
	"""
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, biggest_num):
	if n < 0:
		n *= (-1)
	if 0 < n <= 9:      # ct+1 = 位數
		ct = 0
	elif 0 < n // 10 <= 9:
		ct = 1
	elif 0 < n // 100 <= 9:
		ct = 2
	elif 0 < n // 1000 <= 9:
		ct = 3
	elif 0 < n // 10000 <= 9:
		ct = 4
	if ct == 0:
		if n > biggest_num:
			biggest_num = n
		return biggest_num
	else:
		# Recursive
		if n // 10**ct > biggest_num:
			biggest_num = n // 10**ct
		n -= (n // 10**ct)*(10**ct)
		return find_largest_digit_helper(n, biggest_num)


if __name__ == '__main__':
	main()
