import sys

# Part 1
'''
def main():
	with open(sys.argv[1]) as f:
		file_data = f.read().split(' ')
	children = file_data.pop(0)
	metadata = file_data.pop(0)
	ret = recurse(file_data, children, metadata)
	# print(file_data)
	return ret
	
def recurse(data, children, metadata):
	# print(data)
	# print('Children: ' + str(children))
	# print('Metadata: ' + str(metadata))
	# print(len(data))
	total = 0
	if int(children) > 0:
		for i in range(int(children)):
			children_ = data.pop(0)
			metadata_ = data.pop(0)
			total += recurse(data, children_, metadata_)
			# print('Total: ' + str(total))
	# print('Children: ' + str(children))
	# print('Metadata: ' + str(metadata))
	# print('Adding metadata...')
	for i in range(int(metadata)):
		new = int(data.pop(0))
		# print('New: ' + str(new)) 
		total += new
	return total
'''

# Part 2

def main():
	with open(sys.argv[1]) as f:
		file_data = f.read().split(' ')
	children = file_data.pop(0)
	metadata = file_data.pop(0)
	ret = recurse(file_data, children, metadata)
	# print(file_data)
	return ret
	
def recurse(data, children, metadata):
	if int(children) == 0:
		total = 0
		for i in range(int(metadata)):
			total += int(data.pop(0))
		'''
		print('Children: ' + str(children))
		print('Metadata: ' + str(metadata))
		'''
		return total
	totals = []
	if int(children) > 0:
		for i in range(int(children)):
			children_ = int(data.pop(0))
			metadata_ = int(data.pop(0))
			totals.append(recurse(data, children_, metadata_))
	# print(totals)
	total = 0
	for i in range(int(metadata)):
		new = int(data.pop(0))
		if new < int(children) + 1:
			total += totals[new - 1]
	return total
	
print(main())

	