# find the smallest value of the convex array ( which first decreases and then increases)
# sample data = [ 10,9,8,6.5,4.1,3.2,2,4,4.5,6]
def find_smallest_value(arr):
    left=0
    right=len(arr)-1
    print( "RIGHT =" ,right)
    while left<right:
        mid=(left+right)//2
        print("mid=" , mid)
        if arr[mid]<arr[mid+1] and arr[mid]<arr[mid-1]:
            return arr[mid]
        elif arr[mid]>arr[mid+1]:
            left=mid+1
            print("left=" ,left)
        else:
            right= mid-1
            print(right)
    return arr[left]

print(find_smallest_value([10,9,8,6.5,4.1,3.2,2,4,4.5,6]))

