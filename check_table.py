import pyodbc

# Configurações de conexão padrão do sistema
server = r"servidor\sqlexpress"
database = "msinfor"
username = "sa"
password = "Mabelu2011"

conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # Busca todas as colunas da tabela crmov2
    query = """
    SELECT COLUMN_NAME, DATA_TYPE 
    FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE TABLE_NAME = 'crmov2'
    ORDER BY ORDINAL_POSITION;
    """
    
    cursor.execute(query)
    columns = cursor.fetchall()
    
    print("Colunas da tabela crmov2:")
    print("-" * 40)
    for col in columns:
        col_name = col[0]
        data_type = col[1]
        
        # Destacar colunas que parecem ser de data/hora
        is_time = False
        if any(keyword in col_name.lower() for keyword in ['hora', 'time', 'data', 'date', 'lanc', 'inc']):
            is_time = True
        if data_type.lower() in ['datetime', 'date', 'time', 'datetime2', 'smalldatetime']:
            is_time = True
            
        marker = " ⏰ (Possível horário)" if is_time else ""
        print(f"{col_name.ljust(20)} | {data_type.ljust(15)}{marker}")
        
    conn.close()
except pyodbc.Error as e:
    print(f"Erro ao conectar ou consultar o banco de dados:\n{e}")
except Exception as e:
    print(f"Ocorreu um erro:\n{e}")
