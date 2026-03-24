import os

classes_str = """

# =====================================================================
# NOVAS TELAS: RESUMO, INATIVOS, CONTAS RECEBER
# =====================================================================

class BaseWindow(ctk.CTkToplevel):
    def __init__(self, parent, title_str, id_str):
        super().__init__(parent)
        self.title(title_str)
        self.geometry("900x650")
        self.grab_set()
        centralizar_tela(self, 900, 650)
        self.grid_rowconfigure(1, weight=1); self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="#FFFFFF")

        # Top Bar
        self.top_frame = ctk.CTkFrame(self, fg_color="#F5F5F7", height=80, corner_radius=0)
        self.top_frame.grid(row=0, column=0, sticky="ew")

        # Grid frame
        self.grid_frame = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        self.grid_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        style = ttk.Style()
        style.configure(id_str + ".Treeview", background="#FFFFFF", fieldbackground="#FFFFFF", foreground="black", rowheight=32, font=("Arial", 11))
        style.configure(id_str + ".Treeview.Heading", background="#1565C0", foreground="white", font=("Arial", 11, "bold"))

        self.tree = ttk.Treeview(self.grid_frame, show="headings", selectmode="browse")
        self.tree.pack(fill="both", expand=True, side="left")
        self.tree.tag_configure('even', background='#FFFFFF')
        self.tree.tag_configure('odd', background='#E2E8F0')

        # Rodape
        self.bottom_bar = ctk.CTkFrame(self, fg_color="#F5F5F7", height=40, corner_radius=0)
        self.bottom_bar.grid(row=2, column=0, sticky="ew")
        
        btn_sair = ctk.CTkButton(self.bottom_bar, text="Fechar", command=self.destroy, fg_color="#C62828", hover_color="#B12020", width=100)
        btn_sair.pack(side="left", padx=20, pady=5)

        self.lbl_id = ctk.CTkLabel(self.bottom_bar, text=f"Tela: {id_str}", font=("Arial", 11, "bold"), text_color="gray")
        self.lbl_id.pack(side="right", padx=20)

class ResumoClienteWindow(BaseWindow):
    def __init__(self, parent, config):
        super().__init__(parent, "Resumo por Cliente", "RESUMO_CLI")
        ctk.CTkLabel(self.top_frame, text="👤 Resumo por Cliente", font=("Arial", 16, "bold")).pack(pady=25)
        self.tree.configure(columns=("Rank", "Cod", "Nome", "Vendas", "Faturamento"))
        self.tree.heading("Rank", text="#"); self.tree.heading("Cod", text="Cod"); self.tree.heading("Nome", text="Cliente"); self.tree.heading("Vendas", text="Vendas"); self.tree.heading("Faturamento", text="Fat. Total")
        self.tree.column("Rank", width=50); self.tree.column("Cod", width=80); self.tree.column("Nome", width=350)

class ClientesPararamWindow(BaseWindow):
    def __init__(self, parent, config):
        super().__init__(parent, "Clientes que Pararam de Comprar", "CLI_INATIVOS")
        ctk.CTkLabel(self.top_frame, text="🛑 Clientes Inativos", font=("Arial", 16, "bold")).pack(pady=25)
        self.tree.configure(columns=("Cod", "Nome", "Dias", "Ultima_Compra", "Valor"))
        self.tree.heading("Cod", text="Cod"); self.tree.heading("Nome", text="Cliente"); self.tree.heading("Dias", text="Dias s/ Comprar"); self.tree.heading("Ultima_Compra", text="Últ. Compra"); self.tree.heading("Valor", text="Últ. Valor")
        self.tree.column("Cod", width=80); self.tree.column("Nome", width=350)

class PosicaoContasReceberWindow(BaseWindow):
    def __init__(self, parent, config):
        super().__init__(parent, "Posição Contas a Receber", "CR_POSICAO")
        ctk.CTkLabel(self.top_frame, text="💰 Contas a Receber", font=("Arial", 16, "bold")).pack(pady=25)
        self.tree.configure(columns=("Vencimento", "Cliente", "Documento", "Valor", "Status"))
        self.tree.heading("Vencimento", text="Vencimento"); self.tree.heading("Cliente", text="Cliente"); self.tree.heading("Documento", text="Nº Doc"); self.tree.heading("Valor", text="Valor"); self.tree.heading("Status", text="Status")
        self.tree.column("Vencimento", width=120); self.tree.column("Cliente", width=300)

"""

filepath = r"c:\Sistemas\IA\SIL3000_IA_WIN\SIL_IA_WIN.py"
with open(filepath, 'a', encoding='utf-8') as f:
    f.write(classes_str)

print("Injeção de Classes Concluída")
