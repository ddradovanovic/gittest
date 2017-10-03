file1 = open('test.txt', 'w')
file1.write('Hey I am here')
file1.close()

file1 = open('test.txt', 'r')
content = file1.read()
print(content)


file1 = open('test.txt', 'a')
file1.write('\nI am going to try something new for a change.')
file1.close()