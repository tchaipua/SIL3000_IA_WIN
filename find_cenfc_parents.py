import pyodbc
conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=servidor\\sqlexpress;DATABASE=msinfor;UID=sa;PWD=Mabelu2011;'
try:
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            fk.name AS FK_Name,
            OBJECT_NAME(fk.parent_object_id) AS ParentTable,
            OBJECT_NAME(fk.referenced_object_id) AS ReferencedTable
        FROM sys.foreign_keys fk
        WHERE OBJECT_NAME(fk.referenced_object_id) = 'CENFC'
    """)
    for r in cur.fetchall():
        print(f"FK: {r[0]} | Parent: {r[1]} | Ref: {r[2]}")
    conn.close()
except Exception as e:
    print(e)
