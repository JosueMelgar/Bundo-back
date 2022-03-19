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
    userid=get_userid()
    #print('Content-Type: application/json')
    print('Content-Type: text/html')
    print('')
    a=selectCL(f"lender={userid}",'agreements',['agrid','lender','borrower','amount','tip','sdate','edate','freq','autopay','cash','npays','t','status'])
    print('{"status":"OK"'+',"data":'+json.dumps(a)+'}')
#except:
#    print('{"status":"ERROR"}')
