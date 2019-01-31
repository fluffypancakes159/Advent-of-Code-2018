import sys

# Part 1
'''
def main():
	
	players = 452
	last_marble = 70784 
	
	scores = [0] * players
	board = [0]
	index = 0
	for i in range(1, last_marble + 1): # (i-1) % players -> index of players
		# print(board)
		if i % 23 != 0:
			# print(index)
			index = (index + 2) % len(board)
			board.insert(index, i)
		else:
			# print(i)
			index = (index - 7) % len(board)
			scores[i % players - 1] += board.pop(index) + i
			# print(scores)
			# print(index)
	# print(board)
	# print(scores)
	return max(scores)
'''

# Part 2

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None
		
	def __str__(self):
		return str(val)

class LinkedList:
	def __init__(self):	
		self.root = None
		self.end = None
		self.seventh = None
		self.len = 0
		
	def add (self, node):
		if self.len == 0:
			self.root = node
			self.root.next = node
			self.root.prev = node
			self.end = node
			self.seventh = node
		else:
			if self.len == 1:
				self.root.next = node
				self.end.prev = self.root
			self.seventh = self.root.prev.prev.prev.prev.prev.prev.prev
			self.len += 1			

def main():
	
	players = 452
	last_marble = 7078400 
	
	scores = [0] * players
	board = [0]
	index = 0
	for i in range(1, last_marble + 1): # (i-1) % players -> index of players
		# print(board)
		if i % 23 != 0:
			# print(index)
			index = (index + 2) % len(board)
			board.insert(index, i)
		else:
			# print(i)
			index = (index - 7) % len(board)
			scores[i % players - 1] += board.pop(index) + i
			# print(scores)
			# print(index)
	# print(board)
	# print(scores)
	return max(scores)

print(main())

# This takes a really fucking long time to run 