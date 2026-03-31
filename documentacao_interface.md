# Documentação de Interface - SIL3000_IA_WIN

## 1. Padrões de Grid (Tabelas)
O sistema utiliza um padrão avançado de "Excel Mirroring" para exibição de dados e totais.

### 1.1 Configuração do Grid
Toda tela que contém listagem deve herdar de `BaseWindow` e utilizar o método `self.configurar_grid`:
```python
self.configurar_grid(
    columns=("Col1", "Col2"),
    headings=("Título 1", "Título 2"),
    widths=(100, 200),
    aligns=("center", "e")
)
```

### 1.2 Totais Estilo Excel
- **Localização**: Sempre fixos no `summary_frame` (azul marinho `#0D47A1`).
- **Visibilidade**: Devem permanecer estáticos na base do grid, não sumindo durante o scroll.
- **Alinhamento**: Devem utilizar o `self.tree_totais` para garantir sincronia milimétrica com as colunas do grid principal.
- **Formatação**: Valores monetários alinhados à direita (`anchor="e"`), quantidades centralizadas.

## 2. Cores e Identidade
- **Barra Lateral**: `#0D47A1` (Azul Marinho)
- **Cabeçalhos de Grid**: `#D1D5DB` (Cinza Claro) com texto Preto
- **Linhas Zebradas**: Branco (`#FFFFFF`) e Cinza Azulado (`#E2E8F0`)
- **Linha de Totais**: Fundo `#0D47A1`, Texto Branco, Fonte Negrito

## 3. Navegação
- **Acesso Rápido**: Onde houver necessidade de detalhamento (ex: parcelas), clicar uma vez sobre a linha do grid deve abrir automaticamente a tela de detalhes.
- **Scroll**: Todos os grids devem possuir barra de rolagem lateral (`ttk.Scrollbar`) configurada via `BaseWindow`.

## 4. Botões de Rodapé
- **Localização**: Sempre na `self.bottom_bar` (row 3).
- **Ações Padrão**: Fechar Tela (esquerda), Exportar PDF/Excel (direita).
