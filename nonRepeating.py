#function for non-repeatnig elements
def non_repeat(a):
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                represult.append(a[i])
    #non-repeated elements
    for i in a:
        if i not in represult:
            result.append(i)
    print("Non-repeating elements are :", result)


a=[5,10,15,20,25,30,35,40,45,50,55,20,25,30,35,40,45,50,5,10]
represult=[]
result=[]
non_repeat(a)