'''#function
#based on arguments
def function1(num1,num2,num3,num4):
    print(num1,num2,num3,num4)
function1(560,145,113,134)
function1(100,123,143,154)
#keyword arguments
def function1(num1,num2,num3,num4):
    print(num1,num2,num3,num4)
function1(num4=560,num1=145,num2=113,num3=134)
#default arguments
def function3(name,roll,branch,collagenum="GIET"):
    print(name,roll,branch,collagenum)
function3("srikant",12,"cse")


#var no of arguments
def func4(*var):
    for i in var:
    print(i,end=' ')
func4(10,20)
print()
func4(10,20,30,40)
print()
func4(10,20,30,40,50,60)
def add(*var):
    sum1=0
    for i in var:
        sum1=sum1+i
    return(sum1)
print(add(10,20))
print()
print(add(10,20,30,40))
print()
print(add(10,20,30,40,50,60))
a=int(input())
b=int(input())
c=int(input())
if(a==7):
    print(b*c)
elif(b==7):
    print(c)
elif(c==7):
    print(-1)
else:
    print(a*b*c)
#currency problem
n=float(input())
s=input("enter country name")
if s=="Euro":
    print(n*(0.01417))
elif s=="Pound":
    print(n*(0.0100))
elif s=="Australian Dollar":
    print(n*(0.02140))
elif s=="Canadian dollar":
    print(n*(0.02027))
else:
    print("invalid")
n=int(input("no. of adults"))
c=int(input("no. of child"))
res=(n*37550)+(c*(37550/3))
fi=res+(res*7/100)
final=fi-(fi*10/100)
print(final)'''
x=int(input("1rs"))
y=int(input("5rs"))
c=int(input("amount needed"))
if((y*5+x*1)<=c):
      print("invalid")
n1=c%5
n5=c//5
    if(x>=n1):
        print("number of 1",n1)
    else:
        print(-1)
if(y>=n5):
    print("number of 5",n5)
else:
    print(-1)
    



      

