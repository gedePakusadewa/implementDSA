class Node():
	def __init__(self, data=None):
		self.data = dataNode
		self.next = None

class SLL():
	def __init__(self):
		self.headNode = None

	def print_(self):
		dataNode = self.headNode
		while dataNode is not None:
			print(dataNode.data)
			dataNode = dataNode.next

	# insert in last node
	def insert(self, data):
		dataNode = self.headNode
		while dataNode.next is not None:
			dataNode = dataNode.next

		dataNode.next = Node(data)

class InsertionSort():
	def __init__(self, data=None):
		self.data = data
		self.dataNode = self.convert_list_to_SLL(data)

	def convert_list_to_SLL(self, listData):
		if listData is None:
			return None

		dataNode = SLL()

		for idx in range(len(listData)):
			dataNode.insert(listData[idx])

		return dataNode

	def asc_sort(self):
		node = self.dataNode.headNode
		sorted_node = None

		while node is not None:

			sorted_node = tes1(sorted_node, node.data)

			node = node.next

	def tes1(self, curr_node, data):
		head = 




