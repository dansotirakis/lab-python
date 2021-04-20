a = int(input())
b = int(input())
c = int(input())
s = (a + b + c) == 180
valid = "The triangle is valid!"
not_valid = "The triangle is not valid!"

if s:
    print(valid)
else:
    print(not_valid)
