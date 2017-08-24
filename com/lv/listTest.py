#coding:utf-8
'''
edward = ['Edward Gumy', 42]
john = ['John Smith', 36]
database = [edward,john]
print database
'''
#ͨ通用索引
from _ast import Num

'''
greeting = 'Hello'
print greeting[0]
print greeting[-1]

months = ['January','February','March','April','May','June',
          'July','August','September','October','November','December']
endings = ['st','nd','rd'] + 17 * ['th'] \
        + ['st','nd','rd'] + 7 * ['th'] \
        + ['st']

year = raw_input('Year: ')
month = raw_input('Month(1-12): ')
day = raw_input('Day(1-31): ')

month_number = int(month)
day_number = int(day)

month_name = months[month_number-1]
ordinal = day + endings[day_number-1]

print month_name + ' ' + ordinal + ', ' + year
'''

'''
tag = '<a href="http://www.python.org">Python web site</a>'
print tag[9:30]
print tag[32:-4]
print tag[-3:]
print tag[:3]
print tag[:]
print tag[0:10:3]
print tag[10:0:-3]
'''
'''
print [1,2,3] + [4,5,6]
print 'Hello. ' + 'world!'
# print 'Hello. ' + [4,5,6]

print 'python' * 5
print [42] * 10
sequence = [None] * 10
print sequence
'''
'''
sentence = raw_input("Sentence: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 4
left_margin = (screen_width - box_width) // 2

print
print ' ' * left_margin + '+' + '-' * (box_width - 2) + '+'
print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
print ' ' * left_margin + '| ' + sentence + ' |'
print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
print ' ' * left_margin + '+' + '-' * (box_width - 2) + '+'
'''

'''
permissions = 'rw'
print 'w' in permissions
print 'x' in permissions

users = ['mlh','foo','bar']
print raw_input('Enter your user name: ') in users

subject = '$$$ Get rich now!!! $$$'
print '$$$' in subject
'''

'''
database = [
    ['albert',  '1234'],
    ['dilbert', '4242'],
    ['smith',   '7542'],
    ['jones',   '9843']
]

username = raw_input('User name: ')
pin = raw_input('PIN code: ')

if [username, pin] in database:
    print 'Access granted'
'''

'''
numbers = [100,34,678]
print len(numbers)
print max(numbers)
print min(numbers)
'''
    
    
# print list('Hello')
'''
x = [1,1,1]
x[1] = 3
print x

names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[3]
print names
'''


'''
name = list('Perl')
print name

name[2:] = list('ar')
print name

name[1:] = list('ython')
print name
'''

'''
numbers = [1,5]
numbers[1:1] = [2,3,4]
print numbers

# numbers[1:4] = []
# print numbers

numbers[-3:-1]=[]
print numbers
'''
'''
lst = [1,2,3]
lst.append(4)
print lst

print ['to','be','or','not','to','be'].count('to')
x = [[1,2],1,1,[2,1,[1,2]]]
print x.count(1)
print x.count([1,2])
'''

'''
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print a

a = [1,2,3]
b = [4,5,6]
print a + b
print a


knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'hi']
print knights.index('who')
print knights.index('herring')
'''


'''
numbers = [1,2,3,5,6,7]
numbers.insert(3,'four')
print numbers


x = [1,2,3]
print x.pop()
print x
print x.pop(0)
print x


x = ['to','be','or','not','to','be']
x.remove('be')
print x

x.remove('bee')



x = [1,2,3]
# x.reverse()
# print x
print list(reversed(x))


x = [4,6,2,1,8,7,9]
# x.sort()
# print x
# y = x.sort()
# print y
# y = x[:]
# y = x
# y.sort()
# print x
# print y

y = sorted(x)
print x
print y


print cmp(42,32)
print cmp(42,58)

numbers = [5,2,9,7]
numbers.sort(cmp)
print numbers

x = ['aardvark','abalone','acme','add','aerate']
x.sort(key=len)
print x

y = [4,6,3,5,9,7,8]
# y.sort(reverse=True)
list(sorted(y))
y.reverse()
print y
'''
# x = 1,2,3
# print x

# x = (1,2,3,4)
# x[2]=7
# print x
print 3 * (40+2)
print 3 * (40+2,)

print tuple([1,2,3])
print tuple('abc')
print tuple((1,2,3))
