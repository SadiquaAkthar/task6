def prime():
    lis=[10, 501, 22, 37, 100, 999, 87, 351]
    primeL=[]
    #iterate over the list
    for i in lis:
        # if number is >1 iterate and find % until i 
        if i>1:
            for j in range(2,i):
                if i % j == 0:
                    break
            # if prime append
            else:
                primeL.append(i)
    #display the prime number in the list and the number of prime number
    print(primeL)
    print("Prime numbers in the list : ",len(primeL))
prime()