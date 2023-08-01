# O(n^2), 이차식복잡도
def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, '' , item2)

quadratic_algo([4,5,6,8])

# O(log(n)), 로그복잡도
# 이진 검색은 대표적인 로그 복잡도 알고리즘
# 이진 검색 : 배열의 중간 지점의 원소를 검사하고, 
#             원하는 값이 없는 절반을 제외한 나머지에 대해서 다시 원하는 값을 찾음.
