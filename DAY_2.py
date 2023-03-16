'''#list--> ordered--default index
list1=[]
print(list1,type(list1))
list2=[1,2,3,4,5]
print(list2)
list2.append(501)
print(list2)
list2.extend([301,345,675])
print(list2)
list2.insert(0,5)
print(list2)
list2.insert(4,350)
print(list2)
list2.remove(501)
print(list2)
list2.pop(0)
print(list2)
del list2[1]
print(list2)
#question
def count(str1):
    l_count=0
    d_count=0
    for i in str1:
        if i.isalpha():
             l_count= l_count+1
        elif i.isdigit():
            d_count=d_count+1
        else:
            continue
    return[ l_count,d_count]
print(count("Infosys 123"))
def find_pairs_of_numbers(num,n):
    count=0
    for x in num:
        index=num.index(x)+1
        for y in range(index,len(num)):
            if x+num[y]==n:
               count+=1
    return count
num=[1,2,7,4,5,6,0,3]
n=6
print(find_pairs_of_numbers(num,n))


def fun1(str1):
    if len(str1)<2:
        return -1
    else:
        return str1[0:2]+str1[-2:]
print(fun1("w3resource"))
print(fun1("w3"))
print(fun1("A"))


def fun9(str9):
    if len(str9)<3:
        return str9
    elif (str9[-3:]=="ing"):
        return str9+"ly"
    else:
        return str9+"ing"
print(fun9("amazing"))
print(fun9("sleep"))
print(fun9("is"))


def function(num):
    num2=str(num*2)
    num=str(num)
    count=0
    for i in num:
        if i in num2:
            count+=1
        else:
            return False
    if count==len(num):
        return True
    
print(function(2))
print(function(125874))


lst_of_marks=(12,18,25,24,2,5,18,20,20,21)
def find_more_than_average():
    marks=0
    count=0
    for x in lst_of_marks:
        marks+=x
    average=marks/len(lst_of_marks)
    for x in lst_of_marks:
        if x>average:
            count+=1
    percentage=(count*100)/len(lst_of_marks)
    return percentage
def sort_marks():
    global lst_of_marks
    lst_of_marks=sorted(lst_of_marks)
    return lst_of_marks
def generate_frequency():
    freq=[]
    for x in range(26):
        count=0
        for y in lst_of_marks:
            if x==y:
                count+=1
        freq.append(count)
    return freq
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())


def translate(dict1,list1):
    list2=[]
    for i in list1:
        list2.append(dict1[i])
    return list2
dict1={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
list1=["merry","christmas"]
print(translate(dict1,list1))'''


















