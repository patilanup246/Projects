# -*- coding: utf-8 -*-
import sys
import random
from symbol import classdef
from _operator import add
from _ast import Num
import math
# def find_biggest_num(i,j):
#     '''
#     This method is created for finding the biggest number
#     '''
#     #Finding the square root of the input number
#     c_sqrt = i**0.5
#     d_sqrt = j**0.5
#     s = "tashhu"
#     #Comparing which square root is greater amd printing 
#     if c_sqrt > d_sqrt:
#         print ('{} > {}'.format(str(i),str(j)))
#     else:
#         print ('{} > {}'.format(str(j),str(i)))
# 
# #Finding the biggest number by sqauer root 
# a = 0
# b = 0
# try:
# 	a = int(sys.argv[1])
# 	b = int(sys.argv[4])
# except:
# 	print ('Please enter integer')
#           
# find_biggest_num(a, b)

#import requests
#import time
#url = "http://127.0.0.1:22999/api/refresh_sessions/24000"

#headers = {
 #   'accept': "application/json, text/plain, */*",
  #  'accept-encoding': "gzip, deflate, br",
   # 'accept-language': "en-US,en;q=0.9",
    #'connection': "keep-alive",
    #'content-length': "0",
    #'cookie': "_ga=GA1.1.1032280437.1519835973; _gid=GA1.1.1494721881.1526790505",
    #'host': "127.0.0.1:22999",
    #'origin': "http://127.0.0.1:22999",
    #'referer': "http://127.0.0.1:22999/proxies",
    #'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    #'cache-control': "no-cache"
    #}
#while True:
#    response = requests.request("POST", url, headers=headers)
    
#    print('Done')
    
#    time.sleep(25)


# Measure some strings:
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#      print(w, len(w))


#program for fibonacci series
# def fibonacci_series(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci_series(n-1) + fibonacci_series(n-2)
# print(fibonacci_series(10))
# # 
# a, b = 0, 1
# while a < 1000:
#     print(a, end=',')
#     a, b = b, a+b
# print()



# def marks_obtained(x,y,z):
#      x = int(input("Marks obtained in Math: "))
#     y = int(input("Marks obtained in English: "))
#     z = int(input("Marks obtained in Science: "))
#     
#     if x>90:
#         print('Grade A+')
#     elif x>60:
#         print('Grade A')    
#     elif x>50:
#         print ('Grade B')    
#     elif x>30:
#         print ('Grade D')  
#     else:
#         print('Fail')      


# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#             print(n, 'is a prime number')


'''string'''
# a = "tasneem"
# print (a[2:6:])

# print ('un'*3 + 'ium') #3 times 'un' +'ium'
# print('Py' 'thon') #printing two strings as a single word, concatenated string
# print("""\
#     Name        
#     Address
#     Phone number
# """)        #mutilines

''' Dictionary'''
# dict= {'Name': 'Tasneem' , 'Address': 'Pune', 'Phone': 7878787878}
# print ("'Name':", dict['Name'])
# print(len(dict))
# print(dict.keys())
# print(dict['address'])    #print the value of key-address
# dict['address']= 'i live in pune'   #changes the address value
# dict['zip']= 909090 #adds a new key-value in the end
# print(dict.values())
# print(dict.items())
# print ("""\
#     "'Name':", dict['Name']
#     "'Address':", dict['Address']
#     "'Phone':", dict['Phone']
# """)    

# def main():
#     details= {'Name': 'Tasneem' , 'Address': 'Pune', 'Phone': 7878787878}
#     print_dict(details)
# def print_dict(o):
#     for x in o:
#         print(f'{x}: {o[x]}')
# 
# main()

####or
# def main():
#     details= {'Name': 'Tasneem' , 'Address': 'Pune', 'Phone': 7878787878}
# #     for k, v in details.items():
# #         print(f'{k}: {v}') 
#     for k in details.keys(): print(k)
#     for v in details.values(): print(v)
# #     print_dict(details)   
# # def print_dict(o):
# #     for k, v in o.items():
# #         print(f'{k}: {v}')
# main()




'''strings'''

# word= 'Learning_python'
# # print (word[0:15:3]) #word[start:end:step]
# print(word[0:15:1])
# print (word[-15:-5:1])
#   word[0]='j'      #strings cannot be changed they are immutable
# print(word[0:15])  
# print(len(word))

