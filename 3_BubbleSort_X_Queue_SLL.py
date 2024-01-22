class Node():
	def __init__(self, data=None):
		self.data = data
		self.next = None

class Queue():
	def __init__(self):
		self.head = None

	def enqueue(self, data):
		if self.head is None:
			self.head = Node(data)

			return

		currNode = self.head
		while currNode.next is not None:
			currNode = currNode.next

		currNode.next = Node(data)

	def dequeue(self):
		if self.head.next is None:
			self.head = None

			return

		nextNode = self.head.next
		self.head = nextNode

	def convert_array_to_queue(self, data):
		self.enqueue(data[0])

		if len(data) <= 1:
			return

		currNode = self.head

		for x in range(1, len(data)):
			self.enqueue(data[x])

	def print_all(self):
		if self.head.next is None:
			print(self.head.data)

			return

		temp = ""
		currNode = self.head

		while currNode is not None:
			temp += str(currNode.data) + " <= "
			currNode = currNode.next

		print(temp)

class BubbleSort():
	def __init__(self, data=None):
		self.queue = self.convert_list_to_queue(data)

	def sort(self):
		self.queue.print_all()

	def convert_list_to_queue(self, data) -> Queue():
		temp = Queue()
		temp.convert_array_to_queue(data)

		return temp


tm = [2, 45, 23, 98, 49, 11]

t1 = BubbleSort(tm)
t1.sort()
