import os

filepath = r"c:\Sistemas\IA\SIL3000_IA_WIN\SIL_IA_WIN.py"

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_class = """
class AnaliseVendasWindow(ctk.CTkToplevel):
    def __init__(self, parent, config):
        super().__init__(parent)
        self.title("Análise de Vendas")
        self.config = config
        
        # Centraliza
        w, h = 900, 600
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")
        
        self.transient(parent)
        
        # 1. Barra de Identificação de Tela
        self.bottom_bar = ctk.CTkFrame(self, fg_color="transparent")
        self.bottom_bar.pack(side="bottom", fill="x", padx=20, pady=(0, 10))
        
        self.frame_id = ctk.CTkFrame(self.bottom_bar, fg_color="transparent")
        self.frame_id.pack(side="right")
        self.lbl_tela_id = ctk.CTkLabel(self.frame_id, text="Tela: ANALISE_VENDAS", font=ctk.CTkFont(size=11, weight="bold"), text_color="gray")
        self.lbl_tela_id.pack(side="left")
        self.btn_copy_id = ctk.CTkButton(self.frame_id, text="📋", width=20, height=20, fg_color="transparent", hover_color="#E0E0E0", text_color="black", command=lambda: self.copiar_id("ANALISE_VENDAS"))
        self.btn_copy_id.pack(side="left", padx=5)
        ToolTip(self.btn_copy_id, "COPIAR NOME TELA")

        # 2. Barra de Botões (Rodapé)
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(side="bottom", fill="x", padx=30, pady=(15, 5))
        
        self.btn_sair = ctk.CTkButton(self.buttons_frame, text="❌ Retornar", width=140, height=32, fg_color="#C62828", text_color="white", hover_color="#B12020", command=self.destroy)
        self.btn_sair.pack(side="left")

        # Exportações
        self.btn_export_pdf = ctk.CTkButton(self.buttons_frame, text="📄 Exportar PDF", width=140, height=32, fg_color="#E53935", hover_color="#B71C1C", command=self.exportar_pdf)
        self.btn_export_pdf.pack(side="right", padx=5)
        
        self.btn_export_excel = ctk.CTkButton(self.buttons_frame, text="📊 Exportar Excel", width=140, height=32, fg_color="#43A047", hover_color="#2E7D32", command=self.exportar_excel)
        self.btn_export_excel.pack(side="right", padx=5)

        # 3. Topo: Controles
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(side="top", fill="x", padx=20, pady=20)
        
        ctk.CTkLabel(self.top_frame, text="Totalizar por:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=10)
        
        self.combo_agrupamento = ctk.CTkComboBox(self.top_frame, values=["Ano", "Mês", "Dia", "Faixa de Horário"])
        self.combo_agrupamento.pack(side="left", padx=10, pady=10)
        self.combo_agrupamento.set("Mês")
        
        ctk.CTkLabel(self.top_frame, text="Métrica:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=10)
        
        self.combo_metrica = ctk.CTkComboBox(self.top_frame, values=["Quantidade de Vendas", "Valor Total (R$)"])
        self.combo_metrica.pack(side="left", padx=10, pady=10)
        self.combo_metrica.set("Valor Total (R$)")

        self.btn_gerar = ctk.CTkButton(self.top_frame, text="Gerar Gráfico", command=self.gerar_grafico, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_gerar.pack(side="left", padx=20, pady=10)

        # 4. Centro: Gráfico
        self.chart_frame = ctk.CTkFrame(self, fg_color="white")
        self.chart_frame.pack(side="top", fill="both", expand=True, padx=20, pady=(0, 10))
        
        self.fig = Figure(figsize=(8, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.chart_frame)
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        
        self.df_raw = None
        self.df_grouped = None
        self.after(100, self.carregar_dados)

    def copiar_id(self, texto):
        self.clipboard_clear()
        self.clipboard_append(texto)
        self.update()
        messagebox.showinfo("Sucesso", "NOME DA TELA COPIADO")

    def carregar_dados(self):
        try:
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config['servidor']};DATABASE={self.config['banco']};UID={self.config['usuario_bd']};PWD={self.config['senha_bd']}"
            conn = pyodbc.connect(conn_str)
            query = "SELECT CRMovDta, CRMov2CHor, CRMov2VlrO FROM crmov2 WHERE CRMovDta IS NOT NULL"
            self.df_raw = pd.read_sql(query, conn)
            conn.close()
            
            # Limpeza de dados básica
            self.df_raw['CRMovDta'] = pd.to_datetime(self.df_raw['CRMovDta'], errors='coerce')
            self.df_raw['CRMov2VlrO'] = pd.to_numeric(self.df_raw['CRMov2VlrO'], errors='coerce').fillna(0)
            
            # Extrair atributos
            self.df_raw['Ano'] = self.df_raw['CRMovDta'].dt.year.astype('Int64')
            self.df_raw['Mes'] = self.df_raw['CRMovDta'].dt.to_period('M')
            self.df_raw['Dia'] = self.df_raw['CRMovDta'].dt.date
            
            # Hora (Tratando strings variadas)
            def extrair_hora(h):
                try: 
                    return int(str(h).replace(':', '')[:2])
                except: 
                    return None
            
            self.df_raw['Hora'] = self.df_raw['CRMov2CHor'].apply(extrair_hora)
            self.gerar_grafico()
            
        except Exception as e:
            messagebox.showerror("Erro ao carregar dados", str(e))

    def gerar_grafico(self):
        if self.df_raw is None or self.df_raw.empty:
            return
            
        agrupamento = self.combo_agrupamento.get()
        metrica = self.combo_metrica.get()
        
        # Agrupamento base
        if agrupamento == "Ano":
            grouper = 'Ano'
        elif agrupamento == "Mês":
            grouper = 'Mes'
        elif agrupamento == "Dia":
            grouper = 'Dia'
        else: # Faixa de horário
            grouper = 'Hora'
            
        # Calcula dados
        if grouper not in self.df_raw.columns: return
        df_valid = self.df_raw.dropna(subset=[grouper])
        
        if metrica == "Quantidade de Vendas":
            self.df_grouped = df_valid.groupby(grouper).size().reset_index(name='Valor')
            ylabel = "Qtd. de Vendas"
        else:
            self.df_grouped = df_valid.groupby(grouper)['CRMov2VlrO'].sum().reset_index(name='Valor')
            ylabel = "Valor Total (R$)"
            
        # Pular se nulo
        if self.df_grouped.empty: return
        
        # Formata x para exibição (pandas period Mês não plota nativamente bem se for object string)
        self.df_grouped[grouper] = self.df_grouped[grouper].astype(str)
        
        # Plot
        self.ax.clear()
        x_vals = self.df_grouped[grouper]
        y_vals = self.df_grouped['Valor']
        
        self.ax.bar(x_vals, y_vals, color='#1E88E5', edgecolor='#1565C0')
        self.ax.set_title(f"{metrica} por {agrupamento}")
        self.ax.set_ylabel(ylabel)
        self.ax.set_xlabel(agrupamento)
        
        # Rotacionar texto eixo X se houver muitos 
        if len(x_vals) > 10:
            self.ax.tick_params(axis='x', rotation=45)
        else:
            self.ax.tick_params(axis='x', rotation=0)
            
        self.fig.tight_layout()
        self.canvas.draw()
        
    def exportar_excel(self):
        if self.df_grouped is None or self.df_grouped.empty:
            messagebox.showwarning("Aviso", "Nenhum dado gerado para exportar.")
            return
        
        filepath = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")], title="Salvar Excel", initialfile="Analise_Vendas.xlsx")
        if filepath:
            try:
                self.df_grouped.to_excel(filepath, index=False)
                messagebox.showinfo("Sucesso", f"Salvo em: {filepath}")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    def exportar_pdf(self):
        if self.df_grouped is None or self.df_grouped.empty:
            messagebox.showwarning("Aviso", "Nenhum gráfico gerado para exportar.")
            return
        
        filepath = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Salvar PDF", initialfile="Grafico_Vendas.pdf")
        if filepath:
            try:
                self.fig.savefig(filepath, format="pdf", bbox_inches="tight")
                messagebox.showinfo("Sucesso", f"Gráfico salvo em: {filepath}")
            except Exception as e:
                messagebox.showerror("Erro", str(e))\n
"""

# Inject class before MainHub
for i, line in enumerate(lines):
    if "class MainHub(ctk.CTk):" in line:
        lines.insert(i, new_class)
        break

# Modify MainHub __init__ to hook btn_analise
# and add new method abrir_analise

for i, line in enumerate(lines):
    if "self.btn_analise = ctk.CTkButton(" in line:
        # Substitui a declaração do botão sem command para o command novo
        lines[i] = line.replace('fg_color="#1E88E5"', 'command=self.abrir_analise, fg_color="#1E88E5"')
        
    if "def abrir_cep(self):" in line:
        lines.insert(i, "    def abrir_analise(self): \n        app_win = AnaliseVendasWindow(self, self.config)\n        app_win.after(100, lambda: app_win.lift())\n\n")
        break

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(lines)
    
print("Classe Análise de Vendas injetada com sucesso e botão ativado.")
