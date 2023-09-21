# getting the input value as string
digit=input("enter the number ")
#creating a list to store the single digits
digitList=[]
#iterating and appending the digits
for i in digit:
    digitList.append(i)
#sum of the first digit and the last digit converting to int
print(int(digitList[0])+int(digitList[(len(digitList)-1)]))