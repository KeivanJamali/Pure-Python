while True:
    try:
        data = input().split(" ")
        data = [int(i) for i in data]
    except:
        break

    if data[1] < data[3]:
        print("YES")
    elif data[0] + data[2] < data[3]:
        print("YES")
    elif data[3] == data[1]:
        if data[0] < data[3] and data[2] < data[3]:
            print("YES")
        elif data[0] + data[2] < 2 * data[3]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
