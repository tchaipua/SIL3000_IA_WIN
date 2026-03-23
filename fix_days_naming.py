import os

filepath = r"c:\Sistemas\IA\SIL3000_IA_WIN\SIL_IA_WIN.py"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Modifica carregar_dados para usar Categorical limpo
old_dias = """            # Dias da Semana
            dias_dict = {0:"02 - Segunda-feira", 1:"03 - Terça-feira", 2:"04 - Quarta-feira", 3:"05 - Quinta-feira", 4:"06 - Sexta-feira", 5:"07 - Sábado", 6:"01 - Domingo"}
            self.df_raw['Dia_Semana'] = self.df_raw['CRMovDta'].dt.dayofweek.map(dias_dict)"""

new_dias = """            # Dias da Semana
            dias_dict = {0:"Segunda-feira", 1:"Terça-feira", 2:"Quarta-feira", 3:"Quinta-feira", 4:"Sexta-feira", 5:"Sábado", 6:"Domingo"}
            self.df_raw['Dia_Semana'] = self.df_raw['CRMovDta'].dt.dayofweek.map(dias_dict)
            
            dias_ordem = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
            import pandas as pd
            self.df_raw['Dia_Semana'] = pd.Categorical(self.df_raw['Dia_Semana'], categories=dias_ordem, ordered=True)"""

if old_dias in content:
    content = content.replace(old_dias, new_dias)

# 2. Modifica gerar_grafico para grouper de lista no duo
old_agrupamento = """        elif visao == "Dia da Semana + Horário":
            grouper = 'Dia_Horario'
            agrupamento_str = "Dia da Semana + Horário" """

new_agrupamento = """        elif visao == "Dia da Semana + Horário":
            grouper = ['Dia_Semana', 'Hora']
            agrupamento_str = "Dia da Semana + Horário" """

if old_agrupamento in content:
    content = content.replace(old_agrupamento, new_agrupamento)

# 3. Tratamento pós-agregacao no dataframe agrupado para montar rótulo de exibição
old_pos_agg = """        if self.df_grouped.empty: return"""
new_pos_agg = """        if self.df_grouped.empty: return
        
        # Cria rótulo combinado para visão duo list
        if isinstance(grouper, list):
            self.df_grouped['Dia_Horario'] = self.df_grouped['Dia_Semana'].astype(str) + " - " + self.df_grouped['Hora'].map(lambda x: f"{int(x):02d}h")
            grouper_plot = 'Dia_Horario'
        else:
            grouper_plot = grouper"""

if old_pos_agg in content:
    # Como o IF nulo aparece duas vezes ou é bem comum, vamos achar o groupby
    old_calc = """        self.df_grouped = df_valid.groupby(grouper).agg(
            Qtd=('CRMovDta', 'size'),
            ValorTotal=('CRMov2VlrO', 'sum')
        ).reset_index()"""
        
    new_calc = """        self.df_grouped = df_valid.groupby(grouper).agg(
            Qtd=('CRMovDta', 'size'),
            ValorTotal=('CRMov2VlrO', 'sum')
        ).reset_index()
        
        # Cria rótulo combinado para visão duo list
        if isinstance(grouper, list):
            self.df_grouped['Dia_Horario'] = self.df_grouped['Dia_Semana'].astype(str) + " - " + self.df_grouped['Hora'].map(lambda x: f"{int(x):02d}h")
            grouper_plot = 'Dia_Horario'
        else:
            grouper_plot = grouper"""
            
    if old_calc in content:
         content = content.replace(old_calc, new_calc)

# 4. Ajustar variáveis de plotagem para usar grouper_plot
content = content.replace("self.df_grouped[grouper]", "self.df_grouped[grouper_plot]")
content = content.replace("x_vals = self.df_grouped[grouper]", "x_vals = self.df_grouped[grouper_plot]")
content = content.replace("for bar, label in zip(bars, self.df_grouped[grouper]):", "for bar, label in zip(bars, self.df_grouped[grouper_plot]):")

# 5. Ajustar a ordenação e os rótulos de tooltip que passam grouper
old_cursor = """        # Tooltip interativo com mplcursors
        cursor = mplcursors.cursor(bars, hover=True)
        
        @cursor.connect("add")
        def on_add(sel):"""
# Como já tem bastante replace, vamos rodar essa primeira parte e garantir que o grouper_plot está sendo usado onde deve.

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Ajuste de Categoria e Duo-Grouping aplicado!")
