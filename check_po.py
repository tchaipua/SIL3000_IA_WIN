import pyodbc

conn_str = r"DRIVER={ODBC Driver 17 for SQL Server};SERVER=servidor\sqlexpress;DATABASE=msinfor;UID=sa;PWD=Mabelu2011"
conn = pyodbc.connect(conn_str)
cur = conn.cursor()

tables = ["POCF2", "POCF3", "POCF4"]

for t in tables:
    print(f"\n--- {t} ---")
    cur.execute(f"""
        SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME='{t}' 
        ORDER BY ORDINAL_POSITION
    """)
    for c in cur.fetchall():
        tp = c.DATA_TYPE
        if c.CHARACTER_MAXIMUM_LENGTH:
            tp += f"({c.CHARACTER_MAXIMUM_LENGTH})"
        print(f"  {c.COLUMN_NAME:<30} {tp}")

conn.close()
