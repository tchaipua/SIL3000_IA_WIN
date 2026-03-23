import os

filepath = r"c:\Sistemas\IA\SIL3000_IA_WIN\SIL_IA_WIN.py"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Altera except na Janela de CEP (Classe App, simular_atualizacao)
old_cep_except = """            except Exception as e:
                messagebox.showerror("Erro", f"Falha na conexão:\\n{e}")
                return"""

new_cep_except = """            except Exception as e:
                messagebox.showerror("Erro de Conexão", f"Falha na conexão com o Banco de Dados:\\n{e}\\n\\nAbrindo Configurações...")
                self.abrir_config()
                return"""

if old_cep_except in content:
    content = content.replace(old_cep_except, new_cep_except)

# 2. Altera except na Janela de Análise (AnaliseVendasWindow, carregar_dados)
old_analise_except = """        except Exception as e:
            messagebox.showerror("Erro ao carregar dados", str(e))"""

new_analise_except = """        except Exception as e:
            messagebox.showerror("Erro de Conexão", f"Falha ao carregar dados do banco de dados:\\n\\n{str(e)}")
            # Força a abertura da janela de configuração para correção
            ConfigWindow(self, self.config, lambda c: [setattr(self, 'config', c), self.carregar_dados()])"""

if old_analise_except in content:
    content = content.replace(old_analise_except, new_analise_except)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Regras de fallback de erro de conexão com Banco de Dados injetadas.")
