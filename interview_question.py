import os
import csv
from collections import defaultdict,Counter,deque
from itertools import islice


#**1. Write a program to find the length of the string without using inbuilt function (len)**
'''
s = "HELLO WORLD"
count = 0
for ch in s:
    count += 1
    
print(count)

s.count(ch)
'''
##**2. Write a program to reverse a string without using any inbuilt functions.**
'''
s = 'hello world'
res = ''
for ch in s:
    res = ch + res
print(res)
'''
##3.**3. Write a program to replace one string with another. e.g. "Hello World" replaces "World" with "Universe".**
'''
s = 'hello world'
print(s.replace('world','universe'))

l=s.split()
l2 = [ 'universe' if word == 'world' else word for word in l]
print(' '.join(l2))
'''
###**4. How to convert a string to a list and vice-versa.**
'''
s = 'hello world'
l = list(s)
print(l)

l2 = []
for ch in s:
    l2.append(ch)
print(l2)

print(''.join(l2))

res = ''
for ch in l:
    res += ch
print(res)
'''
##**5. Convert the string "Hello welcome to Python" to a comma separated string.**
'''

s = "Hello welcome to Python"
l = list(s)
print(','.join(l))

s2 = ''
for ch in s:
    s2 +=  ch+','
print(s2)
    

l1 = s.split()
print(','.join(l1))

s1 = s.replace(' ',',')
print(s1)

'''
###**6. Write a program to print alternate characters in a string.**
'''
s = "Hello welcome to Python"
print(s[::2])


for i in range(len(s)):
    if i % 2 == 0:
        print(s[i], end = ' ')

'''
### **7. Write a Program to print ascii values of the characters present in a string.**
'''
s = 'jeeviTHa'
for ch in s:
    print(ord(ch))
'''

###**8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.**
'''
s = 'jeeviTHa'

res = ''
for ch in s:
    if ord('a') <= ord(ch) <= ord('z'):
        res = res + chr(ord(ch)-32)
    elif ord  ('A') <= ord(ch) <= ord('Z'):
        res = res + chr(ord(ch)+32)
    else:
        res = res + ch
print(res)        
        
s1 = ''
for ch in s:
    if ch.islower():
        s1 = s1 + chr(ord(ch)-32)
    elif ch.isupper():
        s1 = s1 + chr(ord(ch)+32)
    else:
        s1 = s1 + ch
print(s1)

'''
##**9. Write a program to swap two numbers without using the 3rd variable.**
'''
a =12
b= 23
a,b =b,a
print(a)
print(b)
'''
##**10. Write a program to merge two different lists.**
'''
l1 = [1,4,6,88,4,3]
l2 = ['jeevi' ,'trht','ghut']
print(l1+l2)

l1.extend(l2)
print(l1)
'''
###**11. Write a program to read a random line in a file. (ex. 50, 65, 78th line)**

import os
os.chdir(r'C:\Users\kiran\Desktop\python_practice\files')
from collections import deque, defaultdict,Counter
from itertools import islice
'''
n = 4
with open('access_log.txt') as file:
    for line_no,line in enumerate(file,start=1):
        if line_no == n:
            #print(line)
    
'''

##**12. Write a program to read random lines in a file. (ex. I want read all lines 10th to 15th line)**
'''
s = 10
e = 15
with open('access_log.txt') as file:
    for line_no, line in enumerate(file,start = 1):
        if s <= line_no <= e:
            #print(line)

with open('access_log.txt') as file:
    lines = islice(file,s-1,e)
    for line in lines:
        #print(line)

'''
###**13 Program to print the last "N" lines of a file.**
'''
n= 6
with open('access_log.txt') as file:
    line_count = 0
    for _ in file:
        line_count += 1
    file.seek(0)
    lines = islice(file,line_count - n, line_count)
    for line in lines:
        #print(line)

with open('access_log.txt') as file:
    lines = deque(file,n)
    for line in lines:
        #print(line)
'''
## **14. Write a program to check if the given string is Palindrome or not without using reversed method.**
'''
s = 'maam'
res = ''
for ch in s:
    res = ch + res
if s == res:
    print('string is palindrome')
else:
    print('string is not palindrome')

if s == s[::-1]:
    print('string is palindrome')
else:
    print('string is not palindrome')
'''
###**15 Write a program to search for a character in a given string and return the corresponding index.

'''
s = "Hello welcome to Python"
ch = 'o'
for i,in range(len(s)):
    if ch == s[i]:
        print(i, end = ' ' )
'''

