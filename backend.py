import sqlite3


def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY ,date TEXT,earnings INTEGER,exercise TEXT,study TEXT,diet TEXT,python TEXT)")
    conn.commit()
    conn.close()


def insert(date, earnings, exercise, study, diet, python):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO TABLE routine VALUES(NULL,?,?,?,?,?,?)", (date, earnings, exercise, study, diet, python))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(Id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=?", (Id,))
    conn.commit()
    conn.close()


def Search(date='', earnings='', exercise='', study='', diet='', python=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=? OR earnings=? OR exercise=? OR study=? OR diet=? OR python=?",
                (date, earnings, exercise, study, diet, python))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

