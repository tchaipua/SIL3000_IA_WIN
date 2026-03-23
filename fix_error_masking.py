import os

filepath = r"c:\Sistemas\IA\SIL3000_IA_WIN\SIL_IA_WIN.py"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Altera except na Janela de CEP (App) para usar mensagem amigável e abrir ConfigWindow
old_cep_except = """            except Exception as e:
                messagebox.showerror("Erro de Conexão", f"Falha na conexão com o Banco de Dados:\\n{e}\\n\\nAbrindo Configurações...")
                self.abrir_config()
                return"""

new_cep_except = """            except Exception as e:
                messagebox.showerror("Erro de Conexão", "Não foi possível conectar ao Banco de Dados com as credenciais fornecidas.\\n\\nVerifique os dados de acesso (Servidor, Banco, Usuário ou Senha) nas configurações e tente novamente.")
                # Abre a tela ConfigWindow (CFG_ACESSO)
                ConfigWindow(self, self.config, lambda c: [setattr(self, 'config', c)])
                return"""

if old_cep_except in content:
    content = content.replace(old_cep_except, new_cep_except)

# 2. Altera except na Janela de Análise (AnaliseVendasWindow)
old_analise_except = """        except Exception as e:
            messagebox.showerror("Erro de Conexão", f"Falha ao carregar dados do banco de dados:\\n\\n{str(e)}")
            # Força a abertura da janela de configuração para correção
            ConfigWindow(self, self.config, lambda c: [setattr(self, 'config', c), self.carregar_dados()])"""

new_analise_except = """        except Exception as e:
            messagebox.showerror("Erro de Conexão", "Não foi possível conectar ao Banco de Dados com as credenciais fornecidas.\\n\\nVerifique os dados de acesso (Servidor, Banco, Usuário ou Senha) nas configurações e tente novamente.")
            # Abre a tela ConfigWindow (CFG_ACESSO) de forma autônoma
            ConfigWindow(self, self.config, lambda c: [setattr(self, 'config', c), self.carregar_dados()])"""

if old_analise_except in content:
    content = content.replace(old_analise_except, new_analise_except)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Mensagens de erro amigáveis para conexão de Banco de Dados injetadas.")
