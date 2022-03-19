#! C:\Python39\python.exe

import sys
import cgitb
import os
sys.path.insert(0, 'C:\Apache24\core')
from operation import selectCL,selectC
from queue import get_userid
import json
cgitb.enable()
print('Content-Type: text/html')
print('')
try:
#if(True):
    userid=get_userid()
    a=selectC(f"lender={userid}",'agreements','agrid')
    a=selectCL(f"agrid in ({','.join([str(b[0]) for b in a])})",'transactions',['transid','agrid','pdate','n','amount','status'])
    print('{"status":"OK"'+',"data":'+json.dumps(a)+'}')
except:
    print('{"status":"ERROR"}')
