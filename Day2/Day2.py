import sys

# Part 1
'''
def main():
    two_count = 0
    three_count = 0
    with open('Day2_input.txt') as f:
        file_data = f.read().split('\n')
    for line in file_data:
        two = False
        three = False
        for i in line:
            print(line.count(i))
            if line.count(i) == 2:
                two = True
            if line.count(i) == 3:
                three = True
        if two:
            print('inc two')
            two_count += 1
        if three:
            print('inc three')
            three_count += 1
    return two_count * three_count
'''

# Part 2
def main():
    prev_lines = set()
    with open('Day2_input.txt') as f:
        file_data = f.read().split('\n')
    for line in file_data:
        for prev in prev_lines:
            diff = []
            for i in range(26):
                if line[i] != prev[i]:
                    diff.append(i)
            if len(diff) == 1:
                '''
                print(diff)
                print(line)
                print(prev)
                '''
                return line[:diff[0]] + line[diff[0] + 1:]          
        prev_lines.add(line)
    return 'nut'
    
print(main())