import os

search_dir = r'C:\Sistemas'
matches = []

# To avoid crashing on infinite loops or huge folders, we can keep it to relevant files.
relevant_exts = ('.cs', '.py', '.txt', '.bat', '.config', '.csproj', '.sln')

for root, dirs, files in os.walk(search_dir):
    # Skip large folders that aren't source code
    if 'node_modules' in dirs: dirs.remove('node_modules')
    if 'bin' in dirs: dirs.remove('bin')
    if 'obj' in dirs: dirs.remove('obj')
    
    for file in files:
        if file.lower().endswith(relevant_exts):
            path = os.path.join(root, file)
            # Avoid HUGE XML files just to find containing code
            if file.lower().endswith('.xml') and os.path.getsize(path) > 10 * 1024 * 1024:
                continue
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if 'refazer cep' in content.lower() or ('cep' in content.lower() and ('update' in content.lower() or 'connection' in content.lower())):
                        matches.append(path)
            except:
                pass

print("Files containing 'cep' or 'refazer cep':")
for m in matches:
    print(m)
