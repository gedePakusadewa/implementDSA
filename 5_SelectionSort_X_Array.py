class SelectionSort():
	def __init__(self, data=None):
		self.data = data

	def asc_sort(self):
		data = self.data
		min_idx = 0
		temp = 0
		len_data = len(data)

		for i in range(len_data):
			min_idx = i
			for j in range(i, len_data):
				if data[min_idx] > data[j]:
					min_idx = j

			if min_idx != i:
				temp = data[min_idx]
				data[min_idx] = data[i]
				data[i] = temp

	def print_(self):
		print(self.data)



t1 = SelectionSort([-2, 45, 0, 11, -9,88,-97,-202,47])
t1.asc_sort()
t1.print_()
