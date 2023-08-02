# 공간 복잡도: 프로그램 실행 중에 메모리에 할당해야 하는 공간의 크기를 나타내는 공간 복잡성

def return_squares(n):
    square_list = []
    for num in n:
        square_list.append(num*num)
        
    return square_list

nums = [2,4,6,8,10]
print(return_squares(nums))

# 정답: 공간복잡도 O(n)