import os

filepath = r"c:\Sistemas\IA\SIL3000_IA_WIN\SIL_IA_WIN.py"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

nova_classe = """
# =====================================================================
# TELA 4: ANÁLISE DE VENDAS POR PRODUTO (CFG_PRODS)
# =====================================================================
import tkinter.ttk as ttk

class AnaliseProdutoWindow(ctk.CTkToplevel):
    def __init__(self, parent, config):
        super().__init__(parent)
        self.title("Análise de Vendas por Produto")
        self.geometry("850x650")
        self.config_db = config
        self.grab_set()  # Trava a janela pai
        
        largura = 850; altura = 650
        x = (self.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.winfo_screenheight() // 2) - (altura // 2)
        self.geometry(f"{largura}x{altura}+{x}+{y}")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # 1. Top Filters
        self.top_frame = ctk.CTkFrame(self, fg_color="#F5F5F7", height=80, corner_radius=0)
        self.top_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        self.top_frame.grid_columnconfigure(6, weight=1)

        ctk.CTkLabel(self.top_frame, text="Ano:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=(20, 5), pady=20, sticky="e")
        self.combo_ano = ctk.CTkComboBox(self.top_frame, values=["Todos"], width=100)
        self.combo_ano.grid(row=0, column=1, padx=5, pady=20, sticky="w")

        ctk.CTkLabel(self.top_frame, text="Mês:", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=(20, 5), pady=20, sticky="e")
        self.combo_mes = ctk.CTkComboBox(self.top_frame, values=["Todos"] + [f"{i:02d}" for i in range(1, 13)], width=100)
        self.combo_mes.grid(row=0, column=3, padx=5, pady=20, sticky="w")

        ctk.CTkLabel(self.top_frame, text="Exibir:", font=("Arial", 12, "bold")).grid(row=0, column=4, padx=(20, 5), pady=20, sticky="e")
        self.combo_limite = ctk.CTkComboBox(self.top_frame, values=["Top 10", "Top 20", "Top 50", "Top 100"], width=110)
        self.combo_limite.set("Top 20")
        self.combo_limite.grid(row=0, column=5, padx=5, pady=20, sticky="w")

        self.btn_filtrar = ctk.CTkButton(self.top_frame, text="🔍 Atualizar", font=("Arial", 12, "bold"), width=120, command=self.carregar_dados, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_filtrar.grid(row=0, column=6, padx=20, pady=20, sticky="w")

        # 2. Main Frame
        self.grid_frame = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        self.grid_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#FFFFFF", fieldbackground="#FFFFFF", foreground="black", rowheight=32, font=("Arial", 11))
        style.configure("Treeview.Heading", background="#1565C0", foreground="white", font=("Arial", 11, "bold"))
        style.map("Treeview", background=[('selected', '#1E88E5')], foreground=[('selected', 'white')])

        self.tree = ttk.Treeview(self.grid_frame, columns=("Rank", "Cod", "Desc", "Qtd"), show="headings", selectmode="browse")
        self.tree.pack(fill="both", expand=True, side="left")

        self.tree.heading("Rank", text="🏆 #")
        self.tree.heading("Cod", text="🔑 Código")
        self.tree.heading("Desc", text="📦 Produto")
        self.tree.heading("Qtd", text="🛒 Quantidade")

        self.tree.column("Rank", width=60, anchor="center")
        self.tree.column("Cod", width=100, anchor="center")
        self.tree.column("Desc", width=500, anchor="w")
        self.tree.column("Qtd", width=120, anchor="center")

        sb = ttk.Scrollbar(self.grid_frame, orient="vertical", command=self.tree.yview)
        sb.pack(fill="y", side="right")
        self.tree.configure(yscrollcommand=sb.set)

        # 3. Footer
        self.footer_frame = ctk.CTkFrame(self, height=50, fg_color="#F5F5F7", corner_radius=0)
        self.footer_frame.grid(row=2, column=0, sticky="ew", padx=0, pady=0)

        fechar_ico_path = os.path.join(os.path.dirname(__file__), "btn_fechar.png")
        if os.path.exists(fechar_ico_path):
            img_fechar = Image.open(fechar_ico_path).resize((18, 18))
            self.fechar_img = ctk.CTkImage(light_image=img_fechar, dark_image=img_fechar, size=(18, 18))
            self.btn_fechar = ctk.CTkButton(self.footer_frame, text="Fechar Tela", image=self.fechar_img, compound="left", font=("Arial", 12, "bold"), fg_color="transparent", text_color="black", border_width=2, border_color="black", hover_color="#E0E0E0", width=130, command=self.destroy)
        else:
            self.btn_fechar = ctk.CTkButton(self.footer_frame, text="Fechar Tela", font=("Arial", 12, "bold"), fg_color="transparent", text_color="black", border_width=2, border_color="black", hover_color="#E0E0E0", width=130, command=self.destroy)
        self.btn_fechar.pack(side="left", padx=20, pady=10)

        self.frame_id = ctk.CTkFrame(self.footer_frame, fg_color="transparent")
        self.frame_id.pack(side="right", padx=15)
        self.lbl_tela_id = ctk.CTkLabel(self.frame_id, text="Tela: CFG_PRODS", font=ctk.CTkFont(size=11, weight="bold"), text_color="gray")
        self.lbl_tela_id.pack(side="left")
        
        # Bootstrap
        self.after(200, self.carregar_anos)

    def carregar_anos(self):
        server = self.config_db.get("servidor")
        database = self.config_db.get("banco")
        username = self.config_db.get("usuario_bd")
        password = self.config_db.get("senha_bd")
        
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"
        try:
            import pyodbc, pandas as pd
            conn = pyodbc.connect(conn_str)
            df_anos = pd.read_sql("SELECT DISTINCT YEAR(CRMov2DAte) as Ano FROM crmov2 WHERE CRMov2DAte IS NOT NULL", conn)
            conn.close()
            
            anos = sorted(df_anos['Ano'].dropna().unique().tolist(), reverse=True)
            self.combo_ano.configure(values=["Todos"] + [str(int(a)) for a in anos])
            self.carregar_dados()
        except: pass

    def carregar_dados(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        server = self.config_db.get("servidor"); database = self.config_db.get("banco"); username = self.config_db.get("usuario_bd"); password = self.config_db.get("senha_bd")
        
        ano = self.combo_ano.get(); mes = self.combo_mes.get(); limite = self.combo_limite.get().replace("Top ", "")
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"
        
        try:
            import pyodbc, pandas as pd
            conn = pyodbc.connect(conn_str)
            where_clauses = ["1=1"]
            if ano != "Todos": where_clauses.append(f"YEAR(c2.CRMov2DAte) = {int(ano)}")
            if mes != "Todos": where_clauses.append(f"MONTH(c2.CRMov2DAte) = {int(mes)}")
            where_str = " AND ".join(where_clauses)

            query = f\"\"\"
                SELECT TOP {int(limite)} c4.CEProCod, p.CEProDes, SUM(c4.CRMov4Qtd) as TotalQtd
                FROM crmov4 c4
                INNER JOIN crmov2 c2 ON c4.CMEmpCod = c2.CMEmpCod AND c4.CMFilCod = c2.CMFilCod AND c4.CRMovDta = c2.CRMovDta AND c4.CRMovSeq = c2.CRMovSeq
                INNER JOIN cepro p ON c4.CEProCod = p.CEProCod
                WHERE {where_str}
                GROUP BY c4.CEProCod, p.CEProDes ORDER BY TotalQtd DESC
            \"\"\"
            df = pd.read_sql(query, conn); conn.close()

            for index, row in df.iterrows():
                self.tree.insert("", "end", values=(index + 1, row['CEProCod'], row['CEProDes'].strip(), f"{row['TotalQtd']:.1f}"))
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erro de Filtro", f"Não foi possível carregar os produtos:\\n\\n{str(e)}")
"""

search_str = "if __name__ == '__main__':"

if search_str in content:
    idx = content.find(search_str)
    content = content[:idx] + nova_classe + "\n\n" + content[idx:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Classe AnaliseProdutoWindow injetada com FIND.")
else:
    print("Falha ao achar __main__")
