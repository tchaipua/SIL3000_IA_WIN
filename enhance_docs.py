import xml.etree.ElementTree as ET
import os

xml_path = r'C:\Sistemas\IA\SIL_IA\tabelas_win.xml'
out_path = r'C:\Sistemas\IA\SIL_IA\documentacao_tabelas.md'

attributes = {} # name -> { 'type': '', 'len': '', 'dec': '', 'desc': '' }
tables = {}     # name -> { 'desc': '', 'keys': [], 'indexes': [], 'fields': [] }
transactions = []

# First Pass: Parse Attributes and Tables using iterparse
print("Iniciando a leitura do XML (61MB)...")

try:
    context = ET.iterparse(xml_path, events=('end',))
    for event, elem in context:
        if elem.tag == 'Object':
            guid = elem.attrib.get('guid')
            name = elem.attrib.get('name')
            type_guid = elem.attrib.get('type')
            
            # 1. Attributes / Domains
            if type_guid == '00972a17-9975-449e-aab1-d26165d51393':
                desc = name
                atype = "N/A"
                alen = ""
                adec = ""
                for prop in elem.findall('.//Properties/Property'):
                    p_name = prop.find('Name').text
                    p_val = prop.find('Value').text if prop.find('Value') is not None else ""
                    if p_name == 'Description': desc = p_val
                    elif p_name == 'ATTCUSTOMTYPE': atype = p_val
                    elif p_name == 'Length': alen = p_val
                    elif p_name == 'Decimals': adec = p_val
                
                attributes[name.lower()] = {
                    'name': name,
                    'desc': desc,
                    'type': atype.replace('bas:', ''),
                    'len': alen,
                    'dec': adec
                }

            # 2. Table Objects
            elif type_guid == '857ca50e-7905-0000-0007-c5d9ff2975ec':
                desc = name
                for prop in elem.findall('.//Properties/Property'):
                    if prop.find('Name').text == 'Description':
                        desc = prop.find('Value').text if prop.find('Value') is not None else name
                
                keys = []
                key_part = elem.find(".//Part[@type='00000000-0000-0000-0002-000000000004']")
                if key_part is not None:
                    for item in key_part.findall('.//Item'):
                        if item.text: keys.append(item.text.strip())

                indexes = []
                index_part = elem.find(".//Part[@type='a5c0e770-560d-0001-0001-7fe71c260de3']")
                if index_part is not None:
                    for idx in index_part.findall('.//Index'):
                        idx_name = idx.attrib.get('name', 'Index')
                        idx_type = idx.attrib.get('Type', 'Duplicate')
                        members = [m.text.strip() for m in idx.findall('.//Member') if m.text]
                        if idx_name:
                            indexes.append({'name': idx_name, 'type': idx_type, 'members': members})

                tables[name.lower()] = {
                    'name': name,
                    'desc': desc,
                    'keys': keys,
                    'indexes': indexes,
                    'fields': []
                }

            # 3. Transaction Objects (Collect for level derivation)
            elif type_guid == '1db606f2-af09-4cf9-a3b5-b481519d28f6':
                level_root = elem.find(".//Part[@type='264be5fb-1b28-4b25-a598-6ca900dd059f']/Level")
                if level_root is not None:
                    transactions.append(level_root)

            elem.clear() # clear memory for this element

    print(f"Lidos {len(attributes)} atributos, {len(tables)} tabelas e {len(transactions)} transações.")

    # Pass 2: Map Transaction Levels to Tables
    def traverse_level(level_node, parent_keys, parent_all_attrs):
        this_keys = list(parent_keys)
        this_all_attrs = list(parent_all_attrs)
        
        for attr in level_node.findall('Attribute'):
            attr_name = attr.text.strip()
            is_key = attr.attrib.get('key') == 'True'
            if is_key and attr_name not in this_keys:
                this_keys.append(attr_name)
            if attr_name not in this_all_attrs:
                this_all_attrs.append(attr_name)

        # Match with tables based on keys
        pk_set = set([k.lower() for k in this_keys])
        for t_key, t_data in tables.items():
            if set([k.lower() for k in t_data['keys']]) == pk_set:
                for a in this_all_attrs:
                    if a.lower() not in [f.lower() for f in t_data['fields']]:
                        t_data['fields'].append(a)

        for sub_level in level_node.findall('Level'):
            traverse_level(sub_level, this_keys, this_all_attrs)

    print("Associando campos das transações às tabelas...")
    for root_lvl in transactions:
        traverse_level(root_lvl, [], [])

    # Pass 3: Build Markdown
    print("Gerando documentação...")
    with open(out_path, 'w', encoding='utf-8') as md:
        md.write("# 📋 Documentação das Tabelas (GeneXus Completo)\n\n")
        md.write("Esta documentação reúne definições físicas e lógicas de colunas.\n\n")
        
        md.write("## 🗂️ Lista de Tabelas e Chaves\n\n")
        md.write("| Tabela | Descrição | Chave Primária | Nro de Campos |\n")
        md.write("| :--- | :--- | :--- | :--- |\n")
        for t_key, t in tables.items():
            key_str = ", ".join([f"`{k}`" for k in t['keys']]) if t['keys'] else "*N/A*"
            md.write(f"| `{t['name']}` | {t['desc']} | {key_str} | {len(t['fields'])} |\n")
        md.write("\n---\n\n")

        md.write("## 🔍 Detalhamento de Campos e Índices\n\n")
        for t_key, t in tables.items():
            md.write(f"### 📌 {t['name']}\n")
            md.write(f"- **Descrição:** {t['desc']}\n")
            key_str = ", ".join([f"`{k}`" for k in t['keys']])
            md.write(f"- **Chave Primária:** {key_str}\n\n")

            # Fields
            md.write("#### 📄 Colunas / Campos\n")
            if t['fields']:
                md.write("| Campo | Tipo | Descrição |\n")
                md.write("| :--- | :--- | :--- |\n")
                for f in t['fields']:
                    attr_info = attributes.get(f.lower())
                    if attr_info:
                        atype = attr_info['type']
                        if attr_info['dec'] and attr_info['dec'] != '0':
                            type_str = f"{atype}({attr_info['len']},{attr_info['dec']})"
                        elif attr_info['len']:
                            type_str = f"{atype}({attr_info['len']})"
                        else:
                            type_str = atype
                        md.write(f"| `{f}` | `{type_str}` | {attr_info['desc']} |\n")
                    else:
                        md.write(f"| `{f}` | `N/D` | - |\n")
            else:
                md.write("*Nenhum campo adicional encontrado nas transações para esta tabela.*\n")
            md.write("\n")

            # Indexes
            if t['indexes']:
                md.write("#### 🗺️ Índices\n")
                for ix in t['indexes']:
                    member_str = ", ".join([f"`{m}`" for m in ix['members']])
                    md.write(f"- `{ix['name']}` ({ix['type']}): {member_str}\n")
            md.write("\n---\n\n")

    print(f"Documentação finalizada com sucesso em {out_path}")
except Exception as e:
    print(f"Erro geral: {e}")
    import traceback
    traceback.print_exc()
