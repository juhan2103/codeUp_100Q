result = 0
a, b, c = map(int, input().split())
result += a + b + c
avg = result/3
print(result, format(avg, ".2f"))
