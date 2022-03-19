#! C:\Python39\python.exe

import sys
import cgitb
import os
sys.path.insert(0, 'C:\Apache24\core')
from operation import select
from queue import get_userid
cgitb.enable()
try:
    userid=get_userid()
    print('Content-Type: text/html')
    print('')
    a=select(f"lender={userid} AND status=0",'agreements')
    print('{"status":"OK"'+',"data":'+str(list([list(b) for b in a]))+'}')
except:
    print('{"status":"ERROR"}')
