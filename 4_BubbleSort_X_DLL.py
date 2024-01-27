class Node():
	def __init__(self, data=None):
		self.data = data
		self.next = None
		self.prev = None
		
class DLL():
	def __init__(self):
		self.head = None

	def insert_in_last(self, data):
		if self.head is None:
			self.head = Node(data)

			return

		headNode = self.head

		while headNode.next is not None:
			headNode = headNode.next

		headNode.next = Node(data)
		headNode.next.prev = headNode

	def insert_in_between(self, data, pos1, pos2):
		if self.head is None:
			self.head = Node(data)

			return

		headNode = self.head

		while headNode is not None:
			if headNode.prev is not None and (headNode.prev.data == pos1 and headNode.data == pos2):
				break

			headNode = headNode.next

		temp = Node(data)

		headNode.prev.next = temp
		temp.prev = headNode.prev

		headNode.prev = temp
		temp.next = headNode

	def insert_in_first(self, data):
		if self.head is None:
			self.head = Node(data)

			return

		temp = Node(data)

		self.head.prev = temp
		temp.next = self.head
		self.head = temp

	def delete_all(self):
		self.head = None

	def delete(self, data):
		if self.head.next is None:
			delete_all()

			return

		headNode = self.head

		while headNode.next is not None:
			if headNode.data == data:
				break

			headNode = headNode.next

		headNode.prev.next = headNode.next
		headNode.next.prev = headNode.prev

	def delete_first(self):
		if self.head.next is None:
			delete_all()

			return

		self.head = self.head.next

	def delete_last(self):
		if self.head.next is None:
			delete_all()

			return

		headNode = self.head

		while headNode.next is not None:
			headNode = headNode.next

		headNode.prev.next = None

	def print_all(self):
		temp = ""
		temp1 = ""


		headNode = self.head

		while headNode is not None:
			temp += str(headNode.data) + " <-> "
			temp1 += "kiri=>" + str(self.print1(headNode.prev)) + " tengah=>" + str(headNode.data) + " kanan=>" + str(self.print1(headNode.next)) + " <-> \n"
			headNode = headNode.next

		print(temp)
		# print(temp1)

	def print1(self, node):
		if node == None:
			return None
		return node.data


class BubbleSort():
	def __init__(self, data):
		self.nodes = self.convert_list_to_DLL(data)

	def convert_list_to_DLL(self, data) -> DLL():
		t1 = DLL()

		t1.head = Node(data[0])

		for x in range(1, len(data)):
			t1.insert_in_last(data[x])

		return t1

	def run(self):
		head = self.nodes.head

		while head is not None:
			incre = self.nodes.head
			while incre.next is not None:
				if incre.data > incre.next.data:
					temp = incre.data
					incre.data = incre.next.data
					incre.next.data = temp

				incre = incre.next

			head = head.next

		self.nodes.print_all()

t1 = BubbleSort([29, 45, 87, 23, 56, 19])
t1.run()

			