from mysql.connector import MySQLConnection, Error
 
def connect():
    """ Connect MySql """
    db_config = {
        'host': 'localhost',
        'database': 'DatingApp',
        'user': 'root',
        'password': 'pass123'
    }
 
    conn = None
 
    try:
        conn = MySQLConnection(**db_config)
 
        if conn.is_connected():
            return conn
 
    except Error as error:
        print(error)
 
    return conn

def show_account():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User_account")
        rows = cursor.fetchall()
 
        print('Total Row(s):', cursor.rowcount)
        return(rows)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_info():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User_Information")
        rows = cursor.fetchall()
 
        print('Total Row(s):', cursor.rowcount)
        return(rows)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_basics():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User_basics")
        rows = cursor.fetchall()
 
        print('Total Row(s):', cursor.rowcount)
        return(rows)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()
        
def show_interests():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User_interests")
        rows = cursor.fetchall()
 
        print('Total Row(s):', cursor.rowcount)
        return(rows)
 
    except Error as e:
        print(e)
 
    finally:
        # close connection
        cursor.close()
        conn.close()