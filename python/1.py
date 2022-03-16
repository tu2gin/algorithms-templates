from typing import List

def nearest_zero(distance: List[int]):
    zeros = [0] * len(distance)
    index_zeros = [i for i in range(len(distance)) if distance[i] == 0]
    for i in range(index_zeros[0], len(distance), +1):
        if distance[i] == 0:
            zeros[i] = 0
        else:
            zeros[i] = zeros[i-1] + 1
    for i in range(index_zeros[-1], index_zeros[0], -1):
        if distance[i] == 0:
            zeros[i] = 0
        else:
            zeros[i] = min(zeros[i], zeros[i + 1] + 1)
    for i in range(index_zeros[0] - 1, -1, -1):
        zeros[i] = zeros[i + 1] + 1
    return zeros


def read_input() -> List[int]:
    num_list = list(map(int, input().strip().split()))
    return num_list

str_list = read_input()
print(nearest_zero(str_list))