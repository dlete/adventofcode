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
    for row_index, row_content in enumerate(input_list):
        #print("processing row number", row_index)
        #print("initial state of row number", row_index, "has content:", row_content)

        # remove leading/trailing characters
        #elment_content = element_content.strip()

        # Split row into header and content, split on ":"
        row_header, row_content = row_content.split(":")

        # Sanitise
        row_header = row_header.strip()
        row_content = row_content.strip()
        #print("row header:", row_header)
        #print("row content:", row_content)
        
        # Extract the values from the content, sanitize, and convert them to integers
        # When the str.split() method is called without an argument, it considers 
        # consecutive whitespace characters as a single separator.
        row_values = row_content.split()
        row_values = [int(value) for value in row_values]
        #print("row values:", row_values)
        # print("verify the values are of type integer")
        # [print(type(value)) for value in row_values]
        #print("\n")

        ########## PART2 ##########
        # Initialize empty string
        row_value_part2 = ''

        # Convert each value to string and then concatenate the strings
        for entry in row_values:
            # Convert to string
            entry = str(entry)
            # Concatenate
            row_value_part2 = row_value_part2 + entry
           # print("row_value_part2", row_value_part2, "of type:", type(row_value_part2))
        
        # Convert back to integer
        row_value_part2 = int(row_value_part2)
        # Add to a list that will be returned
        row_values_part2 = [row_value_part2]
        ########## PART2 ##########

        # rebuild the input list with the processed data
        # Part 1
        #input_list[row_index] = row_values
        # Part 2
        input_list[row_index] = row_values_part2

    races_times = input_list[0]
    races_record_distances = input_list[1]
    #print("races times:", races_times)
    #print("races distances:", races_distances)
    
    # Finish
    return (races_times, races_record_distances)


def my_computation(races_times:list, races_distances:list):
    # Initialize result
    successful_attempts_per_race = []

    # How many races we have as input
    number_of_races = len(races_times)

    # Go race by race and calculate all the combinations of 
    # release times/release speeds/attempt distance for each race
    for race_index in range(number_of_races):
        #print("race number:", race_index+1, "has race index:", race_index)
        race_time = races_times[race_index]
        race_distance_record = races_distances[race_index]
        #print("race number:", race_index+1)
        #print("race time:", race_time, "race distance_record:", race_distance_record)

        # Calculate distances for each release time
        release_times = [t+1 for t in range(race_time)]
        release_speeds = release_times
        number_of_release_times = len(release_times)
        #print("release times:", release_times)
        #print("release speeds:", release_speeds)
        #print("the possible number of release times is:", number_of_release_times)

        # Initialize list to hold the 
        successful_attempts = []

        # Compute all the possible attempts for this race
        for release_time in release_times:
            release_speed = release_time
            moving_time = release_times[-1] - release_time
            distance_attempt = moving_time * release_speed
            if distance_attempt > race_distance_record:
                successful_attempts.append(distance_attempt)
            
            #print("releasing at time", release_time, 
            #      "releases with speed:", release_time,
            #      "allows to race for time:", moving_time,
            #      "reaches distance:", distance_attempt)
        
        number_of_successful_attempts_in_this_race = len(successful_attempts)
        successful_attempts_per_race.append(number_of_successful_attempts_in_this_race)
    
    result_part_1 = 1
    for race_index in range(number_of_races):
        #print("race_index:", race_index)
        #print(successful_attempts_per_race[race_index])
        result_part_1 = result_part_1 * successful_attempts_per_race[race_index]
        #print("\n")

    return result_part_1



def main():
    # Open input file
    input_list = file_open("input_day06.txt")
    #input_list = file_open("input_example_day06_part1.txt")

    # Prepare data, process the data and compute the total number of points
    prepared_data = prepare_and_process_data(input_list)
    races_times = prepared_data[0]
    races_distances = prepared_data[1]

    # Report on the data we will be working with
    print("MAIN, races times:", races_times)
    print("MAIN, races distances:", races_distances)

    # Compute
    result_part2 = my_computation(races_times, races_distances)
    print("MAIN: result of part1 is:", result_part2)

def sandbox():
    # Open input file
    input_list = file_open("input_example_day06_part1.txt")
    #input_list = file_open("input_day06.txt")
    #print("input data, raw:", input_list)
    #print("number of elements in the input data:", len(input_list))
    #print("first element:", input_list[0])
    #print("second element:", input_list[1])

    # Prepare data, process the data and compute the total number of points
    prepared_data = prepare_and_process_data(input_list)

    # Report on the data we will be working with
    races_times = prepared_data[0]
    races_record_distances = prepared_data[1]
    print("SANDBOX, races times:", races_times)
    print("SANDBOX, races record distances:", races_record_distances)

    # Verify
    #print("verify the values are integers")
    #for value in races_times:
    #    print(type(value))

    # Compute
    result_part2 = my_computation(races_times, races_record_distances)
    print("SANDBOX: result of part2 is:", result_part2)

# Execute this function automatically when the file is invoked from the CLI
sandbox()
print("\n")
main()