#16. Write a program to get the below output
'''
sentence = "hello world welcome to python programming hi there"
#d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }

d = {}
for word in sentence.split():
    if word[0] not in d:
        d[word[0]] = [word]
    else:
        d[word[0]] += [word]
print(d)

from collections import defaultdict
dd =defaultdict(list)
for word in sentence.split():
    dd[word[0]] += [word]
print(dd)
'''

##**17 Write a to replace all the vowel characters with - if the character occurs more than once in a string**
##```python
##my_string = 'hellohai' # O/P should be '-e--o-ai'
'''
my_string = 'hellohai'
res = ''
for ch in my_string:
    if ch not in "aeiouAEIOU":
        res = res + '-'
    else:
        res = res + ch
print(res)
'''
#**18 write a decorator that returns only positive values of subtraction**
'''
def outer(func):
    def wrapper(*args,**kwargs):
        return abs(func(*args,**kwargs))
    return wrapper
@outer
def sub_(a,b):
    return a-b
print(sub_(7,9))
'''
#**19 How to get the count of the number of instances of a class that is being created.**
class Point:
    count=0
    def __init__(self):
        Point.count+=1
p1=Point()
p2= Point()
p3=Point()
print(Point.count)
#**20 Write a function which takes a list of strings and integers.If the item is a string it should print as is and if the item is integer or float it should reverse it.**
'''
l = ['jeevitha' , 12.56, 'divya' , 45, 'pooja', 78.345]
def func_(l):
    for word in l:
        if isinstance(word, str):
            print(word)
        elif isinstance(word, (int,float)):
            print(str(word)[::-1])
func_(l)
'''         
            
#**21 Write a class named Simple and it should have iteration capability.**
class Simple:
    def __init__(self, iterable):
        self.iterable=iterable
    def __iter__(self):
        return iter (self.iterable)
s=Simple("hello")
print(s)
#**22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a**
class Simple:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __getitem__(self,index):
        return self.__dict__.get(index, 'key does not exist')
s=Simple(10,20)
print(s.a)   #10
print(s['a']) #10

#**23 Write a python program to get the below output**
'''
sentence = "Hi How are you" 
#o/p should be "iH woH era uoy"
res= ''
for word in sentence.split():
    res = res +  word[::-1] + ' '
print(res)

l = []
for word in sentence.split():
    l.append(word[::-1])
print(' '.join(l))

'''
#**24 Write a python program to get the below output**
'''
sentence = "Hi How are you" 
#o/p should be "ouy era woH iH"
l = sentence.split()
l1 = []
for word in l[::-1]:
    l1.append(word[::-1])
print(' '.join(l1))
'''

#**25 Write a lambda function to add two numbers (a, b)**
'''
c= lambda a,b: a+b
print(c(1,4))
'''

#**26 What is the output of the following**
'''
a = [1, 2, 3]
b = [4, 5, 6]
print([a, b])
print((a, b))
#[[1, 2, 3], [4, 5, 6]]
#([1, 2, 3], [4, 5, 6])
'''
#**27 How to remove duplicates from the list without using inbuilt functions**
'''
l = [1, 2, 3, 4, 1, 2, 3, 4, 5]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i] == l[j]:
            print(l[i])
            
l= [1, 2, 3, 4, 1, 2, 3, 4, 5]
k=[]
for i in l:
    if i not in k:
        l.append(i)
print(l)            

'''

#**28 Find the longest word in the sentence**
'''
s = "hai how are python is a programming language"
l = s.split()
smallest,*res, longest= sorted(l,key = len)
print(longest)
'''


#**29 write a program to reverse the values in the dictionary if the value is of type String**
'''
d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
d1 = {}
for key, value in d.items():
    if isinstance(value ,str):
        d1[key] = value[::-1]
    else:
        d1[key] = value
print(d1)
'''
        
#**30 write a program to get 1234
'''
t = ('1', '2', '3', '4')
res = ''
for i in t:
    res += i
print(res)
'''
#**31 How to get the elements that are in list b but not in list a**
'''
a = [1, 2, 3]
b = [1, 2, 3, 4]
c=set(a)
d=set(b)
print(list(d.difference(c)))  # print(list(set(b)-set(a)))

for item in b:
    if item not in a:
        print(item)
'''
##**32 A function takes variable number of positional arguments as input. How to check if the arguments that are passed are more than 5**
'''
def func_(*args,**kwargs):
    if len(args) > 5:
        return 'posithinal argument passed more than 5'
    else:
        return 'positional argument passed less than 5'
print(func_(1,2,3,5,9,6))
        
'''
#**33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**
#```python
# Assume Below is the contents of the log file
'''
lines = """CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical"""
'''

