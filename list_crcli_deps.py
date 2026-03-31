import pyodbc

conn_str = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=servidor\sqlexpress;DATABASE=msinfor;UID=sa;PWD=Mabelu2011'
try:
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()
    
    print("\n--- Tabelas que referenciam crcli via Foreign Key ---")
    query = """
    SELECT 
        OBJECT_NAME(parent_object_id) AS TableName,
        COL_NAME(parent_object_id, parent_column_id) AS ColumnName
    FROM sys.foreign_key_columns
    WHERE OBJECT_NAME(referenced_object_id) = 'crcli'
    """
    cur.execute(query)
    for r in cur.fetchall():
        print(f"Tabela: {r[0]} | Coluna: {r[1]}")
    
    conn.close()
except Exception as e:
    print(f"Erro: {e}")
