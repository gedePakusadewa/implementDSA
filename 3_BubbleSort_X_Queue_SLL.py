PENDING

# q1 = [30, 16, 25, 52, 75, 57, 12, 50, 23]
# q2 = empty

# q1 = [30, 16, 25, 52, 75, 57, 12, 50]
# q2 = 23

# q1 = [30, 16, 25, 52, 75, 57, 12]
# 1. cek apakah q2 kosong, klo kosong langsung masukin 50
# klo nggk maka keluarin 23 terus bandingkan mana yg lebih besar, yg lebih besar masuk duluan
# q2 = 23, 50

# q1 = [30, 16, 25, 52, 75, 57]
# q2 = 12, 23, 50

# q1 = [30, 16, 25, 52, 75]
# q2 = 12, 23, 50, 57

# q1 = [30, 16, 25, 52]
# q2 = 12, 23, 50, 57, 75

# q1 = [30, 16, 25]
# q2 = 12, 23, 50, 52, 57, 75

# q1 = [30, 16]
# q2 = 12, 23, 25, 50, 52, 57, 75

# q1 = [30]
# q2 = 12, 16, 23, 25, 50, 52, 57, 75

# q1 = empty
# q2 = 12, 16, 23, 25, 30, 50, 52, 57, 75


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
			temp = self.head
			self.head = None

			return temp

		nextNode = self.head.next
		temp = self.head
		self.head = nextNode

		return temp.data

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

	def peek(self):
		if self.head is None:
			return

		return self.head.data

	def rear(self):
		if self.head is None:
			return

		currNode = self.head
		while currNode.next is not None:
			currNode = currNode.next

		return currNode.data

	def is_empty(self):
		if self.head is None:
			return True

		return False

	def q_length(self):
		if self.head is None:

			return 0

		incre = 0
		currNode = self.head
		while currNode.next is not None:
			currNode = currNode.next
			incre += 1

		return incre


class BubbleSort():
	def __init__(self, data=None):
		self.queue = self.convert_list_to_queue(data)


	def sort(self):

		# self.queue.print_all()
		# print(self.queue.rear())
		# print(self.queue.peek())

		# q1 = self.queue
		# q2 = Queue()

		# while q1.is_empty() is not True:
		# 	if q2.is_empty() is True:
		# 		q2.enqueue(q1.dequeue())

		# 	while q2.is_empty() is

		print(self.is_sorted())

	def is_sorted(self):
		q1 = self.queue
		q2 = Queue()
		stop = True
		while q1.is_empty() is not True:
			temp = q1.dequeue()
			if q2.is_empty():
				q2.enqueue(temp)

				continue

			if temp > q2.peek():
				stop = False
				break

			q2.enqueue(temp)
			q2.print_all()

		return stop


	def convert_list_to_queue(self, data) -> Queue():
		temp = Queue()
		temp.convert_array_to_queue(data)

		return temp


# tm = [2, 45, 23, 98, 49, 11]
tm = [12, 16, 23, 25]


t1 = BubbleSort(tm)
t1.sort()


PENDING