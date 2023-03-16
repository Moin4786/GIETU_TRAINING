#CLOSEST PALINDROME
'''import sys
def next_smallest(num):
    for i in range (num+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i)
print (next_smallest(99))
print(next_smallest(1221))


def max_visited(patient_ms,medical_s):
    max_visit=0
    P=patient_ms.count('P')
    E=patient_ms.count('E')
    O=patient_ms.count('O')
    if P>E and P>O:
        
        speciality=medical_s['P']
    elif E>O:
          speciality=medical_s['E']
    else:
          speciality=medical_s['O']
    return speciality
patient_ms=[301,'P',302,'P',305,'P',401,'E',656,'E']
medical_s={'P':"Pediatrics",'O':"Orthopedics",'E':"ENT"}
speciality=max_visited(patient_ms,medical_s)
print(speciality)
#repeating characters
def common_char(str1, str2):
    common = ""
    for char in str1:
        if char in str2 and char not in common:
            common += char
    if common:
        return common
    else:
        return -1


string1 = "I like Python"
string2 = "Java is a very popular language"
print(common_char(string1, string2))

#overlapping max characters
w1,w2=input().split()
ans=[[0 for i in range(len(w2)+1)] for j in range(len(w1)+1)]
val=-1
r=0
c=0
for i in range(len(w1)+1):
    for j in range(len(w2)+1):
        if(i==0 or j==0):
            ans[i][j]=0
        elif(w1[i-1]==w2[j-1]):
            ans[i][j]=ans[i-1][j-1]+1
            if(ans[i][j]>=val):
                val=max(ans[i][j],val)
                r=i
                c=j
        else:
            ans[i][j]=0

a=''
while(ans[r][c]>0):
    a=w1[r-1]+a
    r-=1
    c-=1
print(a)
#STARTING OOPS CONCEPT IN PYTHON
class Example:

    def __init__(self, num):
        self.num=num

    def set_num(self, num):
        self.num=num

    def get_num(self):
        return self.num

obj=Example(10) 

print(obj.get_num()) 
obj.set_num(15)
print(obj.get_num())
class Book:
    def init(self):
        self.title=None

my_fav=Book()
my_fav.title="Head First Programming"
your_fav=Book()
your_fav.title="Learn Python the hard way"
my_fav.title="Learning Python"

print("My favorite is",my_fav.title)
print("Your's is",your_fav.title)

class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
                                                                                                
s1=Shoe(2000,"Canvas")
print("The unique id of the object is ",id(s1))
#print(s1)
print(s1.price,s1.material)



class Mobile:
    def display(self):
        print("diplaying details")
        

    def purchase(self):
        
         
        self.display()
        print("cal price")

Mobile().purchase()


class Mobile:
    def __init__(self, brand, price):
        self.brand=brand
        self.price=price
        self.total_price = None
    def purchase(self):
        if self.brand=="Apple":
            discount=10
        else:
            discount=5
        self.total_price = self.price- self.price*(discount/100)
        print("Total price of", self.brand, "mobile is", self.total_price)
mob1=Mobile("Apple",20000)
mob2=Mobile("Samsung",10000)
mob1.purchase()
mob2.purchase()




class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id= cust_id
        self.name = name
        self.age = age
        self.wallet_balance =  wallet_balance
    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount
    def show_balance(self):
        print("The balance is ", self.wallet_balance)
c1=Customer(100, "Gopal", 24, 1000)
c1.update_balance(500)
c1.show_balance()



class Table:
    def init(self):
        self.no_of_legs=4
        self._glass_top=None
        self._wooden_top=None
    def assign_data(self, glass_top,wooden_top):
        self._glass_top=glass_top
        self._wooden_top=wooden_top
    def identify_rate(self, glass_top, wooden_top):
        self.assign_data(glass_top, wooden_top)
        if(self._glass_top==True):
            rate=20000
        elif(self._wooden_top==True):
            rate=30000
        else:
            rate=0
        return rate
dining_table=Table()
rate=dining_table.identify_rate (False, True)
print(rate)'''




                                                                                                
class Table:
    def __init__(self):
        self.no_of_legs=4
        self._glass_top=None
        self._wooden_top=None
dining_table = Table()
back_table = Table()
front_table = back_table
back_table  = dining_table
print(dining_table, back_table, front_table )











