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
    # Finish
    return lines


def prepare_and_process_data(input_list:list):
    """Prepares the input data and returns it formated and sanitized

    Args:
        input_list: list

    Returns:
        One integer. The aggregate number of points of all the cards
    """
    for hand_index, hand_content in enumerate(input_list):
        #print("processing row number", row_index)
        #print("initial state of row number", row_index, "has content:", row_content)

        # remove leading/trailing characters
        #elment_content = element_content.strip()

        # Split row into hand_cards and hand_bid
        hand_cards, hand_bid = hand_content.split()
        # Sanitize, strip leading/trailing characters
        hand_cards = hand_cards.strip()
        hand_bid = hand_bid.strip()
        # Conver the bid to integers
        hand_bid = int(hand_bid)

        # Put all the properties of a hand in a list
        hand = [hand_index, hand_cards, hand_bid]

        # Verify (could be done with an "assert" command)
        #print("index:", hand[0], type(hand[0]),
        #      "cards:", hand[1], type(hand[1]), 
        #      "bid:", hand[2], type(hand[2]))

        # Replace the raw input_list with the processed data
        input_list[hand_index] = hand
    
    # Finish
    return (input_list)


def classify_hand(hand:list):
    # Cards in the hand
    hand_cards = hand[1]

    # Labels, unique figures in the hand
    hand_labels = set(hand_cards)
    #print("hand_unique_characters:", hand_labels)
    # How many labels/unique figures there are
    number_of_labels_in_hand = len(hand_labels)

    # Dictionary, the labels are the keys, the number label occurrences are the values
    label_repetitions = {label: hand_cards.count(label) for label in hand_labels}
    #print(label_repetitions)
    # What is the maximum number of repetitions
    maximum_number_of_label_repetitions = max(label_repetitions.values())
    #print("maximum_number_of_repetitions:", maximum_number_of_label_repetitions)

    # Logic
    if number_of_labels_in_hand == 1:
        # Five of a kind, all five cards have the same label: AAAAA
        hand_type = "five_of_a_kind"
    elif number_of_labels_in_hand == 2:
        # Two labels need further digging
        if maximum_number_of_label_repetitions == 4:
            # Four of a kind, four cards have the same label and one card has a different label: AA8AA
            hand_type = "four_of_a_kind"
        elif maximum_number_of_label_repetitions == 3:
            # Full house, three cards have the same label, and the remaining two cards share a different label: 23332
            hand_type = "full_house"
        else:
            raise Exception("I do not know what type of hand is this:", hand)
    elif number_of_labels_in_hand == 3:
        # Three labels need further digging
        if maximum_number_of_label_repetitions == 3:
            # Three of a kind, three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
            hand_type = "three_of_a_kind"
        elif maximum_number_of_label_repetitions == 2:
            # Two pair, two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
            hand_type = "two_pair"
        else:
            raise Exception("I do not know what type of hand is this:", hand)
    elif number_of_labels_in_hand == 4:
        # One pair, two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        hand_type = "one_pair"
    elif number_of_labels_in_hand == 5:
        # High card, all cards' labels are distinct: 23456
        hand_type = "high_card"
    else:
        raise Exception("Could not classify these cards:", hand_cards)

    #print("CLASSIFY HAND:",
    #      "hand:", hand,
    #      "hand cards:", hand_cards,
    #      "hand labels:", hand_labels,
    #      "number of labels in hand:", number_of_labels_in_hand,
    #      "maximum_number_of_label_repetitions:", maximum_number_of_label_repetitions,
    #      "hand type is:", hand_type)
    return hand_type



def add_auxiliary(hands_set):
    for hand in hands_set:
        #hand_auxiliary_cards = hand[1].replace('J', 'R')
        hand_cards = hand[1]
        hand_auxiliary_cards = hand_cards
        hand_auxiliary_cards = hand_auxiliary_cards.replace('A', 'Z')
        hand_auxiliary_cards = hand_auxiliary_cards.replace('A', 'Z')
        hand_auxiliary_cards = hand_auxiliary_cards.replace('K', 'Y')
        hand_auxiliary_cards = hand_auxiliary_cards.replace('Q', 'X')
        hand_auxiliary_cards = hand_auxiliary_cards.replace('J', 'W')
        hand_auxiliary_cards = hand_auxiliary_cards.replace('T', 'V')
        hand.append(hand_auxiliary_cards)
    return hands_set


