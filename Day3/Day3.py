import sys

# Part 1
'''
def main():
    big_dict = {}
    count = 0
    
    with open(sys.argv[1]) as f:
        file_data = f.read().split('\n')
    
    file_data = ['#1 @ 387,801: 11x22']
    
    for line in file_data:
        # print(line)
        # print(line.split(' @ '))
        id = line.split(' @ ')[0]
        coords, dimens = line.split(' @ ')[1].split(': ')
        coords = coords.split(',')
        dimens = dimens.split('x')
        # print(coords)
        # print(dimens)
        # dimens[0] -> y, dimens[1] -> x
        for i in range(int(dimens[0])):
            for j in range(int(dimens[1])):
                new_coords = (int(coords[0]) + i, int(coords[1]) + j)
                # print(new_coords)
                if new_coords not in big_dict:
                    big_dict[new_coords] = 0
                else:
                    big_dict[new_coords] += 1
    for coord in big_dict:
        if big_dict[coord] >= 1:
            count += 1
    return count
'''

# Part 2

def main():
    big_dict = {}
    big_set = set()
    count = 0
    with open(sys.argv[1]) as f:
        file_data = f.read().split('\n')
    for line in file_data:
        id = int(line.split(' @ ')[0].replace('#', ''))
        big_set.add(id)
        coords, dimens = line.split(' @ ')[1].split(': ')
        coords = coords.split(',')
        dimens = dimens.split('x')
        for i in range(int(dimens[0])):
            for j in range(int(dimens[1])):
                new_coords = (int(coords[0]) + i, int(coords[1]) + j)
                # print(new_coords)
                if new_coords not in big_dict:
                    big_dict[new_coords] = [id]
                else:
                    big_dict[new_coords].append(id)
    for coord in big_dict:
        if len(big_dict[coord]) > 1:
            for id in big_dict[coord]:
                if id in big_set:
                    big_set.remove(id)
    return list(big_set)[0]

print(main())
