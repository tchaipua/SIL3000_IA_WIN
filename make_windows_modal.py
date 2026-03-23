import os

filepath = r"c:\Sistemas\IA\SIL3000_IA_WIN\SIL_IA_WIN.py"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Torna TabelaConfigWindow em modal (L52)
old_tabela_cfg = """    def __init__(self, parent, config, update_callback):
        super().__init__(parent)"""

new_tabela_cfg = """    def __init__(self, parent, config, update_callback):
        super().__init__(parent)
        self.grab_set()  # Trava a janela pai"""

if old_tabela_cfg in content:
    content = content.replace(old_tabela_cfg, new_tabela_cfg)

# 2. Torna ConfigWindow em modal (L140)
old_cfg = """    def __init__(self, parent, config, update_callback):
        super().__init__(parent)"""

new_cfg = """    def __init__(self, parent, config, update_callback):
        super().__init__(parent)
        self.grab_set()  # Trava a janela pai"""

if old_cfg in content:
    content = content.replace(old_cfg, new_cfg)

# 3. Torna Janela CEP (App) em modal (L198)
old_cep = """    def __init__(self, parent, db_config):
        super().__init__(parent)"""

new_cep = """    def __init__(self, parent, db_config):
        super().__init__(parent)
        self.grab_set()  # Trava a janela pai"""

if old_cep in content:
    content = content.replace(old_cep, new_cep)

# 4. Torna Janela AnaliseVendas em modal (L646)
old_analise = """    def __init__(self, parent, config):
        super().__init__(parent)"""

new_analise = """    def __init__(self, parent, config):
        super().__init__(parent)
        self.grab_set()  # Trava a janela pai"""

if old_analise in content:
    content = content.replace(old_analise, new_analise)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Janelas configuradas para Modais (grab_set).")
