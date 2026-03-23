import os

filepath = r"c:\Sistemas\IA\SIL3000_IA_WIN\SIL_IA_WIN.py"

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

cut_index = -1
for i, line in enumerate(lines):
    if "class MainHub(ctk.CTk):" in line:
        cut_index = i
        break

if cut_index == -1:
    print("Erro: 'class MainHub' não encontrada")
    exit(1)

content_before = "".join(lines[:cut_index])

new_main_hub = """class MainHub(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SIL_IA_WIN")
        self.geometry("1000x650")
        self.after(100, lambda: self.state("zoomed"))
        ctk.set_appearance_mode("Light")
        
        self.config = {"nome_usuario": "Operador", "servidor": r"servidor\\sqlexpress", "banco": "msinfor", "usuario_bd": "sa", "senha_bd": "Mabelu2011"}
        self.grid_rowconfigure(0, weight=1); self.grid_columnconfigure(1, weight=1)

        # Sidebar (Faixa Azul)
        self.sidebar_frame = ctk.CTkFrame(self, width=250, corner_radius=0, fg_color="#1565C0")
        self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        
        self.sb_header = ctk.CTkFrame(self.sidebar_frame, fg_color="transparent")
        self.sb_header.pack(fill="x", padx=15, pady=(25, 10))
        
        logo_path = os.path.join(os.path.dirname(__file__), "logo_msinfor.jpg")
        if os.path.exists(logo_path):
            try:
                logo_img = Image.open(logo_path)
                self.logo_image = ctk.CTkImage(light_image=logo_img, dark_image=logo_img, size=(45, 45))
                self.logo_label = ctk.CTkLabel(self.sb_header, text="", image=self.logo_image)
                self.logo_label.pack(side="left")
            except Exception as e: pass

        ctk.CTkLabel(self.sb_header, text="Módulos", font=("Arial", 18, "bold"), text_color="white").pack(side="left", padx=10)
        ctk.CTkFrame(self.sidebar_frame, height=2, fg_color="#1E88E5").pack(fill="x", padx=15, pady=(5, 15))

        # Main Area
        self.main_frame = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        ctk.CTkLabel(self.main_frame, text="Hub Principal", font=("Arial", 18, "italic"), text_color="gray").pack(pady=(20, 0))

        # Frame centralizado para os módulos (Cards)
        self.center_box = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.center_box.place(relx=0.5, rely=0.4, anchor="center")
        
        self.btn_cep = ctk.CTkButton(self.center_box, text="📍 Atualizador de CEP", width=220, height=130, font=("Arial", 16, "bold"), command=self.abrir_cep, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_cep.grid(row=0, column=0, padx=20, pady=20)

        self.btn_config = ctk.CTkButton(self.center_box, text="⚙️ Configurações", width=220, height=130, font=("Arial", 16, "bold"), command=self.abrir_configuracoes, fg_color="#455A64", hover_color="#37474F")
        self.btn_config.grid(row=0, column=1, padx=20, pady=20)

        # Rodapé
        self.footer_frame = ctk.CTkFrame(self, height=35, fg_color="#1E1E1E")
        self.footer_frame.grid(row=1, column=1, sticky="ew")
        
        # ID da Tela no Canto Direito
        self.frame_id = ctk.CTkFrame(self.footer_frame, fg_color="transparent")
        self.frame_id.pack(side="right", padx=15)
        
        self.lbl_tela_id = ctk.CTkLabel(self.frame_id, text="📌 TELA_ID: MAIN_HUB", font=ctk.CTkFont(size=11, weight="bold"), text_color="gray")
        self.lbl_tela_id.pack(side="left")
        
        self.btn_copy_id = ctk.CTkButton(self.frame_id, text="📋", width=20, height=20, fg_color="transparent", hover_color="#333333", text_color="white", command=lambda: self.copiar_id("MAIN_HUB"))
        self.btn_copy_id.pack(side="left", padx=5)
        ToolTip(self.btn_copy_id, "COPIAR NOME TELA")

        self.lbl_footer = ctk.CTkLabel(self.footer_frame, text="", text_color="white", font=("Arial", 11))
        self.lbl_footer.pack(side="left", padx=15, expand=True)
        self.atualizar_rodape()

    def copiar_id(self, texto):
         self.clipboard_clear()
         self.clipboard_append(texto)
         self.update()
         messagebox.showinfo("Sucesso", "NOME DA TELA COPIADO")

    def atualizar_rodape(self):
        self.lbl_footer.configure(text=f"👤 {self.config['nome_usuario']}  |  🖥️ {self.config['servidor']}  |  🗄️ {self.config['banco']}")

    def abrir_configuracoes(self): 
        ConfigWindow(self, self.config, lambda c: [setattr(self, 'config', c), self.atualizar_rodape()])

    def abrir_cep(self): 
        app_win = App(self, self.config)
        app_win.after(100, lambda: app_win.lift())

def centralizar_tela(tela, w, h):
    x = (tela.winfo_screenwidth() // 2) - (w // 2)
    y = (tela.winfo_screenheight() // 2) - (h // 2)
    tela.geometry(f"{w}x{h}+{x}+{y}")

if __name__ == '__main__':
    app = MainHub()
    app.mainloop()
"""

new_content = content_before + new_main_hub

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Limpeza e Layout aplicados com sucesso!")
