# put input in list of lists
# each list is one row
# all lists should have the same lenght
#
# iterate through each list to find digits
# when a digit is found
#  look around for symbols
#  look besides for another digit, or not
#  save the whole number
#  mark the number as a part or a no-part


# Open intput file, create a list with element being one of the lines
# https://realpython.com/read-write-files-python/#tips-and-tricks
#with open("input_example_part1_game1.txt", "r") as file:
#with open("input_example_part1_game4.txt", "r") as file:
#with open("input_example_part1.txt", "r") as file:
#with open("input_example_day03_part1.txt", "r") as file:
#    # read the lines from the file object and return them as a list
#    lines = file.readlines()
#    #print(type(games))    # this is a list

# https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings

def file_open(input_file):
    """Opens a file as read and returns a list with the lines as its elements

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
    return lines

def prepare_data(input_list:list):
    """Sanitizes and pre-processes a list

    Takes a list as input. Each of the elements is assumed to be a string.
    Each element is trimmed of leading/trailing spurious characters.
    Each elements is then converted to a list (from string object to list object)
    In the inner lists, each charater is one element of the list.
    Each of inner lists is then added to an aggregation list.
    The format of that aggregation list is a list of lists.
    Returns the aggegation list.

    Args:
        my_list: list

    Returns:
        One list. The elements of the list are lists. The elements of the 
        inner lists are characters.
    """
    # initialize the aggregation list
    list_of_lists = []

    for element in input_list:
        # Sanitize, remove leading and trailing whitespaces
        element_sanitized = element.strip()

        # Convert each element (string) to a list. 
        # Each single character becomes an element of the new inner list
        # The elements of the inner lists are of type string.
        element_as_list = list(element_sanitized)

        # Add the new inner list to the aggregation list
        list_of_lists.append(element_as_list)

    # Finish
    return list_of_lists

def classify_character(input_character:str):
    """Tells if a character is a number, a dot, or a symbol else.

    Symbols are defined as any character that it is not a number or a dot.

    Args:
        input_character: one single character
    
    Returns:
        One string. Either of 'a_number', 'a_dot', or 'a_symbol'
    
    To_do:
        Verify that the input is one single character, no more than one.
        Define the symbols?
    """
    if input_character.isnumeric() == True:
        character_type = "a_number"
    elif input_character == ".":
        character_type = "a_dot"
    else:
        character_type = "a_symbol"
    
    # Finish
    return character_type



def find_numbers_in_line(input_line:list):
    """Finds and returns numbers in a list made of character elements

    Args:
        input_line: list made of character elements

    Returns:
        numbers_in_line, a list made of integer elements
    """
    #print("Testing line:", input_line)
    # Initialize
    number_in_progress = False
    number_instance = ''
    numbers_in_line = []

    # Iterate characters of ths line
    for element_index, element_content in enumerate(input_line):
        # Determine what type of character is
        character_type = classify_character(element_content)
        #print("element with index:", element_index, "has the value:", element_content, "and it is:", character_type)

        match character_type:
            case 'a_number':
                # Always add the number characters to the number in progress
                number_instance = number_instance + str(element_content)
                #print("have added number", str(element_content), "to the number instance, and now looks like", number_instance)

                # Always start a number or continue building one
                number_in_progress = True
                #print("number_in_progress has value:", number_in_progress)  
            case _:
                if number_in_progress == True:
                    # Convert the number_instance, as is at this point, to a integer
                    number_instance = int(number_instance)
                    # Add the number_instance to the list of numbers in the line
                    numbers_in_line.append(number_instance)
                    #print("Have just added number:", number_instance, "to the list of numbers in this line")

                    # reset to initial values
                    number_instance = ''
                    #print("number instance has been reset to:", number_instance)

                # Always end the build of a number
                number_in_progress = False
                #print("number_in_progress has been reset to:", number_in_progress)

    #print("Numbers in the line:", numbers_in_line)
    # Finish
    return numbers_in_line

def find_numbers_in_input(lol:list):
    """
    Args:
        lol: list. List of lists
    
    Returns:
        One list with all the numbers in the input
    """

    # Initialize list of numbers in the whole input
    numbers_in_the_input = []

    # Find all the numbers in the input 
    for line_index, line_content in enumerate(lol):
        # Find numbers in this line
        numbers_in_this_line = find_numbers_in_line(line_content)
        print("in line:", line_index, 
              "have found these numbers:", numbers_in_this_line)
        
        # If this line does have numbers, 
        # add them to the list we are building with all the input numbers 
        if len(numbers_in_this_line) > 0:
            numbers_in_the_input.extend(numbers_in_this_line)
    
    print("numbers found in the input file:", numbers_in_the_input)
    return numbers_in_the_input

def find_parts_in_input(lol:list):
    """
    Args:
        lol: list. List of lists
    
    Returns:
        One list with all the numbers in the input
    """

    # Initialize list of parts in the whole input
    parts_in_the_input = []

    # Find all the numbers in the input 
    for line_index, line_content in enumerate(lol):
        # Find parts in this line
        parts_in_this_line = find_parts_in_line(lol, line_index)
        print("in line:", line_index, 
              "have found these parts:", parts_in_this_line)
        
        # If this line does have parts, 
        # add them to the list we are building with all the input parts 
        if len(parts_in_this_line) > 0:
            parts_in_the_input.extend(parts_in_this_line)
    
    # Finish
    print("parts found in the input file:", parts_in_the_input)
    return parts_in_the_input


def find_points_around_target(target:tuple):
    """Returns all the elements around the input target

    Args:
        target: tuple indentifying the position to scan around. The format is
        (<row_index>, <column_index>)

    Returns:
        points_around_me: list of tuple elements. Each tuple is one point 
        directly in touch with the target. 
        The order is that of reading/writing: from top to bottom and from
        left to right:
          row above the target
          column before the target, column of the target, column after the target
          row of the target
          column after the target
          column before the target, column of the target, column after the target
    """
    # Initialize list of points around the target
    points_around_target = []

    # Taking the target as reference, the points surronding it are those points
    # in the range going from one point behind/above to one point ahead/below
    row_range = [target[0]-1, target[0], target[0]+1]
    column_range = [target[1]-1, target[1], target[1]+1]
    #print(target)
    #print(row_range)
    #print(column_range)
    for row in row_range:
        #print("row:", row)
        for column in column_range:
            #print("position (row, column):", row, column)
            # Add tuple to the list of points around the target
            points_around_target.append((int(row), int(column)))
    
    # Finish
    return points_around_target


def find_parts_in_line(lol:list, line_index:int):
    """Finds and returns parts in a list made of character elements

    Args:
        input_line: list made of character elements

    Returns:
        numbers_in_line, a list made of integer elements
    """
    #print("Testing line:", input_line)
    # Initialize
    number_in_progress = False
    can_be_part = False
    number_instance = ''
    parts_in_line = []

    line_content = lol[line_index]

    # Iterate characters of ths line
    for element_index, element_content in enumerate(line_content):
        # Determine what type of character is
        character_type = classify_character(element_content)
        #print("element with index:", element_index, "has the value:", element_content, "and it is:", character_type)

        match character_type:
            case 'a_number':
                # Always add the number characters to the number in progress
                number_instance = number_instance + str(element_content)
                #print("have added number", str(element_content), "to the number instance, and now looks like", number_instance)

                character_types_around_element = find_character_types_around_target(lol, (line_index, element_index))
                #print(character_types_around_element)
                if 'a_symbol' in character_types_around_element:
                    #print("ALERTA, I found a symbol!!! around number:", element_content)
                    can_be_part = True

                # Always start a number or continue building one
                number_in_progress = True
                #print("number_in_progress has value:", number_in_progress)  
            case _:
                if number_in_progress == True and can_be_part == True:
                    # Convert the number_instance, as is at this point, to a integer
                    number_instance = int(number_instance)
                    # Add the number_instance to the list of parts in the line
                    parts_in_line.append(number_instance)
                    #print("Have just added number:", number_instance, "to the list of parts in this line")

                    # reset to initial values
                    number_instance = ''
                    #print("number instance has been reset to:", number_instance)

                # Always end the build of a number
                number_in_progress = False
                #print("number_in_progress has been reset to:", number_in_progress)
                can_be_part = False
                #print("can_be_part has been reset to:", can_be_part)

    #print("Parts in the line:", parts_in_line)
    # Finish
    return parts_in_line


def find_character_types_around_target(lol:list, target:tuple):
    """
    Args:
        lol: list. List of lists

        target: tuple
    """

    # Identify the target point in the grid
    #print("target is:", target)
    row_index = target[0]
    column_index = target[1]

    # Identify the lenght of the row and column where the target is
    row_lenght = len(lol[row_index])
    column_lenght = len(lol[column_index])
    #print("row lenght is:", row_lenght)
    #print("column lenght is:", column_lenght)
    
    # Select all the points around the target
    target_perimeter = find_points_around_target(target)
    #print("BEFORE, target perimeter is:", target_perimeter)

    # Remove points that are outside bounds, outside the grid
    # Initialize empty list to place the points that are within the grid
    within_bounds = []

    # Probe the points around the target systematically
    for probe in target_perimeter:
        # Identify the probe in the grid
        probe_row_index = probe[0]
        probe_column_index = probe[1]
        
        # If the probe is inside the grid, add it to the list of valid points
        if (probe_row_index >= 0 and 
            probe_column_index >= 0 and
            probe_row_index <= row_lenght-1 and
            probe_column_index <= column_lenght-1
            ):
            within_bounds.append(probe)
    #print("AFTER, whitin bounds is:", within_bounds)


    # Now we will go through the points around the target, that are 
    # within the grid, retrieve the value, inspect what type of character
    # is that value, and add that character type to a list specific for 
    # that particular target

    # Initialize empty list to place the character types that we find
    # around the target
    character_types_around_target = []

    # Retrieve the character types around the probe systematically
    # and put them in a list
    for probe in within_bounds:
        # Identify the probe in the grid
        probe_row_index = probe[0]
        probe_column_index = probe[1]

        # Retrieve the value in the probe
        #probe_value = lol[probe_row_index][probe_column_index]
        # TEST
        probe_value = retrieve_value_of_target(lol, probe)
        #print("in probe:", probe, "I find this value", probe_value)

        # Verify what type of character is that value
        # and add it to the list specific for the target
        character_type = classify_character(probe_value)
        #print(character_type)
        character_types_around_target.append(character_type)

    # Finish
    return character_types_around_target

def retrieve_value_of_target(lol:list, target:tuple):
    """Retrieves the value of a grid point
    Args:
        lol: list

        target: tuple

    Returns:
        element_value: str. Value found in the grid point
    """
    # Identify the target point in the grid
    #print("target is:", target)
    target_row_index = target[0]
    target_column_index = target[1]

    # Retrieve the value in the probe
    target_value = lol[target_row_index][target_column_index]

    # Finish
    return target_value

def main():
    """Whole logic

    Pulls and glues all the other elements of the module.
    """

    # Open input file
    input_list = file_open("input_example_day03_part1.txt")
    input_list = file_open("input_day03.txt")

    # Pre-process input file
    lol = prepare_data(input_list)

    # Report of the input data
    print("Summary of the input data:")
    print("The input data is of type:", type(lol), "and has", len(lol), "lines")
    print("Each line is of type:", type(lol[0]), "and has:", len(lol[0]), "characters")

    parts_in_input = find_parts_in_input(lol)
    print("SANDBOX, PARTS IN INPUT:", parts_in_input)
    sum_of_parts_in_input = sum(parts_in_input)
    print("sum of parts in the input is:", sum_of_parts_in_input)
    


def sandbox():
    # Open input file
    input_list = file_open("input_example_day03_part1.txt")
    #input_list = file_open("input_day03.txt")

    # Pre-process input file
    lol = prepare_data(input_list)

    sample_target = (1,1)   # .
    sample_target = (0,1)   # 6
    sample_target = (0,0)   #
    #sample_target = (9,9)   # 
    character_types_around_target = find_character_types_around_target(lol, sample_target)
    #print("SANDBOX: symbols_around_target", sample_target, "are:", symbols_around_target)
    #print("character types around", sample_target, "are:", character_types_around_target)

    sample_row = lol[1]
    for column_index, column_value in enumerate(sample_row):
        coordinates = (1, column_index)
        value_retrieved = retrieve_value_of_target(lol, coordinates)
        #print("coordinates:", coordinates, "value, native:", column_value, "value, retrieved", value_retrieved)

        # retrieve_value_of_target(lol:list, target:tuple):
        #character_types_around_element = find_character_types_around_target(lol, element)
        #print(character_types_around_element)

    sample_line = lol[0]
    numbers_in_sample_line = find_numbers_in_line(sample_line)
    #print("numbers is line:", numbers_in_sample_line)
    #parts_in_sample_line = find_parts_in_line(sample_line)
    #print("parts is line:", parts_in_sample_line)

    ### parts
    sample_line_index = 0
    sample_line_index = 1
    sample_line_index = 2
    sample_line_index = 3
    sample_line_index = 4
    sample_line_index = 5
    sample_line_index = 6
    sample_line_index = 7
    parts_in_sample_line = find_parts_in_line(lol, sample_line_index)
    print("parts in sample line with index:", sample_line_index, "are:", parts_in_sample_line)

    parts_in_input = find_parts_in_input(lol)
    print("SANDBOX, PARTS IN INPUT:", parts_in_input)
    sum_of_parts_in_input = sum(parts_in_input)
    print("sum of parts in the input is:", sum_of_parts_in_input)

# Execute this function when the file is invoked from the CLI
main()

#sandbox()

# at 19:03 answer is too high, 924575583163