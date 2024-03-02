print("hello world!")


#variable concept
message="hello world! this is sai kiran"
print(message)

message='this is sai kiran i have started learning python'
print(message)

a=20+20
print(a)
print(id(a))  #id function say where the value is being stored

##data types
a=3
print(type(a))
print(a)

b=1.5
print(b)
print(type(b))

c="sai kiran"
print(c)
print(type(c))

d=True
print(d)
print(type(d))

###input function 
# f=input()
# print(type(f))


###type conversion
# g=input()
# h=float(g)
# print(type(h))

# i=input()
# j=int(i)
# print(j)
# print(type(j))

# k=input()
# m=int(k)
# l=input()
# n=int(l)
# print(m+n)


age=23
print("happy"+str(age)+"rd birthday")

# finding the type of the variable
q=4
print(type(q))

##end parameter
print("welcome to",end=' ')
print('coding ninjas')

## separator parameter
print('1','2','2024',sep='-')



#white spacing 
print('programminglanguages=\n\tpython,\n\trust,\n\tjava')


#arithmetic operators
a=3
g=4
print(a+g) #addition
print(a-g)  #subtraction
print(a*g)  #multiplication
print(a%g)  #module gives the reminder value
print(a/g)  #division give the float value
print(a**g)  #power of
print(a//g) #floor division means it gives a nearest smallest integer 
print(2*0.2) ##float multiplication

#comparasion operator
a=4
h=3
print(a==h)
print(a!=h)
print(a>h)
print(a<h)
print(a>=h)
print(a<=h)

##assignment operator
y=6  #assigning the value

y+=y
print(y)

y-=2
print(y)

y/=2
print(y)

##logical operator  (and , or , not)

#and 
h=4>5 & 5>4    # false and true
print(h)

j=7>5 & 9<10    #true and true
print(j)

k=1>5 & 9>8  # false and true
print(k)

s=6>7 & 5>6   # false and false
print(s)

print()
#or
i=6>7 or 9>8   #false and true
print(i)

n=7>5 or 9>10  # true and false
print(n)

w=7>4 or 8>7    #true and true
print(w)

q=8>9 or 10>11      #false and false
print(q)


print()
#not
r=not 3<5  ##when we type not the true becomes false and viseversa
print(r)

##volume of the shpere with 2 decimals in the end
pi=22/7
r=8
volume_of_sphere=(4*pi*r**3)/3
print(round(volume_of_sphere,2))

## conditionals statements 
##                  if else
# age=int(input())
# if age>18:
#     print("you are eligible for driving")
# else:
#     print("you are not eligible to drive")

##                  nested if  
# age=input()
# if age>18:
#     if age>65:
#         print("take rest")
#     else:
#         print("drive safely")
# else:
#     print("wait till you get license")

##                   if elif else    
# a=int(input())
# if a>0:
#     print("positive")
# elif a==0:
#     print("equal to zero")
# else:
#     print("positive")

########printing the highest marks using max and min function
marks=[90,30,100,85,45,95]
v=max(marks)
s=min(marks)
print(v,s,sep=",")

##########grading system  using conditional statements
# marks=int(input())
# if marks>=90 and marks<=100:
#     print("grade A")
# elif marks<90 and marks>=80:
#     print("grade B")
# elif marks<80 and marks>=70:
#     print("grade C")
# elif marks<70 and marks>=60:
#     print("grade D")
# elif marks <60:
#     print("grade E")
# else:
#     print("invalid")


###fizzbuzz
# number=int(input())
# if number%3==0 and number%5==0:
#     print("FizzBuzz")
# elif number%5==0:
#     print("Buzz")
# elif number%3==0:
#     print("Fizz")
# else:
#     print(number)


## while loop
i=1
while i<5:
    print("sai kiran",i)
    i+=1
j=1
while j<=5:
    print("hello",j)
    j+=1

k=1
while k<=10:
    print(k, end=' ')
    k+=1
print()

m=1
while m<=10:
    if m%2==0:
        print(m,end='')
    m+=1

print()
n=1
while n<=10:
    if n%2!=0:
        print(n,sep=',', end='')
    n+=1

print()

h=1
f=0
while h<=10:
    f+=h
    print(f,sep=',',end=' ')
    h+=1

print()

g=1
s=0
while g<=10:
    if g%2==0:
        s+=g
        print(s,sep=",", end=' ')
    g+=1
print()
##range function
q=list(range(5))    ### by default the start will be zero
print(q)

c=list(range(1,5))    #### by default the jump will be 1
print(c)

b=list(range(1,10,2)) ##### all three values are given 
print(b)

### for loop
for i in range(6):
    print(i)
print()

for i in range(1,6):
    if i%2==0:
        print(i)
print()

for i in range(1,6,3):
    if i%2!=0:
        print(i)
print()

for i in range(1,11):
    print(5*i)

print()
### pattern printing
for i in range(4):
    for j in range(4):
        print('#',end="")
    print()

print()
    
for i in range(1,5):
    for j in range(i):
        print('#',end='')
    print()
print()

for i in range(1,5):
    for j in range(5-i):
        print('#',end=' ')
    print()
print()

for i in range(1,6):
    for j in range(i):
        print(j,end='')
    print()
print()

for i in range(1,5):
    for j in range(5-i):
        print(j,end='')
    print()
print()

for i in range(1,6):
    for j in range(i):
        print(i,end='')
    print()
print()

for i in range(1,6):
    if i%2!=0:
        for j in range(i):
            print("#",end=' ')
    print()
print()        


k=1
for i in range(1,4):
    for j in range(1,k+1):
        print('#',end=' ')
    k=k+2
    print()
print()


for i in range(4):
    for j in range(4-i-1):
        print(' ',end='')
    for k in range(i+1):
            print('#',end='')
    print()
print()

for i in range(4):
    for j in range(4-i-1):
        print(' ',end='')
    for k in range(i+1):
            print('#',end=' ')
    print()
print()

for i in range(4):
    for k in range(4-i):
            print('#',end=' ')
    print()
    for j in range(i+1):
        print(' ',end='')
print()

for i in range(4):
    for k in range(4-i):
            print('#',end='')
    print()
    for j in range(i+1):
        print(' ',end='')
print()

####strings
s='saikiran'
i=len(s)
print(i)
w=s[0]
print(w)
q=s[-1]
print(q)
print()
name='saikiranpuppala'
u=len(name)
print(u)
i=name[0:len(name)]
print(i)
print()
w=name[:15:2]  ### start:end:length(how many jumps we will be doing )
print(w)
print()
u=name[-1:-(len(name)+1):-1]
print(u)
r=-(len(name)+1)
print(r)
print()
#### string methods
_name="sai kiran puppala"
print(_name.title())   ### makes the first letter of each word into capital
print(_name.upper())   ### makes the whole string into capital  
print(_name.lower())   ### makes the whole string into lower
print(_name.capitalize())   ### makes the first letter of the whole string to capital
print(_name.replace("k","K"))   ### replaces the character with the desired character 
print(_name.count("a"))   ###counts how many times the character occures in the string
print(_name.index("k"))    ### finds the index values of the character
print(_name.find("s"))    ### finds the index values which are lowest
print(_name.split())   ### split is used to convert the string into list and to separate the string into individual elements
print()

kulu,bolu,dola=_name.split()
print("kulu:",kulu ,"bolu:",bolu ,"dola:",dola)

volt="2 3"
h,g=map(int,volt.split())     #### in this the map function is used to map the splited string to there particular variable and int to convert the string to int
print(h,g)

### formating
# place=input()
# print(f"the place my friends visited are {place}")
print()

_place="goa"
print(f"the place my friends visited are {_place}")
print()

##concatination   adding the two strings
_first_="sai"
_second_="kiran"
_third_="puppala"
print(_first_ + _second_ + _third_)
print()
#printing vowels from the sentence
text="the quick brown fox jumps over the lazy dog"
for i in text:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        print(i)
#### palindrome (if the sentence is same from both the sides)
sentence="radar"
if sentence == sentence[::-1]:
    print("yes")
else:
    print("no")
print()

#### list 
li=[1,2,3,4,5]
print(li)

###accessing the list elements
print(li[0])
print(li[-5])
print(li[::-1])   #printing the list reverse 
print(li[0:len(li)])
print(len(li))
## list operations
lit=["bag","rag","clag","vag"]  
lit.pop(1)               ##removes the string of the desired index (use only index )
print(lit)

lit.pop()             ###removes the last string in the list
print(lit)

lit.remove("bag")           ### removes the desired string from the list 
print(lit)

crop=['suresh','ramesh','balu','somu','nigga']
del crop[0:4]               #### remove multiple elements from the list
print(crop)

gap=[100,50,170,670,239,234]
gap.sort()           ########### sorts the list in the order 
print(gap)

lit.insert(0,'rap')      ### inserts the string in the list in particular index places
print(lit)

lit.append('jay garick')  #### inserts the element in the last of the list
print(lit)

lit.extend(['karan','sharukh','salmon'])     ### extend will iterates the given list in the list or you can say extend is used to add multiple elements to the list (in the form of list only)
print(lit)

###2D list 
virat=['50','100','150','180']
dhoni=['40','60','100','60']
rohith=['20','50','70','100']
team=[virat,dhoni,rohith]
print(team[0])
print(team[0][0])      ##accessing the list 

l1=['3','4','5','6']
l2=['2','8','5','9','1']
l=[l1,l2]
for i in l:
    print(i)

for i in l:
    for j in i:
        print(j)

###list comprehension
gler=[i for i in range(10)]
print(gler)

##taking the input from the user for the list
# la=[]
# for i in range(int(input())):
#     la.append(i)
# print(la)

# la=[]
# la.append(input())
# print(la)

languages=['python','java','go','ruby','perl','c']
lenghts=[len(i) for i in languages]
print(lenghts)

l=['4','6','5','8','9','3','2','4','5','4','3','2','3','4']
total=0
for i in l:
    total += int(i)
print(total)
print()

######tuple
t=('mercury','venus','earth','mars','jupiter','saturn','uranus','neptune')
print(type(t))
print()

t1=()      ##empty tuple
print(t1)
print()

t2=(2,)     ##non empty and , is mandatory to recognize as tuple
print(t2)
print()

t3=('rahul',)
print(t3)
print()

t4=tuple('rahul')        ###tuple function is used to convert the iterable like list,set,string to tuple
print(t4)

t5=(['1','2','3','4'],'string',True) ###heterogenious types can be present in tuple
print(type(t5))     ###type does not change 
print(t5[0])        ###accessing the tuple
print(t5[0][0])     ###accessing the particular tuple 
print(t5[0][0]=='45')      

t5[0][0]='5'      ### the tuple is mutable if and only if the elements are mutable like list
print(t5)

name_lst = ["Vijay", "Vickey"]
tup = ("Item_1", 0.5, name_lst)
name_lst.append("Vishal")     
print(tup)

elements = (10, 20, 30, 40, 50, 60, 70, 80)
print(elements[2:5], elements[:4], elements[3:100])

###dictionary 
d={}    ###empty dict
print(type(d))

d=dict()   ##type conversion
print(type(d))

dic={"apple":20,"banana":30,"mango":20}
print(dic)

##zip
name=["apple","banana","mango"]
prices=['20','20','20']                   
fruits=dict(zip(name,prices))    ### zip function is used to list element wise ex:[(apple,20),......]
print(fruits)

##accessing the dictionary 
print(dic["apple"])  ##can be accessed using  only the key 

print(dic.get("banana"))


### updating  and inserting the value in the dict
print(dic)
print()
##inserting
dic['mango']={"small":15,"large":30}   ###only one element can be changed like this
print(dic)
print()

#updating
new={"grapes":30,"orange":40,"berry":50}
dic.update(new)      ####multiple elements can be added using this method
print(dic)
print()

##deleting the elements from the dictionary 
dic.pop("apple")          ## delete particular element
print(dic)
print()

dic.popitem()            ##deleting the last element by defaultly
print(dic)

###iterations in dictionaries
for i in dic:
    print(i)      ###for keys 

print()

for i in dic:
    print(dic[i])   ## for values

print()

for i in dic:
    print(i,dic[i])   ##for both keys and values
print()
##this is the short cut with the name that can be remembered 
for key,value in dic.items():   ### we have to use dict.items
    print(key,value)

print()
#dic methods
print(dic.items())
print()
print(dic.keys())
print()
print(dic.values())
print()

#### to find the """frequency""" of the letter 
name='saikiran'
dictionary={}
for i in name:
    if i not in dictionary:
        dictionary[i]=1
    else:
        dictionary[i]+=1
print(dictionary)
print()

dic={"key":25,"key2":25,"key3":50}
gorila=0
for i in dic:
    gorila+=dic[i]
print(gorila)

print()
flag={"key":25,"key2":25,"key3":50}
flag.update({"key4":30})
print(flag)

###sets
s={1,2,3,4,2,1}
print(s)   ### sets contains unique values means it doesnot repeat the values 
print()

se=set("sai")       ##set function is used for 
print(se)
print()

for i in s: 
    print(i) 
print()
 
for i in se:
    print(i)

##inserting the values in the set 
lap={"saikiran"}    ## it is used to add the one single element to set 
lap.add("puppala")
print(lap)
print()

lap.update("harshini")
print(lap)      ## it is used to add the iterated elements to set 
print()

s.pop()
print(s)
print()

bap={"ironman","hulk","thor","captain"}
rap={"captain","superman","batman","wondewomen"}
print(bap.intersection(rap))    ## intersection is used to find the common element in both the sets
print()
print(rap.union(bap))     ##union is the all elements in the sets with out repetation
print()
print(bap.difference(rap))      ## difference is used to display not common elements 
print()

##find the unique elements from the set
keep="this is the sentence used for the example for set"
ls=keep.split()
print(ls)
print()
rust=set(ls)
print(rust)
print()


### this question is finding the frequency of the number
values=("10","8","5","2","10","15","10","8","5","8","8","2")
set={}
for i in values:
    if i not in set:
        set[i]=1
    else:
        set[i]+=1
print(set)
print()

#####functions
def greet():
    print("hello have a good day.")
greet()             #### a user defined function can be created and the code can be written in that and that can be called by just typing the function.
print()

def greeting():
    print("hello good morning")
    """this function greets the user with the good morning when u call it"""   ###docstring is nothing but documentation in the form of string about the code 
greeting()
print()

def car():
    a, b =2 ,3
    if a>b:
        return a
    else:
        return b
print(car())
print()

def hulk():
    print("hello,have a good day")
    return "saikiran"
result=hulk()
print(result)
print()

###parameter and argument in function 
def greets(name):     #### when defining them we call them as parameter
    print("hello,nice to meet you",name)
greets("saikiran puppala")   ### when calling them we call them as argument.
print()

def add(a,b):
    c=a+b
    return c
d=add(2,3)
print(d)
print()


def dog(a,b):
    if a>b:
        print(a)
    else:
        print(b)
cat=dog(30,20)
print(cat)
print()

### scope of the variable 
a=2
def func():
    a=20
    print(a)
func()        ### apon calling the function the value in the function will be printed 
print(a)        ### this will print the global variable bacause the print is out of the function and there is a global variable out of the function with the same variable name.

print()

### global keyword
b=4
def fun():
    global b     ### this key word is used to convert the local variable to global variable.
    b=30
    print(b)
print(b)      ### the print(b) will print the global values because the function is not activated 
fun()         ### as the function is activated the local variable is converted to global variable and the global variable doesnot work any more.
print(b)       ### this will be printing the local variable that which is converted to global variable bacause the function is activated.
print()

#####lambda function ( lambda function can be used as the function with out any name or nameless function)

##lambda (parameter):expression (values u want to input) 
screen=(lambda a,b : a+b)(3,4)
print(screen)

print()

freen=(lambda c,d : c if c>d else d)
print(freen(5,4))       ##you can give the input values this way too
print()


thor=[1,3,4,7,45,64,23]
captain=sorted(thor,key=lambda i :i)      ###key parameter is used in the sorted function and in key parameter you have to give the condition or create a function with condition
print(captain)
print()

def even(lits):
    for i in lits:
        if i%2==0:
            print(i)     #### returns none as well 
print(even([1,2,3,4,5,6,7,8,9]))


def even(lits):
    even_numbers = []
    for i in lits:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers               ###returns the values only
result = even([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(result)
 
print()

#### this question is returning the new list  of unique elements from the existing list.
gan=[1,2,3,1,2,4]
fand=[]
def fan(lkt):
    for i in gan:
        if i not in fand:
            fand.append(i)
    return fand
print(fan(gan))
print()

###arbitrary arguments  ( this is used when we dont know how many parameters and arguments are to be taken)
def glad(*args):
    for i in args:
        return i
print(glad(1,2,5,4,6,"rahul"))
print()

### keyword argument this will store the value in the form of dictionary 
def sul(**kwargs):
    return kwargs
print(sul(name="saikiran",age=20))
print()

def sal(**kwargs):
    for i in kwargs:
        print(i,kwargs[i])                   #### in this none is returning 
print(sal(glao=1,bola=2,sdf=3,erw=4))

print()

def sal(**kwergs):
    for key, value in kwergs.items():       #### in this none is not returning and another list is not needed
        print(key, value)

sal(glao=1, bola=2, sdf=3, erw=4)

print()


### u should not use *args after **kwargs 
def hitler(*args,**kwargs):
    print(args,kwargs)
print(hitler(23,34,45,56,golddogger=342,binladin=235))

def convert(t):
    return t*9/5 + 32

print(convert(20))
print()




##oops in python 
class cars:
    pass
roseroseeee=cars()
print(type(roseroseeee))       ### this is saying that this object belong to cars class
 
print()

class road:
    def __init__(self):    ### this is a dunder method(double under) or constructor this will execute itself with out calling it explecitly
        print("this will execute itself")
hyderabad=road()   ##this is called instance or object

print()

class train:
    def __init__(self,name,age,gender):     ### this is called parameter
        self.name=name
        self.age=age
        self.gender=gender
hyderabad=train("kiran",20,"boy")      ### this is arguments
print(hyderabad.age)                     ### printing the specific parameter

print()

class finger:
    def __init__(self,year,month,date):
        self.year=year
        self.month=month
        self.date=date
    def tip(self):                          ### there can be any number of methods and objects 
        print(f"this is {self.year}.")
leftring=finger("2024","feb",19)
print(leftring.year)
leftring.tip()                              ### calling the seconds method

print()

class leg:
    def lap(self,name,age):      ### this is a normal method.
        self.name=name
        self.age=age
rightleg=leg()
rightleg.lap("sai",20)
print(rightleg.age)
print(type(rightleg.age))
print()

 
### class variable 
class keys:
    population=0         ### this is the global class which can be written out side of the method and can be used inside of the method
    data=[]
    def __init__(self,name,age,alive=True):
        self.name=name
        self.age=age
        keys.population+=1    ### like this we can use the class variable in the method
        keys.data.append(name)
        self.alive=alive

    def dead(self):
        if self.alive:
            print("he is no more")
            keys.population-=1
            print(self.name)
            self.alive=False
        else:
            print("this person is already dead")

    def child(self, number):
        keys.population+= number

booka=keys("shaki",23)
chuuka=keys("megapra",25)
print(keys.population,booka.age,booka.data,sep="\n")
booka.dead()
print(keys.population)
print()
booka.dead()
print(keys.population)
print()
chuuka.dead()
print(keys.population)
print()
booka.child(2)
print(keys.population)

print()

#### inheritance           

class employee(keys):
    def __init__(self,name,age,company,position):        ### though you derive the class you need to write the attributes of the main class in this.
        super() .__init__(name,age)      ### we will use super constructor to inherit the methods from the main class to derived class
        self.company=company
        self.position=position
person1=employee("varun",21,"dontknow","unemployeed")
print(person1.company)
print()

###########################################################################################################
### practice or revision




































































































