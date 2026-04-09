num = int(input("enter number :"))
flag = True
for i in range(1,num):
    if num%i == 0:
        flag = False
        break
if flag:
    print("number is prime")
else:
    print("number is not prime")
