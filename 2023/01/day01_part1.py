# https://adventofcode.com/2023/day/1
#
#--- Day 1: Trebuchet?! ---
#Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.
#
#You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.
#
#Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
#
#You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").
#
#As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.
#
#The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
#
#For example:
#
#1abc2
#pqr3stu8vwx
#a1b2c3d4e5f
#treb7uchet
#In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
#
#Consider your entire calibration document. What is the sum of all of the calibration values?
#
#Your puzzle answer was 52974.
#
#The first half of this puzzle is complete! It provides one gold star: *



# Open file
# https://realpython.com/read-write-files-python/#tips-and-tricks
#with open("input_example_part1.txt", "r") as file:
with open("input_day01.txt", "r") as file:
    sum_of_calibration_values = 0
    for line in file:
        print(line)
        # what type of object is "line"
        #print(type(line))   # string
        for character in line:
            #print(character)
            if character.isdigit():
                first_digit = character
                # https://learnpython.com/blog/end-loop-python/
                # https://wiki.python.org/moin/ForLoop
                break
        print("first digit is:", first_digit)

        # https://realpython.com/reverse-string-python/
        #reversed_line = reversed(line)
        reversed_line = line[::-1]
        #print(reversed_line)
        for character in reversed_line:
            if character.isdigit():
                last_digit = character
                break
        print("last digit is:", last_digit)

        # combine first and last digit
        calibration_value = int(str(first_digit) + str(last_digit))
        print("combined digit is:", calibration_value)
        print("type of combined digit is:", type(calibration_value))
        sum_of_calibration_values = sum_of_calibration_values + calibration_value
    print("sum of all the calibration values is:", sum_of_calibration_values)

