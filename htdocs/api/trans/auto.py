#! C:\Python39\python.exe

import sys
import cgi,cgitb
from datetime import datetime,timedelta
from math import ceil
sys.path.insert(0, 'C:\Apache24\core')
from operation import value,insertMany,selectC,update,equal,insert
from queue import get_userid,get_lastid
cgitb.enable()
print('Content-Type: text/html')
print('')
#try:
if(True):
    userid=get_userid()
    form = cgi.FieldStorage()
    values=[value('transid','int')]
    transid=form.getvalue('transid')
    agrs=selectC(f"lender={userid}",'agreements','agrid')
    a=update(f"agrid in ({','.join([str(b[0]) for b in agrs])}) AND {' AND '.join(equal(values))}",'transactions','status=status+1')
    if(a):
        print('{"status":"OK"'+',"data":[]')
    else:
        agrs=selectC(f"borrower={userid}",'transactions','agrid')
        a=update(f"agrid in ({','.join([str(b[0]) for b in agrs])}) AND {' AND '.join(equal(values))}",'transactions','status=status+2')
        if(a):
            print('{"status":"OK"'+',"data":[]')
#except:
#    print('{"status":"ERROR"}')
