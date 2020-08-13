'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache={}):
    # base case
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        if n in cache.keys():
            return cache[n]
        else:
            # make 3 recursive calls
            value1 = eating_cookies(n - 1)
            cache[n - 1] = value1
            value2 = eating_cookies(n - 2)
            cache[n - 2] = value2
            value3 = eating_cookies(n - 3)
            cache[n - 3] = value3
            return value1 + value2 + value3


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 500

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
