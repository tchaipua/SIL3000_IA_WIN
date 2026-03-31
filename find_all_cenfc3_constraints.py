import pyodbc
conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=servidor\\sqlexpress;DATABASE=msinfor;UID=sa;PWD=Mabelu2011;'
try:
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            fk.name AS FK_Name,
            OBJECT_NAME(fk.parent_object_id) AS ChildTable,
            OBJECT_NAME(fk.referenced_object_id) AS ParentTable
        FROM sys.foreign_keys AS fk
        WHERE fk.name LIKE '%CENFC3%' OR fk.name = 'CENFC3'
    """)
    for r in cur.fetchall():
        print(f"FK: {r[0]} | Child: {r[1]} | Parent: {r[2]}")
    conn.close()
except Exception as e:
    print(e)
