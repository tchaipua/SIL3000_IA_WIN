import re

FILE_PATH = "SIL_IA_WIN.py"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. BaseWindow Update
old_base_copy = """        btn_copy_id = ctk.CTkButton(self.bottom_bar, text="📋", width=25, height=25, fg_color="transparent", hover_color="#E0E0E0", text_color="black", font=("Arial", 11, "bold"), command=lambda: [self.clipboard_clear(), self.clipboard_append(id_str), messagebox.showinfo("Sucesso", "NOME DA TELA COPIADO")])"""

new_base_copy = """        self.id_str = id_str
        btn_copy_id = ctk.CTkButton(self.bottom_bar, text="📋", width=25, height=25, fg_color="transparent", hover_color="#E0E0E0", text_color="black", font=("Arial", 11, "bold"), command=self.acao_copiar_e_sql)"""

content = content.replace(old_base_copy, new_base_copy)

old_base_tooltip = """        ToolTip(btn_copy_id, "COPIAR NOME TELA")

    def fechar_tela(self):"""

new_base_tooltip = """        ToolTip(btn_copy_id, "COPIAR NOME TELA E VER SQL")

    def acao_copiar_e_sql(self):
        self.clipboard_clear()
        self.clipboard_append(self.id_str)
        summary = self.get_sql_summary()
        msg = f"NOME DA TELA COPIADO: {self.id_str}"
        if summary:
            msg += "\\n\\n--- ESTRUTURA SQL (RESUMO) ---\\n" + summary
        from tkinter import messagebox
        messagebox.showinfo("Informação do Sistema", msg)

    def get_sql_summary(self):
        return "Sql Data not ready"

    def fechar_tela(self):"""

content = content.replace(old_base_tooltip, new_base_tooltip)

# 2. AnaliseVendasWindow Update
old_vendas_copy = """    def copiar_id(self, texto):
        self.clipboard_clear()
        self.clipboard_append(texto)
        self.update()
        messagebox.showinfo("Sucesso", "NOME DA TELA COPIADO")"""

new_vendas_copy = """    def get_sql_summary(self):
        emp = self.config.get("empresa", "01")
        return (
            "TABELA:\\n"
            "- CRMOV2 (Vendas)\\n\\n"
            "CAMPOS UTILIZADOS:\\n"
            "- CRMovDta: Para extrair Ano, Mês e Dia da Semana\\n"
            "- CRMov2CHor: Para extrair Faixa de Horário\\n"
            "- CRMov2VlrO: Valor Base das Vendas\\n"
            "- CMEmpCod: Filtro de Empresa\\n"
            "- CRMov2Flag: Situação da Venda (A, F)\\n\\n"
            "FILTRO BASE:\\n"
            f"- CMEmpCod = '{emp}'\\n"
            "- CRMov2Flag IN ('A', 'F')\\n"
            "- CRMovDta IS NOT NULL"
        )

    def copiar_id(self, texto):
        self.clipboard_clear()
        self.clipboard_append(texto)
        self.update()
        sql_summary = self.get_sql_summary()
        from tkinter import messagebox
        messagebox.showinfo("ID Copiado + SQL Info", f"ID da Tela: {texto}\\n\\n--- RESUMO TÉCNICO SQL ---\\n{sql_summary}")"""

content = content.replace(old_vendas_copy, new_vendas_copy)

# Tooltip de grafico em AnaliseVendasWindow
old_tt = """            idx = sel.index
            label_x = self.df_grouped.iloc[idx][grouper_plot]
            qtd = self.df_grouped.iloc[idx]['Qtd']
            valor = self.df_grouped.iloc[idx]['ValorTotal']
            texto = f"{label_x}\\n----------------\\nVendas: {qtd}\\nTotal: R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            sel.annotation.set_text(texto)
            sel.annotation.get_bbox_patch().set(boxstyle="round,pad=0.5", fc="white", alpha=0.9, ec="#1E88E5")"""

new_tt = """            idx = sel.index
            label_x = self.df_grouped.iloc[idx][grouper_plot]
            qtd = self.df_grouped.iloc[idx]['Qtd']
            valor = self.df_grouped.iloc[idx]['ValorTotal']

            total_qtd = self.df_grouped['Qtd'].sum()
            total_vlr = self.df_grouped['ValorTotal'].sum()
            perc_qtd = (qtd / total_qtd * 100) if total_qtd > 0 else 0
            perc_vlr = (valor / total_vlr * 100) if total_vlr > 0 else 0

            try:
                if self.combo_visao.get() == "Horário":
                    h = int(float(label_x))
                    label_x = f"Horário das {h}-{h+1}h"
            except: pass

            fmt_v = f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            texto = (f"{label_x}\\n----------------\\n"
                    f"Quantidade: {qtd} ({perc_qtd:.1f}%)\\n"
                    f"Valor: {fmt_v} ({perc_vlr:.1f}%)\\n")
            
            sel.annotation.set_text(texto)
            sel.annotation.get_bbox_patch().set(boxstyle="round,pad=0.5", fc="white", alpha=0.9, ec="#1E88E5")"""
            
