def count_sort(arr):
    m=max(arr)
    count=[0]*(m+1)
    output=[0]*len(arr)

    for i in range(len(arr)):
        count[arr[i]]+=1
    
    for i in range(1,m+1):
        count[i]+=count[i-1]
    
    for i in range(len(arr)-1,-1,-1):
        output[count[arr[i]]-1]=arr[i]
        count[arr[i]]-=1

    return output

arr=list(map(int,input("Enter elements separated by spaces:").split()))
print(count_sort(arr))