import random

random.seed(0)

def genRandomList(n):
	rand_list = []
	for i in range(n):
		rand_list.append(random.randint(-100000, 100000))
	return rand_list
