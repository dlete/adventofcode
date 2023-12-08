
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
    # Initialize list to stack repetitions for next cards
    maximum_number_of_prizes = 10
    staked_repetitions = [0 for i in range(maximum_number_of_prizes)]
    #print("staked_repetitions:", staked_repetitions)
    #print("lenght of stacked repetitions:", len(staked_repetitions))

    # Start with one copy of each card, index 0 will be the card being processed
    copies_of_cards = [1 for i in range(maximum_number_of_prizes + 1)]
    print("initialized copies_of_cards:", copies_of_cards)

    total_points = 0
    total_points_part1 = 0
    total_points_part2 = 0
    total_scratchards_part2 = 0
    for line_index, line_content in enumerate(input_list):
        # Set variable
        card_index = line_index+1

        # Split on "|"
        card_left, card_playing_numbers = line_content.split(" | ")
        # Split on ": "
        card_header, card_winning_numbers = card_left.split(": ")

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


        # COMPUTE PRIZES IN CARD
        # Does the card have any price points?
        number_of_price_numbers_in_card = len(card_prize_numbers)
        #print("number_of_price_numbers_in_card:", number_of_price_numbers_in_card)

        if number_of_price_numbers_in_card > 0:
            # The card has some price points

            # Initialize the first value
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
        total_points_part1 = total_points_part1 + card_points
        ### END OF PART 1 ###

        ### BEGIN OF PART 2 ###
        #card_points_part2 = copies_of_cards[0] + card_points

        # PREPARE THE NEXTS, THE FOLLOWING COPIES
        print("\n")
        print("Card:", card_index)
        print("copies_of_cards as encountered by card:", card_index, "before doing anything related to part2 is:", copies_of_cards)
        number_of_card_copies_part2 = copies_of_cards[0]
        print("number of copies of card", card_index, "is:", number_of_card_copies_part2)
        print("number_of_price_numbers_in_card:", card_index, "is:", number_of_price_numbers_in_card)
        print("card points part1:", card_points)

        # ADD COPIES TO NEXT CARDS
        for i in range(number_of_price_numbers_in_card):
            # COULD GIVE TROUBLE WHEN THERE ARE 10 PRICES!!!! MAKE THE LIST OF COPIES ONE ELEMENT LONGER
            #copies_of_cards[i+1] = copies_of_cards[i+1] + 1
            # Add as many copies as there are copies of this card (which is the first element of the list)
            copies_of_cards[i+1] = copies_of_cards[i+1] + copies_of_cards[0]
        print("list of card copies after adding card points of card:", card_index, "is:", copies_of_cards)
        
        # CALCULATE THE POINTS OF THIS CARD ACCORING TO THE PART2 RULES
        card_points_part2 = card_points * copies_of_cards[0]
        print("card_points_part2 for card:", card_index, "is:", card_points_part2)
        
        # Already have the points2 for this card -> reset the list of copies for this card
        # I do not think there is need, but in case
        copies_of_cards[0] = 0
        print("copies_of_cards after reseting the first element:", copies_of_cards)

        # SHIFT THE CARD COPIES LIST
        for i in range(len(copies_of_cards)-1):
            copies_of_cards[i] = copies_of_cards[i+1]
        # set the last element to zero
        copies_of_cards[-1] = 0
        print("copies_of_cards after shifting them one step up:", copies_of_cards)
        print("This is the state we hand the copies_of_cards to the next card")

        # Add the individual card points to the overall score
        total_points_part2 = total_points_part2 + card_points_part2
        total_scratchards_part2 = total_scratchards_part2 + number_of_card_copies_part2

    # Finish
    # part1 sample: 13
    # part1 exercise: 24848
    print("total_points_part1:", total_points_part1)
    print("total_points_part2:", total_points_part2)
    print("total number of scratchcards part2:", total_scratchards_part2)
    return (total_points_part1, total_scratchards_part2)



def main():
    # Open input file
    #input_list = file_open("input_example_day04_part1.txt")
    input_list = file_open("input_day04.txt")

    # Prepare data, process the data and compute the total number of points
    total_number_of_points_part1 = prepare_and_process_data(input_list)[0]
    total_number_of_scratchcards_part2 = prepare_and_process_data(input_list)[1]
    print("part 1: total number of poitns:", total_number_of_points_part1)
    print("part 2: total number of scratchcards:", total_number_of_scratchcards_part2)

def sandbox():
    # Open input file
    input_list = file_open("input_example_day04_part1.txt")
    #input_list = file_open("input_day04.txt")

    # Prepare data, process the data and compute the total number of points
    total_number_of_points_part1 = prepare_and_process_data(input_list)[0]
    total_number_of_scratchcards_part2 = prepare_and_process_data(input_list)[1]
    print("part 1: total number of points:", total_number_of_points_part1)
    print("part 2: total number of scratchcards:", total_number_of_scratchcards_part2)


# Execute this function when the file is invoked from the CLI
#main()
sandbox()

# Part 1
# 09:12, 28848, too high
#
# Part 2
# 16:50, 46159, too low
# 21:45 1998173, too low