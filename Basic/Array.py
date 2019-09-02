

"""Sum of array"""


def _sum(arr):
    return sum(arr)


def splitarr(arr, d):
    for i in range(d):
        new_arr = arr
        x = arr.pop(0)
        new_arr.append(x)
        print(new_arr)


def largest(arr, d):
     large = arr[0]
     for i in range(0, d):
         if arr[i] > large:
             large = arr[i]
     print(large)


if __name__ == '__main__':
    arr = [6, 2, 3, 4, 5,90,88]
    # splitarr(arr, 2)
    n = len(arr)
    largest(arr, n)

