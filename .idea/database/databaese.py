import sqlite3
def check_database():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print(cursor.fetchall())
    connection.close()

def get_connection():

    connection = sqlite3.connect(r"C:\Users\\drago\\IdeaProjects\\untitled\\.idea\\database\\journal.db")
    return connection
if __name__== '__main__':
    check_database()