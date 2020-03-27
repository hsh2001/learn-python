print("0 + 1 =", 0 + 1)  # 더하기
print("2 - 1 =", 2 - 1)  # 빼기
print("2 * 2 =", 2 * 2)  # 곱하기
print("6 / 2 =", 6 / 2)  # 나누기

print("3 ** 5 =", 3 ** 5)  # n제곱
print("7 // 2 =", 7 // 2)  # 몫
print("7 % 2 =", 7 % 2)  # 나머지

a = 0
a += 1  # a = a + 1과 동치
print("a =", a)

a -= 1  # a = a - 1과 동치
print("a =", a)

a = 5
b = 10

a += 1
b -= 3

a += b
print("a =", a)  # 13
print("b =", b)  # 7

print(float(10))  # 실수형 변환
print(int(10.3))  # 정수형 변환

print(1 == True)
print(0 == False)
print(1 == False)
print(0 == True)

a = '76.3'
b = float(a)

# print(a + b) => ERROR! 문자열과 실수(또는 정수)끼리의 덧셈 연산은 불가능

b = str(a)
print(a + b)  # (=76.376.3) 문자와 문자의 덧셈은 문자의 붙이기

age = 20.5
age = str(int(age))
print("만 " + age + '세 생일을 "미리" 축하합니다!')
