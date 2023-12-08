
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


def prepare_and_process_data(input_list:list):
    """Prepares the input data, computes and returns the total number of points

    Args:
        my_list: list

    Returns:
        One integer. The aggregate number of points of all the cards
    """
    # initialize the aggregation list
    list_of_lists = []

    total_points = 0
    for element in input_list:
        # Split on "|"
        element_left, card_playing_numbers = element.split(" | ")
        # Split on ": "
        card_header, card_winning_numbers = element_left.split(": ")

        # Sanitize, remove leading and trailing whitespaces
        card_header = card_header.strip()
        card_winning_numbers = card_winning_numbers.strip()
        card_playing_numbers = card_playing_numbers.strip()

        # Convert string of numbers to lists
        card_playing_numbers = card_playing_numbers.split()
        card_winning_numbers = card_winning_numbers.split()

        # Find the winner numbers in the playing numbers
        card_prize_numbers = set(card_playing_numbers).intersection(card_winning_numbers)

        # Convert set to list
        card_prize_numbers = list(card_prize_numbers)

        # Convert lists of strings to lists of numbers
        card_winning_numbers = [int(i) for i in card_winning_numbers]
        card_playing_numbers = [int(i) for i in card_playing_numbers]
        card_prize_numbers = [int(i) for i in card_prize_numbers]


        # COMPUTE SUMS
        # Does the card have any price points?
        number_of_price_numbers_in_card = len(card_prize_numbers)
        #print("number_of_price_numbers_in_card:", number_of_price_numbers_in_card)

        if number_of_price_numbers_in_card > 0:
            # The card has some price points
            multiplier = 1
            card_points = 1
            for price_number_index, price_number_value in enumerate(range(number_of_price_numbers_in_card)):
                card_points = card_points * multiplier
                multiplier = 2
                #print("price_number_index:", price_number_index, "price_number_value:", price_number_value)
                #print("card_points:", card_points)
        else:
            # No price points
            card_points = 0
        
        # Report
        #print("card_header", card_header)
        #print("card winning numbers", card_winning_numbers)
        #print("card playing numbers", card_playing_numbers)
        #print("card prize numbers", card_prize_numbers)
        #print("card poins:", card_points)
        #print("\n")

        # Add the individual card points to the overall score
        total_points = total_points + card_points

    # Finish
    #print("total_points:", total_points)
    return total_points

def main():
    # Open input file
    input_list = file_open("input_example_day04_part1.txt")
    #input_list = file_open("input_day04.txt")

    # Prepare data
    lol = prepare_and_process_data(input_list)

def sandbox():
    # Open input file
    #input_list = file_open("input_example_day04_part1.txt")
    input_list = file_open("input_day04.txt")

    # Prepare data, process the data and compute the total number of points
    total_number_of_points = prepare_and_process_data(input_list)

    print("total_number_of_points:", total_number_of_points)


# Execute this function when the file is invoked from the CLI
#main()
sandbox()

# 09:12, 28848, too high