path = r'C:\Users\kiran\Desktop\in_q.log'
with open(path) as file:
    d = {}
    for line in file:
        if line.strip():
            l = line.split()
            if l[0] not in d:
                d[l[0]] = 1
            else:
                d[l[0]] += 1
    #print(d)
                        

##**34 Write a function to reverse any iterable without using reverse function.


#**35 Write a function to print the below output.**
# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX
'''
def func(s,n):
    if n == 0:
        return s[1::2]
    elif n == 1:
        return s[::2]
print(func("TRACXN", 0))
print(func("TRACXN", 1))

'''

#**36 Sum all the numbers in the below string.**
'''
s = "Sony12India567Pvt2ltd"
from re import findall
result = findall(r'[0-9]+',s)
sum_ = 0
for n in result:
      sum_ += int(n)
print(sum_)


s1 = ''
sum_=0
for i in range(len(s)-1):
    if s[i].isalpha() and s[i+1].isdigit():
        s1 = s1 + s[i] + ','
    elif s[i].isdigit() and s[i+1].isalpha():
        s1 = s1 + s[i] + ','
    else:
        s1 = s1 + s[i]
for i in s1.split(','):
    if i.isdigit():
        sum_ += int(i)
print(sum_)
        
'''       

#**37 Write a program to sum all the numbers in below string.**
'''
s = "Sony12India567Pvt2ltd" # eg.12+567+2
from re import findall
result = findall(r'[0-9]+',s)
sum_ = 0
for n in result:
      sum_ += int(n)
print(sum_)
'''
#**38 Print all the numbers in the below list**
'''
a = ['abc', '123', 'hello', '23']
for word in a:
    if word.isdigit():
        print(word)
'''
#**39 Program to print the number of occurrences of characters in a String without using inbuilt functions.**
'''
s = 'hai hello how are you'
d = {}
for ch in s:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] += 1
print(d)
        
from collections import defaultdict
dd = defaultdict(int)
for ch in s:
    dd[ch] += 1    
print(dd)

'''
#**40 Program to print only the repeated characters and count of the same.**
'''
s = 'hai hello how are you'
d = { ch : s.count(ch) for ch in s if s.count(ch) > 1}
print(d)

from collections import defaultdict
dd = defaultdict(int)
for ch in s:
    if s.count(ch)>1:
        dd[ch] = s.count(ch)
print(dd)
'''       

#**41 Write a program to get alternate characters of a string in list format.**
'''
s = 'hai hello how are you'
a = s[1::2]
l = list(a)
print(l)


l1 = []
for i in range(len(s)):
    if i % 2 == 1:
        l1.append(s[i])
print(l1)
'''        

##**42 Write a program to get square of list of number's using lambda function .**
'''
l = [1,4,7,9,4,6,8,11,45]
a = lambda n: [ i**2 for i in n]
print(a(l))
'''

##**43 Write a function that accepts two strings and returns True if the two strings are anagrams of each other.**

'''
def func_(s1,s2):
    a1 = ''.join(sorted(s1))
    a2 = ''.join(sorted(s2))
    if a1 == a2:
        return 'string is anagram'
    else:
        return 'string is not anagram'
print(func_('ate','tea'))
''' 
##**44 Write a program to iterate through list and build a new list, only if the items of the list has even number of characters.**
'''
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
l = [ ]
for item in names:
    if len(item) % 2 == 0:
        l.append(item)
print(l)
'''     

#**45 Write a program to iterate through list and build a new dictionary, only if the items of the list has even number of characters.**
'''
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
d = {}
for item in names:
    if len(item)% 2 == 0:
        if 'even' not in d:
           d['even'] = [item]
        else:
            d['even'] += [item]
    elif len(item) %2 == 1:
        if 'odd' not in d:
           d['odd'] = [item]
        else:
            d['odd'] += [item]
        
print(d)
'''
##**46 Write a program which squares the numbers in a list using map object**
'''
a = [1, 2, 3, 4, 5]
print(list(map(lambda n: n**2,a)))
'''

##**47 Count number of lines in a file without loading the file to the memory**

