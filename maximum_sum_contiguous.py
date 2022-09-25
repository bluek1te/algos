# Algorithms 6.1

def solution(S: list) -> int:
    n = len(S)
    T = [0] * n
    T[0] = S[0]
    for i in range(1, n):
        T[i] = max(T[i-1], 0) + S[i]
    return max(T)

test_case_1 = [5, 15, -30, 10, -5, 25, 10]
assert(solution(test_case_1) == 40)