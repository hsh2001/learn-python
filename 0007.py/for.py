for i in [1, 2, 3, 4, 5]:
    print(i)

print('----')
print(list(range(5)))
print('----')

for i in range(4):
    print(i)

print('----')

for i in range(10, 1, -1):
    print(i)

print('----')

i = 1
while i < 10:
    print(i)
    i += 1

print('----')

for i in range(10):
    if i == 5:
        continue
    print(i)


print('----')

for i in range(10):
    if i == 5:
        continue
    print(i)
else:
    print('end')

print('----')

dan = int(input("구구단 몇 단을 계산할까? "))

for i in range(1, 10):
    print(dan, 'x', i, '=', dan * i)

sentence = "gnidoc yojne I"
