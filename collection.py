from collections import Counter

# Create a Counter from a iterables
st = "hello world hello koi world world"
li = ["Hi",1,2,2,"Hi"]
tu = ("Hi",1,2,2,"Hi")
se = {"Hi",1,2,2,"Hi"}
di = {"one":1,"two":1,"three":1}
word_count = Counter(di)

# Print the count of each word
print(word_count)
