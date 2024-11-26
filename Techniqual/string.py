# Q - Write a pogramme to count occurance of each word in a string

# ans1
def word_count(str):
    str_list = str.split()
    count_dict = {}
    for item in str_list:
        if item not in count_dict.keys():
            count_dict[item] = 1
        else:
            count_dict[item] += 1

    return print(count_dict)

# word_count("hello world hello koi world world")

# ans 2
from collections import Counter

def word_count(str):
    str_list = str.split()
    return print(Counter(str_list))

# word_count("hello world hello koi world world")



