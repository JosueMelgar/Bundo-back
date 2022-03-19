#! C:\Python39\python.exe

import sys
import cgitb
import os
sys.path.insert(0, 'C:\Apache24\core')
from operation import selectCL
from queue import get_userid
import json
cgitb.enable()
#try:
if(True):
    print('Content-Type: text/html')
    print('')
    userid=get_userid()
    a=selectCL(f"userid={userid}",'users',['userid','name','lastname','phone','email','password','balance'])
    print('{"status":"OK"'+',"data":'+json.dumps(a[0])+'}')
#except:
#    print('{"status":"ERROR"}')
