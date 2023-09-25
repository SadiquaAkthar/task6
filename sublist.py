def sub_zerosum(list1):
    # Create a dictionary to store cumulative sums and their corresponding indices
    sum_dict={}
    csum=0
    sub_list=[]

    for i, num in enumerate(list1):
        csum +=num
        if csum==0:
            sub_list = list1[:i+1]
        elif csum in sum_dict:
            sub_list=list1[sum_dict[csum] + 1:i+1]
        # Store the current cumulative sum and its index   
        sum_dict[csum]=i
    return sub_list

list1=[4, 2, -3, 1, 6]
print(sub_zerosum(list1))