print(os.getcwd())
'''
with open('sample.txt') as file:
    count_line = 0
    for line in file:
        count_line += 1
    print(count_line)

'''
##**48 Printing line and line no's**
'''
with open('sample.txt') as file:
    for line_no,line in enumerate(file,start = 1):
        print(line_no, line, sep = ' -- ')
'''
##**49 Write a Program to print the sum of entire list and sum of only internal list**
'''
l = [[1,2,3],[4,5,6],[7,8,9]]
l1 = []
for item in l:
    int_sum = 0
    int_sum += sum(item)
    l1.append(int_sum)
print('internal list sum:' ,l1)
print('entire list sum:' , sum(l1))
'''
#**50 Write a program to reverse the list as below**
#words = ["hi", "hello", "python"]

#**51 Write a program to update the tuple**
'''
t1 = (1, 2, 3, 4)
t2 = (100, 200, 300)
# o/p (1, 2, 3, 4, 100, 200, 300)
t3 = (*t1,*t2)
print(t3)
'''

#**52 Write a program to replace value present in nested dictionary.**
# Replace "nose" with "net"
'''
d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}

d1 = {}
for key,value in d.items():
    if isinstance(value,dict):
        for k,v in value.items():
            if v == 'nose':
                value[k] = 'net'
            else:
                value[k] = v
            d1[key]= value
    else:
        d1[key] = value
print(d1)
'''

#**53 Write a program to count the number of white spaces in a file.**


#**54 Grouping anagrams.**
'''
words = ['eat','ate','tea','hello','silent','listen']
d = {}
for word in words:
    w = "".join(sorted(word))
    if w not in d:
        d[w] = [word]
    else:
        d[w] += [word]
print(d)

from collections import defaultdict
dd = defaultdict(list)
for word in words:
    key = "".join(sorted(word))
    dd[key] += [word]
print(dd)
'''
#**55 What is the difference between defaultdict and normal dictionary.**
#```python
"""
Defaultdict
-----------
1. When each key is encountered for the first time, it will not be there in the mapping.
2. So an entry is automatically created with default value (an empty list in case of defaultdict of list and zero in case of defaultdict int).
3. When keys are encountered again, the look-up proceeds normally as like a normal dictionary.
4. So, in defaultdict, creation of key, initialisation will happen simultaneously. 
Normal Dictionary
------------------
1. In case of normal dictionary, if the key does not exist, "KeyError" is raised. 
2. In order to work on the value, first the key needs to be created and initialised.
"""
#```
#**56 Explain property decorator in python.**
#**57 What is Mutable and Immutable datatypes.**
#```python
"""
1. Mutable datatypes are objects whose value can be changed after creation. e.g. list, dict, set, user defined classes.
2. Immutable datatypes are objects whose value can not be changed after creating. e.g. int, float, bool, tuple, namedtuple
"""
#```
#**58 Explain get() method in dictionaries.**
#```python
"""
point =  {'a': 1, 'b': 2}
1. Values of dictionary can be accessed in two different ways. using square bracket syntax and the other one is using get() method.
2. When we try to access a key of a dictionary which does not exist using square bracket syntax (point['c']), "KeyError" exception is raised.
3. When we try to access a key of a dictionary which does not exist using get() method (point.get('c')), None is returned and no exception is raised.
4. We can pass a positional argument to get() method as custom message, so that get() method returns the custom message if the key does not exist.
           e.g. profile.get('c', 'Sorry the key does not exist')
"""
#```
#**59 Write a list comprehension to get a list of even numbers from 1-50**
'''
l = [i for i in range(1,51) if i %2 == 0]
print(l)
'''
#**60 Find the longest non-repeated substring in the below string**
'''
s = 'hai hello python is a programming language programming is fun'
l =[]
for word in s.split():
    if word not in l:
        l.append(word)
smallest,*res,longest = sorted(l,key = len)
print(longest)

l1 = s.split()
l1.sort(key = len)
smallest,*res,longest = l1
print(longest)
'''
#**61 Write a program to find the duplicate elements in the list without using inbuilt functions**
'''
names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
for i in range(0,len(names)):
    for j in range(i+1,len(names)):
        if names[i] == names[j]:
            print(names[i])
print()
##inbuilt
for word in set(names):
    if names.count(word) > 1:
        print(word)

'''
#**62 Write a program to count the number occurrences of each item in the list without using any inbuilt functions**
'''
names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
d= {}
for word in names:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
print(d)

from collections import defaultdict
dd = defaultdict(int)
for word in names:
    dd[word] += 1
print(dd)

d = { word : names.count(word) for word in names}
print(d)
'''
#**63 Write a function to check if the number is Prime**
'''
n = 6
def prime_(n):
    for i in range(2,n):
        if n % i == 0:
            return f'{n} is not a prime number'
    return f'{n} is a prime number'
print(prime_(n))
print(prime_(7))
'''

