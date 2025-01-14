from typing import List

def zero_location(distance):
    distance_list =distance
    result_list = [0]*len(distance_list)
    n = 1
    zero_index = 1
    for i in range(0,len(distance_list)):
        dist_ind = distance_list[i]
        if int(dist_ind) == 0:
            zero_index = i
    for i in range(zero_index+1,len(distance_list)):
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
print(zero_location(str_list))

# print('zero_index(1 0 9 4 8 3)')
# dist_str = '1 0 9 4 8 3'
# dist = dist_str.split(' ')
# print(zero_index(dist))

# print('zero_index(5 7 9 0 8 2)')
# dist_str = '5 7 9 0 8 2'
# dist = dist_str.split(' ')
# print(zero_index(dist))

# print('zero_index(2 1 4 9 0 5)')
# dist_str = '2 1 4 9 0 5'
# dist = dist_str.split(' ')
# print(zero_index(dist))

# 0 7 9 4 8 3
# 5 7 9 0 8 2
# 2 1 4 9 0 5