def add_classification(hands_set):
    for hand in hands_set:
        hand_type = classify_hand(hand)
        hand.append(hand_type)
    return hands_set


def bundle_hands(hands_set:list):
    hands_five_of_a_kind = []
    hands_four_of_a_kind = []
    hands_full_house = []
    hands_three_of_a_kind = []
    hands_two_pair = []
    hands_one_pair = []
    hands_high_card = []

    for hand in hands_set:
        hand_type = hand[3]
        match hand_type:
            case 'five_of_a_kind':
                hands_five_of_a_kind.append(hand)
            case 'four_of_a_kind':
                hands_four_of_a_kind.append(hand)
            case 'full_house':
                hands_full_house.append(hand)
            case 'three_of_a_kind':
                hands_three_of_a_kind.append(hand)
            case 'two_pair':
                hands_two_pair.append(hand)
            case 'one_pair':
                hands_one_pair.append(hand)
            case 'high_card':
                hands_high_card.append(hand)
            case _:
                raise Exception("BUNDLE HANDS: These hand cards do not have a hand type:", hand[1])

    lol = [hands_five_of_a_kind,
           hands_four_of_a_kind,
           hands_full_house,
           hands_three_of_a_kind,
           hands_two_pair,
           hands_one_pair,
           hands_high_card
    ]
    
    # Finish
    return lol


def extract_auxiliaries(bundle:list):
    """Finds auxiliary cards in a bundle, orders them and puts them in a list
    """
    list_of_auxiliaires = []
    for hand in bundle:
        #print("EXTRACT AUXILIARIES, hand:", hand)
        auxiliary_cards = hand[4]
        list_of_auxiliaires.append(auxiliary_cards)
    
    list_of_auxiliaires = sorted(list_of_auxiliaires, reverse=False)

    #print("EXTRACT AUXILIARIES, list of auxiliaries:", list_of_auxiliaires)
    return list_of_auxiliaires

def add_bundle_rank(card_bundles:list):
    for card_bundle_index, card_bundle_content in enumerate(card_bundles):
        for hand in card_bundle_content:
            hand.append(card_bundle_index)
    return card_bundles

def add_hand_rank_in_bundle(bundle:list):
    """Adds rank to the hands of a bundle
    """
    bundle_auxiliaries = extract_auxiliaries(bundle)
    bundle_auxiliaries = sorted(bundle_auxiliaries, reverse=True)

    number_of_elements_in_bundle = len(bundle)
    for auxiliary_index, auxiliary_cards in enumerate(bundle_auxiliaries):
        #print("looking for match for:", auxiliary_cards)
        for hand in bundle:
            if auxiliary_cards in hand:
                #print("found", auxiliary_cards, "in hand", hand)
                bundle_rank = auxiliary_index + 1
                hand.append(bundle_rank)
                #print("hand after appending rank in bundle:", hand)
    return bundle

def add_total_rank(hands_set:list):
    for hand_index, hand_content in enumerate(hands_set):
        total_rank = hand_index + 1
        hand_content.append(total_rank)
    return hands_set



