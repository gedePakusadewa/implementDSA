# berdasarkan array merge sort, cobak bikin perlahan bagian merge_sort dengan SLL
# kemudian bikin bagian merge dengan SLL

# cobak pelajari lagi ini
# https://www.geeksforgeeks.org/merge-sort-for-linked-list/

class Node():
	# make object Node
	def __init__(self, data=None):
		self.data = data
		self.next = None

class SLL():
	def __init__(self):
		self.headNode = None

	# print all data in one 
	# print/line using list
	def print_all(self):
		dataNode = self.headNode
		list_data = []

		while dataNode is not None:
			list_data.append(dataNode.data)
			dataNode = dataNode.next

		print(list_data)	

	# insert new data in tail of nodes
	def insert_in_last(self, data):
		if self.headNode == None:
			self.headNode = Node(data)

			return

		dataNode = self.headNode
		while dataNode.next is not None:
			dataNode = dataNode.next

		dataNode.next = Node(data)

# get total length from SLL
# total number of node/data in one SLL
def get_len_SLL(SLL):
	len_sll = 0
	dataNode = SLL.headNode

	while dataNode is not None:
		len_sll += 1
		dataNode = dataNode.next

	return len_sll

# get cutted SLL using data from start and end
# start and end is index
# start indicate what node will be start of cutting
# end indicate what node will be the end of cutting
# ex nodes 3 -> 1 -> 4 -> 5
# the indices will be:
# index = 0    1    2    3
# nodes = 3 -> 1 -> 4 -> 5
# so when start is 1 and end is 2
# then it cut from index 1 to 2 and the result is
# 1 -> 4
def cut_SLL(SLL_data, start, end):
	len_sll = 0
	dataNode = SLL_data.headNode
	tes1 = SLL()

	while dataNode is not None:
		if len_sll >= start and len_sll < end:
			tes1.insert_in_last(dataNode.data)

		dataNode = dataNode.next
		len_sll += 1

	return tes1


def merge_sort(unsorted_list):
	if unsorted_list.headNode == None:
		return

	if unsorted_list.headNode.next == None:
		return unsorted_list

	len_data = get_len_SLL(unsorted_list)
	middle = len_data // 2

	left_list = cut_SLL(unsorted_list, 0, middle)
	right_list = cut_SLL(unsorted_list, middle, len_data)

	# list_data = []
	# dataNode = right_list.headNode
	# while dataNode is not None:
	# 	list_data.append(dataNode.data)
	# 	# print("asdasd ", dataNode.data)
	# 	dataNode = dataNode.next
	# print(list_data)

	left_list = merge_sort(left_list)
	right_list = merge_sort(right_list)

	return merge(left_list, right_list)

def merge(left_half, right_half):
	res = SLL()

	head_l = left_half.headNode
	head_r = right_half.headNode

	while head_l != None and head_r != None:

		if head_l.data < head_r.data:
			res.insert_in_last(head_l.data)
			head_l = head_l.next
		else:
			res.insert_in_last(head_r.data)

			head_r = head_r.next

	if head_l == None:
		res.insert_in_last(head_r.data)
	else:
		res.insert_in_last(head_l.data)

	return res


def print_all_1(sll_data):
	dataNode = sll_data.headNode
	list_data = []

	while dataNode is not None:
		list_data.append(dataNode.data)
		# print("asdasd ", dataNode.data)
		dataNode = dataNode.next

	print(list_data)	

s1 = SLL()
s1.insert_in_last(3)
s1.insert_in_last(5)

# s2 = SLL()
# s2.insert_in_last(1)
# s2.insert_in_last(2)
# s2.insert_in_last(4)

s1.insert_in_last(4)
s1.insert_in_last(1)
s1.insert_in_last(2)

s1.print_all()

# merge(s1, s2)
# s1.print_all()
lp = merge_sort(s1)

lp.print_all()
# print(lp)
