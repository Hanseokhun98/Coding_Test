#%%
from itertools import combinations
from copy import deepcopy

def find_min_sums(nums, prev_sum=0):
    # Base case: only two numbers left in the list
    if len(nums) == 2:
        return [prev_sum + nums[0] + nums[1]]
    
    sums = []
    # Find all combinations of 2 numbers
    for pair in combinations(nums, 2):
        new_nums = deepcopy(nums)  # Make a copy of the list
        new_nums.remove(pair[0])  # Remove the two numbers from the list
        new_nums.remove(pair[1])
        new_nums.append(sum(pair))  # Add the sum to the list
        # Recursive call with the new list and the updated sum
        sums.extend(find_min_sums(new_nums, prev_sum + sum(pair)))
    return sums

list_ex = [1,2,3,4,5,6,7,8]
list_sum = find_min_sums(list_ex)
print(f"경우의 수는 {len(list_sum)} 입니다.")
print(f"이 중 최솟값은 {min(list_sum)} 입니다.")

# %%
"""
1. 리스트 길이가 3일때 [a1,a2,a3]
경우의 수: 3 
2. 리스트 길이가 4일때 [a1,a2,a3,a4]
경우의 수: 18 (6*3)
3. 리스트 길이가 5일때 [a1,a2,a3,a4,a5]
경우의 수: 180 (10*18)
4. 리스트 길이가 6일때 [a1,a2,a3,a4,a5,a6]
경우의 수: 2700 (15*180)
5. 리스트 길이가 7일때 [a1,a2,a3,a4,a5,a6,a7]
경우의 수: 56700 (21*2700)
"""