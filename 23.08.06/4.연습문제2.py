# %%
def A공장에서_합금을_위한_비용(list):
    result_num = 0
    
    for i in range(len(list)):
        if len(list) == 1:
            break
        list.sort()
        a=list.pop(0)
        b=list.pop(0)
        c=max(a,b)
        print(f"{i+1}번째 시행했을 때 뽑은 수는 {a}, {b}이다.그 때 추가하는 숫자는 {c}이다.")

        result_num +=c
        list.append(a+b)
        
    print(f"최종적으로 나오는 값은{result_num}입니다.")

A공장에서_합금을_위한_비용([4,7,13,19,21,24,33])
# %%
