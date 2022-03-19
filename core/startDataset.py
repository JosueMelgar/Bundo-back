import sqlite3  
db = sqlite3.connect("db")
db.execute('CREATE TABLE users(userid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL, lastname TEXT NOT NULL, phone INT NOT NULL UNIQUE, email TEXT NOT NULL UNIQUE, password TEXT NOT NULL, balance REAL NOT NULL DEFAULT 0)')
db.execute('CREATE TABLE agreements(agrid INTEGER PRIMARY KEY AUTOINCREMENT,lender INT NOT NULL,borrower INT NOT NULL, amount REAL NOT NULL, tip REAL NOT NULL, sdate INT NOT NULL, edate INT NOT NULL, freq INT NOT NULL,autopay INT NOT NULL DEFAULT 0, cash INT NOT NULL DEFAULT 0,npays INT NOT NULL,t INT NOT NULL,status INT NOT NULL DEFAULT 0)')
db.execute('CREATE TABLE transactions(transid INTEGER PRIMARY KEY AUTOINCREMENT,agrid INT NOT NULL, pdate INT NOT NULL, n INT NOT NULL, amount REAL NOT NULL, status INT NOT NULL DEFAULT 0)')
db.execute('CREATE TABLE sessions(userid INTEGER PRIMARY KEY,token TEXT)')
db.commit()
'''
db.execute('
    CREATE TABLE users(
        userid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        lastname TEXT NOT NULL,
        phone INT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        balance REAL NOT NULL DEFAULT 0)')
db.execute('
    CREATE TABLE agreements
        agrid INTEGER PRIMARY KEY AUTOINCREMENT,
        lender INT NOT NULL,
        borrower INT NOT NULL,
        amount REAL NOT NULL,
        tip REAL NOT NULL,
        sdate INT NOT NULL,
        edate INT NOT NULL,
        freq INT NOT NULL,
        autopay INT NOT NULL DEFAULT 0,
        cash INT NOT NULL DEFAULT 0,
        npays INT NOT NULL,
        t INT NOT NULL,
        status INT NOT NULL DEFAULT 0)')
db.execute('
    CREATE TABLE transactions(
        transid INTEGER PRIMARY KEY AUTOINCREMENT,
        agrid INT NOT NULL,
        pdate INT NOT NULL,
        n INT NOT NULL,
        amount REAL NOT NULL,
        status INT NOT NULL DEFAULT 0)')
db.execute('
    CREATE TABLE sessions(
        userid INTEGER PRIMARY KEY,
        token TEXT)')
'''
