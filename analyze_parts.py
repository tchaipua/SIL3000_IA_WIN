import xml.etree.ElementTree as ET

# We'll parse the file in chunks or just look for <Part> tags
child_tags = set()
part_types = {}

with open('C:\\Sistemas\\IA\\SIL_IA\\tabelas_win.xml', 'r', encoding='utf-8') as f:
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
                    # Parse this single object
                    root = ET.fromstring(content)
                    if root.attrib.get('type') == '857ca50e-7905-0000-0007-c5d9ff2975ec': # Table
                        for part in root.findall('.//Part'):
                            ptype = part.attrib.get('type')
                            part_types[ptype] = part_types.get(ptype, 0) + 1
                            for child in part:
                                child_tags.add(child.tag)
                except Exception as e:
                    pass # Skip invalid XML if any (e.g. nested things)

print("Child tags found inside <Part> in Table objects:")
for tag in child_tags:
    print(tag)

print("\nPart types present in Table objects:")
for k, v in part_types.items():
    print(f"Type: {k}, Count: {v}")
