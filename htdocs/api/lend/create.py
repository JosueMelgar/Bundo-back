#! C:\Python39\python.exe

import sys
import cgi,cgitb
from datetime import datetime,timedelta
from math import ceil
sys.path.insert(0, 'C:\Apache24\core')
from operation import value,insert,insertMany
from queue import get_userid,get_lastid
cgitb.enable()
print('Content-Type: text/html')
print('')
try:
#if(True):
    userid=get_userid()
    #keys=['name','phone','email','password']
    form = cgi.FieldStorage()
    it=datetime.fromtimestamp(int(form.getvalue('sdate')))
    et=datetime.fromtimestamp(int(form.getvalue('edate')))
    freq=int(form.getvalue('freq'))
    np=ceil((et-it).days/freq)
    values=[['lender',f"'{userid}'"],
            value('borrower','str'),
            value('sdate','int'),
            value('edate','int'),
            value('amount','int'),
            value('tip','int'),
            value('freq','str'),
            ['npays',str(np)],
            ['t',"strftime('%s','now')"]]
    a=insert(values,'agreements')
    print('{"status":"OK"'+',"data":'+str(list([list(b) for b in a]))+'}')
except:
    print('{"status":"ERROR"}')
