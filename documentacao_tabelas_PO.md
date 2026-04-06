# Documentação das Tabelas PO — Sistema de Posto de Combustível

> **Base:** `msinfor` | **Prefixo:** `PO` | **Total:** 25 tabelas
> **Última atualização:** 2026-04-05

---

## 📊 Mapa Geral de Relacionamentos

```
POEmp (Posto)
  │
  ├── POTnq (Tanques do Posto)
  │     └── POLvrCod → POLvr (Livro LMC)
  │     └── POTnqTipCo → POTCo (Tipo de Combustível)
  │
  ├── POBom (Bombas - Configuração)
  │     ├── POBomTnqCo → POTnq (Tanque vinculado)
  │     ├── POTCoCod → POTCo (Tipo de Combustível)
  │     └── Cada bomba = 1 tipo de combustível, puxa de 1 tanque
  │
  ├── POMBo (Cadastro das Bombas)
  │     └── POBxB (Vínculo Bico ↔ Bomba) → POMBoCod + POBomCod
  │
  ├── POBIT (Cadastro de Bicos)
  │     └── Cada bico tem seu velocímetro (POVel1/POVel2)
  │
  ├── POLac (Lacres por Bomba)
  │
  ├── POFor (Fornecedores de Combustíveis)
  │
  ├── POENF (Entrada de NF → Estoque dos Tanques)
  │
  ├── POPer (Períodos de Funcionamento do Caixa — N por posto)
  │
  ├── POCF1 (⭐ MOVIMENTOS PRINCIPAIS — Todas as transações)
  │     ├── POCF1Usu → Frentista
  │     ├── POCF1BomCo → Bomba
  │     ├── POCF1Bic → Bico
  │     ├── POCF1ProCo → Produto/Combustível
  │     ├── POCF1DtaMo → CRMovDta (sistema de vendas)
  │     ├── POCF1SeqMo → CRMovSeq ou POValCod
  │     └── POCF1Sts: A(berto) / F(echado) / C(ancelado)
  │
  ├── POCF2 (Caixa por Frentista — Cabeçalho/Resumo)
  │     └── POCF2Usu → Frentista
  │     └── POCF2DCx → Data Fechamento Caixa
  │
  ├── POCF3 (Caixa por Frentista — Totalização por Tipo Movimento)
  │     └── Vincula a POCF2 via POEmpCod + POCF2Usu + POCF2Tst
  │
  ├── POCF4 (Caixa por Frentista — Movimentos Individuais)
  │     └── Espelho de POCF1 filtrado por frentista
  │
  ├── POCxa1 (Controle de Caixa Geral — independente de frentista)
  ├── POCxa2 (Controle de Caixa Geral — detalhe)
  │
  ├── POVel1 (Velocímetros/Encerrantes por Bico)
  ├── POVel2 (Velocímetros — detalhe/histórico)
  │     └── Base de cálculo para POLMC1 → POLMC2 → POLMC3
  │
  ├── POLMC1 (LMC — Movimentação por Bomba/Tanque diária)
  ├── POLMC2 (LMC — Estoque/Entradas por Tanque)
  ├── POLMC3 (LMC — Resumo de Vendas por Tipo de Combustível)
  │     └── POLMC3TCoC → POTCo (vendas agrupadas por tipo)
  │
  ├── POVal (Cadastro de Vales)
  │
  └── POTCV (Total de Compras e Vendas)
```

---

## 📋 Detalhamento por Tabela

### 1. POEmp — Cadastro de Postos
| Campo | Tipo | Descrição |
|-------|------|-----------|
| POEmpCod | smallint | 🔑 Código do Posto |
| POEmpDes | char(30) | Descrição/Nome |
| POEmpRazSo | varchar(40) | Razão Social |
| PoEmpEnd | varchar(70) | Endereço |
| POEmpCGC | char(20) | CNPJ |
| POEmpI_E | char(20) | Inscrição Estadual |
| POEmpDtaUs | datetime | Data último uso |
| POEmpQtdPe | smallint | Quantidade de Períodos |

### 2. POBom — Bombas (Configuração)
| Campo | Tipo | Descrição |
|-------|------|-----------|
| POEmpCod | smallint | 🔑 Posto |
| POBomCod | smallint | 🔑 Código da Bomba |
| POBomDes | char(25) | Descrição |
| POBomVlrUn | smallmoney | Valor Unitário |
| POTCoCod | smallint | 🔗 Tipo de Combustível |
| POBomTnqCo | smallint | 🔗 Tanque vinculado |
| POBomCusUn | money | Custo Unitário |
| POBomCanal | char(2) | Canal |
| POBomCodPr | decimal | Código do Produto |
| POBomEncer | money | Encerrante |
| POBomSts | char(1) | Status |
| POBomLucMe | money | Lucro Médio |

### 3. POBIT — Cadastro de Bicos
| Campo | Tipo | Descrição |
|-------|------|-----------|
| POEmpCod | smallint | 🔑 Posto |
| POBomCod | smallint | 🔑 Bomba |
| POBITNroIn | decimal | Número Inicial |
| POBITDta | datetime | Data |
| POBITMot | varchar(100) | Motivo |
| POBITNom | varchar(60) | Nome |
| POBITCNPJ | char(20) | CNPJ |
| POBITCPF | char(14) | CPF |