#**64 How to create a tuple of numbers from 0 to 10 using range function**
'''
t = ( i for i in range(0,11))
print(tuple(t))

'''
#**65 Write a program to find the largest number in the list without using any inbuilt functions**
'''
l = [1,5,8,0,23,56,87,90,23]
max_ = 0
for n in l:
    if max_ < n:
        max_ = n
print(max_)

small,*res,largest = sorted(l)
print(largest)

l = [1,5,8,0,23,56,87,90,23]
for _ in range(len(l)-1):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
print(l[-1])

'''
#**66 Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) should return 2.**
'''
def get_last_digit(n):
    ld = 0
    ld = n % 10
    return ld
print(get_last_digit(3572))
'''
#**67 Write a program to find most common words in a given list.**
'''
words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes','the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the','eyes', 'look', 'into','my', 'eyes', "you're", 'under']
d = {word : words.count(word) for word in words}
l = sorted(d.items(),key = lambda item: item[-1])
print(l[-1])

from collections import Counter,defaultdict
c = Counter(words)
#print(c)
print(c.most_common(1))
'''
#**68 Make a function named tail that takes a sequence (like a list, string, or tuple) and a number n and returns the last n elements from the given sequence, as a list.**
'''
def tail(sequence,n):
    return sequence[-n::]
print(tail('hello',3))
print(tail([1,4,6,7,9,3],3))
print(tail((1,4,6,3,5,7),3))
'''

#**69 Write function named is_perfect_square that accepts a number and returns True if it's a perfect square and False if it's not.**
'''
n = 64
def is_perfect_square(l,n):
    for i in l:
        if i*i == n:
            return True
    else:
        return False
print(is_perfect_square(range(0,n),n))
-----------
from math import sqrt
def solve(n):
    sq_rt = int(sqrt(n))
    return (sq_rt** sq_rt) == n
print(solve(36))

'''
#**70 Write a program to get all the duplicate items and the number of times the item is repeated in the list.**
'''
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
d = { word: names.count(word) for word in names}
print(d)
--------
d = {}
for word in names:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
print(d)
-----------
from collections import defaultdict
dd = defaultdict(int)
for word in names:
    dd[word] += 1
print(dd)

'''
#**71 Write a program to count the number of occurrences of each word in a file.**
'''
from collections import defaultdict
dd = defaultdict(int)
with open('sample.txt') as f:
    for line in f:
        if line.strip():
            l = line.split()
            for word in l:
                dd[word] += 1
print(dd)

'''

#**72 Write a program to count the number of occurrences of vowels in a file.**
'''
from collections import defaultdict
dd = defaultdict(int)
with open('sample.txt') as f:
    for line in f:
        if line.strip():
            for ch in line:
                if ch.lower() in "aeiou":
                    dd[ch] += 1
print(dd)
'''
#**73 Write a program to print all numeric values in a list**
'''
items = ['apple', 1.2, 'google', '12.6', 26, '100']
for word in items:
    if isinstance(word ,(float,int)):
        print(word) 
'''
#**74 Triangle Patterns**

'''
*         
* *       
* * *     
* * * *   
* * * * *
'''
for row in range(0,6):
    print('* ' *row)
print()
'''
        * 
      * * 
    * * * 
  * * * * 
* * * * *
'''
for row in range(0,6):
    print(f'{"* " *row:>10}')
print()

'''
    *     
   * *    
  * * *   
 * * * *  
* * * * *
'''
for row in range(0,6):
    print(f'{"* " *row:^10}')
print()
'''
* * * * * * 
* * * * * 
* * * * 
* * * 
* *   
*
'''
for row in range(6,0,-1):
    print(f'{"* " *row}')
print()

'''
* * * * * * 
  * * * * * 
    * * * * 
      * * * 
        * * 
          *
'''
for row in range(6,0,-1):
    print(f'{"* " *row:>12}')
print()

'''

 * * * * * *
  * * * * * 
   * * * *  
    * * *   
     * *    
      *
'''
for row in range(6,0,-1):
    print(f'{"* " *row:^12}')
print()


