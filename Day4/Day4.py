import sys

class LinkedList:
    def __init__(self):
        self.root = None
        self.last = None
        self.len = 0
        
    def add(self, instance):
        if self.root is None:
            self.root = instance
            self.last = instance
        elif self.len == 1:
            if instance < self.root: # this is a problem because in
                instance.next = self.root
                self.root = instance
            else:
                self.last = instance
                self.root.next = instance
        else:
            current = self.root
            if instance < self.root: # this is a problem
                instance.next = self.root
                self.root = instance
            else:    
                while current.next is not None and current.next < instance:
                    current = current.next
                if current.next is None:
                    current.next = instance
                    self.last = instance
                else:
                    instance.next = current.next
                    current.next = instance
        self.len += 1
        
    def pop(self):
        out = self.root
        self.root = self.root.next
        self.len -= 1
        return out
        
    def __len__(self):
        return self.len

class Instance:
    def __init__(self, time, command):
        self.next = None
        self.command = command
        self.time = time
        self.date, self.clock_time = time.split(' ')
        self.year, self.month, self.day = self.date.split('-')
        self.hour, self.minute = self.clock_time.split(':')
        self.year = int(self.year)
        self.month = int(self.month)
        self.day = int(self.day)
        self.hour = int(self.hour)
        self.minute = int(self.minute)
    
    def __str__(self):
        return '[' + self.time + '] ' + self.command
        
    def __lt__(self, other):
        if other.year == self.year:
            if other.month == self.month:
                if other.day == self.day:
                    if other.hour == self.hour:
                        return self.minute < other.minute
                    else:
                        return self.hour < other.hour
                else:
                    return self.day < other.day
            else:
                return self.month < other.month
        else:
            return self.year < other.year
        
# Part 1
'''     
def main():
    big_list = LinkedList()
    with open(sys.argv[1]) as f:
        file_data = f.read().split('\n')
    for line in file_data:
        time, command = line.replace('[', '').split('] ')
        new = Instance(time, command)
        big_list.add(new)  
    guard_dict = {} # value: [total time slept, [list of minutes]
    current_guard = None
    last_time = None
    while len(big_list) > 0:
        token = big_list.pop()
        token_comm_args = token.command.split(' ')
        if token_comm_args[0] == 'Guard':
            if token_comm_args[1] not in guard_dict:
                guard_dict[token_comm_args[1]] = [0, []]
            current_guard = token_comm_args[1]  
        elif token_comm_args[0] == 'falls':
            last_time = [token.year, token.month, token.day, token.hour, token.minute]
            if current_guard == '#733':
                print(last_time)
        elif token_comm_args[0] == 'wakes':
            current_time = [token.year, token.month, token.day, token.hour, token.minute]
            if current_guard == '#733':
                print(current_time)
            sleep_time = token.minute - last_time[4]
            guard_dict[current_guard][0] += sleep_time
            if current_guard == '#733':
                print(range(last_time[4] , current_time[4]))
            guard_dict[current_guard][1] = guard_dict[current_guard][1] + range(last_time[4] , current_time[4])
        
    sleepiest_guard = None
    longest = 0
    for guard in guard_dict:
        if guard_dict[guard][0] > longest:
            longest = guard_dict[guard][0]
            sleepiest_guard = guard
    common_min = 0
    num = 0
    # print(sorted(guard_dict[sleepiest_guard][1]))
    for min in set(guard_dict[sleepiest_guard][1]):
        # print(str(min) + ' count: ' + str(guard_dict[sleepiest_guard][1].count(min)))
        if guard_dict[sleepiest_guard][1].count(min) > num:
            common_min = min
            num = guard_dict[sleepiest_guard][1].count(min)
    return int(sleepiest_guard.replace('#', '')) * common_min
'''

# Part 2

def main():
    big_list = LinkedList()
    with open(sys.argv[1]) as f:
        file_data = f.read().split('\n')
    for line in file_data:
        time, command = line.replace('[', '').split('] ')
        new = Instance(time, command)
        big_list.add(new)  
    min_dict = {} # key: minute, value: [list of guards]
    current_guard = None
    last_time = None
    while len(big_list) > 0:
        token = big_list.pop()
        token_comm_args = token.command.split(' ')
        if token_comm_args[0] == 'Guard':
            if token.minute not in min_dict:
                min_dict[token.minute] = []
            current_guard = token_comm_args[1]  
        elif token_comm_args[0] == 'falls':
            last_time = [token.year, token.month, token.day, token.hour, token.minute]
        elif token_comm_args[0] == 'wakes':
            current_time = [token.year, token.month, token.day, token.hour, token.minute]
            for min in range(last_time[4] , current_time[4]):
                if min not in min_dict:
                    min_dict[min] = []
                min_dict[min].append(current_guard)
    freq_guard = 0
    freq_min = 0
    num = 0
    for min in min_dict:
        # print(str(min) + ' count: ' + str(guard_dict[sleepiest_guard][1].count(min)))
        for guard in sorted(min_dict[min]):
            if min_dict[min].count(guard) > num:
                freq_guard = guard
                freq_min = min
                num = min_dict[min].count(guard)
    return int(freq_guard.replace('#', '')) * freq_min

# Testing Stuff
''' i didn't even need the fucking linked list, i could've just sorted the file data
def main():
    with open(sys.argv[1]) as f:
        file_data = f.read().split('\n')
    file_data.sort()
    for line in file_data:
        print(line)
'''

print(main())
