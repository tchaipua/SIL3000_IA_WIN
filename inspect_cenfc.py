import pyodbc
conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=servidor\\sqlexpress;DATABASE=msinfor;UID=sa;PWD=Mabelu2011;'
try:
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sys.tables WHERE name LIKE 'CENFC%'")
    res = [r[0] for r in cur.fetchall()]
    print("TABLES:", res)
    for t in res:
        try:
            print(f"\nSCHEMA {t}:")
            cur.execute(f"SELECT TOP 1 * FROM {t}")
            cols = [desc[0] for desc in cur.description]
            print(cols)
        except:
            print(f"Erro ao ler {t}")
    conn.close()
except Exception as e:
    print(e)
