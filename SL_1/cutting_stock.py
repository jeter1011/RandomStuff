import knapsack
import math
import itertools



def max_num_len(list1, list2):
    """list 1: list of lengths
        list2: list of raw material lengths
    """
    total_length = sum(list2)
    upper_lim = []

    for len in list1:
        upper_lim.append(math.floor(total_length/len))

    return upper_lim



blanks = [{"len": 92, "count": 60},{"len": 72, "count": 90},{"len": 66, "count": 120}]
materials = [{"rod": 330},{"rod": 350},{"rod": 430}]

list_of_len = []
list_of_rods = []

for lengths in blanks:
    list_of_len.append(lengths["len"])

for rods in materials:
    list_of_rods.append(rods["rod"])


upper_limit = max_num_len(list_of_len,list_of_rods)


iteration_nestlist =[]

for i in range(0,3):
   iteration_nestlist.append([list_of_len[i]]*upper_limit[i])

flatten = itertools.chain.from_iterable
iteration_list = list(flatten(iteration_nestlist))

print(iteration_list)



