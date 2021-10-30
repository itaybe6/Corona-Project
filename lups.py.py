'''my_list = [1,123,4,5,2,8,90]
print(my_list)
print(my_list.count(1))
my_list.sort()
print(my_list)
num1 = len(my_list)
print(num1)
print("The min value is {}".format(my_list[0]))
print("The max value is {}".format(my_list[len(my_list) -1]))
index , sum = 0 , 0
while(index < len(my_list)):
    sum += my_list[index]
    index += 1

print(sum)

avg =  sum / len(my_list)
print(avg)

my_list = [1,1,1,2,2,2,3,6,6,6,7,7,7]
print(my_list)
my_list = set(my_list)
print(my_list)
my_list.update([5,67,9])
print(my_list)

my_list = [2,1,4,5,6,5,12,41]
x = 0
num1 = 0
for x in range(len(my_list)):
    if (x % 2 == 0 and my_list[x] % 2 == 0):
        num1 += 1
    elif(x % 2 != 0 and my_list[x] % 2 != 0):
        num1 += 1

if num1 == len(my_list):
    print("ok")
else:
    print("No ok")

my_list = ['ester' , 'asd' , 'nadir' , 123]
for ab in my_list:
    print(my_list.index(ab))

for index,value in enumerate(my_list):
    print('the {}'.format(index))'''


'''num1 = 0
while(num1 < 8):
    for i in range(num1):
        print('*',end = '')
    num1 +=1
    print(" ")


my_list = ['itay' , 'beni', 'rotem']
'''

'''''
my_list = ['ester' , 'asd' , 'nadir' , 123]

for ab in enumerate(my_list):
    print('the {}'.format(ab))

num_list = [1,2,3,4]
str_list = ['itay', ' efrat' , 'dor' , 'lir']

for item in zip(num_list,str_list,my_list):
    print(item)



def print_mul(x,y):
    print(x * y , end = "##")
    return x * y


print(print_mul(4,7))
print_mul(4,9)

def print_name(name):
    print(name)

print_name("itayyyyyyyyyy")

def print_args(*args):
    for i in args:
        print(i)

print_args(1,3,4,'itay','ben',1.3)

class Person():
    name = "itay"

    def speak(self):
        Person.name = "EFRAT"
        return 3



person1 = Person()
print(person1.speak())
print(person1.name) 


for i in range(10):
    for j in range(1,4):
        print(i**j,end = ' | ')
    print("\n")

my_list = ['spe','eps','lop',12,'pol','poe']
for i in my_list :
    if i[::-1] in my_list:
        print(i)

class student:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "Student : neme :{} , age : {}".format(self.name,self.age)


student1 = student('itay' ,23)
student2 = student('dor',24)

student3 = student('matan',25)


students = [student1,student2,student3]
for stu in students:
    print(stu )'''

def surf_tri(n,a):
    if(n > 0 and a > 0):
        return a * n / 2

def absolute(num):
    if(num >= 0):
        return num
    else: return num * -1


print(surf_tri(4,8))