'''
1    
12   
123  
1234 
12345
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=' ')
    print()
    
pat =''
for row in range(1,6):
    pat = pat + ' ' + str(row)
    print(pat)
print()

'''
    1
   12
  123
 1234
12345
'''
pat =''
for row in range(1,6):
    pat = pat + ' ' + str(row)
    print(f'{pat:>10}')
print()


'''

     1    
    1 2   
   1 2 3  
  1 2 3 4 
 1 2 3 4 5
'''
pat =''
for row in range(1,6):
    pat = pat + ' ' + str(row)
    print(f'{pat:^10}')
print()

#**75 Write a program count the occurrence of a particular word in the file**
'''
s = 'hello'
with open('sample.txt') as file:
    count_word = 0
    for line in file:
        if line.strip():
            l =line.split()
            for word in l:
                if word == s:
                    count_word += l.count(word)
    print(count_word)

dd =defaultdict(int)    
s = 'hello'
with open('sample.txt') as file:
    count_word = 0
    for line in file:
        if line.strip():
            l =line.split()
            for word in l:
                if word == s:
                    dd[word] += l.count(word)
print(dd)
'''



#**76 Write a program to map a product to a company and build a dictionary with company and list of products pair**
#>>> all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows', 
#                'iOS', 'Google Drive', 'One Drive']
#>>> # Pre-defined products for different companies
#>>> apple_products = {'iPhone', 'Mac', 'iWatch'}
#>>> google_products = {'Gmail', 'Maps', 'Google Drive'}
#>>> msft_products = {'Windows', 'One Drive'}


#**77 Write a program to rotate items of the list**
#>>> names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]

#**78 Write a program to rotate characters in a string**

#**79 Write a program to count the number of white spaces in a given string**
from re import findall
'''
s = 'the number of white spaces in a given string'
result = len(findall(r'\s',s))
print(result)


space_count = 0
for ch in s:
    if ch == ' ':
        space_count += 1
print(space_count)
'''
#**80 Write a program to print only non-repeated characters in a string**
'''
s = 'hello world'
for ch in s:
    if s.count(ch) == 1:
        print(ch)

l = [ ch for ch in s if s.count(ch) == 1]
print(l)

'''

#**81 What is the difference between a list and a tuple**
#```python
"""
1. The main difference between a list and a tuple is that list's are mutable and tuples are immutable.
2. Python over allocates memory for lists. The reason for over allocation of memory is to support append operation. 
Where as in tuples, memory is not over allocated, as tuples does not support append operation. 
(Since tuples are immutable, it does not support append operation). 
3. Tuples are more memory efficient than lists. (because in tuples no extra memory is allocated. It is fixed).
4. Tuples are negligibly faster than lists. 
"""

#**82 Write a program to print all the consonants in a given string**
'''
s = 'Python over allocates memory for lists  The reason for over allocation of memory is to support append operation'
result = findall(r'[^aeioAEIOU\s]',s)
print(result)

for ch in s:
    if ch.lower() not in 'aeiou' and ch != ' ':
        print(ch)
'''     

#**83 Write a program to count the number of commented lines in a text file**
#**84 Write a program to check if the year is leap year or not**
#```python
'''
>>> import calendar
>>> print(calendar.isleap(2012))
>>> True
>>> print(calendar.isleap(2013))
>>> False
>>> print(calendar.isleap(2016))
>>> True
#```
'''
#**85 Liner Search**

#**86 Difference between xrange and range**
#```python
"""
python2- xrange
python3- range
1. xrange does not stop, start and step attributes. But range object has start, stop and step attributes.
  Python-3
  r = range(0, 10)
  r.start
  r.stop
  r.step
   
  r = xrange(0, 10)
  In Python-2 The above attributes are not supported.
2. range Object supports slicing! But xrange does not support slicing
3. range object has __contains__ method implemented. So it supports membership testing. 
   But xrange does not implement __contains__ method. 
   So Python will iterate over each and every item in the range xrange object until it finds a match. 
   (So if you are searching for a number in range is faster than xrange)
4. range will accept integer of any size. But xrange objects accepts integer size equivalent to C long!
"""
#**87 Write a program to count no of capital letters in a string**


'''
**88 Write a program to get the below output**
* 
* * 
* 
* * * 
* 
* * * * 
* 
* * * * * 
```
**89 Write a program to get the below output**
```python
>>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
o/p:
>>> [1, 2]
    [3, 4]
    [5, 6]
    [7, 8]
    [9]
