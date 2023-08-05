#%%
from itertools import combinations
from copy import deepcopy

def find_min_sums(nums, prev_sum=0):
    # Base case: only two numbers left in the list
    if len(nums) == 2:
        return [prev_sum + max(nums)]
    
    sums = []
    # Find all combinations of 2 numbers
    for pair in combinations(nums, 2):
        new_nums = deepcopy(nums)  # Make a copy of the list
        new_nums.remove(pair[0])  # Remove the two numbers from the list
        new_nums.remove(pair[1])
        new_nums.append(sum(pair))  # Add the sum of pair to the list
        # Recursive call with the new list and the updated sum
        sums.extend(find_min_sums(new_nums, prev_sum + max(pair)))
    return sums

list_ex = [4,7,13,19,21,24,33]
list_sum = find_min_sums(list_ex)
print(f"경우의 수는 {len(list_sum)} 입니다.")
print(f"이 중 최솟값은 {min(list_sum)} 입니다.")
# %%
