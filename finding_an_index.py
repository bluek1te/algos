def solution(A):
    L = 0
    R = len(A)-1
    i = 0
    while(True):
        if i == (L+R) // 2:
            return "no"
        i = (L+R) // 2
        print(i)
        print(2*i+5)
        if A[i] == 2 * i + 5:
            return "yes"
        elif A[i] < 2 * i + 5:
            L = i+1
        elif A[i] > 2 * i + 5:
            R = i
        
print(solution([1, 3, 7, 9, 13]))