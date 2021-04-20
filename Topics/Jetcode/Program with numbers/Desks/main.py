a = int(input())
b = int(input())
c = int(input())

ra = int(a // 2)
rb = int(b // 2)
rc = int(c // 2)

if a % 2 != 0:
    ra += 1
if b % 2 != 0:
    rb += 1
if c % 2 != 0:
    rc += 1

print(ra + rb + rc)
