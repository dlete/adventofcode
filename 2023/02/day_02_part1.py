#--- Day 2: Cube Conundrum ---
#You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.
#
#The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?
#
#As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.
#
#To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.
#
#You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).
#
#For example, the record of a few games might look like this:
#
#Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
#Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
#Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
#Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
#In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.
#
#The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
#
#In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.
#
#Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
#
#Your puzzle answer was 2085.
#
#The first half of this puzzle is complete! It provides one gold star: *



# Open intput file, create a list with element being one of the lines
# https://realpython.com/read-write-files-python/#tips-and-tricks
#with open("input_example_part1_game1.txt", "r") as file:
#with open("input_example_part1_game4.txt", "r") as file:
#with open("input_example_part1.txt", "r") as file:
with open("input_day02.txt", "r") as file:
    # read the lines from the file object and return them as a list
    games = file.readlines()
    # print(type(lines))    # this is a list


# practice line, valid
#pl_v = games[0]
#pl_i = games[2]
#print("This is a sample of a possible game")
#print(pl_v)
#print("This is a sample of an impossible game")
#print(pl_i)

#####################################################################
# SPLIT LINE
# Observe that each line has the format <ID : results>
# That means we can use the character ":" to separate the line in two
# game_parts is a list. The first element is the game id, the second the game results
#game_parts = pl_v.split(sep=': ')
#game_header = game_parts[0]
#game_content = game_parts[1]
#print("game_header is:", game_header)
#print("game_content is:", game_content)

def split_line(line:str):
    """
    Splits a line in two.
    The first part contains up to the delimeter ":"
    The second part contains from the delimeter ":" onwards

    Input
      String
    Output
      Duple

    # Observe that each line has the format <ID : results>
    # That means we can use the character ":" to separate the line in two
    # game_parts is a list. The first element is the game id, the second the game results
    """
    game_parts = line.split(sep=': ')
    game_header = game_parts[0]
    game_content = game_parts[1]
    #print("FUNCTION SPLIT_LINE, BEGIN")
    #print("game_header is:", game_header)
    #print("game_content is:", game_content)
    #print("FUNCTION SPLIT_LINE, END")
    return (game_header, game_content)

#game_header, game_content = split_line(pl_v)
#####################################################################



#####################################################################
# SPLIT GAME
# Observe that each game header has the format <"Game" "<integer>">
# That means we can use the space character "" to separate the line in two
# game_parts is a list. The first element is the game id, the second the game results
#game_header_parts = game_header.split(sep=" ")
#print("1st element of the game_header_parts is:", game_header_parts[0], "and it is of type", type(game_header_parts[0]))
#print("2nd element of the game_header_parts is:", game_header_parts[1], "and it is of type", type(game_header_parts[1]))
# we need to transform the second 
#game_id = int(game_header_parts[1])
#print("the game_id is:", game_id, "and it is of type:", type(game_id))

def split_game_header(game_header:str):
    """
    Input
      String
    Output
      Integer
    
    # Observe that each game header has the format <"Game" "<integer>">
    # That means we can use the space character "" to separate the line in two
    # game_parts is a list. The first element is the game id, the second the game results
    """
    game_header_parts = game_header.split(sep=" ")
    #print("1st element of the game_header_parts is:", game_header_parts[0], "and it is of type", type(game_header_parts[0]))
    #print("2nd element of the game_header_parts is:", game_header_parts[1], "and it is of type", type(game_header_parts[1]))
    # we need to transform the second 
    game_id = int(game_header_parts[1])
    #print("the game_id is:", game_id, "and it is of type:", type(game_id))
    return game_id

#game_id = split_game_header(game_header)
#####################################################################



#####################################################################
# SPLIT RESULTS
# Observe that each game content has the format <<subset> ; <subset> ; ... ; <subset>>
# That means we can use the characters "; " to separate the line in as many subsets as there are in a game
# subsets is a list. Each element is a draw of cubes from the bag
#subsets = game_content.split(sep="; ")
#print("this game has this number of subsets:", len(subsets))
#for subset in subsets:
#    print("subset:", subset)
#    print("is of type:", type(subset))

# SPLIT RESULTS
def split_game_results(game_content:str):
    """
    """
    subsets = game_content.split(sep="; ")
    #print("FUNCTION SPLIT_RESULTS, BEGIN")
    #print("this game has this number of subsets:", len(subsets))
    #for subset in subsets:
        #print("subset:", subset)
        #print("is of type:", type(subset))
    #for subset_index, subset_content in enumerate(subsets):
        #print("subset_index:", subset_index, "subset_content:", subset_content)
    #print("FUNCTION SPLIT_RESULTS, END")
    return subsets

#subsets = split_game_results(game_content)
#####################################################################


#####################################################################
# SPLIT SUBSET
# Observe that each subset has the format <<int> <color>, ... , <int> <color>>
# That means we can use the characters ", " to separate the subset into as many colors there are in a subset
# colors is a list. Each element is a draw of cubes from the bag
# sample subset is subsets[0]
#colors = subsets[0].split(sep=", ")
#for color in colors:
#    print(color)

