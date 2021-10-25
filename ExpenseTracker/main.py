import sqlite3 as db
from datetime import datetime

def init():
    #init a new database to store expense
    connection = db.connect("ExpenseTracker\Maindb.db")
    cur = connection.cursor()
    sql = '''
    create table if not exists expenses (
        amount number,
        category string,
        message string,
        date string
        )
    '''
    cur.execute(sql)
    connection.commit()

def log(amount, category, message=""):
    date = str(datetime.now())
    connection = db.connect("ExpenseTracker\Maindb.db")
    cur = connection.cursor()
    sql = '''
    insert into expenses values (
         {},
        '{}',
        '{}',
        '{}'
        )
    '''.format(amount, category, message, date)
    cur.execute(sql)
    connection.commit()

def view(category=None):
    connection = db.connect("ExpenseTracker\Maindb.db")
    cur = connection.cursor()
    if category:
        sql = '''
        select * from expenses where category = '{}'
        '''.format(category)
        sqlTotal = '''
        select sum(amount) from expenses where category = '{}'
        '''.format(category)
    else:
        sql = '''
        select * from expenses
        '''.format(category)
        sqlTotal = '''
        select sum(amount) from expenses
        '''.format(category)
    cur.execute(sql)
    results = cur.fetchall()
    cur.execute(sqlTotal)
    total_Amount = cur.fetchone()[0]

    return total_Amount, results