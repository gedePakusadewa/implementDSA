class Node():
	def __init__(self, data=None):
		self.data = data
		self.next = None

class SLL():
	def __init__(self):
		self.headNode = None

	def print_(self):
		temp = ""
		dataNode = self.headNode
		while dataNode is not None:
			temp += " " + str(dataNode.data)
			dataNode = dataNode.next
		print(temp)

	# insert in last node
	def insert_in_last(self, data):
		if self.headNode is None:
			self.headNode = Node(data)

			return

		dataNode = self.headNode
		while dataNode.next is not None:
			dataNode = dataNode.next

		dataNode.next = Node(data)

	def insert_in_first(self, data):
		tempNode = self.headNode
		self.headNode = Node(data)
		self.headNode.next = tempNode

	def insert_between(self, node, data):
		temp = Node(data)

		temp.next = node.next
		node.next = temp


class InsertionSort():
	def __init__(self, data=None):
		self.data = data
		self.dataNode = self.convert_list_to_SLL(data)

	def convert_list_to_SLL(self, listData):
		if listData is None:
			return None

		dataNode = SLL()

		for idx in range(len(listData)):
			dataNode.insert_in_last(listData[idx])

		return dataNode

	def asc_sort(self):
		node = self.dataNode.headNode
		sorted_node = SLL()

		while node is not None:
			sorted_node = self.sort_the_node(sorted_node, node)

			node = node.next

		self.dataNode = sorted_node

	def sort_the_node(self, node, curr_data):

		if node.headNode is None:
			node.insert_in_last(curr_data.data)

			return node

		if node.headNode.data > curr_data.data:
			node.insert_in_first(curr_data.data)
		else:
			curr = node.headNode
			while curr.next is not None and curr.next.data < curr_data.data:
				curr = curr.next
				
			node.insert_between(curr, curr_data.data)

		return node

	def print_(self):
		self.dataNode.print_()


t1 = InsertionSort([73, 26, 99, -33, 42, -52, 44, -33, 65, -53])
# t1.print_()
t1.asc_sort()
t1.print_()