### 4. POBxB — Vínculo Bico ↔ Bomba
| Campo | Tipo | Descrição |
|-------|------|-----------|
| POEmpCod | smallint | 🔑 Posto |
| POMBoCod | smallint | 🔗 Bomba (POMBo) |
| POBomCod | smallint | 🔗 Bomba (POBom) |
| POBxBSts | char(1) | Status |

### 5. POFor — Fornecedores de Combustíveis
| Campo | Tipo | Descrição |
|-------|------|-----------|
| POForCod | smallint | 🔑 Código |
| POForDes | varchar(40) | Descrição/Nome |

### 6. POTnq — Tanques
| Campo | Tipo | Descrição |
|-------|------|-----------|
| POEmpCod | smallint | 🔑 Posto |
| POTnqCod | smallint | 🔑 Código do Tanque |
| POTnqDes | char(30) | Descrição |
| POLvrCod | smallint | 🔗 Livro LMC |
| POTnqTipCo | smallint | 🔗 Tipo de Combustível |
| POTnqCusUn | money | Custo Unitário |
| POTnqQtd | int | Quantidade/Capacidade |

### 7. POTCo — Tipos de Combustível
> Uma bomba só tem um tipo de combustível.

### 8. POLvr — Livros do LMC
> Vinculado aos tanques via POTnq.POLvrCod.

### 9. POLac — Lacres por Bomba

### 10. POMBo — Cadastro das Bombas

### 11. POFor — Fornecedores

### 12. POENF — Entrada de Notas Fiscais
> Dão entrada no estoque dos tanques.

### 13. POPer — Períodos de Funcionamento do Caixa
> O posto pode ter N períodos.

### 14. POVal — Cadastro de Vales

### 15. POTCV — Total de Compras e Vendas

---

## ⭐ POCF1 — Movimentos Principais (Tabela Central)

> Contém TODOS os movimentos do posto. Registra abastecimentos, vendas, 
> qual frentista operou, se o caixa já foi fechado, valores financeiros, 
> leituras de velocímetros, dados fiscais, etc.

### Chaves
| Campo | Tipo | Descrição |
|-------|------|-----------|
| POEmpCod | numeric(3) | 🔑 Empresa/Posto |
| POCF1Tst | datetime | 🔑 Data/Hora Lançamento |
| POCF1Regis | numeric(10) | 🔑 Nº Registro Concentrador |

### Dados do Abastecimento
| Campo | Tipo | Descrição |
|-------|------|-----------|
| POCF1Bic | numeric(2) | Código do Bico |
| POCF1BomCo | numeric(2) | Código da Bomba |
| POCF1ProCo | numeric(18) | Código do Produto |
| POCF1ProDe | char(35) | Descrição do Produto |
| POCF1Qtd | numeric(9,3) | Quantidade (litros) |
| POCF1VelIn | numeric(18,3) | Velocímetro Inicial |
| POCF1VelFi | numeric(18,3) | Velocímetro Final |
| POCF1VlrUn | numeric(12,3) | Valor Unitário |
| POCF1VlrBo | numeric(12,2) | Valor vindo da Bomba |
| POCF1PUBom | numeric(15,4) | Preço Unitário na Bomba |
| POCF1Canal | char(2) | Bico no Concentrador |
| POCF1DataA | date | Data do Abastecimento |
| POCF1HoraA | char(8) | Hora do Abastecimento |

### Valores Financeiros
| Campo | Tipo | Descrição |
|-------|------|-----------|
| POCF1VlrCx | numeric(12,2) | Valor entrou no Caixa |
| POCF1VlrMo | numeric(12,2) | Valor do Movimento |
| POCF1VlrDs | numeric(12,2) | Valor Desconto |
| POCF1VlrAc | numeric(12,2) | Valor Acréscimo |
| POCF1VlrSa | numeric(12,2) | Saldo após Movimento |
| POCF1CusUn | numeric(10,3) | Custo Unitário |
| POCF1VlrLu | numeric(12,2) | Valor Lucro |
| POCF1Mrg | numeric(9,3) | Margem |
| POCF1VUF | numeric(12,4) | Valor Unitário Fiscal (líquido) |
| POCF1VDF | numeric(12,2) | Valor Desconto Fiscal |
| POCF1PECDs | numeric(10,3) | Desconto PEC (Preço Especial Cliente) |
| POCF1VlrCC | numeric(12,2) | Valor adicional Cartão Crédito |
| POCF1NroNf | numeric(10) | Número Nota Fiscal |

### Frentista / Caixa / Status
| Campo | Tipo | Descrição |
|-------|------|-----------|
| POCF1Usu | char(10) | Frentista |
| POCF1TipMo | char(1) | Tipo do Movimento |
| POCF1Sts | char(1) | Status: A(berto) / F(echado) / C(ancelado) |
| POCF1TstFe | datetime | Data/Hora Fechamento Caixa |
| POCF1DCx | datetime | Data/Hora Fechamento (= POCF2DCx = POCxa1DCx) |
| POCF1TstCo | datetime | Data/Hora Confirmação |

