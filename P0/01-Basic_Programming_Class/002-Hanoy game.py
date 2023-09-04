def hanoy(n, fir, fin, temp):
    print(n)
    print(fir, fin)
    if n == 1:
        print("Move disk from {0} to {1}".format(fir, fin))
    else:
        hanoy(n - 1, fir, temp, fin)
        hanoy(1, fir, fin, temp)
        hanoy(n - 1, temp, fin, fir)


n = 3

hanoy(n, "A", "C", "B")
