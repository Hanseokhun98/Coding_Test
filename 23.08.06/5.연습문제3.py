# %%
def 랠리_최단거리(list):
    result_num = 0
    if len(list) < 3:
        print("모순")

    if min(list[0:3])==list[0]:
        x = list[0] #점검시간
        y = 0 #센터번호
        for j in range(y+1,len(list)):
            if y == len(list)-1:
                break
            for i in range(y+1,len(list)):
                if i > y+3:
                    break
                if x > list[i]:
                    x = list[i]
                    y=i
                    result_num += x
    if min(list[0:3])==list[1]:
        x = list[1]
        y = 1
        for j in range(y+1,len(list)):
            if y == len(list)-1:
                break
            for i in range(y+1,len(list)):
                if i > y+3:
                    break
                if x > list[i]:
                    x = list[i]
                    y=i
                    result_num += x
    if min(list[0:3])==list[2]:
        x = list[2]
        y = 2
        for j in range(y+1,len(list)):
            if y == len(list)-1:
                break
            for i in range(y+1,len(list)):
                if i > y+4:
                    break
                if min(y+1,y+2,y+3):
                    result_num += x
    print(f"랠리의 최종점검 시간의 최솟값은{result_num}이다.")
# %%
랠리_최단거리([3,4,1,7,8,4,1,2])
