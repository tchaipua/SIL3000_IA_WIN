import xml.etree.ElementTree as ET
import os

xml_path = r'C:\Sistemas\IA\SIL_IA\tabelas_win.xml'
out_path = r'C:\Sistemas\IA\SIL_IA\documentacao_tabelas.md'

tables = []

try:
    with open(xml_path, 'r', encoding='utf-8') as f:
        content = ""
        in_object = False
        for line in f:
            if '<Object' in line:
                in_object = True
                content = ""
            if in_object:
                content += line
                if '</Object>' in line:
                    in_object = False
                    try:
                        root = ET.fromstring(content)
                        if root.attrib.get('type') == '857ca50e-7905-0000-0007-c5d9ff2975ec': # Table
                            name = root.attrib.get('name')
                            # Find description from properties
                            desc = name
                            for prop in root.findall('.//Properties/Property'):
                                if prop.find('Name').text == 'Description':
                                    desc = prop.find('Value').text if prop.find('Value') is not None else name
                            
                            # Keys
                            keys = []
                            key_part = root.find(".//Part[@type='00000000-0000-0000-0002-000000000004']")
                            if key_part is not None:
                                for item in key_part.findall('.//Item'):
                                    if item.text:
                                        keys.append(item.text.strip())
                            
                            # Indexes
                            indexes = []
                            index_part = root.find(".//Part[@type='a5c0e770-560d-0001-0001-7fe71c260de3']")
                            if index_part is not None:
                                for index in index_part.findall('.//Index'):
                                    idx_type = index.attrib.get('Type')
                                    idx_name = index.attrib.get('name')
                                    members = []
                                    for member in index.findall('.//Member'):
                                        if member.text:
                                            members.append(member.text.strip())
                                    if idx_name:
                                        indexes.append({
                                            'name': idx_name,
                                            'type': idx_type,
                                            'members': members
                                        })
                            tables.append({
                                'name': name,
                                'desc': desc,
                                'keys': keys,
                                'indexes': indexes
                            })
                    except Exception as e:
                        pass # Skip invalid XML chunks

    # Build Markdown
    with open(out_path, 'w', encoding='utf-8') as md:
        md.write("# 📋 Documentação das Tabelas (GeneXus)\n\n")
        md.write("Esta documentação foi extraída automaticamente de `tabelas_win.xml`.\n\n")
        
        md.write("## 🗂️ Lista de Tabelas e Chaves\n\n")
        md.write("| Tabela | Descrição | Chave Primária |\n")
        md.write("| :--- | :--- | :--- |\n")
        for t in tables:
            key_str = ", ".join([f"`{k}`" for k in t['keys']]) if t['keys'] else "*N/A*"
            md.write(f"| `{t['name']}` | {t['desc']} | {key_str} |\n")
        
        md.write("\n---\n\n")
        md.write("## 🔍 Detalhes de Índices de Cada Tabela\n\n")
        for t in tables:
            md.write(f"### 📌 {t['name']}\n")
            md.write(f"- **Descrição:** {t['desc']}\n")
            key_str = ", ".join([f"`{k}`" for k in t['keys']]) if t['keys'] else "N/A"
            md.write(f"- **Chave Primária:** {key_str}\n")
            if t['indexes']:
                md.write("- **Índices:**\n")
                for ix in t['indexes']:
                    member_str = ", ".join([f"`{m}`" for m in ix['members']])
                    md.write(f"  - `{ix['name']}` ({ix['type']}): {member_str}\n")
            md.write("\n")

    print(f"Documentação gerada com sucesso em {out_path}")
except Exception as e:
    print(f"Erro geral: {e}")
