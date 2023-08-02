# O(n^2 -n)
def func(nums: list):
    for num1 in nums:
        for num2 in nums:
            if num1 != num2 :
                print(num1, num2)
                