### Cancelamento
| Campo | Tipo | Descrição |
|-------|------|-----------|
| POCF1Can | char(1) | Movimento cancelado? |
| POCF1TstCa | datetime | Data/Hora Cancelamento |
| POCF1UsuCa | char(10) | Usuário que cancelou |
| POCF1TipOr | char(1) | Tipo Original (antes de alteração) |
| POCF1LibGe | char(1) | Liberado pelo Gerente |

### Vínculos com Sistema de Vendas
| Campo | Tipo | Descrição |
|-------|------|-----------|
| POCF1FilCo | numeric(3) | Código da Filial |
| POCF1DtaMo | date | Data da CRMovDta |
| POCF1SeqMo | numeric(18) | Sequência CRMovSeq ou POValCod |
| POCF1IteMo | numeric(6) | Item da CRMov4 |

### Fórmulas Calculadas
| Campo | Fórmula | Descrição |
|-------|---------|-----------|
| POCF1CusTo | POCF1Qtd × POCF1CusUn | Custo Total |
| POCF1VTF | POCF1VUF × POCF1Qtd | Valor Total Fiscal |

---

## 💼 POCF2 — Caixa por Frentista (Cabeçalho/Resumo)

> Controle de caixa individual por frentista. Cada abertura/fechamento de caixa
> gera um registro aqui.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| POEmpCod | smallint | 🔑 Posto |
| POCF2Usu | char(10) | 🔑 Frentista |
| POCF2Tst | datetime | 🔑 Data/Hora abertura |
| POCF2Sts | char(1) | Status (A/F) |
| POCF2VlrMa | money | Valor máximo |
| POCF2TSTFe | datetime | Data/Hora fechamento |
| POCF2UsuFe | char(10) | Usuário que fechou |
| POCF2DCx | datetime | Data/Hora fechamento caixa |
| POCF2VlrCo | money | Valor combustível |
| POCF2VlrBo | money | Valor bombas |
| POCF2VlrDe | money | Valor devoluções |
| POCF2VlrRe | money | Valor recebido |
| POCF2RecCa | money | Recebimento em cartão |
| POCF2LucCo | money | Lucro combustível |
| POCF2VlrCh | money | Valor cheques |
| POCF2VlrMo | money | Valor moedas |
| POCF2Qtd2..Qt100 | smallint | Contagem de cédulas (R$2, R$5, R$10, R$20, R$50, R$100) |
| POCF2Msg1..Msg5 | varchar(100) | Mensagens |

---

## 💼 POCF3 — Caixa por Frentista (Totais por Tipo de Movimento)

> Totalização dos movimentos do frentista agrupados por tipo.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| POEmpCod | smallint | 🔑 Posto |
| POCF2Usu | char(10) | 🔗 Frentista (vincula POCF2) |
| POCF2Tst | datetime | 🔗 Abertura (vincula POCF2) |
| POCF3TipMo | char(1) | Tipo do Movimento |
| POCF3VlrFi | money | Valor Final |

---

## 💼 POCF4 — Caixa por Frentista (Movimentos Individuais)

> Espelho dos movimentos de POCF1 filtrado/organizado por frentista.
> Estrutura praticamente idêntica à POCF1.

| Campo | Tipo | Descrição |
|-------|------|-----------|
| POEmpCod | smallint | 🔑 Posto |
| POCF4Tst | datetime | 🔑 Data/Hora |
| POCF4Regis | decimal | 🔑 Nº Registro |
| POCF4Usu | char(10) | Frentista |
| POCF4BomCo | smallint | Bomba |
| POCF4Bic | smallint | Bico |
| POCF4ProCo | decimal | Produto |
| POCF4Qtd | smallmoney | Quantidade |
| POCF4VlrCx | money | Valor Caixa |
| POCF4VlrMo | money | Valor Movimento |
| POCF4VlrUn | money | Valor Unitário |
| POCF4Sts | char(1) | Status (A/F/C) |
| *(demais campos)* | | *Mesma estrutura de POCF1* |

---

## 🔄 Fluxos Operacionais

### Fluxo de Abastecimento:
```
Bico (POBIT) → Bomba (POBom/POMBo) → Tanque (POTnq) → Tipo Combustível (POTCo)
```

### Fluxo de Movimentação:
```
Velocímetros (POVel1/2) → POCF1 (Movimento) → POLMC1 (por Bomba) → POLMC2 (por Tanque) → POLMC3 (por Tipo)
```

### Fluxo de Caixa:
```
POCF1 (Todos os movimentos)
  ├── POCxa1/POCxa2 (Caixa GERAL do posto)
  └── POCF2 (Caixa por FRENTISTA)
        ├── POCF3 (Totais por tipo de movimento)
        └── POCF4 (Movimentos individuais do frentista)
```

### Fluxo de Estoque:
```
POENF (Entrada NF) → POTnq (Estoque Tanque) → POLMC2 (Controle LMC)
POFor (Fornecedor) → POENF (Nota Fiscal)
```
