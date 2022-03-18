from typing import List

def zero_index(n, data):
    result_list = [n+1]*len(data)
    index_zero = [i for i in range(len(data)) if data[i] == 0]
    for ind_z in range(0,len(index_zero)):
        result_list[index_zero[ind_z]] = 0
        n_plus = 1
        for i in range(index_zero[ind_z]+1,len(data)):
            if result_list[i] > n_plus:
                result_list[i] = n_plus
                n_plus = n_plus + 1
            else:
                break
        n_minus = 1   
        for i in range(index_zero[ind_z]-1,-1,-1):
            if result_list[i] > n_minus:
                result_list[i] = n_minus
                n_minus = n_minus + 1
            else:
                break
    
    return result_list


def read_input() -> List[int]:
    n = int(input())
    num_list = list(map(int, input().strip().split()))
    return num_list , n

n, str_list = read_input()
print(" ".join(map(str, zero_index(str_list, n))))

# print('zero_index(1 0 9 4 8 3)')

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
# 2 0 4 9 0 5 2 0 4 9 0 5