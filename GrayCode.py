# Gray code generation for laplace expansion module for Boson sampling simulation
# Author: Edmund Dable-Heath
#
# The gray code needs to be generated for the space {-1,1}^n and the first element is required to be 1
# Ideally this check a look up table and if it doesn't find the Gray code already generated it will generate it
#
# First pass: Manually enter Gray code

# For Gray code gen
def GrayCode(n):
    n = n - 1
    if n <= 0:
        return
    arr = [[1], [-1]]
    i = 2
    while True:
        if i >= 1 << n:
            break
        for j in range(i - 1, -1, -1):
            arr.append(arr[j])
        for j in range(i):
            arr[j] = [1] + arr[j]
        for j in range(i, 2*i):
            arr[j] = [-1] + arr[j]
        i = i << 1
    for k in range(len(arr)):
        arr[k] = [1] + arr[k]
    return arr


# Gray Codes
GC_1 = [[1]]

GC_2 = [[1, 1],
        [1, -1]]

GC_3 = [[1, 1, 1],
        [1, 1, -1],
        [1, -1, -1],
        [1, -1, 1]]

GC_4 = [[1, 1, 1, 1],
        [1, 1, 1, -1],
        [1, 1, -1, -1],
        [1, 1, -1, 1],
        [1, -1, -1, 1],
        [1, -1, -1, -1],
        [1, -1, 1, -1],
        [1, -1, 1, 1]]

GC_5 = [[1, 1, 1, 1, 1],
        [1, 1, 1, 1, -1],
        [1, 1, 1, -1, -1],
        [1, 1, 1, -1, 1],
        [1, 1, -1, -1, 1],
        [1, 1, -1, -1, -1],
        [1, 1, -1, 1, -1],
        [1, 1, -1, 1, 1],
        [1, -1, -1, 1, 1],
        [1, -1, -1, 1, -1],
        [1, -1, -1, -1, -1],
        [1, -1, -1, -1, 1],
        [1, -1, 1, -1, 1],
        [1, -1, 1, -1, -1],
        [1, -1, 1, 1, -1],
        [1, -1, 1, 1, 1]]

GC_6 = [[1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, -1],
        [1, 1, 1, 1, -1, -1],
        [1, 1, 1, 1, -1, 1],
        [1, 1, 1, -1, -1, 1],
        [1, 1, 1, -1, -1, -1],
        [1, 1, 1, -1, 1, -1],
        [1, 1, 1, -1, 1, 1],
        [1, 1, -1, -1, 1, 1],
        [1, 1, -1, -1, 1, -1],
        [1, 1, -1, -1, -1, -1],
        [1, 1, -1, -1, -1, 1],
        [1, 1, -1, 1, -1, 1],
        [1, 1, -1, 1, -1, -1],
        [1, 1, -1, 1, 1, -1],
        [1, 1, -1, 1, 1, 1],
        [1, -1, -1, 1, 1, 1],
        [1, -1, -1, 1, 1, -1],
        [1, -1, -1, 1, -1, -1],
        [1, -1, -1, 1, -1, 1],
        [1, -1, -1, -1, -1, 1],
        [1, -1, -1, -1, -1, -1],
        [1, -1, -1, -1, 1, -1],
        [1, -1, -1, -1, 1, 1],
        [1, -1, 1, -1, 1, 1],
        [1, -1, 1, -1, 1, -1],
        [1, -1, 1, -1, -1, -1],
        [1, -1, 1, -1, -1, 1],
        [1, -1, 1, 1, -1, 1],
        [1, -1, 1, 1, -1, -1],
        [1, -1, 1, 1, 1, -1],
        [1, -1, 1, 1, 1, 1]]

# Look up library:

GrayCodes = {1: GC_1,
             2: GC_2,
             3: GC_3,
             4: GC_4,
             5: GC_5,
             6: GC_6}




