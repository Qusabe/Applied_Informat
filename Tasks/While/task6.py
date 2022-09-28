n = int(input())
fb1 = 1
fb2 = 1
fb_sum = 0
count = 1
while fb2 < n:
    fb_sum = fb1 + fb2
    fb1 = fb2
    fb2 = fb_sum
    count += 1
if fb2 == n:
    print(count+1)
else: print(-1)