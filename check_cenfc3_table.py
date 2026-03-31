import pyodbc
conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=servidor\\sqlexpress;DATABASE=msinfor;UID=sa;PWD=Mabelu2011;'
try:
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sys.tables WHERE name LIKE '%CENFC3%' OR name LIKE 'CENFC%'")
    print([r[0] for r in cur.fetchall()])
    conn.close()
except Exception as e:
    print(e)
