import os

filepath = r"c:\Sistemas\IA\SIL3000_IA_WIN\SIL_IA_WIN.py"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Altera ComboBox de Visão Especial para remover "Dia da Semana + Horário"
old_combo = """self.combo_visao = ctk.CTkComboBox(self.top_grid_frame, values=["Padrão", "Horário", "Dias da Semana", "Dia da Semana + Horário"], width=190)"""
new_combo = """self.combo_visao = ctk.CTkComboBox(self.top_grid_frame, values=["Padrão", "Horário", "Dias da Semana"], width=190)"""

if old_combo in content:
    content = content.replace(old_combo, new_combo)

# 2. Em carregar_dados, injeta criador de Faixa_Horario
old_hora = """            self.df_raw['Hora'] = self.df_raw['CRMov2CHor'].apply(extrair_hora)"""
new_hora = """            self.df_raw['Hora'] = self.df_raw['CRMov2CHor'].apply(extrair_hora)
            
            def extrair_faixa(h):
                try:
                    hora_int = int(str(h).replace(':', '')[:2])
                    if hora_int >= 24: return None
                    lim = (hora_int // 2) * 2
                    return f"{lim:02d}h às {lim+2:02d}h"
                except: return None
            
            self.df_raw['Faixa_Horario'] = self.df_raw['CRMov2CHor'].apply(extrair_faixa)"""

if old_hora in content:
    content = content.replace(old_hora, new_hora)

# 3. Em gerar_grafico, muda 'Hora' para 'Faixa_Horario' e remove o bloco de Dia+Hora
old_agrupar = """        if visao == "Horário":
            grouper = 'Hora'
            agrupamento_str = "Faixa de Horário"
        elif visao == "Dias da Semana":
            grouper = 'Dia_Semana'
            agrupamento_str = "Dia da Semana"
        elif visao == "Dia da Semana + Horário":
            grouper = ['Dia_Semana', 'Hora']
            agrupamento_str = "Dia da Semana + Horário" """

new_agrupar = """        if visao == "Horário":
            grouper = 'Faixa_Horario'
            agrupamento_str = "Faixa de Horário"
        elif visao == "Dias da Semana":
            grouper = 'Dia_Semana'
            agrupamento_str = "Dia da Semana" """

if old_agrupar in content:
    content = content.replace(old_agrupar, new_agrupar)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Faixa de 2h configurada e agrupadores atualizados.")
