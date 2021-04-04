order = int(input())

if order < 1:
    print("no army")
elif order <= 9:
    print("few")
elif order <= 49:
    print("pack")
elif order <= 499:
    print("horde")
elif order <= 999:
    print("swarm")
elif order >= 1000:
    print("legion")
