import pyodbc

conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=servidor\\sqlexpress;DATABASE=msinfor;UID=sa;PWD=Mabelu2011;"
try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 1 * FROM crmov2")
    cols2 = [desc[0] for desc in cursor.description]
    conn.close()

    with open("colunas_crmov2.txt", "w") as f:
        for c in cols2:
            f.write(c + "\n")
    print("Salvo em colunas_crmov2.txt")
except Exception as e:
    print("Erro:", e)
