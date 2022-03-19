#! C:\Python39\python.exe

import sys
import cgitb
import os
sys.path.insert(0, 'C:\Apache24\core')
from operation import select
from queue import get_userid
cgitb.enable()
print('Content-Type: text/html')
print('')
try:
    userid=get_userid()
    a=select(f"borrower={userid}",'agreements')
    print('{"status":"OK"'+',"data":'+str(list([list(b) for b in a]))+'}')
except:
    print('{"status":"ERROR"}')
