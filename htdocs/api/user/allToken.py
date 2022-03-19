#! C:\Python39\python.exe

import sys
import cgitb
import os
sys.path.insert(0, 'C:\Apache24\core')
from operation import selectAll
cgitb.enable()

try:
#if(True):
    print('Content-Type: text/html')
    print('')
    a=selectAll('sessions')
    print('{"status":"OK"'+',"data":'+str(list([list(b) for b in a]))+'}')
except:
    print('{"status":"ERROR"}')
