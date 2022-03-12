a = int(input())
b = 0
for i in range(a):
    b += 1
    if b % 10 == 3 or b % 10 == 6 or b % 10 == 9:
        print("X", end=" ")
    else:
        print(b, end=" ")