def main():
    # Open input file
    hands_set = file_open("day07_input.txt")

    # Prepare data, process the data and compute the total number of points
    hands_set = prepare_and_process_data(hands_set)

    # Classify the hands and append their classification to their list of properties
    #hand_set = [hand.append(classify_hand(hand)) for hand in hands_set]
    hands_set = add_classification(hands_set)
    # Verify the hands have been classified
    #for hand in hands_set:
    #    print(hand)
    # Format of hand
    # [row_index, hand_cards, hand_bid, hand_type]

    # Add auxiliary cards
    hands_set = add_auxiliary(hands_set)
    #for hand in hands_set:
    #    print(hand)
    # Format of hand
    # [row_index, hand_cards, hand_bid, hand_type, hand_auxiliary_cards]

    # Bundle the cards into their types
    # this is a list of lists
    card_bundles = bundle_hands(hands_set)
    #for card_bundle in card_bundles:
    #    print("card_bundle:", card_bundle)

    card_bundles = add_bundle_rank(card_bundles)

    # Create a list with the auxiliary
    # Order the auxiliar
    # Add a rank
    for card_bundle in card_bundles:
        #bundle_auxiliaries = extract_auxiliaries(card_bundle)
        #print("bundle:", card_bundle)
        #print("bundle lenght:", len(card_bundle))
        #print("bundle auxiliaires:", bundle_auxiliaries)
        #print("\n")
        add_hand_rank_in_bundle(card_bundle)
    # Verify
    #for card_bundle in card_bundles:
    #    for hand in card_bundle:
    #        print("hand:", hand)

    # Put all the bundles together
    hands_set = []
    for card_bundle in card_bundles:
        for hand in card_bundle:
            hands_set.append(hand)
    # Verify
    #for hand in hands_set:
    #    print("hand", hand)

    # Order
    from operator import itemgetter
    hands_set = sorted(hands_set, key=itemgetter(5, 6), reverse=True)
    # Verify
    #for hand in hands_set:
    #    print("hand", hand)

    # Add total rank
    hands_set = add_total_rank(hands_set)
    # Verify
    for hand in hands_set:
        print("hand", hand)

    # Calculate total winnings
    total_winnings = 0
    for hand in hands_set:
        hand_winnings = hand[2] * hand[-1]
        #print("hand winnings", hand[2], "*", hand[-1], "is:", hand_winnings)
        total_winnings = total_winnings + hand_winnings
    print("total winnings:", total_winnings)


def sandbox():
    # Open input file
    hands_set = file_open("day07_input_part1_example.txt")

    # Prepare data, process the data and compute the total number of points
    hands_set = prepare_and_process_data(hands_set)

    # Classify the hands and append their classification to their list of properties
    #hand_set = [hand.append(classify_hand(hand)) for hand in hands_set]
    hands_set = add_classification(hands_set)
    # Verify the hands have been classified
    #for hand in hands_set:
    #    print(hand)
    # Format of hand
    # [row_index, hand_cards, hand_bid, hand_type]

    # Add auxiliary cards
    hands_set = add_auxiliary(hands_set)
    for hand in hands_set:
        print(hand)
    # Format of hand
    # [row_index, hand_cards, hand_bid, hand_type, hand_auxiliary_cards]

    # Bundle the cards into their types
    # this is a list of lists
    card_bundles = bundle_hands(hands_set)
    #for card_bundle in card_bundles:
    #    print("card_bundle:", card_bundle)

    card_bundles = add_bundle_rank(card_bundles)

    # Create a list with the auxiliary
    # Order the auxiliar
    # Add a rank
    for card_bundle in card_bundles:
        #bundle_auxiliaries = extract_auxiliaries(card_bundle)
        #print("bundle:", card_bundle)
        #print("bundle lenght:", len(card_bundle))
        #print("bundle auxiliaires:", bundle_auxiliaries)
        #print("\n")
        add_hand_rank_in_bundle(card_bundle)
    # Verify
    #for card_bundle in card_bundles:
    #    for hand in card_bundle:
    #        print("hand:", hand)

    # Put all the bundles together
    hands_set = []
    for card_bundle in card_bundles:
        for hand in card_bundle:
            hands_set.append(hand)
    # Verify
    #for hand in hands_set:
    #    print("hand", hand)

    # Order
    from operator import itemgetter
    hands_set = sorted(hands_set, key=itemgetter(5, 6), reverse=True)
    # Verify
    #for hand in hands_set:
    #    print("hand", hand)

    # Add total rank
    hands_set = add_total_rank(hands_set)
    # Verify
    for hand in hands_set:
        print("hand", hand)

    # Calculate total winnings
    total_winnings = 0
    for hand in hands_set:
        hand_winnings = hand[2] * hand[-1]
        #print("hand winnings", hand[2], "*", hand[-1], "is:", hand_winnings)
        total_winnings = total_winnings + hand_winnings
    print("total winnings:", total_winnings)


# Execute this function automatically when the file is invoked from the CLI
main()
print("\n")
sandbox()