#! C:\Python39\python.exe

import sys
import cgitb
import os
sys.path.insert(0, 'C:\Apache24\core')
from operation import selectAll
cgitb.enable()
print('Content-Type: text/html')
print('')
try:
    a=selectAll('agreements')
    print('{"status":"OK"'+',"data":'+str(list([list(b) for b in a]))+'}')
except:
    print('{"status":"ERROR"}')
