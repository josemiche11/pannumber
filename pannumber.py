number=int(input("Enter the number :"))
list1=[]
num=number
while number>0:
    rem=number%10
    list1.append(rem)
    number=number//10
for i in range(10):
    count=list1.count(i)
    for j in range(count-1):
        list1.remove(i)
    count=0
if len(list1)==10:
    print("{0} is pan number ".format(num))
else:
    print("{0} is not a pan number ".format(num))
