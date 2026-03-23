import os

filepath = r"c:\Sistemas\IA\SIL3000_IA_WIN\SIL_IA_WIN.py"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Altera Combo de Mês para Extenso no __init__
old_mes = """        ctk.CTkLabel(self.top_frame, text="Mês:", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=(20, 5), pady=20, sticky="e")
        self.combo_mes = ctk.CTkComboBox(self.top_frame, values=["Todos"] + [f"{i:02d}" for i in range(1, 13)], width=100)
        self.combo_mes.grid(row=0, column=3, padx=5, pady=20, sticky="w")"""

new_mes = """        ctk.CTkLabel(self.top_frame, text="Mês:", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=(20, 5), pady=20, sticky="e")
        self.meses_ext = ["Todos", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        self.combo_mes = ctk.CTkComboBox(self.top_frame, values=self.meses_ext, width=120)
        self.combo_mes.set("Todos")
        self.combo_mes.grid(row=0, column=3, padx=5, pady=20, sticky="w")"""

if old_mes in content:
    content = content.replace(old_mes, new_mes)

# 2. Adiciona Botão de Cópia e ToolTip decente no __init__ (fim da classe)
old_id = """        self.frame_id = ctk.CTkFrame(self.footer_frame, fg_color="transparent")
        self.frame_id.pack(side="right", padx=15)
        self.lbl_tela_id = ctk.CTkLabel(self.frame_id, text="Tela: CFG_PRODS", font=ctk.CTkFont(size=11, weight="bold"), text_color="gray")
        self.lbl_tela_id.pack(side="left")"""

new_id = """        self.frame_id = ctk.CTkFrame(self.footer_frame, fg_color="transparent")
        self.frame_id.pack(side="right", padx=15)
        self.lbl_tela_id = ctk.CTkLabel(self.frame_id, text="Tela: CFG_PRODS", font=ctk.CTkFont(size=11, weight="bold"), text_color="gray")
        self.lbl_tela_id.pack(side="left")
        from tkinter import messagebox
        self.btn_copy_id = ctk.CTkButton(self.frame_id, text="📋", width=20, height=20, fg_color="transparent", hover_color="#E0E0E0", text_color="black", command=lambda: [self.clipboard_clear(), self.clipboard_append("CFG_PRODS"), messagebox.showinfo("Sucesso", "NOME DA TELA COPIADO")])
        self.btn_copy_id.pack(side="left", padx=5)
        ToolTip(self.btn_copy_id, "COPIAR NOME TELA")"""

if old_id in content:
    content = content.replace(old_id, new_id)

# 3. Altera carregar_anos para puxar de crmov4 campo CRMovDta
old_anos = """            df_anos = pd.read_sql("SELECT DISTINCT YEAR(CRMov2DAte) as Ano FROM crmov2 WHERE CRMov2DAte IS NOT NULL", conn)"""
new_anos = """            df_anos = pd.read_sql("SELECT DISTINCT YEAR(CRMovDta) as Ano FROM crmov4 WHERE CRMovDta IS NOT NULL", conn)"""

if old_anos in content:
    content = content.replace(old_anos, new_anos)

# 4. Altera carregar_dados para converter o Mês em index e validar c4.CRMovDta
old_where = """            where_clauses = ["1=1"]
            if ano != "Todos": where_clauses.append(f"YEAR(c2.CRMov2DAte) = {int(ano)}")
            if mes != "Todos": where_clauses.append(f"MONTH(c2.CRMov2DAte) = {int(mes)}")
            where_str = " AND ".join(where_clauses)"""

new_where = """            where_clauses = ["1=1"]
            if ano != "Todos": where_clauses.append(f"YEAR(c4.CRMovDta) = {int(ano)}")
            if mes != "Todos": 
                try: mes_idx = self.meses_ext.index(mes); where_clauses.append(f"MONTH(c4.CRMovDta) = {mes_idx}")
                except: pass
            where_str = " AND ".join(where_clauses)"""

if old_where in content:
    content = content.replace(old_where, new_where)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Melhorias na visualização e busca de produtos injetadas com sucesso!")
