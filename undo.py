import os

filepath = r"c:\Sistemas\IA\SIL3000_IA_WIN\SIL_IA_WIN.py"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_code = """        self.grid_rowconfigure(0, weight=1); self.grid_columnconfigure(1, weight=1)

        # Sidebar
        self.sidebar_frame = ctk.CTkFrame(self, width=240, corner_radius=0); self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        ctk.CTkLabel(self.sidebar_frame, text="Módulos", font=("Arial", 22, "bold")).pack(pady=30)
        ctk.CTkButton(self.sidebar_frame, text="📍 Atualizador de CEP", height=40, font=("Arial", 14, "bold"), command=self.abrir_cep, fg_color="#1E88E5", hover_color="#1565C0").pack(pady=10, padx=20, fill="x")
        ctk.CTkButton(self.sidebar_frame, text="⚙️ Configurações", height=40, command=self.abrir_configuracoes, fg_color="#455A64").pack(pady=10, padx=20, fill="x", side="bottom")

        # Main Area
        self.main_frame = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0); self.main_frame.grid(row=0, column=1, sticky="nsew")

        # Carregar logo
        logo_path = os.path.join(os.path.dirname(__file__), "logo_msinfor.jpg")
        if os.path.exists(logo_path):
            try:
                logo_img = Image.open(logo_path)
                # O logotipo é redondo, tamanho 250x250 fica excelente e proporcional
                self.logo_image = ctk.CTkImage(light_image=logo_img, dark_image=logo_img, size=(250, 250))
                self.logo_label = ctk.CTkLabel(self.main_frame, text="", image=self.logo_image)
                self.logo_label.pack(expand=True, pady=(60, 0))
            except Exception as e:
                print(f"❌ Erro ao renderizar Logo: {e}")
        else:
             ctk.CTkLabel(self.main_frame, text="MSINFOR Sistemas", font=("Arial", 28, "bold"), text_color="#1E1E1E").pack(expand=True)

        ctk.CTkLabel(self.main_frame, text="Hub Principal", font=("Arial", 18, "italic"), text_color="gray").pack(expand=True, pady=(0, 80))

        # Rodapé
        self.footer_frame = ctk.CTkFrame(self, height=35, fg_color="#1E1E1E"); self.footer_frame.grid(row=1, column=1, sticky="ew")
        self.lbl_footer = ctk.CTkLabel(self.footer_frame, text="", text_color="white", font=("Arial", 11)); self.lbl_footer.pack(side="left", padx=15, expand=True)
        self.atualizar_rodape()

    def atualizar_rodape(self):
        self.lbl_footer.configure(text=f"👤 {self.config['nome_usuario']}  |  🖥️ {self.config['servidor']}  |  🗄️ {self.config['banco']}")

    def abrir_configuracoes(self): 
        ConfigWindow(self, self.config, lambda c: [setattr(self, 'config', c), self.atualizar_rodape()])

    def abrir_cep(self): 
        app_win = App(self, self.config)
        app_win.after(100, lambda: app_win.lift())"""

anchor_start = 'self.config = {"nome_usuario": "Operador", "servidor": r"servidor\\sqlexpress", "banco": "msinfor", "usuario_bd": "sa", "senha_bd": "Mabelu2011"}'
index_start = content.find(anchor_start)

if index_start == -1:
    print("Erro: Âncora de início não encontrada")
    exit(1)

index_start += len(anchor_start) + 1

anchor_end = "def centralizar_tela(tela, w, h):"
index_end = content.find(anchor_end)

if index_end == -1:
    print("Erro: Âncora de fim não encontrada")
    exit(1)

new_content = content[:index_start] + old_code + "\n\n" + content[index_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Restaurado com sucesso!")