# word= 'python'
# print ('j' + word[1:]) 
# print (word[:2] + 'py')


''' lists'''
# list= ['abc', 'xyz', '1', '2', '3']
# print(list)
# print(len(list))
# print(list[1:4])
# insert(0, 'zzz')
# print(list)   #inserts a value'zzz' on 0th position
# i= list.index('xyz')
# print(list[i])
# list.remove('xyz')
# print(list)
# list.pop()  #removes item from the end of the list... #list.pop(3) -removes 4th num item
# print(list)
# x= list.pop()    #print removed element
# print(x) 
# del list[1:5:2]    #deletes element by index
# print(list)   
# print(', '.join(list))  #join list by comma's
# list1= [1, 2, 3, 'xyz', 'abc']
# print(list + list1) #print concatenated list
# list[3]= 10 #lists are a mutable type, i.e. it is possible to change their content:
# print(list)
# list.append(4)  #add new items at the end of the list, by using the append() method
# list.append(5)
# print(list)
# print(list[0][1]) #word of list 'abc', printing only letter 'b'
# list[3] = 2 #replacing 4th value of the list
# print(list)

# list2= [7, 8, 9]
# x= [list, list2]    #adding two lists
# print(x)

'''tuple'''
# tuple= ('1', '2', '5', 7, 9)  #tuple is imutable, you cannot insert or delete element of tuple like list

'''sets'''
# x={1, 2, 3, 4, 5}
# print(x)
# print(len(x))

'''list comprehension'''
# from math import pi
# 
# seq= range(11)
# print(list(seq))
# seq2= [x*2 for x in seq]
# seq3=[x for x in seq if x%3!=0]
# seq4= [(x, x**2) for x in seq]
# seq5= [round(pi, i) for i in seq] 
# 
# print(seq)
# print(seq2)
# print(seq3)
# print(seq4)
# print(seq5)



'''If statement- if_condition:'''
#program for calculating grade
# y = []
# for i in range(3):
#     y.append(int(input("Marks obtained in Math: ")))
# for x in y:
#     if x>90:
#         print('Grade A+')
#     elif x>60:
#         print('Grade A')    
#     elif x>50:
#         print ('Grade B')    
#     elif x>30:
#         print ('Grade D')  
#     else:
#         print('Fail')      


''' For statement- for condition:'''
# word= ['i', 'love', 'icecream']
# # print(len(word))
# # word.insert(0, 'hey')
# # print(word)
# for i in word[:]:
#     if len(i)> 4:
#         word.insert(1, i)   #(0,i)- it will replace the last value in 0th place
#         print(word)
# words= 'Name'
# for i in words:
#     print(i, len(i))

# temperature = float(input('What is the temperature? '))
# if temperature > 70:
#     print('Wear shorts.')
# else:
#     print('Wear long pants.')
# print(' And Get some exercise outside.')



# def calweeklywages(totalHours, hourlyWage):
#     '''Return the total weekly wages for a worker working totalHours,
#     with a given regular hourlyWage.  Include overtime for hours over 40.
#     '''
#     if totalHours <= 40:
#         totalWages = hourlyWage*totalHours
#     else:
#         overtime = totalHours - 40
#         totalWages = hourlyWage*40 + (1.5*hourlyWage)*overtime
#     return totalWages
#  
# def main():
#     hours = float(input('Enter hours worked: '))
#     wage = float(input('Enter dollars paid per hour: '))
#     total = calcWeeklyWages(hours, wage)
#     print('Wages for {hours} hours at ${wage:.2f} per hour are ${total:.2f}.' .format(**locals()))
# main()


# ''' Write a program sign.py to ask the user for a number. Print out which category the number is in: 'positive', 'negative', or 'zero'.'''
# 
# num= float(input('Ente a number: '))
# if num ==0:
#     print ('The number is "Zero"')
# elif num>0:       
#     print('The number is "Positive"')
# else:
#     print('The Number is "Negative"')
#         
        
# ''' headstail example and strange fuction ex   ??? '''

