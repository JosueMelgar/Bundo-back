import sqlite3
import cgi

def value(field, type):
    form = cgi.FieldStorage()
    if type=='str':
        return [field,"'"+str(form.getvalue(field))+"'"]
    if type=='int':
        return [field,str(form.getvalue(field))]
    if type=='date':
        return [field,str(form.getvalue(field))]
def equal(values):
    s=[]
    for a in values:
        s.append('='.join(a))
    return s
def insert(values,table):
    db = sqlite3.connect("C:/Apache24/core/db")
    q=f"INSERT INTO {table}({','.join([a[0] for a in values])}) VALUES({','.join([a[1] for a in values])})"
    a=db.execute(q).fetchall()
    db.commit()
    db.close()
    return a
def insertMany(columns,table,values):
    db = sqlite3.connect("C:/Apache24/core/db")
    q=f"INSERT INTO {table}({columns}) VALUES({','.join(['?']*len(values[0]))})"
    a=db.executemany(q,values).fetchall()
    db.commit()
    db.close()
    return a
def selectAll(table):
    #db = sqlite3.connect("C:/Apache24/core/db")
    #q=f"SELECT * FROM {table}"
    #a=db.execute(q)
    #return a
    return select('1>0',table)
def select(conditions,table):
    db = sqlite3.connect("C:/Apache24/core/db")
    q=f"SELECT * FROM {table} WHERE {conditions}"
    a=db.execute(q).fetchall()
    db.close()
    return a
def selectC(conditions,table,columns):
    db = sqlite3.connect("C:/Apache24/core/db")
    q=f"SELECT {columns} FROM {table} WHERE {conditions}"
    a=db.execute(q).fetchall()
    r=[]
    for b in a:
        d={}
        d.update(zip(columns,b))
        r.append(d)
    db.close()
    return a
def selectCL(conditions,table,columns):
    db = sqlite3.connect("C:/Apache24/core/db")
    q=f"SELECT {str(columns)[1:-1]} FROM {table} WHERE {conditions}"
    print(q)
    a=db.execute(q).fetchall()
    r=[]
    for b in a:
        d={}
        d.update(zip(columns,b))
        r.append(d)
    db.close()
    return a
def selectOLW(order,limit,conditions,table):
    db = sqlite3.connect("C:/Apache24/core/db")
    q=f"SELECT * FROM {table} WHERE {conditions} ORDER BY {order} LIMIT {limit}"
    a=db.execute(q).fetchall()
    db.close()
    return a
def equalSelect(values,table):
    #db = sqlite3.connect("C:/Apache24/core/db")
    #q=f"SELECT * FROM {table} WHERE {}"
    #a=db.execute(q)
    #return a
    a=select(' AND '.join(equal(values)),table)
    return a
def upsert(values,table,conflict):
    db = sqlite3.connect("C:/Apache24/core/db")
    q=f"INSERT INTO {table} ({','.join([a[0] for a in values])}) VALUES({','.join([a[1] for a in values])}) ON CONFLICT({conflict}) DO UPDATE SET {','.join(equal(values))};"
    a=db.execute(q)
    db.commit()
    db.close()
    return a
def update(conditions,table,setting):
    db = sqlite3.connect("C:/Apache24/core/db")
    q=f"UPDATE {table} SET {setting} WHERE {conditions}"
    a=db.execute(q)
    db.commit()
    db.close()
    return a
