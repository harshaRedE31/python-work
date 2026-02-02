# Writing to a file
with open('example.txt', 'w') as file:
  file.write('Hello, World!\n')
  file.write('This is a test file.')

# Reading from a file
with open('example.txt', 'r') as file:
  content = file.read()
  print(content)

# Reading line by line
with open('example.txt', 'r') as file:
  for line in file:
    print(line.strip())

# Appending to a file
with open('example.txt', 'a') as file:
  file.write('\nAppended text.')

# Reading into a list
with open('example.txt', 'r') as file:
  lines = file.readlines()
  print(lines)