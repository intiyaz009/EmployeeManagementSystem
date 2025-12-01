import oracledb as orc
def connection():
    try:
        con = orc.connect("System/Dhone_518@localhost/orcl")
        print("connected database")
        return con
    except orc.DatabaseError as db:
        print("Connection Error ",db)
connection()