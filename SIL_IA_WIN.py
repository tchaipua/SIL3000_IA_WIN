import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import pyodbc
import sys
import os
import time
import requests
import urllib.parse
from unidecode import unidecode
from tkinter import messagebox
from PIL import Image

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import mplcursors

class ToolTip(object):
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)

    def enter(self, event=None):
        x = y = 0
        try:
            x, y, cx, cy = self.widget.bbox("insert")
        except:
            pass
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tooltip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        tw.attributes("-topmost", True)
        label = tk.Label(tw, text=self.text, justify='left',
                         background="#ffffe0", relief='solid', borderwidth=1,
                         font=("Arial", "9", "normal"))
        label.pack(ipadx=2, ipady=1)

    def leave(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

class TabelaConfigWindow(ctk.CTkToplevel):
    def __init__(self, parent, config, update_callback):
        super().__init__(parent)
        self.grab_set()  # Trava a janela pai
        self.grab_set()  # Trava a janela pai
        self.title("Mapeamento da Tabela")
        
        # Centraliza a tela
        w, h = 450, 600
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")
        
        self.transient(parent)
        self.grab_set() 
        self.update_callback = update_callback
        
        # 1. Barra de Identificação de Tela (Absolute Bottom)
        self.bottom_bar = ctk.CTkFrame(self, fg_color="transparent")
        self.bottom_bar.pack(side="bottom", fill="x", padx=20, pady=(0, 10))
        
        self.frame_id = ctk.CTkFrame(self.bottom_bar, fg_color="transparent")
        self.frame_id.pack(side="right")
        
        self.lbl_tela_id = ctk.CTkLabel(self.frame_id, text="Tela: CFG_TABELA_CEP", font=ctk.CTkFont(size=11, weight="bold"), text_color="gray")
        self.lbl_tela_id.pack(side="left")
        
        self.btn_copy_id = ctk.CTkButton(self.frame_id, text="📋", width=20, height=20, fg_color="transparent", hover_color="#E0E0E0", text_color="black", command=lambda: self.copiar_id("CFG_TABELA_CEP"))
        self.btn_copy_id.pack(side="left", padx=5)
        ToolTip(self.btn_copy_id, "COPIAR NOME TELA")

        # 2. Barra de Botões (Logo acima da Identificação)
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(side="bottom", fill="x", padx=30, pady=(15, 5))
        
        # Botão Retornar à Esquerda
        self.btn_sair = ctk.CTkButton(self.buttons_frame, text="❌ Retornar", width=140, height=32, fg_color="#C62828", text_color="white", hover_color="#B12020", command=self.destroy)
        self.btn_sair.pack(side="left")

        # Botão Salvar à Direita
        self.btn_salvar = ctk.CTkButton(self.buttons_frame, text="💾 Salvar", width=140, height=32, command=self.salvar, fg_color="#43A047", hover_color="#2E7D32")
        self.btn_salvar.pack(side="right")

        # --- Corpo da Tela (Formulário) ---
        self.lbl_title = ctk.CTkLabel(self, text="⚙️ Colunas da Tabela de Clientes", font=ctk.CTkFont(size=18, weight="bold"))
        self.lbl_title.pack(pady=(20, 10))

        self.e_tabela = self.criar_input("Nome da Tabela", config["tabela"])
        self.e_id = self.criar_input("Coluna do ID/Código", config["col_id"])
        self.e_nome = self.criar_input("Coluna do Nome", config["col_nome"])
        self.e_cep = self.criar_input("Coluna do CEP", config["col_cep"])
        self.e_rua = self.criar_input("Coluna da Rua", config["col_rua"])
        self.e_log = self.criar_input("Coluna do Logradouro", config["col_logradouro"])
        self.e_bairro = self.criar_input("Coluna do Bairro", config["col_bairro"])
        self.e_uf = self.criar_input("Estado sempre (Valor Fixo)", config["col_uf"])

    def copiar_id(self, texto):
        self.clipboard_clear()
        self.clipboard_append(texto)
        self.update()

    def criar_input(self, label_text, valor):
        lbl = ctk.CTkLabel(self, text=label_text, anchor="w")
        lbl.pack(fill="x", padx=30, pady=(5, 0))
        entry = ctk.CTkEntry(self, width=340)
        entry.pack(fill="x", padx=30, pady=(0, 5))
        if valor: entry.insert(0, valor)
        return entry

    def salvar(self):
        novas_config = {
            "tabela": self.e_tabela.get(),
            "col_id": self.e_id.get(),
            "col_nome": self.e_nome.get(),
            "col_cep": self.e_cep.get(),
            "col_rua": self.e_rua.get(),
            "col_logradouro": self.e_log.get(),
            "col_bairro": self.e_bairro.get(),
            "col_uf": self.e_uf.get(),
        }
        self.update_callback(novas_config)
        self.destroy()


def centralizar_tela(tela, w, h):
    x = (tela.winfo_screenwidth() // 2) - (w // 2)
    y = (tela.winfo_screenheight() // 2) - (h // 2)
    tela.geometry(f"{w}x{h}+{x}+{y}")


class ConfigWindow(ctk.CTkToplevel):
    def __init__(self, parent, config, update_callback):
        super().__init__(parent)
        self.grab_set()  # Trava a janela pai
        self.grab_set()  # Trava a janela pai
        self.title("Configurações do Banco de Dados")
        centralizar_tela(self, 420, 560) # Aumentado para garantir espaço
        self.transient(parent); self.grab_set() 
        self.update_callback = update_callback

        # 1. Barra de Identificação de Tela (Absolute Bottom)
        self.bottom_bar = ctk.CTkFrame(self, fg_color="transparent")
        self.bottom_bar.pack(side="bottom", fill="x", padx=20, pady=(0, 10))
        
        self.frame_id = ctk.CTkFrame(self.bottom_bar, fg_color="transparent")
        self.frame_id.pack(side="right")
        
        self.lbl_tela_id = ctk.CTkLabel(self.frame_id, text="Tela: CFG_ACESSO", font=ctk.CTkFont(size=11, weight="bold"), text_color="gray")
        self.lbl_tela_id.pack(side="left")
        
        self.btn_copy_id = ctk.CTkButton(self.frame_id, text="📋", width=20, height=20, fg_color="transparent", hover_color="#E0E0E0", text_color="black", command=lambda: self.copiar_id("CFG_ACESSO"))
        self.btn_copy_id.pack(side="left", padx=5)
        ToolTip(self.btn_copy_id, "COPIAR NOME TELA")

        # 2. Barra de Botões (Logo acima da Identificação)
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(side="bottom", fill="x", padx=30, pady=(15, 5))
        
        # Botão Sair sem Salvar à Esquerda
        self.btn_sair = ctk.CTkButton(self.buttons_frame, text="❌ Sair sem Salvar", width=140, height=32, fg_color="#C62828", text_color="white", hover_color="#B12020", command=self.destroy)
        self.btn_sair.pack(side="left")

        # Botão Salvar à Direita
        self.btn_salvar = ctk.CTkButton(self.buttons_frame, text="💾 Salvar", width=140, height=32, command=self.salvar, fg_color="#43A047", hover_color="#2E7D32")
        self.btn_salvar.pack(side="right")

        # --- Corpo da Tela (Empacotado depois, para o topo) ---
        ctk.CTkLabel(self, text="⚙️ Configurar Acesso", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(20, 10))
        self.e_nome = self.criar_input("Nome do Usuário", config["nome_usuario"])
        self.e_servidor = self.criar_input("Servidor / Host", config["servidor"])
        self.e_banco = self.criar_input("Banco de Dados", config["banco"])
        self.e_user = self.criar_input("Usuário do Banco", config["usuario_bd"])
        self.e_senha = self.criar_input("Senha do Banco", config["senha_bd"], show="*")

    def copiar_id(self, texto):
        self.clipboard_clear()
        self.clipboard_append(texto)
        self.update()
        messagebox.showinfo("Sucesso", "NOME DA TELA COPIADO")

    def criar_input(self, label, valor, show=None):
        ctk.CTkLabel(self, text=label, anchor="w").pack(fill="x", padx=30, pady=(10, 0))
        entry = ctk.CTkEntry(self, width=340, show=show); entry.pack(fill="x", padx=30, pady=(0, 5))
        if valor: entry.insert(0, valor)
        return entry

    def salvar(self):
        self.update_callback({"nome_usuario": self.e_nome.get(), "servidor": self.e_servidor.get(), "banco": self.e_banco.get(), "usuario_bd": self.e_user.get(), "senha_bd": self.e_senha.get()})
        self.destroy()

class App(ctk.CTkToplevel):
    def __init__(self, parent, db_config):
        super().__init__(parent)
        self.grab_set()  # Trava a janela pai
        self.transient(parent)
        centralizar_tela(self, 1100, 700)

        self.title("Atualizador de CEPs - SQL Server")
        w, h = 1100, 700
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")
        
        # Tema claro obrigatório para o Atualizador também
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")
        self.configure(fg_color="#FFFFFF")

        # Configurações DB via CLI
        self.cfg_server = db_config["servidor"]
        self.cfg_db = db_config["banco"]
        self.cfg_user = db_config["usuario_bd"]
        self.cfg_pass = db_config["senha_bd"]

        # Configurações Iniciais da Tabela
        self.tabela_config = {
            "tabela": "crcli",
            "col_id": "crclicod",
            "col_nome": "crclides",
            "col_cep": "cmcepcod",
            "col_rua": "crcliend",
            "col_logradouro": "crclilog",
            "col_bairro": "crclibai",
            "col_uf": "SP"
        }

        self.mostrar_somente_invalidos = False
        self.ceps_invalidos_cache = set()
        self.lista_updates = []

        # Única Coluna no App
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # --- Top Frame (Menu Superior Expandido) ---
        self.top_frame = ctk.CTkFrame(self, height=70, corner_radius=10)
        self.top_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
        self.top_frame.grid_columnconfigure(6, weight=1) # Espaçador

        # Componentes do Top Frame
        self.btn_config = ctk.CTkButton(self.top_frame, text="⚙️ Mapear", width=100, fg_color="#455A64", hover_color="#37474F", command=self.abrir_config)
        self.btn_config.grid(row=0, column=0, padx=10, pady=15)

        self.search_entry = ctk.CTkEntry(self.top_frame, placeholder_text="Buscar cliente (Deixe vazio para TODOS)...", width=260)
        self.search_entry.grid(row=0, column=1, padx=10, pady=15)

        self.btn_listar = ctk.CTkButton(self.top_frame, text="🔍 Simular Atualização", fg_color="#1E88E5", hover_color="#1565C0", command=self.simular_click)
        self.btn_listar.grid(row=0, column=2, padx=10, pady=15)

        self.btn_filtrar = ctk.CTkButton(self.top_frame, text="👁️ Mostrar: TODOS", width=130, fg_color="#7B1FA2", hover_color="#4A148C", command=self.alternar_filtro_click)
        self.btn_filtrar.grid(row=0, column=3, padx=10, pady=15)

        self.btn_gravar = ctk.CTkButton(self.top_frame, text="💾 Gravar no BD", width=120, fg_color="#43A047", hover_color="#2E7D32", state="disabled", command=self.gravar_click)
        self.btn_gravar.grid(row=0, column=4, padx=10, pady=15)
        
        self.lbl_stats = ctk.CTkLabel(self.top_frame, text="Simulação pendente...", font=ctk.CTkFont(slant="italic"))
        self.lbl_stats.grid(row=0, column=5, padx=10)

        # --- Frames Interiores (Grid e Log) ---
        self.main_content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_content_frame.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="nsew")
        self.main_content_frame.grid_rowconfigure(0, weight=3)
        self.main_content_frame.grid_rowconfigure(1, weight=1)
        self.main_content_frame.grid_columnconfigure(0, weight=1)

        # Treeview
        self.table_frame = ctk.CTkFrame(self.main_content_frame, corner_radius=10)
        self.table_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 10))
        self.table_frame.grid_rowconfigure(0, weight=1)
        self.table_frame.grid_columnconfigure(0, weight=1)

        columns = ("id", "nome", "cidade", "cep_antigo", "cep_novo", "rua")
        style = ttk.Style()
        style.theme_use("default")
        # Ajuste de cores da grade (Treeview) para o tema claro
        style.configure("Treeview", background="#FFFFFF", foreground="black", rowheight=30, fieldbackground="#FFFFFF", borderwidth=0)
        style.map('Treeview', background=[('selected', '#1E88E5')])
        style.configure("Treeview.Heading", background="#E0E0E0", foreground="black", borderwidth=0, font=('Arial', 10, 'bold'))

        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings", selectmode="browse")
        self.tree.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.tree.tag_configure('correto', background='#2E7D32', foreground='white') 
        self.tree.tag_configure('invalido', background='#C62828', foreground='white') 
        self.tree.tag_configure('desconhecido', background='#EF6C00', foreground='white') 

        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("cidade", text="Cidade")
        self.tree.heading("cep_antigo", text="CEP Antigo")
        self.tree.heading("cep_novo", text="CEP Novo")
        self.tree.heading("rua", text="Rua")

        self.tree.column("id", width=60, anchor="center")
        self.tree.column("nome", width=180)
        self.tree.column("cidade", width=120)
        self.tree.column("cep_antigo", width=90, anchor="center")
        self.tree.column("cep_novo", width=100, anchor="center")
        self.tree.column("rua", width=250)

        scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns", pady=10)

        # Log
        self.log_frame = ctk.CTkFrame(self.main_content_frame, corner_radius=10)
        self.log_frame.grid(row=1, column=0, sticky="nsew")
        self.log_frame.grid_rowconfigure(0, weight=1)
        self.log_frame.grid_columnconfigure(0, weight=1)

        self.log_text = ctk.CTkTextbox(self.log_frame, wrap="word", font=('Consolas', 10))
        self.log_text.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.log_text.configure(state="disabled")

        # --- Barra de Status Inferior ---
        self.bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.bottom_frame.grid(row=2, column=0, padx=20, pady=(0, 10), sticky="ew")
        
        # Botão de retorno único
        try:
            img_fechar_pil = Image.open(os.path.join(os.path.dirname(__file__), "btn_fechar.png"))
            self.img_fechar_at = ctk.CTkImage(img_fechar_pil, size=(22, 22))
        except:
            self.img_fechar_at = None

        self.btn_sair = ctk.CTkButton(
            self.bottom_frame, 
            text="Fechar Tela", 
            image=self.img_fechar_at, 
            compound="left", 
            width=130, 
            height=32, 
            fg_color="transparent", 
            text_color="black", 
            hover_color="#E0E0E0", 
            border_width=2,
            border_color="black",
            command=self.destroy
        )
        self.btn_sair.pack(side="left", padx=(0, 15))

        self.lbl_status = ctk.CTkLabel(self.bottom_frame, text="💡 Status: Pronto. Preencha a Busca e clique em Simular.", font=ctk.CTkFont(size=12))
        self.lbl_status.pack(side="left")

        self.frame_id = ctk.CTkFrame(self.bottom_frame, fg_color="transparent")
        self.frame_id.pack(side="right")
        self.lbl_tela_id = ctk.CTkLabel(self.frame_id, text="Tela: ATUALIZA_CEP", font=ctk.CTkFont(size=11, weight="bold"), text_color="gray")
        self.lbl_tela_id.pack(side="left")
        self.btn_copy_id = ctk.CTkButton(self.frame_id, text="📋", width=20, height=20, fg_color="transparent", hover_color="#E0E0E0", text_color="black", command=lambda: self.copiar_id("ATUALIZA_CEP"))
        self.btn_copy_id.pack(side="left", padx=5)
        ToolTip(self.btn_copy_id, "COPIAR NOME TELA")

    def abrir_config(self):
        TabelaConfigWindow(self, self.tabela_config, self.salvar_config)

    def salvar_config(self, config):
        self.tabela_config = config
        self.log("⚙️ Mapeamento de Tabela atualizado!")

    def copiar_id(self, texto):
        self.clipboard_clear()
        self.clipboard_append(texto)
        self.update()
        messagebox.showinfo("Sucesso", "NOME DA TELA COPIADO")

    def log(self, mensagem):
        self.log_text.configure(state="normal")
        self.log_text.insert(tk.END, mensagem + "\n")
        self.log_text.see(tk.END)
        self.log_text.configure(state="disabled")
        self.update()

    def limpar_texto(self, texto):
        if not texto: return ""
        return unidecode(str(texto)).strip().upper()

    def buscar_cep_por_endereco(self, uf, cidade, logradouro):
        uf = uf.strip().upper()
        cidade = cidade.strip()
        logradouro = logradouro.strip()
        if len(logradouro) < 3: return []
        cidade_encoded = urllib.parse.quote(cidade)
        logradouro_encoded = urllib.parse.quote(logradouro)
        url_viacep = f"https://viacep.com.br/ws/{uf}/{cidade_encoded}/{logradouro_encoded}/json/"
        try:
            response = requests.get(url_viacep, timeout=3)
            if response.status_code == 200:
                dados = response.json()
                if isinstance(dados, list) and len(dados) > 0:
                    return dados
        except: pass
        return []

    def simular_click(self):
        server = self.cfg_server
        database = self.cfg_db
        username = self.cfg_user
        password = self.cfg_pass

        c = self.tabela_config
        tabela = c["tabela"]
        c_id = c["col_id"]
        c_nome = c["col_nome"]
        c_cep = c["col_cep"]
        c_rua = c["col_rua"]
        c_logradouro = c["col_logradouro"]
        c_bairro = c["col_bairro"]
        valor_uf = c["col_uf"]
        
        busca = self.search_entry.get().strip()

        for item in self.tree.get_children(): self.tree.delete(item)

        self.log_text.configure(state="normal")
        self.log_text.delete("1.0", tk.END)
        self.log_text.configure(state="disabled")

        self.log("🚀 Iniciando Simulação...")
        self.lbl_status.configure(text="⏳ Conectando ao SQL Server...")
        self.update()

        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"
        try:
            conn = pyodbc.connect(conn_str)
        except:
            try:
                conn_str_alt = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"
                conn = pyodbc.connect(conn_str_alt)
            except Exception as e:
                messagebox.showerror("Erro de Conexão", "Não foi possível conectar ao Banco de Dados com as credenciais fornecidas.\n\nVerifique os dados de acesso (Servidor, Banco, Usuário ou Senha) nas configurações e tente novamente.")
                # Abre a tela ConfigWindow (CFG_ACESSO)
                ConfigWindow(self, self.config, lambda c: [setattr(self, 'config', c)])
                return

        cursor = conn.cursor()

        # Condição de Busca (WHERE)
        where_clause = ""
        if busca:
            where_clause = f" WHERE {c_nome} LIKE '%{busca}%' OR {c_id} LIKE '%{busca}%'"

        query = f"""
            SELECT 
                c.{c_id}, 
                c.{c_nome}, 
                c.{c_cep}, 
                c.{c_rua}, 
                c.{c_bairro}, 
                c.{c_logradouro},
                m.CMUFCod as UF_Dinamica,
                m.CMCEPDes as Cidade_Dinamica,  
                c.CMCEPCod  
            FROM {tabela} c
            LEFT JOIN CMCEP m ON c.CMCEPCod = m.CMCEPCod
            {where_clause}
        """
        
        try:
            cursor.execute(query)
            clientes = cursor.fetchall()
        except Exception as e:
             messagebox.showerror("Erro de Query", f"Não foi possível ler a tabela '{tabela}' com as colunas definidas.\n\nDetalhe: {e}")
             cursor.close()
             conn.close()
             return
            
        self.log(f"📊 {len(clientes)} clientes filtrados no banco.")
        
        if len(clientes) == 0:
            self.lbl_status.configure(text=f"Nenhum cliente encontrado com a busca '{busca}'")
            return

        invalidos = 0
        total_analisado = 0
        self.lista_updates = [] 

        for cli in clientes:
            total_analisado += 1
            time.sleep(0.05) 
            self.lbl_status.configure(text=f"📊 Analisando Cliente {total_analisado} de {len(clientes)} ...")

            cod = str(cli[0])
            nome = str(cli[1])
            campo_cep = str(cli[2]).strip() if cli[2] else ""
            campo_logradouro = str(cli[5]).strip() if cli[5] else "" 
            cep_atual = (campo_cep + campo_logradouro).replace("-", "").replace(".", "").strip()
            # Máscara xxxxx-xxx para visualização na Treeview
            cep_antigo_formatado = f"{cep_atual[:5]}-{cep_atual[5:]}" if len(cep_atual) == 8 else cep_atual
            rua_orig = str(cli[3]) if cli[3] else "" 
            bairro_orig = str(cli[4]) if cli[4] else ""
            
            valor_uf = str(cli[6]).strip() if cli[6] else "SP" 
            cidade_busca = str(cli[7]).strip() if cli[7] else "Ipuã"
            chave_cidade = cli[8] 

            self.log(f"🔎 Cliente {cod} ({nome}) -> CEP Atual: '{cep_atual}'")

            if cep_atual in self.ceps_invalidos_cache:
                 cep_valido = False
            else:
                cep_valido = False
                if len(cep_atual) == 8:
                    try:
                        r_cep = requests.get(f"https://viacep.com.br/ws/{cep_atual}/json/", timeout=2)
                        if r_cep.status_code == 200 and "erro" not in r_cep.text:
                            cep_valido = True 
                        else:
                             self.ceps_invalidos_cache.add(cep_atual)
                    except: pass

            if cep_valido:
                if not self.mostrar_somente_invalidos:
                    self.tree.insert("", tk.END, values=(cod, nome, cidade_busca, cep_antigo_formatado, "✓ OK", rua_orig), tags=('correto',))
                continue 

            if campo_logradouro.isdigit() or campo_logradouro == "000":
                 logradouro_completo = rua_orig.strip()
            else:
                 logradouro_completo = f"{campo_logradouro} {rua_orig}".strip() 
            
            if not logradouro_completo.replace("None", "").strip():
                continue

            resultados = self.buscar_cep_por_endereco(valor_uf, cidade_busca, logradouro_completo)
            if not resultados:
                resultados = self.buscar_cep_por_endereco(valor_uf, cidade_busca, rua_orig)

            if resultados:
                cep_encontrado = None
                bairro_local_limpo = self.limpar_texto(bairro_orig)
                for res in resultados:
                    if self.limpar_texto(res.get("bairro", "")) == bairro_local_limpo:
                        cep_encontrado = res.get("cep")
                        res_rua = res.get("logradouro", logradouro_completo)
                        res_bairro = res.get("bairro", bairro_orig)
                        break

                if not cep_encontrado and len(resultados) == 1:
                    cep_encontrado = resultados[0].get("cep")
                    res_rua = resultados[0].get("logradouro", logradouro_completo)
                    res_bairro = resultados[0].get("bairro", bairro_orig)

                if cep_encontrado:
                     invalidos += 1
                     self.tree.insert("", tk.END, values=(cod, nome, cidade_busca, cep_antigo_formatado, cep_encontrado, logradouro_completo), tags=('invalido',))
                     self.tree.see(self.tree.get_children()[-1])
                     self.update() 
                     
                     self.lista_updates.append({
                         "cod": cod,
                         "cep": cep_encontrado.replace("-", ""),
                         "chave_cidade": chave_cidade, 
                         "nome_cidade": cidade_busca,
                         "nome_uf": valor_uf,
                         "rua": res_rua,
                         "bairro": res_bairro
                     })
                else:
                    if not self.mostrar_somente_invalidos:
                         self.tree.insert("", tk.END, values=(cod, nome, cidade_busca, cep_antigo_formatado, "⚠️ Sem CEP", logradouro_completo), tags=('desconhecido',))

        cursor.close()
        conn.close()

        self.btn_gravar.configure(state="normal" if self.lista_updates else "disabled")
        self.lbl_stats.configure(text=f"✅ {invalidos} Clientes precisam de correção.")
        self.lbl_status.configure(text=f"💡 Verifique a lista. {invalidos} CEPs para atualizar. Clique em 'Gravar' se concordar.")

    def alternar_filtro_click(self):
        self.mostrar_somente_invalidos = not self.mostrar_somente_invalidos
        if self.mostrar_somente_invalidos:
            self.btn_filtrar.configure(text="👁️ Mostrar: SÓ ERROS", fg_color="#C62828")
            for item in self.tree.get_children():
                tags = self.tree.item(item, "tags")
                if 'correto' in tags or 'desconhecido' in tags:
                    self.tree.detach(item) 
        else:
            self.btn_filtrar.configure(text="👁️ Mostrar: TODOS", fg_color="#7B1FA2")
            messagebox.showinfo("Filtro", "Para voltar a ver os corretos na busca atual, clique em 'Simular Atualização' novamente.")

    def gravar_click(self):
        if not hasattr(self, 'lista_updates') or not self.lista_updates:
            return

        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.cfg_server};DATABASE={self.cfg_db};UID={self.cfg_user};PWD={self.cfg_pass};"
        c = self.tabela_config
        
        try:
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()
            
            sucessos_cliente = 0
            insercoes_cmcep = 0
            insercoes_cmcepl = 0

            for up in self.lista_updates:
                cod_cliente = up["cod"]
                cep_limpo = up["cep"] 

                cm_cep_cod = int(cep_limpo[:5]) 
                cm_cep_log = str(cep_limpo[5:]).strip() 

                nome_cidade = up["nome_cidade"]
                nome_uf = up["nome_uf"]
                nome_rua = up["rua"]
                nome_bairro = up["bairro"]

                cursor.execute("SELECT CMCEPCod FROM CMCEP WHERE CMCEPCod = ?", cm_cep_cod)
                if not cursor.fetchone():
                    cursor.execute("""
                        INSERT INTO CMCEP (CMCEPCod, CMUFCod, CMCEPDes, CMCEPCUsu, CMCEPCHor, CMCEPCPrg)
                        VALUES (?, ?, ?, 'IA', '00:00:00', 'UPDATE')
                    """, cm_cep_cod, nome_uf, nome_cidade)
                    insercoes_cmcep += 1
                
                cursor.execute("SELECT CmCepLCod FROM cmcepl WHERE CmCepLCod = ? AND CmCepLLog = ?", cm_cep_cod, cm_cep_log)
                if not cursor.fetchone():
                     cursor.execute("""
                        INSERT INTO cmcepl (CmCepLCod, CmCepLLog, CmCepLDes, CmCepLBai, CmCepLCid, CmCepLUf, CmCepLPat)
                        VALUES (?, ?, ?, ?, ?, ?, '')
                     """, cm_cep_cod, cm_cep_log, nome_rua, nome_bairro, nome_cidade, nome_uf)
                     insercoes_cmcepl += 1

                cursor.execute(f"UPDATE {c['tabela']} SET {c['col_cep']} = ?, {c['col_logradouro']} = ? WHERE {c['col_id']} = ?", cm_cep_cod, cm_cep_log, cod_cliente)
                sucessos_cliente += 1

            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Sucesso", f"📊 Atualização Concluída!\n• {sucessos_cliente} Clientes Atualizados ✅\n• {insercoes_cmcep} Cidades (CMCEP) 🏙️\n• {insercoes_cmcepl} Ruas (cmcepl) 🛣️")
            self.lbl_status.configure(text="✅ Tudo atualizado! Simule novamente para conferir.")
            self.btn_gravar.configure(state="disabled")
            for item in self.tree.get_children(): self.tree.delete(item)

        except Exception as e:
            messagebox.showerror("Erro SQL", f"Erro ao gravar:\n{e}")


