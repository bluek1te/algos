from pandas import DataFrame
def solution(n: int) -> int:
    T = [[0 for i in range(n)] for j in range(n)]
    T[0][0] = 1
    T[1][2] = 1
    T[2][1] = 1
    for i in range(1, n):
        for j in range(1, n):
            T[i][j] = T[i-1][j-2] + T[i-2][j-1]
    #print(DataFrame(T))

solution(19)