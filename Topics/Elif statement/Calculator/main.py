a = float(input())
b = float(input())
c = str(input())
div = ['/', '//', 'div', 'mod']

if c in div and b == 0.0:
    print(str("Division by 0!"))
else:
    if c == '+':
        print(str(a + b))
    elif c == '-':
        print(str(a - b))
    elif c == '*':
        print(str(a * b))
    elif c == 'pow':
        print(str(pow(a, b)))
    elif c == 'mod':
        print(str(a % b))
    elif c == 'div':
        print(str(a // b))
    else:
        print(a / b)
