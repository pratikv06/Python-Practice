'''
Program to Store Data in JSON file
'''
import sqlite3

def db_connect():
    ''' Connecting to DB '''
    conn = sqlite3.connect('database.db')
    conn.isolation_level = None
    try:
        c = conn.cursor()
        sql = "CREATE TABLE user (userid INTEGER PRIMARY KEY AUTOINCREMENT, website TEXT NOT NULL, username TEXT NOT NULL, pwd TEXT NOT NULL)"
        c.execute(sql)
    except:
        pass
    return conn

def db_close(conn):
    ''' Closing the connection '''
    conn.close()

def data_display():
    ''' Reading Data from DB '''
    conn = db_connect()
    c = conn.cursor()
    sql = 'SELECT * FROM user'
    result = c.execute(sql)
    result2 = result.fetchall()
    result_count = len(result2)
    if result_count > 0:
        print("ID  |  Website  | UserName  |  Password")
        for row in result2:
            print(str(row[0]) +"  |  "+ row[1] +"  |  "+ row[2] +"  |  "+ row[3])
    else:
        print("Table is Empty...")
    db_close(conn)

def data_add():
    ''' Adding data to DB '''
    website = input("Enter Website: ")
    userid = input("Enter Username: ")
    password = input("Enter Password: ")
    conn = db_connect()
    c = conn.cursor()
    sql = "INSERT INTO user (website, username, pwd) VALUES (?, ?, ?)"
    c.execute(sql, (website, userid, password,))
    print("*** Successfully Added! ***")
    db_close(conn)

def data_delete():
    to_remove = int(input("Id to Delete: "))
    conn = db_connect()
    c = conn.cursor()
    sql = 'DELETE FROM user WHERE userid = ?'
    c.execute(sql, (to_remove,))
    print("*** Successfully Deleted! ***")
    db_close(conn)

def main():
    while True:
        choice = input("*"*30 +"\n1. Open\n2. Add\n3. Delete\n4. Exit\n>> ")
        if choice == '1':
            data_display()
        elif choice == '2':
            data_add()
        elif choice == '3':
            data_delete()
        elif choice == '4':
            break
        else:
            print('Value Not Found!!!')


if __name__ == "__main__":
    main()    