for i in range(1, 6):
    if i == 3:
        continue
    print(i)

for i in range(1, 6):
    if i == 2:
        continue
    elif i == 4:
        break
    else:
        print(i)