# https://adventofcode.com/2024/day/3

# APPROACH
# Put each row in a list
# In each list/row, iterate through the elements verifying the conditions
# if any given pair of elements do not conmply, reject the row, otherwise count

# Imports
import re
from typing import TextIO

def file_to_list(file:TextIO) -> list:
    '''
    Opens a file and returns a list with one row in each element of the list
    '''
    # Open file, and put rows/lines in a list
    #with open('input_day02_example.txt', 'r') as f:     # Correct answer is 2
    #with open('input_day02.txt', 'r') as f:             # Correct answer is 670
    with open(file, 'r') as f:
        lines = [line.strip() for line in f]
        #print(lines)
        return lines

# CAN DELETE
def text_to_list(tx:str) -> list:
    '''
    Converts text to a list. Each word/character separated 
    by a space becomes an element

    report in advent of code is a line
    level in advent of code is an element
    '''
    new_list = [ int(element) for element in tx.split() ]
    return new_list

def pattern_finds_in_text(t:str) -> list:
    pattern_finds = re.findall("mul\([0-9]+,[0-9]+\)", t)
    return pattern_finds

def cleanse_finds(l:list) -> list:
    list_to_text = ''.join(l)
    cleansed_finds = re.findall("[0-9]+,[0-9]+", list_to_text)
    return cleansed_finds

def multiply_cleansed(l:list):
    #for e in l:
    #    print("multiply element", e)
    #    digits = e.split(",")
    #    print("multiply digits", digits)
    #    e_multiplication = int(digits[0]) * int(digits[1])
    #    print("multiplication e_multiplication", e_multiplication)
    multiplied_cleansed = [ int(e.split(",")[0]) * int(e.split(",")[1]) for e in l]
    return multiplied_cleansed
    #print(lm)

def main():
    lines = file_to_list('input_day03_example.txt')     # valid records 
    lines = file_to_list('input_day03.txt')             # valid records 
    #print("main lines are of type", type(lines))
    print("number of lines", len(lines))
    total_sum = 0
    for line in lines:
        #print("main line:", line)
        #print("main line is of type", type(line))   # string

        # Put findings of pattern in this line into a list
        pattern_finds = pattern_finds_in_text(line)
        print("main pattern finds in line", pattern_finds)

        cleansed_finds = cleanse_finds(pattern_finds)
        print("main cleansed finds", cleansed_finds)

        multiplied_cleansed = multiply_cleansed(cleansed_finds)
        print("main multiplied cleansed", multiplied_cleansed)

        total_sum = total_sum + sum(multiplied_cleansed)
    print("main total sum", total_sum)


if __name__ == "__main__":
    main()