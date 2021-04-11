count = int(input())
objects = []
for _ in range(count):
    objects.append(int(input()))
print(sum(objects) / len(objects))
