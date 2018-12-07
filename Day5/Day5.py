import sys

# Part 1
'''
def main():
    index = 0
    with open(sys.argv[1]) as f:
        file_data = f.read()
    # file_data = 'dabAcCaCBAcCcaDA '
    while index < len(file_data) - 1:
        if abs(ord(file_data[index]) - ord(file_data[index+1])) == 32:
            file_data = file_data[:index] + file_data[index + 2:]
            index -= 2
            # print(file_data)
        index += 1
    return len(file_data) - 1
'''

# Part 2

def main():
    types = []
    for i in range(26): # generate list of letter pairs
        types.append([chr(65 + i), chr(97 + i)])
    # print(types)
    index = 0
    shortest = 100000000000000000000000000000000 # thicc number
    with open(sys.argv[1]) as f:
        file_data = f.read()
    for type in types:
        new_file_data = file_data.replace(type[0], '').replace(type[1], '')
        while index < len(new_file_data) - 1: # added a space at the end of the input as a buffer
            if abs(ord(new_file_data[index]) - ord(new_file_data[index+1])) == 32:
                new_file_data = new_file_data[:index] + new_file_data[index + 2:]
                index -= 2
                # print(file_data)
            index += 1
        if len(new_file_data) < shortest:
            shortest = len(new_file_data) - 1
        index = 0
    return shortest
    
print(main())
       