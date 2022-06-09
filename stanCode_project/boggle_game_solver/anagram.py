"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


def main():
    """
    TODO:
    """
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        start = time.time()
        if s == EXIT:
            break
        else:
            find_anagrams(s)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary(s):
    dictionary_dict = {}
    with open(FILE, 'r') as f:
        for line in f:
            new_line = line.strip()
            if new_line[0] in s and len(new_line) == len(s):
                if matching_char(s, new_line):
                    if new_line[0] not in dictionary_dict:
                        dictionary_dict[new_line[0]] = [new_line]
                    else:
                        dictionary_dict[new_line[0]].append(new_line)
    return dictionary_dict


def matching_char(s, new_line):
    for ch in new_line:
        if ch not in s:
            return False
    return True


def find_anagrams(s):
    """
    :param s: user's input
    :return:
    """
    current_lst = []
    dict_dict = read_dictionary(s)
    print('Searching...')
    find_anagrams_helper(s, '', [], len(s), current_lst, dict_dict)
    print(f'{len(current_lst)} anagrams: {current_lst}')


def find_anagrams_helper(s, current_str, ans, s_len, current_lst, dict_dict):
    if len(ans) == s_len:   # ans: the index of s
        for j in ans:
            current_str += s[j]
        if current_str in dict_dict[current_str[0]] and current_str not in current_lst:
            current_lst.append(current_str)
            print(f'Found: {current_str}')
            print('Searching...')
    else:
        for i in range(len(s)):
            if i in ans:
                pass
            else:
                # Choose
                ans.append(i)
                # Explore
                find_anagrams_helper(s, current_str, ans, s_len, current_lst, dict_dict)
                # Un-choose
                ans.pop()


# def has_prefix(lst, sub_s):
#     """
#     :param sub_s: the substring
#     :return: Return True if dictionary has sub_s, otherwise return False
#     """
#     for word in lst:
#         if word.startswith(sub_s):
#             return True
#     return False


if __name__ == '__main__':
    main()
