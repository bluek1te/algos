from cmath import inf
from typing import List

def solution(a: List[int]) -> int:
    n = len(a)
    p = [0] * n
    p[0] = 0
    for i in range(1,n):
        p[i] = (200 - a[i])**2
        for j in range(1,i):
            if p[i] > p[j] + (200 - (a[i]-a[j]))**2:
                p[i] = p[j] + (200 - (a[i]-a[j]))**2
    return p[n-1]

test_input_0 = [0, 20, 200, 220, 430, 500]
print(solution(test_input_0))