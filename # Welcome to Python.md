\# Welcome to Python





\###########

A built-in python function that displays messages on the output screen to communicate with users.



Print(“Helloo world”)

Print(“ Hi \\”python\\”“) escape character

Print(‘Hi “Python” ’) #both quote

Print(“path : C:\\\\user\\\\desktop”)  #escape charater used

Print(“message1\\nmegsage2”) #new line

Print(“message1\\tmegsage2”) #tab separetad





\################



Print(“my name is xyz”)

Print(“xyz is learning python”)			#makes program dynamic



Name = “tanmay”					#name to store a value

Language = “python

Print(“my name is ”, name)				#resusable anytime

Print(name, “ is learning ”, language)



X = 1				

Print(x)

X = 2

Print(x)



Q: create a calculator which will take values from user?



a = int(input("enter number: "))

b = int(input("enter number: "))

print("sum =", a + b)





Q: write a program to input name and print hello "input name"



name = input("enter your name:")

print("Hello",name)



\########################

**Data types**





A = 10 #integer  b = “ hello” #string”  c = “True” #Boolean

D = 3.14 #float  e = None   #none data type



List = \[ 1, 2, 3]

Tuple = (3,4,5)

Dict = { ‘a’:1, ‘b’:2 , ‘c’:3}





**List**



color = \["red","green","yellow"]



features of list 

list are mutables,ordered,duplicate allowed, acces using index

print(color)



print(color\[0])

modify list

color\[1] = "blue"



color.append("white")



color.remove("red")





**Tuple**

A tuple is similar to list but cannot be changed after creation.

fruits = ("apple","mango","banana")

tuples are immutable,ordered,acces using index

print(fruits\[1])

tuple cannot be modified

fruits\[0] = "cherry"





color = \["red","green","yellow"]



features of list 

list are mutables,ordered,duplicate allowed, acces using index

print(color)



print(color\[0])

modify list

color\[1] = "blue"



color.append("white")



color.remove("red")















Dictonary



a dictionary stores data in key and value format unordered, mutable, key must be unique

student = {

&#x09;"name" : "tanmay",

&#x09;"age"  : 25,

&#x09;"city" : "bengaluru"

}

print(student)

\###access values##

print(student\["name"])

add or update values

student\["age"] = 26

student\["job"] = "engineer"

print(student)







\####################



A function is a reusable block of code that can be called independently, whereas a method is a function that belongs to an object or class and is called through that object. For example, len() is a function, while upper() is a method of a string object.





Function Example

def greet(name):
    print("Hello", name)

greet("Tanmay")





Built-in Function



print("Hello")

len("Python")

type(10)



print(), len(), and type() are functions.







Built-in Method

name = "Tanmay"



print(name.upper())

print(name.lower())



upper() and lower() are methods of the string object.





Q: Check whether an email has a basic valid format



def is\_valid\_email(email):

    return "@" in email and "." in email

print(is\_valid\_email("sara@gmail.com"))

print(is\_valid\_email("saragmail.com"))

print(is\_valid\_email("sara@gmailcom"))





WAP to clean a work and convert to lower

ex:



def clean\_name(name):

    cleaned = name.strip().lower()

    print(cleaned)




clean\_name("   MariA  ")





ex:



def clean\_name(name):

   cleaned = name.strip().lower()

   return(cleaned)

clean\_name("   MariA  ")

cl = clean\_name("   MariA  ")

print(clean\_name)

print(cl)







ex: WAP to sort email and domain using function





def clean\_and\_split\_email(email):

    cl\_email = email.strip().lower()

    #sara@gmail.com

    username, domain = cl\_email.split("@")

    return {"username": username,

            "doimain" : domain}

print(clean\_and\_split\_email("  SARA@gmail.com "))





\##################################



**Parameter and arguments**



def clean\_name(first\_name, last\_name):

    first = first\_name.strip().lower()

    last = last\_name.strip().lower()

    full\_name = first + " " + last

    print(full\_name)




clean\_name("  Maria ", "sahoo")

\#RULE

\#no of argument must math the number of paramater







**Exception Handling**



\* Error caused by not following proper syntax of any language.

&#x20; This is also called syntax error

\* A python program terminates as soon as it encounters an unhandled error.

\* Error that occur at runtime even if syntax is correct are called exception or logical error.

\* whenever these types of runtime errors occur, python creates and exception object.

