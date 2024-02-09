class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class SLL():
	def __init__(self):
		self.headNode = None

	def printAll(self):
		dataNode = self.headNode

		while dataNode is not None:
			print(dataNode.data)

			dataNode = dataNode.next

	def insertInLast(self, data):
		if self.headNode is None:
			self.headNode = Node(data)

			return

		dataNode = self.headNode
		while dataNode.next is not None:
			dataNode = dataNode.next

		dataNode.next = Node(data)

class SelectionSortSLL():
	def __init__(self, data=None):
		self.data = data
		self.dataNode = self.convert_list_to_SLL(data)

	def convert_list_to_SLL(self, listData):
		if listData is None:
			return None

		dataNode = SLL()

		for idx in range(len(listData)):
			dataNode.insertInLast(listData[idx])

		return dataNode

	def asc_sort(self):
		outerNodes = self.dataNode.headNode
		innerNodes = None
		init_data = None

		while outerNodes is not None:
			innerNodes = outerNodes.next
			init_data = outerNodes

			while innerNodes is not None:
				if innerNodes.data < init_data.data:
					init_data = innerNodes

				innerNodes = innerNodes.next

			if init_data != outerNodes:
				temp = outerNodes.data
				outerNodes.data = init_data.data
				init_data.data = temp

			outerNodes = outerNodes.next

	def desc_sort(self):
		outerNodes = self.dataNode.headNode
		innerNodes = None
		init_data = None

		while outerNodes is not None:
			innerNodes = outerNodes.next
			init_data = outerNodes

			while innerNodes is not None:
				if innerNodes.data > init_data.data:
					init_data = innerNodes

				innerNodes = innerNodes.next

			if init_data != outerNodes:
				temp = outerNodes.data
				outerNodes.data = init_data.data
				init_data.data = temp

			outerNodes = outerNodes.next

	def print_(self):
		self.dataNode.printAll()


t1 = SelectionSortSLL([-2, 45, 0, 11, -9])
# t1.print_()
t1.desc_sort()
print("---------------")
t1.print_()