import pyodbc

conn_str = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=servidor\sqlexpress;DATABASE=msinfor;UID=sa;PWD=Mabelu2011'
try:
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()
    
    # 1. Analisar a Constraint "CRMOV52"
    query = """
    SELECT 
        OBJECT_NAME(f.parent_object_id) AS ParentTable, 
        COL_NAME(fc.parent_object_id, fc.parent_column_id) AS ParentColumn, 
        OBJECT_NAME(f.referenced_object_id) AS ReferencedTable, 
        COL_NAME(f.referenced_object_id, fc.referenced_column_id) AS ReferencedColumn 
    FROM sys.foreign_keys AS f 
    INNER JOIN sys.foreign_key_columns AS fc ON f.object_id = fc.constraint_object_id 
    WHERE f.name = 'CRMOV52'
    """
    cur.execute(query)
    rows = cur.fetchall()
    print("\n--- FK: CRMOV52 ---")
    for r in rows:
        print(f"Parent: {r[0]}.{r[1]} -> Refered: {r[2]}.{r[3]}")
        
    print("\n--- Tabelas Filhas Reais de CRMov2 (por FK) ---")
    query_real_child = """
    SELECT 
        OBJECT_NAME(f.parent_object_id) AS TableName
    FROM sys.foreign_keys AS f
    WHERE OBJECT_NAME(f.referenced_object_id) = 'crmov2'
    GROUP BY OBJECT_NAME(f.parent_object_id)
    """
    cur.execute(query_real_child)
    for r in cur.fetchall():
        print(f"Filha: {r[0]}")
        
    # 3. Conferir colunas de CRMov5 para deleção por código cliente
    cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'CRMov5'")
    print(f"\n--- Colunas de CRMov5: {[r[0] for r in cur.fetchall()]} ---")
    
    conn.close()
except Exception as e:
    print(f"Erro: {e}")
