import os

filepath = r"c:\Sistemas\IA\SIL3000_IA_WIN\SIL_IA_WIN.py"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Injeta chamada after no __init__ do MainHub e o método testar_conexao_banco
old_init_end = """        self.atualizar_rodape()

    def copiar_id(self, texto):"""

new_init_end = """        self.atualizar_rodape()
        self.after(200, self.testar_conexao_banco)

    def testar_conexao_banco(self):
        import pyodbc
        from tkinter import messagebox
        
        server = self.config.get("servidor")
        database = self.config.get("banco")
        username = self.config.get("usuario_bd")
        password = self.config.get("senha_bd")
        
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"
        
        try:
            conn = pyodbc.connect(conn_str)
            conn.close()
        except:
            try:
                # Fallback de Driver legado
                conn_str_alt = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"
                conn = pyodbc.connect(conn_str_alt)
                conn.close()
            except Exception as e:
                # Alerta Amigável
                messagebox.showerror("Erro de Conexão", "Não foi possível conectar ao Banco de Dados com as credenciais fornecidas.\\n\\nPor favor, verifique os dados de acesso (Servidor, Banco, Usuário ou Senha) nas Configurações.")
                # Abre ConfigWindow (CFG_ACESSO) de forma automática
                self.abrir_configuracoes()

    def copiar_id(self, texto):"""

if old_init_end in content:
    content = content.replace(old_init_end, new_init_end)
else:
    print("Bloco de texto não encontrado. Tentando variação...")
    # Tenta sem o espaçamento excessivo se houver
    if "self.atualizar_rodape()" in content and "def copiar_id(self, texto):" in content:
         content = content.replace("    def copiar_id(self, texto):", """    def testar_conexao_banco(self):
        import pyodbc
        from tkinter import messagebox
        
        server = self.config.get("servidor")
        database = self.config.get("banco")
        username = self.config.get("usuario_bd")
        password = self.config.get("senha_bd")
        
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"
        
        try:
            conn = pyodbc.connect(conn_str)
            conn.close()
        except:
            try:
                conn_str_alt = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"
                conn = pyodbc.connect(conn_str_alt)
                conn.close()
            except Exception as e:
                messagebox.showerror("Erro de Conexão", "Não foi possível conectar ao Banco de Dados com as credenciais fornecidas.\\n\\nPor favor, verifique os dados de acesso (Servidor, Banco, Usuário ou Senha) nas Configurações.")
                self.abrir_configuracoes()

    def copiar_id(self, texto):""")
         content = content.replace("self.atualizar_rodape()", "self.atualizar_rodape()\n        self.after(200, self.testar_conexao_banco)")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Teste de arranque principal configurado.")
