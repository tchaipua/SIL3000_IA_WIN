import pyodbc

# Configuração Padrão Detectada
conn_str = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=msinfor;Trusted_Connection=yes;"

try:
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()

    print("--- INICIANDO CONVERSÃO POEmp PARA UPPERCASE ---")
    
    # Buscar colunas do tipo string
    cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'POEmp' AND DATA_TYPE IN ('char', 'varchar', 'nvarchar', 'nchar')")
    cols = [row[0] for row in cur.fetchall()]
    
    if not cols:
        print("Nenhuma coluna de texto encontrada para atualizar.")
    else:
        # Criar cláusula de UPDATE
        set_clause = ", ".join([f"{c} = UPPER({c})" for c in cols])
        sql = f"UPDATE POEmp SET {set_clause}"
        
        print(f"Executando: {sql}")
        cur.execute(sql)
        row_count = cur.rowcount
        conn.commit()
        
        print(f"SUCESSO: {row_count} registros da POEmp foram convertidos para UPPERCASE.")

    conn.close()
except Exception as e:
    print(f"ERRO AO PROCESSAR: {e}")
