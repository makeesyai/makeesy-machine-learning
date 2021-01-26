import numpy as np

a = np.array([
    [[[1, 2, 3],
     [4, 5, 6]],
    [[7, 8, 9],
     [10, 11, 12]]],
    [[[13, 14, 15],
     [16, 17, 18]],
    [[19, 20, 21],
     [22, 23, 24]]],
    [[[130, 140, 150],
      [160, 170, 180]],
     [[190, 200, 210],
      [220, 230, 240]]],
    [[[1300, 1400, 1500],
      [1600, 1700, 1800]],
     [[1900, 2000, 2100],
      [2200, 2300, 2400]]]
])
print(a.shape)
print(a[0:4, 0:2, 0:1, 0:3])
# 0:4: iterates over outer dim
# 0:2: iterates over second dim
# 0:1: iterates over third dim
# 0:3: iterates over 4th dim (on each element of the rows)
