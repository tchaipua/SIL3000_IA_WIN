import customtkinter as ctk
import ctypes
import time

root = ctk.CTk()
root.title("Teste Desabilitar Close")
root.geometry("400x300")

def desabilitar_close(window):
    try:
        # Pega o handle da janela do Tkinter
        hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
        if not hwnd:
            hwnd = window.winfo_id() # fallback
            
        print(f"HWND: {hwnd}")
        hMenu = ctypes.windll.user32.GetSystemMenu(hwnd, False)
        print(f"HMenu: {hMenu}")
        if hMenu:
            SC_CLOSE = 0xF060
            # MF_BYCOMMAND = 0x0, MF_GRAYED = 0x1, MF_DISABLED = 0x2
            ctypes.windll.user32.EnableMenuItem(hMenu, SC_CLOSE, 1 | 2)
            print("Botão Close cinza devera estar desabilitado.")
    except Exception as e:
        print(f"Erro ctypes: {e}")

# Aguarda a janela ser mapeada
root.update()
desabilitar_close(root)

root.protocol("WM_DELETE_WINDOW", lambda: print("Alt+F4 bloqueado!"))

btn = ctk.CTkButton(root, text="Sair do Script", command=root.destroy)
btn.pack(expand=True)

# Como é background, vou fechar sozinho daqui 5 seg
root.after(5000, root.destroy)

root.mainloop()
