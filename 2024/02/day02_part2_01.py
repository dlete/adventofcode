# https://adventofcode.com/2024/day/2

# APPROACH
# Put each row in a list
# In each list/row, iterate through the elements verifying the conditions
# if any given pair of elements do not conmply, reject the row, otherwise count

# Imports
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


def text_to_list(tx:str) -> list:
    '''
    Converts text to a list. Each word/character separated 
    by a space becomes an element

    report in advent of code is a line
    level in advent of code is an element
    '''
    new_list = [ int(element) for element in tx.split() ]
    return new_list


def percolator(l: list, report_deltas: tuple, report_ascending: tuple, report_descending: tuple):
    '''
    take a list, 
    find where it fails, 
    remove the block, 
    go and chec,
    if fails, go again removing other block

    you need a coutner
    '''
    print("percolator invoked")
    print("report deltas", report_deltas)
    deltas_falses = report_deltas[1].count(False)
    ascending_falses = report_ascending[1].count(False)
    descending_falses = report_descending[1].count(False)

    #if ((ascending_falses or descending_falses) > 1):
    #    print("Impossible to salvaje, more than 1 False in ascending/descending")
    #    return False


    if (report_deltas[0]==False and (report_ascending[0]==True or report_descending[0]==True)):
        print("Case Deltas FAIL, Growth PASS")
        # percolate deltas
        pass
    if (report_deltas[0]==True and (report_ascending[0]==False and report_descending[0]==False)):
        print("Case Deltas PASS, Growth FAIL")
        # find who fails
        # percolate ascending and descending and deltas!!!
        pass   
    if (report_deltas[0]==False and (report_ascending[0]==False and report_descending[0]==False)):
        print("Case Deltas FAIL, Growth FAIL")
        # percolate deltas, ascending and descending
        pass
 


def check_deltas(l:list) -> tuple[bool, list]:
    '''
    Checks if the absolute value of the difference between 
    two intergers is between 1 and 3 

    Make two copies of the input list
    remove the first element of one
    remove the last element of the other
    delete one list from the other checking the rule operation wise
    '''
    la = list(l)
    lb = list(l)
    la.pop(-1)
    lb.pop(0)
    checks_deltas = [ (0 < abs(b-a) < 4) for b, a in zip(lb, la) ]

    if False in checks_deltas:
        status_delta = False
    else:
        status_delta = True
    
    return (status_delta, checks_deltas)


def check_ascending(l:list) -> tuple[bool, list]:
    '''
    Checks is the elements are ascencing

    Make two copies of the input list
    remove the first element of one
    remove the last element of the other
    delete one list from the other checking the rule operation wise
    '''
    la = list(l)
    lb = list(l)
    la.pop(-1)
    lb.pop(0)
    checks_ascending = [ (0 < (b-a)) for b, a in zip(lb, la)]

    if False in checks_ascending:
        status_ascending = False
    else:
        status_ascending = True
    
    return (status_ascending, checks_ascending)

def check_descending(l:list) -> tuple[bool, list]:
    '''
    Checks is the elements are descencing

    Make two copies of the input list
    remove the first element of one
    remove the last element of the other
    delete one list from the other checking the rule operation wise
    '''
    la = list(l)
    lb = list(l)
    la.pop(-1)
    lb.pop(0)
    checks_descending = [ ((b-a) < 0) for b, a in zip(lb, la)]

    if False in checks_descending:
        status_descending = False
    else:
        status_descending = True
    
    return (status_descending, checks_descending)


def  check_rules(l:list) -> bool:
    report_deltas = check_deltas(l)
    report_ascending = check_ascending(l)
    report_descending = check_descending(l)

    print("check_rules report_deltas", check_deltas(l))
    print("check_rules report_ascending", check_ascending(l))
    print("check_rules report_descending", check_descending(l))

    # Growth = ascending or descending
    if (report_ascending[0] or report_descending[0]) is True:
        status_growth = True
    else:
        status_growth = False

    # Deltas
    if report_deltas[0] is True:
        status_deltas = True
    else:
        status_deltas = False

    # Growth and Deltas
    if (status_growth and status_deltas) is True:
        return True
    else:
        try_again = percolator(l, report_deltas, report_ascending, report_descending)
        return False


def main():
    valid_records = 0
    lines = file_to_list('input_day02_example.txt')
    for line in lines:
        record = text_to_list(line)
        print("main record:", record)

        #record_status = check_rules(record)
        #print("record status", record_status, "\n")
        #if record_status == True:
        #    valid_records += 1

        record_status = check_rules(record)
        print("main record status", record_status, "\n")
        if record_status == True:
            valid_records += 1

    print("valid records", valid_records)


if __name__ == "__main__":
    main()