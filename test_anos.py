import pyodbc, pandas as pd
try:
    conn_str = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=servidor\\sqlexpress;DATABASE=msinfor;UID=sa;PWD=Mabelu2011"
    conn = pyodbc.connect(conn_str)
    df = pd.read_sql("SELECT DISTINCT YEAR(CRMovDta) as Ano FROM crmov2 WHERE CRMovDta IS NOT NULL AND YEAR(CRMovDta) != 9999", conn)
    conn.close()
    print("DataFrame:", df)
    anos = sorted(df['Ano'].dropna().unique().astype(int).tolist(), reverse=True)
    print("Anos processados:", anos)
except Exception as e:
    print("Erro capturado:", str(e))
