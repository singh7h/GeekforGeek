
import array
# Function to left rotate arr[] of size n by d*/
def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)

    # Function to left Rotate arr[] of size n by 1*/


def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp



# utility function to print an array */
def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=" ")

    # Driver program to test above functions */

def muliptlearray(arr,n):
    mul =1
    for i in range(len(arr)):
        mul = mul * arr[i]
        print(mul)


def compressthestring(str):
    new_str  = set(str)
    oldstr = str
    newstr={}
    for i in new_str:
        print(i, oldstr.count(i))
        newstr.update({i: oldstr.count(i)})
    print("a{a}b{b}e{e}".format(**newstr))




arr = [1, 2, 3, 4, 5, 6, 7]
#leftRotate(arr, 2, 7)
#printArray(arr, 7)
#muliptlearray(arr,7)
#compressthestring("aaabbeeaaa")

def rotatearr(arr,d):
    for i in range(d):
        temp = arr.pop(0)
        arr.append(temp)
        print(arr)

rotatearr(arr,2)