# def calweeklywages(totalhours, hourlywage):
#     if totalhours <=40:
#         totalwages = totalhours*hourlywage
#     else:
#         overtime= totalhours-40
#         totalwages= hourlywage*40 + (1.5*hourlywage)*overtime
#     
#     if totalhours <=60:
# #         totalwages = totalhours*hourlywage
# #     else:
#         doubletime= totalhours -overtime
#         totalwages= hourlywage*40 +(1.5*hourlywage)*overtime + (2*hourlywage)*doubletime
#     else:
#         pass
#     return totalwages
# 
# def main():
#     total_hours= float(input('Enter hours worked: '))     
#     wage= float(input('Enter hourly rate: '))   
#     total= calweeklywages(total_hours, wage)
#     print('Wages for {total_hours} hours at ${wage:.2f} per hour are ${total:.2f}.' .format(**locals()))
# main()     


# if hours <= 40, then $10

#code

# if hours 40 < hours<= 60, then $10*1.5

#code

# if hours > 60, then $10

#code


# def calweeklywages(totalhours, hourlywage):
#  ''' Calculate weekly wages'''   
#     upto40 = 0
#     fortyto60 = 0
#     sixtyplus = 0
#     if totalhours > 60:
#         sixtyplus = totalhours - 60
#         fortyto60 = 20
#         upto40 = 40
#     
#     if 40 < totalhours <=60:
#         fortyto60 = totalhours - 40
#         upto40 = 40
#     if totalhours <= 40:
#         upto40 = totalhours
#         
#     return (sixtyplus*2 +fortyto60*1.5 + upto40)*hourlywage
#     
# 
# 
# 
# def main():
#     total_hours= float(input('Enter hours worked: '))     
#     wage= float(input('Enter hourly rate: '))   
#     total= calweeklywages(total_hours, wage)
#     print('Wages for {total_hours} hours at ${wage:.2f} per hour are ${total:.2f}.' .format(**locals()))
# main()     

''' print all positive numbers'''
# def positivenum(num_list):
#     
#     for num in num_list:
#         if num>0:
#             print(num)
# positivenum= float(input('enter number list '))
# # positivenum ([9, -7, -19, 89, 57]   
# 
# def even(num):
# for num in range(2,10):
#     if num % 2 ==0:
#         print(num)
# even ([2, 4, 5, 7, 9, 10])  


      
# senator>=30
# us citizen >=9
# us representative >=25
# us citizen >=7
# 
# house and senate when age=30+ and Us citizen = 9+ (eligible)
# house when age= 25+ and us citizen= 7+ (eligible)
# congress when age=<25 and citizen<7 (not eligible)

# age= float(input('how old are you? '))
# us_citizen= float(input('for how long you have been a US citizen? '))
# if age>=30 and us_citizen>=9:
#     print('Your are eligible for both')
# elif age>=25 and us_citizen>=7:
#     print('Your are eligible for the house')
# else:
#     print('You are not eligible for congress')    
# 
# '''if __name__=="__main__"
#     main()   #way of calling a def main()'''

# '''calculate power'''
# def power(num, x=1):
#     result =1
#     for i in range(x):
#         result= result*num
#     return result
# 
# print(power(2))    
# print (power(2,3))
# 
# 
# ''' adding different arguments ('*' character means i can pass in a variable number of arguments)'''
# def multi_add(*args):
#     result=0
#     for x in args:
#         result = result+ x
#     return result
# 
# print(multi_add(10, 3, 6, 8, 90))

'''print cube'''
# def cube(num):
#     return num*num*num
# 
# print(cube(10))


# # def main():
# x, y= 200, 1000
#  
# if (x > y):
#     st= "x is greater than y"    
# elif (x == y):
#     st="x is same as y"
# else:
#     st="x is less than y"
# print (st)
#      

''' while loop'''
# def main():
# x=0
# while(x<5):
#     print(x)
#     x=x+1

'''range function'''
# for x in range(5,10):
#     print (x)
#     

'''list'''
# list=["abc", "xyz", "asdf", "jkl"]
# # for l in list:
# print(list[1:4]) 
# list.append("poi")
# print(list)   
# print(list[0][1])


'''break and continue statement'''
# for x in range(5,10):
#     if(x==7):
#         break
#     print(x)
# #     if (x % 2 == 0): continue
# #     print (x)

