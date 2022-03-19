#! C:\Python39\python.exe

import sys
import cgitb
import os
sys.path.insert(0, 'C:\Apache24\core')
from operation import select,selectC
from queue import get_userid
cgitb.enable()
print('Content-Type: text/html')
print('')
try:
#if(True):
    userid=get_userid()
    a=selectC(f"lender={userid}",'agreements','agrid')
    a=select(f"agrid in ({','.join([str(b[0]) for b in a])})",'transactions')
    print('{"status":"OK"'+',"data":'+str([list(b) for b in a])+'}')
except:
    print('{"status":"ERROR"}')
