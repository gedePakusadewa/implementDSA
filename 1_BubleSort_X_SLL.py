# buble sort using single linked list

class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class SLL():
	def __init__(self):
		self.headNode = None

	def buble_sort(self):
		headNode = self.headNode
		node1 = self.headNode
		node2 = self.headNode

		while node1 is not None:

			while node2 is not None:
				if node2.next is not None:
					if node2.data > node2.next.data:
						temp = node2.data
						node2.data = node2.next.data
						node2.next.data = temp

				node2 = node2.next

			node2 = self.headNode

			node1 = node1.next

	def print_all(self):
		dataNode = self.headNode
		data = ""

		while dataNode is not None:
			data += str(dataNode.data) + " "
			dataNode = dataNode.next

		print(data)

	def insert_in_last(self, data):
		dataNode = self.headNode
		while dataNode.next is not None:
			dataNode = dataNode.next

		dataNode.next = Node(data)

	def convert_list_to_SLL(self, listData):
		self.headNode = listData[0]

		if len(listData) > 1:
			for idx in range(1, len(listData)):
				self.insert_in_last(listData[idx])

# 45 89 12 90 78
t1 = SLL()

# t1.headNode = Node(45)
# t1.insert_in_last(89)
# t1.insert_in_last(12)
# t1.insert_in_last(90)
# t1.insert_in_last(78)

# t1.print_all()

# t1.buble_sort()
# print()
# t1.print_all()

ex = [45, 89, 12, 90, 78]

t1.convert_list_to_SLL(ex)
t1.print_all()
