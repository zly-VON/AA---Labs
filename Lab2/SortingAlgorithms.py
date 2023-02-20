import time
import matplotlib.pyplot as plt
from listGenerator import genRandomList
from prettytable import PrettyTable

time_table1 = []
time_table2 = []
time_table3 = []
time_table4 = []


def quickSort(array):
	if len(array) <= 1:
		return array

	pivot = array[len(array) // 2]

	left = [x for x in array if x < pivot]
	middle = [x for x in array if x == pivot]
	right = [x for x in array if x > pivot]

	return quickSort(left) + middle + quickSort(right)


def quickArray(data):
	start_time = time.perf_counter()
	quickSort(data)
	time_table1.append(time.perf_counter() - start_time)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, i, n)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i)


def max_heapify(arr, i, n):
	largest = i
	left = 2 * i + 1
	right = 2 * i + 2

	if left < n and arr[left] > arr[largest]:
		largest = left
	if right < n and arr[right] > arr[largest]:
		largest = right

	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		max_heapify(arr, largest, n)


def heapArray(data):
	start_time = time.perf_counter()
	heapSort(data)
	time_table2.append(time.perf_counter() - start_time)


def mergeSort(array):
	if len(array) > 1:
		mid = len(array)//2
		left_list = array[:mid]
		right_list = array[mid:]
		mergeSort(left_list)
		mergeSort(right_list)

		i = j = k = 0

		while i < len(left_list) and j < len(right_list):
			if left_list[i] <= right_list[j]:
				array[k] = left_list[i]
				i += 1
			else:
				array[k] = right_list[j]
				j += 1
			k += 1

		while i < len(left_list):
			array[k] = left_list[i]
			i += 1
			k += 1

		while j < len(right_list):
			array[k] = right_list[j]
			j += 1
			k += 1


def mergeArray(data):
	start_time = time.perf_counter()
	mergeSort(data)
	time_table3.append(time.perf_counter() - start_time)


def selectionSort(arr):
	n = len(arr)
	for i in range(n):
		min_index = i
		for j in range(i + 1, n):
			if arr[j] < arr[min_index]:
				min_index = j
		arr[i], arr[min_index] = arr[min_index], arr[i]


def selectionArray(data):
	start_time = time.perf_counter()
	selectionSort(data)
	time_table4.append(time.perf_counter() - start_time)


n = [10, 100, 1000, 10000, 25000, 50000, 75000, 100000, 250000, 500000]
n2 = [10, 100, 1000, 10000, 25000]
for i in range(len(n)):
	list4 = list3 = list2 = list1 = genRandomList(n[i])

	quickArray(list1)
	heapArray(list2)
	mergeArray(list3)
	if i < len(n2): selectionArray(list4)

myTable = PrettyTable(["Algorithm", "10", "100", "1000", "10000", "50000", "100000", "500000"])
myTable.add_row(["quickSort", time_table1[0], time_table1[1], time_table1[2], time_table1[3], time_table1[5],
				time_table1[7], time_table1[9]])
myTable.add_row(["heapSort", time_table2[0], time_table2[1], time_table2[2], time_table2[3],time_table2[5],
				time_table2[7], time_table2[9]])
myTable.add_row(["mergeSort", time_table3[0], time_table3[1], time_table3[2], time_table3[3],time_table3[5],
				time_table3[7], time_table3[9]])
myTable.add_row(["selectionSort", time_table4[0], time_table4[1], time_table4[2], time_table4[3], "x",
				"x", "x"])
print(myTable)

plt.plot(n, time_table1, label="quickSort")
plt.plot(n, time_table2, label="heapSort")
plt.plot(n, time_table3, label="mergeSort")
plt.plot(n2, time_table4, label="selectionSort")
plt.ylabel('Time (s)')
plt.xlabel('n-terms Array')
plt.title('Sorting Algorithms')
plt.legend()
plt.show()

