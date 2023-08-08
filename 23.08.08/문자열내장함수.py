# %%
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
# %%
# 1. 왼쪽 공백 지우기 (lstrip), 오른쪽 공백 지우기(rstrip), 양쪽 공백 지우기(strip)
a = " hi"
a.lstrip()

# 2. 문자열 바꾸기(replace)
a = "Life is too short" 
a.replace("Life","Your leg")

string = "Butter"
print(string.replace("t","m"))
print(string.replace("t","m",1)) #몇 번 지울지 세번째 파라미터로 지정 가능

# 3. 문자열 나누기(split)
a = "Life is too short"
a.split()

b = "a:b:c:d"
b.split(':') #괄호안의 값을 구분자로 나눌 수 도 있음

# 4. 문자가 숫자인지 검사
s = "2023"
print(s.isdigit()) #True 반환, 모두 숫자일 경우

# 코딩테스트에서는 주로 문자열의 문자 한 개가 숫자인지를 검사하는 데 자주 사용
s = "4 July"
for char in s:
    print(char.isdigit(), end='')

# True False Fasle False False False

# isdigit : 문자열의 모양이 숫자처럼 생겼다면 숫자로 변환
# isnumeric : isdigit + 로마숫자 변환
# isdecimal : 정수 형태의 10진수 변환

# 5. 문자가 알파벳/한글 또는 숫자인지 검사(isalnum)

s = "안녕, Python3"
for char in s:
    print(char.isalnum(), end='')

# True True False False True True True True True True True

# 6. 문자열을 아스키 코드값으로(ord), 아스키 코드값을 문자열로(chr)
char = 'A'
code_point = ord(char)
print(code_point) # 출력: 65

new_char = chr(code_point)
print(new_char) # 출력: A
