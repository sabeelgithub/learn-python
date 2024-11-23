
# file handling 
f = open('/Users/mohammedsabeel/MyFiles/sabeel.txt', 'w' )  # w for writing over ride happen
f.write('miss you more \n')
f.close()

f = open('/Users/mohammedsabeel/MyFiles/test.txt', 'a' )  # a for writing over ride not happen
f.write('miss you more again\n')
f.close()

f = open('/Users/mohammedsabeel/MyFiles/test.txt', 'r' )   # r for reading
read = f.read()
print(read)
f.close()
# file handling end
