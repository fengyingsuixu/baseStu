#coding:utf-8
'''
Created on 2017年5月12日

@author: lvyanghui
'''

# fibs = [0,1]
# for i in range(8):
#     fibs.append(fibs[-2]+fibs[-1])
#     
# print fibs

'''
import math
x = 1
y = math.sqrt
print callable(x)
print callable(y)


def hello(name):
    print 'Hello,' + name
    
hello('world')

def fibs(num):
    result = [0,1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result

print fibs(10)

'''


'''
def square(x):
    '求数的平方'
    return x * x
print square.__doc__


# help(square)
'''

'''
def hello1(greeting, name):
    print '%s, %s!' % (greeting, name)

def hello2(name, greeting):
    print '%s, %s!' % (name, greeting)

hello1('hello', 'world')
hello2('hello', 'world')

hello1(greeting='hello', name='world')
hello2(greeting='hello', name='world')


def hello3(greeting='hello', name='world'):
    print '%s, %s!' % (greeting, name)

hello3()
hello3('greeting')
hello3('greeting', 'universe')
hello3(name='gumby')

def hello4(name, greeting='hello', punctuation='!'):
    print '%s, %s%s' % (greeting, name, punctuation)

hello4('mars')
hello4('mars', 'howdy')
hello4('mars', 'howdy', '...')
hello4()
'''


def print_params(*params):
    print params

print_params('testing')

print_params(1,2,3)

def print_params2(title, *params):
    print title
    print params

print_params2('Params is:', 1,2,3)
print_params2('Nothing:')
#print_params('Hmm...', something=42)

def print_params3(**params):
    print params

print_params3(x = 1, y = 2, z = 3)


def print_params4(x, y , z = 3, *pospar, **keypar):
    print x, y, z
    print pospar
    print keypar


print_params4(1,2,3, 5, 6, 7, foo = 1, bar = 2)