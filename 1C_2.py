# 세 정수를 입력받아 중앙값 구하기 1

def med3(a,b,c):
    """ a,b,c 의 중앙값을 구하여 반환"""
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b


print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

print(f'중앙값은 {med3(a,b,c)}입니다. ')

# 세 정수를 입력받아 중앙값 구하기 2

# def med3(a,b,c):
#     """ a,b,c의 중앙값을 구하여 반환(다른 방법)"""       # 위의 방법보다 효율이 떨어짐. b >= a, b <=a a > b, a < b 를 일일이 썼음.  
#     if (b >= a and c <= a) or (b <= a and c >=a):     # if 문의 조건식이 성립하지 않으면(즉, 거짓이면) dldjwlsms elif 문은 이 판단을 수행할 필요가 없으므로 당연히 효율적이지 않음.
#         return a
#     elif (a > b and c < b) or (a < b and c > b):
#         return b
#     return c