# SPLIT SUBSET
def split_subset(subset:str):
    """
    Separates a string in as many blocks as necessary. 
    Each block is a subset of the same format <<int> <color>, ... , <int> <color>>
    It is necessary that the format of the input string is precisely this: <<int> <color>, ... , <int> <color>>

    Input:
      Sting of the format <<int> <color>, ... , <int> <color>>
    
    Output:
      List of (<int> <color/string>)
    
    # Observe that each subset has the format <<int> <color>, ... , <int> <color>>
    # That means we can use the characters ", " to separate the subset into as many colors there are in a subset
    # colors is a list. Each element is a draw of cubes from the bag
    """
    colors = subset.split(sep=", ")
    #for color in colors:
    #    print("FUNCTION SPLIT_SUBSET", color)
    #print(type(colors)) # should be a list
    return colors

# invoke a sample subset
#colors = split_subset(subsets[0])
#####################################################################



#####################################################################
# SPLIT COLORS
# Observe that each color has the format <<int> <color>>
# That means we can use the space character " " to separate each color into its number_of_cubes and color_word
# colors is a list. Each element is a draw of cubes from the bag
# sample color result
#color_results = colors[0].split(sep=" ")
#number_of_cubes = color_results[0]
#color_of_cubes = color_results[1]
#print("number of cubes:", number_of_cubes, "of color:", color_of_cubes)

def split_color(color_result:str):
    """
    Separates a string in two. The first part is a number, the second a color.
    It is necessary that the format of the input string is precisely this: <int> <string>

    Input:
      Sting of the format <<int> <color_name>>
    
    Output:
      Tuple of the format (<int> <color/string>)
    
    # Observe that each color has the format <<int> <color>>
    # That means we can use the space character " " to separate each color into its number_of_cubes and color_word
    # colors is a list. Each element is a draw of cubes from the bag
    """
    color_split = color_result.split(sep=" ")
    number_of_cubes = int(color_split[0])
    #print(type(number_of_cubes))       # should be "int"
    color_of_cubes = color_split[1]
    #print("FUNCTION SPLIT_COLOR: number of cubes:", number_of_cubes, ", the color of the cubes is:", color_of_cubes)
    return (number_of_cubes, color_of_cubes)

#my_colors = split_color(colors[0])
#print(my_colors)
#####################################################################



maximum_number_of_cubes_blue = 14
maximum_number_of_cubes_green = 13
maximum_number_of_cubes_red = 12
games_possible = []
games_impossible = []

for game in games:
    # Split each Game into its header and its content
    game_header, game_content = split_line(game)
    print("Testing:", game_header)
    print("Testing content:", game_content, end='')

    # Extract the GAME_ID from each game header
    game_id = split_game_header(game_header)

    # We start by adding the game to the possible ones. 
    # later on we evaluate the game, if it is impossible, then we remove that game from the possible ones
    #games_possible.append(game_id)
    game_possible = True

    # Split the game content into a list of subsets
    subsets = split_game_results(game_content)

    # Split each subset into its colors
    for subset_index, subset_content in enumerate(subsets):
        subset_possible = True
        #print("subset with index:", subset_index, "subset content:", subset_content)
        print("Testing subset:", subset_content)
        #print("Before testing the colors, the subset:", subset_content, "is:", subset_possible)

        # Split each color into its color name and the number of cubes of that color
        colors = split_subset(subset_content)
        
        
        for color_index, color_content in enumerate(colors):
            color_possible = True
            print("Testing color:", color_content)
            
            number_of_cubes, color_of_cubes = split_color(color_content)
            #print("color index", color_index, "has:", number_of_cubes, "cubes of color:", color_of_cubes)

            match color_of_cubes.strip():
                case 'blue':
                    if number_of_cubes > maximum_number_of_cubes_blue:
                        color_possible = False
                        subset_possible = False
                        print(color_of_cubes, "is impossible")
                case 'green':
                    if number_of_cubes > maximum_number_of_cubes_green:
                        color_possible = False
                        subset_possible = False
                        print(color_of_cubes, "is impossible")
                case 'red':
                    if number_of_cubes > maximum_number_of_cubes_red:
                        color_possible = False
                        subset_possible = False
                        print(color_of_cubes, "is impossible")
                case _:
                    print("I do not recognize this color:", color_of_cubes)
                    exit()
            #print("we have completed testing color", color_of_cubes)
            #print("this far, the subset:", subset_content, "is:", subset_possible)

        if subset_possible == True:
            print("Subset possible")
        elif subset_possible == False:
            print("Subset impossible")
            game_possible = False
        else:
            print("I do not know if the subset is possible or impossible")
            exit()
    
    if game_possible == True:
        print("Game possible")
        games_possible.append(game_id)
    elif game_possible == False:
        print("Game impossible")
        #games_possible.remove(game_id)
        games_impossible.append(game_id)
    else:
        print("I do not know if the game is possible or impossible")
        exit()

print("\n")
print("games possible:", games_possible)
print("games impossible:", games_impossible)
print("sum of the ID of possible games:", sum(games_possible))
