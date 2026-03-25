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
        self.lbl_title = ctk.CTkLabel(self, text="⚙️ MAPEAMENTO DA TABELA", font=ctk.CTkFont(size=18, weight="bold"), text_color="#1565C0", anchor="w")
        self.lbl_title.pack(pady=(20, 10), padx=30, fill="x")


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
        ctk.CTkLabel(self, text="⚙️ CONFIGURAR ACESSO", font=ctk.CTkFont(size=20, weight="bold"), text_color="#1565C0", anchor="w").pack(pady=(20, 10), padx=30, fill="x")

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

class App(ctk.CTkFrame):
    def __init__(self, parent, db_config):
        super().__init__(parent, fg_color="#FFFFFF", corner_radius=0)

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

        # --- Top Frame (Menu Superior Expandido) Cor Chumbo ---
        self.top_frame = ctk.CTkFrame(self, fg_color="#D1D5DB", corner_radius=0)
        self.top_frame.grid(row=0, column=0, padx=0, pady=0, sticky="ew")
        self.top_frame.grid_columnconfigure(6, weight=1) # Espaçador

        # --- NOVO: Linha de Título Superior ---
        self.title_bar = ctk.CTkFrame(self.top_frame, fg_color="transparent", height=35)
        self.title_bar.grid(row=0, column=0, columnspan=7, sticky="ew", padx=20, pady=(5, 0))
        
        self.lbl_titulo = ctk.CTkLabel(self.title_bar, text="📍 ATUALIZAÇÃO DE CEP", font=("Arial", 16, "bold"), text_color="#1565C0")
        self.lbl_titulo.pack(side="left")

        # Componentes do Top Frame (Agora na Row 1)
        self.btn_config = ctk.CTkButton(self.top_frame, text="⚙️ Mapear", width=100, fg_color="#455A64", hover_color="#37474F", command=self.abrir_config)
        self.btn_config.grid(row=1, column=0, padx=10, pady=(5, 15))

        self.search_entry = ctk.CTkEntry(self.top_frame, placeholder_text="Buscar cliente (Deixe vazio para TODOS)...", width=260)
        self.search_entry.grid(row=1, column=1, padx=10, pady=(5, 15))

        self.btn_listar = ctk.CTkButton(self.top_frame, text="🔍 Simular Atualização", fg_color="#1E88E5", hover_color="#1565C0", command=self.simular_click)
        self.btn_listar.grid(row=1, column=2, padx=10, pady=(5, 15))

        self.btn_filtrar = ctk.CTkButton(self.top_frame, text="👁️ Mostrar: TODOS", width=130, fg_color="#7B1FA2", hover_color="#4A148C", command=self.alternar_filtro_click)
        self.btn_filtrar.grid(row=1, column=3, padx=10, pady=(5, 15))

        self.btn_gravar = ctk.CTkButton(self.top_frame, text="💾 Gravar no BD", width=120, fg_color="#43A047", hover_color="#2E7D32", state="disabled", command=self.gravar_click)
        self.btn_gravar.grid(row=1, column=4, padx=10, pady=(5, 15))
        
        self.lbl_stats = ctk.CTkLabel(self.top_frame, text="Simulação pendente...", font=ctk.CTkFont(slant="italic"))
        self.lbl_stats.grid(row=1, column=5, padx=10, pady=(5, 15))


        # Botão Fechar de topo removido para usar apenas o do rodapé

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
            command=self.fechar_tela
        )
        self.btn_sair.pack(side="left", padx=(0, 15))

        self.lbl_status = ctk.CTkLabel(self.bottom_frame, text="💡 Status: Pronto. Preencha a Busca e clique em Simular.", font=ctk.CTkFont(size=12))
        self.lbl_status.pack(side="left")

        # Botões de Exportação CEP
        self.btn_export_pdf = ctk.CTkButton(self.bottom_frame, text="📄 Exportar PDF", width=120, height=32, fg_color="#E53935", hover_color="#B71C1C", command=self.exportar_pdf)
        self.btn_export_pdf.pack(side="right", padx=5)
        
        self.btn_export_excel = ctk.CTkButton(self.bottom_frame, text="📊 Exportar Excel", width=120, height=32, fg_color="#43A047", hover_color="#2E7D32", command=self.exportar_excel)
        self.btn_export_excel.pack(side="right", padx=5)

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

    def exportar_excel(self):
        items = self.tree.get_children()
        from tkinter import messagebox
        if not items: messagebox.showwarning("Aviso", "Nenhum dado para exportar."); return
        columns = self.tree["columns"]; cols_titles = [self.tree.heading(c)["text"] for c in columns]; data = [self.tree.item(k)['values'] for k in items]
        try:
             import pandas as pd, tempfile, os
             df = pd.DataFrame(data, columns=cols_titles)
             filepath = os.path.join(tempfile.gettempdir(), "Relatorio_CEPs.xlsx")
             
             writer = pd.ExcelWriter(filepath, engine='openpyxl')
             df.to_excel(writer, index=False, sheet_name='Sheet1')
             worksheet = writer.sheets['Sheet1']
             for i, col in enumerate(df.columns):
                  max_len = max(df[col].astype(str).map(len).max(), len(str(col))) + 2
                  from openpyxl.utils import get_column_letter
                  worksheet.column_dimensions[get_column_letter(i+1)].width = max_len
             writer.close()
             
             os.startfile(filepath)
        except Exception as e: messagebox.showerror("Erro Excel", str(e))

    def exportar_pdf(self):
        items = self.tree.get_children()
        from tkinter import messagebox
        if not items: messagebox.showwarning("Aviso", "Nenhum dado para exportar."); return
        columns = self.tree["columns"]; cols_titles = [self.tree.heading(c)["text"] for c in columns]; data = [self.tree.item(k)['values'] for k in items]
        try:
             import tempfile, os
             filepath = os.path.join(tempfile.gettempdir(), "Relatorio_CEPs.pdf")
             import sys, subprocess
             try: import fpdf
             except: subprocess.run([sys.executable, "-m", "pip", "install", "fpdf"], capture_output=True); import fpdf
             pdf = fpdf.FPDF(); pdf.add_page(); pdf.set_font("Arial", 'B', 12); pdf.cell(190, 10, "RELATORIO DE CEPs", 0, 1, 'C'); pdf.ln(5)
             pdf.set_font("Arial", 'B', 8); num_cols = len(cols_titles); w_col = 190 / num_cols if num_cols > 0 else 30
             for c in cols_titles: pdf.cell(w_col, 8, str(c), 1, 0, 'C')
             pdf.ln(8); pdf.set_font("Arial", '', 7)
             for r in data:
                  for val in r: pdf.cell(w_col, 7, str(val)[:20], 1, 0, 'C')
                  pdf.ln(7)
             pdf.ln(5); pdf.output(filepath); os.startfile(filepath)
        except Exception as e: messagebox.showerror("Erro PDF", str(e))

    def fechar_tela(self):
         if hasattr(self, 'hub'):
              self.hub.fechar_modulo_atual()
         else:
              self.destroy()


