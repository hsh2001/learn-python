colors = ["빨", "주", "노", "초", "파", "남", "보"]

print(colors[1])
print(colors[3])
print(len(colors))

week = ["월", "화", "수", "목", "금", "토", "일"]
print("주중:", week[:5])
print("주말:", week[5:])
print("프로그래밍기초1(11분반):", [week[2], week[4]])

print(week[::-1])

print([1, 2, 3, 4, 5] + [9, 10, 11, 22])
print([1, 2, 3] * 3)
print(2 in [1, 2, 3])
print(100 in [1, 2, 3])

colors.append('하양')
print(colors)

colors.extend(['검정', '회색'])
print(colors)

colors.insert(2, '갈색')
print(colors)

colors.remove('주')
print(colors)

del colors[0]
print(colors)
