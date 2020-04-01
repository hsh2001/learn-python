name = input('Enter your name: ')
print(name + ', Welcome!')

print("본 프로그램은 섭씨온도를 화씨온도로 변환하는 프로그램입니다")
data = input("변환하고 싶은 섭씨온도를 입력하세요.")
temperature = (float(data) * 1.8) + 32
print("섭씨온도:", data)
print("화씨온도:", temperature)
