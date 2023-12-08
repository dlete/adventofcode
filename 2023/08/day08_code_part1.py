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

def prepare_instructions(instructions:str):
    """Takes a list with a single string element, returns a list of characters"""
    instructions = list(instructions[0])
    # Verify
    #print("directions is an object of type:", type(directions))
    #print("lenght of the list directions:", len(directions))
    #for direction in directions:
    #    print(direction)
    
    # Finish
    return instructions

def prepare_network(network:list):
    """Takes a list any number of network nodes/peers, returns them 
    sanitized and formated

    Returns a tuple of lists. First list has the node numbers, second list has
    the node peers.

    Returns:
      (node_names, nodes_peers)
    
    """
    # Initialize
    nodes_names = []
    nodes_peers = []
    for node_details in network:
        # Split in two: name and peers
        node_name, node_peers = node_details.split(" = ")
        # Cleanse/trim both node and peers
        node_name = node_name.strip()
        node_peers = node_peers.strip()
        node_peers = node_peers.replace('(', '')
        node_peers = node_peers.replace(')', '')
        # Convert peers to a tuple
        node_peer_left, node_peer_right = node_peers.split(", ")
        node_peer_left = node_peer_left.strip()
        node_peer_right = node_peer_right.strip()
        node_peers = (node_peer_left, node_peer_right)
        # Place both node and peers into their corresponding lists
        nodes_names.append(node_name)
        nodes_peers.append(node_peers)
        # Verify
        #print("PREPARE NETWORK,", "node name:", node_name, "and node peers:", node_peers, "node peers is object of type:", type(node_peers), "this far there are:", len(nodes_names), "nodes")

    # Finish
    #print("PREPARE NETWORK, node_names:", nodes_names)
    #print("PREPARE NETWORK, node_peers:", nodes_peers)
    return (nodes_names, nodes_peers)


def node_name_to_node_index(nodes_names:list, node_name:str):
    """Given a list and a element, returns the index of the element in the list
    
    Returns:
        node_index_found: int
    """
    node_index_found = nodes_names.index(node_name)
    # Verify
    #print("FIND NODE:",
    #      "input node name to find is:", node_name,
    #      "index found for that node name is:", node_index_found, 
    #      "node name of element in that index is:", nodes_names[node_index_found])

    # Finish
    return node_index_found


def trace_node(network:list, instructions:list, node_name_start:str, node_name_end:str, iteration:int, steps:int):
    # Define
    nodes_names = network[0]    # list
    nodes_peers = network[1]    # list

    # Initialize
    node_name = node_name_start
    node_index = node_name_to_node_index(nodes_names, node_name)
    node_peers = nodes_peers[node_index]

    instruction_index = 0
    instruction_direction = instructions[instruction_index]
    steps = steps

    while node_name != node_name_end:
        print("node:", node_name, "peers", node_peers)
        print("instruction index:", instruction_index)
        print("direction:", instruction_direction, "going to next node")

        if instruction_direction == 'L':
            node_name = node_peers[0]
        elif instruction_direction == 'R':
            node_name = node_peers[1]

        node_index = node_name_to_node_index(nodes_names, node_name)
        node_peers = nodes_peers[node_index]
        
        instruction_index = (instruction_index + 1)%len(instructions)
        instruction_direction = instructions[instruction_index]
        steps = steps + 1

        if steps > 77000:
            quit()
    
    print("SUCCESS, have gone",
          "from", node_name_start, 
          "to", node_name_end, 
          "in", steps, "steps")
    return steps


def sandbox():
    # Open input file
    #instructions = file_open("day08_input_part1_example1_instructions.txt")
    #network = file_open("day08_input_part1_example1_network.txt")
    #instructions = file_open("day08_input_part1_example2_instructions.txt")
    #network = file_open("day08_input_part1_example2_network.txt")
    instructions = file_open("day08_input_code_instructions.txt")
    network = file_open("day08_input_code_network.txt")
    # Verify
    #for direction in directions:
    #    print(direction)
    #for node in nodes:
    #    print(node)

    # Prepare data, process the data and compute the total number of points
    instructions = prepare_instructions(instructions)
    network = prepare_network(network)
    # Verify
    #print("VERIFY SANDBOX")
    #print("directions is an object of type:", type(instructions))
    #print("lenght of the list directions:", len(instructions))
    #print("network is an object of type:", type(network))
    #print("lenght of the list network:", len(network))
    #nodes_names = network[0]
    #nodes_peers = network[1]
    #for node_index, node_name in enumerate(nodes_names):
    #    node_peers = nodes_peers[node_index]
    #    node_peers_left = nodes_peers[node_index][0]
    #    node_peers_right = nodes_peers[node_index][1]
    #    print("network element with index:", node_index, 
    #          "has node name:", node_name, 
    #          ", and peers:", node_peers,
    #          "peer on the left is:", node_peers_left,
    #         "peer on the right is:", node_peers_right)

    node_name_start = 'AAA'
    node_name_end = 'ZZZ'
    #trace_results = trace_node(network, instructions, node_name_start, node_name_end, iteration=1, steps=0)
    #print("SANDBOX, trace:", trace_results)
    steps = trace_node(network, instructions, node_name_start, node_name_end, iteration=1, steps=0)
    print("SANDBOX, have gone",
          "from", node_name_start, 
          "to", node_name_end, 
          "in", steps, "steps")

# Execute this function automatically when the file is invoked from the CLI
#main()
print("\n")
sandbox()