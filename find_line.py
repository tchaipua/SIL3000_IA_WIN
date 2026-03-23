with open(r'C:\Sistemas\IA\SIL_IA\Atualizador_CEPs_ViaCEP.py', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'sair' in line.lower() or 'voltar' in line.lower() or 'atualiza_cep' in line.upper():
            print(f"Linha {i+1}: {line.strip()}")
