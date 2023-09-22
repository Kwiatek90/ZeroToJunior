from matplotlib import pyplot as plt

xs = [0, 1, 2, 3, 4]
y1 = [1, 2, 3, 4, 5]
y2 = [1, 2, 4, 8, 16]
plt.plot(xs, y1, "g-o", xs, y2, "b-^")
print(plt.show())