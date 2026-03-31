import pyodbc

# Configurações
conn_str = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=servidor\sqlexpress;DATABASE=msinfor;UID=sa;PWD=Mabelu2011'

try:
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()
    
    # 1. Encontrar todas as Tabelas que possuem colunas como "CliCod", "CodC", etc.
    # 2. Encontrar tabelas filhas diretas de crmov2
    
    print("\n--- Tabelas que parecem referenciar Clientes (CRCliCod ou CodC) ---")
    query = """
    SELECT TABLE_NAME, COLUMN_NAME 
    FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE (COLUMN_NAME LIKE '%CliCod%' OR COLUMN_NAME LIKE '%CodC%')
      AND TABLE_NAME NOT LIKE 'sys%'
    ORDER BY TABLE_NAME
    """
    cur.execute(query)
    for r in cur.fetchall():
        print(f"Tabela: {r[0].ljust(15)} | Coluna: {r[1]}")
        
    print("\n--- Hierarquia Filha de CRMov2 (Tabelas que possuem CMEmpCod, CMFilCod, CRMovDta, CRMovSeq) ---")
    # CRMov2 primary key is CMEmpCod, CMFilCod, CRMovDta, CRMovSeq
    query_child = """
    SELECT DISTINCT TABLE_NAME 
    FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE COLUMN_NAME IN ('CMEmpCod', 'CMFilCod', 'CRMovDta', 'CRMovSeq')
      AND TABLE_NAME <> 'crmov2'
      AND TABLE_NAME NOT LIKE 'sys%'
    GROUP BY TABLE_NAME
    HAVING COUNT(DISTINCT COLUMN_NAME) = 4
    """
    cur.execute(query_child)
    for r in cur.fetchall():
        print(f"Filha de CRMov2: {r[0]}")
        
    conn.close()
except Exception as e:
    print(f"Erro: {e}")
