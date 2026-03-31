import re

with open('SIL_IA_WIN.py', 'rb') as f:
    text = f.read().decode('utf-8')

# 1. Clear out the corrupted button block
start_str = 'self.btn_pararam = ctk.CTkButton(self.col1_frame, text="🛑'
end_str = 'self.btn_vendas = ctk.CTkButton(self.col2_frame,'

try:
    start_idx = text.index(start_str)
    
    # Encontrar end_idx de maneira segura
    end_idx = text.find(end_str, start_idx)
    if end_idx == -1:
        end_idx = text.find('self.btn_vendas', start_idx)
    
    if end_idx != -1:
        clean = '''self.btn_pararam = ctk.CTkButton(self.col1_frame, text="🛑 Clientes Deixaram de Comprar", width=btn_width, height=45, font=("Arial", 13, "bold"), command=self.abrir_clientes_pararam, fg_color="#E53935", hover_color="#C62828")
        self.btn_pararam.pack(pady=8, padx=15)

        self.btn_cobranca = ctk.CTkButton(self.col2_frame, text="📞 Cobrança por Cliente", width=btn_width, height=45, font=("Arial", 13, "bold"), command=self.abrir_cobranca, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_cobranca.pack(pady=8, padx=15)

        self.btn_excluir_inativos = ctk.CTkButton(self.col2_frame, text="🗑️ Excluir Clientes Inativos", width=btn_width, height=45, font=("Arial", 13, "bold"), command=self.abrir_excluir_inativos, fg_color="#C62828", hover_color="#B12020")
        self.btn_excluir_inativos.pack(pady=8, padx=15)

        '''
        text = text[:start_idx] + clean + text[end_idx:]
except ValueError as e:
    print('Failed to find indices:', e)

# 2. Certifica-se de que os métodos de hook de MainHub estão definidos (pois podem ter sumido também dependendo de como o diff foi colado)
# O app está iniciando, então os hooks 'abrir_cobranca' precisam existir.
# Vamos injetá-los no MainHub se não existirem
if 'def abrir_cobranca' not in text:
    hooks = '''
    def abrir_cobranca(self): self.abrir_modulo(CobrancaClienteWindow)
    def abrir_excluir_inativos(self): self.abrir_modulo(ExcluirClientesInativosWindow)

    def abrir_modulo_detalhes_inativos(self, cod, nome):
        if hasattr(self, "modulo_atual") and self.modulo_atual:
             self.modulo_atual.destroy()
        self.modules_frame.pack_forget()
        from __main__ import DetalhesParcelasInativosWindow
        self.modulo_atual = DetalhesParcelasInativosWindow(self.main_frame, self.config, cod, nome)
        self.modulo_atual.hub = self
        self.modulo_atual.pack(fill="both", expand=True)

'''
    # Insere logo antes de centralizar_tela
    if 'def centralizar_tela(janela):' in text:
        text = text.replace('def centralizar_tela', hooks + 'def centralizar_tela')
    elif 'def logout(self):' in text:
        text = text.replace('    def logout(self):', hooks + '    def logout(self):')

with open('SIL_IA_WIN.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('BOTOES FIXADOS.')
