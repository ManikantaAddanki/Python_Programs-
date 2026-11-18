#binary search
arr = [12, 25, 18, 23, 45, 67, 80]
target = 45

arr.sort()

low = 0
high = len(arr) - 1
found = -1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        found = mid
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if found != -1:
    print(f"Found at sorted index: {found}")
else:
    print("Not found")

# o/p:first occurance at index 1
# last occurance at index 3   
list =[1,2,2,2,3,4,5]
target=2
first = -1 
last = -1
for x in range(len(list)):
    if list[x]==target:
        if first==-1:
            first=x
            last=x
print(first)
print(last)

#3
l=[1,2,3,4,5,7]
for n in range(1,8):
    if n not in l:
        print(n,"missing")


#bubblesort
array=[8,6,9,3,1,5,2]
for a in range(len(array)-1):
    for b in range(len(array)-a-1):
        if array[b]>array[b+1]:
            array[b],array[b+1]=array[b+1],array[b]
print(arr)



