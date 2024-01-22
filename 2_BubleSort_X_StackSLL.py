# REF https://iq.opengenus.org/bubble-sort-using-two-stacks/
# how bubble sort with Stack SLL work:
# for example, there are two stacks U1 and U2. U1 with data stack 1, 45,
# 87, 23, 56, 19 where 19 is in the top position and 1 is in the
# bottom position of the stack.

# U1 = 1 (bottom), 45, 87, 23, 56, 19 (top)
# U2 = Blank

# Step 1:
# U1 = 1, 45, 87, 23, 56 -> U1 POPs 19
# temp = 19 -> value 19 goes into temporary variable temp
# check whether U2 is empty or the peak value of the stack U2 >= temp
# if true then the value 19 is pushed to U2
# if false then all values in U2 are popped then these pop values are pushed to U1
# until the condition evaluates to true
# U2 = 19

# step 2
# U1 = 1, 45, 87, 23 -> U1 POPs 56
# temp = 56

# Check whether U2 peek value >= temp
# because the condition is false, all U2 values are pop and pushed to U1 until the condition is true

# result:
# U1 = 1, 45, 87, 23, 19
# U2 = 56

# step 3
# U1 = 1, 45, 87, 23 -> U1 POPs 19
# temp = 19
# U2 = 56

# result:
# U1 = 1, 45, 87, 23,
# U2 = 56, 19

# step 3
# U1 = 1, 45, 87 -> U1 POPs 23
# temp = 23
# U2 = 56, 19

# result:
# U1 = 1, 45, 87, 19,
# U2 = 56, 23

# step 4
# U1 = 1, 45, 87 -> U1 POPs 19
# temp = 19
# U2 = 56, 23

# result:
# U1 = 1, 45, 87,
# U2 = 56, 23, 19

# step 5
# U1 = 1, 45 -> U1 POPs 87
# temp = 87
# U2 = 56, 23

# result:
# U1 = 1, 45, 19, 23, 56
# U2 = 87

# step 6
# U1 = 1, 45, 19, 23 -> U1 POPs 56
# temp = 56
# U2 = 87

# result:
# U1 = 1, 45, 19, 23
# U2 = 87, 56

# step 7
# U1 = 1, 45, 19 -> U1 POPs 23
# temp = 23
# U2 = 87, 56

# result:
# U1 = 1, 45, 19
# U2 = 87, 56, 23

# step 7
# U1 = 1, 45 -> U1 POPs 19
# temp = 19
# U2 = 87, 56, 23

# result:
# U1 = 1, 45
# U2 = 87, 56, 23, 19

# step 8
# U1 = 1 -> U1 POPs 45
# temp = 45
# U2 = 87, 56, 23, 19

# result:
# U1 = 1, 19, 23
# U2 = 87, 56, 45

# step 9
# U1 = 1, 19 -> U1 POPs 23
# temp = 23
# U2 = 87, 56, 45

# result:
# U1 = 1, 19
# U2 = 87, 56, 45, 23

# step 10
# U1 = 1 -> U1 POPs 19
# temp = 19
# U2 = 87, 56, 45, 23

# result:
# U1 = 1
# U2 = 87, 56, 45, 23, 19

# step 11
# U1 = empty -> U1 POPs 1
# temp = 1
# U2 = 87, 56, 45, 23, 19

# result:
# U1 = empty
# U2 = 87, 56, 45, 23, 19, 1


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


