import os

filepath = r"c:\Sistemas\IA\SIL3000_IA_WIN\SIL_IA_WIN.py"

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 1. Modifica o Layout Topo para Grid
top_start = -1
top_end = -1
for i, line in enumerate(lines):
    if "self.top_frame = ctk.CTkFrame(self)" in line:
        top_start = i
    elif "self.chart_frame = ctk.CTkFrame(self, fg_color=" in line:
        top_end = i
        break

if top_start != -1 and top_end != -1:
    new_topo = """        # 3. Topo: Controles
        self.top_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.top_frame.pack(side="top", fill="x", padx=20, pady=10)
        
        # Sub-container interno para margens
        self.top_grid_frame = ctk.CTkFrame(self.top_frame)
        self.top_grid_frame.pack(side="top", fill="x", padx=10, pady=10)
        self.top_grid_frame.grid_columnconfigure((1, 3, 5), weight=1)

        # LINHA 0
        ctk.CTkLabel(self.top_grid_frame, text="Ano:").grid(row=0, column=0, padx=(15, 5), pady=8, sticky="e")
        self.combo_ano = ctk.CTkComboBox(self.top_grid_frame, values=["Todos"], width=100)
        self.combo_ano.grid(row=0, column=1, padx=5, pady=8, sticky="ew")
        self.combo_ano.set("Todos")

        ctk.CTkLabel(self.top_grid_frame, text="Mês:").grid(row=0, column=2, padx=(15, 5), pady=8, sticky="e")
        self.meses = ["Todos", "01 - Janeiro", "02 - Fevereiro", "03 - Março", "04 - Abril", "05 - Maio", "06 - Junho", "07 - Julho", "08 - Agosto", "09 - Setembro", "10 - Outubro", "11 - Novembro", "12 - Dezembro"]
        self.combo_mes = ctk.CTkComboBox(self.top_grid_frame, values=self.meses, width=140)
        self.combo_mes.grid(row=0, column=3, padx=5, pady=8, sticky="ew")
        self.combo_mes.set("Todos")

        ctk.CTkLabel(self.top_grid_frame, text="Visão Especial:").grid(row=0, column=4, padx=(15, 5), pady=8, sticky="e")
        self.combo_visao = ctk.CTkComboBox(self.top_grid_frame, values=["Padrão", "Horário", "Dias da Semana", "Dia da Semana + Horário"], width=190)
        self.combo_visao.grid(row=0, column=5, padx=5, pady=8, sticky="ew")
        self.combo_visao.set("Padrão")

        # LINHA 1 - Botão Atualizar Gráficos alinhado abaixo de Ano
        self.btn_gerar = ctk.CTkButton(self.top_grid_frame, text="Atualizar Gráfico", command=self.gerar_grafico, fg_color="#1E88E5", hover_color="#1565C0", width=130)
        self.btn_gerar.grid(row=1, column=1, padx=5, pady=8, sticky="ew")

        ctk.CTkLabel(self.top_grid_frame, text="Métrica:").grid(row=1, column=2, padx=(15, 5), pady=8, sticky="e")
        self.combo_metrica = ctk.CTkComboBox(self.top_grid_frame, values=["Quantidade de Vendas", "Valor Total (R$)"], width=200)
        self.combo_metrica.grid(row=1, column=3, padx=5, pady=8, sticky="ew")
        self.combo_metrica.set("Valor Total (R$)")\n\n"""
    
    lines = lines[:top_start] + [new_topo] + lines[top_end:]

content = "".join(lines)

# 2. Injeta lógica de DataFrame Combinada para Dia_Horario em carregar_dados
old_hora = r"""            self.df_raw['Hora'] = self.df_raw['CRMov2CHor'].apply(extrair_hora)"""
new_hora = r"""            self.df_raw['Hora'] = self.df_raw['CRMov2CHor'].apply(extrair_hora)
            
            # Combinação Dia da Semana + Hora
            mask = self.df_raw['Hora'].notna() & self.df_raw['Dia_Semana'].notna()
            self.df_raw.loc[mask, 'Dia_Horario'] = self.df_raw.loc[mask, 'Dia_Semana'] + self.df_raw.loc[mask, 'Hora'].apply(lambda x: f" - {int(x):02d}h")"""

if old_hora in content:
    content = content.replace(old_hora, new_hora)

# 3. Injeta o Elif em gerar_grafico
old_elif_visao = r"""        elif visao == "Dias da Semana":
            grouper = 'Dia_Semana'
            agrupamento_str = "Dia da Semana"
        else:"""

new_elif_visao = r"""        elif visao == "Dias da Semana":
            grouper = 'Dia_Semana'
            agrupamento_str = "Dia da Semana"
        elif visao == "Dia da Semana + Horário":
            grouper = 'Dia_Horario'
            agrupamento_str = "Dia da Semana + Horário"
        else:"""

if old_elif_visao in content:
    content = content.replace(old_elif_visao, new_elif_visao)

# 4. Injeta a Ordenação
old_sort = r"""        if grouper in ['Mes_Extenso', 'Dia_Semana']:"""
new_sort = r"""        if grouper in ['Mes_Extenso', 'Dia_Semana', 'Dia_Horario']:"""

if old_sort in content:
    content = content.replace(old_sort, new_sort)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injeção Layout Grid Completa e Alinhamentos Resolvidos")
