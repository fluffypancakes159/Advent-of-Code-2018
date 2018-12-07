import sys

# Part 1
'''
def main():
    big_dict = {}
    with open(sys.argv[1]) as f:
        file_data = f.read().split('\n')
    for line in file_data:
        xcor, ycor = line.split(', ')
        xcor = int(xcor)
        ycor = int(ycor)
        big_dict[xcor, ycor] = 0
    max_x = max(coor[0] for coor in big_dict)
    min_x = min(coor[0] for coor in big_dict)
    max_y = max(coor[1] for coor in big_dict)
    min_y = min(coor[1] for coor in big_dict)
    
    print(max_x)
    print(min_x)
    print(max_y)
    print(min_y)
    
    remove_coors = set()
    # print(big_dict)
    remove_coors = remove_coors.union(find_invalid_horiz(big_dict, min_x, max_x, min_y, max_y))
    # print(find_invalid_horiz(big_dict, min_x, max_x, min_y, max_y))
    remove_coors = remove_coors.union(find_invalid_vert(big_dict, min_x, max_x, min_y, max_y))
    # print(find_invalid_vert(big_dict, min_x, max_x, min_y, max_y))
    print(remove_coors)
    # print(big_dict)
    for y in range(min_y + 1, max_y):
        for x in range(min_x + 1, max_x):
            dists = []
            coords = []
            for coor in big_dict:
                _dist = dist(coor, (x, y))
                dists.append(_dist)
                coords.append(coor)
            if dists.count(min(dists)) > 1:
                continue
            # print(closest)
            if coords[dists.index(min(dists))] not in remove_coors:
                big_dict[coords[dists.index(min(dists))]] += 1
    print(big_dict)
    return max(big_dict.values())
'''

# Part 2

def main():
    big_dict = {}
    with open(sys.argv[1]) as f:
        file_data = f.read().split('\n')
    for line in file_data:
        xcor, ycor = line.split(', ')
        xcor = int(xcor)
        ycor = int(ycor)
        big_dict[xcor, ycor] = 0
    max_x = max(coor[0] for coor in big_dict)
    min_x = min(coor[0] for coor in big_dict)
    max_y = max(coor[1] for coor in big_dict)
    min_y = min(coor[1] for coor in big_dict)
    '''
    remove_coors = set()
    remove_coors = remove_coors.union(find_invalid_horiz(big_dict, min_x, max_x, min_y, max_y))
    remove_coors = remove_coors.union(find_invalid_vert(big_dict, min_x, max_x, min_y, max_y))
    print(remove_coors)
    '''
    num_coords = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            total = 0
            for coor in big_dict:
                _dist = dist(coor, (x, y))
                total += _dist
            # print(closest)
            if total < 10000:
                num_coords += 1
    # print(big_dict)
    return num_coords
    
def dist(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])
    
def find_invalid_vert(big_dict, min_x, max_x, min_y, max_y):
    remove_coors = set()
    for c in range(min_y, max_y + 1):
        dists = []
        coords = []
        for coor in big_dict:
            _dist = dist(coor, (max_x, c))
            dists.append(_dist)
            coords.append(coor)
        if dists.count(min(dists)) > 1:
            continue
        # print(closest)
        remove_coors.add(coords[dists.index(min(dists))])
    for c in range(min_y, max_y + 1):
        dists = []
        coords = []
        for coor in big_dict:
            _dist = dist(coor, (min_x, c))
            dists.append(_dist)
            coords.append(coor)
        if dists.count(min(dists)) > 1:
            continue
        # print(closest)
        remove_coors.add(coords[dists.index(min(dists))])
    return remove_coors

def find_invalid_horiz(big_dict, min_x, max_x, min_y, max_y):
    remove_coors = set() 
    for c in range(min_x, max_x + 1):
        dists = []
        coords = []
        for coor in big_dict:
            _dist = dist(coor, (c, max_y))
            dists.append(_dist)
            coords.append(coor)
        if dists.count(min(dists)) > 1:
            continue
        # print('Closest to ' + str((c, max_y)) + ': ' + str(coords[dists.index(min(dists))]))
        remove_coors.add(coords[dists.index(min(dists))])
    for c in range(min_x, max_x + 1):
        dists = []
        coords = []
        for coor in big_dict:
            _dist = dist(coor, (c, min_y))
            dists.append(_dist)
            coords.append(coor)
        if dists.count(min(dists)) > 1:
            continue
        # print('Closest to ' + str((c, min_y)) + ': ' + str(coords[dists.index(min(dists))]))
        remove_coors.add(coords[dists.index(min(dists))])
    return remove_coors
    
print(main())
#8937 too high
#not 3606
#not 5826