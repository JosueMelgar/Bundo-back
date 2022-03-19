#! C:\Python39\python.exe

import sys
import cgitb
import os
sys.path.insert(0, 'C:\Apache24\core')
from operation import selectCL
from queue import get_userid
import json
cgitb.enable()
try:
    userid=get_userid()
    print('Content-Type: text/html')
    print('')
    a=selectCL(f"lender={userid} AND status=1",'agreements',['agrid','lender','borrower','amount','tip','sdate','edate','freq','autopay','cash','npays','t','status'])
    print('{"status":"OK"'+',"data":'+json.dumps(a)+'}')
except:
    print('{"status":"ERROR"}')
