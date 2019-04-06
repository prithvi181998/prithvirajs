a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
else:
    print("c is greater")



a=int(input("enter a no. "))
if a==10:
      print("number entered is 10")
elif a==50:
      print("number entered is 50")
elif a==100:
      print("number entered is 100")



a=int(input("enter your marks:"))
if a>=90 and a<=100:
      print("your grade is A")
elif a>=80 and a<90:
      print("your grade is B")
elif a>=60 and a<80:
      print("your grade is C")
elif a>=50 and a<60:
      print("your grade is D")
elif a>=40 and a<50:
      print("your grade is E")
elif a<40:
      print("tumse na hopayega")
      

a=str(input("enter a character:"))
b=a.lower()
if b=='a' and b=='e' and b=='i' and b=='o' and b=='u':
      print("its a vowel")
else:
      print("its consonant")
      
      
            
a=int(input("enter a year:"))
if ((a%400==0) or (a%100!=0)) and (a%4==0):
    print("leap year")
else:
    print("not a leap year")
    



a=str(input("enter a word"))
b=""
for i in a:
    b=i+b
if (a==b):
    print("palindrome")
else:
    print("not palindrome")
    

    

a=int(input("enter a number"))
for i in range(1,11):
      b=a*i
      print(a,"*",i,"=",b)



n=int(input("enter the number of rows you want to print"))
i,j=0,0
for i in range(0,n):
    print()
    for j in range(0,i+1):
        print("*",end="")



for i in range(0,100):
    print(i)
else:
    print("for loop completely exhausted,since there is no break.")



def hello_world():
    print("hello world")


hello_world()




#defining the function
def func(name):
    print("Hi",name);

#calling the function
func("Prithvi")


def si(p,r,t):
    si=((p*r*t)/100)
    return si
p=float(input("enter principle"))
r=float(input("enter rate"))
t=float(input("enter time"))
print("simple interest is=",si(p,r,t))


def add(a,b):
    add=(a+b)
    return add
a=int(input("enter value of a"))
b=int(input("enter value of b"))
print("sum of a and b is=",add(a,b))




def func(name,message):
    print("printing the message with",name,"and",message)
func(name=(input("enter your name")),message=(input("enter a message")))


def simple_interest(p,t,r):
    return (p*t*r)/100
print("simple interest:",simple_interest(t=10,r=10,p=1900)) 



def print_message():
    message="hello world"
    print(message)
print_message()
print(message)













































