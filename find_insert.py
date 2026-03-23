with open(r'C:\Sistemas\IA\SIL_IA\Atualizador_CEPs_ViaCEP.py', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if '.insert(' in line and 'cep_atual' in line:
            print(f"Linha {i+1}: {line.strip()}")
        elif 'cep_atual =' in line:
            print(f"Linha {i+1}: {line.strip()}")
        elif 'clientes = cursor.fetchall()' in line:
            print(f"Linha {i+1}: Clientes FetchAll")
