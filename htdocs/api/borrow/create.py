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
    userid=get_userid()
    #keys=['name','phone','email','password']
    form = cgi.FieldStorage()
    it=datetime.fromtimestamp(int(form.getvalue('sdate')))
    et=datetime.fromtimestamp(int(form.getvalue('edate')))
    freq=int(form.getvalue('freq'))
    np=ceil((et-it).days/freq)
    values=[['borrower',f"'{userid}'"],
            value('lender','str'),
            value('sdate','int'),
            value('edate','int'),
            value('amount','int'),
            value('tip','int'),
            value('freq','str'),
            ['npays',str(np)],
            ['t',"strftime('%s','now')"]]
    a=insert(values,'arrangement')
    if(a):
        v=[]
        id=get_lastid()[0]
        for i in range(1,np+1):
            c=timedelta(days=freq*i)
            v.append((str(id),str((it+c).timestamp()),str(i),str(int(form.getvalue('freq'))/np)))
        a=insertMany('arrid,pdate,n,amount','transactions',v)
        print('{"status":"OK"'+',"data":'+str(list([list(b) for b in a]))+'}')
except:
    print('{"status":"ERROR"}')
