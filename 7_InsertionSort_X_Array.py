class Insertion():
	def __init__(self, data):
		self.data = data

	def asc_sort(self):
		print("source : ", self.data)
		data = self.data
		len_data = len(data)

		for idx in range(len_data):
			temp1 = idx 
			for jdx in range(idx, -1, -1):
				if data[temp1] < data[jdx]:
					temp = data[temp1]
					data[temp1] = data[jdx]
					data[jdx] = temp
					temp1 = jdx
				# print(data[temp1], jdx, idx, temp1)
 
			# print(self.data)
			# print("\n")

	def print_(self):
		print(self.data)

t1 = Insertion([73, 26, 99, 42, -52, 44, -33, 65, -53])
t1.asc_sort()
t1.print_()

# 1 2 3 4 5
# 
