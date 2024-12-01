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
    print("FILE OPEN")
    print("type is:", type(lines), "lenght is:", len(lines), "content is:", lines)
    print("\n")
    
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
        # At this point the elements are of type string
        line = line.split(" ")
        # Convert from string to list, 
        # and remove leading/trailing characters
        # and convert the elements to integers
        line = [int(entry.strip()) for entry in line]
        lines_processed.append(line)

    # Verify
    print("PREPARE INPUT")
    for line in lines_processed:
        print("type is:", type(line), "content is:", line)
    print("\n")

    # Finish
    return lines_processed

def history_sequences(history:list) -> list:
    """Takes a list and returns a list of lists with its sequences

    Args:
        history: list of integers
    
    Return:
        history_sequences: list of lists
    """
    history_sequences = [history]
    sequence = history

    while sum(sequence) != 0:
        # populate a sequence
        new_sequence = []
        for  i in range(len(sequence)-1):
            new_sequence_element = sequence[i+1] - sequence[i]
            new_sequence.append(new_sequence_element)

        # Verify
        #print("HISTORY SEQUENCES")
        #print("previuos sequence:", sequence)
        #print("new sequence:", new_sequence)
        #print("lenght previous sequence:", len(sequence), 
        #      "lenght this sequence:", len(new_sequence),
        #      "difference should be 1 and it is:", len(sequence)-len(new_sequence))

        # Append the new sequence to the list of sequences
        history_sequences.append(new_sequence)
        # Prepare for the new interation
        sequence = new_sequence
    
    # Verify
    print("HISTORY SEQUENCES, for history:", history, "its sequences are:", history_sequences)
    #print("\n")

    # Finish
    return history_sequences

def extrapolate_history2(history_sequences:list) -> int:
    """Takes a history sequences, and returns the history extrapolated next value

    Args:
        history_sequences: list

    Return:
        history_extrapolated_next_value: int
    """
    # Initialize extrapolated sequence value 
    a = 0

    # For each sequence of the input history, calculate its extrapolated sequence value
    for sequence in reversed(history_sequences):
        #last_sequence_element = sequence[-1]
        first_sequence_element = sequence[0]
        #a = a + last_sequence_element
        a = first_sequence_element - a
        # Verify
        print("EXTRAPOLATED HISTORY, for sequence", sequence, "its extrapolated value is:", a)

    # Finish
    # Verify
    print("EXTRAPOLATED HISTORY, for history", history_sequences[0], "its extrapolated value is:", a)
    return a

def sandbox():
    # Open input file
    #histories = file_open("input_part1_example1.txt")
    histories = file_open("puzzle.txt")
    histories = file_open("puzzle.txt")

    # Prepare the data
    histories = prepare_input(histories)

    # Test
    extrapolated_history_values_sum = 0
    for history in histories:
        sequences = history_sequences(history)
        history_extrapolated_next_value = extrapolate_history2(sequences)
        extrapolated_history_values_sum = extrapolated_history_values_sum + history_extrapolated_next_value
        print("SANDBOX, extrapolated history value is", history_extrapolated_next_value)
        print("\n")
        # Verify
        #print("for history:", history)
        #print("its sequences are:", sequences)
        #print("\n")
    
    print("SANDBOX, sum of all the extrapolated history values is:", extrapolated_history_values_sum)


# Execute this function automatically when the file is invoked from the CLI
print("\n")
sandbox()