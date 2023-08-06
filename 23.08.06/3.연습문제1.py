# %%
def minimum(list):
    result_num = 0
    
    
    for i in range(len(list)):
        if len(list) == 1:
            break
        
        list.sort()
        a=list.pop(0)
        b=list.pop(0)
        result_num +=a+b
        list.append(a+b)
        
    print(f"최종적으로 나오는 값은{result_num}입니다.")

minimum([1,2,3,4,5,6,7,8])