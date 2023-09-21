#list of numbers
a=[10,20,30,40,50,60]
b=[5,10,15,20,25,30,35,40,45,50,55]
c=[2,4,6,8,10,12,14,16,18,20]
result=[]
#iterate over the a and check if i in other list
for i in a:
    if i in b and i in c:
        # append if duplicate
        result.append(i)
print(result)
        