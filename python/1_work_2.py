from typing import List
print('-----------------------')
def zero_index(data):
    print('----------')
    result_list = [1000000]*len(data)
    print(data)
    index_zero = [i for i in range(len(data)) if data[i] == 0]
    print(index_zero)
    n = 1
    for i in range(0,len(data)):
        dist_ind = data[i]
        if int(dist_ind) == 0:
            zero_index = i
    for i in range(zero_index+1,len(data)):
        result_list[i] = n
        n = n + 1
    n=1
    for i in range(zero_index-1,-1,-1):
        result_list[i] = n
        n = n + 1
    return result_list


def read_input() -> List[int]:
    num_list = list(map(int, input().strip().split()))
    return num_list

str_list = read_input()
print(zero_index(str_list))

# # print('zero_index(1 0 9 4 8 3)')
# dist_str = '1 0 9 4 8 3 1 0 9 4 8 3 1 0 9 4 8 3'
# dist_list = dist_str.split(' ')
# dist = list(map(int, dist_list))
# print(zero_index(dist))

# # print('zero_index(5 0 9 0 8 2)')
# dist_str = '5 0 9 0 8 2 5 0 9 0 8 2 5 0 9 0 8 2'
# dist_list = dist_str.split(' ')
# dist = list(map(int, dist_list))
# print(zero_index(dist))

# # print('zero_index(2 1 4 9 0 5)')
# dist_str = '2 1 4 9 0 5 2 1 4 9 0 5 2 1 4 9 0 5'
# dist_list = dist_str.split(' ')
# dist = list(map(int, dist_list))
# print(zero_index(dist))

# 0 7 9 4 8 3
# 5 0 9 0 8 2
# 5 7 9 0 8 2
# 2 1 4 9 0 5