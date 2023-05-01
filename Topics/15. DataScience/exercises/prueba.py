import matplotlib.pyplot as plt

numbers = {4.0: 4, 5.0: 2, 8.0: 1, 3.0: 1, 667.0: 2}

labels = [str(key) for key in numbers.keys()]
values = list(numbers.values())
keys = list(numbers.keys())

plt.bar(labels, values)

plt.xticks(labels)
plt.xlim(-0.5, len(keys) - 0.5)

plt.show()

a = 10