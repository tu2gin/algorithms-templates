from typing import List, Tuple

def zipper(a: List[int], b: List[int]) -> List[int]:
    # Здесь реализация вашего решения
    result = ''
    for i in range(len(a)):
        result = result + str(a[i]) + str(b[i])
    return result
    

def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b

a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
