def Insertion_Sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
    print(arr)

n = int(input("Enter number of elements: "))
arr = [int(input()) for i in range(n)]
Insertion_Sort(arr)