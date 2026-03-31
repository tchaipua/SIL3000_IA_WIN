import pyodbc

conn_str = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=servidor\sqlexpress;DATABASE=msinfor;UID=sa;PWD=Mabelu2011'
try:
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()
    
    print("\n--- Tabelas que referenciam CENFC via FK ---")
    query = """
    SELECT 
        OBJECT_NAME(f.parent_object_id) AS ParentTable, 
        COL_NAME(fc.parent_object_id, fc.parent_column_id) AS ParentColumn,
        f.name AS FK_Name
    FROM sys.foreign_keys AS f 
    INNER JOIN sys.foreign_key_columns AS fc ON f.object_id = fc.constraint_object_id 
    WHERE OBJECT_NAME(f.referenced_object_id) = 'CENFC'
    """
    cur.execute(query)
    for r in cur.fetchall():
        print(f"Parent: {r[0]} | Coluna: {r[1]} | FK: {r[2]}")
    
    conn.close()
except Exception as e:
    print(f"Erro: {e}")
