import sys

# Part 1
'''
def main():
    capitals = set()
    for i in range(26):
        capitals.add(chr(65+i))
    # print(capitals)
    big_dict = {}
    order = []
    with open(sys.argv[1]) as f:
        file_data = f.read().split('\n')
    for line in file_data:
        # print len(line)
        if line[5] in big_dict:
            big_dict[line[5]][0].append(line[36])
        else:
            big_dict[line[5]] = [[line[36]], 0]
        # print(args)
    vals = []
    for val in big_dict.values():
        vals = vals + val[0]
    for letter in capitals:
        if letter not in big_dict:
            big_dict[letter] = [[], 0]
    for line in file_data:
        # print len(line)
        if line[36] in big_dict:
            big_dict[line[36]][1] += 1
    frontier = list(capitals - set(vals))
    frontier.sort()
    # print(frontier)
    while len(frontier) > 0:
        print(frontier)
        next = frontier.pop(0)
        order.append(next)
        new_nodes = []
        for next_node in big_dict[next][0]:
            big_dict[next_node][1] -= 1
            if big_dict[next_node][1] == 0:
                new_nodes.append(next_node)
        frontier = frontier + new_nodes
        frontier.sort()
    return ''.join(order)
 '''     
      
 # Part 2

def main():
    # retrieve/initialize nodes
    capitals = set()
    for i in range(26):
        capitals.add(chr(65+i))
    big_dict = {}
    order = []
    with open(sys.argv[1]) as f:
        file_data = f.read().split('\n')
    for line in file_data:
        if line[5] in big_dict:
            big_dict[line[5]][0].append(line[36])
        else:
            big_dict[line[5]] = [[line[36]], 0]
    vals = []
    for val in big_dict.values():
        vals = vals + val[0]
    for letter in capitals:
        if letter not in big_dict:
            big_dict[letter] = [[], 0]
    for line in file_data:
        if line[36] in big_dict:
            big_dict[line[36]][1] += 1
    frontier = list(capitals - set(vals))
    frontier.sort()
    # deal out workload
    workers = [None, None, None, None, None]
    time_left = [0, 0, 0, 0, 0]
    total_time = 0
    while len(order) < 26:
        for j in range(min(len(frontier), workers.count(None))):
            for i, w in enumerate(workers):
                if w is None:
                    workers[i] = frontier.pop(0)
                    time_left[i] = ord(workers[i]) - 4
                    break
        passed_time = min_(time_left)
        time_left = [x - passed_time for x in time_left]
        total_time += passed_time
        for i in range(len(time_left)):
            if time_left[i] == 0:
                next = workers[i]
                order.append(next)
                new_nodes = []
                for next_node in big_dict[next][0]:
                    big_dict[next_node][1] -= 1
                    if big_dict[next_node][1] == 0:
                        new_nodes.append(next_node)
                workers[i] = None
        frontier = frontier + new_nodes
        frontier.sort()
    return total_time

def min_ (list):
    min = 100000000000000000000000000
    for i in list:
        if i > 0 and i < min:
            min = i
    return min
    
print(main())