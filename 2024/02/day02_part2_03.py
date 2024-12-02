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


def percolator(l: list, report_deltas: tuple, report_ascending: tuple, report_descending: tuple, tokens: int):
    '''
    take a list, 
    find where it fails, 
    remove the block, 
    go and chec,
    if fails, go again removing other block

    you need a coutner
    '''
    print("percolator invoked")
    #print("percolator entry tokens", tokens)
    tokens -=1
    #print("percolator out tokens", tokens)

    #print("percolator report deltas", report_deltas)
    #print("percolator report_ascending", report_ascending)
    #print("percolator report_descending", report_descending)

    if (report_deltas[0]==False and (report_ascending[0]==True or report_descending[0]==True)):
        print("percolator Case Deltas FAIL, Growth PASS")
        index_first_false = report_deltas[1].index(False)

    if (report_deltas[0]==False and (report_ascending[0]==False or report_descending[0]==False)):
        print("percolator Case Deltas FAIL, Ascending FAIL, Descending FAIL")
        index_first_false_delta = report_deltas[1].index(False)
        try:
            index_first_false_ascending = report_ascending[1].index(False)
        except:
            index_first_false_ascending = 1000
        try:
            index_first_false_descending = report_descending[1].index(False)
        except:
            index_first_false_descending = 1000
        
        index_first_false = min(index_first_false_delta, 
                                index_first_false_ascending,
                                index_first_false_descending)
        
    if (report_deltas[0]==True and (report_ascending[0]==False or report_descending[0]==False)):
        print("percolator Case Deltas PASS, Ascending FAIL or Descending FAIL")
        try:
            index_first_false_ascending = report_ascending[1].index(False)
        except:
            index_first_false_ascending = 1000
        try:
            index_first_false_descending = report_descending[1].index(False)
        except:
            index_first_false_descending = 1000
        
        index_first_false = min(index_first_false_ascending,
                                index_first_false_descending)

    print("percolator index_first_false", index_first_false)

    li = list(l)
    li.pop(index_first_false+1)
    print("percolator list with removed element", li)
    second_try = check_rules(li, tokens)
    print("percolator second try", second_try)
    return second_try


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


def  check_rules_00(l:list, tokens: int) -> bool:
    print("check_rules check_rules invoked")
    report_deltas = check_deltas(l)
    report_ascending = check_ascending(l)
    report_descending = check_descending(l)

    print("check_rules report_deltas", report_deltas)
    print("check_rules report_ascending", report_ascending)
    print("check_rules report_descending", report_descending)

    # Deltas
    if report_deltas[0] is True:
        status_deltas = True
    else:
        status_deltas = False
        
    # Growth = ascending or descending
    if (report_ascending[0] or report_descending[0]) is True:
        status_growth = True
    else:
        status_growth = False

    # Growth and Deltas
    if (status_growth and status_deltas) is True:
        return True
    else:
        if tokens > 0:
            try_again = percolator(l, report_deltas, report_ascending, report_descending, tokens)
            return try_again
        else:
            return False

def  check_rules(l:list, tokens: int) -> bool:
    print("check_rules check_rules invoked")
    report_deltas = check_deltas(l)
    report_ascending = check_ascending(l)
    report_descending = check_descending(l)

    print("check_rules lista", l)
    print("check_rules report_deltas", report_deltas)
    print("check_rules report_ascending", report_ascending)
    print("check_rules report_descending", report_descending)
    tokens -=1

    # T (FT / TF / TT)
    if ( (report_deltas[0] is True) and ((report_ascending[0] is True) or (report_descending[0] is True))):
        return True
    if tokens < 0:
        return False
    
    # F (FT / TF / TT)
    if ( (report_deltas[0] is False) and ((report_ascending[0] is True) or (report_descending[0] is True))):
        index_first_false_delta = report_deltas[1].index(False)
        index_first_false = index_first_false_delta
    # T F F
    if ( (report_deltas[0] is True) and ((report_ascending[0] is False) and (report_descending[0] is False))):
        if report_ascending[1].count(False) == 1:
            index_first_false_ascending = report_ascending[1].index(False)
        else:
            index_first_false_ascending = 1000

        if report_descending[1].count(False) == 1:
            index_first_false_descending = report_descending[1].index(False)
        else:
            index_first_false_descending = 1000
        
        index_first_false = min(index_first_false_ascending,
                                index_first_false_descending)
        if index_first_false == 1000:
            return False
    # F F F
    if ( (report_deltas[0] is False) and ((report_ascending[0] is False) and (report_descending[0] is False))):
        index_first_false_delta = report_deltas[1].index(False)
        if report_ascending[1].count(False) == len(report_ascending[1]):
            index_first_false_ascending = 1000
        else:
            index_first_false_ascending = report_ascending[1].index(False)

        if report_descending[1].count(False) == len(report_descending[1]):
            index_first_false_descending = 1000
        else:
            index_first_false_descending = report_descending[1].index(False)

        index_first_false = min(index_first_false_delta,
                                index_first_false_ascending,
                                index_first_false_descending)

    li = list(l)
    li.pop(index_first_false+1)
    try_again = check_rules(li, tokens)
    return try_again


def main():
    valid_records = 0
    #lines = file_to_list('input_day02_example.txt')     # valid records 4
    lines = file_to_list('input_day02.txt')             # valid records 686 
    for line in lines:
        tokens = 1
        record = text_to_list(line)
        print("main record:", record)

        record_status = check_rules(record, tokens)
        print("main record status", record_status, "\n")
        if record_status == True:
            valid_records += 1

    print("valid records", valid_records)


if __name__ == "__main__":
    main()