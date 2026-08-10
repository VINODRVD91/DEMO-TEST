import numpy as np

# Create a 5x5 array with random integers between 1 and 20
# Note: high=21 because the upper bound is exclusive in NumPy
array_5x5 = np.random.randint(1, 21, size=(5, 5))
print("Original 5x5 Array:\n", array_5x5)
