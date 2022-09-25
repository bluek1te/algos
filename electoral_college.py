from typing import List
from pandas import DataFrame
import math

def solution(P: List[int], V: List[int], Z: int) -> int:
    n = len(P)
    T = [[0 for _ in range(Z+1)] for _ in range(n+1)]
    T[0][0] = 0
    for j in range(1, Z+1):
        T[0][j] = math.inf
    for i in range(1, n+1):
        for j in range(Z+1):
            if j >= V[i-1]:
                T[i][j] = min(T[i-1][j], T[i-1][j - V[i-1]] + P[i-1])
            else:
                T[i][j] = min(T[i-1][j], T[i-1][0] + P[i-1])
    return T[n][Z]

test_case_1_p = [200, 100, 30, 700, 250]
test_case_1_v = [5, 1, 2, 7, 6]
test_case_1_z = 12
#solution(test_case_1_p, test_case_1_v, test_case_1_z)

#test_case_2_p = [1,2,3,4,5]
#test_case_2_v = [4,2,1,4,3] #14
#test_case_2_z = 10

for i in range(1, 22):
    print(solution(test_case_1_p, test_case_1_v, i))