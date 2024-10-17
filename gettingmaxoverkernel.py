

num_list = [3, 1, -2, -1, 5, 4]
k = 4
result=[]
sub_list = []
for element in num_list:
    sub_list.append(element)
    if len(sub_list) == k:
        result.append(max(sub_list))
        del sub_list[0] #indexing      
print(result)

#slicing
num_lists = [3, 1, -2, -1, 5, 4]
k1 = 2
start_indexs = list(range(0, len(num_lists)-k+1))
end_indexs = list(range(k, len(num_lists)+1))
results = []
for start_index, end_index in zip(start_indexs, end_indexs):
    sub_list = num_list[start_index : end_index]
    result.append(max(sub_list))
    
print(result)