&#x20; if not handled properly. it prints the error and some details about it.



eg:



try:

&#x20; 1/0

except:

&#x20;  print("can't divide by zero")







\* First try clause i.e the code between try and except clause.

\* if there is no exception, then only try clause will run, except clause is finished.

\* if any exception occur, but the except clause within the code doesn't handle it 

&#x20; it is passed on to the outer try statements. If the exception left unhandled, then the execution stops.

&#x20; 

&#x20;\* a try statement can have more than one except clause.







\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



try:

  a = 10                                    #try changing value b= 0 zero error ,b= d name error, b=4 successful 

  b = 4

  c = a/b

except ZeroDivisionError as e:    

  print(e)

  print(" enter valid number in b:")




except NameError as e:

  print(e)




else:

  print("executed succesfully")

  print(c)



\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*







**ex:**





try:

&#x20; 1/0

except ZeroDivisionError as e:

&#x20; print("error")

&#x20; print(e)

else:

&#x20; print("No error")

finally:

&#x20; print("completed")





\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



**Raise an Exception**



\-python enable developer to create their own exception by using raise keyword

\- this can also be called user defined exception



Example:

try:

&#x20; num=input("enter a positive integer:")

&#x20; if int(num)<0:

&#x09;raise ValueError

except ValueError:

&#x09;print("sorry ! number is negative or zero")







**File Operation**

order of file operation in python:

1\. open a file

2\. read or write

3\. close the file





opening file:

open() function is used to open a file , it returns a file object.

take two parameters: filename and mode.





'r" - read - default value. open a file for reading. error if the file does not exist.

"a" - append - open a file for appending. creates the file if it does not exist

"w" = write - open a file for writing. create the file if it does not exist

"x" - create the specific file . returns an error if file exists



f  = open('filename.txt')

f = open('filename.txt','w')





Reading Files



f.open(r'C:\\\\Users\\Desktop\\sample.txt')

print(f.read()) #read the entire file

print(f.read(5)) # read the 1st 5 characters of file

print(f.readline()) #read the first line

print(f.tell()) #return current file position

f.seek(0) #bring the cursor to initial position



Encoding

encoding is platform dependent. In windows it is cp1252 but utf-8 in linux. if we can't rely on the default encoding we must specify encoding types

f = open('test.txt',encoding='utf-8')









writing in new file:

f=open('myfile.txt','w') #write mode create new filename

f.write('hello my file') #overwrite the file already exist





write in a exixting file:

f=open('myfile.txt','a') #append mode

f.write("\\nNew line added") #append new content in existing file



closing file:

after performing operation, the files should be closed. It will free up the space.

f.close()



writing file using with:

it ensures that the file is closed when the block inside the with statement is exited.

with open("myfile.txt",'w') as f:

&#x09;f.write("He there \\n")

&#x09;f.write("How you doing")

it will close the file once write operation is done









**Directory**

To handle large number of files, directories can be used to make it manageable.

python has in-built os module to manage directories and files.



import os

print(os.getcwd())   # get current working directory

os.chdir("D:\\\\terrform") # change working directories

print(os.listdir())  #return list of directories and files



\#to craete a new directory

os.mkdir("my\_dir")



\#removing directory

os.rmdir("my\_dir")

\#removing file

os.remove("myfile.txt")

\#renaming a file or directories

os.rename('my\_dir','new\_name')







\#########################



**Class**





A class is a blueprint or template used to create objects.



Class = Car Blueprint

Objects = BMW, Audi, Tesla



Without classes:

name = "Tanmay"

age = 25

city = "Bangalore"





ex:



class Person:

&#x20;   def \_\_init\_\_(self, name, age):

&#x20;       self.name = name

&#x20;       self.age = age



p1 = Person("Tanmay", 25)



print(p1.name)

print(p1.age)





\_\_init\_\_ is a special method called automatically when an object is created.



p1 = Person("Tanmay", 25)

Person.\_\_init\_\_(p1, "Tanmay", 25)



self refers to the current object.



class Person:

&#x20;   def \_\_init\_\_(self, name):

&#x20;       self.name = name







class Person:



&#x20;   def \_\_init\_\_(self, name):

&#x20;       self.name = name



&#x20;   def greet(self):

&#x20;       print("Hello", self.name)



p1 = Person("Tanmay")

p1.greet()

















