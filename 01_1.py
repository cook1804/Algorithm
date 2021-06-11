# 세 정수의 최댓값 구하기

print('세 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))   #input함수는 문자열을 반환한다. int 를 써주면 숫자는 정수로 바뀐다. type conversion(형 변환) str -> int
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

maximum = a                 # maximum에 a 값을 대입
if b > maximum: maximum = b # b 가 maximum 보다 크면 maximum 에 b 값을 대입
if c > maximum: maximum = c 

print(f'최댓값은 {maximum}입니다.')





