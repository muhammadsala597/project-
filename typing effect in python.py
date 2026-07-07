import time
s = input("Enter your input:")
for i in s:
    if i in "?!.":
        print(i, end="")
        time.sleep(0.5)
    elif i in ",":
        print(i, end="")
        time.sleep(0.2)
    else:
        print(i, end="")
        time.sleep(0.04)