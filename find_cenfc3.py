import pyodbc
conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=servidor\\sqlexpress;DATABASE=msinfor;UID=sa;PWD=Mabelu2011;'
try:
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            OBJECT_NAME(parent_object_id) AS ParentTable,
            OBJECT_NAME(referenced_object_id) AS ReferencedTable
        FROM sys.foreign_keys 
        WHERE name = 'CENFC3'
    """)
    res = cur.fetchone()
    print("CENFC3 Constraint Info:", res)
    conn.close()
except Exception as e:
    print(e)
