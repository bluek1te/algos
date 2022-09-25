from typing import List

def solution(m: List[int], p: List[int], k: int) -> int:
    n = len(m)
    a = [0] * n
    for i in range(1, n):
        a[i] = p[i]
        for j in range(1, i):
            if a[j] + p[i] > a[i] and i - j > k:
                a[i] = a[j] + p[i]

    return max(a)

test_input_m = [0, 4, 5, 7, 10]
test_input_p = [100, 200, 100, 500, 300]
test_k = 2

print(solution(test_input_m, test_input_p, test_k))