class AnaliseVendasWindow(ctk.CTkFrame):
    def __init__(self, parent, config):
        super().__init__(parent, fg_color="#FFFFFF", corner_radius=0)
        self.config = config
        
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
            command=self.fechar_tela
        )
        self.btn_sair.pack(side="left")

        # Exportações
        self.btn_export_pdf = ctk.CTkButton(self.buttons_frame, text="📄 Exportar PDF", width=140, height=32, fg_color="#E53935", hover_color="#B71C1C", command=self.exportar_pdf)
        self.btn_export_pdf.pack(side="right", padx=5)
        
        self.btn_export_excel = ctk.CTkButton(self.buttons_frame, text="📊 Exportar Excel", width=140, height=32, fg_color="#43A047", hover_color="#2E7D32", command=self.exportar_excel)
        self.btn_export_excel.pack(side="right", padx=5)

        # 3. Topo: Controles (Cabeçalho Chumbo Ocupando Extensão)
        self.top_frame = ctk.CTkFrame(self, fg_color="#D1D5DB", corner_radius=0)
        self.top_frame.pack(side="top", fill="x", padx=0, pady=0)      

        # --- NOVO: Linha de Título Superior ---
        self.title_bar = ctk.CTkFrame(self.top_frame, fg_color="transparent", height=35)
        self.title_bar.pack(side="top", fill="x", padx=20, pady=(5, 0))
        
        self.lbl_titulo = ctk.CTkLabel(self.title_bar, text="📊 ANÁLISE DE VENDAS POR HORA", font=("Arial", 16, "bold"), text_color="#1565C0")
        self.lbl_titulo.pack(side="left")

        # Sub-container interno para margens (Transparente para manter o fundo chumbo)
        self.top_grid_frame = ctk.CTkFrame(self.top_frame, fg_color="transparent")
        self.top_grid_frame.pack(side="top", fill="x", padx=10, pady=(5, 10))

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
            query = "SELECT CRMovDta, CRMov2CHor, CRMov2VlrO FROM crmov2 WHERE CRMovDta IS NOT NULL AND CRMov2Flag IN ('A', 'F')"
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
        
        try:
            import tempfile, os, pandas as pd
            filepath = os.path.join(tempfile.gettempdir(), "Analise_Vendas.xlsx")
            
            writer = pd.ExcelWriter(filepath, engine='openpyxl')
            self.df_grouped.to_excel(writer, index=False, sheet_name='Sheet1')
            worksheet = writer.sheets['Sheet1']
            for i, col in enumerate(self.df_grouped.columns):
                 max_len = max(self.df_grouped[col].astype(str).map(len).max(), len(str(col))) + 2
                 from openpyxl.utils import get_column_letter
                 worksheet.column_dimensions[get_column_letter(i+1)].width = max_len
            writer.close()
            
            os.startfile(filepath)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def exportar_pdf(self):
        if self.df_grouped is None or self.df_grouped.empty:
            messagebox.showwarning("Aviso", "Nenhum gráfico gerado para exportar.")
            return
        
        try:
            import tempfile, os
            filepath = os.path.join(tempfile.gettempdir(), "Grafico_Vendas.pdf")
            self.fig.savefig(filepath, format="pdf", bbox_inches="tight")
            os.startfile(filepath)  # Abre o PDF automaticamente
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def fechar_tela(self):
         if hasattr(self, 'hub'):
              self.hub.fechar_modulo_atual()
         else:
              self.destroy()

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
        self.modules_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1) # 5 Colunas
        self.modules_frame.grid_rowconfigure(0, weight=1)
        
        btn_width = 240 # Ligeiramente reduzido para acomodar 5 colunas
        
        # --- CONTAINER 1º COLUNA ---
        self.col1_frame = ctk.CTkFrame(self.modules_frame, fg_color="#F8FAFC", corner_radius=15, border_width=2, border_color="#E2E8F0")
        self.col1_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        ctk.CTkLabel(self.col1_frame, text="1º Coluna", font=("Arial", 15, "bold"), text_color="#1E293B").pack(pady=(20, 15))

        # Botões Coluna 1 (Empilhados)
        self.btn_cep = ctk.CTkButton(self.col1_frame, text="📍 Atualizar CEP", width=btn_width, height=45, font=("Arial", 13, "bold"), command=self.abrir_cep, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_cep.pack(pady=8, padx=15)
        ToolTip(self.btn_cep, "Reparo automatizado de CEPs")

        self.btn_analise = ctk.CTkButton(self.col1_frame, text="📊 Vendas por Hora", width=btn_width, height=45, font=("Arial", 13, "bold"), command=self.abrir_analise, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_analise.pack(pady=8, padx=15)

        self.btn_analise_prod = ctk.CTkButton(self.col1_frame, text="🛒 Vendas por Produto", width=btn_width, height=45, font=("Arial", 13, "bold"), command=self.abrir_analise_produto, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_analise_prod.pack(pady=8, padx=15)

        self.btn_resumo_cli = ctk.CTkButton(self.col1_frame, text="🛍️ Análise Compras por Cliente", width=btn_width, height=45, font=("Arial", 13, "bold"), command=self.abrir_resumo_cliente, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_resumo_cli.pack(pady=8, padx=15)

        self.btn_pararam = ctk.CTkButton(self.col1_frame, text="🛑 Clientes Inativos", width=btn_width, height=45, font=("Arial", 13, "bold"), command=self.abrir_clientes_pararam, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_pararam.pack(pady=8, padx=15)

        self.btn_contas = ctk.CTkButton(self.col1_frame, text="💰 Resumo por Tipo Venda", width=btn_width, height=45, font=("Arial", 13, "bold"), command=self.abrir_posicao_contas, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_contas.pack(pady=8, padx=15)

        # --- 2º COLUNA ( OPERAÇÃO / ESTOQUE ) ---
        self.col2_frame = ctk.CTkFrame(self.modules_frame, fg_color="#F8FAFC", corner_radius=15, border_width=2, border_color="#E2E8F0")
        self.col2_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        ctk.CTkLabel(self.col2_frame, text="2º Coluna", font=("Arial", 15, "bold"), text_color="#1E293B").pack(pady=(20, 15))

        self.btn_estoque_parado = ctk.CTkButton(self.col2_frame, text="📦 Estoque Parado", width=btn_width, height=45, font=("Arial", 13, "bold"), command=self.abrir_estoque_parado, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_estoque_parado.pack(pady=8, padx=15)

        self.btn_sugestao_compra = ctk.CTkButton(self.col2_frame, text="🛒 Sugestão de Compra", width=btn_width, height=45, font=("Arial", 13, "bold"), command=self.abrir_sugestao_compra, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_sugestao_compra.pack(pady=8, padx=15)

        self.btn_parcelas = ctk.CTkButton(self.col2_frame, text="💳 Análise das Parcelas", width=btn_width, height=45, font=("Arial", 13, "bold"), command=self.abrir_analise_parcelas, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_parcelas.pack(pady=8, padx=15)

        self.btn_cobranca = ctk.CTkButton(self.col2_frame, text="📞 Cobrança por Cliente", width=btn_width, height=45, font=("Arial", 13, "bold"), command=lambda: None, fg_color="#1E88E5", hover_color="#1565C0")
        self.btn_cobranca.pack(pady=8, padx=15)

        # --- OUTRAS COLUNAS VAZIAS ( placeholder ) ---
        for col_idx in range(2, 5):
             f = ctk.CTkFrame(self.modules_frame, fg_color="#F8FAFC", corner_radius=15, border_width=1, border_color="#E2E8F0")
             f.grid(row=0, column=col_idx, sticky="nsew", padx=10, pady=10)
             ctk.CTkLabel(f, text=f"{col_idx + 1}º Coluna", font=("Arial", 15, "bold"), text_color="#94A3B8").pack(pady=(20, 15))

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

        self.protocol("WM_DELETE_WINDOW", lambda: None)
        self.after(100, self._desabilitar_close_windows)

    def _desabilitar_close_windows(self):
        try:
            import ctypes
            hwnd = ctypes.windll.user32.GetParent(self.winfo_id())
            if not hwnd: hwnd = self.winfo_id()
            hMenu = ctypes.windll.user32.GetSystemMenu(hwnd, False)
            if hMenu:
                 ctypes.windll.user32.EnableMenuItem(hMenu, 0xF060, 1 | 2)
        except: pass

    def copiar_id(self, texto):
         self.clipboard_clear()
         self.clipboard_append(texto)
         self.update()
         messagebox.showinfo("Sucesso", "NOME DA TELA COPIADO")

    def atualizar_rodape(self):
        self.lbl_footer.configure(text=f"👤 {self.config['nome_usuario']}  |  🖥️ {self.config['servidor']}  |  🗄️ {self.config['banco']}")

    def abrir_configuracoes(self): 
        ConfigWindow(self, self.config, lambda c: [setattr(self, 'config', c), self.atualizar_rodape()])

    def fechar_modulo_atual(self):
        if hasattr(self, 'modulo_atual') and self.modulo_atual:
             self.modulo_atual.destroy()
             self.modulo_atual = None
        self.modules_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Bugfix CustomTkinter: Força recalculo de geometria
        self.update()
        w = self.winfo_width(); h = self.winfo_height()
        if w > 1 and h > 1:
             self.geometry(f"{w+1}x{h}")
             self.after(5, lambda: self.geometry(f"{w}x{h}"))

    def abrir_modulo(self, classe_modulo):
        if hasattr(self, "modulo_atual") and self.modulo_atual:
             self.modulo_atual.destroy()
        self.modules_frame.pack_forget()
        self.modulo_atual = classe_modulo(self.main_frame, self.config)
        self.modulo_atual.hub = self
        self.modulo_atual.pack(fill="both", expand=True)
        
        # Bugfix CustomTkinter: Força recalculo ao abrir módulo
        self.update()
        w = self.winfo_width(); h = self.winfo_height()
        if w > 1 and h > 1:
             self.geometry(f"{w+1}x{h}")
             self.after(50, lambda: self.geometry(f"{w}x{h}")) # <--- Delay aumentado para 50ms

    def abrir_analise_produto(self): self.abrir_modulo(AnaliseProdutoWindow)
    def abrir_analise(self): self.abrir_modulo(AnaliseVendasWindow)
    def abrir_cep(self): self.abrir_modulo(App)

    def abrir_resumo_cliente(self): self.abrir_modulo(ResumoClienteWindow)
    def abrir_clientes_pararam(self): self.abrir_modulo(ClientesPararamWindow)
    def abrir_posicao_contas(self): self.abrir_modulo(PosicaoContasReceberWindow)
    def abrir_estoque_parado(self): self.abrir_modulo(EstoqueParadoWindow)
    def abrir_sugestao_compra(self): self.abrir_modulo(SugestaoCompraWindow)
    def abrir_analise_parcelas(self): self.abrir_modulo(AnaliseParcelasWindow)

def centralizar_tela(tela, w, h):
    x = (tela.winfo_screenwidth() // 2) - (w // 2)
    y = (tela.winfo_screenheight() // 2) - (h // 2)
    tela.geometry(f"{w}x{h}+{x}+{y}")


# =====================================================================
# TELA 4: ANÁLISE DE VENDAS POR PRODUTO (CFG_PRODS)
# =====================================================================
# NOVAS TELAS: BASE E ESPECIALIZADAS
# =====================================================================

class BaseWindow(ctk.CTkFrame):
    def __init__(self, parent, title_str, id_str):
        super().__init__(parent, fg_color="#FFFFFF", corner_radius=0)
        self.grid_rowconfigure(1, weight=1); self.grid_columnconfigure(0, weight=1)

        # Top Bar (Cabeçalho Chumbo)
        self.top_frame = ctk.CTkFrame(self, fg_color="#D1D5DB", corner_radius=0)
        self.top_frame.grid(row=0, column=0, sticky="ew")
        
        # --- NOVO: Linha de Título Superior ---
        self.title_bar = ctk.CTkFrame(self.top_frame, fg_color="transparent", height=25)
        self.title_bar.pack(side="top", fill="x", padx=20, pady=(0, 0))


        
        # Título da Tela à Esquerda (Azul)
        self.lbl_titulo = ctk.CTkLabel(self.title_bar, text=title_str.upper(), font=("Arial", 16, "bold"), text_color="#1565C0")
        self.lbl_titulo.pack(side="left", pady=0)



        # Grid frame
        self.grid_frame = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        self.grid_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 10))


        style = ttk.Style()
        style.configure(id_str + ".Treeview", background="#FFFFFF", fieldbackground="#FFFFFF", foreground="black", rowheight=32, font=("Arial", 11))
        style.configure(id_str + ".Treeview.Heading", background="#1565C0", foreground="white", font=("Arial", 11, "bold"))

        self.tree = ttk.Treeview(self.grid_frame, show="headings", selectmode="browse")
        self.tree.pack(fill="both", expand=True, side="left")
        self.tree.tag_configure('even', background='#FFFFFF')
        self.tree.tag_configure('odd', background='#E2E8F0')

        # Rodape (Transparente para consistência)
        self.bottom_bar = ctk.CTkFrame(self, fg_color="transparent", height=40, corner_radius=0)
        self.bottom_bar.grid(row=2, column=0, sticky="ew")
        
        btn_sair = ctk.CTkButton(self.bottom_bar, text="✖  Fechar Tela", command=self.fechar_tela, fg_color="transparent", hover_color="#E0E0E0", text_color="black", font=("Arial", 12, "bold"), border_width=2, border_color="black", width=130)
        btn_sair.pack(side="left", padx=20, pady=5)

        # Botões de Exportação
        self.btn_export_pdf = ctk.CTkButton(self.bottom_bar, text="📄 Exportar PDF", width=120, height=32, fg_color="#E53935", hover_color="#B71C1C", command=self.exportar_pdf)
        self.btn_export_pdf.pack(side="right", padx=5)
        
        self.btn_export_excel = ctk.CTkButton(self.bottom_bar, text="📊 Exportar Excel", width=120, height=32, fg_color="#43A047", hover_color="#2E7D32", command=self.exportar_excel)
        self.btn_export_excel.pack(side="right", padx=5)

        from tkinter import messagebox
        btn_copy_id = ctk.CTkButton(self.bottom_bar, text="📋", width=25, height=25, fg_color="transparent", hover_color="#E0E0E0", text_color="black", font=("Arial", 11, "bold"), command=lambda: [self.clipboard_clear(), self.clipboard_append(id_str), messagebox.showinfo("Sucesso", "NOME DA TELA COPIADO")])
        btn_copy_id.pack(side="right", padx=(5, 20))

        self.lbl_id = ctk.CTkLabel(self.bottom_bar, text=f"Tela: {id_str}", font=("Arial", 11, "bold"), text_color="gray")
        self.lbl_id.pack(side="right", padx=5)
        ToolTip(btn_copy_id, "COPIAR NOME TELA")

    def fechar_tela(self):
        self.pack_forget()
        if hasattr(self, 'hub') and hasattr(self.hub, 'modules_frame'):
            self.hub.modules_frame.pack(fill="both", expand=True, padx=30, pady=30)
        self.destroy()

    def exportar_excel(self):
        items = self.tree.get_children()
        from tkinter import messagebox
        if not items: messagebox.showwarning("Aviso", "Nenhum dado para exportar."); return
        try:
             columns = self.tree["columns"]; cols_titles = [self.tree.heading(c)["text"] for c in columns]; data = [self.tree.item(k)['values'] for k in items]
             import pandas as pd, tempfile, os
             df = pd.DataFrame(data, columns=cols_titles)
             filepath = os.path.join(tempfile.gettempdir(), "Relatorio_Dados.xlsx")
             
             writer = pd.ExcelWriter(filepath, engine='openpyxl')
             df.to_excel(writer, index=False, sheet_name='Sheet1')
             worksheet = writer.sheets['Sheet1']
             for i, col in enumerate(df.columns):
                  max_len = max(df[col].astype(str).map(len).max(), len(str(col))) + 2
                  from openpyxl.utils import get_column_letter
                  worksheet.column_dimensions[get_column_letter(i+1)].width = max_len
             writer.close()
             
             os.startfile(filepath)
        except Exception as e: messagebox.showerror("Erro Excel", str(e))

    def exportar_pdf(self):
        items = self.tree.get_children()
        from tkinter import messagebox
        if not items: messagebox.showwarning("Aviso", "Nenhum dado para exportar."); return
        try:
             columns = self.tree["columns"]; cols_titles = [self.tree.heading(c)["text"] for c in columns]; data = [self.tree.item(k)['values'] for k in items]
             import tempfile, os
             filepath = os.path.join(tempfile.gettempdir(), "Relatorio_Dados.pdf")
             import sys, subprocess
             try: import fpdf
             except: subprocess.run([sys.executable, "-m", "pip", "install", "fpdf"], capture_output=True); import fpdf
             pdf = fpdf.FPDF(); pdf.add_page(); pdf.set_font("Arial", 'B', 12); pdf.cell(190, 10, "RELATORIO DE DADOS", 0, 1, 'C'); pdf.ln(5)
             pdf.set_font("Arial", 'B', 8); num_cols = len(cols_titles); w_col = 190 / num_cols if num_cols > 0 else 30
             for c in cols_titles: 
                  c_str = str(c).encode('latin-1', 'replace').decode('latin-1')
                  pdf.cell(w_col, 8, c_str, 1, 0, 'C')
             pdf.ln(8); pdf.set_font("Arial", '', 7)
             for r in data:
                  for val in r: 
                       v_str = str(val)[:20].encode('latin-1', 'replace').decode('latin-1')
                       pdf.cell(w_col, 7, v_str, 1, 0, 'C')
                  pdf.ln(7)
             if hasattr(self, 'lbl_rodape_total'):
                  pdf.ln(5); pdf.set_font("Arial", 'B', 10)
                  txt_rodape = self.lbl_rodape_total.cget("text").encode('latin-1', 'replace').decode('latin-1')
                  pdf.cell(190, 10, txt_rodape, 0, 1, 'R')
             pdf.ln(5); pdf.output(filepath); os.startfile(filepath)
        except Exception as e: messagebox.showerror("Erro PDF", str(e))


class AnaliseProdutoWindow(BaseWindow):
    def __init__(self, parent, config):
        super().__init__(parent, "Análise de Vendas por Produto", "CFG_PRODS")
        self.config_db = config

        # Barra de Filtros (Alinhada à esquerda e transparente)
        self.filter_frame = ctk.CTkFrame(self.top_frame, fg_color="transparent")
        self.filter_frame.pack(side="left", padx=20, pady=(0, 5), anchor="w")


        # LINHA 1
        ctk.CTkLabel(self.filter_frame, text="Ano:", font=("Arial", 16, "bold"), text_color="#1E293B").pack(side="left", padx=(10, 5))
        self.combo_ano = ctk.CTkComboBox(self.filter_frame, values=["Todos"], width=90, font=("Arial", 15))
        self.combo_ano.pack(side="left", padx=5); self.combo_ano.set("Todos")

        ctk.CTkLabel(self.filter_frame, text="Mês:", font=("Arial", 16, "bold"), text_color="#1E293B").pack(side="left", padx=(15, 5))
        self.meses_ext = ["Todos", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        self.combo_mes = ctk.CTkComboBox(self.filter_frame, values=self.meses_ext, width=120, font=("Arial", 15))
        self.combo_mes.pack(side="left", padx=5); self.combo_mes.set("Todos")

        ctk.CTkLabel(self.filter_frame, text="Métrica:", font=("Arial", 16, "bold"), text_color="#1E293B").pack(side="left", padx=(15, 5))
        self.combo_metrica = ctk.CTkComboBox(self.filter_frame, values=["Quantidade", "Valor Venda", "Lucro"], width=130, font=("Arial", 15))
        self.combo_metrica.pack(side="left", padx=5); self.combo_metrica.set("Quantidade")

        ctk.CTkLabel(self.filter_frame, text="Exibir:", font=("Arial", 16, "bold"), text_color="#1E293B").pack(side="left", padx=(15, 5))
        self.combo_limite = ctk.CTkComboBox(self.filter_frame, values=["Top 10", "Top 20", "Top 50", "Top 100"], width=110, font=("Arial", 15))
        self.combo_limite.pack(side="left", padx=5); self.combo_limite.set("Top 20")

        ctk.CTkLabel(self.filter_frame, text="Produto:", font=("Arial", 16, "bold"), text_color="#1E293B").pack(side="left", padx=(25, 5))
        self.txt_pesquisa = ctk.CTkEntry(self.filter_frame, placeholder_text="Filtrar por nome...", width=200, font=("Arial", 15))
        self.txt_pesquisa.pack(side="left", padx=5)

        btn_processar = ctk.CTkButton(self.filter_frame, text="🔍 Atualizar", command=self.carregar_dados, fg_color="#1E88E5", hover_color="#1565C0", width=110, font=("Arial", 13, "bold"))
        btn_processar.pack(side="left", padx=15)

        # Ajuste Colunas
        self.tree.configure(columns=("Rank", "Cod", "Desc", "Qtd", "Venda", "Lucro"))
        self.tree.heading("Rank", text="🏆 #"); self.tree.heading("Cod", text="🔑 Código"); self.tree.heading("Desc", text="📦 Produto"); self.tree.heading("Qtd", text="🛒 Qtd"); self.tree.heading("Venda", text="💰 Total Venda"); self.tree.heading("Lucro", text="📈 Lucro")
        self.tree.column("Rank", width=50, anchor="center"); self.tree.column("Cod", width=90, anchor="center"); self.tree.column("Desc", width=350); self.tree.column("Qtd", width=90, anchor="center"); self.tree.column("Venda", width=160, anchor="e"); self.tree.column("Lucro", width=150, anchor="e")

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
            where_clauses = ["c4.CRMovDta IS NOT NULL", "YEAR(c4.CRMovDta) != 9999", "c2.CRMov2Flag IN ('A', 'F')"]
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

    def exportar_excel(self):
        items = self.tree.get_children()
        from tkinter import messagebox
        if not items: messagebox.showwarning("Aviso", "Nenhum dado para exportar."); return
        try:
             columns = ["Rank", "Cod", "Desc", "Qtd", "Venda", "Lucro"]
             cols_titles = ["🏆 #", "🔑 Código", "📦 Produto", "🛒 Qtd", "💰 Total Venda", "📈 Lucro"]
             data = [self.tree.item(k)['values'] for k in items]
             import pandas as pd, tempfile, os
             df = pd.DataFrame(data, columns=cols_titles)
             
             # Totalização
             try:
                  sum_qtd = sum([float(str(r[3]).replace('.', '').replace(',', '.')) for r in data if len(r) > 3 and str(r[3]).strip()])
                  sum_venda = sum([float(str(r[4]).replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.')) for r in data if len(r) > 4 and str(r[4]).strip()])
                  sum_lucro = sum([float(str(r[5]).replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.')) for r in data if len(r) > 5 and str(r[5]).strip()])
                  def format_v(v): return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                  df.loc[len(df)] = ["TOTAL", f"({len(data)} regs)", "", f"{sum_qtd:,.0f}".replace(",", "."), format_v(sum_venda), format_v(sum_lucro)]
             except: pass

             filepath = os.path.join(tempfile.gettempdir(), "Analise_Produtos.xlsx")
             writer = pd.ExcelWriter(filepath, engine='openpyxl')
             df.to_excel(writer, index=False, sheet_name='Sheet1')
             worksheet = writer.sheets['Sheet1']
             for i, col in enumerate(df.columns):
                  max_len = max(df[col].astype(str).map(len).max(), len(str(col))) + 2
                  from openpyxl.utils import get_column_letter
                  worksheet.column_dimensions[get_column_letter(i+1)].width = max_len
             writer.close()
             os.startfile(filepath)
        except Exception as e: messagebox.showerror("Erro Excel", str(e))

    def exportar_pdf(self):
        items = self.tree.get_children()
        from tkinter import messagebox
        if not items: messagebox.showwarning("Aviso", "Nenhum dado para exportar."); return
        try:
             columns = ["Rank", "Cod", "Desc", "Qtd", "Venda", "Lucro"]
             cols_titles = ["🏆 #", "🔑 Código", "📦 Produto", "🛒 Qtd", "💰 Total Venda", "📈 Lucro"]
             data = [self.tree.item(k)['values'] for k in items]
             import tempfile, os
             filepath = os.path.join(tempfile.gettempdir(), "Analise_Produtos.pdf")
             import sys, subprocess
             try: import fpdf
             except: subprocess.run([sys.executable, "-m", "pip", "install", "fpdf"], capture_output=True); import fpdf
             pdf = fpdf.FPDF(); pdf.add_page(); pdf.set_font("Arial", 'B', 12); pdf.cell(190, 10, "ANALISE DE PRODUTOS", 0, 1, 'C'); pdf.ln(5)
             pdf.set_font("Arial", 'B', 7); num_cols = len(cols_titles); w_cols = [12, 18, 55, 18, 43, 44]
             for i, c in enumerate(cols_titles): 
                  c_str = str(c).encode('latin-1', 'replace').decode('latin-1')
                  pdf.cell(w_cols[i], 8, c_str, 1, 0, 'C')
             pdf.ln(8); pdf.set_font("Arial", '', 7)
             for r in data:
                  for i, val in enumerate(r): 
                       v_str = str(val)[:25].encode('latin-1', 'replace').decode('latin-1')
                       pdf.cell(w_cols[i], 7, v_str, 1, 0, 'C' if i != 2 else 'L')
                  pdf.ln(7)
             
             # Totalização PDF
             try:
                  sum_qtd = sum([float(str(r[3]).replace('.', '').replace(',', '.')) for r in data if len(r) > 3 and str(r[3]).strip()])
                  sum_venda = sum([float(str(r[4]).replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.')) for r in data if len(r) > 4 and str(r[4]).strip()])
                  sum_lucro = sum([float(str(r[5]).replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.')) for r in data if len(r) > 5 and str(r[5]).strip()])
                  def format_v(v): return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                  pdf.ln(2); pdf.set_font("Arial", 'B', 7)
                  pdf.cell(w_cols[0]+w_cols[1]+w_cols[2], 8, f"TOTAL ({len(data)} Registros)", 1, 0, 'R')
                  pdf.cell(w_cols[3], 8, f"{sum_qtd:,.0f}".replace(",", "."), 1, 0, 'C')
                  pdf.cell(w_cols[4], 8, format_v(sum_venda), 1, 0, 'C')
                  pdf.cell(w_cols[5], 8, format_v(sum_lucro), 1, 1, 'C')
             except: pass

             pdf.ln(5); pdf.output(filepath); os.startfile(filepath)
        except Exception as e: messagebox.showerror("Erro PDF", str(e))

    def fechar_tela(self):
         self.pack_forget()
         if hasattr(self, 'hub') and hasattr(self.hub, 'modules_frame'):
              self.hub.modules_frame.pack(fill="both", expand=True, padx=30, pady=30)
         self.destroy()


# [Bloco __main__ movido para o final definitivo do arquivo]




class ResumoClienteWindow(BaseWindow):
    def __init__(self, parent, config):
        super().__init__(parent, "Análise de Vendas por Cliente", "RESUMO_CLI")
        self.config_db = config

        # Filtros (Alinhados à esquerda e transparentes)
        self.filter_frame = ctk.CTkFrame(self.top_frame, fg_color="transparent")
        self.filter_frame.pack(side="left", padx=20, pady=(0, 5), anchor="w")


        ctk.CTkLabel(self.filter_frame, text="Ano:", font=("Arial", 16, "bold"), text_color="#1E293B").pack(side="left", padx=(10, 5))
        self.combo_ano = ctk.CTkComboBox(self.filter_frame, values=["Todos"], width=90, font=("Arial", 15))
        self.combo_ano.pack(side="left", padx=5)
        self.combo_ano.set("Todos")

        ctk.CTkLabel(self.filter_frame, text="Mês:", font=("Arial", 16, "bold"), text_color="#1E293B").pack(side="left", padx=(15, 5))
        self.combo_mes = ctk.CTkComboBox(self.filter_frame, values=["Todos", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"], width=130, font=("Arial", 15))
        self.combo_mes.pack(side="left", padx=5)
        self.combo_mes.set("Todos")

        ctk.CTkLabel(self.filter_frame, text="Listagem:", font=("Arial", 16, "bold"), text_color="#1E293B").pack(side="left", padx=(15, 5))
        self.combo_top = ctk.CTkComboBox(self.filter_frame, values=["Top 10", "Top 20", "Top 50", "Top 100", "Todos"], width=110, font=("Arial", 15))
        self.combo_top.pack(side="left", padx=5)
        self.combo_top.set("Top 20")

        btn_processar = ctk.CTkButton(self.filter_frame, text="⚙️ Processar", command=self.carregar_dados, fg_color="#1E88E5", hover_color="#1565C0", width=120, font=("Arial", 13, "bold"))
        btn_processar.pack(side="right", padx=15)


        # Ajuste Colunas
        self.tree.configure(columns=("Rank", "Cod", "Nome", "Valor", "Percent"))
        self.tree.heading("Rank", text="#"); self.tree.heading("Cod", text="Cód Cliente"); self.tree.heading("Nome", text="Nome do Cliente"); self.tree.heading("Valor", text="Total Faturado"); self.tree.heading("Percent", text="% Particip.")
        self.tree.column("Rank", width=50, anchor="center"); self.tree.column("Cod", width=90, anchor="center"); self.tree.column("Nome", width=380); self.tree.column("Valor", width=160, anchor="e"); self.tree.column("Percent", width=110, anchor="center")

        self.after(200, self.carregar_anos)

    def carregar_anos(self):
        try:
            import pyodbc; import pandas as pd
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config_db['servidor']};DATABASE={self.config_db['banco']};UID={self.config_db['usuario_bd']};PWD={self.config_db['senha_bd']}"
            conn = pyodbc.connect(conn_str)
            df_anos = pd.read_sql("SELECT DISTINCT YEAR(CRMovDta) as Ano FROM crmov2 WHERE CRMovDta IS NOT NULL AND YEAR(CRMovDta) != 9999", conn)
            anos = sorted(df_anos['Ano'].dropna().unique().tolist(), reverse=True)
            self.combo_ano.configure(values=["Todos"] + [str(int(a)) for a in anos])
            self.combo_ano.set("Todos")
        except: pass

    def carregar_dados(self):
        try:
            import pyodbc
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config_db['servidor']};DATABASE={self.config_db['banco']};UID={self.config_db['usuario_bd']};PWD={self.config_db['senha_bd']}"
            conn = pyodbc.connect(conn_str); cursor = conn.cursor()

            ano = self.combo_ano.get()
            mes = self.combo_mes.get()
            top = self.combo_top.get()

            limit = ""
            if top.startswith("Top"): limit = f"TOP {top.replace('Top ', '')} "

            where_clauses = ["CRMov2Flag IN ('A', 'F')", "CRMovDta IS NOT NULL", "YEAR(CRMovDta) != 9999"]
            if ano != "Todos": where_clauses.append(f"YEAR(CRMovDta) = {int(ano)}")
            if mes != "Todos": 
                meses_ext = ["Todos", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
                try: mes_idx = meses_ext.index(mes); where_clauses.append(f"MONTH(CRMovDta) = {mes_idx}")
                except: pass

            where_str = " AND ".join(where_clauses)

            # Query para calcular % Total Geral (sem limite de TOP)
            cursor.execute(f"SELECT SUM(CRMov2VlrO) FROM crmov2 WHERE {where_str}")
            total_g_v = cursor.fetchone()[0]; total_geral = float(total_g_v) if total_g_v else 0.0

            query = f"""
                SELECT {limit}
                    CRMov2CodC, CRMov2DesC, SUM(CRMov2VlrO) as Valor
                FROM crmov2
                WHERE {where_str} AND CRMov2CodC NOT IN (1)
                GROUP BY CRMov2CodC, CRMov2DesC
                ORDER BY Valor DESC
            """
            cursor.execute(query)
            rows = cursor.fetchall(); conn.close()

            for item in self.tree.get_children(): self.tree.delete(item)
            if not rows: return

            for idx, r_item in enumerate(rows):
                cod_c = str(int(r_item[0])) if r_item[0] is not None else "0"
                nome = str(r_item[1]).strip() if r_item[1] else "Desconhecido"
                valor = float(r_item[2]) if r_item[2] else 0.0
                percent = (valor / total_geral * 100) if total_geral > 0 else 0

                v_f = f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                p_f = f"{percent:.1f} %"

                tag = 'even' if idx % 2 == 0 else 'odd'
                self.tree.insert("", "end", values=(idx + 1, cod_c, nome, v_f, p_f), tags=(tag,))
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erro Carregar Clientes", f"Não foi possível listar os clientes:\n\n{str(e)}")

class ClientesPararamWindow(BaseWindow):
    def __init__(self, parent, config):
        super().__init__(parent, "Clientes Inativos", "CLI_INATIVOS")
        self.config_db = config
        self.emp_fil_cache = {} # Cache para armazenar (emp, fil) por item_id da treeview

        # Filtros (Alinhados à esquerda e transparentes)
        self.filter_frame = ctk.CTkFrame(self.top_frame, fg_color="transparent")
        self.filter_frame.pack(side="left", padx=20, pady=(0, 5), anchor="w")


        ctk.CTkLabel(self.filter_frame, text="Inativo Há:", font=("Arial", 16, "bold"), text_color="#1E293B").pack(side="left", padx=(10, 5))
        self.combo_dias = ctk.CTkComboBox(self.filter_frame, values=["30 dias", "60 dias", "90 dias", "180 dias", "365 dias"], width=120, font=("Arial", 15))
        self.combo_dias.pack(side="left", padx=5); self.combo_dias.set("90 dias")

        self.entry_busca = ctk.CTkEntry(self.filter_frame, placeholder_text="Filtrar por nome...", width=220, font=("Arial", 15))
        self.entry_busca.pack(side="left", padx=10)
        self.entry_busca.bind("<KeyRelease>", self.filtrar_grid)

        btn_processar = ctk.CTkButton(self.filter_frame, text="⚙️ Processar", command=self.carregar_dados, fg_color="#1E88E5", hover_color="#1565C0", width=120, font=("Arial", 13, "bold"))
        btn_processar.pack(side="right", padx=15)


        # Ajuste Colunas
        self.tree.configure(columns=("Rank", "Cod", "Nome", "Ultima_Compra", "Dias", "Media", "Contatos"))
        self.tree.heading("Rank", text="#", command=lambda: self.sort_column("Rank", False))
        self.tree.heading("Cod", text="Cód Cliente", command=lambda: self.sort_column("Cod", False))
        self.tree.heading("Nome", text="Nome do Cliente", command=lambda: self.sort_column("Nome", False))
        self.tree.heading("Ultima_Compra", text="Última Compra", command=lambda: self.sort_column("Ultima_Compra", False))
        self.tree.heading("Dias", text="Dias Inativo", command=lambda: self.sort_column("Dias", False))
        self.tree.heading("Media", text="Média/Ano", command=lambda: self.sort_column("Media", False))
        self.tree.heading("Contatos", text="Telefones")
        
        self.tree.column("Rank", width=40, anchor="center"); self.tree.column("Cod", width=80, anchor="center"); self.tree.column("Nome", width=280); self.tree.column("Ultima_Compra", width=110, anchor="center"); self.tree.column("Dias", width=100, anchor="center"); self.tree.column("Media", width=130, anchor="e"); self.tree.column("Contatos", width=110, anchor="center")

        # Clique para ver Telefones
        self.tree.bind("<ButtonRelease-1>", self.on_click_item)

        # Botões de Exportação
        self.btn_exp_excel = ctk.CTkButton(self.bottom_bar, text="📊 Excel", command=self.exportar_excel, fg_color="#43A047", hover_color="#2E7D32", width=90)
        self.btn_exp_excel.pack(side="right", padx=(5, 20), pady=5)
        
        self.btn_exp_pdf = ctk.CTkButton(self.bottom_bar, text="📄 PDF", command=self.exportar_pdf, fg_color="#E53935", hover_color="#B71C1C", width=90)
        self.btn_exp_pdf.pack(side="right", padx=5, pady=5)

        self.after(200, self.carregar_dados)

    def on_click_item(self, event):
        item_id = self.tree.identify_row(event.y)
        col_id = self.tree.identify_column(event.x)
        if item_id and col_id == "#7": # Coluna 'Contatos' é a index 7
            self.abrir_telefones(item_id)

    def abrir_telefones(self, item_id):
        values = self.tree.item(item_id, "values")
        if not values: return
        cod_c = values[1]
        nome_c = values[2]
        emp, fil = self.emp_fil_cache.get(item_id, (1, 1))

        janela = ctk.CTkToplevel(self)
        janela.title(f"Telefones de do Cliente {cod_c}")
        janela.geometry("380x320")
        centralizar_tela(janela, 380, 320)
        janela.grab_set()

        ctk.CTkLabel(janela, text=f"👤 {nome_c}", font=("Arial", 14, "bold"), text_color="#1E88E5").pack(pady=(15, 10))
        
        cont_frame = ctk.CTkFrame(janela, fg_color="#F8FAFC", corner_radius=10)
        cont_frame.pack(padx=20, pady=10, fill="both", expand=True)

        try:
            import pyodbc
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config_db['servidor']};DATABASE={self.config_db['banco']};UID={self.config_db['usuario_bd']};PWD={self.config_db['senha_bd']}"
            conn = pyodbc.connect(conn_str); cursor = conn.cursor()
            
            query = "SELECT CRCliTel1, CRCliTel2, CRCliTel3, CRCliTel4, CRCliCon FROM crcli WHERE cmempcod = ? AND crclicod = ?"
            cursor.execute(query, (emp, cod_c))
            row = cursor.fetchone(); conn.close()

            if row:
                fones = [str(f).strip() for f in row[:4] if f and str(f).strip()]
                contato = str(row[4]).strip() if row[4] else ""

                if fones:
                    ctk.CTkLabel(cont_frame, text="📞 Ligações / WhatsApp:", font=("Arial", 12, "bold"), text_color="#1E293B").pack(pady=(10, 5))
                    for f in fones:
                        ctk.CTkLabel(cont_frame, text=f"📱 {f}", font=("Arial", 13)).pack(pady=2)
                else:
                    ctk.CTkLabel(cont_frame, text="Nenhum número encontrado.", text_color="gray").pack(pady=20)

                if contato:
                    ctk.CTkLabel(cont_frame, text="🙋‍♂️ Pessoa de Contato:", font=("Arial", 12, "bold"), text_color="#1E293B").pack(pady=(15, 2))
                    ctk.CTkLabel(cont_frame, text=contato, font=("Arial", 13, "italic")).pack()
            else:
                ctk.CTkLabel(cont_frame, text="Cliente não encontrado na CrCli.", text_color="red").pack(pady=30)
        except Exception as e:
            ctk.CTkLabel(cont_frame, text=f"Erro de Busca:\n{str(e)}", text_color="red", wraplength=300).pack(pady=20)

    def sort_column(self, col, reverse):
        l = [(self.tree.set(k, col), k) for k in self.tree.get_children('')]
        def try_convert(x):
            if col in ["Nome", "Contatos"]:
                return str(x[0]).casefold()
            try: return float(x[0].replace('R$ ', '').replace('.', '').replace(',', '.'))
            except: 
                try: return int(x[0].replace(' dias', ''))
                except: return str(x[0]).casefold()

        l.sort(key=try_convert, reverse=reverse)
        for index, (val, k) in enumerate(l):
            self.tree.move(k, '', index)
            self.tree.set(k, "Rank", index + 1)
        self.tree.heading(col, command=lambda: self.sort_column(col, not reverse))

    def filtrar_grid(self, event=None):
        busca = self.entry_busca.get().strip().upper()
        for item in self.tree.get_children(): self.tree.delete(item)
        if not hasattr(self, 'rows_cache'): return

        self.emp_fil_cache.clear()
        idx_count = 1
        for r_item in self.rows_cache:
            nome = str(r_item[1]).strip().upper()
            if busca and busca not in nome: continue

            cod_c = str(int(r_item[0])) if r_item[0] is not None else "0"
            dta_compra = r_item[2].strftime('%d/%m/%Y') if r_item[2] else "S/ Data"
            dias = int(r_item[3]) if r_item[3] is not None else 0
            media = int(round(float(r_item[4]))) if r_item[4] else 0

            v_f = f"R$ {media:,}".replace(",", ".")
            tag = 'even' if idx_count % 2 == 0 else 'odd'
            
            node_id = self.tree.insert("", "end", values=(idx_count, cod_c, r_item[1].strip(), dta_compra, f"{dias} dias", v_f, "📞 Ver"), tags=(tag,))
            
            # Cache de emp, fil associado ao node_id exato (Incluído contato e tels)
            tels = [r_item[7], r_item[8], r_item[9], r_item[10]]
            tels_str = " / ".join([str(t).strip() for t in tels if t and str(t).strip()])
            contato = str(r_item[11]).strip() if r_item[11] else ""

            self.emp_fil_cache[node_id] = (r_item[5], r_item[6], tels_str, contato) # Salva dados de contato
            idx_count += 1

    def carregar_dados(self):
        try:
            import pyodbc
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config_db['servidor']};DATABASE={self.config_db['banco']};UID={self.config_db['usuario_bd']};PWD={self.config_db['senha_bd']}"
            conn = pyodbc.connect(conn_str); cursor = conn.cursor()

            dias_inativo = int(self.combo_dias.get().replace(" dias", ""))

            query = f"""
                SELECT 
                    c2.CRMov2CodC, c2.CRMov2DesC, MAX(c2.CRMovDta) as UltimaCompra,
                    DATEDIFF(day, MAX(c2.CRMovDta), GETDATE()) as DiasInativo,
                    SUM(CASE WHEN YEAR(c2.CRMovDta) >= YEAR(GETDATE()) - 1 THEN c2.CRMov2VlrO ELSE 0 END) / 2.0 as MediaAno,
                    MAX(c2.cmempcod) as Emp, MAX(c2.cmfilcod) as Fil,
                    MAX(cli.CRCliTel1) as Tel1, MAX(cli.CRCliTel2) as Tel2, MAX(cli.CRCliTel3) as Tel3, MAX(cli.CRCliTel4) as Tel4, MAX(cli.CRCliCon) as Contato
                FROM crmov2 c2
                LEFT JOIN crcli cli ON c2.cmempcod = cli.cmempcod AND c2.CRMov2CodC = cli.crclicod
                WHERE c2.CRMov2Flag IN ('A', 'F') AND c2.CRMov2CodC NOT IN (1)
                GROUP BY c2.CRMov2CodC, c2.CRMov2DesC
                HAVING MAX(c2.CRMovDta) <= DATEADD(day, -{dias_inativo}, GETDATE())
                ORDER BY MediaAno DESC
            """
            cursor.execute(query)
            self.rows_cache = cursor.fetchall(); conn.close()
            self.filtrar_grid()
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erro Carregar Inativos", f"Não foi possível listar os clientes inativos:\n\n{str(e)}")

    def exportar_excel(self):
        items = self.tree.get_children()
        from tkinter import messagebox, filedialog
        if not items:
            messagebox.showwarning("Aviso", "Nenhum dado para exportar.")
            return

        try:
            cols = ["#", "Cod", "Nome", "Última Compra", "Dias", "Média/Ano", "Telefones", "Contato"]
            data = []
            for k in items:
                 v = self.tree.item(k)['values']
                 cache_item = self.emp_fil_cache.get(k, ("", "", "", ""))
                 tels = cache_item[2] if len(cache_item) > 2 else ""
                 contato = cache_item[3] if len(cache_item) > 3 else ""
                 
                 v_0 = str(v[0]) if len(v) > 0 else ""
                 v_1 = str(v[1]) if len(v) > 1 else ""
                 v_2 = str(v[2]) if len(v) > 2 else ""
                 v_3 = str(v[3]) if len(v) > 3 else ""
                 v_4 = str(v[4]) if len(v) > 4 else ""
                 v_5 = str(v[5]) if len(v) > 5 else ""

                 data.append([v_0, v_1, v_2, v_3, v_4, v_5, tels, contato])
            import pandas as pd
            df = pd.DataFrame(data, columns=cols)
            filepath = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")], title="Salvar Excel", initialfile="Clientes_Inativos.xlsx")
            if filepath:
                 df.to_excel(filepath, index=False)
                 messagebox.showinfo("Sucesso", f"Excel salvo com sucesso em:\n\n{filepath}")
        except Exception as e:
             messagebox.showerror("Erro Excel", str(e))

    def exportar_pdf(self):
        items = self.tree.get_children()
        from tkinter import messagebox
        if not items:
            messagebox.showwarning("Aviso", "Nenhum dado para exportar.")
            return

        try:
             cols = ["#", "Cod", "Nome", "Ult Cmp", "Dias", "Média \\ Anual", "Telefones"]
             data = []
             for k in items:
                  v = self.tree.item(k)['values']
                  cache_item = self.emp_fil_cache.get(k, ("", "", "", ""))
                  tels = cache_item[2] if len(cache_item) > 2 else ""
                  
                  v_0 = str(v[0]) if len(v) > 0 else ""
                  v_1 = str(v[1]) if len(v) > 1 else ""
                  v_2 = str(v[2])[:25] if len(v) > 2 else ""
                  v_3 = str(v[3]) if len(v) > 3 else ""
                  v_4 = str(v[4]) if len(v) > 4 else ""
                  v_5 = str(v[5]) if len(v) > 5 else ""

                  data.append([v_0, v_1, v_2, v_3, v_4, v_5, tels[:35]])
             import tempfile, os
             filepath = os.path.join(tempfile.gettempdir(), "Clientes_Inativos.pdf")

             import sys, subprocess
             try: import fpdf
             except: 
                 subprocess.run([sys.executable, "-m", "pip", "install", "fpdf"], capture_output=True)
                 import fpdf

             pdf = fpdf.FPDF(orientation='L') 
             pdf.add_page()
             pdf.set_font("Arial", 'B', 14)
             pdf.cell(280, 10, "RELATORIO DE CLIENTES INATIVOS", 0, 1, 'C')
             pdf.ln(5)

             pdf.set_font("Arial", 'B', 10)
             w_cols = [10, 15, 55, 25, 25, 40, 110]
             for i, c in enumerate(cols):
                  pdf.cell(w_cols[i], 8, c, 1, 0, 'C')
             pdf.ln(8)

             pdf.set_font("Arial", '', 9)
             for r in data:
                  f_0 = str(r[0]).encode('latin-1', 'replace').decode('latin-1')
                  f_1 = str(r[1]).encode('latin-1', 'replace').decode('latin-1')
                  f_2 = str(r[2]).encode('latin-1', 'replace').decode('latin-1')
                  f_3 = str(r[3]).encode('latin-1', 'replace').decode('latin-1')
                  f_4 = str(r[4]).encode('latin-1', 'replace').decode('latin-1')
                  f_5 = str(r[5]).encode('latin-1', 'replace').decode('latin-1')
                  f_6 = str(r[6]).encode('latin-1', 'replace').decode('latin-1')
                  
                  pdf.cell(w_cols[0], 7, f_0, 1, 0, 'C')
                  pdf.cell(w_cols[1], 7, f_1, 1, 0, 'C')
                  pdf.cell(w_cols[2], 7, f_2, 1, 0, 'L')
                  pdf.cell(w_cols[3], 7, f_3, 1, 0, 'C')
                  pdf.cell(w_cols[4], 7, f_4, 1, 0, 'C')
                  pdf.cell(w_cols[5], 7, f_5, 1, 0, 'R')
                  pdf.cell(w_cols[6], 7, f_6, 1, 1, 'L')

             pdf.output(filepath)
             os.startfile(filepath)
        except Exception as e:
             messagebox.showerror("Erro PDF", str(e))

class SugestaoCompraWindow(BaseWindow):
    def __init__(self, parent, config):
        super().__init__(parent, "Sugestão de Compra", "SUGESTAO_COMPRA")
        self.config_db = config

        # Barra de Filtros (Alinhada à esquerda e transparente)
        self.filter_frame = ctk.CTkFrame(self.top_frame, fg_color="transparent")
        self.filter_frame.pack(side="top", fill="x", padx=20, pady=0, anchor="w")




        ctk.CTkLabel(self.filter_frame, text="Demanda para:", font=("Arial", 14, "bold"), text_color="#1E293B").pack(side="left", padx=(10, 5))
        self.combo_dias = ctk.CTkComboBox(self.filter_frame, values=["10 dias", "20 dias", "30 dias"], width=110, font=("Arial", 14))
        self.combo_dias.pack(side="left", padx=5); self.combo_dias.set("30 dias")

        ctk.CTkLabel(self.filter_frame, text="Grupo:", font=("Arial", 14, "bold"), text_color="#1E293B").pack(side="left", padx=(10, 5))
        self.combo_grupo = ctk.CTkComboBox(self.filter_frame, width=150, font=("Arial", 14), command=self.selecionar_grupo)
        self.combo_grupo.pack(side="left", padx=5)

        ctk.CTkLabel(self.filter_frame, text="Sub:", font=("Arial", 14, "bold"), text_color="#1E293B").pack(side="left", padx=(10, 5))
        self.combo_subgrupo = ctk.CTkComboBox(self.filter_frame, width=150, font=("Arial", 14), command=self.selecionar_subgrupo)
        self.combo_subgrupo.pack(side="left", padx=5)

        self.entry_busca = ctk.CTkEntry(self.filter_frame, placeholder_text="Filtrar...", width=140, font=("Arial", 14))
        self.entry_busca.pack(side="left", padx=10)
        self.entry_busca.bind("<KeyRelease>", self.filtrar_grid)

        btn_processar = ctk.CTkButton(self.filter_frame, text="⚙️ Processar", command=self.carregar_dados, fg_color="#1E88E5", hover_color="#1565C0", width=110, font=("Arial", 13, "bold"))
        btn_processar.pack(side="left", padx=10, pady=2)

        # Linha inferior para filtros adicionais
        self.check_frame = ctk.CTkFrame(self.top_frame, fg_color="transparent")
        self.check_frame.pack(side="top", fill="x", padx=20, pady=(0, 5), anchor="w")

        self.check_somente_compra = ctk.CTkCheckBox(self.check_frame, text="Mostrar Somente os que Precisam de Repor o Estoque", font=("Arial", 15, "bold"), text_color="#C62828", fg_color="#C62828", border_color="#B71C1C", hover_color="#EF9A9A", command=self.filtrar_grid)
        self.check_somente_compra.pack(side="left", padx=10)


        # Frame de Tags (Filtros Ativos) - Começa com altura 0 para não criar espaço vago
        self.tags_frame = ctk.CTkFrame(self.top_frame, fg_color="transparent", height=0)
        self.tags_frame.pack(side="top", fill="x", padx=30, pady=0)
        
        # Ajuste para o grid colar no cabeçalho sem nenhum espaço vago
        self.grid_frame.grid_configure(pady=0)





        columns = ("Rank", "Cod", "Produto", "Estoque", "Vendas3M", "MediaDia", "Demanda", "Sugestao")
        self.tree.configure(columns=columns)
        self.tree.heading("Rank", text="#")
        self.tree.heading("Cod", text="Código")
        self.tree.heading("Produto", text="Produto")
        self.tree.heading("Estoque", text="Estoque")
        self.tree.heading("Vendas3M", text="Vend 90d")
        self.tree.heading("MediaDia", text="Média/Dia")
        self.tree.heading("Demanda", text="Demanda")
        self.tree.heading("Sugestao", text="Sugestão")

        w_col = [40, 75, 230, 95, 95, 95, 95, 110]
        for i, c in enumerate(columns):
             self.tree.column(c, width=w_col[i], anchor="center" if c != "Produto" else "w")

        self.grupos_selecionados = {}
        self.subgrupos_selecionados = {}
        self.rows_cache = []
        self.after(100, self.carregar_combos_filtros)
        self.after(300, self.carregar_dados)

    def carregar_dados(self):
        try:
            import pyodbc
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config_db['servidor']};DATABASE={self.config_db['banco']};UID={self.config_db['usuario_bd']};PWD={self.config_db['senha_bd']}"
            conn = pyodbc.connect(conn_str); cursor = conn.cursor()

            where_grp = f"p.cegrpcod IN ({','.join(self.grupos_selecionados.keys())})" if self.grupos_selecionados else "1=1"
            where_sgr = f"p.cesgrcod IN ({','.join(self.subgrupos_selecionados.keys())})" if self.subgrupos_selecionados else "1=1"

            query = f"""
                SELECT 
                    p.ceprocod, 
                    p.CEProDes, 
                    ISNULL(SUM(f.ceprofqtda), 0) as Estoque, 
                    ISNULL(SUM(c4.CRMov4Qtd), 0) as Vendas3M
                FROM cepro p
                LEFT JOIN ceprof f ON p.ceprocod = f.ceprocod
                LEFT JOIN crmov4 c4 ON p.ceprocod = c4.CEProCod
                LEFT JOIN crmov2 c2 ON c4.CMEmpCod = c2.CMEmpCod AND c4.CMFilCod = c2.CMFilCod AND c4.CRMovDta = c2.CRMovDta AND c4.CRMovSeq = c2.CRMovSeq
                    AND c2.CRMovDta >= DATEADD(day, -90, GETDATE()) AND c2.CRMov2Flag IN ('A', 'F')
                WHERE {where_grp} AND {where_sgr}
                GROUP BY p.ceprocod, p.CEProDes
                HAVING ISNULL(SUM(c4.CRMov4Qtd), 0) > 0 OR ISNULL(SUM(f.ceprofqtda), 0) > 0
                ORDER BY p.CEProDes
            """
            cursor.execute(query)
            self.rows_cache = cursor.fetchall(); conn.close()
            self.filtrar_grid()
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erro Dados", f"Erro no agrupamento:\n{str(e)}")

    def filtrar_grid(self, event=None):
        search = self.entry_busca.get().casefold()
        for i in self.tree.get_children(): self.tree.delete(i)
        
        dias_filtro = int(self.combo_dias.get().replace(" dias", ""))
        idx_count = 1

        for r in self.rows_cache:
            des = str(r[1]).strip()
            if search and search not in des.casefold() and str(r[0]) not in search: continue

            est = float(r[2]); vendas = float(r[3])
            media = vendas / 90.0
            demanda = media * dias_filtro
            sug = demanda - est
            if sug < 0: sug = 0

            if hasattr(self, 'check_somente_compra') and self.check_somente_compra.get() and sug <= 0:
                continue

            v_est = f"{int(est)}" if est.is_integer() else f"{est:.2f}"
            v_vend = f"{int(vendas)}" if vendas.is_integer() else f"{vendas:.2f}"
            
            zebra = 'even' if idx_count % 2 == 0 else 'odd'
            tags = ('alerta',) if sug > 0 else (zebra,)
            self.tree.insert("", "end", values=(idx_count, r[0], des, v_est, v_vend, f"{media:.2f}", f"{demanda:.1f}", f"{sug:.1f}"), tags=tags)
            idx_count += 1
        self.tree.tag_configure('alerta', background='#FFEBEE')

    def carregar_combos_filtros(self):
        try:
            import pyodbc
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config_db['servidor']};DATABASE={self.config_db['banco']};UID={self.config_db['usuario_bd']};PWD={self.config_db['senha_bd']}"
            with pyodbc.connect(conn_str) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT CEGrpCod, CEGrpDes FROM CEGrp ORDER BY CEGrpDes")
                valores_g = ["Todos"] + [f"{int(r[0])} - {str(r[1]).strip()}" for r in cursor.fetchall() if r[1]]
                self.combo_grupo.configure(values=valores_g)
                self.combo_grupo.set("Todos")
        except: pass

    def selecionar_grupo(self, valor):
        if valor == "Todos": return
        g_id = valor.split(" - ")[0]
        g_nome = valor.split(" - ")[1]
        self.grupos_selecionados[g_id] = g_nome
        self.renderizar_tags()
        self.combo_grupo.set("Todos")
        try:
            import pyodbc
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config_db['servidor']};DATABASE={self.config_db['banco']};UID={self.config_db['usuario_bd']};PWD={self.config_db['senha_bd']}"
            with pyodbc.connect(conn_str) as conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT CESgrCod, CESgrDes FROM CESgr WHERE CEGrpCod = {g_id} ORDER BY CESgrDes")
                valores_s = ["Todos"] + [f"{int(r[0])} - {str(r[1]).strip()}" for r in cursor.fetchall() if r[1]]
                self.combo_subgrupo.configure(values=valores_s)
                self.combo_subgrupo.set("Todos")
        except: pass

    def selecionar_subgrupo(self, valor):
        if valor == "Todos": return
        s_id = valor.split(" - ")[0]
        s_nome = valor.split(" - ")[1]
        self.subgrupos_selecionados[s_id] = s_nome
        self.renderizar_tags()
        self.combo_subgrupo.set("Todos")

    def renderizar_tags(self):
        for w in self.tags_frame.winfo_children(): w.destroy()
        for k, v in self.grupos_selecionados.items():
            f = ctk.CTkFrame(self.tags_frame, fg_color="#E3F2FD", corner_radius=5, height=25)
            f.pack(side="left", padx=3)
            ctk.CTkLabel(f, text=f"📁 {v}", font=("Arial", 11), text_color="#1565C0").pack(side="left", padx=(8, 4))
            ctk.CTkButton(f, text="×", width=18, height=18, fg_color="transparent", text_color="#C62828", hover_color="#FFCDD2", command=lambda key=k: self.remover_grupo(key)).pack(side="left", padx=(0, 4))
        for k, v in self.subgrupos_selecionados.items():
            f = ctk.CTkFrame(self.tags_frame, fg_color="#E8F5E9", corner_radius=5, height=25)
            f.pack(side="left", padx=3)
            ctk.CTkLabel(f, text=f"📄 {v}", font=("Arial", 11), text_color="#2E7D32").pack(side="left", padx=(8, 4))
            ctk.CTkButton(f, text="×", width=18, height=18, fg_color="transparent", text_color="#C62828", hover_color="#FFCDD2", command=lambda key=k: self.remover_subgrupo(key)).pack(side="left", padx=(0, 4))

    def remover_grupo(self, key):
        if key in self.grupos_selecionados: del self.grupos_selecionados[key]
        self.renderizar_tags()

    def remover_subgrupo(self, key):
        if key in self.subgrupos_selecionados: del self.subgrupos_selecionados[key]
        self.renderizar_tags()

class PosicaoContasReceberWindow(BaseWindow):
    def __init__(self, parent, config):
        super().__init__(parent, "Posição de Vendas", "POS_VENDAS")
        self.config_db = config

        # Barra de Filtros (Alinhada à esquerda e transparente)
        self.filter_frame = ctk.CTkFrame(self.top_frame, fg_color="transparent")
        self.filter_frame.pack(side="left", padx=20, pady=(0, 5), anchor="w")


        ctk.CTkLabel(self.filter_frame, text="Ano:", font=("Arial", 16, "bold"), text_color="#1E293B").pack(side="left", padx=(10, 5))
        self.combo_ano = ctk.CTkComboBox(self.filter_frame, values=["Todos"], width=100, font=("Arial", 15))
        self.combo_ano.pack(side="left", padx=5); self.combo_ano.set("Todos")

        ctk.CTkLabel(self.filter_frame, text="Mês:", font=("Arial", 16, "bold"), text_color="#1E293B").pack(side="left", padx=(15, 5))
        self.meses_ext = ["Todos", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        self.combo_mes = ctk.CTkComboBox(self.filter_frame, values=self.meses_ext, width=130, font=("Arial", 15))
        self.combo_mes.pack(side="left", padx=5); self.combo_mes.set("Todos")

        ctk.CTkLabel(self.filter_frame, text="Visualização:", font=("Arial", 16, "bold"), text_color="#1E293B").pack(side="left", padx=(25, 5))
        self.seg_view = ctk.CTkSegmentedButton(self.filter_frame, values=["Tabela", "Gráfico"], command=self.alternar_visualizacao, width=170, font=("Arial", 13, "bold"))
        self.seg_view.pack(side="left", padx=5)
        self.seg_view.set("Tabela")

        btn_processar = ctk.CTkButton(self.filter_frame, text="⚙️ Processar", command=self.carregar_dados, fg_color="#1E88E5", hover_color="#1565C0", width=120, font=("Arial", 13, "bold"))
        btn_processar.pack(side="right", padx=15)


        # Ajuste Colunas
        self.tree.configure(columns=("Tipo", "Descricao", "Qtd", "Valor", "Percent"))
        self.tree.heading("Tipo", text="Cód Tipo"); self.tree.heading("Descricao", text="Tipo de Venda"); self.tree.heading("Qtd", text="Volume Notas"); self.tree.heading("Valor", text="Total Faturado"); self.tree.heading("Percent", text="% Particip.")
        self.tree.column("Tipo", width=80, anchor="center"); self.tree.column("Descricao", width=250); self.tree.column("Qtd", width=120, anchor="center"); self.tree.column("Valor", width=150, anchor="e"); self.tree.column("Percent", width=100, anchor="center")

        # Container para o Gráfico
        self.chart_frame = ctk.CTkFrame(self.grid_frame, fg_color="#FFFFFF")

        # Legenda
        self.legendas = { 1: "Vista", 2: "Crediário", 5: "Cartão", 13: "Pix" }
 
        # Label de Resumo de Cartão no Footer
        self.lbl_cartao = ctk.CTkLabel(self.grid_frame, text="", font=("Arial", 13, "bold"), text_color="#1E88E5", anchor="center")
        self.lbl_cartao.pack(side="bottom", fill="x", pady=5)
 
        self.after(200, self.carregar_anos)

    def alternar_visualizacao(self, valor):
        if valor == "Tabela":
            self.chart_frame.pack_forget()
            self.tree.pack(fill="both", expand=True, side="left")
        else:
            self.tree.pack_forget()
            self.chart_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def carregar_anos(self):
        server = self.config_db.get("servidor")
        database = self.config_db.get("banco")
        username = self.config_db.get("usuario_bd")
        password = self.config_db.get("senha_bd")
        
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"
        try:
            import pyodbc, pandas as pd
            conn = pyodbc.connect(conn_str)
            df_anos = pd.read_sql("SELECT DISTINCT YEAR(CRMovDta) as Ano FROM crmov2 WHERE CRMovDta IS NOT NULL AND YEAR(CRMovDta) != 9999", conn)
            conn.close()
            
            anos = sorted(df_anos['Ano'].dropna().unique().tolist(), reverse=True)
            self.combo_ano.configure(values=["Todos"] + [str(int(a)) for a in anos])
            self.combo_ano.set("Todos")
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erro Carregar Anos", f"Não foi possível listar os anos:\n\n{str(e)}")

    def carregar_dados(self):
        try:
            import pyodbc
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config_db['servidor']};DATABASE={self.config_db['banco']};UID={self.config_db['usuario_bd']};PWD={self.config_db['senha_bd']}"
            conn = pyodbc.connect(conn_str); cursor = conn.cursor()

            ano = self.combo_ano.get()
            mes = self.combo_mes.get()

            where_clauses = ["c.CRMov2Flag IN ('A', 'F')", "c.CRMovDta IS NOT NULL", "YEAR(c.CRMovDta) != 9999"]
            if ano != "Todos": where_clauses.append(f"YEAR(c.CRMovDta) = {int(ano)}")
            if mes != "Todos": 
                try: mes_idx = self.meses_ext.index(mes); where_clauses.append(f"MONTH(c.CRMovDta) = {mes_idx}")
                except: pass

            where_str = " AND ".join(where_clauses)
            query = f"""
                SELECT 
                    c.crmov2sit, 
                    r.CRCCrTip,
                    COUNT(*) as Qtd, 
                    SUM(c.CRMov2VlrO) as Valor
                FROM crmov2 c
                LEFT JOIN crccr r ON c.cmempcod = r.cmempcod 
                                AND c.cmfilcod = r.cmfilcod 
                                AND c.crccrcod = r.crccrcod
                WHERE {where_str}
                GROUP BY c.crmov2sit, r.CRCCrTip
            """
            cursor.execute(query)
            rows = cursor.fetchall(); conn.close()
 
            for item in self.tree.get_children(): self.tree.delete(item)
            for widget in self.chart_frame.winfo_children(): widget.destroy()
 
            if not rows: return
 
            # Agrupamento e Acumuladores em Python
            agrupado = {}
            v_debito = 0.0; v_credito = 0.0
            total_geral = 0.0
 
            for r_item in rows:
                sit = r_item[0] if r_item[0] is not None else 0
                tip = str(r_item[1]).strip().upper() if r_item[1] else ''
                qtd = int(r_item[2])
                vlr = float(r_item[3]) if r_item[3] else 0.0
 
                total_geral += vlr
                if sit not in agrupado: agrupado[sit] = {'qtd': 0, 'vlr': 0.0}
                agrupado[sit]['qtd'] += qtd
                agrupado[sit]['vlr'] += vlr
 
                if sit == 5:
                    if tip == 'D': v_debito += vlr
                    else: v_credito += vlr
 
            # Atualizar Label de Sumário de Cartão
            total_cart = v_debito + v_credito
            if total_cart > 0:
                p_deb = (v_debito / total_cart) * 100
                p_cre = (v_credito / total_cart) * 100
                resumo_txt = f"💳 DETALHAMENTO CARTÃO  ➔  Débito: R$ {int(round(v_debito)):,} ({int(round(p_deb))}%)  |  Crédito: R$ {int(round(v_credito)):,} ({int(round(p_cre))}%)".replace(",", ".")
                self.lbl_cartao.configure(text=resumo_txt)
            else: self.lbl_cartao.configure(text="")
 
            # Preparar linhas ordenadas para Grid e Grafico
            rows_proc = []
            for k, v in agrupado.items(): rows_proc.append((k, v['qtd'], v['vlr']))
            rows_proc = sorted(rows_proc, key=lambda x: x[2], reverse=True)
 
            for idx, row in enumerate(rows_proc):
                sit_cod = row[0]
                qtd = row[1]
                valor = row[2]
                percent = (valor / total_geral * 100) if total_geral > 0 else 0
                
                descricao = self.legendas.get(sit_cod, "Desconhecido")
                valor_f = f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                percent_f = f"{percent:.1f} %"
                
                tag = 'even' if idx % 2 == 0 else 'odd'
                self.tree.insert("", "end", values=(str(int(sit_cod)), descricao, f"{qtd:,}".replace(",", "."), valor_f, percent_f), tags=(tag,))

            # Renderizar Gráfico ( Se houver linhas )
            try:
                 import matplotlib.pyplot as plt
                 from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

                 labels = [self.legendas.get(row[0], "Desconhecido") for row in rows_proc]
                 valores = [float(row[2]) for row in rows_proc]
                 percentuais = [(v / total_geral * 100) if total_geral > 0 else 0 for v in valores]
 
                 fig, ax = plt.subplots(figsize=(8, 4))
                 bars = ax.bar(labels, valores, color="#1E88E5")
                 ax.set_title("Faturamento por Tipo de Venda", fontsize=12, fontweight="bold")
                 
                 def format_currency(x, pct): 
                     v_int = int(round(x))
                     p_int = int(round(pct))
                     return f"R$ {v_int:,}".replace(",", ".") + f" ({p_int}%)"
                 ax.bar_label(bars, labels=[format_currency(v, p) for v, p in zip(valores, percentuais)], padding=3, fontsize=8, fontweight="bold")

                 plt.xticks(rotation=25, ha='right', fontsize=9)
                 ax.spines['top'].set_visible(False)
                 ax.spines['right'].set_visible(False)
                 fig.tight_layout()

                 canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
                 canvas.draw()
                 canvas.get_tk_widget().pack(fill="both", expand=True)
                 plt.close(fig) # Liberar memoria
            except: pass

        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erro SQL", f"Erro ao processar dados:\n{e}")

class EstoqueParadoWindow(BaseWindow):
    def __init__(self, parent, config):
        super().__init__(parent, "Análise de Estoque Parado", "ESTOQUE_PARADO")
        self.config_db = config

        # Filtros (Alinhados à esquerda e transparentes)
        self.filter_frame = ctk.CTkFrame(self.top_frame, fg_color="transparent")
        self.filter_frame.pack(side="left", padx=20, pady=(0, 5), anchor="w")


        ctk.CTkLabel(self.filter_frame, text="Sem Giro Há:", font=("Arial", 16, "bold"), text_color="#1E293B").pack(side="left", padx=(10, 5))
        self.combo_dias = ctk.CTkComboBox(self.filter_frame, values=["30 dias", "60 dias", "90 dias", "180 dias", "365 dias"], width=120, font=("Arial", 15))
        self.combo_dias.pack(side="left", padx=5); self.combo_dias.set("90 dias")

        self.entry_busca = ctk.CTkEntry(self.filter_frame, placeholder_text="Filtrar produto...", width=220, font=("Arial", 15))
        self.entry_busca.pack(side="left", padx=15)

        btn_processar = ctk.CTkButton(self.filter_frame, text="⚙️ Processar", command=self.carregar_dados, fg_color="#1E88E5", hover_color="#1565C0", width=120, font=("Arial", 13, "bold"))
        btn_processar.pack(side="right", padx=15)



        # Ajuste Colunas
        self.tree.configure(columns=("Rank", "Cod", "Nome", "Ultima_Venda", "Estoque", "Custo", "Total"))
        self.tree.heading("Rank", text="#")
        self.tree.heading("Cod", text="Cód Produto")
        self.tree.heading("Nome", text="Descrição do Produto")
        self.tree.heading("Ultima_Venda", text="Última Venda", command=lambda: self.sort_column("Ultima_Venda", False))
        self.tree.heading("Estoque", text="Estoque", command=lambda: self.sort_column("Estoque", False))
        self.tree.heading("Custo", text="Custo Unit.")
        self.tree.heading("Total", text="Total Parado", command=lambda: self.sort_column("Total", False))
        
        self.tree.column("Rank", width=40, anchor="center"); self.tree.column("Cod", width=80, anchor="center"); self.tree.column("Nome", width=240); self.tree.column("Ultima_Venda", width=110, anchor="center"); self.tree.column("Estoque", width=90, anchor="center"); self.tree.column("Custo", width=100, anchor="e"); self.tree.column("Total", width=120, anchor="e")

        # Label de Alerta p/ Regras
        self.lbl_vazio = ctk.CTkLabel(self.grid_frame, text="Use o botão Processar para listar os produtos sem giro.", font=("Arial", 13, "italic"), text_color="gray")
        self.lbl_vazio.place(relx=0.5, rely=0.5, anchor="center")

        # Rodapé de Totais (Acopla no bottom_bar da BaseWindow)
        self.lbl_rodape_total = ctk.CTkLabel(self.bottom_bar, text="", font=("Arial", 13, "bold"), text_color="#1565C0")
        self.lbl_rodape_total.pack(side="left", padx=10)

        # Botões de Exportação
        self.btn_exp_excel = ctk.CTkButton(self.bottom_bar, text="📊 Excel", command=self.exportar_excel, fg_color="#43A047", hover_color="#2E7D32", width=90)
        self.btn_exp_excel.pack(side="right", padx=(5, 20), pady=5)
        
        self.btn_exp_pdf = ctk.CTkButton(self.bottom_bar, text="📄 PDF", command=self.exportar_pdf, fg_color="#E53935", hover_color="#B71C1C", width=90)
        self.btn_exp_pdf.pack(side="right", padx=5, pady=5)

    def sort_column(self, col, reverse):
        l = [(self.tree.set(k, col), k) for k in self.tree.get_children('')]
        def try_convert(x):
            try: return float(x[0].replace('R$ ', '').replace('.', '').replace(',', '.'))
            except: 
                try: return int(x[0].replace(' unid', ''))
                except: 
                     if "/" in x[0]: 
                         try: return "".join(reversed(x[0].split("/"))) # yyyymmdd
                         except: pass
                     return str(x[0]).casefold()

        l.sort(key=try_convert, reverse=reverse)
        for index, (val, k) in enumerate(l):
            self.tree.move(k, '', index)
            self.tree.set(k, "Rank", index + 1)
        self.tree.heading(col, command=lambda: self.sort_column(col, not reverse))

    def carregar_dados(self):
        try:
            import pyodbc
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config_db['servidor']};DATABASE={self.config_db['banco']};UID={self.config_db['usuario_bd']};PWD={self.config_db['senha_bd']}"
            conn = pyodbc.connect(conn_str); cursor = conn.cursor()

            dias = int(self.combo_dias.get().replace(" dias", ""))
            busca = self.entry_busca.get().strip().upper()

            query = f"""
                SELECT 
                    p.CEProCod, 
                    p.CEProDes, 
                    SUM(f.CEProFQtdA) as Estoque, 
                    p.CEProPreCu as Custo,
                    MAX(m.CRMovDta) as UltimaVenda
                FROM cepro p
                INNER JOIN ceprof f ON p.CEProCod = f.CEProCod
                LEFT JOIN crmov4 m ON p.CEProCod = m.CEProCod
                GROUP BY p.CEProCod, p.CEProDes, p.CEProPreCu
                HAVING SUM(f.CEProFQtdA) > 0 
                  AND (MAX(m.CRMovDta) <= DATEADD(day, -{dias}, GETDATE()) OR MAX(m.CRMovDta) IS NULL)
                ORDER BY (SUM(f.CEProFQtdA) * ISNULL(p.CEProPreCu, 0)) DESC
            """
            cursor.execute(query)
            rows = cursor.fetchall(); conn.close()

            self.lbl_vazio.place_forget()
            for item in self.tree.get_children(): self.tree.delete(item)

            if not rows: return

            total_parado_geral = 0.0
            total_linhas = 0

            idx_count = 1
            for r_item in rows:
                cod_p = str(int(r_item[0])) if r_item[0] is not None else "0"
                nome = str(r_item[1]).strip() if r_item[1] else "Desconhecido"
                if busca and busca not in nome.upper(): continue

                qtd = float(r_item[2]) if r_item[2] else 0.0
                custo = float(r_item[3]) if r_item[3] else 0.0
                total = qtd * custo
                
                total_parado_geral += total
                total_linhas += 1

                dta_venda = r_item[4].strftime('%d/%m/%Y') if r_item[4] else "Sem Venda"

                custo_int = int(round(custo))
                total_int = int(round(total))

                v_custo = f"R$ {custo_int:,}".replace(",", ".")
                v_total = f"R$ {total_int:,}".replace(",", ".")

                tag = 'even' if idx_count % 2 == 0 else 'odd'
                self.tree.insert("", "end", values=(idx_count, cod_p, nome, dta_venda, f"{int(qtd)} unid", v_custo, v_total), tags=(tag,))
                idx_count += 1

            tot_p_int = int(round(total_parado_geral))
            self.lbl_rodape_total.configure(text=f"📊 PRODUTOS: {total_linhas}  |  💰 TOTAL PARADO: R$ {tot_p_int:,}".replace(",", "."))

        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erro Carregar Estoque", f"Não foi possível listar o estoque parado:\n\n{str(e)}")

class AnaliseParcelasWindow(BaseWindow):
    def __init__(self, parent, config):
        super().__init__(parent, "Análise das Parcelas", "ANALISE_PARCELAS")
        self.config_db = config

        # Ocultar a Treeview da classe base (usada apenas no modal)
        self.tree.pack_forget()

        # Botão Processar na Top Bar
        self.btn_processar = ctk.CTkButton(self.top_frame, text="⚙️ Processar Gráfico", command=self.carregar_dados, fg_color="#1E88E5", hover_color="#1565C0", width=160, font=("Arial", 13, "bold"))
        self.btn_processar.pack(side="left", padx=20, pady=5)

        # Frame para o Gráfico
        self.chart_frame = ctk.CTkFrame(self.grid_frame, fg_color="white")
        self.chart_frame.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        # Configuração do Matplotlib
        self.fig = Figure(figsize=(10, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.chart_frame)
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

        # Evento de clique no gráfico
        self.canvas.mpl_connect('button_press_event', self.on_click)

        self.df_parcelas = None
        self.faixas_info = [] # Armazena range e label de cada barra
        self.bars = None

        self.after(100, self.carregar_dados)

    def carregar_dados(self):
        try:
            import pyodbc
            import pandas as pd
            from datetime import datetime

            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config_db['servidor']};DATABASE={self.config_db['banco']};UID={self.config_db['usuario_bd']};PWD={self.config_db['senha_bd']}"
            conn = pyodbc.connect(conn_str)
            
            # Query com JOIN para pegar dados do cliente e filtro de Flag 'A', excluindo CodC = 1
            query = """
                SELECT 
                    c2.CRMov2CodC as CodC, 
                    c2.CRMov2DesC as Nome, 
                    c3.CRMov3DtaV as Vencimento, 
                    c3.CRMov3VlAb as Valor
                FROM crmov3 c3
                INNER JOIN crmov2 c2 ON c3.CMEmpCod = c2.CMEmpCod 
                                   AND c3.CMFilCod = c2.CMFilCod 
                                   AND c3.CRMovDta = c2.CRMovDta 
                                   AND c3.CRMovSeq = c2.CRMovSeq
                WHERE c3.CRMov3VlAb > 0 
                  AND c3.CRMov3Flag = 'A'
                  AND c2.CRMov2CodC <> 1
            """
            self.df_parcelas = pd.read_sql(query, conn)
            conn.close()

            if self.df_parcelas.empty:
                self.ax.clear()
                self.ax.set_title("NENHUMA PARCELA 'ABERTA' ENCONTRADA")
                self.canvas.draw()
                return

            hoje = datetime.now()
            self.df_parcelas['Vencimento'] = pd.to_datetime(self.df_parcelas['Vencimento'])
            self.df_parcelas['dias_diff'] = (self.df_parcelas['Vencimento'] - hoje).dt.days

            # Faixas definidas pelo usuário
            faixas = [
                # VENCIDAS
                (-99999, -360, "+360d", "#B71C1C"),
                (-360, -180, "+180d", "#C62828"),
                (-180, -90, "+90d", "#D32F2F"),
                (-90, -60, "+60d", "#E53935"),
                (-60, -30, "+30d", "#EF5350"),
                (-30, 0, "Até 30d", "#F44336"),
                # A VENCER
                (0, 31, "Até 30d", "#4CAF50"),
                (31, 61, "30d", "#43A047"),
                (61, 91, "60d", "#388E3C"),
                (91, 181, "90d", "#2E7D32"),
                (181, 361, "180d", "#1B5E20"),
                (361, 99999, "+360d", "#004D40")
            ]

            self.faixas_info = faixas
            labels_x = []
            valores_y = []
            cores = []

            for start, end, label, cor in faixas:
                soma = self.df_parcelas[(self.df_parcelas['dias_diff'] >= start) & (self.df_parcelas['dias_diff'] < end)]['Valor'].sum()
                labels_x.append(label)
                valores_y.append(soma)
                cores.append(cor)

            self.ax.clear()
            self.bars = self.ax.bar(labels_x, valores_y, color=cores, width=0.7, picker=True)
            
            self.ax.set_title("ANÁLISE DE VENCIMENTOS (PARCELAS ABERTAS)", fontsize=14, fontweight='bold', pad=25)
            self.ax.set_ylabel("Valor Total (R$)", fontsize=11)
            self.ax.tick_params(axis='x', rotation=0, labelsize=9)
            
            for bar in self.bars:
                height = bar.get_height()
                if height > 0:
                    self.ax.text(bar.get_x() + bar.get_width()/2., height,
                                f'R$ {height:,.0f}'.replace(',', '.'),
                                ha='center', va='bottom', fontsize=8, fontweight='bold')

            from matplotlib.patches import Patch
            legend_elements = [
                Patch(facecolor='#C62828', label='Parcelas Vencidas'),
                Patch(facecolor='#2E7D32', label='Parcelas A Vencer')
            ]
            self.ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=2, frameon=False)

            self.ax.spines['top'].set_visible(False)
            self.ax.spines['right'].set_visible(False)
            self.fig.tight_layout()
            self.canvas.draw()

        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erro Carregar Parcelas", f"Erro no processamento:\n{str(e)}")

    def on_click(self, event):
        if event.inaxes != self.ax: return
        for i, bar in enumerate(self.bars):
            if bar.contains(event)[0]:
                label_txt = self.faixas_info[i][2]
                start, end = self.faixas_info[i][0], self.faixas_info[i][1]
                tipo = "Vencidas" if start < 0 else "A Vencer"
                self.abrir_detalhes(f"{tipo} ({label_txt})", start, end)
                break

    def abrir_detalhes(self, titulo_faixa, start, end):
        if self.df_parcelas is None: return
        
        # Filtrar dados da faixa
        df_sub = self.df_parcelas[(self.df_parcelas['dias_diff'] >= start) & (self.df_parcelas['dias_diff'] < end)].copy()
        if df_sub.empty: return

        # Criar Janela Toplevel
        top = ctk.CTkToplevel(self)
        top.title(f"Detalhes: {titulo_faixa}")
        top.geometry("800x500")
        top.after(10, lambda: top.focus_force())
        top.grab_set() # Modal

        # Centralizar
        x = self.winfo_screenwidth() // 2 - 400
        y = self.winfo_screenheight() // 2 - 250
        top.geometry(f"800x500+{x}+{y}")

        # Label Título
        ctk.CTkLabel(top, text=f"📄 LISTA DE PARCELAS - {titulo_faixa}", font=("Arial", 16, "bold"), text_color="#1565C0").pack(pady=15)

        # Frame para o Grid
        f_grid = ctk.CTkFrame(top)
        f_grid.pack(fill="both", expand=True, padx=20, pady=10)

        # Treeview com Zebra
        cols = ("Cod", "Nome", "Vencimento", "Valor")
        tree = ttk.Treeview(f_grid, columns=cols, show="headings", height=15)
        tree.pack(fill="both", expand=True, side="left")

        # Configuração de Cores para o Zebra
        tree.tag_configure('even', background='#FFFFFF')
        tree.tag_configure('odd', background='#E2E8F0')

        # Scrollbar
        scb = ttk.Scrollbar(f_grid, orient="vertical", command=tree.yview)
        scb.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scb.set)

        tree.heading("Cod", text="Cód. Cliente")
        tree.heading("Nome", text="Nome do Cliente")
        tree.heading("Vencimento", text="Vencimento")
        tree.heading("Valor", text="Valor Aberto")

        tree.column("Cod", width=100, anchor="center")
        tree.column("Nome", width=350)
        tree.column("Vencimento", width=120, anchor="center")
        tree.column("Valor", width=120, anchor="e")

        # Inserir dados com Zebra
        total_acumulado = 0
        for i, (_, row) in enumerate(df_sub.sort_values('Vencimento').iterrows()):
            v_ab = float(row['Valor'])
            total_acumulado += v_ab
            tag = 'even' if i % 2 == 0 else 'odd'
            tree.insert("", "end", values=(
                str(int(row['CodC'])),
                str(row['Nome']).strip(),
                row['Vencimento'].strftime('%d/%m/%Y'),
                f"R$ {v_ab:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            ), tags=(tag,))

        # Rodapé com total
        ctk.CTkLabel(top, text=f"💰 TOTAL DESTA FAIXA: R$ {total_acumulado:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'), font=("Arial", 14, "bold")).pack(pady=10)

        # Identificador de Tela (Nome Exclusivo) no Canto Inferior Direito
        f_id = ctk.CTkFrame(top, fg_color="transparent")
        f_id.pack(side="bottom", fill="x", padx=20, pady=(0, 10))

        btn_fechar_det = ctk.CTkButton(f_id, text="✖ Fechar", width=90, height=25, fg_color="transparent", hover_color="#E0E0E0", text_color="black", font=("Arial", 11, "bold"), border_width=1, border_color="black", command=top.destroy)
        btn_fechar_det.pack(side="left")

        btn_copy_det = ctk.CTkButton(f_id, text="📋", width=25, height=25, fg_color="transparent", hover_color="#E0E0E0", text_color="black", font=("Arial", 11, "bold"), 
                                    command=lambda: [top.clipboard_clear(), top.clipboard_append("ANALISE_PARCELAS_DET"), messagebox.showinfo("Sucesso", "NOME DA TELA COPIADO")])
        btn_copy_det.pack(side="right")

        lbl_id_det = ctk.CTkLabel(f_id, text="Tela: ANALISE_PARCELAS_DET", font=("Arial", 11, "bold"), text_color="gray")
        lbl_id_det.pack(side="right", padx=5)

        ToolTip(btn_copy_det, "COPIAR NOME TELA")

    def exportar_pdf(self): pass
    def exportar_excel(self): pass

    def exportar_pdf(self): pass
    def exportar_excel(self): pass

if __name__ == '__main__':
    import sys, argparse
    parser = argparse.ArgumentParser(description="Módulo de Análise e Atualização")
    parser.add_argument("--tela", type=str, choices=["ANALISE", "CEP"], help="Abre uma tela específica diretamente")
    parser.add_argument("--servidor", type=str, help="Servidor")
    parser.add_argument("--banco", type=str, help="Banco")
    parser.add_argument("--usuario", type=str, help="Usuário")
    parser.add_argument("--senha", type=str, help="Senha")
    
    args = parser.parse_args()
    config = {"nome_usuario": "Operador", "servidor": r"servidor\sqlexpress", "banco": "msinfor", "usuario_bd": "sa", "senha_bd": "Mabelu2011"}
    
    if args.servidor: config["servidor"] = args.servidor
    if args.banco: config["banco"] = args.banco
    if args.usuario: config["usuario_bd"] = args.usuario
    if args.senha: config["senha_bd"] = args.senha

    if args.tela:
        root = ctk.CTk(); root.withdraw()
        if args.tela.upper() == "ANALISE": app_win = AnaliseVendasWindow(root, config)
        elif args.tela.upper() == "CEP": app_win = App(root, config)
        root.mainloop()
    else:
        app = MainHub()
        if args.servidor: app.config["servidor"] = args.servidor
        if args.banco: app.config["banco"] = args.banco
        if args.usuario: app.config["usuario_bd"] = args.usuario
        if args.senha: app.config["senha_bd"] = args.senha
        app.mainloop()

