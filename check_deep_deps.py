import pyodbc

conn_str = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=servidor\sqlexpress;DATABASE=msinfor;UID=sa;PWD=Mabelu2011'
try:
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()
    
    # Lista de tabelas que eu já excluo
    tabelas_pai = [
        'CENFC', 'CRNF1', 'CRNF2', 'CRDA1', 'CRDM1', 'CRANT', 'CRTipH', 'CRMov2'
    ]
    
    print("\n--- Verificando Filhos das Tabelas Principais ---")
    for pai in tabelas_pai:
        query = f"""
        SELECT 
            DISTINCT OBJECT_NAME(parent_object_id) AS ChildTable
        FROM sys.foreign_keys
        WHERE OBJECT_NAME(referenced_object_id) = '{pai}'
        """
        cur.execute(query)
        filhos = [r[0] for r in cur.fetchall()]
        if filhos:
            print(f"Pai: {pai} | Filhos: {filhos}")
    
    conn.close()
except Exception as e:
    print(f"Erro: {e}")
