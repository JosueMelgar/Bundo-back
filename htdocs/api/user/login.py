#! C:\Python39\python.exe

import sys
import cgitb
sys.path.insert(0, 'C:\Apache24\core')
from operation import value,equalSelect,insert,upsert
from misc import gen_token
#from operator import itemgetter
cgitb.enable()
#print('Content-Type: text/html')
#print('')
try:
    values=[value('email','str'),
            value('password','str')]
    r=equalSelect(values,'users')
    if(r[0]):
        token=gen_token()
        nr=upsert([['userid',str(r[0][0])],
                ['token',"'"+token+"'"]
            ],'sessions','userid')
        if(nr):
            print('Content-Type: text/html')
            print(f"Set-Cookie: token={token}; Path=/")
            print()
            print('{"status":"OK"}')
    else:
        print('Content-Type: text/json')
        print()
        print('{"status":"OK"}')
except:
    print('Content-Type: text/json')
    print()
    print('{"status":"ERROR"}')
