import os

search_dir = r'C:\Users\User'
matches = []
relevant_exts = ('.cs', '.py', '.txt', '.bat', '.config', '.csproj', '.sln')

for root, dirs, files in os.walk(search_dir):
    # Skip huge folders we don't care
    if 'AppData' in root or '.gemini' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.lower().endswith(relevant_exts):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read().lower()
                    if 'cep' in content and ('update' in content or 'conexao' in content or 'sql' in content):
                        matches.append(path)
            except:
                pass

print("Files containing 'cep' or similar:")
for m in matches:
    print(m)
