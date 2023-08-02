def search_algo(num, items):
    for item in items:
        if item == num:
            return True
        else:
            pass

nums = [2,4,6,8,10]

print(search_algo(2, nums))  
# 일반적으로 알고리즘의 복잡도를 다루는 경우, 최악의 복잡도를 말함
# 최상의 경우: O(1), 최악의 경우: O(n)