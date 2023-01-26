import numpy as np

a = np.random.uniform(1, 20, 20)
print("Original array:")
print(a)

b = a.reshape(4, 5)
print("Reshaped array:")
print(b)

b[np.arange(len(b)), b.argmax(1)] = 0
print("Maximum value replaced by 0:")
print(b)
