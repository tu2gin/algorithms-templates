from typing import List, Tuple

def moving_average(timeseries, K):
    result = []  # Пустой массив.
    # Первый раз вычисляем значение честно и сохраняем результат.
    current_sum = sum(timeseries[0:K])
    result.append(current_sum / K)
    for i in range(0, len(timeseries) - K):
        current_sum -= timeseries[i]
        current_sum += timeseries[i+K]
        current_avg = current_sum / K
        result.append(current_avg)
    return result

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size

arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))




# В первой строке передаётся натуральное число n, количество секунд, 
# в течение которых велись измерения. 1 ≤ n ≤ 105
#  
# Во второй строке через пробел записаны n целых неотрицательных чисел qi,
#  каждое лежит в диапазоне от 0 до 103.
#  
# В третьей строке записано натуральное число k (1 ≤ k ≤ n) —– окно сглаживания.
 
# Ввод
# 7
# 1 2 3 4 5 6 7
# 4
#  
# Вывод
# 2.5 3.5 4.5 5.5
