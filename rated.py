def minimum(list1):
    # Initialize pointers for binary search
    l=0
    r= len(list1)-1
    # Binary search to find the minimum element
    while l<r:
        m=l+(r-l)//2
        # Check if the mid element is greater than the last element
        if list1[m]> list1[r]:
            l=m+1
        else:
            r=m
    return list1[l]

list1=[20 ,30, 4, 50, 60, 90, 2, 9]
print(minimum(list1))
