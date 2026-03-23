import os

path_latest = r'C:\Users\User\AppData\Roaming\Antigravity\User\History\5d77f9fb\8IfQ.py'
path_out = r'C:\Sistemas\IA\SIL_IA\Atualizador_CEPs_ViaCEP.py'

with open(path_latest, 'r', encoding='utf-8') as f:
    full_latest = f.read()

# extrai App completo de 8IfQ.py
class_app_start = full_latest.index('class App(ctk.CTk):')
class_app_end = full_latest.index('if __name__ == "__main__":')
app_content = full_latest[class_app_start:class_app_end].strip()

# Adapta para Toplevel (CTkToplevel)
app_content = app_content.replace('class App(ctk.CTk):', 'class App(ctk.CTkToplevel):')
app_content = app_content.replace('super().__init__()', 'super().__init__(parent)\n        self.transient(parent)\n        centralizar_tela(self, 1100, 700)')
app_content = app_content.replace('def __init__(self):', 'def __init__(self, parent, db_config):')

# Injeta os argumentos CLI para db_config
app_content = app_content.replace('self.cfg_server = sys.argv[1] if len(sys.argv) > 1 else r"servidor\\sqlexpress"', 'self.cfg_server = db_config["servidor"]')
app_content = app_content.replace('self.cfg_db = sys.argv[2] if len(sys.argv) > 2 else "msinfor"', 'self.cfg_db = db_config["banco"]')
app_content = app_content.replace('self.cfg_user = sys.argv[3] if len(sys.argv) > 3 else "sa"', 'self.cfg_user = db_config["usuario_bd"]')
app_content = app_content.replace('self.cfg_pass = sys.argv[4] if len(sys.argv) > 4 else "Mabelu2011"', 'self.cfg_pass = db_config["senha_bd"]')

# Extrai ConfigWindow de _0CyN.py que geramos anteriormente, mas podemos apenas usar o full_latest e appendar o MainHub no pé dele!
# Na verdade, é melhor escrever o arquivo final COM o MainHub no final!

main_hub_code = """
class MainHub(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("MSINFOR Sistemas - Hub Integrado")
        self.geometry("1000x650")
        self.after(100, lambda: self.state("zoomed"))
        ctk.set_appearance_mode("Light")
        
        self.config = {"nome_usuario": "Operador", "servidor": r"servidor\\sqlexpress", "banco": "msinfor", "usuario_bd": "sa", "senha_bd": "Mabelu2011"}
        self.grid_rowconfigure(0, weight=1); self.grid_columnconfigure(1, weight=1)

        # Sidebar
        self.sidebar_frame = ctk.CTkFrame(self, width=240, corner_radius=0); self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        ctk.CTkLabel(self.sidebar_frame, text="Módulos", font=("Arial", 22, "bold")).pack(pady=30)
        ctk.CTkButton(self.sidebar_frame, text="📍 Atualizador de CEP", height=40, font=("Arial", 14, "bold"), command=self.abrir_cep, fg_color="#1E88E5", hover_color="#1565C0").pack(pady=10, padx=20, fill="x")
        ctk.CTkButton(self.sidebar_frame, text="⚙️ Configurações", height=40, command=self.abrir_configuracoes, fg_color="#455A64").pack(pady=10, padx=20, fill="x", side="bottom")

        # Main Area
        self.main_frame = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0); self.main_frame.grid(row=0, column=1, sticky="nsew")

        # Carregar logo
        logo_path = r"C:\\Sistemas\\IA\\RenomeadorXML_ENVIA_EMAIL\\logo.png"
        if os.path.exists(logo_path):
            try:
                logo_img = Image.open(logo_path)
                self.logo_image = ctk.CTkImage(light_image=logo_img, dark_image=logo_img, size=(340, 140))
                self.logo_label = ctk.CTkLabel(self.main_frame, text="", image=self.logo_image)
                self.logo_label.pack(expand=True, pady=(80, 0))
            except: pass
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
        app_win.after(100, lambda: app_win.lift())

def centralizar_tela(tela, w, h):
    x = (tela.winfo_screenwidth() // 2) - (w // 2)
    y = (tela.winfo_screenheight() // 2) - (h // 2)
    tela.geometry(f"{w}x{h}+{x}+{y}")
"""

# Copiar ConfigWindow de 0CyN.py de forma bruta
config_window_code = """
class ConfigWindow(ctk.CTkToplevel):
    def __init__(self, parent, config, update_callback):
        super().__init__(parent)
        self.title("Configurações do Banco de Dados")
        centralizar_tela(self, 400, 500)
        self.transient(parent); self.grab_set() 
        self.update_callback = update_callback
        ctk.CTkLabel(self, text="⚙️ Configurar Acesso", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(20, 10))
        self.e_nome = self.criar_input("Nome do Usuário", config["nome_usuario"])
        self.e_servidor = self.criar_input("Servidor / Host", config["servidor"])
        self.e_banco = self.criar_input("Banco de Dados", config["banco"])
        self.e_user = self.criar_input("Usuário do Banco", config["usuario_bd"])
        self.e_senha = self.criar_input("Senha do Banco", config["senha_bd"], show="*")
        ctk.CTkButton(self, text="💾 Salvar", command=self.salvar, fg_color="#43A047").pack(pady=20)

    def criar_input(self, label, valor, show=None):
        ctk.CTkLabel(self, text=label, anchor="w").pack(fill="x", padx=30, pady=(10, 0))
        entry = ctk.CTkEntry(self, width=340, show=show); entry.pack(fill="x", padx=30, pady=(0, 5))
        if valor: entry.insert(0, valor)
        return entry

    def salvar(self):
        self.update_callback({"nome_usuario": self.e_nome.get(), "servidor": self.e_servidor.get(), "banco": self.e_banco.get(), "usuario_bd": self.e_user.get(), "senha_bd": self.e_senha.get()})
        self.destroy()
"""

# Junta tudo e grava
with open(path_out, 'w', encoding='utf-8') as f:
    f.write(full_latest[:full_latest.index('class App(ctk.CTk):')]) # Tudo até o App do 8IfQ (ToolTip, TabelaConfigWindow)
    f.write("\ndef centralizar_tela(tela, w, h):\n    x = (tela.winfo_screenwidth() // 2) - (w // 2)\n    y = (tela.winfo_screenheight() // 2) - (h // 2)\n    tela.geometry(f\"{w}x{h}+{x}+{y}\")\n\n")
    f.write(config_window_code)
    f.write("\n" + app_content)
    f.write("\n" + main_hub_code)
    f.write("\nif __name__ == '__main__':\n    app = MainHub()\n    app.mainloop()\n")

print("Backup completo e fusão realizada com sucesso!")
