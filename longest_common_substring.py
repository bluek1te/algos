from pandas import DataFrame
from numpy import amax

def solution(X: str, Y: str) -> int:
    I = len(X)
    J = len(Y)
    T = [[0 for j in range(J)] for i in range(I)]
    for i in range(0, I):
        for j in range(0, J):
            if X[i] == Y[j]:
                T[i][j] = T[i-1][j-1] + 1
    return amax(T)

assert(solution("test", "test_str") == 4)
assert(solution("omaewamou", "sofwamouas") == 5)
