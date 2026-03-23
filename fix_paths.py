import os

filepath = r"c:\Sistemas\IA\SIL3000_IA_WIN\SIL_IA_WIN.py"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Substitui o carregamento da imagem em App (CEP)
old_cep = """        try:
            img_fechar_pil = Image.open("btn_fechar.png")"""
            
new_cep = """        try:
            img_fechar_pil = Image.open(os.path.join(os.path.dirname(__file__), "btn_fechar.png"))"""

if old_cep in content:
    content = content.replace(old_cep, new_cep)

# Substitui o carregamento da imagem em AnaliseVendasWindow
old_analise = """        try:
            img_fechar_pil = Image.open("btn_fechar.png")"""

# O replace acima pode ser idêntico, então vamos usar um replace simples
content = content.replace('Image.open("btn_fechar.png")', 'Image.open(os.path.join(os.path.dirname(__file__), "btn_fechar.png"))')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Caminhos de imagem ajustados para empacotamento PyInstaller.")
