class CobrancaClienteWindow(BaseWindow):
    def __init__(self, parent, config):
        super().__init__(parent, "Cobrança por Cliente", "COBRANCA_CLIENTE")
        self.config_db = config

        # Barra de Filtros
        self.filter_frame = ctk.CTkFrame(self.top_frame, fg_color="transparent")
        self.filter_frame.pack(side="top", fill="x", padx=20, pady=5, anchor="w")

        ctk.CTkLabel(self.filter_frame, text="Filtro Atraso:", font=("Arial", 14, "bold"), text_color="#1E293B").pack(side="left", padx=(10, 5))
        self.combo_atraso = ctk.CTkComboBox(self.filter_frame, values=["Todos", "Até 30 dias", "Até 60 dias", "Até 90 dias", "Superior a 90 dias"], width=180, font=("Arial", 14), command=lambda _: self.carregar_dados())
        self.combo_atraso.pack(side="left", padx=5); self.combo_atraso.set("Todos")

        self.entry_busca = ctk.CTkEntry(self.filter_frame, placeholder_text="Buscar cliente...", width=200, font=("Arial", 14))
        self.entry_busca.pack(side="left", padx=10)
        self.entry_busca.bind("<KeyRelease>", lambda _: self.filtrar_grid())

        btn_processar = ctk.CTkButton(self.filter_frame, text="⚙️ Atualizar", command=self.carregar_dados, fg_color="#1E88E5", hover_color="#1565C0", width=110, font=("Arial", 13, "bold"))
        btn_processar.pack(side="left", padx=10)

    def get_sql_summary(self):
        emp = self.config_db.get("empresa", "01")
        atraso = self.combo_atraso.get()
        having = ""
        if atraso == "Até 30 dias": having = "HAVING MAX(DATEDIFF(day, c3.CRMov3DtaV, GETDATE())) <= 30"
        elif atraso == "Até 60 dias": having = "HAVING MAX(DATEDIFF(day, c3.CRMov3DtaV, GETDATE())) <= 60"
        elif atraso == "Até 90 dias": having = "HAVING MAX(DATEDIFF(day, c3.CRMov3DtaV, GETDATE())) <= 90"
        elif atraso == "Superior a 90 dias": having = "HAVING MAX(DATEDIFF(day, c3.CRMov3DtaV, GETDATE())) > 90"

        return (
            "TABELAS:\n"
            "- CRMOV3 c3 (Parcelas)\n"
            "- CRMOV2 c2 (Cabeçalho Venda)\n\n"
            "CAMPOS PARA ANÁLISE:\n"
            "- c3.CRMov3DtaV: Data de Vencimento\n"
            "- c3.CRMov3VlAb: Valor em Aberto Atual (Soma)\n"
            "- c3.CRMov3Flag: Situação Parcela (A=Aberta)\n"
            "- c2.CRMov2CodC: Código do Cliente (Agrupamento)\n"
            "- c2.CRMov2DesC: Razão Social/Nome p/ Lista\n"
            "- c2.CMEmpCod: Identificação da Empresa\n\n"
            "FILTRO ATUAL (WHERE/HAVING):\n"
            f"  c2.CMEmpCod = '{emp}'\n"
            "  AND c3.CRMov3VlAb > 0\n"
            "  AND c3.CRMov3Flag = 'A'\n"
            "  AND c2.CRMov2Flag IN ('A','F')\n"
            f"  {having}"
        )

        # Configurar Colunas do Grid
        self.tree["columns"] = ("Cod", "Nome", "QtdAtraso", "ValorAtraso", "ValorAVencer", "ValorTotal", "DtaMaisAtrasada", "DiasAtraso")
        
        self.headers_dict = {
            "Cod": "Cód.",
            "Nome": "Nome do Cliente",
            "QtdAtraso": "Qtd.",
            "ValorAtraso": "Vlr. Atraso",
            "ValorAVencer": "Vlr. a Vencer",
            "ValorTotal": "Vlr. Total",
            "DtaMaisAtrasada": "Dta. Atrasada",
            "DiasAtraso": "Dias"
        }

        for col in self.tree["columns"]:
            self.tree.heading(col, text=self.headers_dict[col] + " ↕", command=lambda c=col: self.ordenar_por(c, False))

        self.tree.column("Cod", width=60, anchor="center")
        self.tree.column("Nome", width=240)
        self.tree.column("QtdAtraso", width=60, anchor="center")
        self.tree.column("ValorAtraso", width=110, anchor="e")
        self.tree.column("ValorAVencer", width=110, anchor="e")
        self.tree.column("ValorTotal", width=110, anchor="e")
        self.tree.column("DtaMaisAtrasada", width=100, anchor="center")
        self.tree.column("DiasAtraso", width=60, anchor="center")

        self.rows_cache = []
        self.reverse_sort = False

        # Rodapé de Totais
        self.lbl_rodape_total = ctk.CTkLabel(self.bottom_bar, text="", font=("Arial", 13, "bold"), text_color="#1565C0")
        self.lbl_rodape_total.pack(side="left", padx=10)

        self.after(100, self.carregar_dados)

    def ordenar_por(self, col, reverse):
        # 1. Obter os dados atuais do grid
        data = [(self.tree.set(k, col), k) for k in self.tree.get_children("")]
        
        # 2. Função de limpeza de valores para ordenação correta
        def clean_val(v, column):
            if not v: return ""
            s = str(v).strip()
            
            # Se for a coluna Nome, faz ordenação de texto pura
            if column == "Nome":
                try:
                    import unidecode
                    return unidecode.unidecode(s.upper())
                except: return s.upper()

            # Moeda R$ 1.234,56
            if "R$" in s:
                try: return float(s.replace("R$", "").replace(".", "").replace(",", ".").strip())
                except: return 0.0
            
            # Números inteiros
            if s.isdigit(): return int(s)
            
            # Datas DD/MM/AAAA
            if "/" in s and len(s) == 10:
                try:
                    import datetime
                    return datetime.datetime.strptime(s, "%d/%m/%Y")
                except: pass

            return s.upper()

        # 3. Ordenar os dados
        data.sort(key=lambda t: clean_val(t[0], col), reverse=reverse)
        
        # 4. Mover itens no grid
        for index, (val, k) in enumerate(data):
            self.tree.move(k, "", index)
        
        # 5. Atualizar TODOS os cabeçalhos para garantir que o comando não se perca e os ícones fiquem certos
        for c in self.tree["columns"]:
            if c == col:
                seta = " ▼" if reverse else " ▲"
                self.tree.heading(c, text=self.headers_dict[c] + seta, command=lambda _c=c: self.ordenar_por(_c, not reverse))
            else:
                self.tree.heading(c, text=self.headers_dict[c] + " ↕", command=lambda _c=c: self.ordenar_por(_c, False))

    def carregar_dados(self):
        try:
            import pyodbc
            import pandas as pd
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config_db['servidor']};DATABASE={self.config_db['banco']};UID={self.config_db['usuario_bd']};PWD={self.config_db['senha_bd']}"
            conn = pyodbc.connect(conn_str)
            
            filtro_atraso = self.combo_atraso.get()
            having_clause = ""
            if filtro_atraso == "Até 30 dias": having_clause = "HAVING MAX(DATEDIFF(day, c3.CRMov3DtaV, GETDATE())) <= 30"
            elif filtro_atraso == "Até 60 dias": having_clause = "HAVING MAX(DATEDIFF(day, c3.CRMov3DtaV, GETDATE())) <= 60"
            elif filtro_atraso == "Até 90 dias": having_clause = "HAVING MAX(DATEDIFF(day, c3.CRMov3DtaV, GETDATE())) <= 90"
            elif filtro_atraso == "Superior a 90 dias": having_clause = "HAVING MAX(DATEDIFF(day, c3.CRMov3DtaV, GETDATE())) > 90"

            query = f"""
                SELECT 
                    c2.CRMov2CodC as CodC, 
                    MAX(c2.CRMov2DesC) as Nome, 
                    COUNT(CASE WHEN c3.CRMov3DtaV < CAST(GETDATE() AS DATE) THEN 1 END) as QtdAtraso,
                    SUM(CASE WHEN c3.CRMov3DtaV < CAST(GETDATE() AS DATE) THEN c3.CRMov3VlAb ELSE 0 END) as ValorAtraso,
                    SUM(CASE WHEN c3.CRMov3DtaV >= CAST(GETDATE() AS DATE) THEN c3.CRMov3VlAb ELSE 0 END) as ValorAVencer,
                    SUM(c3.CRMov3VlAb) as ValorTotal,
                    MIN(CASE WHEN c3.CRMov3DtaV < CAST(GETDATE() AS DATE) THEN c3.CRMov3DtaV END) as DtaAtraso,
                    MAX(CASE WHEN c3.CRMov3DtaV < CAST(GETDATE() AS DATE) THEN DATEDIFF(day, c3.CRMov3DtaV, GETDATE()) ELSE 0 END) as DiasAtraso
                FROM crmov3 c3
                INNER JOIN crmov2 c2 ON c3.CMEmpCod = c2.CMEmpCod 
                                   AND c3.CMFilCod = c2.CMFilCod 
                                   AND c3.CRMovDta = c2.CRMovDta 
                                   AND c3.CRMovSeq = c2.CRMovSeq
                WHERE c2.CMEmpCod = ? AND c2.CRMov2Flag IN ('A','F') AND c3.CRMov3VlAb > 0
                  AND c3.CRMov3Flag = 'A'
                  AND c2.CRMov2Flag IN ('A','F')
                  AND c2.CRMov2CodC <> 1
                GROUP BY c2.CRMov2CodC
                {having_clause}
                ORDER BY ValorAtraso DESC
            """
            cursor = conn.cursor()
            cursor.execute(query, (self.config_db.get("empresa", "01"),))
            self.rows_cache = cursor.fetchall()
            conn.close()
            self.filtrar_grid()
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erro Carregar Cobrança", f"Erro no processamento:\n{str(e)}")

    def filtrar_grid(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        busca = self.entry_busca.get().strip().upper()

        idx = 0
        total_clientes = 0
        soma_atraso = 0.0

        for row in self.rows_cache:
            cod_c = str(int(row[0]))
            
            if busca and (busca not in str(row[1]).strip().upper() and busca not in cod_c):
                continue
            
            total_clientes += 1
            qtd_atraso = int(row[2])
            v_atraso = float(row[3])
            soma_atraso += v_atraso
            v_vencer = float(row[4])
            v_total = float(row[5])
            dta_atraso = row[6].strftime("%d/%m/%Y") if row[6] else "-"
            dias_atraso = int(row[7])

            tag = 'even' if idx % 2 == 0 else 'odd'
            self.tree.insert("", "end", values=(
                cod_c, 
                row[1].strip(), 
                qtd_atraso,
                f"R$ {v_atraso:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                f"R$ {v_vencer:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                f"R$ {v_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                dta_atraso,
                dias_atraso
            ), tags=(tag,))
            idx += 1

        # Atualizar Rodapé
        txt_total = f"👥 CLIENTES: {total_clientes}  |  💰 TOTAL EM ATRASO: R$ {soma_atraso:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        self.lbl_rodape_total.configure(text=txt_total)

    def exportar_pdf(self): pass
    def exportar_excel(self): pass

class ExcluirClientesInativosWindow(BaseWindow):
    def __init__(self, parent, config):
        super().__init__(parent, "Excluir Clientes Inativos (Regra Avançada)", "EXCLUIR_INATIVOS")
        self.config_db = config

        # Barra de Busca e Ações no Header
        self.filter_frame = ctk.CTkFrame(self.top_frame, fg_color="transparent")
        self.filter_frame.pack(side="left", fill="x", expand=True, padx=20, pady=(0, 5))

        ctk.CTkLabel(self.filter_frame, text="Buscar:", font=("Arial", 16, "bold"), text_color="#1E293B").pack(side="left", padx=(10, 5))
        self.entry_busca = ctk.CTkEntry(self.filter_frame, placeholder_text="Filtrar por nome ou código...", width=250, font=("Arial", 15))
        self.entry_busca.pack(side="left", padx=5)
        self.entry_busca.bind("<KeyRelease>", self.filtrar_grid)

        self.btn_processar = ctk.CTkButton(self.filter_frame, text="⚙️ Processar", command=self.carregar_dados, fg_color="#1E88E5", hover_color="#1565C0", width=110, font=("Arial", 13, "bold"))
        self.btn_processar.pack(side="left", padx=10)

        self.btn_help_exclusao = ctk.CTkButton(self.filter_frame, text="?", width=30, height=35, fg_color="#546E7A", hover_color="#455A64", font=("Arial", 14, "bold"), command=self.mostrar_ajuda_exclusao)
        self.btn_help_exclusao.pack(side="right", padx=(5, 15))
        ToolTip(self.btn_help_exclusao, "MOSTRAR SEQUÊNCIA DE EXCLUSÃO")

        # Botão de Exclusão (Destaque em Vermelho)
        self.btn_excluir = ctk.CTkButton(self.filter_frame, text="🗑️ EXCLUIR DEFINITIVAMENTE", command=self.confirmar_exclusao, fg_color="#D32F2F", hover_color="#B71C1C", width=220, font=("Arial", 13, "bold"))
        self.btn_excluir.pack(side="right", padx=0)

        # --- NOVO PADRAO: Usar configurar_grid ---
        cols = ("Rank", "Cod", "Nome", "Det", "UltVenc", "VlAb", "MedMensal", "Status")
        heads = ("🏆 #", "🔑 Cód", "👤 Cliente", "📋", "📅 UltVenc", "💰 Saldo", "📈 Média", "🔘")
        wids = (50, 70, 250, 50, 110, 110, 110, 100)
        aligns = ("center", "center", "w", "center", "center", "e", "e", "center")
        self.configurar_grid(cols, heads, wids, aligns)

        self.tree.bind("<Button-1>", self.on_click_tree)
        self.tree.bind("<Double-1>", self.on_click_tree) 

        self.after(200, self.carregar_dados)

    def mostrar_ajuda_exclusao(self):
        msg = (
            "SEQUÊNCIA E CAMPOS DE EXCLUSÃO (CASCATA):\n\n"
            "1. Títulos/Vínculos Secundários (crmov8 a crmov3):\n"
            "   - Campos: CMEmpCod, CRMovDta ou CRMovSeq\n"
            "   - Regra: Remove todos os registros vinculados às vendas do cliente.\n\n"
            "2. Cabeçalho de Vendas (crmov2):\n"
            "   - Campos: CRMov2CodC (ID Cliente), CMEmpCod\n"
            "   - Regra: Remove o histórico de vendas/documentos.\n\n"
            "3. Notas Fiscais (CENFC):\n"
            "   - Campos: CRCliCod (ID Cliente), CMEmpCod\n"
            "   - Regra: Remove vínculos de faturamento.\n\n"
            "4. Cadastro Principal (crcli):\n"
            "   - Campos: CRCliCod (ID Cliente), CMEmpCod\n"
            "   - Regra: Exclusão definitiva do registro do cliente.\n\n"
            "Toda a operação é executada dentro de uma transação SQL (Commit/Rollback)."
        )
        messagebox.showinfo("Detalhes da Exclusão", msg)

    def ordenar_por(self, col, reverse):
        data = [(self.tree.set(k, col), k) for k in self.tree.get_children("")]
        def clean_val(v, column):
            if not v: return ""
            s = str(v).strip()
            if column == "Nome":
                try: import unidecode; return unidecode.unidecode(s.upper())
                except: return s.upper()
            if column == "VlAb":
                try: return float(s.replace("R$ ", "").replace(".", "").replace(",", "."))
                except: return 0.0
            if column == "Cod": return int(s) if s.isdigit() else 0
            if column == "UltVenc":
                try:
                    from datetime import datetime
                    return datetime.strptime(s, "%d/%m/%Y")
                except: return s
            if s.isdigit(): return int(s)
            return s.upper()
        data.sort(key=lambda t: clean_val(t[0], col), reverse=reverse)
        for index, (val, k) in enumerate(data):
            self.tree.move(k, "", index)
            self.tree.set(k, "Rank", index + 1)
        for c in self.tree["columns"]:
            if c == col:
                seta = " ▼" if reverse else " ▲"
                self.tree.heading(c, text=self.headers_dict[c] + seta, command=lambda _c=c: self.ordenar_por(_c, not reverse))
            else:
                self.tree.heading(c, text=self.headers_dict[c] + " ↕", command=lambda _c=c: self.ordenar_por(_c, False))

    def carregar_dados(self):
        try:
            import pyodbc
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config_db['servidor']};DATABASE={self.config_db['banco']};UID={self.config_db['usuario_bd']};PWD={self.config_db['senha_bd']}"
            conn = pyodbc.connect(conn_str); cur = conn.cursor()
            
            emp_padrao = self.config_db.get("empresa", "01")

            # 1. Buscar Candidatos (Base)
            # Ajustado para considerar apenas parcelas em aberto no filtro de dívidas > 2 anos
            query_base = """
            SELECT 
                c.CRCliCod, 
                c.CRCliDes, 
                MAX(c3.CRMov3DtaV) as UltimaDataGeral,
                c.CRCliAti,
                SUM(ISNULL(c3.CRMov3VlAb, 0)) as TotalAberto,
                MAX(CASE WHEN ISNULL(c3.CRMov3VlAb, 0) > 0 THEN c3.CRMov3DtaV ELSE NULL END) as UltimaDataAberta
            FROM crcli c
            LEFT JOIN crmov2 c2 ON c.CRCliCod = c2.CRMov2CodC AND c.CMEmpCod = c2.CMEmpCod AND c2.CRMov2Flag IN ('A','F')
            LEFT JOIN crmov3 c3 ON c2.CMEmpCod = c3.CMEmpCod AND c2.CMFilCod = c3.CMFilCod AND c2.CRMovDta = c3.CRMovDta AND c2.CRMovSeq = c3.CRMovSeq
            WHERE c.CMEmpCod = ?
            GROUP BY c.CRCliCod, c.CRCliDes, c.CRCliAti
            HAVING 
                c.CRCliAti = 'D'
                OR (
                    MAX(c3.CRMov3DtaV) < DATEADD(year, -1, GETDATE())
                    AND SUM(ISNULL(c3.CRMov3VlAb, 0)) = 0
                    AND MAX(c3.CRMov3DtaV) IS NOT NULL
                )
                OR (
                    MAX(CASE WHEN ISNULL(c3.CRMov3VlAb, 0) > 0 THEN c3.CRMov3DtaV ELSE NULL END) < DATEADD(year, -2, GETDATE())
                    AND SUM(ISNULL(c3.CRMov3VlAb, 0)) > 0
                )
            ORDER BY c.CRCliDes
            """
            cur.execute(query_base, (emp_padrao,))
            self.rows_cache = cur.fetchall()

            # 2. Buscar Histórico Mensal para Cálculo de Média
            query_med = """
            SELECT 
                CRMov2CodC,
                YEAR(CRMovDta) as Ano, 
                MONTH(CRMovDta) as Mes, 
                SUM(CRMov2VlrO) as TotalMes
            FROM crmov2
            WHERE CMEmpCod = ? AND CRMov2Flag IN ('A','F') AND CRMovDta >= DATEADD(month, -48, GETDATE())
            GROUP BY CRMov2CodC, YEAR(CRMovDta), MONTH(CRMovDta)
            """
            cur.execute(query_med, (emp_padrao,))
            history = cur.fetchall()

            # 3. Buscar Soma Total do Sistema (Abertas e Quitadas) e Clientes Geral
            query_totais = """
                SELECT 
                    SUM(ISNULL(c3.CRMov3VlAb, 0)) as SaldoAberto,
                    SUM(ISNULL(c3.CRMov3VlrO, 0) - ISNULL(c3.CRMov3VlAb, 0)) as Pago,
                    SUM(ISNULL(c3.CRMov3VlrO, 0)) as VolumeGeral
                FROM crmov3 c3
                INNER JOIN crmov2 c2 ON c3.CMEmpCod = c2.CMEmpCod AND c3.CMFilCod = c2.CMFilCod AND c3.CRMovDta = c2.CRMovDta AND c3.CRMovSeq = c2.CRMovSeq
                WHERE c2.CMEmpCod = ? AND c2.CRMov2Flag IN ('A','F')
            """
            cur.execute(query_totais, (emp_padrao,))
            tot_ab, tot_pq, vol_geral = cur.fetchone()
            tot_ab = tot_ab or 0.0; tot_pq = tot_pq or 0.0; vol_geral = vol_geral or 0.0

            cur.execute("""
                SELECT 
                    COUNT(*), 
                    SUM(CASE WHEN CRCliAti<>'D' THEN 1 ELSE 0 END),
                    SUM(CASE WHEN CRCliAti='D' THEN 1 ELSE 0 END)
                FROM crcli WHERE CMEmpCod=?
            """, (emp_padrao,))
            tot_cli_g, tot_cli_a, tot_cli_i = cur.fetchone()
            
            def fmt(v): return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            self.lbl_rodape_sistema.configure(text=f"🌍 SISTEMA | Abertas: {fmt(tot_ab)} | Quitadas: {fmt(tot_pq)}")
            self.lbl_vlr_geral_parcelas.configure(text=f"Vol. Geral: {fmt(vol_geral)}")
            self.lbl_cli_geral.configure(text=f"Geral: {tot_cli_g}")
            self.lbl_cli_ativos.configure(text=f"Ativos: {tot_cli_a or 0}")
            self.lbl_cli_inativos_db.configure(text=f"Inativos (DB): {tot_cli_i or 0}")

            conn.close()

            # Organizar histórico por cliente
            hist_dict = {}
            for h in history:
                cod_c, ano, mes, vlr = h
                if cod_c not in hist_dict: hist_dict[cod_c] = []
                hist_dict[cod_c].append(float(vlr))

            # Calcular médias com as regras de exclusão de outliers (muito abaixo da média)
            self.medias_cache = {}
            for cod_c, valores in hist_dict.items():
                if not valores: 
                    self.medias_cache[cod_c] = 0.0
                    continue
                
                # Regra 1: Não contar meses sem movimento (já garantido pelo GROUP BY que não traz zeros)
                # Regra 2: Calcular média inicial
                v_filtered = [v for v in valores if v > 0]
                if not v_filtered:
                    self.medias_cache[cod_c] = 0.0
                    continue
                
                avg_inicial = sum(v_filtered) / len(v_filtered)
                
                # Regra 3: Não contar meses em que seja muito abaixo da média (Outliers inferiores)
                # Definimos "muito abaixo" como menos de 10% da média inicial (Solicitado pelo usuário)
                threshold = avg_inicial * 0.10
                v_final = [v for v in v_filtered if v >= threshold]
                
                if not v_final:
                    self.medias_cache[cod_c] = avg_inicial # Fallback caso todos sejam filtrados (improvável)
                else:
                    self.medias_cache[cod_c] = sum(v_final) / len(v_final)

            self.filtrar_grid()
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erro Carregar", f"Erro no processamento das médias e inativos:\n{str(e)}")

    def filtrar_grid(self, event=None):
        busca = self.entry_busca.get().strip().upper()
        for item in self.tree.get_children(): self.tree.delete(item)
        if not hasattr(self, 'rows_cache'): return

        total = 0
        soma_aberto = 0.0
        def fmt(v): return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        
        for idx, row in enumerate(self.rows_cache):
            cod_c = str(int(row[0]))
            nome_c = str(row[1]).strip().upper()
            if busca and (busca not in nome_c and busca not in cod_c): continue

            total += 1
            
            # Formatar Data e Valores
            vl_aberto = float(row[4] or 0.0)
            dta_exib = row[5] if vl_aberto > 0 and row[5] else row[2]
            dta_str = dta_exib.strftime("%d/%m/%Y") if dta_exib else "N/A"
            soma_aberto += vl_aberto
            
            vl_txt = fmt(vl_aberto)
            media_v = self.medias_cache.get(row[0], 0.0)
            med_txt = fmt(media_v)

            # Status e Tags
            tags = []
            tags.append('even' if total % 2 == 0 else 'odd')
            
            if row[3] == 'D':
                status_txt = "BLOQUEADO (D)"
                tags.append('status_d')
            elif vl_aberto > 0:
                status_txt = "DÍVIDA > 2 ANOS"
            else:
                status_txt = "INATIVO > 1 ANO"
            
            self.tree.insert("", "end", values=(total, cod_c, nome_c, " 🔍 VER ", dta_str, vl_txt, med_txt, status_txt), tags=tuple(tags))
        
        # Atualizar Resumo de Totais (Padrao Excel)
        fmt = lambda v: f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        for item in self.tree_totais.get_children(): self.tree_totais.delete(item)
        self.tree_totais.insert("", "end", values=(f" TOTAIS ({total}):", "", "", "", "", fmt(soma_aberto), fmt(soma_med), ""))

    def on_click_tree(self, event):
        item_id = self.tree.identify_row(event.y)
        if not item_id: return
        
        # Forçar seleção do item clicado para consistência
        self.tree.selection_set(item_id)
        self.tree.focus(item_id)

        # Conforme solicitado: "clicar sobre a linha já abrir as parcelas"
        # Isso cobre tanto o clique simples quanto o duplo clique
        self.abrir_detalhes_parcelas(item_id)

    def abrir_detalhes_parcelas(self, item_id=None):
        if not item_id:
            sel = self.tree.selection()
            if not sel: return
            item_id = sel[0]

        item_vals = self.tree.item(item_id)['values']
        cod_cliente = item_vals[1]
        nome_cliente = item_vals[2]
        self.hub.abrir_modulo_detalhes_inativos(cod_cliente, nome_cliente)

    def confirmar_exclusao(self):
        sel = self.tree.selection()
        if not sel:
            from tkinter import messagebox
            messagebox.showwarning("Aviso", "Selecione um cliente para excluir.")
            return
        
        vals = self.tree.item(sel[0])['values']
        cod_c = vals[1]
        nome_c = vals[2]
        
        # Diálogo customizado p/ confirmação de exclusão
        class ConfirmDeleteDialog(ctk.CTkToplevel):
            def __init__(self, master, cod, nome):
                super().__init__(master)
                self.title("🔴 CONFIRMAÇÃO DE EXCLUSÃO")
                self.geometry("550x300")
                self.configure(fg_color="#F8FAFC")
                self.result = False
                self.grab_set(); self.resizable(False, False); self.transient(master)
                
                # Centralizar
                self.update_idletasks()
                x = master.winfo_x() + (master.winfo_width() // 2) - 275
                y = master.winfo_y() + (master.winfo_height() // 2) - 150
                self.geometry(f"+{x}+{y}")
                
                ctk.CTkLabel(self, text="⚠️", font=("Arial", 60)).pack(pady=(20, 5))
                ctk.CTkLabel(self, text="Deseja EXCLUIR DEFINITIVAMENTE o cliente:", font=("Arial", 14), text_color="#1E293B").pack(pady=5)
                ctk.CTkLabel(self, text=f"({cod}) {str(nome).upper()}", font=("Arial", 20, "bold"), text_color="#E11D48", wraplength=500).pack(pady=10, fill="x", padx=20)
                ctk.CTkLabel(self, text="Esta ação não poderá ser desfeita!", font=("Arial", 12, "italic"), text_color="gray").pack(pady=5)
                
                btn_frame = ctk.CTkFrame(self, fg_color="transparent")
                btn_frame.pack(pady=20)
                
                ctk.CTkButton(btn_frame, text="✅ SIM, EXCLUIR", command=self.confirmar, fg_color="#D32F2F", hover_color="#B71C1C", width=160, height=40, font=("Arial", 13, "bold")).pack(side="left", padx=10)
                ctk.CTkButton(btn_frame, text="✖ CANCELAR", command=self.destroy, fg_color="#DEE2E6", text_color="black", width=140, height=40, font=("Arial", 13, "bold")).pack(side="left", padx=10)
                
            def confirmar(self):
                self.result = True
                self.destroy()

        dialog = ConfirmDeleteDialog(self, cod_c, nome_c)
        self.wait_window(dialog)
        
        if dialog.result:
            self.executar_exclusao(cod_c, nome_c)

    def executar_exclusao(self, cod, nome):
        # 1. Dialog customizado para senha (MAIOR)
        class SenhaDialog(ctk.CTkToplevel):
            def __init__(self, master):
                super().__init__(master)
                self.title("Autenticação Necessária")
                self.geometry("450x250")
                self.configure(fg_color="#F8FAFC")
                self.result = None
                self.grab_set() # Modal
                self.resizable(False, False)
                
                # Centralizar
                self.transient(master)
                self.update_idletasks()
                x = master.winfo_x() + (master.winfo_width() // 2) - 225
                y = master.winfo_y() + (master.winfo_height() // 2) - 125
                self.geometry(f"+{x}+{y}")

                ctk.CTkLabel(self, text="⚠️ EXCLUSÃO DEFINITIVA", font=("Arial", 16, "bold"), text_color="#E11D48").pack(pady=(20, 10))
                ctk.CTkLabel(self, text=f"Informe a senha para excluir:\n{nome}", font=("Arial", 13)).pack(pady=5)
                
                self.entry = ctk.CTkEntry(self, show="*", width=300, height=40, font=("Arial", 16), placeholder_text="Senha master...")
                self.entry.pack(pady=10)
                self.entry.focus_set()
                self.entry.bind("<Return>", lambda e: self.confirmar())

                btn_frame = ctk.CTkFrame(self, fg_color="transparent")
                btn_frame.pack(pady=10)
                
                ctk.CTkButton(btn_frame, text="Confirmar", command=self.confirmar, fg_color="#1E293B", width=120, height=35).pack(side="left", padx=5)
                ctk.CTkButton(btn_frame, text="Cancelar", command=self.destroy, fg_color="#DEE2E6", text_color="black", width=120, height=35).pack(side="left", padx=5)

            def confirmar(self):
                self.result = self.entry.get()
                self.destroy()

        if not getattr(self, "senha_autenticada", False):
            dialog = SenhaDialog(self)
            self.wait_window(dialog)
            if dialog.result == "Mabelu@2011":
                self.senha_autenticada = True
            elif dialog.result is None:
                return
            else:
                from tkinter import messagebox
                messagebox.showerror("Erro", "Senha incorreta.")
                return

        try:
            import pyodbc
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config_db['servidor']};DATABASE={self.config_db['banco']};UID={self.config_db['usuario_bd']};PWD={self.config_db['senha_bd']}"
            conn = pyodbc.connect(conn_str); cur = conn.cursor()
            emp = self.config_db.get("empresa", "01")
            conn.autocommit = False
            try:
                # 2. Ordem de Exclusão Robusta para Evitar Conflitos de FK
                # Verifica colunas existentes para construir os DELETEs sem erro de "coluna inválida"
                for tab in ["crmov8", "crmov7", "crmov6", "crmov5", "crmov4", "crmov3"]:
                    try:
                        # Testar se a coluna CRMovDta existe na tabela
                        cur.execute(f"SELECT TOP 0 CRMovDta FROM {tab}")
                        # Se não deu erro, executa o DELETE por data e seq
                        cur.execute(f"""
                            DELETE FROM {tab} 
                            WHERE CMEmpCod=? AND CRMovDta IN (SELECT CRMovDta FROM crmov2 WHERE CRMov2CodC=? AND CMEmpCod=?)
                        """, (emp, cod, emp))
                    except:
                        # Se CRMovDta não existir, tenta por CRMovSeq se possível
                        try:
                            cur.execute(f"SELECT TOP 0 CRMovSeq FROM {tab}")
                            cur.execute(f"""
                                DELETE FROM {tab} 
                                WHERE CMEmpCod=? AND CRMovSeq IN (SELECT CRMovSeq FROM crmov2 WHERE CRMov2CodC=? AND CMEmpCod=?)
                            """, (emp, cod, emp))
                        except:
                            pass # Tabela não segue o padrão ou não existe

                # Deletar cabeçalho
                cur.execute("DELETE FROM crmov2 WHERE CRMov2CodC=? AND CMEmpCod=?", (cod, emp))
                
                # Deletar Vínculos de Notas Fiscais (Children of CENFC)
                # CENFD (Duplicatas), CENFP (Produtos), CENFO1 (Observações), etc.
                for child in ["CENFD", "CENFP", "CENFO1", "CENFR", "CENFV", "CENFM", "CENFK"]:
                    try:
                        cur.execute(f"""
                            DELETE FROM {child} 
                            WHERE CMEmpCod=? AND CENFCSeq IN (SELECT CENFCSeq FROM CENFC WHERE CRCliCod=? AND CMEmpCod=?)
                        """, (emp, cod, emp))
                    except:
                        pass

                # Deletar Notas Fiscais (CENFC)
                cur.execute("DELETE FROM CENFC WHERE CRCliCod=? AND CMEmpCod=?", (cod, emp))

                # Deletar cliente
                cur.execute("DELETE FROM crcli WHERE CRCliCod=? AND CMEmpCod=?", (cod, emp))
                
                conn.commit()
                class SuccessDeleteDialog(ctk.CTkToplevel):
                    def __init__(self, master, nome):
                        super().__init__(master)
                        self.title("✅ EXCLUSÃO CONCLUÍDA")
                        self.geometry("500x320")
                        self.configure(fg_color="#FFFFFF")
                        self.grab_set() 
                        self.resizable(False, False)
                        self.transient(master)
                        
                        # Centralizar
                        self.update_idletasks()
                        x = master.winfo_x() + (master.winfo_width() // 2) - 250
                        y = master.winfo_y() + (master.winfo_height() // 2) - 160
                        self.geometry(f"+{x}+{y}")

                        try:
                            img_path = os.path.join(os.path.dirname(__file__), "success_check.png")
                            success_img_pil = Image.open(img_path)
                            self.success_img = ctk.CTkImage(success_img_pil, size=(90, 90))
                            ctk.CTkLabel(self, text="", image=self.success_img).pack(pady=(25, 10))
                        except Exception:
                            ctk.CTkLabel(self, text="✅", font=("Arial", 60)).pack(pady=(25, 10))

                        ctk.CTkLabel(self, text="Operação Finalizada!", font=("Arial", 20, "bold"), text_color="#15803D").pack(pady=5)
                        
                        msg = f"O cliente {nome.upper()}\ne seus vínculos foram excluídos com sucesso."
                        ctk.CTkLabel(self, text=msg, font=("Arial", 14), justify="center").pack(pady=(10, 20))
                        
                        ctk.CTkButton(self, text="OK", command=self.destroy, fg_color="#1E293B", hover_color="#334155", width=140, height=40, font=("Arial", 13, "bold")).pack(side="bottom", pady=25)

                SuccessDeleteDialog(self, nome)
                self.carregar_dados()
            except Exception as e_sql:
                conn.rollback(); raise e_sql
            finally: conn.close()
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erro", f"Erro na exclusão: {e}")

class DetalhesParcelasInativosWindow(BaseWindow):
    def __init__(self, parent, config, cod_cliente, nome_cliente):
        super().__init__(parent, f"Histórico de Parcelas - {nome_cliente}", "DET_PARCELAS_INATIVOS")
        self.config_db = config
        self.cod_cliente = cod_cliente
        self.nome_cliente = nome_cliente

        # Ocultar botões de exportação padrão se não quiser agora, ou manter
        # Usar novo padrao configurar_grid
        self.configurar_grid(
             columns=("DtaV", "VlNo", "VlAb", "DtaP"),
             headings=("Vencimento", "Valor Parcela", "Saldo Aberto", "Data Pagamento"),
             widths=(150, 180, 180, 150),
             aligns=("center", "e", "e", "center")
        )

        self.after(100, self.carregar_dados)

    def get_sql_summary(self):
        emp = self.config_db.get("empresa", "01")
        return (
            "TABELAS:\n"
            "- CRMOV3 c3 (Histórico Parcelas)\n"
            "- CRMOV2 c2 (Documento Venda)\n\n"
            "CAMPOS PARA ANÁLISE:\n"
            "- c3.CRMov3DtaV: Data de Vencimento\n"
            "- c3.CRMov3VlrO: Valor Original da Parcela\n"
            "- c3.CRMov3VlAb: Saldo Pendente na Data\n"
            "- c3.CRMov3DtaP: Data da Baixa Efetuada\n"
            "- c2.CRMov2CodC: Código do Cliente Selecionado\n"
            "- c2.CRMov2Flag: Flag Válida (Ativa/Finalizada)\n\n"
            "FILTRO ATUAL (WHERE):\n"
            f"- c2.CRMov2CodC = {self.cod_cliente}\n"
            f"- c2.CMEmpCod = '{emp}'\n"
            "- c2.CRMov2Flag IN ('A','F')"
        )

    def fechar_tela(self):
        # Volta especificamente para a tela de inativos
        self.hub.abrir_excluir_inativos()

    def carregar_dados(self):
        try:
            import pyodbc
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.config_db['servidor']};DATABASE={self.config_db['banco']};UID={self.config_db['usuario_bd']};PWD={self.config_db['senha_bd']}"
            conn = pyodbc.connect(conn_str); cur = conn.cursor()
            
            sql = """
            SELECT 
                c3.CRMov3DtaV, 
                c3.CRMov3VlrO, 
                c3.CRMov3VlAb, 
                c3.CRMov3DtaP
            FROM crmov3 c3
            INNER JOIN crmov2 c2 ON c3.CMEmpCod = c2.CMEmpCod AND c3.CMFilCod = c2.CMFilCod AND c3.CRMovDta = c2.CRMovDta AND c3.CRMovSeq = c2.CRMovSeq
            WHERE c2.CRMov2CodC = ? AND c2.CMEmpCod = ? AND c2.CRMov2Flag IN ('A','F')
            ORDER BY c3.CRMov3DtaV DESC
            """
            cur.execute(sql, (self.cod_cliente, self.config_db.get("empresa","01")))
            rows = cur.fetchall()
            
            total_nom = 0.0
            total_aberto = 0.0
            
            def fmt(v): return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            
            for idx, r in enumerate(rows):
                dv, v_nom, v_ab, dp = r
                v_ab = float(v_ab or 0); v_nom = float(v_nom or 0)
                total_nom += v_nom; total_aberto += v_ab
                
                dta_v_s = dv.strftime("%d/%m/%Y") if dv else ""
                dta_p_s = dp.strftime("%d/%m/%Y") if dp else "---"
                tag = 'even' if idx % 2 == 0 else 'odd'
                
                self.tree.insert("", "end", values=(dta_v_s, fmt(v_nom), fmt(v_ab), dta_p_s), tags=(tag,))

            # Atualizar Treeview de Totais (Sincronização Perfeita)
            for item in self.tree_totais.get_children(): self.tree_totais.delete(item)
            self.tree_totais.insert("", "end", values=(f" TOTAIS ({len(rows)}):", fmt(total_nom), fmt(total_aberto), ""))

            conn.close()

        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Erro SQL", f"Erro ao carregar detalhes:\n{e}")
            self.lbl_detalhe_total.configure(text="🔴 Erro ao carregar.")


