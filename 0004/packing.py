t = [1, 2, 3]
a, b, c = t
print(t, a, b, c)

arr = [11, 22, 33, 44, 55]
arr[-1], arr[0] = arr[0], arr[-1]
print(arr)

A = [11, 22, 33, 44, 55]
A.append(A[0])
A.insert(0, A[-2])
del A[1]
del A[-2]
print(A)