'''enumerate() function to get index'''
# list=["abc", "xyz", "asdf", "jkl"]
# for i, l in enumerate(list):
#     print(i,l)


'''classes'''
# class myClass():
#     def method1(self):
#         print ("myClass method1")
#     
#     def method2(self, someString):
#         print("myClass method2" + someString)
#         
# class anotherClass(myClass):        #class inheritence
#     def method1(self):
#         myClass.method1(self)     #(inherited method on the superclass, this will print result "myClass method1")
#         print("anotherClass method1")
#      
#     def method2(self):
#         print("anotheClass method2")        
#          
# def main():
#     c = myClass()
#     c.method1()
#     c.method2(" this is a string")
#     
#     c2 = anotherClass()
#     c2.method1()
#      
#     
# main()
#     
    
    
'''date and time and datetime classes'''
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta   #timedelta is a span of time, used to perform time based mathematics
# today= date.today()
# print("Today's date is- ", today)
# 
# print("Date components: ", today.day, today.month, today.year)
# print("today's weekday is- ", today.weekday())  #retrieve today's weekday, here monday=0
# days=["mon", "tues", "wed", "thu", "fri", "sat", "sun"]
# print("Which is a- ", days[today.weekday()])

# today=datetime.now()
# print("The current date and time is- ", today)
# t= datetime.time(datetime.now())
# print(t)

'''formatting time output'''
# now= datetime.now()
# print(now.strftime("%a, %d  %B, %Y"))   #%a/%A= weekday, %d= date, %b/%B=month, %y/%Y=year
# 
# print(now.strftime("locale date and time is- %c"))    # %c- local date and time, %x is date and %X is time
# print(now.strftime("locale date is- %x"))
# print(now.strftime("locale time is- %X"))

# print(now.strftime("Current time is- %I:%M:%S %p"))  #%I-12 hour format, %H-24 hour format, %M- for minutes, %S- for seconds, %p- AM/PM
# print(now.strftime("24 Hour time- %H:%M"))
# print(now.strftime("Current time is- %I:%M %p"))

'''using timedelta objects''' #firts import timedelta lib (from timedate import timedelta)
# print(timedelta(days=365, hours=5, minutes=1))
# now= datetime.now()
# print("today is: " + str(now))
# 
# print("One year from now will be- " + str(now + timedelta(days=365)))
# print("In 2 days 3 weeks it will be- " + str(now + timedelta(days=2, weeks=3)))

# t= datetime.now()- timedelta(weeks=1)
# s= t.strftime("%A, %B %d, %Y")
# print("One week ago it was- " + s)


#how many days untill next april fool's day
# today= date.today()
# afd= date(today.year, 4, 1)
# if afd < today:
#     print("April fool's day already went by %d days ago" %((today-afd).days))
# afd = afd.replace(year=today.year + 1)
#     
# time_to_afd= afd-today
# print("It's just", time_to_afd.days, "days untill next April fool's day")
 
 
'''working with calenders'''
# import calendar
# 
# c= calendar.TextCalendar(calendar.SUNDAY)
# st= c.formatmonth(2018, 2)
# print(st)
# # calendar.prcal(2018)    #print calendar of whole year
# print(calendar.isleap(2019))    #check true or false if year is leap year 

# def leapyr(n):
#     if n%4==0 and (n%100!=0 or n%400==0):
#         print( n, " is a leap year.")
#     elif n%4!=0:
#         print( n, " is not a leap year.")
#     else:
#         pass
# leapyr(2020)


#html formatted calendar
# hc= calendar.HTMLCalendar(calendar.SUNDAY)
# st= hc.formatmonth(2018,6)
# print(st)

# for i in c.itermonthdays(2018, 6):
#     print(i)
    
# for name in calendar.month_name:
#     print(name)
# for day in calendar.day_name:
#     print(day)
    
''' I had a team of people, and the team met on the first Friday of every month, 
and I wanted to write a script that would print out what those dates would be for the upcoming year'''
    
