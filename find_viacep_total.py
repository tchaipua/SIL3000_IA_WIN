import os

search_root = 'C:\\\\'
exclude_dirs = {r'C:\Windows', r'C:\Program Files', r'C:\Program Files (x86)', r'C:\$Recycle.Bin', r'C:\System Volume Information'}

matches = []

print("Iniciando varredura rápida em C:\\...")

for root, dirs, files in os.walk(search_root):
    # Exclude system folders
    if any(root.startswith(ex) for ex in exclude_dirs):
        continue
    if '.git' in dirs: dirs.remove('.git')
    if 'node_modules' in dirs: dirs.remove('node_modules')

    for file in files:
        if file.lower().endswith('.py'):
            path = os.path.join(root, file)
            try:
                # Small size threshold to run fast
                if os.path.getsize(path) < 5 * 1024 * 1024: 
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        if 'viacep' in f.read().lower():
                            matches.append(path)
            except:
                pass

print("\n--- RESULTADO DA BUSCA ---")
if matches:
    for m in matches:
        print(m)
else:
    print("Nenhum arquivo .py com 'viacep' encontrado.")