```
**90 Write a program to check if the elements in the second list is series of continuation of the items in the first list**
```python
a = [10, 12, 14, 16, 18]
b = [20, 22, 24, 26, 28]
a = [0, 5, 10, 15]
b = [20, 25, 30, 35, 40]
x = [10, 20, 30, 40]
y = [50, 40, 60, 70]
**91 What is the difference between append() and extend() method in list**
```python
"""
1. append() method appends one item at the end of the list.
2. extend() method appends all the items of the iterable to the end of the list.
3. Both append() and extend() method's mutates the existing list.
e.g. 
>>> a = [1, 2, 3]
>>> b = (4, 5, 6)
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6]
>>> c = {7, 8, 9}
>>> a.extend(c)
>>> a
[1, 2, 3, 4, 5, 6, 8, 9, 7]
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> a.extend(d)
>>> a
[1, 2, 3, 4, 5, 6, 8, 9, 7, 'a', 'b', 'c']
The list "a" is getting mutated each time when it is extended.
"""
```
**92 Write a program to find the first repeating character in a string**
**93 Write a program to find the index of nth occurrence of a sub-string in a string**
>>> sentence = "hello world welcome to python hello hi how are you hello there"
>>> index_nth_occurance(sentence, 'hello', 3)
>>> Start Index: 51, End Index: 56
**94 Write a program to print prime numbers from 1 to 50**
**95 Write a program to sort a list which has mix of both odd and even numbers, the sorted list should have odd numbers first and then even numbers in sorted order**
>>> a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
>>> # o/p should be [1, 3, 7, 9, 11, 2, 4, 6, 8, 12]
**96 Write a program to sort a list which has mix of both odd and even numbers, in the sorted list, odd numbers should be in ascending order and even numbers should be in descending order**
>>> a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
>>> # o/p should be [1, 3, 7, 9, 11, 12, 8, 6, 4, 2]
**97 Write a program to count the number of occurrences of non-special characters in a given string**
>>> s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'
**98 Grouping Flowers and Animals in the below list**
items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
**99 Grouping files with same extensions**
files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
**100 Filter only those characters except digits**
s = '@hello12world34welcome!123'
'''




'''       
s = "HHHHAAASSSSSSSSqqqqqEEEEADDADD "
O/P_= (SSSSSSSSS,8)
'''

#145 Write a program to print common character present in all the items of the below list
'''
items = [ "glory", "glass", "sight", "fight"]
l = []
for word in items:
    s = set(word)
    l.append(s)
print(l)
ch = l[0].intersection(l[1],l[2],l[3])
print(ch)
  
'''
##146 Function should accept a list and if any number divisible by 3 then modify to 33 or else keep it as it is
'''
l = [33,90,56,76,34,12,4,7,99,64]

def func_(list_):
    l1 = []
    for i in list_:
        if i % 3 == 0:
            l1.append(33)
        else:
            l1.append(i)
    return l1
print(func_(l))
'''













##1. sort a list in reverse order
'''
l = [1,6,9,4,7,8]

print(l[::-1])
for n in l[::-1]:
    print(n, end = ' ')
print()
for n in reversed(l):
    print(n)

l.sort(reverse =True)
for n in l:
    print(n)
'''
####2. sort the list based on length
'''
names = ['apple','google','yahoo','amazon','facebook','instagram','microsoft','zomato']
#sort()
names.sort(key = len)
print(names)

#sorted()
print(sorted(names,key=len))
'''

##3. sort the list based on the 1st character of each element
'''
names = ['apple','google','yahoo','amazon','facebook','instagram','microsoft','zomato']

#sort()
names.sort()
print(names)

#custom sort
print(sorted(names, key = lambda s : s[0]))
'''
## 4. sort the  list bassed on the last character of each element
'''
names = ['apple','google','yahoo','amazon','facebook','instagram','microsoft','zomato']

