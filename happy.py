class happy():
# to find out the squared sum of the number
    def squaredsum(num,n):
        sum = 0
        print(num,n)
        for i in n:
# call the happy numbers function
            if num.happynumber(i,{}):
                sum += 1
        return sum
# return true is happy number else false
    def happynumber(num,n,v):
        if n==1:
            return True
        if n in v:
            return False
        v[n]=1
        n=str(n)
        l=list(n)
        l=list(map(int,l))
        temp=0
        for i in l:
            temp += (i**2)
        return num.happynumber(temp,v)

ob1=happy()        
l1 = [10,501,22,37,100,999,87,351]
o=ob1.squaredsum(l1)
print("there are ",o," happy numbers in the list.")

