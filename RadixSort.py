def count_sort(arr,digit):
    m=10
    count=[0]*(m)
    output=[0]*len(arr)

    for i in range(len(arr)):
        count[(arr[i]//digit)%10]+=1
    
    for i in range(1,m):
        count[i]+=count[i-1]
    
    for i in range(len(arr)-1,-1,-1):
        output[count[(arr[i]//digit)%10] -1]=arr[i]
        count[(arr[i]//digit)%10]-=1

    return output

def RadixSort(arr):
    max_val=max(arr)
    digit=1
    while(max_val//digit>0):
        arr=count_sort(arr,digit)
        digit*=10
    return arr

arr=[int(input()) for i in range (0,5)]
print(RadixSort(arr))

