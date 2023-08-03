# O(n^2 -n)
# 이게 왜 시간복잡도가 n^2 - n 일까?
def func(nums: list):
    for num1 in nums:
        for num2 in nums:
            if num1 != num2 :
                print(num1, num2)
                
