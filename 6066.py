a, b, c = map(int, input().split())
lst = [a, b, c]
for i in lst:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")
