# evenOdd function
def evenOdd():
    lis=[10, 501, 22, 37, 100, 999, 87, 351]
    even=[]
    odd=[]
    # for loop 
    for i in lis:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
            
    print(even)
    print(odd)
evenOdd()