h, b, c, s = map(int, input().split())
wav = h*b*c/8/1024/1024
mb = wav * s
print("%.1f" % mb, "MB")
