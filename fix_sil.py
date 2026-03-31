import re

filepath = r"c:\Sistemas\IA\SIL3000_IA_WIN\SIL_IA_WIN.py"

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# get_sql_summary for ExcluirClientesInativosWindow (CLI_INATIVOS)
sql_inativos = r"""
    def get_sql_summary(self):
        dias = self.combo_dias.get().replace(" dias", "")
        return (
            "TABELAS:\n- CRCLI (Clientes)\n- CRMOV2 (Vendas)\n\n"
            "REGRA DE NEGÓCIO:\n- Clientes sem vendas há mais de " + dias + " dias.\n"
            "- Filtro: CRMovDta < DATEADD(day, -" + dias + ", GETDATE())\n"
            "- CRMov2Flag IN ('A', 'F')"
        )
"""
if 'class ExcluirClientesInativosWindow(BaseWindow):' in text:
    match = re.search(r'class ExcluirClientesInativosWindow\(BaseWindow\):.*?def on_click_item\(self, event\):', text, re.DOTALL)
    if match:
        text = text[:match.end()-28] + sql_inativos + text[match.end()-28:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Success: Added SQL summary to CLI_INATIVOS")
