import enchant
d = enchant.Dict("en_US")

def solution(S: str) -> bool:
    n = len(S) + 1
    T = [False] * n
    T[0] = True
    for i in range(1, n):
        T[i] = False
        for j in range(1, i):
            T[i] = T[i] or (T[j-1] and d.check(S[j:i]) and len(S[j:i]) >= 2)
    return T[n-1]

test_case_1 = "thisisarealstring"
test_case_2 = "gabbadsnotstrin- -gsaddfsdf"

assert(solution(test_case_1) == True)
assert(solution(test_case_2) == False)
