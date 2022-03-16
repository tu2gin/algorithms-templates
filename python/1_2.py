# pip install numpy
import numpy as np

def func(lst):
    lst=np.array(list(map(int, lst.split())))
    zeros = np.where(lst==0)[0]
    for i in np.nonzero(lst)[0]:
        lst[i] = min(np.abs(i-zeros))
    return lst.tolist()