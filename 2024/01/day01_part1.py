# https://adventofcode.com/2024/day/1

# Open file, and put lines in a list
#with open('input_day01_example.txt', 'r') as f:
with open('input_day01.txt', 'r') as f:
    lines = [line.strip() for line in f]
    print(lines)

# Put the first character of each line in list l_1, the second in list l_2
l_1 = [ int(element.split()[0]) for element in lines ]
l_2 = [ int(element.split()[1]) for element in lines ]
l_1.sort()
l_2.sort()

# Substract the two lists
l_3 = [abs(l_2_i - l_1_i) for l_2_i, l_1_i in zip(l_2, l_1)]

# Sum elements of the difference
my_sum = sum(l_3) 

# Show results
#print(l_1)
#print(l_2)
#print(l_3)
print(my_sum)