# print("Team meetings will be on:")
# for m in range(1,13):
#     cal= calendar.monthcalendar(2018, m)
#     weekone= cal[0]
#     weektwo= cal[1]
#     
#     if weekone[calendar.FRIDAY] != 0:
#         meetday= weekone[calendar.FRIDAY]
#     else:
#         meetday= weektwo[calendar.FRIDAY]
#         
#     print("%10s %2d" %(calendar.month_name[m], meetday))
#   
'''expressions and statements'''
# expressions are eg:
# x=y assignmnet operator
# x*y multiplication operator
# f() function call
# (x,y) list
# x simple variable
# True builtin functiom
# etc

# statements:
# import platform
# version= platform.python_version()
# print('This is Python version {}'.format(version))

'''iterators''' #An iterator is an object that can be iterated (looped) upon.
'''generators'''# generator is a function which returns a generator iterator (just an object we can iterate over) by calling yield and are used if you dont want to load all the data in the memory.
                #generator function returns a generator object, and that generator object will yield a value
# def my_generator():
#     print("inside my generator")
#     yield 'a'
#     yield 'b'
#     yield 'c'
# 
# my_generator()
# itr=my_generator()
# next(itr)

# for char in my_generator():
#     print(char)
    

# def even_num(n):
#     for i in range(n):
#         if i%2==0:
#             yield i

# print(even_num(10))
# print(list(even_num(10)))
###or
# integers = even_num(10)
# print(next(integers))   #0
# print(next(integers))   #2
# print(next(integers))   #4
# print(next(integers))   #6
# print(next(integers))   #8
# print(next(integers))   #stops iteration
###or
# for n in integers:
#     print (n)
# ###or
# for n in even_num(10):
#     print(n)

# for n in(i for i in range(10)):
#     print(n)
#     
# max((i for i in range(10)))
#     print(n)

'''generator expression--(item.upper() for item in colletion)'''
# even_num= (n for n in range(10) if n%2==0)
##example1 
# num= [7,10, 9.0, 10.90, 00.90, '3', '7', 99.79]
# integers= (int(n) for n in num) #coverts num to int using generator expression
# print(integers)
# print(next(integers))
##or
# for i in integers:
#     print(i)

##example2
# name_list= ['adam', 'ali', 'zain', 'john']
# uppercase_name= (name.upper() for name in name_list)
# print(list(uppercase_name))
##or
# for i in uppercase_name:
#     print(i)
##or
# reverse_uppercase= (name[::-1] for name in (name.upper() for name in name_list))
# print(list(reverse_uppercase))
###fibo example using generator
# def fibo_gen():
#     a, b= 0,1
#     while True:
#         yield b
#         a, b= b, a+b
#         
# 
# fib= fibo_gen()
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# for _ in range(10):
#     print(next(fib))




# import math
# n=10
# fact = str(math.factorial(n))
# print(fact)
# add_num = 0
# for i in fact:
#     add_num = add_num + int(i)
# print(add_num)





  
'''args (variable length argument list)'''
# def main():
#     kitten('pet', 'animal', 'wildcat', 'pussy')    #1st way
#     x= ('pet', 'animal', 'wildcat', 'pussy')    #2nd way
#     kitten(*x)                                    #2nd way calling
# def kitten(*args):
#     if len(args):
#         for a in args:
#             print(a)
#     else:
#         print('meow!!')
# 
# main()

'''kwargs (keyword arguments has two asterisk **)'''
# def main():
#     animal(lion ='roar', cat='meow', dog='bark')    #1st way
#     x= dict(lion ='roar', cat='meow', dog='bark')   #2nd way
#     animal(**x)                                      #2nd way calling
# def animal(**kwargs):
#     if len(kwargs):
#         for a in kwargs:
#             print('{} - {}'.format(a, kwargs[a]))
#     else:
#         print('No values given')
# 
# main()




# def fib(n):
#     a,b=0,1
#     while a<n:
#         print(a, end='    ')
#         a, b=b, a+b
#     print()
#     
# def main():
#     f=fib
#     f(1000)
# 
# main()
'''add multiples of 3 or 5'''
# multiple_add = 0
# for i in  range(1, 1000):
#     
#     if i%3==0 or i%5==0:
#         multiple_add+=i
# 
# 
# print (multiple_add)


'''highest prime factor of number'''
# n=13195        #600851475143
# def is_prime(x):
#     count=0
#     for i in range(1, x+1):
#         if x%i==0:
#             count=count+1
#             if count==3:
#                 return False
#     if count == 2:
#         return True        
#              
# for i in range(1,n+1):
#     if n%i==0:
#         if is_prime(i):
#             print(i)


