import re

types = set()
try:
    with open('C:\\Sistemas\\IA\\SIL_IA\\tabelas_win.xml', 'r', encoding='utf-8') as f:
        for line in f:
            match = re.search(r'<Object[^>]+type="([^"]+)"', line)
            if match:
                types.add(match.group(1))
except Exception as e:
    print(f"Error: {e}")

print("Unique types:")
for t in types:
    print(t)
