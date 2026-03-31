import pyodbc

conn_str = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=servidor\sqlexpress;DATABASE=msinfor;UID=sa;PWD=Mabelu2011'
try:
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()
    
    # Analisar a Constraint "CENFC3"
    query = """
    SELECT 
        OBJECT_NAME(f.parent_object_id) AS ParentTable, 
        COL_NAME(fc.parent_object_id, fc.parent_column_id) AS ParentColumn, 
        OBJECT_NAME(f.referenced_object_id) AS ReferencedTable, 
        COL_NAME(f.referenced_object_id, fc.referenced_column_id) AS ReferencedColumn 
    FROM sys.foreign_keys AS f 
    INNER JOIN sys.foreign_key_columns AS fc ON f.object_id = fc.constraint_object_id 
    WHERE f.name = 'CENFC3'
    """
    cur.execute(query)
    rows = cur.fetchall()
    print("\n--- FK: CENFC3 ---")
    for r in rows:
        print(f"Parent: {r[0]}.{r[1]} -> Refered: {r[2]}.{r[3]}")
    
    conn.close()
except Exception as e:
    print(f"Erro: {e}")
