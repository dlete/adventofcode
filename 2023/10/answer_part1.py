import numpy as np
import numpy.typing as npt
from typing import TextIO

def file_open(input_file:TextIO) -> list:
    """Opens a file and returns a list with the lines as its elements

    Opens a file as read only. Each line becomes an element of a list. 
    Each line/element is a string object.

    Args:
        input_file: filepath. String instance.

    Returns:
        A list. Each line in the input file is an element of the list.
    """
    with open(input_file) as file:
        # read all the lines in the file object and put them into a list
        # each line is an element of the list ('lines' in the code below)
        lines = file.readlines()

    # Verify
    #print("FILE OPEN")
    #print("type is:", type(lines), "lenght is:", len(lines), "content is:", lines)
    #print("\n")
    
    # Finish
    return lines

def prepare_input(lines_raw:list) -> list:
    """Takes a list of lists with raw data, returns a list of lists with processed data

    Goes list by list and sanitizes its elements.

    Args:
        lines_raw: List of lists. The elements in the inner lists are the raw input. 
    
    Returns:
        lines: List of lists. The elements in the inner lists are the raw input once 
            it has been sanitized.
    """
    # Initialize list to contain the processed data
    lines_processed = []

    # Sanitize line by line
    for line in lines_raw:
        # Convert each line to a list (initially the lines are of type string)
        line = line.split(" ")
        # Remove leading/trailing characters
        # and convert from string to list, 
        line = [entry.strip() for entry in line]
        line = list(line[0])
        lines_processed.append(line)

    # Verify
    #print("PREPARE INPUT")
    #for line in lines_processed:
    #    #print("type is:", type(line), "content is:", line)
    #    print("lenght of the line:", len(line))
    #print("\n")

    # Finish
    return lines_processed

def convert_to_array(a: npt.ArrayLike) -> np.ndarray:
    as_array = np.array(a)
    # Verify
    #print("CONVERTO TO ARRAY")
    #print("have converted from type", type(a), "to type", type(as_array))
    #print("array is:\n", as_array)

    # Finish
    return as_array


def character_to_indexes(field: np.ndarray, character_to_locate:str) -> tuple:
    """Finds a character in a matrix, returning its position
    
    Args:
        field: np.ndarray
    
    Return:
        coordinates: tuple
    """
    coordinates = np.where(field==character_to_locate)
    # Validate
    print("CHARACTER TO INDEXES", 
          "character:", character_to_locate,
          "position is of type", type(coordinates), 
          "position is of value", coordinates, 
          "integer row", coordinates[0][0], "integer column", coordinates[1][0])

    # Finish
    return coordinates

def load_tiles():
    v_bar = [
        ['.', True, '.'],
        ['.', '.', '.'],
        ['.', True, '.'],
    ]
    h_bar = [
        ['.', '.', '.'],
        [True, '.', True],
        ['.', '.', '.'],
    ]

    ne = [
        ['.', True, '.'],
        ['.', '.', True],
        ['.', '.', '.'],
    ]

    nw = [
        ['.', True, '.'],
        [True, '.', '.'],
        ['.', '.', '.'],
    ]

    se = [
        ['.', '.', '.'],
        ['.', '.', True],
        ['.', True, '.'],
    ]

    se = [
        ['.', '.', '.'],
        [True, '.', '.'],
        ['.', True, '.'],
    ]

    ground = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ]


def can_connect(field:np.ndarray, position_a:tuple, position_b:tuple, connection_a):
    """Says if positions a and b can connect to each other through a given side of a"""
    return True


def character_perimeter(field:np.ndarray, character:str, position:tuple) -> np.ndarray:
    character_perimeter = []
    position_row = position[0]
    position_column = position[1]

    # Sweept row at a time
    for i in range(-1, 2):
        #print("sweeping row", i)
        row = []
        # sweep columns in a given row
        for j in range(-1, 2):
            #print("sweeping column", j)
            # retrieve character and append to row
            element = field.item((position_row+i, position_column+j))
            row.append(element)
        # Append full row to the list of rows
        #print("row fully populated is:", row)
        character_perimeter.append(row)

    # Convert the list of lists (list of rows) to NumPy array
    character_perimeter = np.array(character_perimeter)

    # Finish
    print("CHARACTER PERIMETER, the perimeter of character", character, "in coordindates", position, "is: \n", character_perimeter)
    return character_perimeter

def sandbox():
    # Open input file
    lines = file_open("input_part1_example1.txt")
    #lines = file_open("puzzle.txt")

    # Prepare the data
    lines = prepare_input(lines)

    # Convert to NumPy matrix
    field = convert_to_array(lines)
    #print("SANDBOX, matrix", field)

    # Position of character 'S'
    character_to_locate = 'S'
    character_position_array = character_to_indexes(field, character_to_locate)
    character_tuple = (character_position_array[0][0], character_position_array[1][0])
    #print("SANDBOX")
    #print("confirm that the character we start with:", character_to_locate, 
    #      "is the same that we find in coordinates", character_tuple,
    #      "that is:", field.item(character_tuple))
    
    s_perimeter = character_perimeter(field, character_to_locate, character_tuple)


# Execute this function automatically when the file is invoked from the CLI
print("\n")
sandbox()