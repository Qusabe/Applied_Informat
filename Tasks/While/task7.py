n = int(input())
fb1 = 1
fb2 = 1
fb_sum = 0
i = 0
while i <n-2:
    fb_sum = fb1 + fb2
    fb1 = fb2
    fb2 = fb_sum
    i += 1
print(fb2)