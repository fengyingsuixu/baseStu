#coding:utf-8
'''
Created on 2017年5月4日

@author: lvyanghui
'''

'''
phonebook = {'Alice':'2341', 'Beth':'9102', 'Cecil':'3528'}
print phonebook['Beth']


items = [('name','Gumby'),('age',42)]
d = dict(items)
print d
print d['name']

dd = dict(name='Gumby', age=42)
print dd['age']
print len(d)
print 'age' in dd
del d['age']
print d
'''

# x = []
# x[42] = 'Foobar'
# print x

'''
x = {}
x[42] = 'Foobar'
print x

people = {
    'Alice':{
        'phone': '2341',
        'addr': 'Foo drive 23'        
    },
    'Beth':{
        'phone': '9102',
        'addr': 'Bar street 42'        
    },
    'Alice':{
        'phone': '3158',
        'addr': 'Baz avenue 90'        
    }       
}

labels = {'phone':'phone nmuber','addr':'address'}

name = raw_input('name: ')
request = raw_input('Phone number (p) or address (a)?')
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

if name in people:
    print "%s's %s is %s." %\
    (name,labels[key],people[name][key])
'''

'''
phonebook = {'Alice':'2341', 'Beth':'9102', 'Cecil':'3528'}
print "Cecil's phone number is %(Cecil)s." % phonebook

template = '<html>\
<head><title>%(title)s</title></head>\
<body>\
<h1>%(title)s</h1>\
<p>%(text)s</p>\
</body>'
data = {'title': 'My Home Page', 'text': 'Welcome to my home'}
print template % data
'''
    
# d = {}
# d['name'] = 'Gumby'
# d['age'] = 42
# print d
# return_value = d.clear()
# print d
# print return_value

'''
x = {}
y = x
x['key'] = 'value'
print y
# x = {}
x.clear()
print y
'''

'''
x = {'username': 'admin', 'machines': ['bar','foo','baz']}
y = x.copy()
print y
y['machines'].remove('baz')
print y
print x
'''

'''
from copy import deepcopy
d = {}
d['names']=['Alfred','Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print c
print dc


# print {}.fromkeys(['name', 'age'])
# 
# print dict.fromkeys(['name', 'age'])
# print dict.fromkeys(['name', 'age'], ['Gumby', 42])

d = {}
d['name'] = 'Alice'
# print d['name']
print d.get('name')
print d.get('name', 'Gumby')
# d['name'] = 'Alice'
print d.get('name')

people = {
    'Alice':{
        'phone': '2341',
        'addr': 'Foo drive 23'        
    },
    'Beth':{
        'phone': '9102',
        'addr': 'Bar street 42'        
    },
    'Alice':{
        'phone': '3158',
        'addr': 'Baz avenue 90'        
    }       
}

labels = {'phone':'phone nmuber','addr':'address'}

name = raw_input('name: ')
request = raw_input('Phone number (p) or address (a)?')
key = request
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

person = people.get(name,{})
label = labels.get(key,key)
result = person.get(key, 'not available')

print "%s's %s is %s." % (name, label, result) 
'''

# d = {}
# print d.has_key('name')
# d['name'] = 'Alice'
# print d.has_key('name')

# d = {'title': 'Python Web Site', 'url': 'http://www.Python.org', 'spam': 0}
# print d.items()
# it = d.iteritems()
# print it
# print list(it)
#  
# print d.keys()
# print d.iterkeys()

# print d.popitem()
# print d

# d = {'x': 1, 'y': 2}
# print d.pop('x')
# print d

# d = {}
# print d.setdefault('name')
# print d


d = {'title': 'Python Web Site', 'url': 'http://www.Python.org', 'changed': 'Mar 14 22:09:15 MET 2009'}
x = {'title': 'Python Language Website'}
d.update(x)
print d

print d.values()
print d.itervalues()
