# neighbour_table_list = {["A",4],["B",3]}
# print(neighbour_table_list[1][1])


example_list = [['3', 'A'], ['1', 'C'], ['2', 'B']]
sorted_example_list = sorted(example_list, key=lambda x: x[1])
print(sorted_example_list)


example_list = [['3', 'A'], ['1', 'C'], ['2', 'B']]
sorted_example_list = sorted(example_list)
print(sorted_example_list)

example_list = [['1', 'A'], ['1', 'C'], ['1', 'B']]
sorted_example_list = sorted(example_list)
print(sorted_example_list)


#sorted method is smart in python. If the 0th index is already sorted in the nested list, then
#the method will sort the next index.
#you can specify the index to be sorted by using this sorted(example_list, key=lambda x: x[1])