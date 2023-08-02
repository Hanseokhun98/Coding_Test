# 1. 문자 개수 세기 (count)
a = 'hobby'
a.count('b')

# 2. 위치 알려 주기 (find)
a = 'Python is the best choice'
a.find('b') # 인덱스 위치
a.find('k') # 문자값이 없는 경우 -1 반환 

# 3. 위치 알려 주기 (index)
a = 'Life is too short'
a.index('t')
a.index('k') # find 와는 다르게 문자열에 존재하지 않으면 오류 뱉음

# 4. 문자열 삽입 (join)
",".join('abcd')
# 실행결과 : a,b,c,d

",".join(['a','b','c','d'])
# 실행결과 : a,b,c,d

# 5. 소문자를 대문자로 바꾸기 (upper)
a = 'hi'
a.upper() # 'HI'

# 6. 대문자를 소문자로 바꾸기 (lower)
a = 'HI'
a.lower() # 'hi'