# 🖥️ Documentação da Interface (Python + CustomTkinter)

Esta documentação reúne soluções técnicas e padrões de arquitetura adotados para evitar bugs visuais e estabilizar a navegação.

---

## ⚠️ Bug de Geometria do CustomTkinter (Tela Branca)

### 🔴 O Problema
Ao transitar entre janelas usando `.pack_forget()` no Dashboard (`modules_frame`) e abrir um módulo novo, as colunas internas e filhos às vezes perdiam o cálculo automático de largura/altura (geometria) do Windows. 
O widget existia na memória, mas a renderização ficava travada em **0x0 pixels**, resultando em uma **tela totalmente branca** (ou cinza).

### 🟢 A Solução (Resize Trick)
Para **forçar** o motor do Windows a disparar o recalculo de layout (Redraw) de forma reativa e instantânea, foi inserido uma rotina de *micro-redimensionamento* de 1 pixel nas funções de transição de tela do `MainHub`:

```python
        self.update()
        w = self.winfo_width(); h = self.winfo_height()
        if w > 1 and h > 1:
             self.geometry(f"{w+1}x{h}")
             self.after(5, lambda: self.geometry(f"{w}x{h}"))
```

### 📍 Onde está implementado?
-   `MainHub.abrir_modulo()`: Dispara ao **entrar** em uma tela (Sugestão, CEP, etc).
-   `MainHub.fechar_modulo_atual()`: Dispara ao **sair** de uma tela e retornar ao Dashboard.

---

## 🔒 Controle de Saída do Sistema

### 🔴 O Problema
Saídas acidentais pelo botão **X** do Windows podem causar perda de processos em background ou travar o socket do Banco de Dados.

### 🟢 A Solução (Trava de Segurança)
-   **Remoção Funcional (Desabilitado)**: Através de chamadas `ctypes.windll.user32`, o botão **X** do canto superior direito da janela principal foi desabilitado (fica cinza).
-   **Bloqueio de Alt+F4**: `self.protocol("WM_DELETE_WINDOW", lambda: None)` bloqueia o atalho de teclado tradicional.
-   **Canal Único**: A saída agora deve ser feita exclusivamente pelo botão **❌ Sair do Sistema** na barra lateral.

---
*MSINFOR Sistemas - 2026*
