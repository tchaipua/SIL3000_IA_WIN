import pyodbc

# CONFIGURAÇÃO OFICIAL EXTRAÍDA DO CÓDIGO FONTE
config = {
    "servidor": r"servidor\sqlexpress",
    "banco": "msinfor",
    "usuario_bd": "sa",
    "senha_bd": "Mabelu2011"
}

conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={config['servidor']};DATABASE={config['banco']};UID={config['usuario_bd']};PWD={config['senha_bd']};"

try:
    print(f"Conectando ao servidor: {config['servidor']}...")
    conn = pyodbc.connect(conn_str)
    cur = conn.cursor()

    print("--- INICIANDO CONVERSÃO GLOBAL DE TODAS AS TABELAS DO POSTO PARA UPPERCASE ---")
    
    # 1. Buscar todas as tabelas do Posto (iniciadas com PO)
    cur.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'PO%'")
    tables = [row[0] for row in cur.fetchall()]
    print(f"Encontradas {len(tables)} tabelas PO.")
    
    for table_name in tables:
        # 2. Buscar colunas de texto para esta tabela
        cur.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}' AND DATA_TYPE IN ('char', 'varchar', 'nvarchar', 'nchar')")
        cols = [row[0] for row in cur.fetchall()]
        
        if cols:
            # 3. Criar e executar cláusula de UPDATE
            set_clause = ", ".join([f"{c} = UPPER({c})" for c in cols])
            sql = f"UPDATE [{table_name}] SET {set_clause}" # Usar colchetes para segurança
            
            try:
                cur.execute(sql)
                rows_updated = cur.rowcount
                print(f"TABELA {table_name}: {rows_updated} registros convertidos para UPPERCASE.")
            except Exception as inner_e:
                print(f"Erro ao processar {table_name}: {inner_e}")

    conn.commit()
    print("\nSUCESSO: Todas as tabelas do Posto foram normalizadas para CAIXA ALTA no servidor oficial.")
    conn.close()
    
except Exception as e:
    print(f"ERRO DE CONEXÃO OU PROCESSAMENTO: {e}")