print(sorted(names, key = lambda s : s[-1]))
'''
## 5.sort the dict based on the key
'''
d = {'ACME' :45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20 , 'FB': 10.75}
print(sorted(d))
print(sorted(d.items(), key = lambda item : item [0]))
'''
## 6.sort the dict based on the value
'''
d = {'ACME' :45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20 , 'FB': 10.75}
print(sorted(d.items(), key = lambda item : item [-1]))
'''
## 7. sort the dict based on the length of the key
'''
d = {'ACME' :45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20 , 'FB': 10.75}
print(sorted(d.items(), key = lambda item : len(item [0])))
'''
## 8.sort the dict based on the length of the value
'''
d = {'ACME' :45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20 , 'FB': 10.75}
print(sorted(d.items(), key = lambda item : len(str(item[-1]))))
'''
##9. sort the dict based on the  last character of the key or value
'''
d = {'ACME' :45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20 , 'FB': 10.75}
print(sorted(d.items(), key = lambda item : item[0])[-1])) #### value  str(item[-1])[-1]
'''
##10. sort the dict based on the firt character of the key/ value
'''
d = {'ACME' :45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20 , 'FB': 10.75}
print(sorted(d.items(), key = lambda item : item [0][0])) #### value str(item[-1])[0]
'''
#### write a func taht accepts two strings and returns true if the two strings are anagrams of each other
'''
def anagram_(s1,s2):
    a1 = "".join(sorted(s1))
    a2 = "".join(sorted(s2))
    if a1 == a2:
        return 'strings are anagram'
    else:
        return 'strings are not anagram'
print(anagram_('maoam','maoam'))
'''

###program to largest no in the list
'''
l =[ 1,13,6,5,3,9,16]
print(max(l))

l.sort()
min_,*res, max_ = l
print(max_)

max_ = 0
for i in l:
    if max_ < i:
        max_ = i
print(max_)

for i in range(len(l)-1):
    if l[i] > l[i+1]:
        l[i],l[i+1] = l[i+1], l[i]
print(l)
print(l[-1])
'''

### program to print non repeated word in the sentence
'''
s = 'hai how are you python is a programing language and fun language'
l = s.split()
for word in l:
    if l.count(word) == 1:
        print(word)

l1 = []
for word in l:
    if word not in l1:
        l1.append(word)
print(l1)
'''
### print the all the longest and shortest word in the sentance
'''
s = 'hai how are you python is a programing language and fun language'
l= s.split()
min_,*res,max_ = sorted(l, key=len)
print(max_)

'''
### program to print all largest number in the list
'''
l = [34,67,37,67,9,67,56,35,21,54]
max_ = max(l)
for n in l:
    if n == max_:
        print(n)

print()
mx_ = 0
for i in l:
    if mx_ < i:
        mx_ = i
for n in l:
    if mx_ == n:
        print(n)
'''
### using list comprehensions
##build a list of prime numbers from 1 to 50
'''
n = 5
l2 = [n % i for i in range(2,n)]
print(all(l2))

#normal
l =[]
for i in range(2,n):
    if n%i== 0:
        l.append(False)
    else:
        l.append(True)
print(all(l))

'''
##reverse a item of the list if the item is of odd length string otherwise keep  it as it is
'''
names = ['apple','google','yahoo','gmail','flipkart','instagram','microsoft']
l = [ word[::-1] if len(word) % 2 == 1 else word for word in names]
print(l)
'''
### write a python program to create a lambda function that adds 15 to a given number passed
'''
n = 6
a = lambda n: n+15
print(a(n))
'''
### lambda function to square an cube of any number
'''
a =  lambda n : (n**2,n**3)
print(a(3))

l = [1,4,6,8,9,10]
a = lambda n: (n**2,n**3)
print(list(map(a,l)))
'''
## create lambda func that multiplies 2 arguments
'''
a =  lambda n,m : n*m
print(a(3,2))
'''
### program to solve the expression a**2+b**2+2*a*b
'''
n =  lambda a,b : a**2+b**2+2*a*b
print(n(3,2))
'''
### program to solve the expression 2* a+ 3*b+4*c
'''
n =  lambda a,b,c : 2* a+ 3*b+4*c
print(n(3,2,6))
'''

## program to find the square the item by their index using map
'''
#method 1
nums =[1,2,3,4,5]
def power_(item):
    return item[1] ** item[0]
print(list(map(power_,enumerate(nums))))

##method 2
index = range(0,len(nums))
def power_(index,item):
    return item** index
print(list(map(power_,index,nums)))

'''
### sum of positive number and sum of negative numbers present in the given list
'''
l = [2,6,-1,-5,9,-14]

def sum_(l):
    sum_pn = 0
    sum_nn = 0
    for n in l:
        if n >= 0:
            sum_pn += n
        else:
            sum_nn += n
    print(sum_pn)
    print(sum_nn)
sum_(l)

#  filter
print(sum(list(filter(lambda n : n >0,l))))
print(sum(list(filter(lambda n : n <0,l))))
'''

        

