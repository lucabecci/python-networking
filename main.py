n = int(input(("Please insert your number: ")))
arr = []

for x in range(0, 100):
    arr.append(x)

for i in arr:
    if i == n:
        print("Your number:", i, "===", n)
        break
    continue