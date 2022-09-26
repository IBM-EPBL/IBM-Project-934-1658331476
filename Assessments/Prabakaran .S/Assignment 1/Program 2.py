a=int(input('Enter the start'))
b=int(input('Enter the end'))
for i in range(a+1,b):
i=a
while True :
    i=i+1
    if(i>=b):
        break
    if(i%2!=0):
        print(i)