content = content.replace(old_tt, new_tt)

# 3. ResumoClienteWindow SQL Summary
resumo_cli_sig = """    def carregar_anos(self):
        try:
            import pyodbc; import pandas as pd"""

resumo_cli_sql = """    def get_sql_summary(self):
        ano = self.combo_ano.get()
        mes = self.combo_mes.get()
        emp = self.config_db.get("empresa", "01")
        meses_ext = ["Todos", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        
        where = ["CRMov2Flag IN ('A', 'F')", "CRMovDta IS NOT NULL", "YEAR(CRMovDta) != 9999", f"CMEmpCod = '{emp}'", "CRMov2CodC NOT IN (1)"]
        if ano != "Todos": where.append(f"YEAR(CRMovDta) = {int(ano)}")
        if mes != "Todos": 
            try: mes_idx = meses_ext.index(mes); where.append(f"MONTH(CRMovDta) = {mes_idx}")
            except: pass
            
        where_str = "\\n  AND ".join(where)
        limit = self.combo_top.get().replace("Top ", "")
        
        return (
            "TABELA:\\n"
            "- CRMOV2 (Vendas)\\n\\n"
            "CAMPOS UTILIZADOS:\\n"
            "- CRMov2CodC: Código do Cliente (Agrupamento)\\n"
            "- CRMov2DesC: Razão Social/Nome do Cliente\\n"
            "- CRMov2VlrO: Valor Bruto da Venda (Soma)\\n"
            "- CRMovDta: Data da Venda (Filtro Ano/Mês)\\n"
            "- CMEmpCod: Código da Empresa\\n"
            "- CRMov2Flag: Situação (Flags A=Ativa, F=Finalizada)\\n\\n"
            "FILTRO ATUAL (WHERE):\\n"
            f"  {where_str}\\n\\n"
            "AGRUPAMENTO (GROUP BY):\\n"
            f"  CRMov2CodC, CRMov2DesC (Limitado a TOP {limit})"
        )

    def carregar_anos(self):
        try:
            import pyodbc; import pandas as pd"""

content = content.replace(resumo_cli_sig, resumo_cli_sql)

# AnaliseProdutoWindow SQL Summary
prod_sig = """    def carregar_anos(self):
        server = self.config_db.get("servidor")"""

prod_sql = """    def get_sql_summary(self):
        ano = self.combo_ano.get()
        mes = self.combo_mes.get()
        pesquisa = self.txt_pesquisa.get().strip()
        emp_padrao = self.config_db.get("empresa", "01")
        
        where = ["c2.CMEmpCod = '" + emp_padrao + "'", "c4.CRMovDta IS NOT NULL", "YEAR(c4.CRMovDta) != 9999", "c2.CRMov2Flag IN ('A', 'F')"]
        if ano != "Todos": where.append(f"YEAR(c4.CRMovDta) = {int(ano)}")
        if mes != "Todos": 
            try: mes_idx = self.meses_ext.index(mes); where.append(f"MONTH(c4.CRMovDta) = {mes_idx}")
            except: pass
        if pesquisa: where.append(f"p.CEProDes LIKE '%{pesquisa}%'")
        
        where_str = "\\n  AND ".join(where)
        
        return (
            "TABELA PRINCIPAL:\\n"
            "- CEPRO p (Produtos)\\n"
            "- CRMOV4 c4 (Itens Movimento)\\n"
            "- CRMOV2 c2 (Cabeçalho)\\n\\n"
            "CAMPOS UTILIZADOS:\\n"
            "- p.CEProCod: Código do Produto (JOIN)\\n"
            "- p.CEProDes: Descrição do Produto (Filtro Busca)\\n"
            "- c4.CRMov4Qtd: Quantidade Vendida (Soma)\\n"
            "- c4.CRMov4VlrO: Valor Bruto Item (Soma)\\n"
            "- c4.CRMov4VlrC: Custo do Item (Soma p/ Lucro)\\n"
            "- c4.CRMovDta: Data Base p/ Filtros\\n"
            "- c2.CMEmpCod: Código da Empresa\\n"
            "- c2.CRMov2Flag: Filtro de Venda Ativa (A, F)\\n\\n"
            "FILTRO ATUAL (WHERE):\\n"
            f"  {where_str}"
        )

    def carregar_anos(self):
        server = self.config_db.get("servidor")"""

content = content.replace(prod_sig, prod_sql)


with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Restored successfully.")
