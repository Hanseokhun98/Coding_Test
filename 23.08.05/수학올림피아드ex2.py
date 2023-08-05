#%%
"""
------------------------------------------------------------------------------------------------------------------------------
문제2. (a1, a2, ... , an) 의 수열에서 임의의 두수를 뽑고 그 합을 X1 이라 할때
여기서 임의의 두 수를 a1, a2 라고 한다면 둘 중 큰 수를 X'1 이라고 하자 
최종출력값에는 이 X'1을 더하고 수열에는 X1을 더해서 해당과정을 반복한다.
그럼 결국 마지막은 X(n-1),a' 가 남고 이또한 마지막 과정에서 
둘 중 큰 수를 X'(n-1) 이라고 한다면 다음과 같은 식을 생각해 볼 수 있다. 
X'1 + X'2 + ... + X'(n-1) = Y 
이때 Y값이 최소가 되는 경우의 수를 찾아라
------------------------------------------------------------------------------------------------------------------------------
"""
# %%
def max_minimum (list):
    result_num = 0
    
    for list_length in range(len(list)):

        # list 안에 수열이 하나 남은 경우는 종료
        if len(list) == 1:
            print(f"최종적으로 수열에서 다음 규칙을 적용했을때 최솟값은 {result_num} 입니다.")
            break
        
        list.sort() #list안에 원소 오름차순으로 정렬하는 함수 
        prev_value1 = list[0] # 최솟값
        prev_value2 = list[1] # 두번째로 작은값
        result_num += prev_value2 # 결과값에 둘 중 큰 값 더하기
        
        print(f"{list_length+1}번째로 뽑은 수들은 ( {prev_value1}와 {prev_value2} )이고 결과값에 더할 수 는 {prev_value2} 입니다.)")
        
        del list[0:2] #해당값을 원래 list에서 삭제
        list.append(prev_value1 + prev_value2) #해당 리스트에 합한값을 추가
        list_length += 1 # 반복문을 위한 인자(1씩 올려줘야 다음단계로 넘어가서 위 코드를 수행할 수 있음)


# %%
# 예시1
ex1 = [4,7,13,19,21,24,33]
max_minimum(ex1)

# %%
