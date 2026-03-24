import customtkinter as ctk
import time
from SIL_IA_WIN import MainHub

root = MainHub()
root.update()

# Simula click no CEP
print("Abrindo CEP...")
root.abrir_cep()
root.update()

print("Módulo Atual:", root.modulo_atual)
print("Modules Frame visivel?", root.modules_frame.winfo_ismapped())

# Simula fechar
print("Fechando módulo...")
root.fechar_modulo_atual()
root.update()

print("\n--- DEPOIS DE FECHAR ---")
print("Módulo Atual:", root.modulo_atual)
print("Modules Frame visivel?", root.modules_frame.winfo_ismapped())

print("\nFilhos do modules_frame:")
for child in root.modules_frame.winfo_children():
    print(f"Widget: {child}, Manager: {child.winfo_manager()}, Mapped: {child.winfo_ismapped()}")

root.destroy()
print("Teste concluído.")
