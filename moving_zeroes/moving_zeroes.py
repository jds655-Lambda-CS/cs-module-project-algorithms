'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    zarr = []
    narr = []
    for index, element in enumerate(arr):
        if element == 0:
            zarr.append(element)
        else:
            narr.append(element)
    return narr + zarr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    # arr = [0, 3, 1, 0, -2]
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")