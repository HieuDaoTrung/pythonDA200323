a = list(map(int, input().rstrip().split()))

def mode(arr):
    arr = sorted(arr)
    print(arr)
    times = 1
    status = 1
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            status += 1
        else:
            if status > times:
                times = status
                mode = arr[i]
            status = 1
    return [mode, times]

print(mode(a))
