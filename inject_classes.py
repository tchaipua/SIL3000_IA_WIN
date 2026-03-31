import re

with open('restore_classes.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix ExcluirClientesInativosWindow
# Replace configurar_grid
bad_grid_excluir = '''        # --- NOVO PADRAO: Usar configurar_grid ---
        cols = ("Rank", "Cod", "Nome", "Det", "UltVenc", "VlAb", "MedMensal", "Status")
        heads = ("🏆 #", "🔑 Cód", "👤 Cliente", "📋", "📅 UltVenc", "💰 Saldo", "📈 Média", "🔘")
        wids = (50, 70, 250, 50, 110, 110, 110, 100)
        aligns = ("center", "center", "w", "center", "center", "e", "e", "center")
        self.configurar_grid(cols, heads, wids, aligns)'''

good_grid_excluir = '''        # Configurar Colunas do Grid
        self.tree.configure(columns=("Rank", "Cod", "Nome", "Det", "UltVenc", "VlAb", "MedMensal", "Status"))
        self.headers_dict = {"Rank": "🏆 #", "Cod": "🔑 Cód", "Nome": "👤 Cliente", "Det": "📋", "UltVenc": "📅 UltVenc", "VlAb": "💰 Saldo", "MedMensal": "📈 Média", "Status": "🔘"}
        for col, head in self.headers_dict.items():
            self.tree.heading(col, text=head, command=lambda _c=col: self.ordenar_por(_c, False))
        self.tree.column("Rank", width=50, anchor="center")
        self.tree.column("Cod", width=70, anchor="center")
        self.tree.column("Nome", width=250, anchor="w")
        self.tree.column("Det", width=50, anchor="center")
        self.tree.column("UltVenc", width=110, anchor="center")
        self.tree.column("VlAb", width=110, anchor="e")
        self.tree.column("MedMensal", width=110, anchor="e")
        self.tree.column("Status", width=100, anchor="center")
        
        # Manter labels de totais antigos (rodape)
        self.lbl_vlr_geral_parcelas = __import__('customtkinter').CTkLabel(self.bottom_bar, text="", font=("Arial", 13, "bold"), text_color="#1565C0")
        self.lbl_vlr_geral_parcelas.pack(side="left", padx=10)
        
        self.lbl_rodape_sistema = __import__('customtkinter').CTkLabel(self.bottom_bar, text="", font=("Arial", 13, "bold"), text_color="#1565C0")
        self.lbl_rodape_sistema.pack(side="left", padx=10)
        
        self.lbl_cli_geral = __import__('customtkinter').CTkLabel(self.bottom_bar, text="", font=("Arial", 11, "bold"), text_color="gray")
        self.lbl_cli_geral.pack(side="left", padx=5)
        self.lbl_cli_ativos = __import__('customtkinter').CTkLabel(self.bottom_bar, text="", font=("Arial", 11, "bold"), text_color="#43A047")
        self.lbl_cli_ativos.pack(side="left", padx=5)
        self.lbl_cli_inativos_db = __import__('customtkinter').CTkLabel(self.bottom_bar, text="", font=("Arial", 11, "bold"), text_color="#D32F2F")
        self.lbl_cli_inativos_db.pack(side="left", padx=5)
        '''
if bad_grid_excluir in text:
    text = text.replace(bad_grid_excluir, good_grid_excluir)
else:
    print("WARNING: bad_grid_excluir not found in restore_classes.py")

# Remove tree_totais logic
bad_totais = '''        # Atualizar Resumo de Totais (Padrao Excel)
        fmt = lambda v: f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        for item in self.tree_totais.get_children(): self.tree_totais.delete(item)
        self.tree_totais.insert("", "end", values=(f" TOTAIS ({total}):", "", "", "", "", fmt(soma_aberto), fmt(soma_med), ""))'''
if bad_totais in text:
    text = text.replace(bad_totais, "")
else:
    print("WARNING: bad_totais not found")

# 2. Fix DetalhesParcelasInativosWindow
bad_grid_det = '''        # Ocultar botões de exportação padrão se não quiser agora, ou manter
        # Usar novo padrao configurar_grid
        self.configurar_grid(
             columns=("DtaV", "VlNo", "VlAb", "DtaP"),
             headings=("Vencimento", "Valor Parcela", "Saldo Aberto", "Data Pagamento"),
             widths=(150, 180, 180, 150),
             aligns=("center", "e", "e", "center")
        )'''
good_grid_det = '''        # Configurar Colunas do Grid
        self.tree.configure(columns=("DtaV", "VlNo", "VlAb", "DtaP"))
        self.tree.heading("DtaV", text="Vencimento")
        self.tree.heading("VlNo", text="Valor Parcela")
        self.tree.heading("VlAb", text="Saldo Aberto")
        self.tree.heading("DtaP", text="Data Pagamento")
        self.tree.column("DtaV", width=150, anchor="center")
        self.tree.column("VlNo", width=180, anchor="e")
        self.tree.column("VlAb", width=180, anchor="e")
        self.tree.column("DtaP", width=150, anchor="center")
        self.lbl_detalhe_total = __import__('customtkinter').CTkLabel(self.bottom_bar, text="", font=("Arial", 14, "bold"), text_color="#1565C0")
        self.lbl_detalhe_total.pack(side="left", padx=20)'''
if bad_grid_det in text:
    text = text.replace(bad_grid_det, good_grid_det)
else:
    print("WARNING: bad_grid_det not found")

bad_tot_det = '''            # Atualizar Treeview de Totais (Sincronização Perfeita)
            for item in self.tree_totais.get_children(): self.tree_totais.delete(item)
            self.tree_totais.insert("", "end", values=(f" TOTAIS ({len(rows)}):", fmt(total_nom), fmt(total_aberto), ""))'''
good_tot_det = '''            self.lbl_detalhe_total.configure(text=f"🧾 TOTAL GERAL ({len(rows)} Parcelas): {fmt(total_nom)}  |  💰 TOTAL ABERTO: {fmt(total_aberto)}")'''
if bad_tot_det in text:
    text = text.replace(bad_tot_det, good_tot_det)
else:
    print("WARNING: bad_tot_det not found")

# Append to SIL_IA_WIN.py
with open('SIL_IA_WIN.py', 'a', encoding='utf-8') as f:
    f.write('\n\n')
    f.write(text)

# Fix MainHub methods
with open('SIL_IA_WIN.py', 'r', encoding='utf-8') as f:
    code = f.read()

main_hub_hooks = '''    def abrir_cobranca(self): self.abrir_modulo(CobrancaClienteWindow)
    def abrir_excluir_inativos(self): self.abrir_modulo(ExcluirClientesInativosWindow)

    def abrir_modulo_detalhes_inativos(self, cod, nome):
        if hasattr(self, "modulo_atual") and self.modulo_atual:
             self.modulo_atual.destroy()
        self.modules_frame.pack_forget()
        from __main__ import DetalhesParcelasInativosWindow
        self.modulo_atual = DetalhesParcelasInativosWindow(self.main_frame, self.config, cod, nome)
        self.modulo_atual.hub = self
        self.modulo_atual.pack(fill="both", expand=True)

def centralizar_tela'''
if "def centralizar_tela" in code and "def abrir_cobranca" not in code:
    code = code.replace("def centralizar_tela", main_hub_hooks)
else:
    print("main_hub_hooks already present or centralizar_tela missing")

# changing buttons
old_cobranca = 'self.btn_cobranca = ctk.CTkButton(self.col2_frame, text="📞 Cobrança por Cliente", width=btn_width, height=45, font=("Arial", 13, "bold"), command=lambda: None, fg_color="#1E88E5", hover_color="#1565C0")'
new_cobranca = 'self.btn_cobranca = ctk.CTkButton(self.col2_frame, text="📞 Cobrança por Cliente", width=btn_width, height=45, font=("Arial", 13, "bold"), command=self.abrir_cobranca, fg_color="#1E88E5", hover_color="#1565C0")'
code = code.replace(old_cobranca, new_cobranca)

add_excluir = '''        self.btn_cobranca.pack(pady=8, padx=15)

        self.btn_excluir_inativos = ctk.CTkButton(self.col2_frame, text="🗑️ Excluir Clientes Inativos", width=btn_width, height=45, font=("Arial", 13, "bold"), command=self.abrir_excluir_inativos, fg_color="#C62828", hover_color="#B12020")
        self.btn_excluir_inativos.pack(pady=8, padx=15)'''

if "🗑️ Excluir Clientes Inativos" not in code:
    code = code.replace('        self.btn_cobranca.pack(pady=8, padx=15)', add_excluir)

# Fix Clientes Deixaram de Comprar text
code = code.replace('self.btn_pararam = ctk.CTkButton(self.col1_frame, text="🛑 Clientes Inativos", width=btn_width, height=45', 'self.btn_pararam = ctk.CTkButton(self.col1_frame, text="🛑 Clientes Deixaram de Comprar", width=btn_width, height=45')

with open('SIL_IA_WIN.py', 'w', encoding='utf-8') as f:
    f.write(code)
print("Finished patching SIL_IA_WIN.py")
