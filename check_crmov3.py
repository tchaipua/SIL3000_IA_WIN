import pyodbc
import json

# Try to find config from the script context if possible or assume default
conn_str = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=VIP-SERVER;DATABASE=msinfor;UID=sa;PWD=vipsolutions"

try:
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()
    cur.execute("SELECT TOP 1 * FROM crmov3")
    cols = [column[0] for column in cur.description]
    print(f"COLUMNS: {cols}")
    conn.close()
except Exception as e:
    print(f"ERROR: {e}")
