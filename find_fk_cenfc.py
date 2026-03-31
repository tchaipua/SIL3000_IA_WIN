import pyodbc
conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=servidor\\sqlexpress;DATABASE=msinfor;UID=sa;PWD=Mabelu2011;'
try:
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            fk.name AS FK_Name,
            tp.name AS Parent_Table,
            tr.name AS Ref_Table
        FROM sys.foreign_keys fk
        INNER JOIN sys.tables tp ON fk.parent_object_id = tp.object_id
        INNER JOIN sys.tables tr ON fk.referenced_object_id = tr.object_id
        WHERE tr.name = 'CENFC' OR tp.name = 'CENFC'
    """)
    for r in cur.fetchall():
        print(f"FK: {r[0]} | Parent: {r[1]} | Ref Table: {r[2]}")
    conn.close()
except Exception as e:
    print(e)
