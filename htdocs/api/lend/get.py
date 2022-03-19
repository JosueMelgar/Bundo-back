#! C:\Python39\python.exe

import sys
import cgitb
import os
sys.path.insert(0, 'C:\Apache24\core')
from operation import selectCL,selectC
from queue import get_userid
import json
cgitb.enable()
try:
#if(True):
    userid=get_userid()
    #print('Content-Type: application/json')
    print('Content-Type: text/html')
    print('')
    a=selectCL(f"lender={userid}",'agreements',['agrid','lender','borrower','amount','tip','sdate','edate','freq','autopay','cash','npays','t','status'])
    l=set([b['lender'] for b in a]+[b['borrower'] for b in a])
    r=selectC(f"userid in ({','.join([str(b) for b in l])})",'users','userid,name,lastname')
    name={}
    name.update(list(zip([r2[0] for r2 in r],[r2[1] for r2 in r])))
    lastname={}
    lastname.update(list(zip([r2[0] for r2 in r],[r2[2] for r2 in r])))
    for b in a:
        b.update([
            ['lender_name',name[b['lender']]],
            ['lender_lastname',lastname[b['lender']]],
            ['borrower_name',name[b['borrower']]],
            ['borrower_lastname',lastname[b['borrower']]]
            ])
    print('{"status":"OK"'+',"data":'+json.dumps(a)+'}')
except:
    print('{"status":"ERROR"}')
