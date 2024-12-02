# https://adventofcode.com/2024/day/2

# APPROACH
# Put each row in a list
# In each list/row, iterate through the elements verifying the conditions
# if any given pair of elements do not conmply, reject the row, otherwise count

# Imports
from typing import TextIO

def file_to_list(f:TextIO) -> list:
    '''
    Opens a file and returns a list with one row in each element of the list
    '''
    # Open file, and put rows/lines in a list
    with open('input_day02_example.txt', 'r') as f:
    #with open('input_day02.txt', 'r') as f:
        lines = [line.strip() for line in f]
        #print(lines)
        return lines


def text_to_list(tx:str) -> list:
    '''
    Converts text to a list. Each word/character separated 
    by a space becomes an element

    report in advent of code is a line
    level in advent of code is an element
    '''
    new_list = [ int(element) for element in tx.split() ]
    return new_list


def check_rules(l:list) -> bool:
    '''
    Checks if the absolute value of the difference between 
    two intergers is between 1 and 3 
    Checks is the elements are ascencing
    Checks if the elements are descencing

    Make two copies of the input list
    remove the first element of one
    remove the last element of the other
    delete one list from the other checking the rule operation wise
    '''
    la = list(l)
    lb = list(l)
    la.pop(-1)
    lb.pop(0)
    checks_deltas = [ (0 < abs(b-a) < 4) for b, a in zip(lb, la)]
    checks_ascending = [ (0 < (b-a)) for b, a in zip(lb, la)]
    checks_descending = [ ((b-a) < 0) for b, a in zip(lb, la)]

    if False in checks_deltas:
        status_delta = False
    else:
        status_delta = True
    
    if False in checks_ascending:
        status_ascending = False
    else:
        status_ascending = True
    
    if False in checks_descending:
        status_descending = False
    else:
        status_descending = True


    if (status_ascending or status_descending) is True:
        status_growth = True
    else:
        status_growth = False

    print("list b", lb)
    print("list a", la)
    print("check deltas", checks_deltas)
    print("status delta", status_delta)
    print("check ascencing", checks_ascending)
    print("status ascending", status_ascending)
    print("check descending", checks_descending)
    print("status descending", status_descending)
    print("status growth", status_growth)

    if (status_growth and status_delta) is True:
        return True
    else:
        return False


valid_records = 0
lines = file_to_list('input_day02_example.txt')
for line in lines:
    record = text_to_list(line)
    print("record:", record)

    record_status = check_rules(record)
    print("record status", record_status, "\n")
    if record_status == True:
        valid_records += 1

print("valid records", valid_records)
