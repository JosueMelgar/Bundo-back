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
try:
    userid=get_userid()
    form = cgi.FieldStorage()
    values=[['lender',str(userid)],
            value('transid','str')]
    transid=form.getvalue('transid')
    agrs=selectC(f"lender={userid}",'agreements','agrid')
    a=update(' AND '.join(equal(values)),'agreements','status=1')
    if(a):
        d=selectC(f"lender={userid}",'agreements','sdate,edate,amount,freq,tip')
        (it,et,amount,freq,tip)=d[0]
        it=datetime.fromtimestamp(it)
        et=datetime.fromtimestamp(et)
        np=ceil((et-it).days/freq)
        v=[]
        id=get_lastid()[0]
        for i in range(1,np+1):
            c=timedelta(days=freq*i)
            v.append([str(agrid),str((it+c).timestamp()),str(i),str(amount+tip/np)])
            #a=insert([['agrid',str(agrid)],['pdate',str((it+c).timestamp())],['n',str(i)],['amount',str(amount+tip/np)]],'transactions')
        a=insertMany('agrid,pdate,n,amount','transactions',v)
        print('{"status":"OK"'+',"data":'+str(list([list(b) for b in a]))+'}')
except:
    print('{"status":"ERROR"}')
