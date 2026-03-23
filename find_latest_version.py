import os
import glob

history_dir = r'C:\Users\User\AppData\Roaming\Antigravity\User\History'
matches = []

for root, dirs, files in os.walk(history_dir):
    for file in files:
        if file.lower().endswith('.py'):
            path = os.path.join(root, file)
            try:
                if os.path.getsize(path) < 1024 * 1024:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read().lower()
                        if 'viacep' in content and ('pyodbc' in content or 'connect' in content):
                            matches.append((path, os.path.getmtime(path)))
            except:
                pass

if matches:
    # Sort by modification time descending -> newest first
    matches.sort(key=lambda x: x[1], reverse=True)
    
    print("\n--- VERSÕES ENCONTRADAS (MAIS NOVAS PRIMEIRO) ---")
    for i, (path, mtime) in enumerate(matches[:5]): # Show top 5
        print(f"{i+1}. {path} - Tamanho: {os.path.getsize(path)} bytes")
else:
    print("Nenhuma versão encontrada.")
