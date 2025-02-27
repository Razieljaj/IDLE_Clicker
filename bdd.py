import sqlite3
def create_account(pseudo, password):
    conn = sqlite3.connect('accounts.db')
    cur = conn.cursor()
    verif = cur.execute("""SELECT * FROM Data WHERE pseudo LIKE ?""", (pseudo,))
    one_exist = verif.fetchall()
    print(one_exist)
    if len(one_exist) == 0:
        cur.execute("""INSERT INTO Data (pseudo, password, score) VALUES (?, ?, 0);""", (pseudo, password))
        conn.commit()
        conn.close()
        return True
    conn.close()
    return False

def login_account(pseudo, password):
    conn = sqlite3.connect('accounts.db')
    cur = conn.cursor()
    res = cur.execute("""SELECT * FROM Data WHERE pseudo LIKE ? AND password LIKE ? """, (pseudo, password))
    account = res.fetchall()
    conn.close()
    return account