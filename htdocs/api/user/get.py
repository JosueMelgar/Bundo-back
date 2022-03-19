#! C:\Python39\python.exe

import sys
import cgitb
import os
sys.path.insert(0, 'C:\Apache24\core')
from operation import select
from queue import get_userid
cgitb.enable()
try:
    print('Content-Type: text/html')
    print('')
    userid=get_userid()
    a=select(f"userid={userid}",'users')
    print('{"status":"OK"'+',"data":'+str(list([list(b) for b in a]))+'}')
except:
    print('{"status":"ERROR"}')
