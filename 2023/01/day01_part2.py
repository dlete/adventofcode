# https://adventofcode.com/2023/day/1
#

#--- Part Two ---
#Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
#
#Equipped with this new information, you now need to find the real first and last digit on each line. For example:
#
#two1nine
#eightwothree
#abcone2threexyz
#xtwone3four
#4nineeightseven2
#zoneight234
#7pqrstsixteen
#In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
#
#What is the sum of all of the calibration values?
#
#Answer: 53340


digits_as_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits_as_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Open file
# https://realpython.com/read-write-files-python/#tips-and-tricks
#with open("input_example_part2.txt", "r") as file:
with open("input_day01.txt", "r") as file:
    sum_of_calibration_values = 0
    for line in file:
        lowest_index = 200
        #highest_index = 0
        # if it is not lower than 0, it may be that the previos values interfere with subsequents
        highest_index = -1
        print(line, end='')
        for digit in digits_as_words:
            # https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/
            match digit:
                case 'one':
                    digit_numerical = '1'
                case 'two':
                    digit_numerical = '2'
                case 'three':
                    digit_numerical = '3'
                case 'four':
                    digit_numerical = '4'
                case 'five':
                    digit_numerical = '5'
                case 'six':
                    digit_numerical = '6'
                case 'seven':
                    digit_numerical = '7'
                case 'eight':
                    digit_numerical = '8'
                case 'nine':
                    digit_numerical = '9'

            # https://builtin.com/software-engineering-perspectives/python-substring-indexof
            try:
                # indexing starts in 0
                lowest_index_of_the_pattern = line.index(digit)
                highest_index_of_the_pattern = line.rindex(digit)
                #print("lowest index of the pattern", digit, "is:", lowest_index_of_the_pattern)
                #print("highest index of the pattern", digit, "is:", highest_index_of_the_pattern)
                if lowest_index_of_the_pattern < lowest_index:
                    lowest_index = lowest_index_of_the_pattern
                    first_digit = digit_numerical
                if highest_index_of_the_pattern > highest_index:
                    highest_index = highest_index_of_the_pattern
                    last_digit = digit_numerical
            except:
                pass

        for digit in digits_as_numbers:
            try:
                # indexing starts in 0
                lowest_index_of_the_pattern = line.index(digit)
                highest_index_of_the_pattern = line.rindex(digit)
                #print("lowest index of the pattern", digit, "is:", lowest_index_of_the_pattern)
                #print("highest index of the pattern", digit, "is:", highest_index_of_the_pattern)
                if lowest_index_of_the_pattern < lowest_index:
                    lowest_index = lowest_index_of_the_pattern
                    first_digit = digit
                if highest_index_of_the_pattern > highest_index:
                    highest_index = highest_index_of_the_pattern
                    last_digit = digit
            except:
                pass


        print("lowest index is:", lowest_index, "and the lowest digit is:", first_digit)
        print("highest index is", highest_index, "and the highest digit is:", last_digit)

        # combine first and last digit
        calibration_value = int(str(first_digit) + str(last_digit))
        print("combined digit is:", calibration_value)
        #print("type of combined digit is:", type(calibration_value))
        print("\n")
        sum_of_calibration_values = sum_of_calibration_values + calibration_value
    print("sum of all the calibration values is:", sum_of_calibration_values)