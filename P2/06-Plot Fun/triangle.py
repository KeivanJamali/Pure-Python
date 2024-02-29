import matplotlib.pyplot as plt

x = []
y = []
scale = 1000
change = 0.1

mx1 = 100
my1 = 100

mx2 = 100
my2 = 100

mx3 = 100
my3 = 100

for r in range(1, 3):
    for i in range(int(scale / (3 ** r))):
        x.append(mx1)
        y.append(my1)

        my1 = my1 + change

        x.append(mx2)
        y.append(my2)

        mx2 = mx2 + (change / (2 ** 0.5))
        my2 = my2 - (change / (2 ** 0.5))

        x.append(mx3)
        y.append(my3)

        mx3 = mx3 - (change / (2 ** 0.5))
        my3 = my3 - (change / (2 ** 0.5))

    mx1 = 100
    my1 = 100 + change * int(scale / (3 ** r))

    mx2 = 100
    my2 = 100 + change * int(scale / (3 ** r))

    mx3 = 100
    my3 = 100 + change * int(scale / (3 ** r))

print(len(x), len(y))

plt.scatter(x, y)
plt.show()
