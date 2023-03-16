'''n1=int(input("Enter value of n1"))
n2=int(input("Enter value of n2"))
array=[i for i in range(n1,n2+1)]
print(array)
l1=[array[i:j+1]for i in range(len(array))for j in range(i,len(array))]
print(l1)
c=0
for i in l:
    if sum(i)%2!=0:
        c+=1
print(c)
result=[]
for i in range(len(array)):
    for j in range(i,len(array)):
        result.append(array[i:j+1])
print(result)
result=[array[i:j+1] for i in range(len(array))
        for j in range(i,len(array))]
print(result)
#List Comprehension
#for loop version
result=[]
for i in range(11):
    result.append(i)
print(result)
#list comprehension method
print([i for i in range(11)])
#for loop version--> odd elements
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
print(result)
print([i for i in range(11)if i%2!=0])

#even
result=[]
for i in range(11):
    if i%2==0:
        result.append(i)
print(result)
print([i for i in range(11)if i%2==0])

#odd normL EVEN SQUARE
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)

print([i if i%2!=0 else i**2 for i in range(11)])

result=[]
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#for loop--odd-->square it
#even--> cube it
mat2=[element for row in mat for element in row]
for  i in mat2:
    if i%2!=0:
        result.append(i**2)
    else:
        result.append(i**3)
print(result)

#list comprehension
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print([ele**2 if ele%2!=0 else ele**3 for row in mat for ele in row])

        
print([[ele**2 if ele%2!=0 else ele**3 for ele in row] for row in mat])




mylist=[9,9,3,6,1,5,0,8,2,4,7]
list_b=[6,9,4,6,1,2,2]
#result=[(6,2),(4,8)]
result=[(num,mylist.index(num)) for num in list_b if num in mylist]
print(result)
result=[]
for num in list_b:

        result.append((num,mylist.index(num)))
        
print(result)


sentences = ["a new world record was set", "in the holy city of ayodhya",
             "on the eve of diwali on tuesday", "with over three lakh diya or earthen lamps",
             "lit up simultaneously on the banks of the sarayu river"]
stopwords = ['for','was', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with']

words =[]

for i in sentences:
    
    sentence_words = i.split()
   
    for j in sentence_words:
        if j not in stopwords:
          
            words.append(j)

print(words)



input_str = "3,7,6,5,1,4,8,9"

num_list = [int(n) for n in input_str.split(',')]
pos_5 = num_list.index(5)
pos_8 = num_list.index(8)
num1 = sum(num_list[:pos_5]) + sum(num_list[pos_8+1:])
num2 = int(''.join(map(str, num_list[pos_5:pos_8+1])))
print(num1+num2)


    

s=input().split(",")
stt=[]
numm=[]
for i in s:
    s1,n =i.split(":")
    stt.append(s1)
    numm.append(n) #numm-[246, 1246)

def rotate (ss,n):
    n=str(n)
    s = 0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range (len(numm)):
    print(rotate(stt[i],numm[i]))'''
















