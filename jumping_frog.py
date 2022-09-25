def solution(n: int) -> int:
    T = [0] * (n+1)
    T[0] = 1
    for i in range(1, n+1):
        T[i] = T[i-1]
        if i > 4:
            T[i] += 1
    print(T)
    return T[n]

test_case_1 = 6


#1->2->3->4->5->6->7
#1->2->6->7
#1->5->6->7
#1->3->7