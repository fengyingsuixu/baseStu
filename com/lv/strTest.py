#coding:utf-8
'''
Created on 2017年5月3日

@author: lvyanghui
'''
from string import maketrans

'''
format = "Hello,%s,%s enough for ya?"
values = ('world','hot')
print format % values

from math import pi

print '%10.2f' % pi


from string import Template

# s = Template('$x is glorious $x')
# s = Template("It's ${x}static")
# s = Template("Make $$ is selling $x")
# print s.substitute(x='slum')
# print s
s = Template("A $thing must never $action")
d = {}
d['thing'] = "gentelman"
d['action'] = "socks" 
print s.substitute(d)  
'''

'''
print 'Price of eggs: $%d' % 42
print 'Hexadecimal price of eggs: %x' % 42
from math import pi
print 'Pi: %f...' % pi
print 'Very inexact estimate of pi: %i' % pi
print 'Using str: %s' % 42L
print 'Using repr: %r' % 42L

print '%10f' % pi
print '%10.2f' % pi
print '%.2f' % pi
print '%.5s' % 'Guido van Rossum'
print '%.*s' % (5,'Guido van Rossum')

print '%010.2f' % pi
print 010

print '%-10.2f' % pi
print ('% 5d' % 10) + '\n' + ('% 5d' % -10)
print ('%+5d' % 10) + '\n' + ('%+5d' % -10)
'''

'''
width = input('Please enter width: ')

price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'
format = '%-*s%*.2f'


print '=' * width

print header_format % (item_width, 'item', price_width, 'Price')
print '-' * width
print format % (item_width, 'Apples', price_width, 0.4)
print format % (item_width, 'Pears', price_width, 0.5)
print format % (item_width, 'Cantaloupes', price_width, 1.92)
print format % (item_width, 'Dried Apricots', price_width, 8)
print format % (item_width, 'Prunes (4 lbs.)', price_width, 12)


title = "Monty Python's Flying Circus"
print title.find("Monty")
print title.find("Python")
print title.find("Zirquss")

subject = '$$$ Get rich now!!! $$$'
print subject.find('$$$')
print subject.find('$$$',1)
print subject.find('!!!')
print subject.find('!!!',0,16)



# seq = [1,2,3,4,5]
seq = ['1','2','3','4','5']
sep = '+'
print sep.join(seq)

dirs = ['','usr','bin','env']
print '/'.join(dirs)
print 'c:' + '\\'.join(dirs)



print 'Trondheim Hammer Dance'.lower()
print "thit's all folks".title()
import string
print string.capwords("thit's all folks")
'''

print 'This is a test is '.replace('is', 'eez')

print '1+2+3+4+5'.split('+')


print '    internal whitespace is kept  '.strip()

print ' *** spam * for * everyone !!! ****'.strip(' *!')


from string import maketrans
table = maketrans('cs', 'kz')
print len(table)
print(table[97:123])
print maketrans('', '')[97:123]

print 'this is an incredible test'.translate(table)
print 'this is an incredible test'.translate(table, ' ')