#! C:\Python39\python.exe

import sys
import cgitb
sys.path.insert(0, 'C:\Apache24\core')
from operation import value,insert
#from operator import itemgetter
cgitb.enable()
#print('Content-Type: text/html')
#print()
#keys=['name','phone','email','password']
try:
#if(True):
    values=[value('name','str'),
            value('lastname','str'),
            value('phone','int'),
            value('email','str'),
            value('password','str')]

    print('Content-Type: text/json')
    print('')
    a=insert(values,'users')
    print('{"status":"OK"}')
except:
    print('{"status":"ERROR"}')
