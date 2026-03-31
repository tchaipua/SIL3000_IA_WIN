import pyodbc
conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=servidor\\sqlexpress;DATABASE=msinfor;UID=sa;PWD=Mabelu2011;'
try:
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()
    for t in ['CENFD', 'CENFP', 'CENFO1', 'CENFR', 'CENFV', 'CENFM', 'CENFK']:
        try:
            cur.execute(f"SELECT TOP 0 * FROM {t}")
            cols = [desc[0] for desc in cur.description]
            print(f"Table {t}: {cols}")
        except:
            print(f"Table {t} not found")
    conn.close()
except Exception as e:
    print(e)
