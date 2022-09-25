from typing import List

def solution(x: List[int], v: int) -> bool:
    T = [0] * (v+1)
    n = len(x)
    for j in range(1, v+1):
        for i in range(0, n):
            if x[i] <= j:
                T[j] = max(T[j], T[j-x[i]] + x[i])
    return T[v] == v

test_case_1_x = [5, 10]
test_case_1_v = 15

test_case_2_x = [5, 10]
test_case_2_v = 12

test_case_3_x = [1]
test_case_3_v = 10

assert(solution(test_case_1_x, test_case_1_v) == True)
assert(solution(test_case_2_x, test_case_2_v) == False)
assert(solution(test_case_3_x, test_case_3_v) == True)