def hello(): print("Hello!")


def pack(a, b, c):
    return [a, b, c]


def eat_lunch(first):
    if len(first) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(first)):
            if i == 0:
                print(f"First I eat {first[0]}")
        else:
            print(f"Next I eat {first[i]}")


hello()
print(pack("a", "b", "c"))
print(pack(1, 2, 3))
eat_lunch(["chicken", "rice", "brocolli", "juice"])
