# coding:utf-8
'''
Created on 2017年5月5日

@author: lvyanghui
'''

# name = 'What is your name ?'
# if name.endswith('?'):
#     print 'Hello world'
#     print '123'
#     
# d = (1,2,3)
# print d


'''
print 'Age:', 42

print 1,2,3

name = 'Gumby'
salutation = 'Mr,'
greeting = 'Hello,'

print greeting, salutation, name

print greeting+',', salutation, name

print 'Hello',
print 'World!'
'''

'''
import math as foobar
print foobar.sqrt(4)
from math import sqrt as foobar1
print foobar1(4)

x, y, z = 1, 2, 3
print x, y, z

x, y = y, x
print x, y, z

values = 1, 2, 3
print values

x, y, z = values
print x

scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = scoundrel.popitem()
print key 
print value
'''

'''
x = 2
x += 1
x *= 2
print x

fnord = 'foo'
fnord += 'bar'
fnord *= 2
print fnord
'''

'''
print True
print False
print True == 1
print False == 0
print True + False + 42

print bool('I think, therefore I am')
print bool(42)
print bool('')
print bool(0)
'''

# name = raw_input('What is your name? ')
# if(name.endswith('Gumby')):
#     print 'Hello Gumby'
# else:
#     print 'Hello stranger'
    
# number = input('Enter a number: ')
# if number > 0:
#     print 'The number is positive'
# elif number < 0:
#     print 'The number is negative'
# else:
#     print 'The number is zero'
'''
name = raw_input('What is your name?')
if(name.endswith('Gumby')):
    if name.startswith('Mr.'):
        print 'Hello Mr Gumby'
    elif name.startswith('Mrs.'):
        print 'Hello Mrs Gumby'
    else:
        print 'Hello Gumby'
else:
    print 'Hello stranger'
    
print 'Mrs Gumby'.startswith('Mrs')
'''

'''
print 'foo' == 'foo'
print 'foo' == 'bar'

x = y = [1, 2, 3]
z = [1, 2, 3]
print x == y
print x == z
print x is y
print x is z
'''

'''
print 's' in 'kkone'

print 'alpha' < 'beta'

number = input('Enter a nubmer between 1 and 10: ')
if number > 0 and number < 10:
    print 'Great!'
else:
    print 'Wrong!'
    '''
    
# age = 10
# assert 0 < age < 100

# age = -1
# assert 0 < age < 100

# x = 1
# while x < 100:
#     print x
#     x += 1
    
# name = ''
# while not (name or name.isspace()):
#     name = raw_input('Please enter your name: ')
# print 'Hello. %s!' % name

# words = ['this', 'is', 'an', 'ex', 'parrot']
# for word in words:
#     print word

'''
print range(0, 10)

print range(20)

for number in range(1, 101):
    print number
'''
    
# d = {'x': 1, 'y': 2, 'z': 3}
# for key in d:
#     print key, 'corresponds to', d[key]
#     
# for key, value in d.items():
#     print key, 'corresponds to', value

'''
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]

for i in range(len(names)):
    print names[i], 'is', ages[i], 'years old'
    
print zip(names, ages)

for name, age in zip(names, ages):
    print name, 'is', age, 'years old'
    
print zip(range(5), xrange(100))
'''
   
#strings  = ['xxa', 'bba', 'abbxx', 'bxxcc', 'kkone']
# for string in strings:
#     if 'xx' in string:
#         index = strings.index(string)
#         strings[index] = '[censored]'
'''
index = 0
for string in strings:
    if 'xx' in string:
        index = strings.index(string)
    strings[index] = '[censored]'    
# index += 1        
print strings

for index, string in enumerate(strings):
    if '[censored]' in string:
        strings[index] = 'kk'
        
print strings
'''

'''
print sorted([4, 3, 6, 8, 3])

print sorted('Hello, world')

print list(reversed('Hello, world'))

print ''.join(reversed('Hello, world'))


from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
    
print range(0, 10, 2)
'''
# word = 'dummy'
# while word:
#     word = raw_input('Please enter a word: ')
#     print 'The word was' + word

# word = raw_input('Please enter a word: ')
# while word:
#     print 'The word is ' + word
#     word = raw_input('Please enter a word: ')

# while True:
#     word = raw_input('Please enter a word: ')
#     if not word: 
#         break
#     print 'The word is ' + word

'''
from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
else:
    print "Didn't find it!"  

print [x*x for x in range(10)]  
print [x*x for x in range(10) if x % 3 == 0]

print [(x,y) for x in range(3) for y in range(4)]

result = []
for x in range(3):
    for y in range(4):
        result.append((x, y))
print result

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
# print [b + '+' + g for b in boys for g in girls if b[0] == g[0]]

letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print [b + '+' + g for b in boys for g in letterGirls[b[0]]]
print letterGirls
    '''
    
# pass
# 
# x = 1
# print x
# del x
# print x

# x = ['Hello', 'world']
# y = x
# y[1] = 'Python'
# print x
# del x 
# print y

# exec "print 'Hello, world!'"
# 
# from math import sqrt
# exec "sqrt = 1"
# 1(4)
# sqrt(4)

from math import sqrt
scope = {}
exec 'sqrt = 1' in scope
print sqrt(4)
print scope['sqrt']

print len(scope)
print scope.keys()

eval(raw_input("Enter an arithmetic expression: "))