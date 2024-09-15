n=int(input("Enter number of elements: "))
li=[input() for i in range(n)]
find=(input("Enter element to find: "))
flag=True
for i in li:
    if find==i:
        print("Element found")
        flag=False
        break
if (flag==False):
    print("Element not found")