class AnaliseVendasWindow(ctk.CTkToplevel):
    def __init__(self, parent, config):
        super().__init__(parent)
        self.grab_set()  # Trava a janela pai
        self.title("Análise de Vendas")
        self.config = config
        
        # Centraliza
        w, h = 900, 600
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")
        
        self.transient(parent)
        
        # 1. Barra de Identificação de Tela
        self.bottom_bar = ctk.CTkFrame(self, fg_color="transparent")
        self.bottom_bar.pack(side="bottom", fill="x", padx=20, pady=(0, 10))
        
        self.frame_id = ctk.CTkFrame(self.bottom_bar, fg_color="transparent")
        self.frame_id.pack(side="right")
        self.lbl_tela_id = ctk.CTkLabel(self.frame_id, text="Tela: ANALISE_VENDAS", font=ctk.CTkFont(size=11, weight="bold"), text_color="gray")
        self.lbl_tela_id.pack(side="left")
        self.btn_copy_id = ctk.CTkButton(self.frame_id, text="📋", width=20, height=20, fg_color="transparent", hover_color="#E0E0E0", text_color="black", command=lambda: self.copiar_id("ANALISE_VENDAS"))
        self.btn_copy_id.pack(side="left", padx=5)
        ToolTip(self.btn_copy_id, "COPIAR NOME TELA")

        # 2. Barra de Botões (Rodapé)
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(side="bottom", fill="x", padx=30, pady=(15, 5))
        
        try:
            img_fechar_pil = Image.open(os.path.join(os.path.dirname(__file__), "btn_fechar.png"))
            self.img_fechar = ctk.CTkImage(img_fechar_pil, size=(22, 22))
        except:
            self.img_fechar = None

        self.btn_sair = ctk.CTkButton(
            self.buttons_frame, 
            text="Fechar Tela", 
            image=self.img_fechar, 
            compound="left", 
            width=140, 
            height=32, 
            fg_color="transparent", 
            text_color="black", 
            hover_color="#E0E0E0", 
            border_width=2,
            border_color="black",
            command=self.destroy
        )
        self.btn_sair.pack(side="left")

        # Exportações
        self.btn_export_pdf = ctk.CTkButton(self.buttons_frame, text="📄 Exportar PDF", width=140, height=32, fg_color="#E53935", hover_color="#B71C1C", command=self.exportar_pdf)
        self.btn_export_pdf.pack(side="right", padx=5)
        
        self.btn_export_excel = ctk.CTkButton(self.buttons_frame, text="📊 Exportar Excel", width=140, height=32, fg_color="#43A047", hover_color="#2E7D32", command=self.exportar_excel)
        self.btn_export_excel.pack(side="right", padx=5)

        # 3. Topo: Controles
        # 3. Topo: Controles
        self.top_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.top_frame.pack(side="top", fill="x", padx=20, pady=10)
        
        # Sub-container interno para margens
        self.top_grid_frame = ctk.CTkFrame(self.top_frame)
        self.top_grid_frame.pack(side="top", fill="x", padx=10, pady=10)
        self.top_grid_frame.grid_columnconfigure((1, 3, 5), weight=1)

        # LINHA 0
        ctk.CTkLabel(self.top_grid_frame, text="Ano:").grid(row=0, column=0, padx=(15, 5), pady=8, sticky="e")
        self.combo_ano = ctk.CTkComboBox(self.top_grid_frame, values=["Todos"], width=100)
        self.combo_ano.grid(row=0, column=1, padx=5, pady=8, sticky="ew")
        self.combo_ano.set("Todos")

        ctk.CTkLabel(self.top_grid_frame, text="Mês:").grid(row=0, column=2, padx=(15, 5), pady=8, sticky="e")
        self.meses = ["Todos", "01 - Janeiro", "02 - Fevereiro", "03 - Março", "04 - Abril", "05 - Maio", "06 - Junho", "07 - Julho", "08 - Agosto", "09 - Setembro", "10 - Outubro", "11 - Novembro", "12 - Dezembro"]
        self.combo_mes = ctk.CTkComboBox(self.top_grid_frame, values=self.meses, width=140)
        self.combo_mes.grid(row=0, column=3, padx=5, pady=8, sticky="ew")
        self.combo_mes.set("Todos")

        ctk.CTkLabel(self.top_grid_frame, text="Visão Especial:").grid(row=0, column=4, padx=(15, 5), pady=8, sticky="e")
        self.combo_visao = ctk.CTkComboBox(self.top_grid_frame, values=["Padrão", "Horário", "Dias da Semana"], width=190)
        self.combo_visao.grid(row=0, column=5, padx=5, pady=8, sticky="ew")
        self.combo_visao.set("Padrão")

        # LINHA 1 - Botão Atualizar Gráficos alinhado abaixo de Ano
        self.btn_gerar = ctk.CTkButton(self.top_grid_frame, text="Atualizar Gráfico", command=self.gerar_grafico, fg_color="#1E88E5", hover_color="#1565C0", width=130)
        self.btn_gerar.grid(row=1, column=1, padx=5, pady=8, sticky="ew")

        ctk.CTkLabel(self.top_grid_frame, text="Métrica:").grid(row=1, column=2, padx=(15, 5), pady=8, sticky="e")
        self.combo_metrica = ctk.CTkComboBox(self.top_grid_frame, values=["Quantidade de Vendas", "Valor Total (R$)"], width=200)
        self.combo_metrica.grid(row=1, column=3, padx=5, pady=8, sticky="ew")
        self.combo_metrica.set("Valor Total (R$)")

        self.chart_frame = ctk.CTkFrame(self, fg_color="white")
        self.chart_frame.pack(side="top", fill="both", expand=True, padx=20, pady=(0, 10))
        
        self.fig = Figure(figsize=(8, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.chart_frame)
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        
        self.df_raw = None
        self.df_grouped = None
        self.after(100, self.carregar_dados)

    def copiar_id(self, texto):
        self.clipboard_clear()
        self.clipboard_append(texto)
        self.update()
        messagebox.showinfo("Sucesso", "NOME DA TELA COPIADO")

    def carregar_dados(self):
        try:
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config['servidor']};DATABASE={self.config['banco']};UID={self.config['usuario_bd']};PWD={self.config['senha_bd']}"
            conn = pyodbc.connect(conn_str)
            query = "SELECT CRMovDta, CRMov2CHor, CRMov2VlrO FROM crmov2 WHERE CRMovDta IS NOT NULL"
            self.df_raw = pd.read_sql(query, conn)
            conn.close()
            
            # Limpeza de dados básica
            self.df_raw['CRMovDta'] = pd.to_datetime(self.df_raw['CRMovDta'], errors='coerce')
            self.df_raw['CRMov2VlrO'] = pd.to_numeric(self.df_raw['CRMov2VlrO'], errors='coerce').fillna(0)
            
            # Extrair atributos principais e remover anos inválidos como 9999
            self.df_raw['Ano'] = self.df_raw['CRMovDta'].dt.year.astype('Int64')
            self.df_raw = self.df_raw[self.df_raw['Ano'] < 9999]
            
            self.df_raw['Mes_Int'] = self.df_raw['CRMovDta'].dt.month.astype('Int64')
            
            meses_dict = {1:"01 - Janeiro", 2:"02 - Fevereiro", 3:"03 - Março", 4:"04 - Abril", 5:"05 - Maio", 6:"06 - Junho", 7:"07 - Julho", 8:"08 - Agosto", 9:"09 - Setembro", 10:"10 - Outubro", 11:"11 - Novembro", 12:"12 - Dezembro"}
            self.df_raw['Mes_Extenso'] = self.df_raw['Mes_Int'].map(meses_dict)
            self.df_raw['Dia'] = self.df_raw['CRMovDta'].dt.day.astype('Int64')
            
            # Dias da Semana
            dias_dict = {0:"Segunda-feira", 1:"Terça-feira", 2:"Quarta-feira", 3:"Quinta-feira", 4:"Sexta-feira", 5:"Sábado", 6:"Domingo"}
            self.df_raw['Dia_Semana'] = self.df_raw['CRMovDta'].dt.dayofweek.map(dias_dict)
            
            dias_ordem = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
            self.df_raw['Dia_Semana'] = pd.Categorical(self.df_raw['Dia_Semana'], categories=dias_ordem, ordered=True)
            
            # Hora (Tratando strings variadas)
            def extrair_hora(h):
                try: 
                    return int(str(h).replace(':', '')[:2])
                except: 
                    return None
            
            self.df_raw['Hora'] = self.df_raw['CRMov2CHor'].apply(extrair_hora)
            
            def extrair_faixa(h):
                try:
                    hora_int = int(str(h).replace(':', '')[:2])
                    if hora_int >= 24: return None
                    lim = (hora_int // 2) * 2
                    return f"{lim:02d}h às {lim+2:02d}h"
                except: return None
            
            self.df_raw['Faixa_Horario'] = self.df_raw['CRMov2CHor'].apply(extrair_faixa)
            
            # Preenche o ComboBox de Ano com os anos encontrados no banco (mais recente primeiro)
            anos_unicos = sorted(self.df_raw['Ano'].dropna().unique().tolist(), reverse=True)
            self.combo_ano.configure(values=["Todos"] + [str(a) for a in anos_unicos])
            
            self.gerar_grafico()
            
        except Exception as e:
            messagebox.showerror("Erro de Conexão", "Não foi possível conectar ao Banco de Dados com as credenciais fornecidas.\n\nVerifique os dados de acesso (Servidor, Banco, Usuário ou Senha) nas configurações e tente novamente.")
            # Abre a tela ConfigWindow (CFG_ACESSO) de forma autônoma
            ConfigWindow(self, self.config, lambda c: [setattr(self, 'config', c), self.carregar_dados()])

    def gerar_grafico(self):
        if self.df_raw is None or self.df_raw.empty:
            return
            
        ano_sel = self.combo_ano.get()
        mes_sel = self.combo_mes.get()
        visao = self.combo_visao.get()
        metrica = self.combo_metrica.get()
        
        df_valid = self.df_raw.copy()
        
        # Filtros Dinâmicos
        if ano_sel != "Todos":
            df_valid = df_valid[df_valid['Ano'] == int(ano_sel)]
        if mes_sel != "Todos":
            df_valid = df_valid[df_valid['Mes_Extenso'] == mes_sel]
            
        if df_valid.empty:
            self.ax.clear()
            self.ax.set_title("Nenhum dado encontrado para os filtros selecionados.")
            self.canvas.draw()
            return

        # Agrupamento base
        if visao == "Horário":
            grouper = 'Hora'
            agrupamento_str = "Faixa de Horário"
        elif visao == "Dias da Semana":
            grouper = 'Dia_Semana'
            agrupamento_str = "Dia da Semana"
        elif visao == "Dia da Semana + Horário":
            grouper = 'Dia_Horario'
            agrupamento_str = "Dia da Semana + Horário"
        else:
            if ano_sel != "Todos" and mes_sel == "Todos":
                grouper = 'Mes_Extenso'
                agrupamento_str = "Mês"
            elif ano_sel == "Todos" and mes_sel != "Todos":
                grouper = 'Ano'
                agrupamento_str = "Ano"
            elif ano_sel != "Todos" and mes_sel != "Todos":
                grouper = 'Dia'
                agrupamento_str = "Dia"
            else:
                grouper = 'Ano'
                agrupamento_str = "Ano"
            
        # Calcula dados
        if grouper not in df_valid.columns: return
        df_valid = df_valid.dropna(subset=[grouper])
        
        self.df_grouped = df_valid.groupby(grouper).agg(
            Qtd=('CRMovDta', 'size'),
            ValorTotal=('CRMov2VlrO', 'sum')
        ).reset_index()
        
        # Cria rótulo combinado para visão duo list
        if isinstance(grouper, list):
            self.df_grouped['Dia_Horario'] = self.df_grouped['Dia_Semana'].astype(str) + " - " + self.df_grouped['Hora'].map(lambda x: f"{int(x):02d}h")
            grouper_plot = 'Dia_Horario'
        else:
            grouper_plot = grouper
        
        if metrica == "Quantidade de Vendas":
            self.df_grouped['Valor'] = self.df_grouped['Qtd']
            ylabel = "Qtd. de Vendas"
        else:
            self.df_grouped['Valor'] = self.df_grouped['ValorTotal']
            ylabel = "Valor Total (R$)"
            
        # Pular se nulo
        if self.df_grouped.empty: return
        
        # Ordenar eixo X logicamente
        if grouper in ['Mes_Extenso', 'Dia_Semana', 'Dia_Horario']:
            self.df_grouped = self.df_grouped.sort_values(by=grouper)
        elif grouper == 'Ano':
            self.df_grouped = self.df_grouped.sort_values(by=grouper, ascending=False)
        else:
            self.df_grouped = self.df_grouped.sort_values(by=grouper)
        
        # Formata x para exibição (pandas period Mês não plota nativamente bem se for object string sem conversao)
        self.df_grouped[grouper_plot] = self.df_grouped[grouper_plot].astype(str)
        
        # Plot
        self.ax.clear()
        x_vals = self.df_grouped[grouper_plot]
        y_vals = self.df_grouped['Valor']
        
        bars = self.ax.bar(x_vals, y_vals, color='#1E88E5', edgecolor='#1565C0')
        self.ax.set_title(f"{metrica} por {agrupamento_str}")
        self.ax.set_ylabel(ylabel)
        self.ax.set_xlabel(agrupamento_str)
        
        # Criação do Tooltip Interativo ao passar o mouse
        cursor = mplcursors.cursor(bars, hover=True)
        
        @cursor.connect("add")
        def on_add(sel):
            idx = sel.index
            label_x = self.df_grouped.iloc[idx][grouper_plot]
            qtd = self.df_grouped.iloc[idx]['Qtd']
            valor = self.df_grouped.iloc[idx]['ValorTotal']
            texto = f"{label_x}\n----------------\nVendas: {qtd}\nTotal: R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            sel.annotation.set_text(texto)
            sel.annotation.get_bbox_patch().set(boxstyle="round,pad=0.5", fc="white", alpha=0.9, ec="#1E88E5")
        
        # Formatação
        if len(x_vals) > 10:
            self.ax.tick_params(axis='x', rotation=45)
        else:
            self.ax.tick_params(axis='x', rotation=0)
            
        if "Valor" in metrica:
            self.ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: f"R$ {x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')))
            
        self.fig.tight_layout()
        self.canvas.draw()
        
    def exportar_excel(self):
        if self.df_grouped is None or self.df_grouped.empty:
            messagebox.showwarning("Aviso", "Nenhum dado gerado para exportar.")
            return
        
        filepath = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")], title="Salvar Excel", initialfile="Analise_Vendas.xlsx")
        if filepath:
            try:
                self.df_grouped.to_excel(filepath, index=False)
                messagebox.showinfo("Sucesso", f"Salvo em: {filepath}")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    def exportar_pdf(self):
        if self.df_grouped is None or self.df_grouped.empty:
            messagebox.showwarning("Aviso", "Nenhum gráfico gerado para exportar.")
            return
        
        filepath = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Salvar PDF", initialfile="Grafico_Vendas.pdf")
        if filepath:
            try:
                self.fig.savefig(filepath, format="pdf", bbox_inches="tight")
                messagebox.showinfo("Sucesso", f"Gráfico salvo em: {filepath}")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

class MainHub(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SIL_IA_WIN")
        self.geometry("1000x650")
        self.after(100, lambda: self.state("zoomed"))
        ctk.set_appearance_mode("Light")
        
        self.config = {"nome_usuario": "Operador", "servidor": r"servidor\sqlexpress", "banco": "msinfor", "usuario_bd": "sa", "senha_bd": "Mabelu2011"}
        self.grid_rowconfigure(0, weight=1); self.grid_columnconfigure(1, weight=1)

        # Sidebar (Faixa Azul Escura conforme imagem)
        self.sidebar_frame = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color="#0D47A1") # Azul Marinho Rico
        self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        
        # Frame centralizado no topo da barra
        self.sb_header = ctk.CTkFrame(self.sidebar_frame, fg_color="transparent")
        self.sb_header.pack(fill="x", padx=15, pady=(40, 20))
        
        logo_path = os.path.join(os.path.dirname(__file__), "logo_msinfor.jpg")
        if os.path.exists(logo_path):
            try:
                logo_img = Image.open(logo_path)
                # Logotipo maior
                self.logo_image = ctk.CTkImage(light_image=logo_img, dark_image=logo_img, size=(170, 170))
                self.logo_label = ctk.CTkLabel(self.sb_header, text="", image=self.logo_image)
                self.logo_label.pack(anchor="center") # Centralizado
            except Exception as e: pass

        ctk.CTkFrame(self.sidebar_frame, height=2, fg_color="#1565C0").pack(fill="x", padx=15, pady=(5, 15))

        # Botão Sair do Sistema na Sidebar (Embaixo de tudo)
        self.btn_sair = ctk.CTkButton(self.sidebar_frame, text="❌ Sair do Sistema", font=("Arial", 14, "bold"), command=self.destroy, fg_color="#C62828", hover_color="#B12020")
        self.btn_sair.pack(side="bottom", fill="x", padx=15, pady=(0, 20)) # pady=(top, bottom)

        # Botão Configurações na Sidebar (Acima do Sair)
        self.btn_config = ctk.CTkButton(self.sidebar_frame, text="⚙️ Configurações", font=("Arial", 14, "bold"), command=self.abrir_configuracoes, fg_color="#455A64", hover_color="#37474F")
        self.btn_config.pack(side="bottom", fill="x", padx=15, pady=(20, 10))

        # Main Area
        self.main_frame = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        # Frame para os módulos (Canto Superior Esquerdo)
        self.modules_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.modules_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Todos os botões do menu terão a mesma largura base (estendendo-se horizontalmente conforme a grade)
        btn_width = 300
        
        # Botão alinhado no topo esquerdo
        self.btn_cep = ctk.CTkButton(self.modules_frame, text="📍 Atualizador de CEP", width=btn_width, height=45, font=("Arial", 14, "bold"), command=self.abrir_cep, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_cep.grid(row=0, column=0, sticky="ew")

        # Botão Análise (sem funcionalidade programada ainda)
        self.btn_analise = ctk.CTkButton(self.modules_frame, text="📊 Analise vendas por dia/horário", width=btn_width, height=45, font=("Arial", 14, "bold"), command=self.abrir_analise, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_analise.grid(row=1, column=0, pady=(15, 0), sticky="ew")

        # Botão Análise por Produto (Somente botão por enquanto)
        self.btn_analise_prod = ctk.CTkButton(self.modules_frame, text="🛒 Analise vendas por produto", width=btn_width, height=45, font=("Arial", 14, "bold"), command=self.abrir_analise_produto, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_analise_prod.grid(row=2, column=0, pady=(15, 0), sticky="ew")

        # Rodapé
        self.footer_frame = ctk.CTkFrame(self, height=35, fg_color="#1E1E1E")
        self.footer_frame.grid(row=1, column=1, sticky="ew")
        
        # ID da Tela no Canto Direito
        self.frame_id = ctk.CTkFrame(self.footer_frame, fg_color="transparent")
        self.frame_id.pack(side="right", padx=15)
        
        self.lbl_tela_id = ctk.CTkLabel(self.frame_id, text="Tela: PRINCIPAL", font=ctk.CTkFont(size=11, weight="bold"), text_color="white")
        self.lbl_tela_id.pack(side="left")
        
        self.btn_copy_id = ctk.CTkButton(self.frame_id, text="📋", width=20, height=20, fg_color="transparent", hover_color="#333333", text_color="white", command=lambda: self.copiar_id("PRINCIPAL"))
        self.btn_copy_id.pack(side="left", padx=5)
        ToolTip(self.btn_copy_id, "COPIAR NOME TELA")

        self.lbl_footer = ctk.CTkLabel(self.footer_frame, text="", text_color="white", font=("Arial", 11))
        self.lbl_footer.pack(side="left", padx=15, expand=True)
        self.atualizar_rodape()
        self.after(200, self.testar_conexao_banco)

    def testar_conexao_banco(self):
        import pyodbc
        from tkinter import messagebox
        
        server = self.config.get("servidor")
        database = self.config.get("banco")
        username = self.config.get("usuario_bd")
        password = self.config.get("senha_bd")
        
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"
        
        try:
            conn = pyodbc.connect(conn_str)
            conn.close()
        except:
            try:
                # Fallback de Driver legado
                conn_str_alt = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"
                conn = pyodbc.connect(conn_str_alt)
                conn.close()
            except Exception as e:
                # Alerta Amigável
                messagebox.showerror("Erro de Conexão", "Não foi possível conectar ao Banco de Dados com as credenciais fornecidas.\n\nPor favor, verifique os dados de acesso (Servidor, Banco, Usuário ou Senha) nas Configurações.")
                # Abre ConfigWindow (CFG_ACESSO) de forma automática
                self.abrir_configuracoes()

    def copiar_id(self, texto):
         self.clipboard_clear()
         self.clipboard_append(texto)
         self.update()
         messagebox.showinfo("Sucesso", "NOME DA TELA COPIADO")

    def atualizar_rodape(self):
        self.lbl_footer.configure(text=f"👤 {self.config['nome_usuario']}  |  🖥️ {self.config['servidor']}  |  🗄️ {self.config['banco']}")

    def abrir_configuracoes(self): 
        ConfigWindow(self, self.config, lambda c: [setattr(self, 'config', c), self.atualizar_rodape()])

    def abrir_analise_produto(self):
        AnaliseProdutoWindow(self, self.config)

    def abrir_analise(self): 
        app_win = AnaliseVendasWindow(self, self.config)
        app_win.after(100, lambda: app_win.lift())

    def abrir_cep(self): 
        app_win = App(self, self.config)
        app_win.after(100, lambda: app_win.lift())

def centralizar_tela(tela, w, h):
    x = (tela.winfo_screenwidth() // 2) - (w // 2)
    y = (tela.winfo_screenheight() // 2) - (h // 2)
    tela.geometry(f"{w}x{h}+{x}+{y}")


# =====================================================================
# TELA 4: ANÁLISE DE VENDAS POR PRODUTO (CFG_PRODS)
# =====================================================================
import tkinter.ttk as ttk

class AnaliseProdutoWindow(ctk.CTkToplevel):
    def __init__(self, parent, config):
        super().__init__(parent)
        self.title("Análise de Vendas por Produto")
        self.geometry("850x650")
        self.config_db = config
        self.grab_set()  # Trava a janela pai
        
        largura = 850; altura = 650
        x = (self.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.winfo_screenheight() // 2) - (altura // 2)
        self.geometry(f"{largura}x{altura}+{x}+{y}")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # 1. Top Filters
        self.top_frame = ctk.CTkFrame(self, fg_color="#F5F5F7", height=80, corner_radius=0)
        self.top_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        self.top_frame.grid_columnconfigure(6, weight=1)

        ctk.CTkLabel(self.top_frame, text="Ano:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=(20, 5), pady=20, sticky="e")
        self.combo_ano = ctk.CTkComboBox(self.top_frame, values=["Todos"], width=100)
        self.combo_ano.grid(row=0, column=1, padx=5, pady=20, sticky="w")

        ctk.CTkLabel(self.top_frame, text="Mês:", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=(20, 5), pady=20, sticky="e")
        self.meses_ext = ["Todos", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        self.combo_mes = ctk.CTkComboBox(self.top_frame, values=self.meses_ext, width=120)
        self.combo_mes.set("Todos")
        self.combo_mes.grid(row=0, column=3, padx=5, pady=20, sticky="w")

        ctk.CTkLabel(self.top_frame, text="Métrica:", font=("Arial", 12, "bold")).grid(row=0, column=4, padx=(20, 5), pady=20, sticky="e")
        self.combo_metrica = ctk.CTkComboBox(self.top_frame, values=["Quantidade", "Valor Venda", "Lucro"], width=130)
        self.combo_metrica.set("Quantidade")
        self.combo_metrica.grid(row=0, column=5, padx=5, pady=20, sticky="w")

        ctk.CTkLabel(self.top_frame, text="Exibir:", font=("Arial", 12, "bold")).grid(row=0, column=6, padx=(20, 5), pady=20, sticky="e")
        self.combo_limite = ctk.CTkComboBox(self.top_frame, values=["Top 10", "Top 20", "Top 50", "Top 100"], width=110)
        self.combo_limite.set("Top 20")
        self.combo_limite.grid(row=0, column=7, padx=5, pady=20, sticky="w")

        ctk.CTkLabel(self.top_frame, text="Produto:", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=(20, 5), pady=(5, 20), sticky="e")
        self.txt_pesquisa = ctk.CTkEntry(self.top_frame, placeholder_text="Filtrar por nome do produto...", width=360)
        self.txt_pesquisa.grid(row=1, column=1, columnspan=4, padx=5, pady=(5, 20), sticky="w")

        self.btn_filtrar = ctk.CTkButton(self.top_frame, text="🔍 Atualizar", font=("Arial", 12, "bold"), width=120, command=self.carregar_dados, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_filtrar.grid(row=1, column=5, padx=20, pady=(5, 20), sticky="w")

        # 2. Main Frame
        self.grid_frame = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        self.grid_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#FFFFFF", fieldbackground="#FFFFFF", foreground="black", rowheight=32, font=("Arial", 11))
        style.configure("Treeview.Heading", background="#1565C0", foreground="white", font=("Arial", 11, "bold"))
        style.map("Treeview", background=[('selected', '#1E88E5')], foreground=[('selected', 'white')])

        self.tree = ttk.Treeview(self.grid_frame, columns=("Rank", "Cod", "Desc", "Qtd", "Venda", "Lucro"), show="headings", selectmode="browse")
        self.tree.pack(fill="both", expand=True, side="left")
        self.tree.tag_configure('even', background='#FFFFFF')
        self.tree.tag_configure('odd', background='#E2E8F0')

        self.tree.heading("Rank", text="🏆 #")
        self.tree.heading("Cod", text="🔑 Código")
        self.tree.heading("Desc", text="📦 Produto")
        self.tree.heading("Qtd", text="🛒 Qtd")
        self.tree.heading("Venda", text="💰 Total Venda")
        self.tree.heading("Lucro", text="📈 Lucro")

        self.tree.column("Rank", width=40, anchor="center")
        self.tree.column("Cod", width=80, anchor="center")
        self.tree.column("Desc", width=300, anchor="w")
        self.tree.column("Qtd", width=60, anchor="center")
        self.tree.column("Venda", width=120, anchor="center")
        self.tree.column("Lucro", width=120, anchor="center")

        sb = ttk.Scrollbar(self.grid_frame, orient="vertical", command=self.tree.yview)
        sb.pack(fill="y", side="right")
        self.tree.configure(yscrollcommand=sb.set)

        # 3. Footer
        self.footer_frame = ctk.CTkFrame(self, height=50, fg_color="#F5F5F7", corner_radius=0)
        self.footer_frame.grid(row=2, column=0, sticky="ew", padx=0, pady=0)

        fechar_ico_path = os.path.join(os.path.dirname(__file__), "btn_fechar.png")
        if os.path.exists(fechar_ico_path):
            img_fechar = Image.open(fechar_ico_path).resize((18, 18))
            self.fechar_img = ctk.CTkImage(light_image=img_fechar, dark_image=img_fechar, size=(18, 18))
            self.btn_fechar = ctk.CTkButton(self.footer_frame, text="Fechar Tela", image=self.fechar_img, compound="left", font=("Arial", 12, "bold"), fg_color="transparent", text_color="black", border_width=2, border_color="black", hover_color="#E0E0E0", width=130, command=self.destroy)
        else:
            self.btn_fechar = ctk.CTkButton(self.footer_frame, text="Fechar Tela", font=("Arial", 12, "bold"), fg_color="transparent", text_color="black", border_width=2, border_color="black", hover_color="#E0E0E0", width=130, command=self.destroy)
        self.btn_fechar.pack(side="left", padx=20, pady=10)

        self.frame_id = ctk.CTkFrame(self.footer_frame, fg_color="transparent")
        self.frame_id.pack(side="right", padx=15)
        self.lbl_tela_id = ctk.CTkLabel(self.frame_id, text="Tela: CFG_PRODS", font=ctk.CTkFont(size=11, weight="bold"), text_color="gray")
        self.lbl_tela_id.pack(side="left")
        from tkinter import messagebox
        self.btn_copy_id = ctk.CTkButton(self.frame_id, text="📋", width=20, height=20, fg_color="transparent", hover_color="#E0E0E0", text_color="black", command=lambda: [self.clipboard_clear(), self.clipboard_append("CFG_PRODS"), messagebox.showinfo("Sucesso", "NOME DA TELA COPIADO")])
        self.btn_copy_id.pack(side="left", padx=5)
        ToolTip(self.btn_copy_id, "COPIAR NOME TELA")
        
        # Bootstrap
        self.after(200, self.carregar_anos)

    def carregar_anos(self):
        server = self.config_db.get("servidor")
        database = self.config_db.get("banco")
        username = self.config_db.get("usuario_bd")
        password = self.config_db.get("senha_bd")
        
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"
        try:
            import pyodbc, pandas as pd
            conn = pyodbc.connect(conn_str)
            df_anos = pd.read_sql("SELECT DISTINCT YEAR(CRMovDta) as Ano FROM crmov4 WHERE CRMovDta IS NOT NULL AND YEAR(CRMovDta) != 9999", conn)
            conn.close()
            
            anos = sorted(df_anos['Ano'].dropna().unique().tolist(), reverse=True)
            self.combo_ano.configure(values=["Todos"] + [str(int(a)) for a in anos])
        except: pass

    def carregar_dados(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        server = self.config_db.get("servidor"); database = self.config_db.get("banco"); username = self.config_db.get("usuario_bd"); password = self.config_db.get("senha_bd")
        
        ano = self.combo_ano.get(); mes = self.combo_mes.get(); limite = self.combo_limite.get().replace("Top ", ""); metrica = self.combo_metrica.get()
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"
        
        try:
            import pyodbc, pandas as pd
            conn = pyodbc.connect(conn_str)
            where_clauses = ["c4.CRMovDta IS NOT NULL", "YEAR(c4.CRMovDta) != 9999"]
            if ano != "Todos": where_clauses.append(f"YEAR(c4.CRMovDta) = {int(ano)}")
            if mes != "Todos": 
                try: mes_idx = self.meses_ext.index(mes); where_clauses.append(f"MONTH(c4.CRMovDta) = {mes_idx}")
                except: pass
            
            pesquisa = self.txt_pesquisa.get().strip()
            if pesquisa: where_clauses.append(f"p.CEProDes LIKE '%{pesquisa}%'")

            where_str = " AND ".join(where_clauses)

            order_venda = "SUM((c4.CRMov4Qtd * c4.CRMov4VlrU) - ((c4.CRMov4Qtd * c4.CRMov4PreT) * (c4.CRMov4PerD / 100.0)) - c4.CRMov4VlDs - c4.CRMov4VDV - c4.CRMov4VAF)"
            order_custo = "SUM(c4.CRMov4CusP * c4.CRMov4Qtd)"
            
            if metrica == "Valor Venda": order_by = f"{order_venda} DESC"
            elif metrica == "Lucro": order_by = f"({order_venda} - {order_custo}) DESC"
            else: order_by = "SUM(c4.CRMov4Qtd) DESC"

            query = f"""
                SELECT TOP {int(limite)} c4.CEProCod, p.CEProDes, 
                       SUM(c4.CRMov4Qtd) as TotalQtd,
                       {order_venda} as TotalVenda,
                       {order_custo} as TotalCusto
                FROM crmov4 c4
                INNER JOIN crmov2 c2 ON c4.CMEmpCod = c2.CMEmpCod AND c4.CMFilCod = c2.CMFilCod AND c4.CRMovDta = c2.CRMovDta AND c4.CRMovSeq = c2.CRMovSeq
                INNER JOIN cepro p ON c4.CEProCod = p.CEProCod
                WHERE {where_str}
                GROUP BY c4.CEProCod, p.CEProDes ORDER BY {order_by}
            """
            df = pd.read_sql(query, conn); conn.close()

            for index, row in df.iterrows():
                try: cod_pro = str(int(float(row['CEProCod'])))
                except: cod_pro = str(row['CEProCod']).strip()

                try: qtd_int = int(float(row['TotalQtd'])); qtd = f"{qtd_int:,}".replace(",", ".")
                except: qtd = str(row['TotalQtd'])

                try:
                    venda_val = float(row.get('TotalVenda', 0))
                    custo_val = float(row.get('TotalCusto', 0))
                    lucro_val = venda_val - custo_val
                    
                    def format_money(val): return f"R$ {val:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                    
                    venda_str = format_money(venda_val)
                    lucro_str = format_money(lucro_val)
                except:
                    venda_str = lucro_str = "R$ 0,00"

                self.tree.insert("", "end", values=(index + 1, cod_pro, row['CEProDes'].strip(), qtd, venda_str, lucro_str), tags=('even' if index % 2 == 0 else 'odd',))
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erro de Filtro", f"Não foi possível carregar os produtos:\n\n{str(e)}")


if __name__ == '__main__':
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description="Módulo de Análise e Atualização")
    parser.add_argument("--tela", type=str, choices=["ANALISE", "CEP"], help="Abre uma tela específica diretamente")
    parser.add_argument("--servidor", type=str, help="Servidor SQL Server")
    parser.add_argument("--banco", type=str, help="Nome do Banco de Dados")
    parser.add_argument("--usuario", type=str, help="Usuário SQL Server")
    parser.add_argument("--senha", type=str, help="Senha SQL Server")
    
    args = parser.parse_args()
    
    # Configuração Padrão
    config = {
        "nome_usuario": "Operador", 
        "servidor": r"servidor\sqlexpress", 
        "banco": "msinfor", 
        "usuario_bd": "sa", 
        "senha_bd": "Mabelu2011"
    }
    
    # Sobrescreve com argumentos da linha de comando se houver
    if args.servidor: config["servidor"] = args.servidor
    if args.banco: config["banco"] = args.banco
    if args.usuario: config["usuario_bd"] = args.usuario
    if args.senha: config["senha_bd"] = args.senha

    if args.tela:
        # Se for para abrir uma tela direta, cria um root invisível
        root = ctk.CTk()
        root.withdraw()
        
        if args.tela.upper() == "ANALISE":
            app_win = AnaliseVendasWindow(root, config)
        elif args.tela.upper() == "CEP":
            app_win = App(root, config)
            
        root.mainloop()
    else:
        # Modo Padrão (Sem tela informada, abre o Hub)
        app = MainHub()
        # Se você quiser que o MainHub também aceite os argumentos acima:
        if args.servidor: app.config["servidor"] = args.servidor
        if args.banco: app.config["banco"] = args.banco
        if args.usuario: app.config["usuario_bd"] = args.usuario
        if args.senha: app.config["senha_bd"] = args.senha
        app.mainloop()
