import sys

# Part 1
'''
def main():
    with open(sys.argv[1], 'rU') as f:
        file_data = f.read().split()
    # print(file_data)
    total = 0
    for i in file_data:
        total += int(i)
    return total
'''

# Part 2

def main():
    with open(sys.argv[1], 'rU') as f:
        file_data = f.read().split()
    # print(file_data)
    total = 0
    frequencies = set()
    frequencies.add(0)
    while True:
        for i in file_data:
            # print(frequencies)
            total += int(i)
            if total in frequencies:
                return total
            frequencies.add(total)
    return 'nut'
    
#print( int('+12'))
print(main())