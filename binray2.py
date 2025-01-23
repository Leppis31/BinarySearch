#binary search

def binraySearch(arr, target):
    low = 0 
    high = len(arr)-1
    while low <= high:
        mid = low + (high -low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]< target:
            low = mid + 1
        else:
            high = mid -1
    return -1

def runTest(): 
    array = [1,5,8,10,50,75]
    target = 8
    result = binraySearch(array,target)
    if result != -1:
        print("löytyy: ", result+1)
    else:
        print("ei löydy")

if __name__ == "__main__":
    runTest()