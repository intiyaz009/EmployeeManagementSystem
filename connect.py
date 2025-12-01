import oracledb as orc
def connection():
    try:
        con = orc.connect("Username/Password@DSN")
        print("connected database")
        return con
    except orc.DatabaseError as db:
        print("Connection Error ",db)

connection()
