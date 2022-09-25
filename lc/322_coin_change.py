from cgi import test


from typing import List

class Solution:
    def coinChange(self, x: List[int], v: int) -> int:
        x.sort()
        T = [[]] * (v+1)
        n = len(x)
        for j in range(1, v+1):
            for i in range(0, n):
                if x[i] <= j:
                    new = sum(T[j - x[i]]) + x[i]
                    old = sum(T[j])
                    if new >= old:
                        tmp = T[j - x[i]].copy()
                        tmp.append(x[i])
                        T[j] = tmp
        print(T[6240:])
        print(sum())
        if sum(T[v]) == v:
            return len(T[v])
        else:
            return -1

test_case_1_x = [186,419,83,408]
test_case_1_v = 6249
solution = Solution()
solution.coinChange(test_case_1_x, test_case_1_v)