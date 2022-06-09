"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	s_lst = []   # s_lst: user's input string
	for i in range(4):
		row = input(f'{i+1} row of letters: ')
		row = row.lower()
		if len(row) != 7:
			print('Illegal input')
			break
		else:
			for j in range(len(row)):
				if j % 2 == 0:
					if not row[j].isalpha():
						print('Illegal input')
						break
				else:
					if not row[j] == ' ':
						print('Illegal input')
						break
		for ele in row:
			if ele.isalpha():
				s_lst.append(ele)
		new_lst = [s_lst[:4], s_lst[4:8], s_lst[8:12], s_lst[12:]]
	start = time.time()
	####################
	find_anagrams(s_lst, new_lst)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_anagrams(s_lst, new_lst):
	ans_lst = []    # ans_lst: the word that in the dictionary
	dict_dict = read_dictionary(s_lst)
	for y in range(4):
		for x in range(4):
			find_anagrams_helper(x, y, s_lst, new_lst, ans_lst, '', [], dict_dict)
	print(f'There are {len(ans_lst)} in total.')


def find_anagrams_helper(x, y, s_lst, new_lst, ans_lst, ans_str, ans, dict_dict):
	if len(ans_str) >= 4:
		if ans_str in dict_dict[ans_str[0]] and ans_str not in ans_lst:
			print('Found: '+ans_str)
			ans_lst.append(ans_str)

	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			x_new = x+i
			y_new = y+j
			if 0 <= x_new < 4 and 0 <= y_new < 4:
				if (x_new, y_new) not in ans:
					# Choose
					ans.append((x+i, y+j))
					ans_str += new_lst[x_new][y_new]
					# Explore
					if has_prefix(ans_str, dict_dict):
						find_anagrams_helper(x_new, y_new, s_lst, new_lst, ans_lst, ans_str, ans, dict_dict)
					# Un-choose
					ans.pop()
					ans_str = ans_str[:-1]
					x_new -= i
					y_new -= j
	return ans_lst


def read_dictionary(s_lst):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary_dict = {}
	with open(FILE, 'r') as f:
		for line in f:
			new_line = line.strip()
			if new_line[0] in s_lst and 4 <= len(new_line) <= 16:
				if matching_char(s_lst, new_line):
					if new_line[0] not in dictionary_dict:
						dictionary_dict[new_line[0]] = [new_line]
					else:
						dictionary_dict[new_line[0]].append(new_line)
	return dictionary_dict


def matching_char(s_lst, new_line):
	for ch in new_line:
		if ch not in s_lst:
			return False
	return True


def has_prefix(sub_s, word_dict):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param word_dict: (dict) The dictionary of the input s
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in word_dict[sub_s[0]]:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
