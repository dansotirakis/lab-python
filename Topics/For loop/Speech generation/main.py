def switch_speech(argument):
    switcher = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        0: "zero"
    }
    print(switcher.get(argument, "Invalid month"))


value = input()
res = [int(x) for x in str(value)]
for i in res:
    switch_speech(i)
