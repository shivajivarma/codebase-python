class Node(object):

	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next
        
	def __str__(self): 
		return str(self.data)

class SingleLinkedList(object):
 
	head = None
	tail = None
    
	def append(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
		else:
			self.tail.next = node
		self.tail = node
		
	def remove(self, value):
		current = self.head
		previous = None
		while current is not None:
			if current.data == value:				
				if previous is not None:
					previous.next = current.next
				else:
					self.head = current.next
			else:
				previous = current
			current = current.next
	def search(self, value):
		current = self.head
		found = False
		while current is not None:
			if(current.data == value):
				print("Found : ",value, "\n")
				found = True
				break
			current = current.next
		if not (found):
			print("Not found : ", value, "\n")
		
		
	def print(self):
		print("Linked list data:")
		current = self.head
		while current is not None:
			print(current, " -> ", end="")
			current = current.next
		print(None,'\n')
 
s = SingleLinkedList()
s.append(1)
s.append(2)
s.append(2)
s.append(3)
s.append(2)
s.append(2)
s.append(2)
s.print()
s.search(2)

s.remove(2)
s.print()
s.search(2)
