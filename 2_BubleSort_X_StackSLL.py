# REF https://iq.opengenus.org/bubble-sort-using-two-stacks/
# how bubble sort with Stack SLL work:
example Misalnya ada dua stack U1 dan U2. U1 dengan data stack 1, 45,
87, 23, 56, 19 dimana 19 berada diposisi atas dan 1 berada pada
posisi bawah dari stack.

U1 = 1 (bottom), 45, 87, 23, 56, 19(top)
U2 = Empty

step 1:
U1 = 1, 45, 87, 23, 56 -> U1 mem-POP-kan 19
temp = 19 -> nilai 19 masuk ke variable sementara temp
melakukan pengecekan, apakah U2 kosong atau nilai puncak stack U2 >= temp


class Node():
	def __init__(self, data=None):
		self.data = data
		self.next = None

class StackSLL():
	def __init__(self):
		self.headNode = None

	def push(self, data):
		headNode = self.headNode
		if headNode is None:
			self.headNode = Node(data)

			return

		dataNode = Node(data)

		dataNode.next = self.headNode
		self.headNode = dataNode

	def pop(self):
		headNode = self.headNode

		if headNode.next is None:
			self.headNode = None

		self.headNode = headNode.next

	def pop2(self) -> Node():
		headNode = self.headNode

		if headNode.next is None:
			self.headNode = None

		self.headNode = headNode.next

		return headNode

	def print_all(self):
		head = self.headNode
		tempData = ""

		if head == None:
			print("None")

			return

		if head.next is None:
			print(head.data)

			return
		
		tempData += str(head.data)
		head = head.next

		while head is not None:
			# print(head.data)
			tempData = str(head.data) + " <= " + tempData
			head = head.next

		print(tempData)

	def peak(self):
		return self.headNode.data

	def is_empty(self):
		if self.headNode is None:
			return True

		return False

class BubbleSort():
	def __init__(self, data):
		self.stack_1 = self.convert_to_Stack_SLL(data)
		self.stack_2 = StackSLL()

	def convert_to_Stack_SLL(self, data) -> StackSLL():
		if len(data) < 1:
			return None

		sll = StackSLL()
		sll.headNode = Node(data[0])

		for x in range(1, len(data)):
			sll.push(data[x])

		return sll

	def run_asc(self):
		st_1 = self.stack_1
		st_2 = self.stack_2
		incre = 20

		while st_1.is_empty() is not True:
			temp = st_1.pop2()

			while(st_2.is_empty() is not True and st_2.peak() < temp.data):
				tempNode = st_2.pop2()
				st_1.push(tempNode.data)

			st_2.push(temp.data)

		self.stack_1.print_all()
		self.stack_2.print_all()

	def run_desc(self):
		st_1 = self.stack_1
		st_2 = self.stack_2
		incre = 20

		while st_1.is_empty() is not True:
			temp = st_1.pop2()

			while(st_2.is_empty() is not True and st_2.peak() > temp.data):
				tempNode = st_2.pop2()
				st_1.push(tempNode.data)

			st_2.push(temp.data)

		self.stack_1.print_all()
		self.stack_2.print_all()

t1 = BubbleSort([1, 45, 87, 23, 56, 19])
t1.run_desc()


