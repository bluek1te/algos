from typing import List

def solution(nums: List[int]) -> int:
    n = len(nums)
    l = [0] * n
    for i in range(0, n):
        for j in range(0, i):
            if nums[j] < nums[i] and l[j] + nums[i] > l[i]:
                l[i] = l[j] + nums[i]
    
    return max(l)

test_input_0 = [5, 15, -30, 10, -5, 40, 10]

print(solution(test_input_0))