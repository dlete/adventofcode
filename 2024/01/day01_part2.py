# https://adventofcode.com/2024/day/1

# Open file, and put lines in a list
#with open('input_day01_example.txt', 'r') as f:
with open('input_day01.txt', 'r') as f:
    lines = [line.strip() for line in f]
    #print(lines)

# Put the first character of each line in list l_1, the second in list l_2
l1 = [ int(element.split()[0]) for element in lines ]
l2 = [ int(element.split()[1]) for element in lines ]
l1.sort()
l2.sort()

# Create list with "similarities" of each element in l1
l1_counts_in_l2 = [ l2.count(element) for element in l1]
similarities = [ element * l2.count(element) for element in l1]

# Sum elements of similarities
my_sum = sum(similarities) 

# Show results
#print("list 1")
#print(l1)
#print("list 2")
#print(l2)
#print("each element of l1 appears these times in l2")
#print(l1_counts_in_l2)
#print("similarities")
#print(similarities)
#print("total similarity")
print(my_sum)