'''palindrome number'''
# x=9009
# def is_palindrome(x):
#     x = str(x)
#     if x == x[::-1]:
#         return True
#     
#     return False
#       
#             
# print (is_palindrome(x))

'''largest palindrome product'''
# max_num =0
# for a in range(100, 1000):
#     for b in range(100, 1000):
#         c=a*b 
# 
#         c=str(c)          #1*98, 2*98, 3*98
#         if c==c[::-1]:
#             if int(c) > max_num:
#                 max_num = int(c)
#                 
# print(max_num)
 
 
'''smallest multiple'''

# def is_multiple(x):
#     for i in range(1, 10):  #checks every num from 1 to 9 to see if x is a multiple of every num
#         if x%i!=0:
#             return False
#         else:
#             return True #found if x is multiple of every num
#     x=x+1
# print (is_multiple(12))



'''Sum square difference'''
 
# def sum_of_squares(n):
#     return sum([i*i for i in range(1, n+1)])    #(1+4+9+....100)=385
#  
# print(sum_of_squares(100))   
#      
#  
# def square_of_sum(n):
#     return sum(range(1, n+1)) ** 2    #(1+2+3+....10)**2=(55)**2=3025
#  
# print (square_of_sum(100))
#   
# print (square_of_sum(100) - sum_of_squares(100))
 
 
'''summation of primes'''
# addprime=0
# for x in range(3, 10,2):
#     no_prime = 0
#     for i in range(3, x,2):
#         if (x%i==0):
#             no_prime= 1
#             break
#     if not no_prime:
#         addprime+=x
# print(addprime)

#         addprime= addprime+ x
#         print(addprime)
#       
#     if :
#         add_prime=addprime+x
#  
# print(addprime)

# '''count=1 count will check untill the nth num
#     
# num=1 return 1
# num =2 return 2
# num=3 return 3
# num =4 return 5
# num =5 return 7
# ....
# num=10 return 23 
# '''
# n=13195        #600851475143
# def is_prime(x):
#     count=0
#     for i in range(1, x+1):
#         if x%i==0:
#             count=count+1
#             if count==3:
#                 return False
#     if count == 2:
#         return True        
# print(is_prime(11))
# count=0
# x=1
# if count<=x:
#     x=x+1
#     if is_prime(x):
#         count+=1
#       
# print(is_prime(13195))


# num=10
# add_num=0
# factorial=1 
# for i in range(1, num+1):
#     factorial = factorial*i
# print(factorial)    




# n=10001
# def nth_prime(n):
#     count =0
#     num=1
#     while count<=n:
#         num=num+1
#         if is_prime(num):
#             count=count+1
#     return num
# 
# def is_prime(n):
#      
#     for i in range(2, n+1):
#         if n%i==0:
#             return False
#         else:
#             return True
# # print(is_prime(11))    
# print(nth_prime(10001))    #0th prime=3, 1st prime=5, 2nd =7
 
 
'''pythogorean triplet'''    
#a<b<c
# s=1000
# for a in range(1, s):
#     for b in range(a+1, s):
#         c=(s-a-b)
#         if(a*a + b*b == c*c):
#             print(a, b, c)
#             print(a*b*c)


'''summation of primes'''
# number=10
# prime= []
# for i in range(2, number+1):
#     prime.append(i)     #all numbers appended in prime[] i.e 2, 3, 4, 5,...........
# # print(prime)
# i=2
# while(i<= number):
#     if i in prime:  #if i is in the list 
#             for j in range(i*2, number+1, i):   #then deleting the multiples of i, 2*2=4 delete; 2*4=8 del; 3*2=6 del; 3*3=9 del;
#                 if j in prime:
#                     prime.remove(j) ##deleting the multiple if found in list
# i=i+1
# print(prime)

 

 
# n=15
# add_power=0
# for i in range(1, n+1):
#     x =2**i
#     for i in x:
#        add_power+=i
# print(x)
# print(add_power)
#   
#   
#

add_digit=0 
x=2**1000 
print(x)
for a in str(x):
    add_digit+= int(a)
print(add_digit) 

 
 
 
 
 
 
 
 
 
    
