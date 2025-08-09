#
import numpy as np

#
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

#
def describe(var):
    str_var = namestr(var, globals())
    dtype_var = type(var)
    print(f'{str_var} = {var}, dtype = {dtype_var}')
    return

#
arr = np.zeros((2,4,11), dtype = int)
describe(arr)

#
starting_pos = (0,0,0)
print(starting_pos)
print(arr[starting_pos])
print(arr[0,0,10])
print(arr[0,1,0])
print(arr)

#
def fill_z_ones(arr):
    arr[0, 0, :] = 1
    return arr

#
arr1 = fill_z_ones(arr)
print(starting_pos)
print(arr1[starting_pos])
print(arr1[0,0,10])
print(arr1[0,1,0])
print(arr1)

#
def fill_n_z_ones(arr, n):
    arr[0, 0:n, :] = 1
    return arr

#
arr2 = arr
n_z_arrays = 2
arr2 = fill_n_z_ones(arr2, n_z_arrays)
print(starting_pos)
print(arr2[starting_pos])
print(arr2[0,0,10])
print(arr2[0,2,0])
print(arr2)

#
# Modifying starting position
print(f'starting_pos = {starting_pos}')

# Convert to list
temp = list(starting_pos)

# Modify index 1
temp[1] += n_z_arrays

# Convert back to tuple
starting_pos2 = tuple(temp)

print(f'starting_pos2 = {starting_pos2}')
print(arr2[starting_pos])
print(arr2[starting_pos2])

#
def fill_n_z_ones_pos(arr, n, starting_pos):
    temp = list(starting_pos)
    new_y = temp[1] + n
    
    arr[temp[0], temp[1]:new_y, :] = 1

    ending_list = [temp[0], new_y, 0]
    ending_pos = tuple(ending_list)
    
    return arr, ending_pos

#
arr3 = arr
n_z_arrays = 2
starting_pos = (0,0,0)
describe(n_z_arrays)
describe(starting_pos)

arr3, ending_pos = fill_n_z_ones_pos(arr3, n_z_arrays, starting_pos)
describe(ending_pos)
print(arr2[ending_pos])
print(arr2[0,0,10])
print(arr2[0,2,0])
describe(arr2)
