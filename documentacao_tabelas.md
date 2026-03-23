# 📋 Documentação das Tabelas (GeneXus Completo)

Esta documentação reúne definições físicas e lógicas de colunas.

## 🗂️ Lista de Tabelas e Chaves

| Tabela | Descrição | Chave Primária | Nro de Campos |
| :--- | :--- | :--- | :--- |
| `BKMOV2` | BKMOV2 | `BKEMPCOD`, `BKFILCOD`, `BKMOVDTA`, `BKMOVSEQ` | 172 |
| `BKMOV3` | BKMOV3 | `BKFILCOD`, `BKMOVDTA`, `BKMOVSEQ`, `BKMOV3PAR`, `BKEMPCOD` | 67 |
| `BKMOV4` | BKMOV4 | `BKEMPCOD`, `BKFILCOD`, `BKMOVDTA`, `BKMOVSEQ`, `BKPROCOD`, `BKMOV4ITE` | 87 |
| `BKMOV5` | BKMOV5 | `BKEMPCOD`, `BKFILCOD`, `BKMOVDTA`, `BKMOVSEQ`, `BKMOV3PAR`, `BKMov5Cod` | 51 |
| `BKMOV6` | BKMOV6 | `BKEMPCOD`, `BKFILCOD`, `BKMOV6SEQ` | 41 |
| `CCAno` | Controla Banco Ano\Mês | `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCAnoAno` | 8 |
| `CCBco` | Bancos | `CMEmpCod`, `CMFilCod`, `CCBcoCod` | 105 |
| `CCBxM` | Banco x Movimento | `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCBxMCod` | 5 |
| `CCExt` | Controla Data e Valor do Fechamento do Extrato | `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCExtDta` | 13 |
| `CCMes` | Movimento do Banco no Mês | `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCAnoAno`, `CCMesMes` | 24 |
| `CCMov` | Movimentação do Conta Corrente | `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCMovSeqLct` | 78 |
| `CCRBB` | Retorno Extato do B.Brasil | `CCRBBDta`, `CCRBBNroDoc`, `CCRBBD_C`, `CCRBBDes` | 9 |
| `CCRMC` | Controle Remessa de Arquivo para Banco - Boletos | `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CRRMCTip`, `CCRMCCod` | 13 |
| `CCRMD` | Controle Remessa de Arquivo para Banco - Detalhes | `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CRRMCTip`, `CCRMCCod`, `CCRMDBol`, `CCRMDAux` | 29 |
| `CCSeB` | Controle Númeração Boleto/Remessa Por CNPJ | `CMEmpCod`, `CCBcoCod`, `CCSeBCNPJ` | 7 |
| `CCTMM` | Tipo de Movimento por MÊs | `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCAnoAno`, `CCMesMes`, `CCTMMCod` | 32 |
| `CCTmv` | Tipo de Movimentação Bancária | `CMEmpCod`, `CMFilCod`, `CCTmvCod` | 16 |
| `CEAbc` | CEAbc | `med_abc` | 35 |
| `CEAgr` | Agrupador Produtos | `CMEmpCod`, `CEAgrCod` | 34 |
| `CEAno` | Vendas Produtos Anual | `CMEmpCod`, `CMFilCod`, `CEProCod`, `CEAno` | 25 |
| `CEBFI` | Arquivo CadTxt Filizola | `CEBFICodPro` | 5 |
| `CEBFS` | Arquivo Setortxt Filizola | `CEBFSDes`, `CEBFSProCod` | 4 |
| `CEBTI` | Itens da Balanca Toledo | `CEBTIDepCod`, `CEBTIEtq`, `CEBTIUndPes`, `CEBTICodPro` | 7 |
| `CECA1` | Características dos Produtos | `CMEmpCod`, `CECA1COD` | 5 |
| `CECA2` | Características do Produto 02 | `CMEmpCod`, `CECA1COD`, `CECA2COD` | 7 |
| `CECdx1` | Cardex 01 | `CMEmpCod`, `CMFilCod`, `CECdxDta` | 6 |
| `CECdx2` | Cardex 02 | `CMEmpCod`, `CMFilCod`, `CECdxDta`, `CECdx2Seq` | 53 |
| `CECdx3` | Divergências Estoque x CECdx | `CMEmpCod`, `CMFilCod`, `CECdx3Dta`, `CECdx3ProCod` | 10 |
| `CECEM` | Custo Estoque Mensal - Lazuli | `CMEmpCod`, `CMFilCod`, `CECEMAMe` | 9 |
| `CECES` | Cadastro de CEST | `CECESCod` | 10 |
| `CECGS` | Convênio com Grupo e SubGrupo | `CMEmpCod`, `CECGSCod`, `CEGrpCod`, `CESgrCod` | 8 |
| `CECla` | Tabela Classificação Produtos | `CMEmpCod`, `CEClaCod` | 3 |
| `CECLF` | Cadastro de Classificação Fiscal (Reforma Tributária) | `CMEmpCod`, `CECLFCod` | 11 |
| `CECot1` | Cadastro Cotações | `CMEmpCod`, `CMFilCod`, `CECot1Seq` | 9 |
| `CECot2` | Produtos da Cotacao | `CMEmpCod`, `CMFilCod`, `CECot1Seq`, `CEProCod`, `CECot2ProDes` | 22 |
| `CECot3` | Fornecedores da Cotação | `CMEmpCod`, `CMFilCod`, `CECot1Seq`, `CPCliCod` | 16 |
| `CECot4` | Cotacao dos Fornecedores | `CMEmpCod`, `CMFilCod`, `CECot1Seq`, `CPCliCod`, `CECot2ProDes`, `CEProCod` | 34 |
| `CECrs` | Tabela de Cores | `CMEmpCod`, `CECrsCod` | 12 |
| `CEDCV1` | Desconto Compra Venda 01 | `CMEmpCod`, `CMFilCod`, `CEDCV1Cod` | 20 |
| `CEDCV2` | Desconto Compra Venda 02 | `CMEmpCod`, `CMFilCod`, `CEDCV1Cod`, `CEProCod` | 45 |
| `CEDia` | Acumulo Estoque Diário | `CMEmpCod`, `CMFilCod`, `CEProCod`, `CEAno`, `CEMes`, `CEDia` | 83 |
| `CEEmb` | Cadastro de Embalagens | `CMEmpCod`, `CEEmbCod` | 12 |
| `CEFas` | Fases do Produto até Entrega Final | `CMEmpCod`, `CEFasCod` | 6 |
| `CEFat` | Tabela Fator Produtos | `CMEmpCod`, `CEFatCod` | 7 |
| `CEFaU` | Configura Usuários nas Fases da Entrega | `CMEmpCod`, `CEFaUNom`, `CEFasCod` | 20 |
| `CEGR1` | Grade de Produtos 01 | `CMEmpCod`, `CEGr1Cod` | 5 |
| `CEGR2` | Grade de Produtos | `CMEmpCod`, `CEGr1Cod`, `CEGr2Nro` | 9 |
| `CEGrp` | Grupos de Produtos | `CMEmpCod`, `CEGrpCod` | 22 |
| `CEHPC` | CRM Clientes x Produtos | `CMEmpCod`, `CMFilCod`, `CEHPCTIP`, `CEHPCCLICOD`, `CEHPCPROCOD`, `CEHPCTST` | 16 |
| `CEImp` | Impressoras | `CMEmpCod`, `CEImpCod` | 4 |
| `CEInv` | Diferenças do Estoque | `CMEmpCod`, `CEInvProCod` | 6 |
| `CEKT1` | Kit de Produtos 1 Nivel | `CMEmpCod`, `CEKT1CodOrg` | 13 |
| `CEKT2` | Kit de Produtos 2  Nivel | `CMEmpCod`, `CEKT1CodOrg`, `CEKT2CodPro` | 27 |
| `CELab` | Laboratórios ( Farmacia ) | `CMEmpCod`, `CEProNomLabFar` | 9 |
| `CEMes` | Acumulo Estoque Mensal | `CMEmpCod`, `CMFilCod`, `CEProCod`, `CEAno`, `CEMes` | 57 |
| `CEMst` | Produtos da Master Informática | `CEMstProCod` | 3 |
| `CENBM` | Nomenclatura Brasileira de Medicamentos | `CENBMSeq` | 4 |
| `CENCG` | NCM Geral | `CENCGCod` | 2 |
| `CENCM` | Nomenclatura Comum Mercosul | `CENCMCod` | 3 |
| `CENCU` | NCM Geral por UF | `CENCGCod`, `CENCUUF` | 4 |
| `CENFC` | Cabeçalho da Nota Fiscal | `CMEmpCod`, `CMFilCod`, `CENFCSeq` | 246 |
| `CENFD` | Duplicatas da Nota Fiscal | `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFDCod` | 9 |
| `CENFE` | Distribuição / Manifesto DFe - Eventos | `CMEmpCod`, `CMFilCod`, `CENFNNSU`, `CENFNTipEve`, `CENFNSeqEve` | 27 |
| `CENFK` | Nota Fiscal - Formas de Pagamento | `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFKDet` | 12 |
| `CENFM` | Mensagens da Nota Fiscal / NFe | `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFMSeq` | 10 |
| `CENFN` | Distribuição / Manifesto DFe | `CMEmpCod`, `CMFilCod`, `CENFNNSU` | 20 |
| `CENFO1` | Carta Correção da Nota Fiscal | `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFO1TST` | 15 |
| `CENFO2` | Carta Correção da Nota Fiscal | `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFO1TST`, `CENFO2COD` | 24 |
| `CENFP` | Produtos da Nota Fiscal | `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CEProCod`, `CENFPIte` | 191 |
| `CENFR` | Resumo Icms por Natureza Operação da Nota Fiscal | `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFRTip`, `CENFRCod` | 9 |
| `CENFV` | COO Vinculados à CENFC | `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFVSeq` | 6 |
| `CEOco` | Ocorrências do Produto | `CMEmpCod`, `CEProCod`, `CEOcoTst` | 5 |
| `CEPAP` | Parâmetros da Atualização de Preços da Farmácia | `CEPAPCOD` | 3 |
| `CEPCA` | Produtos x Características | `CMEmpCod`, `CEProACod`, `CECA1COD` | 15 |
| `CEPCN` | Estoque do Produto por Cor e N° | `CMEmpCod`, `CEProCod`, `CEProFilCod`, `CEPCNNro`, `CEPCNCor` | 27 |
| `CEPEC` | Preços Especiais para o Cliente | `CMEmpCod`, `CRCliCod`, `CEPecProCod` | 12 |
| `CEPPr` | Produtos da Profarma | `CEPPrCodEan` | 10 |
| `CEPRF` | Produtos x Filial - Somente Consulta | `CMEmpCod`, `CEPRFCOD`, `CMFilCod` | 7 |
| `CEPRG` | Tabelas Genéricas do Produto | `CMEmpCod`, `CEProCod`, `CMGenCod` | 6 |
| `CEPRI` | Detalhes Genérico dos Produtos | `CMEmpCod`, `CEProCod`, `CMGenCod`, `CEPriSeq` | 8 |
| `CEPrL` | Lotes do Produto | `CMEmpCod`, `CEProCod`, `CEProFilCod`, `CEPrLLot` | 28 |
| `CEPro` | Produtos | `CMEmpCod`, `CEProCod` | 289 |
| `CEProA` | Dados Auxliares do Produto | `CMEmpCod`, `CEProACod` | 28 |
| `CEProC` | Códigos de Barra do Produto | `CMEmpCod`, `CEProCod`, `CEProCCod` | 8 |
| `CEProF` | Produtos da Filial | `CMEmpCod`, `CEProCod`, `CEProFilCod` | 37 |
| `CEProL` | Produtos Local | `CEProLCodBar` | 32 |
| `CEProO` | Observações Adicionais do Produto | `CMEmpCod`, `CEProOCod`, `CEProOLin` | 44 |
| `CEProU` | Cadastro de % IVA por Estado | `CMEmpCod`, `CEProCod`, `CEProUF` | 13 |
| `CEPrU` | Configurações Fiscais do Produto por Estado | `CMEmpCod`, `CEProCod`, `CEPrUUF` | 12 |
| `CEPRV` | Produtos x Vendedores Comissão | `CMEmpCod`, `CEProCod`, `CEPRVUsu` | 6 |
| `CEPxF` | Tabela de Produto x Fornecedor | `CMEmpCod`, `CMFilCod`, `CEPxFDta`, `CEProCod` | 29 |
| `CEPxI` | Produtos x Impressoras | `CMEmpCod`, `CEProCod`, `CEImpCod` | 5 |
| `CERep` | Representantes | `CMEmpCod`, `CERepCod` | 4 |
| `CERIL` | Retorno do Inventário Via Leitor | `CMEmpCod`, `CMFilCod`, `CERILNomInv`, `CERILProCod` | 16 |
| `CERPF` | Produto x Referência do Fornecedor | `CMEmpCod`, `CPCliCod`, `CERPFRef`, `CERPFCodPro` | 12 |
| `CERPS1` | RPS Gerados | `CMEmpCod`, `CMFilCod`, `CERPSTipo`, `CERPSSerie`, `CERPSNum` | 71 |
| `CERPS2` | Lote de RPS | `CMEmpCod`, `CMFilCod`, `CERPSLote` | 8 |
| `CERPS3` | Itens do RPS | `CMEmpCod`, `CMFilCod`, `CERPSTipo`, `CERPSSerie`, `CERPSNum`, `CERPSItem` | 76 |
| `CERxB` | Codigo da Rede Total x Codigo | `CERxBCodRed` | 3 |
| `CESgr` | Sub-Grupo de Produtos | `CMEmpCod`, `CEGrpCod`, `CESgrCod` | 42 |
| `CETGA` | Total Grupo Anual | `CMEmpCod`, `CETGAAno`, `CEGrpCod` | 9 |
| `CETM1` | Temp. Vendas do Período | `CMEmpCod`, `CETM1ProDes`, `CEProCod`, `CETm1NroCxa`, `CETm1IDEPCN`, `CETm1Ite` | 54 |
| `CETm2` | Tabela Temporária | `CMEmpCod`, `CMFilCod`, `CETm2DesPro`, `CETm2Prg`, `CETM2CodBar`, `CETm2ProCod` | 73 |
| `CETM21` | Temp. Totais Gr-Sub-Grp | `CMEmpCod`, `CETM21CheOut` | 4 |
| `CETM22` | Temp. Totais Grupo | `CMEmpCod`, `CETM21CheOut`, `CEGrpCod` | 20 |
| `CETM23` | Temp. Totais Sub-Grupo | `CMEmpCod`, `CETM21CheOut`, `CEGrpCod`, `CESgrCod` | 38 |
| `CETM31` | TCE11D | `CETM31REF` | 1 |
| `CETM32` | Temporaria | `CETM31REF`, `CETM32CrsCod` | 2 |
| `CETM33` | Temporaria | `CETM31REF`, `CETM32CrsCod`, `CETM33Nro` | 4 |
| `CETM34` | Temporaria | `CETM31REF`, `CETM34Nro` | 3 |
| `CETM4` | Temporária Produto Cor/Nº | `CMEmpCod`, `CEProCod`, `CETM4FilCod`, `CETM4Cor` | 49 |
| `CETMP1` | Tabela Temporaria 01 | `CMEmpCod`, `CMFilCod`, `CETMP1IdeFor`, `CETMP1ProDes`, `CETMP1ProCod`, `CETMP1Prg`, `CETMP1CUsu` | 41 |
| `CETN1` | Controle de Tintas CORAL | `CETNCodTin` | 2 |
| `CETN2` | Controle de Tintas CORAL Produtos | `CETNCodTin`, `CETNCodCom` | 19 |
| `CETP1` | Configuração Tabelas de Preço | `CMEmpCod`, `CMFilCod`, `CETP1Cod` | 4 |
| `CETP2` | Configura Tabela de Preço 02 | `CMEmpCod`, `CMFilCod`, `CETP1Cod`, `CETP2Sit` | 9 |
| `CETri` | Acumulo Estoque Trimestral | `CMEmpCod`, `CMFilCod`, `CEAno`, `CETriCod`, `CEProCod` | 16 |
| `CETRS1` | Sequência das Notas Transferências | `CMEmpCod`, `CETrs1Dta` | 5 |
| `CETRS2` | Cabeçalho da Transferência | `CMEmpCod`, `CETrs2FilOrg`, `CETrs2FilDes`, `CETrs1Dta`, `CETrs2Seq` | 27 |
| `CETRS3` | Itens da Nota Transferência | `CMEmpCod`, `CETrs2FilOrg`, `CETrs2FilDes`, `CETrs1Dta`, `CETrs2Seq`, `CETrs3CodCha` | 48 |
| `CETrs4` | Transferência de Produtos Tratando Cor e N° | `CMEmpCod`, `CETrs2FilOrg`, `CETrs2FilDes`, `CETrs1Dta`, `CETrs2Seq`, `CETrs3CodCha`, `CETrs4Cor`, `CETrs4Nro` | 17 |
| `CETSA` | Total SubGrupo Anual | `CMEmpCod`, `CETGAAno`, `CEGrpCod`, `CESgrCod` | 16 |
| `CETSM` | Total SubGrupo Mensal | `CMEmpCod`, `CETGAAno`, `CEGrpCod`, `CESgrCod`, `CETSMMes` | 22 |
| `CEVar` | Cadastro de Variações | `CMEmpCod`, `CEVarCod` | 5 |
| `CEVas` | Vasilhames | `CMEmpCod`, `CEVasCod` | 6 |
| `CFDes1` | Controle Horas Desenvolvimento | `CMEmpCod`, `CFFunCod`, `CFDes1Dta` | 9 |
| `CFDes2` | Controle Funcionários Desenvolvimento | `CMEmpCod`, `CFFunCod`, `CFDes1Dta`, `CFDes2TstIni` | 21 |
| `CFFun` | Funcionarios | `CMEmpCod`, `CFFunCod` | 60 |
| `CFFUQ` | Peças Produzidas pelo Funcionário | `CMEmpCod`, `CFFunCod`, `CFFuQDta`, `CFFuQSeq` | 74 |
| `CFMov` | Movimentacao do Funcionario | `CMEmpCod`, `CFFunCod`, `CFMovDta`, `CFVDeCod`, `CFMovSeq` | 59 |
| `CFTip` | Tipo de Funcionario | `CMEmpCod`, `CFTipCod` | 8 |
| `CFVDe` | Codigos Vencimentos\Descontos | `CMEmpCod`, `CFVDeCod` | 14 |
| `CLHis` | Histórico Entrada/Saida Clube | `CLTt1Cod`, `CLTt2Seq`, `CLHisTstEnt` | 10 |
| `CLTt1` | Cadastro Títulos | `CLTt1Cod` | 10 |
| `CLTt2` | Cadastro de Títulos - Dependentes | `CLTt1Cod`, `CLTt2Seq` | 22 |
| `CLTt3` | Controle de Suspensão | `CLTt1Cod`, `CLTt2Seq`, `CLTt3Seq` | 15 |
| `CMAgA` | Agendamento Alterações por Usuário | `CMEmpCod`, `CMFilCod`, `CMAgeUsu`, `CMAgeDta`, `CMAgeHra`, `CMAgeDtHrA` | 36 |
| `CMAge` | Agenda de Compromissos | `CMEmpCod`, `CMFilCod`, `CMAgeUsu`, `CMAgeDta`, `CMAgeHra` | 241 |
| `CMAgP` | Produtos da Agenda de Compromisso | `CMEmpCod`, `CMFilCod`, `CMAgeUsu`, `CMAgeDta`, `CMAgeHra`, `CMAgPIte` | 21 |
| `CMAgx` | Atendimento - Exames | `CMEmpCod`, `CMFilCod`, `CMAgeUsu`, `CMAgeDta`, `CMAgeHra`, `CMAgxSeqEx` | 14 |
| `CMAno` | Totais Ano\Mes - Tipo de Combustível | `CMEmpCod`, `CMAnoOrg`, `CMAnoFil`, `CMAnoAno`, `CMAnoChv1` | 48 |
| `CMAud` | Auditoria | `CMEmpCod`, `CMFilCod`, `CMAudCod` | 17 |
| `CMAut` | Controle Autoridade - Usuários x Programa | `CMEmpCod`, `CMAutFil`, `CMAutUsu`, `CMAutPrg` | 6 |
| `CMBen` | Cadastro Código Beneficio Por Estado | `CMUFCod`, `CMBenCod` | 17 |
| `CMCA1` | Curva ABC Cabeçalho | `CMEmpCod`, `CMFilCod`, `CMCA1Usu` | 16 |
| `CMCA2` | Curva ABC - Produtos | `CMEmpCod`, `CMFilCod`, `CMCA1Usu`, `CMCA2Cod` | 63 |
| `CMCal1` | Calculadora 1 | `CMCal1CheOut` | 4 |
| `CMCal2` |  Calculadora 2 | `CMCal1CheOut`, `CMCal2Seq` | 6 |
| `CMCCu` | Centro de Custo | `CMEmpCod`, `CMFilCod`, `CMCCuCod` | 11 |
| `CMCEP` | C.E.P. | `CMCEPCod` | 12 |
| `cmcepl` | cmcepl | `CmCepLCod`, `CmCepLLog` | 7 |
| `CMCTe1` | Cadastro Telefone 01 | `CMEmpCod`, `CMFilCod`, `CMCTe1Cod` | 10 |
| `CMCTe2` | Cadastro Telefone 02 | `CMEmpCod`, `CMFilCod`, `CMCTe1Cod`, `CMCTe2Cod` | 16 |
| `CMCV1` | Conversão de Arquivos | `CMCV1TAB` | 3 |
| `CMCV2` | Conversão de Arquivos 2 | `CMCV1TAB`, `CMCV2COD` | 11 |
| `CMCVG` | Comissão do Vendedor por Grupo | `CMEmpCod`, `CMUsuNom`, `CMCVGGrpCod` | 5 |
| `CmEmp` | Empresa | `CMEmpCod` | 137 |
| `CMExA` | Cadastro de Exames | `CMEmpCod`, `CMExACod` | 8 |
| `CMExF` |  T509 | `CMEmpCod`, `CMExACod`, `CMExFCod` | 11 |
| `CMEXN` | Tabela Código EAN (Código de Barras) X NCM | `CMEXNEAN` | 2 |
| `CMFer` | Cadastro de Feriados | `CMFerDta`, `CMFerCEP` | 4 |
| `CMFIA` | CMFIL Auxiliar | `CMEmpCod`, `CMFiACod` | 116 |
| `CMFil` | Filiais | `CMEmpCod`, `CMFilCod` | 265 |
| `CMFt1` | Controle de Fotos 01 | `CMEmpCod`, `CMFt1Org` | 4 |
| `CMFt2` | Controle de Fotos 02 | `CMEmpCod`, `CMFt1Org`, `CMFt2Cod`, `CMFt2Seq` | 13 |
| `CMGen` | Descrições Genéricas por Tipo | `CMEmpCod`, `CMGenCod` | 93 |
| `CMGenO` | Tabela Genérica Códigos - Detalhes | `CMEmpCod`, `CMGenCod`, `CMGenSeq` | 96 |
| `CMGer` | Tabela Genérica para Usar com SDT | `CMEmpCod`, `CMGerFil`, `CMGerTab`, `CMGerCmp` | 5 |
| `CMGR1` | Controle de Gráficos - Configurações | `CMEmpCod`, `CMFilCod`, `CMGr1Usu`, `CMGr1Nom` | 28 |
| `CMGR2` | Controle Gráficos - Valores | `CMEmpCod`, `CMFilCod`, `CMGr1Usu`, `CMGr1Nom`, `CMGr2Cod` | 39 |
| `CMGTX` | Gerar Arquivo Txt | `CMGTXSEQ` | 6 |
| `CMHBc` | Histórico do Backup | `CMHBcDta`, `CMHBcHor` | 3 |
| `CMHEA` | Histórico de Envio de Arquivo | `CMEmpCod`, `CMFilCod`, `CMHEATip`, `CMHEATST` | 8 |
| `CMIdx` | Tabela Usada para Indexar | `CMIdxUsu`, `CMIdxCod` | 2 |
| `CMIFi1` | Impressora Fiscal 01 | `CMEmpCod`, `CMFilCod`, `CMIFiCod` | 21 |
| `CMIFi2` | Impressora Fiscal 2 | `CMEmpCod`, `CMFilCod`, `CMIFiCod`, `CMIFi2PrcIcm` | 28 |
| `CMLib` | TCM02AA | `CMLibCodMs`, `CMLibDtahra` | 11 |
| `CMMes` | Tabela Acumulo Mês | `CMEmpCod`, `CMAnoOrg`, `CMAnoFil`, `CMAnoAno`, `CMAnoChv1`, `CMMesMes` | 83 |
| `CMMMS` | Controla Mensalidades da MSINFOR | `CMEmpCod`, `CMFilCod`, `CMMMSTip`, `CMMMSQtd` | 11 |
| `CMMoe` | Cadastro Moedas | `CMMoeCod` | 8 |
| `CMMoeD` | Cadastro Cotação da Moeda Diário | `CMMoeCod`, `CMMoeDDta` | 11 |
| `CMMSA` | Total Clientes MSINFOR Anual | `CMEmpCod`, `CMFilCod`, `CMMSAAno` | 11 |
| `CMMSI` | Comunicação Entre MSINFOR - Clientes | `CMMSICOD` | 2 |
| `CMMSP` | Total de Clientes Perdidos no Ano | `CMEmpCod`, `CMFilCod`, `CMMSAAno`, `CMMSPCli`, `CMMSPDta` | 14 |
| `CMMun` | Municípios com Código do IBGE | `CMUFCod`, `CMMunIBGE` | 11 |
| `CMNCM` | NCM - Auxiliar | `CMNCMNBM` | 7 |
| `CMNHD` | Nro de série dos HD dos micros | `CMEmpCod`, `CMNHDSeq` | 5 |
| `CMNOP` | Natureza da Operação CFOP | `CMNOpCod` | 13 |
| `CMOTE` | Tabela Operadoras | `CMOTeCod` | 2 |
| `CMPm1` | Parâmetros da Estação | `CMPm1NroMic` | 112 |
| `CMPm2` | Parametros | `CMPm2Cod` | 9 |
| `CMPMT` | Parâmetros do Microterminal | `CMPMTCod` | 71 |
| `CMPNF` | Parâmentros da NFe | `CMEmpCod`, `CMFilCod`, `CMPNFCod` | 17 |
| `CMPrD` | Manutenção da Descrição Programa - MSINFOR | `CMPrDNom` | 4 |
| `CMPrF` | Programas - Parâmetros por Filial | `CMEmpCod`, `CMPrFFil`, `CMPrgnom` | 80 |
| `CMPrg` | Programas | `CMEmpCod`, `CMPrgnom` | 74 |
| `CMPro` | Cadastro Profissionais | `CMProCod`, `CMProTip` | 5 |
| `CMPUL` | Programas Utilizados Local | `CMPULCodMs`, `CMPULProNa` | 3 |
| `CMTAB` | Tabelas do Sistema | `CMTabNom` | 3 |
| `CMTBC` | Campos das Tabelas | `CMTBNNom`, `CMTBCNom` | 10 |
| `CMTBN` | Grava Nomes Tabelas do Sistema e os Campos - Via Instrução SQL | `CMTBNNom` | 4 |
| `CMTFF` | Transferência Entre Filiais | `CMEmpCod`, `CMFilCod`, `CMTFFFil` | 4 |
| `CMTip` | Temporaria Tipo Cliente\Fornec | `CMEmpCod`, `CMTipCod`, `CMTipCF` | 9 |
| `CMTM1` | Temporária Genérica | `CMTM1CHV1`, `CMTM1CHV2`, `CMTM1CHV3` | 11 |
| `CMTM2` | Temporária Genérica 02 | `CMTM2CHV01`, `CMTM2CHV02`, `CMTM2CHV03`, `CMTM2CHV04`, `CMTM2CHV05`, `CMTM2CHV06` | 65 |
| `CMTMS` | Telefones da MS-Informática | `CMTMSCod` | 3 |
| `CMTOP` | Natureza Operação Fiscal | `CMTOPCod` | 221 |
| `CMTOPR` | Classificação Tribuária Por Tipo de Operação (Reforma Tributária) | `CMTOPCod`, `CMTopRCod` | 223 |
| `CMTra` | Transportadora | `CMTraCod` | 17 |
| `CMTxt` | Importa Texto Geral | `CMTxtGer` | 3 |
| `CMUAt` | Últimas Atualizações das Tabel | `CMUAtNomTab` | 3 |
| `CMUBH` | Banco de Horas do Usuário | `CMEmpCod`, `CMUsuNom`, `CMUBHAMe` | 12 |
| `CMUF` | Estados | `CMUFCod` | 14 |
| `CMUFF` | Parâmetros da UF por Filial | `CMUFCod`, `CMUFFilCod` | 3 |
| `CMUsA` | Atendimento Realizado pelos Usuários | `CMEmpCod`, `CMUsuNom`, `CMUsHDta`, `CMUsAEnt` | 18 |
| `CMUsC` | Configura Preço Consulta Por Usuário \ Convênio | `CMEmpCod`, `CMUsuNom`, `CMUsCCod` | 5 |
| `CMUsF` | Usuário - Filiais Que Possui Acesso | `CMUsuNom`, `CMUsuEmp`, `CMUsuFil` | 4 |
| `CMUsH` | Horários dos Funcionários | `CMEmpCod`, `CMUsuNom`, `CMUsHDta` | 41 |
| `CMUsM` | Metas de Vendas por Vendedor | `CMEmpCod`, `CMUsuNom`, `CMUsMAMe` | 33 |
| `CMUSP` | Histórico de Acesso de Programas | `CMEmpCod`, `CMUsuNom`, `CMUSPPrg`, `CMUSPTST` | 17 |
| `CmUsu` | Usuarios | `CMEmpCod`, `CMUsuNom` | 66 |
| `CMVD1` | Cadastros de Vencimentos/Descontos VD | `CMVD1Cod` | 2 |
| `CMVen` | Vencimentos | `CMEmpCod`, `CMVenSeq` | 23 |
| `CMWht` | Controle Mensagens WhatsApp | `CMEmpCod`, `CMFilCod`, `CMWhtSeq` | 18 |
| `CMXML` | Controla Arquivos XML | `CMXmlNom` | 22 |
| `CMXMLI` | Controle Arquivos Por Imposto | `CMXmlNom`, `CMXmlImp` | 24 |
| `COLUNAS` | Colunas | `object_id`, `Colunanome` | 2 |
| `CPCCr` | Cadastro Cartões de Crédito | `CMEmpCod`, `CMFilCod`, `CPCCrCod` | 10 |
| `CPCLI` | Cadastro Fornecedor | `CMEmpCod`, `CPCliCod` | 51 |
| `CPCR1` | Controle Requisições - Ótica | `CMEmpCod`, `CMFilCod`, `CPCliCod`, `CPCR1Dta`, `CPCR1Org` | 12 |
| `CPCR2` | Controle Requisições - Ótica | `CMEmpCod`, `CMFilCod`, `CPCliCod`, `CPCR1Dta`, `CPCR1Org`, `CPCR2NroReq` | 28 |
| `CPCR3` | Controle Requisições - Ótica | `CMEmpCod`, `CMFilCod`, `CPCliCod`, `CPCR1Dta`, `CPCR1Org`, `CPCR2NroReq`, `CPCR3Ite` | 31 |
| `CPCXP` | Fornecedor x CFOP | `CMEmpCod`, `CPCliCod`, `CPCliCFOPO` | 4 |
| `CPDevC` | Cabeçalho Devolução de Produtos da Nota - | `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPDevCTST` | 23 |
| `CPDevP` | Devolução de Produtos da Nota - Produtos | `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPDevCTST`, `CPMov4Ite` | 33 |
| `CPGF1` | Grupos de Fornecedores | `CMEmpCod`, `CPGF1Cod` | 4 |
| `CPGF2` | Grupo de Fornecedores | `CMEmpCod`, `CPGF1Cod`, `CPGF2Cod` | 7 |
| `CPMov1` | Sequencia das Compras | `CMEmpCod`, `CMFilCod`, `CPMovDta` | 5 |
| `CPMov2` | Cabecalho das compras | `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq` | 149 |
| `CPMov3` | Parcelas da Compra | `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMov3Par` | 169 |
| `CPMov4` | Produtos da Compra | `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMov4Ite` | 211 |
| `CPMovG` | Lançamento Contas a Pagar por Grade | `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMov4Ite`, `CPMovGNro`, `CPMovGCor` | 17 |
| `CPMovI` | Impostos da Nota | `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMovIOrg`, `CPMovICod` | 31 |
| `CPMovL` | Cadastro Produtos Compra - Lotes | `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMov4Ite`, `CPMovLNum` | 11 |
| `CPMovR` | Requisições da Nota | `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMovRReq`, `CPMovRPro` | 19 |
| `CPTip` | Tipo de Fornecedor | `CMEmpCod`, `CPTipCod` | 10 |
| `CPTmp1` | Temporária | `CMEmpCod`, `CMFilCod`, `CPTmp1Cod` | 11 |
| `CPTPF` | Tabela de Preço do Fornecedor | `CMEmpCod`, `CPCliCod`, `CMFilCod`, `CPTPFProCod` | 19 |
| `CRCCr` | Cartao de Crédito | `CMEmpCod`, `CMFilCod`, `CRCCrCod` | 25 |
| `CRCCV` | Controle Contra Vale | `CMEmpCod`, `CMFilCod`, `CRCCVCod` | 40 |
| `CRCen` | Endereços do Cliente | `CMEmpCod`, `CRCliCod`, `CRCEnTip` | 15 |
| `CRChA` | Cheques Avulsos | `CMEmpCod`, `CMFilCod`, `CRChACod` | 52 |
| `CRCla` | Cadastro de Associados Sindicato | `CMEmpCod`, `CRClaCod` | 64 |
| `CRCLD` | Dados do Cliente | `CMEmpCod`, `CRCliCod`, `CRCLDIte` | 79 |
| `CRClG1` | Gastos Cliente 01 - VD | `CMEmpCod`, `CRCliCod`, `CRCLG1AnoMes` | 5 |
| `CRClG2` | Gastos Cliente 02 - VD | `CMEmpCod`, `CRCliCod`, `CRCLG1AnoMes`, `CRClG2VD` | 14 |
| `CRCli` | Cadastro de Clientes | `CMEmpCod`, `CRCliCod` | 210 |
| `CRCliC` | Características do Cliente | `CMEmpCod`, `CRCliCod`, `CRCrtCod` | 10 |
| `CRCLO` | Observações Gerais do Cliente | `CMEmpCod`, `CMFilCod`, `CRCliCod`, `CRClODta` | 47 |
| `CRClr` | Receituário Médito | `CMEmpCod`, `CRClrMovFil`, `CRClrMovDta`, `CRClrMovSeq`, `CRClRSeq` | 132 |
| `CRClT` | Telefones/Senhas do Cliente | `CMEmpCod`, `CRCliCod`, `CRCltSeq`, `CMOTeCod` | 16 |
| `CRClV` | Cadastro Clientes x Veículos | `CMEmpCod`, `CRCliCod`, `CRClVSeq` | 17 |
| `CRClVH` | Histórico Movimentos Veículos/Animais | `CMEmpCod`, `CRCliCod`, `CRClVSeq`, `CRClVHTST` | 21 |
| `CRCM1` | Controle Cartão Magnético | `CMEmpCod`, `CMFilCod`, `CRCM1Cod` | 12 |
| `CRCP1` | Condições de Pagamento | `CMEmpCod`, `CMFilCod`, `CRCP1Cod` | 11 |
| `CRCP2` | Condições de Pagamento | `CMEmpCod`, `CMFilCod`, `CRCP1Cod`, `CRCP2Par` | 13 |
| `CRCre1` | Controla Crédito Cliente 01 | `CMEmpCod`, `CRCliCod`, `CRCre1Dta` | 14 |
| `CRCre2` | Controla Crédito Cliente 02 | `CMEmpCod`, `CRCliCod`, `CRCre1Dta`, `CRCre2Seq` | 42 |
| `CRCrt` | Características | `CMEmpCod`, `CRCrtCod` | 7 |
| `CRCxP` | Produtos Periódicos | `CMEmpCod`, `CRCliCod`, `CRCxPProCod` | 10 |
| `CRDep` | Dependentes | `CMEmpCod`, `CRCliCod`, `CRDepNom` | 35 |
| `CRDepC` | Características do Dependente | `CMEmpCod`, `CRCliCod`, `CRDepNom`, `CRDepCrt` | 11 |
| `CREnc1` | Tabela Encomendas \ Entregas 1 | `CMEmpCod`, `CMFilCod`, `CREnc1Dta`, `CREnc1Hra` | 16 |
| `CREnc2` | Tabela Encomendas \ Entregas 2 | `CMEmpCod`, `CMFilCod`, `CREnc1Dta`, `CREnc1Hra`, `CREnc2ProCod` | 22 |
| `CRFPC` | Cabeçalho Venda Farmácia Popular | `CMEmpCod`, `CMFilCod`, `CRFPCCod` | 24 |
| `CRFPM` | Mercadorias da Farmácia Popular | `CMEmpCod`, `CMFilCod`, `CRFPCCod`, `CEProCod` | 33 |
| `CRFPP` | Parâmetros da Farmácia Popular | `CMEmpCod`, `CMFilCod`, `CRFPPCod` | 11 |
| `CRFPV` | Dados do Cupom Fiscal Vinculado da Farmácia Popular | `CMEmpCod`, `CMFilCod`, `CRFPCCod`, `CRFPVSeq` | 5 |
| `CRHCL1` | Histórico Comercial do Cliente | `CMEmpCod`, `CRHCl1CliCod` | 14 |
| `CRHCL2` | Histórico Comercial do Cliente 02 | `CMEmpCod`, `CRHCl1CliCod`, `CRHCl2AnoMes` | 19 |
| `CRHRB` | Histórico Retorno de Boletos | `CRHRBCod`, `CRHRBBco`, `CRHRBAge` | 20 |
| `CRHVC` | Histórico Cancelamento Venda e Itens | `CMEmpCod`, `CMFilCod`, `CRHVCTST`, `CRHVCCHEOUT`, `CRHVCUSU`, `CRHVCProCod` | 10 |
| `CRIRR` | Tabela Cliente x Produto Retenção Imposto de Renda | `CMEmpCod`, `CRIRRFilCod`, `CRIRRCliCod`, `CEProCod` | 7 |
| `CRLic` | TCR24A | `CMEmpCod`, `CMFilCod`, `CRLicDta`, `CRLicNroEdi`, `CRLicTip` | 15 |
| `CRLMT` | Lançamentos Provenientes de Microterminal | `CRLMTID` | 15 |
| `CRMov1` | Sequencia Diaria das Vendas | `CMEmpCod`, `CMFilCod`, `CRMovDta` | 13 |
| `CRMov2` | Cabecalho das vendas | `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq` | 265 |
| `CRMov3` | Parcelas das Vendas | `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMov3Par` | 258 |
| `CRMov4` | Produtos da Venda | `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov4Ite` | 140 |
| `CRMov5` | Histórico de Baixas e Cheque P | `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMov3Par`, `CRMov5Cod` | 57 |
| `CRMov6` | Resumo das Baixas Parcelas | `CMEmpCod`, `CMFilCod`, `CRMov6Seq` | 46 |
| `CRMov7` | Número Série do Produto | `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov7Item` | 29 |
| `CRmov8` | Resumo das Vendas Juntadas | `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMov8DtaOrg`, `CRMov8SeqOrg` | 70 |
| `CRMov9` | Level1 | `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov4Ite`, `CRMov9CodPro` | 29 |
| `CRMovA` | Dados Adicionais da Venda\Produto | `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMovATip`, `CRMovADtaLct`, `CRMovASeq` | 45 |
| `CRMovE` | Controle Entregas Parcial | `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov4Ite`, `CRMovESeq`, `CRMovEDta` | 25 |
| `CRMovG` | Tabela Genéricas das CRMovs CRMovG | `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMovGChv` | 11 |
| `CRMovH` | Histórico Movimentações Fases Óticas | `CMEmpCod`, `CMFilCod`, `CRMovHDta`, `CRMovHSeq`, `CRMovHCod`, `CRMovHDtaE`, `CRMovHSeqE` | 17 |
| `CRMovR` | Level1 | `CRMovTCtr`, `CRMovRTipo`, `CRMovRSeq` | 35 |
| `CRMovT` | Controle de Emissão de TEF | `CRMovTCtr` | 32 |
| `CROrc1` | Orçamento 01 | `CMEmpCod`, `CMFilCod`, `CROrcDtaHor` | 138 |
| `CROrc2` | Itens Orçamento | `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`, `CROrc2Ite`, `CROrc2ProCod` | 233 |
| `CROrc3` | CROrc3 | `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`, `CROrc2Ite`, `CROrc2ProCod`, `CROrc3Cod` | 77 |
| `CROrc4` | Apontamentos do Orçamento | `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`, `CROrc4Nom`, `CROrc4TSTLct` | 23 |
| `CROrc5` | Detalhes do Orçamento | `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`, `CROrc2Ite`, `CROrc2ProCod`, `CROrc5ProKitCod`, `CROrc5Tip` | 46 |
| `CROrcF` | Fases | `CMEmpCod`, `CMFilCod`, `CROrcFCod` | 4 |
| `CROrcT` | Descrição do Tipo do Status do Orçamento | `CMEmpCod`, `CMFilCod`, `CROrcTCod` | 6 |
| `CROtc` | Cadastro de Ótica | `CMEmpCod`, `CROtcCod` | 3 |
| `CRPtm2` | Pedidos Temporários 02 | `CMEmpCod`, `CRPTmCod` | 63 |
| `CRPtm3` | Pedidos Temporários 03 | `CMEmpCod`, `CRPTmCod`, `CRPtm3NroPar` | 15 |
| `CRPTM4` | Pedidos Temporários 04 | `CMEmpCod`, `CRPTmCod`, `CRPtm4IteAux`, `CEProCod`, `CRPtm4Item` | 42 |
| `CRPVC` | Produtos Última Venda Condicio | `CRPVCNroCxa`, `CRPVCProCod` | 6 |
| `CRRBB1` | Retorno Tit. B.Brasil | `CRRBB1Cod` | 12 |
| `CRRCxA` | Regime Caixa Anual | `CMEmpCod`, `CMFilCod`, `CRRCxAno` | 14 |
| `CRRCxD` | Regime Caixa Diário | `CMEmpCod`, `CMFilCod`, `CRRCxAno`, `CRRCxMes`, `CRRCxDia` | 26 |
| `CRRCxM` | Regime Caixa Mensal | `CMEmpCod`, `CMFilCod`, `CRRCxAno`, `CRRCxMes` | 23 |
| `CRRTo` | Tabela Movimento Rede Total | `CRRToCod` | 1 |
| `CRSin01` | Cadastro Registro Fiscal 60M | `CMEmpCod`, `CMFilCod`, `CRSinNroImp`, `CRSinDataM` | 13 |
| `CRSin02` | Cadastro Registro Fiscal 60A | `CMEmpCod`, `CMFilCod`, `CRSinNroImp`, `CRSinDataA`, `CRSinASitTrib` | 7 |
| `CRSin03` | Cadastro Registro Fiscal 60I | `CMEmpCod`, `CMFilCod`, `CRSinNroImp`, `CRSinDataI`, `CRSinModDI`, `CRSinNumCOO`, `CRSinNumItem` | 14 |
| `CRSin04` | Cadastro Registro Fiscal 60D | `CMEmpCod`, `CMFilCod`, `CRSinNroImp`, `CRSinDataD`, `CRSinDCodPro` | 11 |
| `CRSin05` | Cadastro Registro Fiscal 60R | `CMEmpCod`, `CMFilCod`, `CRSinNroImp`, `CRSinDataR`, `CRSinMesAno`, `CRSinRCodPro` | 11 |
| `CRSin06` | Temporária - Soma COO | `CMEmpCod`, `CMFilCod`, `CRSinModDT`, `CRSinNumT` | 6 |
| `CRSNG` | Sistema Nacional de Gerenciamento de Produto Controlado | `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov4Ite`, `CRSNGAux` | 44 |
| `CRTip` | Tipo de Cliente | `CMEmpCod`, `CRTipCod` | 29 |
| `CRTipH` | Histório Clientes nos Convênios | `CMEmpCod`, `CRTipCod`, `CRTipHDta`, `CRTipHCodCli` | 6 |
| `CRTipV` | Convênio - Valores | `CMEmpCod`, `CRTipCod`, `CRTipVDta`, `CRTipVCodCli`, `CRTipVPar`, `CRTipVFil` | 46 |
| `CRTM1` | Temporária Extrato Cliente | `CMEmpCod`, `CRCliCod`, `CRTm1Dta`, `CRTm1Tip`, `CRTm1SeqLct` | 22 |
| `CRTM2` | Temporária Recebimentos com Cartão de Crédito | `CRTM2Seq`, `CRTM2CheOut` | 10 |
| `CRTMV` | Tipo do Motivo da Venda | `CMEmpCod`, `CRTMVCod` | 5 |
| `CRTrc1` | Troca Mercadoria 1 | `CMEmpCod`, `CMFilCod`, `CRTrc1Dta`, `CRTrc1Hor` | 46 |
| `CRTrc2` | Troca Mercadoria 2 | `CMEmpCod`, `CMFilCod`, `CRTrc1Dta`, `CRTrc1Hor`, `CRTrc2Item` | 76 |
| `CRTX1` | Taxas Financeiras | `CMEmpCod`, `CRTX1Cod` | 4 |
| `CRTX2` | Tabela de Taxas | `CMEmpCod`, `CRTX1Cod`, `CRTX2Cod` | 9 |
| `CRTX3` | Tabela de Taxas | `CMEmpCod`, `CRTX1Cod`, `CRTX2Cod`, `CRTX3Cod` | 14 |
| `CRVCT` | Vencimentos do Cliente | `CMEmpCod`, `CRVCTCliCod`, `CRVctSeqLct` | 13 |
| `CRVEI` | Cadastro veiculos | `CRVeiPlc` | 42 |
| `CRVeiH` | Histórico Abastecimentos Veículos | `CRVeiPlc`, `CRVeiHTST` | 50 |
| `CRVen` | Vendedores para Dinamic Combo Box | `CRVenNom` | 1 |
| `CT01A` | Dados da NFP - Cupom E14 | `CT01ImpFis`, `CT01NumCCF` | 13 |
| `CT01B` | Dados da NFP - Produtos E15 | `CT01ImpFis`, `CT01NumCCF`, `CT01Item` | 32 |
| `CT02A` | Dados da NFP - Relação de Reduções Z | `CT02ImpFis`, `CT02NumCRZ` | 17 |
| `CT02B` | Dados da NFP - Totais de Tributação da Redução Z | `CT02ImpFis`, `CT02NumCRZ`, `CT02TotTri` | 7 |
| `CT03A` | SPED - Participantes (Registro 0150) | `CMEmpCod`, `CT03TipPar`, `CT03CodPar` | 6 |
| `CT03B` | SPED - Produtos (Registro 0200) | `CMEmpCod`, `CT03CodPro` | 4 |
| `CT03C` | SPED - Agrupamento Bloco M (CST) | `CT03TipoPC`, `CT03CST` | 3 |
| `CT03D` | SPED - Agrupamento Bloco M (Nat. Rec.) | `CT03TipoPC`, `CT03CST`, `CT03NatRec` | 4 |
| `CT03E` | SPED - Erros durante a validação | `CT03SeqErr` | 2 |
| `CT03F` | SPED - Temporária para Geração do Arquivo Texto | `CT03SeqArq` | 11 |
| `CT04A` | SPED - Importação do MFD 1 | `CMEmpCod`, `CMFilCod`, `CT04Ano`, `CT04Mes` | 35 |
| `CT04B` | SPED - Importação do MFD 2 | `CMEmpCod`, `CMFilCod`, `CT04Ano`, `CT04Mes`, `CT04Equip`, `CT04SeqTxt` | 7 |
| `CT04C` | SPED - Importação do MFD 3 | `CMEmpCod`, `CMFilCod`, `CT04Ano`, `CT04Mes`, `CT04Equip`, `CT04Data`, `CT04CodPro` | 8 |
| `CT04D` | SPED - Importação do MFD 4 | `CMEmpCod`, `CMFilCod`, `CT04Ano`, `CT04Mes`, `CT04Equip`, `CT04Data`, `CT04COO` | 9 |
| `CT05A` | Dados do Contador | `CT05EmpCod`, `CT05FilCod` | 39 |
| `CT05C` | Parâmetros SPED - PIS/COFINS | `CT05EmpCod`, `CT05FilCod`, `CT05TipoPC`, `CT05CSTPC` | 4 |
| `CT05D` | Parâmetros SPED - PIS/COFINS Natureza da Receita | `CT05EmpCod`, `CT05FilCod`, `CT05TipoPC`, `CT05CSTPC`, `CT05NatRec` | 7 |
| `CT06A` | SPED - Contas Contábeis | `CMEmpCod`, `CMFilCod`, `CT06CodCtb` | 6 |
| `CT07A` | SPED - Histórico Qtde Estoque (Bloco H) | `CMEmpCod`, `CMFilCod`, `CEProCod`, `CT07ADta` | 7 |
| `CxCxa` | Caixa | `CMEmpCod`, `CMFilCod`, `CxCxaDta`, `CxCxaCheOut` | 128 |
| `CxCxa1` | Sangria do Caixa | `CMEmpCod`, `CMFilCod`, `CxCxaDta`, `CxCxaCheOut`, `CxCxa1Seq` | 28 |
| `CXCxC` | Detalhes Recebimento do Cartão | `CMEmpCod`, `CMFilCod`, `CxCxaDta`, `CxCxaCheOut`, `CXCxCSeq` | 15 |
| `CXCXD` | Detalhes dos Movimentos | `CMEmpCod`, `CMFilCod`, `CxCxaDta`, `CxCxaCheOut`, `CXCxDSeq` | 12 |
| `DSCta` | Plano de Contas | `CMEmpCod`, `DSCtaNiv01`, `DSCtaNiv02`, `DSCtaNiv03`, `DSCtaNiv04` | 13 |
| `DSDSA` | Despesa x Setor de Aplicação | `CMEmpCod`, `DSDspCod`, `DSDSACod` | 9 |
| `DSDsp` | Despesas | `CMEmpCod`, `DSDspCod` | 36 |
| `DSDsR` | Rateio de Despesa por Filial | `CMEmpCod`, `DSDspCod`, `DSDsRFil` | 9 |
| `DSEmp` | Empresa | `DSEmpCod` | 3 |
| `DSFAn` | Parametros Anual | `DSEmpCod`, `DSFilCod`, `DSFAnAno` | 10 |
| `DSFil` | Filiais | `DSEmpCod`, `DSFilCod` | 8 |
| `DSFMe` | Resultado Mensal | `DSEmpCod`, `DSFilCod`, `DSFAnAno`, `DSFMeMes` | 23 |
| `DSGrp` | Grupo de Despesas | `CMEmpCod`, `DSGrpCod` | 10 |
| `DSLMG` | Limite Mensal de Gasto da Despesa Saindo do Caixa | `CMEmpCod`, `DSDspCod`, `DSFilCod` | 5 |
| `DSMov1` | Movimento Despesa 01 | `CMEmpCod`, `CMFilCod`, `DSMov2Dta` | 7 |
| `DSMov2` | Movimento Despesa 02 | `CMEmpCod`, `CMFilCod`, `DSMov2Dta`, `DSMov2Seq` | 82 |
| `DSMovS` | Detalhamento do Lançamento por Setor de Aplicação | `CMEmpCod`, `CMFilCod`, `DSMov2Dta`, `DSMov2Seq`, `DSMovSSetCod` | 16 |
| `DSRAn` | Resultado Anual | `CMEmpCod`, `CMFilCod`, `DSRAnAno` | 42 |
| `DSRFA` | Resultado por Fornecedor Anual | `CMEmpCod`, `CMFilCod`, `CPCliCod`, `DSRFAANO` | 10 |
| `DSRFD` | Resultado do Fornecedor Detalhado | `CMEmpCod`, `CMFilCod`, `CPCliCod`, `DSRFAANO`, `DSRFMMES`, `DSRFDCOD` | 57 |
| `DSRFM` | Resultado por Fornecedor Mensal | `CMEmpCod`, `CMFilCod`, `CPCliCod`, `DSRFAANO`, `DSRFMMES` | 26 |
| `DSRMC` | Resultado mensal por Cartão | `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`, `DSRMCCCrCod` | 200 |
| `DSRMD` | Vendas Diárias | `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`, `DSRMDDia` | 204 |
| `DSRMe` | Resultado Mensal | `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes` | 227 |
| `DSRMG` | Resultado Mensal por Grupo | `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`, `DSRMGCodGrp` | 41 |
| `DSRMS` | Resultado Mensal por Subgrupo | `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`, `DSRMGCodGrp`, `DSRMSCodSgr` | 79 |
| `DSRS1` | Histórico Resumo  Grupo/SubGrupo/Despesa | `CMEmpCod`, `CMFilCod`, `DSRS1ANO` | 6 |
| `DSRS2` | Resumo despesas por Ano\Mês | `CMEmpCod`, `CMFilCod`, `DSRS1ANO`, `DSRS2Mes` | 10 |
| `DSRS3` | Resumo despesas por Ano\Mês\Grupo | `CMEmpCod`, `CMFilCod`, `DSRS1ANO`, `DSRS2Mes`, `DSRS3GrpCod` | 15 |
| `DSRS4` | Resumo despesas por Ano\Mês\Grupo\SubGrupo | `CMEmpCod`, `CMFilCod`, `DSRS1ANO`, `DSRS2Mes`, `DSRS3GrpCod`, `DSRS4SgrCod` | 20 |
| `DSRS5` | Resumo despesas por Ano\Mês\Grupo\SubGrupo\despesa | `CMEmpCod`, `CMFilCod`, `DSRS1ANO`, `DSRS2Mes`, `DSRS3GrpCod`, `DSRS4SgrCod`, `DSRS5DspCod` | 26 |
| `DSSet` | Setor de Aplicação | `CMEmpCod`, `DSSetCod` | 9 |
| `DSSgr` | Sub-Grupo de Despesa | `CMEmpCod`, `DSGrpCod`, `DSSgrCod` | 19 |
| `FCMov1` | Fluxo de Caixa 01 | `CMEmpCod`, `CMFilCod`, `FCMovDta` | 10 |
| `FCMov2` | Fluxo de Caixa 02 | `CMEmpCod`, `CMFilCod`, `FCMovDta`, `FCMovSeq` | 26 |
| `FCSAn` | Saldo do Fluxo Caixa Anual | `CMEmpCod`, `CMFilCod`, `FCSAn` | 11 |
| `FCSMe` | Saldo do Fluxo de Caixa Mensal | `CMEmpCod`, `CMFilCod`, `FCSAn`, `FCSMe` | 21 |
| `HTApt` | Cadastro de Quartos | `CMEmpCod`, `CMFilCod`, `HTAptCod` | 13 |
| `HTDAp` | Movimento das Diárias dos Quartos | `CMEmpCod`, `CMFilCod`, `HTAptCod`, `HTDApDta` | 61 |
| `HTDAV` | Vencimento das Parcelas do Aluguel | `CMEmpCod`, `CMFilCod`, `HTAptCod`, `HTDApDta`, `HTDAVPar` | 18 |
| `HTPrm` | Parâmetros do Hotel | `CMEmpCod`, `CMFilCod`, `HTPrmCod` | 8 |
| `IRMov2` | Tabela de Pedidos da Irroba | `CMEmpCod`, `CMFilCod`, `IRMov2Id` | 48 |
| `IRMov4` | Itens de Pedido da Irroba | `CMEmpCod`, `CMFilCod`, `IRMov2Id`, `IRMov4Id` | 53 |
| `KHClH` | KHCl H | `KHEmpEmp`, `KHCliCod`, `KHClHTstLc` | 56 |
| `KHCli` | KHCli | `KHEmpEmp`, `KHCliCod` | 33 |
| `KHEmp` | Empresas KingHost | `KHEmpEmp` | 5 |
| `KHFun` | Funcionários da MSINFOR | `KHEmpEmp`, `KHFunNom` | 4 |
| `KHHAP` | Histórico Acesso programa | `KHEmpEmp`, `KHCliCod`, `KHHAPPrg` | 5 |
| `KHPar` | KHPar | `KHEmpEmp`, `KHCliCod`, `KHParDta`, `KHParSeq`, `KHParPar` | 35 |
| `PDPCR` | % q Cada Recebedor de Comissão | `CMEmpCod`, `CMFilCod`, `PDRprCod`, `PDRCoCod` | 9 |
| `PDPDB` | Baixa Pedidos | `CMEmpCod`, `CMFilCod`, `PDPDCNro`, `PDPDiItem`, `PDPDNNro`, `PDPDBNroNot` | 40 |
| `PDPDC` | Cabecalho Pedidos | `CMEmpCod`, `CMFilCod`, `PDPDCNro` | 25 |
| `PDPDI` | Itens Pedido | `CMEmpCod`, `CMFilCod`, `PDPDCNro`, `PDPDiItem` | 39 |
| `PDPDN` | Pedido por Numeração | `CMEmpCod`, `CMFilCod`, `PDPDCNro`, `PDPDiItem`, `PDPDNNro` | 46 |
| `PDRCo` | Recebedores de Comissão | `CMEmpCod`, `CMFilCod`, `PDRCoCod` | 4 |
| `PDRep` | Representantes | `CMEmpCod`, `CMFilCod`, `PDRepCod` | 5 |
| `PDRpr` | Representadas | `CMEmpCod`, `CMFilCod`, `PDRprCod` | 6 |
| `POBIT` | Bicos - Intervenção Técnica | `POEmpCod`, `POBomCod`, `POBITNroInt` | 9 |
| `POBom` | Cadastro Bombas | `POEmpCod`, `POBomCod` | 18 |
| `POBxB` | Bombas x Bicos | `POEmpCod`, `POMBoCod`, `POBomCod` | 10 |
| `POCF1` | Movimento POCF1 | `POEmpCod`, `POCF1Tst`, `POCF1Regis` | 53 |
| `POCF2` | Resumo Caixa por Frentista | `POEmpCod`, `POCF2Usu`, `POCF2Tst` | 53 |
| `POCF3` | Resumo dos Movimentos do Caixa do Frentista | `POEmpCod`, `POCF2Usu`, `POCF2Tst`, `POCF3TipMov` | 39 |
| `POCF4` | Movimento POCF4 Gravado pelo Programa .Net | `POEmpCod`, `POCF4Tst`, `POCF4Regis` | 41 |
| `POCxa1` | Caixa01 | `POEmpCod`, `PODtaMov`, `POCxaPer` | 82 |
| `POCxa2` | Caixa 2 - Somar Vendas por Tipo de Combustível | `POEmpCod`, `PODtaMov`, `POCxaPer`, `POTCoCod` | 102 |
| `POEmp` | Empresas | `POEmpCod` | 10 |
| `POENF` | Entrada de Notas Fiscais | `POEmpCod`, `PODtaMov`, `POTnqCod`, `POForCod`, `POForNNF` | 17 |
| `POFor` | Fornecedores | `POForCod` | 2 |
| `POLac` | Lacre das Bombas | `POEmpCod`, `POMBoCod`, `POLacNro` | 5 |
| `POLMC1` | LMC | `POEmpCod`, `PODtaMov`, `POTnqCod`, `POBomCod` | 10 |
| `POLMC2` | Estoque dos Tanques LMC | `POEmpCod`, `PODtaMov`, `POTnqCod` | 30 |
| `POLMC3` | Movimento por Tipo Combustível - LMC | `POEmpCod`, `PODtaMov`, `POLMC3TCoCod` | 14 |
| `POLvr` | Livros do LMC | `POEmpCod`, `POLvrCod` | 4 |
| `POMBo` | Cadastro das Bombas | `POEmpCod`, `POMBoCod` | 7 |
| `POPer` | Períodos | `POEmpCod`, `POPerCod` | 4 |
| `POTCo` | Tipos de Combustíveis | `POTCoCod` | 5 |
| `POTCV` | TOTAL COMPRAS/VENDAS | `POEmpCod`, `POTCMAn` | 37 |
| `POTnq` | Tanques | `POEmpCod`, `POTnqCod` | 10 |
| `POVal` | Controle de Vales | `POEmpCod`, `POValCod` | 17 |
| `POVel1` | Velocímetro 01 | `POEmpCod`, `PODtaMov`, `POVel1Per` | 5 |
| `POVel2` | Velocimetro 02 | `POEmpCod`, `PODtaMov`, `POVel1Per`, `POBomCod` | 18 |
| `Precos` | Precos do Simpro | `CD_Cliente` | 9 |
| `SANF1` | Cab. Nota Sagra | `SANF1Ini`, `SANF1NroPed` | 8 |
| `SANF2` | Produtos Nota SAGRA | `SANF1Ini`, `SANF1NroPed`, `SAProCod` | 16 |
| `SAPro` | Produtos da SAGRA | `SAProCod` | 8 |
| `SDMA1` | Movimento do Associado | `CMEmpCod`, `CRCliCod`, `SDMA1Dta` | 19 |
| `SDMV1` | SDMV1 | `CMEmpCod`, `CMFilCod`, `SDMV1AME` | 4 |
| `SDMV2` | SDMV2 | `CMEmpCod`, `CMFilCod`, `SDMV1AME`, `CRClaCod` | 9 |
| `SDPOB` | Observações do Produto do Sindicato | `CMEmpCod`, `CEProCod`, `SDPOB` | 4 |
| `SDUsi` | Cadastro de Usinas | `CMEmpCod`, `SDUsiCod` | 23 |
| `TABELAS` | TABELAS | `object_id` | 2 |

---

## 🔍 Detalhamento de Campos e Índices

### 📌 BKMOV2
- **Descrição:** BKMOV2
- **Chave Primária:** `BKEMPCOD`, `BKFILCOD`, `BKMOVDTA`, `BKMOVSEQ`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `BKEMPCOD` | `N/D` | - |
| `BKFILCOD` | `N/D` | - |
| `BKMOVDTA` | `N/D` | - |
| `BKMOVSEQ` | `N/D` | - |
| `BKMOV2CDTA` | `N/D` | - |
| `BKMOV2CHOR` | `N/D` | - |
| `BKMOV2CUSU` | `N/D` | - |
| `BKMOV2CPRG` | `N/D` | - |
| `BKMOV2NRON` | `N/D` | - |
| `BKMOV2SERN` | `N/D` | - |
| `BKMOV2SENB` | `N/D` | - |
| `BKMOV2VEND` | `N/D` | - |
| `BKMOV2DTAC` | `N/D` | - |
| `BKMOV2FIL` | `N/D` | - |
| `BKMOV2VLRO` | `N/D` | - |
| `BKMOV2VLRC` | `N/D` | - |
| `BKMOV2VLRI` | `N/D` | - |
| `BKMOV2ICM` | `N/D` | - |
| `BKMOV2VLRD` | `N/D` | - |
| `BKMOV2VLR1` | `N/D` | - |
| `BKMOV2NROP` | `N/D` | - |
| `BKMOV2DTAT` | `N/D` | - |
| `BKMOV2DTAN` | `N/D` | - |
| `BKMOV2OBS` | `N/D` | - |
| `BKMOV2SIT` | `N/D` | - |
| `BKMOV2CODC` | `N/D` | - |
| `BKMOV2DESC` | `N/D` | - |
| `BKMOV2FLAG` | `N/D` | - |
| `BKMOV2OBS1` | `N/D` | - |
| `BKMOV2OBS2` | `N/D` | - |
| `BKMOV2PERA` | `N/D` | - |
| `BKMOV2PERD` | `N/D` | - |
| `BKMOV2PRXN` | `N/D` | - |
| `BKMOV2VLAC` | `N/D` | - |
| `BKMOV2VLRA` | `N/D` | - |
| `BKMOV2VLRT` | `N/D` | - |
| `BKMOV2VLRE` | `N/D` | - |
| `BKMOV2DSPV` | `N/D` | - |
| `BKPRGNOM` | `N/D` | - |
| `BKMOV2FLAD` | `N/D` | - |
| `BKMOV2NOPC` | `N/D` | - |
| `BKMOV2SAIO` | `N/D` | - |
| `BKMOV2CANC` | `N/D` | - |
| `BKMOV2IMPC` | `N/D` | - |
| `BKMOV2VDAC` | `N/D` | - |
| `BKMOV2CCUC` | `N/D` | - |
| `BKMOV2TOTV` | `N/D` | - |
| `BKMOV2PERC` | `N/D` | - |
| `BKMOV2LCTH` | `N/D` | - |
| `BKCCRCOD` | `N/D` | - |
| `BKMOV2MOTC` | `N/D` | - |
| `BKMOV2VLRU` | `N/D` | - |
| `BKMOV2CHEO` | `N/D` | - |
| `BKMOV2NFIE` | `N/D` | - |
| `BKMOV2CRMM` | `N/D` | - |
| `BKMOV2NROM` | `N/D` | - |
| `BKMOV2DSTD` | `N/D` | - |
| `BKMOV2COTD` | `N/D` | - |
| `BKMOV2COTS` | `N/D` | - |
| `BKMOV2ALTV` | `N/D` | - |
| `BKMOV2DTAE` | `N/D` | - |
| `BKMOV2TIPC` | `N/D` | - |
| `BKMOV2CONV` | `N/D` | - |
| `BKMOV2RESO` | `N/D` | - |
| `BKMOV2PER_` | `N/D` | - |
| `BKMOV2MRG` | `N/D` | - |
| `BKMOV2MEDP` | `N/D` | - |
| `BKMOV2NFIF` | `N/D` | - |
| `BKMOV2NFID` | `N/D` | - |
| `BKMOV2NFIS` | `N/D` | - |
| `BKMOV2NFIT` | `N/D` | - |
| `BKMOV2CHAC` | `N/D` | - |
| `BKMOV2MED` | `N/D` | - |
| `BKMOV2MEDT` | `N/D` | - |
| `BKMOV2ENT` | `N/D` | - |
| `BKMOV2COMV` | `N/D` | - |
| `BKMOV2IMPN` | `N/D` | - |
| `BKMOV2TMVC` | `N/D` | - |
| `BKMOV2DTEN` | `N/D` | - |
| `BKMOV2TAB` | `N/D` | - |
| `BKMOV2VAF` | `N/D` | - |
| `BKMOV2IDX` | `N/D` | - |
| `BKMOV2PES` | `N/D` | - |
| `BKTRACOD` | `N/D` | - |
| `BKMOV2SNG` | `N/D` | - |
| `BKMOV2CCRP` | `N/D` | - |
| `BKMOV2CPF` | `N/D` | - |
| `BKMOV2DCX` | `N/D` | - |
| `BKMOV2VEN2` | `N/D` | - |
| `BKMOV2VLR2` | `N/D` | - |
| `BKMOV2CCV` | `N/D` | - |
| `BKMOV2VLRR` | `N/D` | - |
| `BKMOV2PLCV` | `N/D` | - |
| `BKMOV2DPRE` | `N/D` | - |
| `BKMOV2DSPC` | `N/D` | - |
| `BKMOV2GRPC` | `N/D` | - |
| `BKMOV2SGRC` | `N/D` | - |
| `BKMOV2PGTM` | `N/D` | - |
| `BKMOV2VAV` | `N/D` | - |
| `BKMOV2USUE` | `N/D` | - |
| `BKMOV2DCXC` | `N/D` | - |
| `BKMOV2SEQL` | `N/D` | - |
| `BKMOV2AUDV` | `N/D` | - |
| `BKMOV2AUDQ` | `N/D` | - |
| `BKMOV2AUDD` | `N/D` | - |
| `BKMOV2FPCC` | `N/D` | - |
| `BKMOV2VLR3` | `N/D` | - |
| `BKMOV2DTA2COM` | `N/D` | - |
| `BKMOV2CODVD` | `N/D` | - |
| `BkMOV2FASCOD` | `N/D` | - |
| `BKMOV2NRODUP` | `N/D` | - |
| `BKMOV2PONFID` | `N/D` | - |
| `BKMOV2USUCON` | `N/D` | - |
| `BKMOV2VDV` | `N/D` | - |
| `BKMOV2ENTFUT` | `N/D` | - |
| `BKMOV2ORCDTAHOR` | `N/D` | - |
| `BKMOV2TSTCAN` | `N/D` | - |
| `BKMOV2UUS_CAN` | `N/D` | - |
| `BKMOV2ENTREB` | `N/D` | - |
| `BKMOV2V_RAT` | `N/D` | - |
| `BKMOV2PGTCOM` | `N/D` | - |
| `BKMOV2TRCORG` | `N/D` | - |
| `BKMOV2CCX` | `N/D` | - |
| `BKMOV2VAFA` | `N/D` | - |
| `BKMOV2MONDTAPRE` | `N/D` | - |
| `BKMOV2MONUSU` | `N/D` | - |
| `BKMOV2MONCXA` | `N/D` | - |
| `BKMOV2DSPEXT` | `N/D` | - |
| `BKMOV2CB1DTAENV` | `N/D` | - |
| `BKMOV2CB2DTARET` | `N/D` | - |
| `BKMOV2CB3DTABOL` | `N/D` | - |
| `BKMOV2CBSEQREM` | `N/D` | - |
| `BKMOV2GERGRPSGR` | `N/D` | - |
| `BKMOV2CMPGEN1` | `N/D` | - |
| `BKMOV2VLVALPRE` | `N/D` | - |
| `BKMOV2CHAVESAT` | `N/D` | - |
| `BKMOV2SITSAT` | `N/D` | - |
| `BKMOV2DHEMISAT` | `N/D` | - |
| `BKMOV2DhCancSAT` | `N/D` | - |
| `BKMOV2SerSAT` | `N/D` | - |
| `BKMOV2ExtSAT` | `N/D` | - |
| `BKMOV2ArqSAT` | `N/D` | - |
| `BKMOV2ModImpFiSAT` | `N/D` | - |
| `BKMOV2ChCancSAT` | `N/D` | - |
| `BKMOV2ArqCanSAT` | `N/D` | - |
| `BKMOV2ExcSAT` | `N/D` | - |
| `BKMOV2SerCancSAT` | `N/D` | - |
| `BKMOV2MicSAT` | `N/D` | - |
| `BKMOV2FilaSAT` | `N/D` | - |
| `BKMOV2SitFila` | `N/D` | - |
| `BKMOV2QRCode` | `N/D` | - |
| `BKMOV2VrAprox` | `N/D` | - |
| `BKMOV2BcoCod` | `N/D` | - |
| `BKMOV2Idx2` | `N/D` | - |
| `BKMOV2EntBxa` | `N/D` | - |
| `BKMOV2EntTST` | `N/D` | - |
| `BKMOV2Txa_IDE` | `N/D` | - |
| `BKMOV2TxaIND` | `N/D` | - |
| `BKMOV2TxaTAC` | `N/D` | - |
| `BKMOV2BAFE` | `N/D` | - |
| `BKMOV2CRClrSeq` | `N/D` | - |
| `BKMOV2CRCP1Cod` | `N/D` | - |
| `BKMOV2VlDscLiqVda` | `N/D` | - |
| `BKMOV2NroCOO` | `N/D` | - |
| `BKMOV2QR1Ass` | `N/D` | - |
| `BKMOV2QR2Ass` | `N/D` | - |
| `BKMOV2CQRCode` | `N/D` | - |
| `BKMOV2CQR1Ass` | `N/D` | - |
| `BKMOV2CQR2Ass` | `N/D` | - |
| `BKMOV2RPS` | `N/D` | - |
| `BKMOV2ApSc` | `N/D` | - |
| `BKMOV2VenOrg` | `N/D` | - |

#### 🗺️ Índices
- `BKMOV2O` (Unique): `BKEMPCOD`, `BKFILCOD`, `BKMOVDTA`, `BKMOVSEQ`
- `BKMOV24` (Duplicate): `BKEMPCOD`, `BKMOV2DTAC`
- `BKMOV25` (Duplicate): `BKEMPCOD`, `BKMOV2FLAG`
- `BKMOV26` (Duplicate): `BKEMPCOD`, `BKMOV2CODC`, `BKMOV2FLAG`, `BKMOVDTA`
- `BKMOV2B` (Duplicate): `BKEMPCOD`, `BKFILCOD`, `BKCCRCOD`
- `BKMOV2H` (Duplicate): `BKMOV2IDX`
- `BKMOV2I` (Duplicate): `BKMOV2DCX`
- `BKMOV2J` (Duplicate): `BKTRACOD`
- `BKMOV27` (Duplicate): `BKEMPCOD`, `BKMOV2DTAN`, `BKMOV2NRON`
- `BKMOV28` (Duplicate): `BKEMPCOD`, `BKMOV2VDAC`
- `BKMOV29` (Duplicate): `BKEMPCOD`, `BKMOV2CODC`, `BKMOVDTA`
- `BKMOV2A` (Duplicate): `BKEMPCOD`, `BKMOVDTA`, `BKMOVSEQ`
- `BKMOV2D` (Duplicate): `BKMOVDTA`, `BKMOV2CHEO`, `BKMOVSEQ`, `BKEMPCOD`
- `BKMOV2C` (Duplicate): `BKEMPCOD`, `BKPRGNOM`
- `BKMOV2E` (Duplicate): `BKEMPCOD`, `BKMOV2DSTD`
- `BKMOV2F` (Duplicate): `BKMOV2COMV`, `BKMOV2CDTA`, `BKMOV2CHOR`, `BKEMPCOD`, `BKPRGNOM`
- `BKMOV2K` (Duplicate): `BKMOV2ENT`, `BKMOV2DTEN`
- `BKMOV2L` (Duplicate): `BKMOV2DTAE`, `BKMOV2CODC`
- `BKMOV2M` (Duplicate): `BKMOV2DCXC`
- `BKMOV2N` (Duplicate): `BKMOV2SEQL`

---

### 📌 BKMOV3
- **Descrição:** BKMOV3
- **Chave Primária:** `BKFILCOD`, `BKMOVDTA`, `BKMOVSEQ`, `BKMOV3PAR`, `BKEMPCOD`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `BKFILCOD` | `N/D` | - |
| `BKMOVDTA` | `N/D` | - |
| `BKMOVSEQ` | `N/D` | - |
| `BKMOV3PAR` | `N/D` | - |
| `BKEMPCOD` | `N/D` | - |
| `BKMOV3VLAB` | `N/D` | - |
| `BKMOV3DTAV` | `N/D` | - |
| `BKMOV3DTAP` | `N/D` | - |
| `BKMOV3OBS` | `N/D` | - |
| `BKMOV3CODC` | `N/D` | - |
| `BKMOV3VLRO` | `N/D` | - |
| `BKMOV3BCOC` | `N/D` | - |
| `BKMOV3CHQN` | `N/D` | - |
| `BKMOV3FUNP` | `N/D` | - |
| `BKMOV3CODB` | `N/D` | - |
| `BKMOV3FLAG` | `N/D` | - |
| `BKMOV3CDTA` | `N/D` | - |
| `BKMOV3CUSU` | `N/D` | - |
| `BKMOV3CHOR` | `N/D` | - |
| `BKMOV3CPRG` | `N/D` | - |
| `BKMOV3PRXC` | `N/D` | - |
| `BKMOV3DTAT` | `N/D` | - |
| `BKMOV3VLRC` | `N/D` | - |
| `BKMOV3FLGC` | `N/D` | - |
| `BKMOV3DTAC` | `N/D` | - |
| `BKMOV3LCTH` | `N/D` | - |
| `BKMOV3DTAO` | `N/D` | - |
| `BKMOV3SENB` | `N/D` | - |
| `BKMOV3FLAD` | `N/D` | - |
| `BKMOV3NDB` | `N/D` | - |
| `BKMOV3RCC` | `N/D` | - |
| `BKMOV3AUDV` | `N/D` | - |
| `BKMOV3AUDD` | `N/D` | - |
| `BKMOV3CHEO` | `N/D` | - |
| `BKMOV3AUXB` | `N/D` | - |
| `BKMOV3VLRT` | `N/D` | - |
| `BKMOV3VLRE` | `N/D` | - |
| `BKMOV3CONV` | `N/D` | - |
| `BKMOV3CCRC` | `N/D` | - |
| `BKMOV3IDX` | `N/D` | - |
| `BKMOV3CHQP` | `N/D` | - |
| `BKMOV3VLRD` | `N/D` | - |
| `BKMOV3DTAE` | `N/D` | - |
| `BKMOV3BXAB` | `N/D` | - |
| `BKMOV3VAC` | `N/D` | - |
| `BKMOV3VDC` | `N/D` | - |
| `BKMOV3DCX` | `N/D` | - |
| `BKMOV3SIT` | `N/D` | - |
| `BKMOV3VL2C` | `N/D` | - |
| `BKMOV3CCV` | `N/D` | - |
| `BKMOV3VL3C` | `N/D` | - |
| `BKMOV3FILPGT` | `N/D` | - |
| `BKMOV3CCRPAR` | `N/D` | - |
| `BKMOV3DTA2COM` | `N/D` | - |
| `BKMOV3VAF` | `N/D` | - |
| `BKMOV3NRODUP` | `N/D` | - |
| `BKMOV3AGECOD` | `N/D` | - |
| `BKMOV3SPC` | `N/D` | - |
| `BKMOV3CCX` | `N/D` | - |
| `BKMOV3CCR_DIV` | `N/D` | - |
| `BKMOV3CB1DTAENV` | `N/D` | - |
| `BKMOV3CB2DTARET` | `N/D` | - |
| `BKMOV3CB3DTABOL` | `N/D` | - |
| `BKMOV3CBSEQREM` | `N/D` | - |
| `BKMOV3AudPgt` | `N/D` | - |
| `BKMOV3Vl1Com` | `N/D` | - |
| `BKMOV3UsuCob` | `N/D` | - |

#### 🗺️ Índices
- `BKMOV3F` (Unique): `BKFILCOD`, `BKMOVDTA`, `BKMOVSEQ`, `BKMOV3PAR`, `BKEMPCOD`
- `BKMOV3G` (Duplicate): `BKEMPCOD`, `BKFILCOD`, `BKMOVDTA`, `BKMOVSEQ`
- `BKMOV38` (Duplicate): `BKEMPCOD`, `BKMOV3CODC`, `BKMOV3FLAG`, `BKMOV3DTAV`
- `BKMOV31` (Duplicate): `BKEMPCOD`, `BKMOV3FLGC`, `BKMOV3DTAV`
- `BKMOV39` (Duplicate): `BKMOV3CODB`
- `BKMOV34` (Duplicate): `BKMOVDTA`, `BKMOVSEQ`, `BKMOV3PAR`, `BKEMPCOD`, `BKMOV3CODC`, `BKMOV3FLAG`
- `BKMOV35` (Duplicate): `BKEMPCOD`, `BKMOV3DTAV`
- `BKMOV36` (Duplicate): `BKEMPCOD`, `BKMOV3FLAG`, `BKMOV3DTAV`
- `BKMOV37` (Duplicate): `BKEMPCOD`, `BKMOV3DTAP`
- `BKMOV3A` (Duplicate): `BKMOV3AUXB`
- `BKMOV3B` (Duplicate): `BKMOV3IDX`
- `BKMOV3C` (Duplicate): `BKEMPCOD`, `BKFILCOD`, `BKMOVDTA`, `BKMOVSEQ`, `BKMOV3FLAG`, `BKMOV3DTAV`
- `BKMOV3D` (Duplicate): `BKEMPCOD`, `BKMOV3DTAC`
- `BKMOV3E` (Duplicate): `BKMOV3DCX`

---

### 📌 BKMOV4
- **Descrição:** BKMOV4
- **Chave Primária:** `BKEMPCOD`, `BKFILCOD`, `BKMOVDTA`, `BKMOVSEQ`, `BKPROCOD`, `BKMOV4ITE`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `BKEMPCOD` | `N/D` | - |
| `BKFILCOD` | `N/D` | - |
| `BKMOVDTA` | `N/D` | - |
| `BKMOVSEQ` | `N/D` | - |
| `BKPROCOD` | `N/D` | - |
| `BKMOV4ITE` | `N/D` | - |
| `BKMOV4PRO_` | `N/D` | - |
| `BKMOV4PERD` | `N/D` | - |
| `BKMOV4PRET` | `N/D` | - |
| `BKMOV4TMP1` | `N/D` | - |
| `BKMOV4TMPR` | `N/D` | - |
| `BKMOV4CHEO` | `N/D` | - |
| `BKMOV4PROP` | `N/D` | - |
| `BKMOV4VLRU` | `N/D` | - |
| `BKMOV4QTD` | `N/D` | - |
| `BKMOV4CUSP` | `N/D` | - |
| `BKMOV4FLAD` | `N/D` | - |
| `BKMOV4DTAT` | `N/D` | - |
| `BKMOV4VLRA` | `N/D` | - |
| `BKMOV4PREV` | `N/D` | - |
| `BKMOV4QTDE` | `N/D` | - |
| `BKMOV4PRCC` | `N/D` | - |
| `BKMOV4QTDD` | `N/D` | - |
| `BKMOV4FILS` | `N/D` | - |
| `BKMOV4TMPC` | `N/D` | - |
| `BKMOV4TMPD` | `N/D` | - |
| `BKMOV4TMPP` | `N/D` | - |
| `BKMOV4VEN` | `N/D` | - |
| `BKMOV4LOT` | `N/D` | - |
| `BKMOV4MODT` | `N/D` | - |
| `BKMOV4VLRC` | `N/D` | - |
| `BKMOV4TIPP` | `N/D` | - |
| `BKMOV4PROC` | `N/D` | - |
| `BKMOV4ORGC` | `N/D` | - |
| `BKMOV4DTAU` | `N/D` | - |
| `BKMOV4TST` | `N/D` | - |
| `BKMOV4DTAE` | `N/D` | - |
| `BKMOV4ENT` | `N/D` | - |
| `BKMOV4CORAUX` | `N/D` | - |
| `BKMOV4GRPCOD` | `N/D` | - |
| `BKMOV4SGRCOD` | `N/D` | - |
| `BKMOV4BASICM` | `N/D` | - |
| `BKMOV4VLRICMS` | `N/D` | - |
| `BKMOV4IDEPCN` | `N/D` | - |
| `BKMOV4ARRTRU` | `N/D` | - |
| `BKMOV4FASCOD` | `N/D` | - |
| `BKMOV4PONFID` | `N/D` | - |
| `BKMOV4GAR` | `N/D` | - |
| `BKMOV4VLUSACRE` | `N/D` | - |
| `BKMOV4VDV` | `N/D` | - |
| `BKMOV4NCM` | `N/D` | - |
| `BKMOV4PERIMP` | `N/D` | - |
| `BKMOV4DEV` | `N/D` | - |
| `BKMOV4LOTVCT` | `N/D` | - |
| `BKMOV4DSPEXT` | `N/D` | - |
| `BKMOV4PRC2COM` | `N/D` | - |
| `BKMOV4ORG2COM` | `N/D` | - |
| `BKMOV4VU2COM` | `N/D` | - |
| `BKMOV4VEN2` | `N/D` | - |
| `BKMOV4PEIE` | `N/D` | - |
| `BKMOV4VAF` | `N/D` | - |
| `BKMOV4VLDSCLIQVDA` | `N/D` | - |
| `BKMOV4AlqPis` | `N/D` | - |
| `BKMOV4BCPis` | `N/D` | - |
| `BKMOV4CSTPis` | `N/D` | - |
| `BKMOV4VTPis` | `N/D` | - |
| `BKMOV4AlqCof` | `N/D` | - |
| `BKMOV4BCCof` | `N/D` | - |
| `BKMOV4CstCof` | `N/D` | - |
| `BKMOV4VTCof` | `N/D` | - |
| `BKMOV4BCIpi` | `N/D` | - |
| `BKMOV4VTIpi` | `N/D` | - |
| `BKMOV4AlqIpi` | `N/D` | - |
| `BKMOV4Dec` | `N/D` | - |
| `BKMOV4PerAcr` | `N/D` | - |
| `BKMOV4DepCod` | `N/D` | - |
| `BKMOV4CFOP` | `N/D` | - |
| `BKMOV4CSOSN` | `N/D` | - |
| `BKMOV4AlICMS` | `N/D` | - |
| `BKMOV4CSTIcms` | `N/D` | - |
| `BKMOV4VDSc` | `N/D` | - |
| `BKMOV4VASc` | `N/D` | - |
| `BKMOV4FlSc` | `N/D` | - |
| `BKMOV4UsSc` | `N/D` | - |
| `BKMOV4PgSc` | `N/D` | - |
| `BKMOV4SitTrib` | `N/D` | - |
| `BKMOV4FabLot` | `N/D` | - |

#### 🗺️ Índices
- `BKMOV4A` (Unique): `BKEMPCOD`, `BKFILCOD`, `BKMOVDTA`, `BKMOVSEQ`, `BKPROCOD`, `BKMOV4ITE`
- `BKMOV4B` (Duplicate): `BKEMPCOD`, `BKFILCOD`, `BKMOVDTA`, `BKMOVSEQ`

---

### 📌 BKMOV5
- **Descrição:** BKMOV5
- **Chave Primária:** `BKEMPCOD`, `BKFILCOD`, `BKMOVDTA`, `BKMOVSEQ`, `BKMOV3PAR`, `BKMov5Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `BKEMPCOD` | `N/D` | - |
| `BKFILCOD` | `N/D` | - |
| `BKMOVDTA` | `N/D` | - |
| `BKMOVSEQ` | `N/D` | - |
| `BKMOV3PAR` | `N/D` | - |
| `BKMov5Cod` | `N/D` | - |
| `BKMov5Vlr_Trc` | `N/D` | - |
| `BKMov5VlrTot` | `N/D` | - |
| `BKMov5VlrOrg` | `N/D` | - |
| `BKMov5VlrDes` | `N/D` | - |
| `BKMov5VlrCre` | `N/D` | - |
| `BKMov5VlrAcr` | `N/D` | - |
| `BKMov5TipBai` | `N/D` | - |
| `BKMov5SenBai` | `N/D` | - |
| `BKMov5QtdDiaAtr` | `N/D` | - |
| `BKMov5Obs` | `N/D` | - |
| `BKMov5ModBxa` | `N/D` | - |
| `BKMov5LctHstCli` | `N/D` | - |
| `BKMov5Idx` | `N/D` | - |
| `BKMov5Flag` | `N/D` | - |
| `BKMov5FlaDel` | `N/D` | - |
| `BKMov5FilPgt` | `N/D` | - |
| `BKMov5Est` | `N/D` | - |
| `BKMov5DtaVct` | `N/D` | - |
| `BKMov5DtaTrs` | `N/D` | - |
| `BKMov5DtaPgto` | `N/D` | - |
| `BKMov5DtaMov` | `N/D` | - |
| `BKMov5DesVlrDevSerCob` | `N/D` | - |
| `BKMov5DCx` | `N/D` | - |
| `BKMov5CUsu` | `N/D` | - |
| `BKMov5CRMov6` | `N/D` | - |
| `BKMov5CRChACod` | `N/D` | - |
| `BKMov5CPrg` | `N/D` | - |
| `BKMov5CodEst` | `N/D` | - |
| `BKMov5CodCtaChq` | `N/D` | - |
| `BKMov5ChqVlrRec` | `N/D` | - |
| `BKMov5ChqObs` | `N/D` | - |
| `BKMov5ChqFlgDes` | `N/D` | - |
| `BKMov5ChqDtaDes` | `N/D` | - |
| `BKMov5Chq` | `N/D` | - |
| `BKMov5CHor` | `N/D` | - |
| `BKMov5CheOut` | `N/D` | - |
| `BKMov5CDta` | `N/D` | - |
| `BKMov5CCV` | `N/D` | - |
| `BKMov5BxaBco` | `N/D` | - |
| `BKMov5Bco` | `N/D` | - |
| `BKMov5BaiCRMov3` | `N/D` | - |
| `BKMov5AcrVlrDevSerCob` | `N/D` | - |
| `BKMOV5AGE` | `N/D` | - |
| `BKMOV5CCX` | `N/D` | - |
| `BKMOV5SPC` | `N/D` | - |

#### 🗺️ Índices
- `BKMOV5A` (Unique): `BKEMPCOD`, `BKFILCOD`, `BKMOVDTA`, `BKMOVSEQ`, `BKMOV3PAR`, `BKMov5Cod`
- `BKMOV5B` (Duplicate): `BKFILCOD`, `BKMOVDTA`, `BKMOVSEQ`, `BKMOV3PAR`, `BKEMPCOD`

---

### 📌 BKMOV6
- **Descrição:** BKMOV6
- **Chave Primária:** `BKEMPCOD`, `BKFILCOD`, `BKMOV6SEQ`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `BKEMPCOD` | `N/D` | - |
| `BKFILCOD` | `N/D` | - |
| `BKMOV6SEQ` | `N/D` | - |
| `BKMOV6DESC` | `N/D` | - |
| `BKMOV6VLRE` | `N/D` | - |
| `BKMOV6VLRD` | `N/D` | - |
| `BKMOV6VLRA` | `N/D` | - |
| `BKMOV6VLRT` | `N/D` | - |
| `BKMOV6VLRR` | `N/D` | - |
| `BKMOV6OBS` | `N/D` | - |
| `BKMOV6EST` | `N/D` | - |
| `BKMOV6ORGL` | `N/D` | - |
| `BKMOV6CXA` | `N/D` | - |
| `BKMOV6HOR` | `N/D` | - |
| `BKMOV6DTAL` | `N/D` | - |
| `BKMOV6CUSU` | `N/D` | - |
| `BKMOV6CLIC` | `N/D` | - |
| `BKMOV6DTAP` | `N/D` | - |
| `BKMOV6SIT` | `N/D` | - |
| `BKMOV6CCRC` | `N/D` | - |
| `BKMOV6CCRD` | `N/D` | - |
| `BKMOV6CCRP` | `N/D` | - |
| `BKMOV6CCRF` | `N/D` | - |
| `BKMOV6CHEO` | `N/D` | - |
| `BKMOV6VLR_` | `N/D` | - |
| `BKMOV6VLEN` | `N/D` | - |
| `BKMOV6CRCH` | `N/D` | - |
| `BKMOV6RCC` | `N/D` | - |
| `BKMOV6DCX` | `N/D` | - |
| `BKMOV6FILP` | `N/D` | - |
| `BKMOV6CCx` | `N/D` | - |
| `BKMOV6MovDta` | `N/D` | - |
| `BKMOV6SeqVda` | `N/D` | - |
| `BKMOV6ParVda` | `N/D` | - |
| `BKMO6ObsBxaCar` | `N/D` | - |
| `BKMOV6TSTPOCF1` | `N/D` | - |
| `BKMOV6TstLct` | `N/D` | - |
| `BKMOV6Idx` | `N/D` | - |
| `BKMOV6VlAcr` | `N/D` | - |
| `BKMOV6CPrg` | `N/D` | - |
| `BKMOV6ObsBxaCar` | `N/D` | - |

#### 🗺️ Índices
- `BKMOV6A` (Unique): `BKEMPCOD`, `BKFILCOD`, `BKMOV6SEQ`
- `BKMOV63` (Duplicate): `BKEMPCOD`, `BKFILCOD`, `BKMOV6SEQ`
- `BKMOV64` (Duplicate): `BKEMPCOD`, `BKMOV6DTAL`
- `BKMOV65` (Duplicate): `BKEMPCOD`, `BKMOV6CLIC`, `BKMOV6DTAL`, `BKMOV6CCRC`
- `BKMOV66` (Duplicate): `BKEMPCOD`, `BKMOV6CCRC`, `BKMOV6CCRF`, `BKMOV6CCRP`
- `BKMOV67` (Duplicate): `BKMOV6DCX`

---

### 📌 CCAno
- **Descrição:** Controla Banco Ano\Mês
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCAnoAno`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CCBcoCod` | `N/D` | - |
| `CCAnoAno` | `N/D` | - |
| `CCAnoExtIni` | `N/D` | - |
| `CCAnoExtFin` | `N/D` | - |
| `CCAnoVlrCre` | `N/D` | - |
| `CCAnoVlrDeb` | `N/D` | - |

#### 🗺️ Índices
- `CCAno1` (Unique): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCAnoAno`
- `CCAno2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCBcoCod`

---

### 📌 CCBco
- **Descrição:** Bancos
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CCBcoCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMFilModBolBco` | `N/D` | - |
| `CCBcoCod` | `N/D` | - |
| `CCBcoNroCta` | `N/D` | - |
| `CCBcoDes` | `N/D` | - |
| `CCBcoEmpDtaVal` | `N/D` | - |
| `CCBcoCUsu` | `N/D` | - |
| `CCBcoCDta` | `N/D` | - |
| `CCBcoCHor` | `N/D` | - |
| `CCBcoCPrg` | `N/D` | - |
| `CCBcoDtaConExt` | `N/D` | - |
| `CCBcoDtaTrs` | `N/D` | - |
| `CCBcoPrxSeqLct` | `N/D` | - |
| `CCBcoFlaDel` | `N/D` | - |
| `CCBcoV1` | `N/D` | - |
| `CCBCoBEB` | `N/D` | - |
| `CCBcoAnoFec` | `N/D` | - |
| `CCBcoMesFec` | `N/D` | - |
| `CCBcoTSTPro` | `N/D` | - |
| `CCBcoSalIniAtu` | `N/D` | - |
| `CCBcoSalFinAtu` | `N/D` | - |
| `CCBcoVlrCre` | `N/D` | - |
| `CCBcoVlrDeb` | `N/D` | - |
| `CCBCoBAg` | `N/D` | - |
| `CCBcoFlxCxa` | `N/D` | - |
| `CCBcoUsuRes` | `N/D` | - |
| `CCBcoVlrFinExt` | `N/D` | - |
| `CCBcoSalAtuCC` | `N/D` | - |
| `CCBcoVer` | `N/D` | - |
| `CCBcoBCl` | `N/D` | - |
| `CCBCoBNr` | `N/D` | - |
| `CCBCoBNC` | `N/D` | - |
| `CCBcoBCr` | `N/D` | - |
| `CCBCoBDC` | `N/D` | - |
| `CCBCoBMd` | `N/D` | - |
| `CCBcoBMo` | `N/D` | - |
| `CCBCoBFV` | `N/D` | - |
| `CCBCoBIB` | `N/D` | - |
| `CCBCoBEM` | `N/D` | - |
| `CCBCOBED` | `N/D` | - |
| `CCBCoBAC` | `N/D` | - |
| `CCBCoBAce` | `N/D` | - |
| `CCBCoOb1` | `N/D` | - |
| `CCBCoOb2` | `N/D` | - |
| `CCBCoOb3` | `N/D` | - |
| `CCBCoOb4` | `N/D` | - |
| `CCBCoOb5` | `N/D` | - |
| `CCBCoOb6` | `N/D` | - |
| `CCBCoOb7` | `N/D` | - |
| `CCBCoOb8` | `N/D` | - |
| `CCBCoBLP` | `N/D` | - |
| `CCBCoBCE` | `N/D` | - |
| `CCBCoBNB` | `N/D` | - |
| `CCBCoBCB` | `N/D` | - |
| `CCBCoCedCC` | `N/D` | - |
| `CCBCoCedDC` | `N/D` | - |
| `CCBCoInst1` | `N/D` | - |
| `CCBCoInst2` | `N/D` | - |
| `CCBCoDigAg` | `N/D` | - |
| `CCBcoBolJur` | `N/D` | - |
| `CCBCOBolMul` | `N/D` | - |
| `CCBcoBolPro` | `N/D` | - |
| `CCBcoBolMsg` | `N/D` | - |
| `CCBcoBolIni` | `N/D` | - |
| `CCBcoBolFin` | `N/D` | - |
| `CCBcoBolTip` | `N/D` | - |
| `CCBcoBolRemLay` | `N/D` | - |
| `CCBcoBolLayRet` | `N/D` | - |
| `CCBcoArqLic` | `N/D` | - |
| `CCBcoBol2Det` | `N/D` | - |
| `CCBcoBol3Det` | `N/D` | - |
| `CCBcoBol4Det` | `N/D` | - |
| `CCBcoBol5Det` | `N/D` | - |
| `CCBcoDirImg` | `N/D` | - |
| `CCBcoDirRem` | `N/D` | - |
| `CCBcoLog` | `N/D` | - |
| `CCBcoBol1Out` | `N/D` | - |
| `CCBcoBol2Out` | `N/D` | - |
| `CCBcoBol1InsCxa` | `N/D` | - |
| `CCBcoBolDem` | `N/D` | - |
| `CCBcoBolCBX` | `N/D` | - |
| `CCBcoBolSeqRem` | `N/D` | - |
| `CCBcoPerMulta` | `N/D` | - |
| `CCBcoPerJuros` | `N/D` | - |
| `CCBcoConv` | `N/D` | - |
| `CCBcoRemTeste` | `N/D` | - |
| `CCBcoModBol` | `N/D` | - |
| `CCBcoRazFan` | `N/D` | - |
| `CCBcoSacRF` | `N/D` | - |
| `CCBcoCarRem` | `N/D` | - |
| `CCBcoJurPV` | `N/D` | - |
| `CCBcoMovRem` | `N/D` | - |
| `CCBcoCodPrt` | `N/D` | - |
| `CCBcoDiasPrt` | `N/D` | - |
| `CCBcoPosto` | `N/D` | - |
| `CCBcoPthCer` | `N/D` | - |
| `CCBcoPthSen` | `N/D` | - |
| `CCBcoCliID` | `N/D` | - |
| `CCBcoCNPJ` | `N/D` | - |
| `CCBcoPthArq` | `N/D` | - |
| `CCBcoTipMul` | `N/D` | - |
| `CCBcoTipJur` | `N/D` | - |
| `CCBcoNroCob` | `N/D` | - |
| `CCBcoDtaUltRet` | `N/D` | - |

#### 🗺️ Índices
- `CCBco1` (Unique): `CMEmpCod`, `CMFilCod`, `CCBcoCod`
- `CCBco2` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CCBco4` (Duplicate): `CMEmpCod`, `CCBcoDes`

---

### 📌 CCBxM
- **Descrição:** Banco x Movimento
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCBxMCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CCBcoCod` | `N/D` | - |
| `CCBxMCod` | `N/D` | - |
| `CCBxMTmvCod` | `N/D` | - |

#### 🗺️ Índices
- `CCBxM1` (Unique): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCBxMCod`
- `CCBxM2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCBcoCod`

---

### 📌 CCExt
- **Descrição:** Controla Data e Valor do Fechamento do Extrato
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCExtDta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CCBcoCod` | `N/D` | - |
| `CCBcoDes` | `N/D` | - |
| `CCExtDta` | `N/D` | - |
| `CCExtSts` | `N/D` | - |
| `CCExtTST` | `N/D` | - |
| `CCExtUsu` | `N/D` | - |
| `CCExtPrg` | `N/D` | - |
| `CCExtVlrCre` | `N/D` | - |
| `CCExtVlrDeb` | `N/D` | - |
| `CCExtVlrIni` | `N/D` | - |
| `CCExtVlrFin` | `N/D` | - |

#### 🗺️ Índices
- `CCExt1` (Unique): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCExtDta`
- `CCExt2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCBcoCod`
- `CCExt3` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCExtDta`

---

### 📌 CCMes
- **Descrição:** Movimento do Banco no Mês
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCAnoAno`, `CCMesMes`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CCBcoCod` | `N/D` | - |
| `CCAnoAno` | `N/D` | - |
| `CCAnoExtIni` | `N/D` | - |
| `CCAnoExtFin` | `N/D` | - |
| `CCAnoVlrCre` | `N/D` | - |
| `CCAnoVlrDeb` | `N/D` | - |
| `CCMesMes` | `N/D` | - |
| `CCMesExtIni` | `N/D` | - |
| `CCMesExtFin` | `N/D` | - |
| `CCMesVlrCre` | `N/D` | - |
| `CCMesVlrDeb` | `N/D` | - |
| `CCMesSts` | `N/D` | - |
| `CCMesDtaFin` | `N/D` | - |
| `CCMesCPrg` | `N/D` | - |
| `CCMesDtaIni` | `N/D` | - |
| `CCMesCHor` | `N/D` | - |
| `CCMesCUsu` | `N/D` | - |
| `CCMesACM` | `N/D` | - |
| `CCMesADM` | `N/D` | - |
| `CCMesACG` | `N/D` | - |
| `CCMesADG` | `N/D` | - |
| `CCBcoDes` | `N/D` | - |

#### 🗺️ Índices
- `CCMes1` (Unique): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCAnoAno`, `CCMesMes`
- `CCMes2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCAnoAno`
- `CCMes3` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCMesDtaIni`
- `CCMes4` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCAnoAno`, `CCBcoCod`
- `CCMes5` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCAnoAno`, `CCMesMes`, `CCBcoCod`

---

### 📌 CCMov
- **Descrição:** Movimentação do Conta Corrente
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCMovSeqLct`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CCBcoCod` | `N/D` | - |
| `CCMovSeqLct` | `N/D` | - |
| `CCMovDtaVcto` | `N/D` | - |
| `CMEmpMoeCodPad` | `N/D` | - |
| `CCBcoEmpDtaVal` | `N/D` | - |
| `CCBcoDtaTrs` | `N/D` | - |
| `CCBcoDes` | `N/D` | - |
| `CCBcoDtaConExt` | `N/D` | - |
| `CCBcoVlrFinExt` | `N/D` | - |
| `CCBcoPrxSeqLct` | `N/D` | - |
| `CMFilDtaValLct` | `N/D` | - |
| `CMFilBcoCof` | `N/D` | - |
| `CMFilFilBcoCof` | `N/D` | - |
| `CCBcoSalFinAtu` | `N/D` | - |
| `CCBcoSalAtuCC` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CCBcoFlxCxa` | `N/D` | - |
| `CCBcoUsuRes` | `N/D` | - |
| `CCMovNro` | `N/D` | - |
| `CCTmvCod` | `N/D` | - |
| `CCTmvFlg` | `N/D` | - |
| `CCTmvDspCod` | `N/D` | - |
| `CCTmvDes` | `N/D` | - |
| `CCTmvDebCre` | `N/D` | - |
| `CMMoeDDta` | `N/D` | - |
| `CCMovDtaLan` | `N/D` | - |
| `CCMovDtaPgto` | `N/D` | - |
| `CCMovFlag` | `N/D` | - |
| `CCMovObs` | `N/D` | - |
| `CCMovDC` | `N/D` | - |
| `CCMovVlr` | `N/D` | - |
| `CCMovVlrOrg` | `N/D` | - |
| `CCMovJus` | `N/D` | - |
| `CCMovCUsu` | `N/D` | - |
| `CCMovCDta` | `N/D` | - |
| `CCMovCHor` | `N/D` | - |
| `CCMovDtaTrs` | `N/D` | - |
| `CCMovCPrg` | `N/D` | - |
| `DSDspCod` | `N/D` | - |
| `DSDspDes` | `N/D` | - |
| `CCMov_DSMov2Seq` | `N/D` | - |
| `CCMovDSMov2Dta` | `N/D` | - |
| `CCMovOrg` | `N/D` | - |
| `CCMovCCrCod` | `N/D` | - |
| `DSDspRecDsp` | `N/D` | - |
| `DSGrpCod` | `N/D` | - |
| `DSGrpDes` | `N/D` | - |
| `DSSgrCod` | `N/D` | - |
| `DSSgrDes` | `N/D` | - |
| `CCMovDSGrpCod` | `N/D` | - |
| `CCMovDSSgrCod` | `N/D` | - |
| `CCMovDSGDes` | `N/D` | - |
| `CCMovDSSDes` | `N/D` | - |
| `CCMovIdeExt` | `N/D` | - |
| `CCMovTMMCod` | `N/D` | - |
| `CCMovObsAux` | `N/D` | - |
| `CCMovSal` | `N/D` | - |
| `CCMovSalOK` | `N/D` | - |
| `CCMovSalSeq` | `N/D` | - |
| `CCMovDcx` | `N/D` | - |
| `CCMovSalSAux` | `N/D` | - |
| `CCMovFilLct` | `N/D` | - |
| `CCMovCnfExt` | `N/D` | - |
| `CCMovStsDev` | `N/D` | - |
| `CCMovVlrJrs` | `N/D` | - |
| `CCMovVlrDsc` | `N/D` | - |
| `CCMovVlrFin` | `N/D` | - |
| `CCMovCanUsu` | `N/D` | - |
| `CCMovCanPrg` | `N/D` | - |
| `CCMovCanTst` | `N/D` | - |
| `CCMovAltUsu` | `N/D` | - |
| `CCMovAltTst` | `N/D` | - |
| `CCMovAltPrg` | `N/D` | - |
| `CCMovDtaDev` | `N/D` | - |
| `CCMovCheOut` | `N/D` | - |
| `CCMovCRChaCod` | `N/D` | - |

#### 🗺️ Índices
- `CCMov1` (Unique): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCMovSeqLct`
- `CCMov3` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCBcoCod`
- `CCMov2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCTmvCod`
- `CCMovA` (Duplicate): `CMEmpCod`, `DSDspCod`
- `CCMov4` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCMovDtaVcto`
- `CCMov5` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCMovDtaLan`
- `CCMov6` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCMovDtaPgto`, `CCMovSalSeq`
- `CCMov7` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCMovFlag`, `CCMovDtaVcto`
- `CCMov8` (Duplicate): `CMEmpCod`, `CCMovDtaTrs`
- `CCMov9` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCMovNro`, `CCMovDtaPgto`
- `CCMovB` (Duplicate): `CCMovStsDev`, `CCMovDtaDev`
- `CCMovC` (Duplicate): `CCMovDtaLan`
- `CCMovD` (Duplicate): `CCMovDtaPgto`

---

### 📌 CCRBB
- **Descrição:** Retorno Extato do B.Brasil
- **Chave Primária:** `CCRBBDta`, `CCRBBNroDoc`, `CCRBBD_C`, `CCRBBDes`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CCRBBDta` | `N/D` | - |
| `CCRBBNroDoc` | `N/D` | - |
| `CCRBBD_C` | `N/D` | - |
| `CCRBBDes` | `N/D` | - |
| `CCRBBVlr` | `N/D` | - |
| `CCRBBDtaImp` | `N/D` | - |
| `CCRBBAux1` | `N/D` | - |
| `CCRBBAux2` | `N/D` | - |
| `CCRBBAux3` | `N/D` | - |

#### 🗺️ Índices
- `CCRBB1` (Unique): `CCRBBDta`, `CCRBBNroDoc`, `CCRBBD_C`, `CCRBBDes`

---

### 📌 CCRMC
- **Descrição:** Controle Remessa de Arquivo para Banco - Boletos
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CRRMCTip`, `CCRMCCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CCBcoCod` | `N/D` | - |
| `CRRMCTip` | `N/D` | - |
| `CCRMCCod` | `N/D` | - |
| `CCRMCTst` | `N/D` | - |
| `CCRMCCusu` | `N/D` | - |
| `CCBcoDes` | `N/D` | - |
| `CCRMCPrg` | `N/D` | - |
| `CCRMCVlrOrg` | `N/D` | - |
| `CCRMCQtd` | `N/D` | - |
| `CCRMCArq` | `N/D` | - |
| `CCRMCOco` | `N/D` | - |

#### 🗺️ Índices
- `CCRMC1` (Unique): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CRRMCTip`, `CCRMCCod`
- `CCRMC2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCBcoCod`

---

### 📌 CCRMD
- **Descrição:** Controle Remessa de Arquivo para Banco - Detalhes
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CRRMCTip`, `CCRMCCod`, `CCRMDBol`, `CCRMDAux`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CCBcoCod` | `N/D` | - |
| `CRRMCTip` | `N/D` | - |
| `CCRMCCod` | `N/D` | - |
| `CCRMCTst` | `N/D` | - |
| `CCRMCCusu` | `N/D` | - |
| `CCBcoDes` | `N/D` | - |
| `CCRMCPrg` | `N/D` | - |
| `CCRMCVlrOrg` | `N/D` | - |
| `CCRMCQtd` | `N/D` | - |
| `CCRMCArq` | `N/D` | - |
| `CCRMCOco` | `N/D` | - |
| `CCRMDBol` | `N/D` | - |
| `CCRMDAux` | `N/D` | - |
| `CCRMDEmp` | `N/D` | - |
| `CCRMDFil` | `N/D` | - |
| `CCRMDDta` | `N/D` | - |
| `CCRMDSeq` | `N/D` | - |
| `CCRMDPar` | `N/D` | - |
| `CCRMDNDB` | `N/D` | - |
| `CCRMDVlrOrg` | `N/D` | - |
| `CCRMDDtaBxa` | `N/D` | - |
| `CCRMDTipBxa` | `N/D` | - |
| `CCRMDDig` | `N/D` | - |
| `CCRMDVrBanco` | `N/D` | - |
| `CCRMDSts` | `N/D` | - |
| `CCRMDDtaVct` | `N/D` | - |
| `CCRMDOco` | `N/D` | - |

#### 🗺️ Índices
- `CCRMD1` (Unique): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CRRMCTip`, `CCRMCCod`, `CCRMDBol`, `CCRMDAux`
- `CCRMD2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CRRMCTip`, `CCRMCCod`

---

### 📌 CCSeB
- **Descrição:** Controle Númeração Boleto/Remessa Por CNPJ
- **Chave Primária:** `CMEmpCod`, `CCBcoCod`, `CCSeBCNPJ`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CCBcoCod` | `N/D` | - |
| `CCSeBCNPJ` | `N/D` | - |
| `CCSeBNroBol` | `N/D` | - |
| `CCSeBNroRem` | `N/D` | - |
| `CCSeBDbg` | `N/D` | - |
| `CCSeBDtaRet` | `N/D` | - |

#### 🗺️ Índices
- `CCSeB1` (Unique): `CMEmpCod`, `CCBcoCod`, `CCSeBCNPJ`
- `CCSeB2` (Duplicate): `CMEmpCod`

---

### 📌 CCTMM
- **Descrição:** Tipo de Movimento por MÊs
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCAnoAno`, `CCMesMes`, `CCTMMCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CCBcoCod` | `N/D` | - |
| `CCAnoAno` | `N/D` | - |
| `CCAnoExtIni` | `N/D` | - |
| `CCAnoExtFin` | `N/D` | - |
| `CCAnoVlrCre` | `N/D` | - |
| `CCAnoVlrDeb` | `N/D` | - |
| `CCMesMes` | `N/D` | - |
| `CCMesExtIni` | `N/D` | - |
| `CCMesExtFin` | `N/D` | - |
| `CCMesVlrCre` | `N/D` | - |
| `CCMesVlrDeb` | `N/D` | - |
| `CCMesSts` | `N/D` | - |
| `CCMesDtaFin` | `N/D` | - |
| `CCMesCPrg` | `N/D` | - |
| `CCMesDtaIni` | `N/D` | - |
| `CCMesCHor` | `N/D` | - |
| `CCMesCUsu` | `N/D` | - |
| `CCMesACM` | `N/D` | - |
| `CCMesADM` | `N/D` | - |
| `CCMesACG` | `N/D` | - |
| `CCMesADG` | `N/D` | - |
| `CCTMMCod` | `N/D` | - |
| `CCTMMDes` | `N/D` | - |
| `CCTMMVlr` | `N/D` | - |
| `CCTMMTmvCod` | `N/D` | - |
| `CCBcoDes` | `N/D` | - |
| `CCTMMTST` | `N/D` | - |
| `CCTMMUSU` | `N/D` | - |
| `CCTMMPRG` | `N/D` | - |
| `CCTMMDebCre` | `N/D` | - |

#### 🗺️ Índices
- `CCTMM1` (Unique): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCAnoAno`, `CCMesMes`, `CCTMMCod`
- `CCTMM2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CCBcoCod`, `CCAnoAno`, `CCMesMes`

---

### 📌 CCTmv
- **Descrição:** Tipo de Movimentação Bancária
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CCTmvCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CCTmvCod` | `N/D` | - |
| `CCTmvDes` | `N/D` | - |
| `CCTmvDebCre` | `N/D` | - |
| `CCTmvCUsu` | `N/D` | - |
| `CCTmvCDta` | `N/D` | - |
| `CCTmvCHor` | `N/D` | - |
| `CCTmvCPrg` | `N/D` | - |
| `CCTmvDtaTrs` | `N/D` | - |
| `CCTmvFlg` | `N/D` | - |
| `CCTmvFlaDel` | `N/D` | - |
| `CCTmvDspCod` | `N/D` | - |
| `CCTmvTip` | `N/D` | - |
| `CCTmvFlxCxa` | `N/D` | - |
| `CCTmvEntSilWeb` | `N/D` | - |

#### 🗺️ Índices
- `CCTmv1` (Unique): `CMEmpCod`, `CMFilCod`, `CCTmvCod`
- `CCTmv2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CEAbc
- **Descrição:** CEAbc
- **Chave Primária:** `med_abc`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `med_abc` | `N/D` | - |
| `med_ctr` | `N/D` | - |
| `med_lab` | `N/D` | - |
| `lab_nom` | `N/D` | - |
| `med_des` | `N/D` | - |
| `med_apr` | `N/D` | - |
| `med_pco18` | `N/D` | - |
| `med_pla18` | `N/D` | - |
| `med_fra18` | `N/D` | - |
| `med_pco1` | `N/D` | - |
| `Med_pla1` | `N/D` | - |
| `med_fra1` | `N/D` | - |
| `med_pco17` | `N/D` | - |
| `med_pla17` | `N/D` | - |
| `med_fra17` | `N/D` | - |
| `med_pco12` | `N/D` | - |
| `med_pla12` | `N/D` | - |
| `med_fra12` | `N/D` | - |
| `med_uni` | `N/D` | - |
| `med_ipi` | `N/D` | - |
| `med_dtvig` | `N/D` | - |
| `exp_13` | `N/D` | - |
| `med_barra` | `N/D` | - |
| `med_gene` | `N/D` | - |
| `med_negpos` | `N/D` | - |
| `med_netro` | `N/D` | - |
| `med_princi` | `N/D` | - |
| `med_pco19` | `N/D` | - |
| `med_pla19` | `N/D` | - |
| `med_fra19` | `N/D` | - |
| `med_pcozfm` | `N/D` | - |
| `med_plazfm` | `N/D` | - |
| `med_frazfm` | `N/D` | - |
| `med_regims` | `N/D` | - |
| `med_varpre` | `N/D` | - |

#### 🗺️ Índices
- `CEABC1` (Unique): `med_abc`
- `CEABC2` (Duplicate): `med_barra`
- `CEABC3` (Duplicate): `med_des`

---

### 📌 CEAgr
- **Descrição:** Agrupador Produtos
- **Chave Primária:** `CMEmpCod`, `CEAgrCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEAgrCod` | `N/D` | - |
| `CEAgrFab` | `N/D` | - |
| `CEAgrGrpCod` | `N/D` | - |
| `CEAgrSgrCod` | `N/D` | - |
| `CEAgrCUsu` | `N/D` | - |
| `CEAgrCDta` | `N/D` | - |
| `CEAgrCHor` | `N/D` | - |
| `CEAgrCPrg` | `N/D` | - |
| `CEAgrDes` | `N/D` | - |
| `CEAgrDesRes` | `N/D` | - |
| `CEAgrMrgLuc` | `N/D` | - |
| `CEAgrQtdPar` | `N/D` | - |
| `CMEmpCEMrgLuc` | `N/D` | - |
| `CMEmpCEQtdPar` | `N/D` | - |
| `CEAgr1Cus` | `N/D` | - |
| `CEAgrPre1Tab` | `N/D` | - |
| `CEAgrPre2Tab` | `N/D` | - |
| `CEAgrPre3Tab` | `N/D` | - |
| `CEAgrPre4Tab` | `N/D` | - |
| `CEAgrPerDes` | `N/D` | - |
| `CEAgrCor` | `N/D` | - |
| `CEAgrVlrPar` | `N/D` | - |
| `CEAgrCusMed` | `N/D` | - |
| `CEAgrPrcCom` | `N/D` | - |
| `CEAgrAtuPrePelDis` | `N/D` | - |
| `CEAgrImpLisCom` | `N/D` | - |
| `CEAgrNomLabFar` | `N/D` | - |
| `CMEmpCEUsaGrpSgr` | `N/D` | - |
| `CEAgrEstMax` | `N/D` | - |
| `CEAgrEstMin` | `N/D` | - |
| `CEAgrPreGel` | `N/D` | - |
| `CEAgrNCM` | `N/D` | - |
| `CEAgrCST` | `N/D` | - |

#### 🗺️ Índices
- `CEAgr1` (Unique): `CMEmpCod`, `CEAgrCod`
- `CEAgr2` (Duplicate): `CMEmpCod`
- `CEAgr3` (Duplicate): `CMEmpCod`, `CEAgrDes`

---

### 📌 CEAno
- **Descrição:** Vendas Produtos Anual
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CEProCod`, `CEAno`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEAno` | `N/D` | - |
| `CEAnoQtdEnt` | `N/D` | - |
| `CEAnoQtdSai` | `N/D` | - |
| `CEAnoQtdVda` | `N/D` | - |
| `CEAnoQtdCom` | `N/D` | - |
| `CEAnoQtd_SaiTrs` | `N/D` | - |
| `CEAnoQtd_EntTrs` | `N/D` | - |
| `CEAnoIND` | `N/D` | - |
| `CEAnoFlaDel` | `N/D` | - |
| `CEAnoDtaTrs` | `N/D` | - |
| `CEAnoVlrLuc` | `N/D` | - |
| `CEAnoVlrCus` | `N/D` | - |
| `CEAnoVlrVda` | `N/D` | - |
| `CEAnoQtdOutEnt` | `N/D` | - |
| `CEAnoQtd_OutSai` | `N/D` | - |
| `CEAnoMrg` | `N/D` | - |
| `CEAnoQtdEVC` | `N/D` | - |
| `CEAnoQtdSCC` | `N/D` | - |
| `CEAnoQtdSTM` | `N/D` | - |
| `CEAnoQtdETM` | `N/D` | - |
| `CEAnoTotEnt` | `N/D` | - |
| `CEAnoTotSai` | `N/D` | - |

#### 🗺️ Índices
- `CEAno1` (Unique): `CMEmpCod`, `CMFilCod`, `CEProCod`, `CEAno`
- `CEAno2` (Duplicate): `CMEmpCod`, `CEProCod`
- `CEAno3` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CEAno4` (Duplicate): `CMEmpCod`, `CMFilCod`, `CEAno`, `CEAnoIND`
- `CEANo5` (Duplicate): `CMEmpCod`, `CEAno`, `CEProCod`
- `CEAno6` (Duplicate): `CMEmpCod`, `CEProCod`, `CEAno`

---

### 📌 CEBFI
- **Descrição:** Arquivo CadTxt Filizola
- **Chave Primária:** `CEBFICodPro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CEBFICodPro` | `N/D` | - |
| `CEBFIPesUnd` | `N/D` | - |
| `CEBFIDes` | `N/D` | - |
| `CEBFIPreUnt` | `N/D` | - |
| `CEBFIPrzVal` | `N/D` | - |

#### 🗺️ Índices
- `CEBFI1` (Unique): `CEBFICodPro`

---

### 📌 CEBFS
- **Descrição:** Arquivo Setortxt Filizola
- **Chave Primária:** `CEBFSDes`, `CEBFSProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CEBFSDes` | `N/D` | - |
| `CEBFSProCod` | `N/D` | - |
| `CEBFIInd` | `N/D` | - |
| `CEBFSTecAss` | `N/D` | - |

#### 🗺️ Índices
- `CEBFS1` (Unique): `CEBFSDes`, `CEBFSProCod`

---

### 📌 CEBTI
- **Descrição:** Itens da Balanca Toledo
- **Chave Primária:** `CEBTIDepCod`, `CEBTIEtq`, `CEBTIUndPes`, `CEBTICodPro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CEBTIDepCod` | `N/D` | - |
| `CEBTIEtq` | `N/D` | - |
| `CEBTIUndPes` | `N/D` | - |
| `CEBTICodPro` | `N/D` | - |
| `CEBTIPreVda` | `N/D` | - |
| `CEBTIDiaVal` | `N/D` | - |
| `CEBTIDes1` | `N/D` | - |

#### 🗺️ Índices
- `CEBTI1` (Unique): `CEBTIDepCod`, `CEBTIEtq`, `CEBTIUndPes`, `CEBTICodPro`

---

### 📌 CECA1
- **Descrição:** Características dos Produtos
- **Chave Primária:** `CMEmpCod`, `CECA1COD`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CECA1COD` | `N/D` | - |
| `CECA1DES` | `N/D` | - |
| `CECA1EXINIV2` | `N/D` | - |
| `CECA1Sts` | `N/D` | - |

#### 🗺️ Índices
- `CECA1A` (Unique): `CMEmpCod`, `CECA1COD`
- `CECA1B` (Duplicate): `CMEmpCod`

---

### 📌 CECA2
- **Descrição:** Características do Produto 02
- **Chave Primária:** `CMEmpCod`, `CECA1COD`, `CECA2COD`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CECA1COD` | `N/D` | - |
| `CECA1DES` | `N/D` | - |
| `CECA1EXINIV2` | `N/D` | - |
| `CECA1Sts` | `N/D` | - |
| `CECA2COD` | `N/D` | - |
| `CECA2DES` | `N/D` | - |

#### 🗺️ Índices
- `CECA2A` (Unique): `CMEmpCod`, `CECA1COD`, `CECA2COD`
- `CECE2B` (Duplicate): `CMEmpCod`, `CECA1COD`

---

### 📌 CECdx1
- **Descrição:** Cardex 01
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CECdxDta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CECdxDta` | `N/D` | - |
| `CECdx1AuxSeq` | `N/D` | - |
| `CECdx1DtaTrs` | `N/D` | - |
| `CECdx1FlaDel` | `N/D` | - |

#### 🗺️ Índices
- `CECdx11` (Unique): `CMEmpCod`, `CMFilCod`, `CECdxDta`
- `CECdx12` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CECdx2
- **Descrição:** Cardex 02
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CECdxDta`, `CECdx2Seq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CECdxDta` | `N/D` | - |
| `CECdx2Seq` | `N/D` | - |
| `CMEmpMoeCodPad` | `N/D` | - |
| `CMMoeDDta` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CECdx2CDta` | `N/D` | - |
| `CECdx2CHor` | `N/D` | - |
| `CECdx2CUsu` | `N/D` | - |
| `CECdx2CPrg` | `N/D` | - |
| `CECdx2NroNFi` | `N/D` | - |
| `CECdx2SerNFi` | `N/D` | - |
| `CECdx2DtaNFi` | `N/D` | - |
| `CECdx2Obs` | `N/D` | - |
| `CECdx2CodCliFor` | `N/D` | - |
| `CECdx2TipMov` | `N/D` | - |
| `CECdx2Qtd` | `N/D` | - |
| `CECdx2Sal` | `N/D` | - |
| `CECdx2SalV1` | `N/D` | - |
| `CECdxFlaDel` | `N/D` | - |
| `CECdxDtaTrs` | `N/D` | - |
| `CECdx2CusAnt` | `N/D` | - |
| `CECdx2MoeCusAnt` | `N/D` | - |
| `CECdx2Moe1CusAtu` | `N/D` | - |
| `CECdx2Cus1Atu` | `N/D` | - |
| `CECdx2NopCod` | `N/D` | - |
| `CECdx2NopDes` | `N/D` | - |
| `CECdx2DtaInv` | `N/D` | - |
| `CECdx2DtaMov` | `N/D` | - |
| `CECdx2SeqMov` | `N/D` | - |
| `CECdx2FilOrg` | `N/D` | - |
| `CECdx2FilDes` | `N/D` | - |
| `CECdx2CusTotMov` | `N/D` | - |
| `CECdx2IgnMov` | `N/D` | - |
| `CECdx2AcuMov` | `N/D` | - |
| `CECdx2Acu_MovAux` | `N/D` | - |
| `CECdx2DesTipMov` | `N/D` | - |
| `CECdx2ErrAcu` | `N/D` | - |
| `CECdx2PreVda` | `N/D` | - |
| `CECdx2Lot` | `N/D` | - |
| `CECdx2LotVct` | `N/D` | - |
| `CECdx2SeqAux` | `N/D` | - |
| `CECdx2SNGMotPer` | `N/D` | - |
| `CECdx2PQA` | `N/D` | - |
| `CECdx2DspCod` | `N/D` | - |
| `CECdx2IteCRCP` | `N/D` | - |
| `CECdx2IDEPCN` | `N/D` | - |
| `CECdx2PVU` | `N/D` | - |
| `CECdx2DesPCN` | `N/D` | - |
| `CECdx2DesCliFor` | `N/D` | - |
| `CECdx2Sit` | `N/D` | - |
| `CECdx2NFCSeq` | `N/D` | - |

#### 🗺️ Índices
- `CECdx21` (Unique): `CMEmpCod`, `CMFilCod`, `CECdxDta`, `CECdx2Seq`
- `CECdx23` (Duplicate): `CMEmpCod`, `CMFilCod`, `CECdxDta`
- `CECdx22` (Duplicate): `CMEmpCod`, `CEProCod`
- `CECdx24` (Duplicate): `CMEmpCod`, `CEProCod`, `CECdxDta`, `CECdx2Seq`
- `CECdx25` (Duplicate): `CMEmpCod`, `CEProCod`, `CECdxDta`, `CECdx2Seq`
- `CECdx26` (Duplicate): `CMEmpCod`, `CECdxDta`, `CEProCod`, `CECdx2Seq`
- `CECdx27` (Duplicate): `CMEmpCod`, `CMFilCod`, `CECdx2DtaMov`, `CECdx2SeqMov`
- `CECdx28` (Duplicate): `CECdx2Acu_MovAux`
- `CECdx29` (Duplicate): `CECdx2AcuMov`, `CEProCod`
- `CECdx2A` (Duplicate): `CEProCod`, `CECdx2SeqAux`

---

### 📌 CECdx3
- **Descrição:** Divergências Estoque x CECdx
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CECdx3Dta`, `CECdx3ProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CECdx3Dta` | `N/D` | - |
| `CECdx3ProCod` | `N/D` | - |
| `CECdx3ProDes` | `N/D` | - |
| `CECdx3QtdEst` | `N/D` | - |
| `CECdx3QtdCdx` | `N/D` | - |
| `CECdx3Usu` | `N/D` | - |
| `CECdx3Prg` | `N/D` | - |
| `CECdx3Tst` | `N/D` | - |

#### 🗺️ Índices
- `CECdx3A` (Unique): `CMEmpCod`, `CMFilCod`, `CECdx3Dta`, `CECdx3ProCod`
- `CECdx3B` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CECdx3C` (Duplicate): `CECdx3ProCod`, `CECdx3Dta`

---

### 📌 CECEM
- **Descrição:** Custo Estoque Mensal - Lazuli
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CECEMAMe`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CECEMAMe` | `N/D` | - |
| `CECEMVlrIni` | `N/D` | - |
| `CECEMVlrCPg` | `N/D` | - |
| `CECEMVlrCRe` | `N/D` | - |
| `CECEMVlrFin` | `N/D` | - |
| `CECEMCDta` | `N/D` | - |
| `CECEMCUsu` | `N/D` | - |

#### 🗺️ Índices
- `CECEMA` (Unique): `CMEmpCod`, `CMFilCod`, `CECEMAMe`
- `CECEMB` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CECEMC` (Duplicate): `CMEmpCod`, `CMFilCod`, `CECEMAMe`

---

### 📌 CECES
- **Descrição:** Cadastro de CEST
- **Chave Primária:** `CECESCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CECESCod` | `N/D` | - |
| `CECESDes` | `N/D` | - |
| `CECESDesC1` | `N/D` | - |
| `CECESDesC2` | `N/D` | - |
| `CECESDesC3` | `N/D` | - |
| `CECESDesC4` | `N/D` | - |
| `CECESDesC5` | `N/D` | - |
| `CECESGrpNIni` | `N/D` | - |
| `CECESGrpNFin` | `N/D` | - |
| `CECESLista` | `N/D` | - |

#### 🗺️ Índices
- `CECESA` (Unique): `CECESCod`
- `CECESB` (Duplicate): `CECESGrpNIni`

---

### 📌 CECGS
- **Descrição:** Convênio com Grupo e SubGrupo
- **Chave Primária:** `CMEmpCod`, `CECGSCod`, `CEGrpCod`, `CESgrCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CECGSCod` | `N/D` | - |
| `CEGrpCod` | `N/D` | - |
| `CESgrCod` | `N/D` | - |
| `CEGrpDes` | `N/D` | - |
| `CECGSPerVda` | `N/D` | - |
| `CECGSPrcDsc` | `N/D` | - |
| `CESgrDes` | `N/D` | - |

#### 🗺️ Índices
- `CECGSA` (Unique): `CMEmpCod`, `CECGSCod`, `CEGrpCod`, `CESgrCod`
- `CECGSB` (Duplicate): `CMEmpCod`, `CEGrpCod`, `CESgrCod`

---

### 📌 CECla
- **Descrição:** Tabela Classificação Produtos
- **Chave Primária:** `CMEmpCod`, `CEClaCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEClaCod` | `N/D` | - |
| `CEClaDes` | `N/D` | - |

#### 🗺️ Índices
- `CEClas1` (Unique): `CMEmpCod`, `CEClaCod`
- `CEClas2` (Duplicate): `CMEmpCod`

---

### 📌 CECLF
- **Descrição:** Cadastro de Classificação Fiscal (Reforma Tributária)
- **Chave Primária:** `CMEmpCod`, `CECLFCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CECLFCod` | `N/D` | - |
| `CECLFNom` | `N/D` | - |
| `CECLFDes` | `N/D` | - |
| `CECLFCST` | `N/D` | - |
| `CECLFCSTDes` | `N/D` | - |
| `CECLFDesArt` | `N/D` | - |
| `CECLFDtaAtu` | `N/D` | - |
| `CECLFUFRetIBS` | `N/D` | - |
| `CECLFMunRetIBS` | `N/D` | - |
| `CECLFRetCBS` | `N/D` | - |

#### 🗺️ Índices
- `CECLFA` (Unique): `CMEmpCod`, `CECLFCod`
- `CECLFB` (Duplicate): `CMEmpCod`

---

### 📌 CECot1
- **Descrição:** Cadastro Cotações
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CECot1Seq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CECot1Seq` | `N/D` | - |
| `CECot1Des` | `N/D` | - |
| `CECot1DtaHorLct` | `N/D` | - |
| `CECot1Obs1` | `N/D` | - |
| `CECot1Obs2` | `N/D` | - |
| `CECot1Obs3` | `N/D` | - |
| `CECot1Obs4` | `N/D` | - |

#### 🗺️ Índices
- `CECot11` (Unique): `CMEmpCod`, `CMFilCod`, `CECot1Seq`
- `CECot12` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CECot13` (Duplicate): `CMEmpCod`, `CMFilCod`, `CECot1Seq`

---

### 📌 CECot2
- **Descrição:** Produtos da Cotacao
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CECot1Seq`, `CEProCod`, `CECot2ProDes`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CECot1Seq` | `N/D` | - |
| `CECot1Des` | `N/D` | - |
| `CECot1DtaHorLct` | `N/D` | - |
| `CECot1Obs1` | `N/D` | - |
| `CECot1Obs2` | `N/D` | - |
| `CECot1Obs3` | `N/D` | - |
| `CECot1Obs4` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CECot2ProDes` | `N/D` | - |
| `CECot2CusAtu` | `N/D` | - |
| `CECot2CusCot` | `N/D` | - |
| `CECot2DesForVcd` | `N/D` | - |
| `CECot2CodForVcd` | `N/D` | - |
| `CECot2Qtd` | `N/D` | - |
| `CECot2Sit` | `N/D` | - |
| `CECot2CUsu` | `N/D` | - |
| `CECot2CDta` | `N/D` | - |
| `CECot2CHor` | `N/D` | - |
| `CECot2CPrg` | `N/D` | - |
| `CECot2Ref` | `N/D` | - |

#### 🗺️ Índices
- `CECot21` (Unique): `CMEmpCod`, `CMFilCod`, `CECot1Seq`, `CEProCod`, `CECot2ProDes`
- `CECot22` (Duplicate): `CMEmpCod`, `CEProCod`
- `CECot23` (Duplicate): `CMEmpCod`, `CMFilCod`, `CECot1Seq`
- `CECot24` (Duplicate): `CMEmpCod`, `CMFilCod`, `CECot1Seq`, `CECot2ProDes`, `CEProCod`

---

### 📌 CECot3
- **Descrição:** Fornecedores da Cotação
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CECot1Seq`, `CPCliCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CECot1Seq` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `CECot1Des` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CPCliSen` | `N/D` | - |
| `CECot3PrcAcr` | `N/D` | - |
| `CECot3TotCus` | `N/D` | - |
| `CECot3TotIteCot` | `N/D` | - |
| `CECot3PrcDes` | `N/D` | - |
| `CECot3DtaPed` | `N/D` | - |
| `CECot3Obs1` | `N/D` | - |
| `CECot3Obs2` | `N/D` | - |
| `CECot3Obs3` | `N/D` | - |
| `CECot3Obs4` | `N/D` | - |

#### 🗺️ Índices
- `CECot31` (Unique): `CMEmpCod`, `CMFilCod`, `CECot1Seq`, `CPCliCod`
- `CECot33` (Duplicate): `CMEmpCod`, `CMFilCod`, `CECot1Seq`
- `CECot32` (Duplicate): `CMEmpCod`, `CPCliCod`

---

### 📌 CECot4
- **Descrição:** Cotacao dos Fornecedores
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CECot1Seq`, `CPCliCod`, `CECot2ProDes`, `CEProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CECot1Seq` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `CECot1Des` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CPCliSen` | `N/D` | - |
| `CECot3PrcAcr` | `N/D` | - |
| `CECot3TotCus` | `N/D` | - |
| `CECot3TotIteCot` | `N/D` | - |
| `CECot3PrcDes` | `N/D` | - |
| `CECot3DtaPed` | `N/D` | - |
| `CECot3Obs1` | `N/D` | - |
| `CECot3Obs2` | `N/D` | - |
| `CECot3Obs3` | `N/D` | - |
| `CECot3Obs4` | `N/D` | - |
| `CECot2ProDes` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CECot2Qtd` | `N/D` | - |
| `CECot4Cus` | `N/D` | - |
| `CECot4PrcAcr` | `N/D` | - |
| `CECot4CusAcr` | `N/D` | - |
| `CECot4CusDsc` | `N/D` | - |
| `CECot4TotCus` | `N/D` | - |
| `CECot4PosMenPre` | `N/D` | - |
| `CECot4CUsu` | `N/D` | - |
| `CECot4CDta` | `N/D` | - |
| `CECot4CHor` | `N/D` | - |
| `CECot4IteCot` | `N/D` | - |
| `CECot4CusInd` | `N/D` | - |
| `CECot4CPrg` | `N/D` | - |
| `CECot4Sts` | `N/D` | - |
| `CECot2Lab` | `N/D` | - |
| `CECot4Ref` | `N/D` | - |

#### 🗺️ Índices
- `CECot41` (Unique): `CMEmpCod`, `CMFilCod`, `CECot1Seq`, `CPCliCod`, `CECot2ProDes`, `CEProCod`
- `CECot42` (Duplicate): `CMEmpCod`, `CMFilCod`, `CECot1Seq`, `CEProCod`, `CECot2ProDes`
- `CECot43` (Duplicate): `CMEmpCod`, `CMFilCod`, `CECot1Seq`, `CPCliCod`
- `CECot44` (Duplicate): `CMEmpCod`, `CMFilCod`, `CECot1Seq`, `CEProCod`, `CECot4PosMenPre`
- `CECot45` (Duplicate): `CMEmpCod`, `CMFilCod`, `CECot1Seq`, `CEProCod`, `CECot4CusInd`

---

### 📌 CECrs
- **Descrição:** Tabela de Cores
- **Chave Primária:** `CMEmpCod`, `CECrsCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CECrsCod` | `N/D` | - |
| `CECrsCHor` | `N/D` | - |
| `CECrsDesRes` | `N/D` | - |
| `CECrsCPrg` | `N/D` | - |
| `CECrsCNom` | `N/D` | - |
| `CECrsDtaTrs` | `N/D` | - |
| `CECrsRGB1` | `N/D` | - |
| `CECrsRGB3` | `N/D` | - |
| `CECrsRGB2` | `N/D` | - |
| `CECrsDes` | `N/D` | - |
| `CECrsCDta` | `N/D` | - |

#### 🗺️ Índices
- `CECrs1` (Unique): `CMEmpCod`, `CECrsCod`
- `CECrs2` (Duplicate): `CMEmpCod`

---

### 📌 CEDCV1
- **Descrição:** Desconto Compra Venda 01
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CEDCV1Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CEDCV1Cod` | `N/D` | - |
| `CEDCV1AtiIna` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `CMFilLctPreCusPro` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CEDCV1IdeFor` | `N/D` | - |
| `CEDCV1ComVda` | `N/D` | - |
| `CEDCV1DtaTrs` | `N/D` | - |
| `CEDCV1CDta` | `N/D` | - |
| `CEDCV1CHor` | `N/D` | - |
| `CEDCV1CPrg` | `N/D` | - |
| `CEDCV1CUsu` | `N/D` | - |
| `CEDCV1DtaIni` | `N/D` | - |
| `CEDCV1DtaFin` | `N/D` | - |
| `CEDCV1PrcCom` | `N/D` | - |
| `CMFilPrcAcrVdaPrz` | `N/D` | - |
| `CMFilUsaTabPre` | `N/D` | - |
| `CEDCV1TipCod` | `N/D` | - |

#### 🗺️ Índices
- `CEDCV11` (Unique): `CMEmpCod`, `CMFilCod`, `CEDCV1Cod`
- `CEDCV12` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CEDCV14` (Duplicate): `CMEmpCod`, `CPCliCod`
- `CEDCV13` (Duplicate): `CMEmpCod`, `CMFilCod`, `CEDCV1AtiIna`

---

### 📌 CEDCV2
- **Descrição:** Desconto Compra Venda 02
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CEDCV1Cod`, `CEProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CEDCV1Cod` | `N/D` | - |
| `CEDCV1AtiIna` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `CMFilLctPreCusPro` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CEDCV1IdeFor` | `N/D` | - |
| `CEDCV1ComVda` | `N/D` | - |
| `CEDCV1DtaTrs` | `N/D` | - |
| `CEDCV1CDta` | `N/D` | - |
| `CEDCV1CHor` | `N/D` | - |
| `CEDCV1CPrg` | `N/D` | - |
| `CEDCV1CUsu` | `N/D` | - |
| `CEDCV1DtaIni` | `N/D` | - |
| `CEDCV1DtaFin` | `N/D` | - |
| `CEDCV1PrcCom` | `N/D` | - |
| `CMFilPrcAcrVdaPrz` | `N/D` | - |
| `CMFilUsaTabPre` | `N/D` | - |
| `CEDCV1TipCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEDCV2ProDes` | `N/D` | - |
| `CEDCV2PerDes` | `N/D` | - |
| `CEDCV2PreVis` | `N/D` | - |
| `CEDCV2PrePrz` | `N/D` | - |
| `CEDCV2DtaIni` | `N/D` | - |
| `CEDCV2DtaFin` | `N/D` | - |
| `CEDCV2ComVda` | `N/D` | - |
| `CEDCV2Sts` | `N/D` | - |
| `CEDCV2PreCus` | `N/D` | - |
| `CEDCV2ProPre1Tab` | `N/D` | - |
| `CEDCV2Pr_VisGel` | `N/D` | - |
| `CEDCV2Pre_PrzGel` | `N/D` | - |
| `CEDCV2Pr_Cnv` | `N/D` | - |
| `CEDCV2QtdEtq` | `N/D` | - |
| `CEDCV2Tab1` | `N/D` | - |
| `CEDCV2Tab2` | `N/D` | - |
| `CEDCV2Tab3` | `N/D` | - |
| `CEDCV2Tab4` | `N/D` | - |
| `CEDCV2QtdPar` | `N/D` | - |
| `CEDCV2VlrPar` | `N/D` | - |
| `CEProPre1Tab` | `N/D` | - |
| `CEProFab` | `N/D` | - |
| `CEDCV2QtdVda` | `N/D` | - |
| `CEDCV2NovPreVda` | `N/D` | - |

#### 🗺️ Índices
- `CEDCV21` (Unique): `CMEmpCod`, `CMFilCod`, `CEDCV1Cod`, `CEProCod`
- `CEDCV22` (Duplicate): `CMEmpCod`, `CEProCod`
- `CEDCV23` (Duplicate): `CMEmpCod`, `CMFilCod`, `CEDCV1Cod`

---

### 📌 CEDia
- **Descrição:** Acumulo Estoque Diário
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CEProCod`, `CEAno`, `CEMes`, `CEDia`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEAno` | `N/D` | - |
| `CEAnoQtdEnt` | `N/D` | - |
| `CEAnoQtdSai` | `N/D` | - |
| `CEAnoQtdVda` | `N/D` | - |
| `CEAnoQtdCom` | `N/D` | - |
| `CEAnoQtd_SaiTrs` | `N/D` | - |
| `CEAnoQtd_EntTrs` | `N/D` | - |
| `CEAnoIND` | `N/D` | - |
| `CEAnoFlaDel` | `N/D` | - |
| `CEAnoDtaTrs` | `N/D` | - |
| `CEAnoVlrLuc` | `N/D` | - |
| `CEAnoVlrCus` | `N/D` | - |
| `CEAnoVlrVda` | `N/D` | - |
| `CEAnoQtdOutEnt` | `N/D` | - |
| `CEAnoQtd_OutSai` | `N/D` | - |
| `CEAnoMrg` | `N/D` | - |
| `CEAnoQtdEVC` | `N/D` | - |
| `CEAnoQtdSCC` | `N/D` | - |
| `CEAnoQtdSTM` | `N/D` | - |
| `CEAnoQtdETM` | `N/D` | - |
| `CEAnoTotEnt` | `N/D` | - |
| `CEAnoTotSai` | `N/D` | - |
| `CEMes` | `N/D` | - |
| `CEMesQtdEnt` | `N/D` | - |
| `CEMesQtdSai` | `N/D` | - |
| `CEMesQtdVda` | `N/D` | - |
| `CEMesQtdOutEnt` | `N/D` | - |
| `CEMesQtd_OutSai` | `N/D` | - |
| `CEMesQtdCom` | `N/D` | - |
| `CEMesQtd_SaiTrs` | `N/D` | - |
| `CEMesQtd_EntTrs` | `N/D` | - |
| `CEMesFlaDel` | `N/D` | - |
| `CEMesDtaTrs` | `N/D` | - |
| `CEMesIND` | `N/D` | - |
| `CEMesVlrLuc` | `N/D` | - |
| `CEMesVlrVda` | `N/D` | - |
| `CEMesVlrCus` | `N/D` | - |
| `CEMesEstIni` | `N/D` | - |
| `CEMesEstFin` | `N/D` | - |
| `CEMesAju` | `N/D` | - |
| `CEMesDtaIni` | `N/D` | - |
| `CEMesDtaFin` | `N/D` | - |
| `CEMesDtaHorPro` | `N/D` | - |
| `CEMesEstVda` | `N/D` | - |
| `CEMesEstCom` | `N/D` | - |
| `CEMesMrg` | `N/D` | - |
| `CEMesQtdEVC` | `N/D` | - |
| `CEMesQtdSCC` | `N/D` | - |
| `CEMesQtdSTM` | `N/D` | - |
| `CEMesQtdETM` | `N/D` | - |
| `CEMesQtdAtu` | `N/D` | - |
| `CEMesTotEnt` | `N/D` | - |
| `CEMesTotSai` | `N/D` | - |
| `CEMesDiaPro` | `N/D` | - |
| `CEDia` | `N/D` | - |
| `CEDiaDtaAux` | `N/D` | - |
| `CEDiaQtdEnt` | `N/D` | - |
| `CEDiaQtdSai` | `N/D` | - |
| `CEDiaQtdVda` | `N/D` | - |
| `CEDiaFlaDel` | `N/D` | - |
| `CEDiaDtaTrs` | `N/D` | - |
| `CEDiaQtd_EntTrs` | `N/D` | - |
| `CEDiaQtd_SaiTrs` | `N/D` | - |
| `CEDiaQtdCom` | `N/D` | - |
| `CEDiaQtdOutEnt` | `N/D` | - |
| `CEDiaQtd_OutSai` | `N/D` | - |
| `CEDiaVlrLuc` | `N/D` | - |
| `CEDiaVlrCus` | `N/D` | - |
| `CEDiaVlrVda` | `N/D` | - |
| `CEDiaMrg` | `N/D` | - |
| `CEDiaQtdEVC` | `N/D` | - |
| `CEDiaQtdSCC` | `N/D` | - |
| `CEDiaQtdSTM` | `N/D` | - |
| `CEDiaQtdETM` | `N/D` | - |
| `CEDiaTotEnt` | `N/D` | - |
| `CEDiaTotSai` | `N/D` | - |
| `CEDiaGrvAME` | `N/D` | - |
| `CEDiaEstIni` | `N/D` | - |
| `CEDiaEstFin` | `N/D` | - |
| `CEDiaEstCal` | `N/D` | - |

#### 🗺️ Índices
- `CEDia1` (Unique): `CMEmpCod`, `CMFilCod`, `CEProCod`, `CEAno`, `CEMes`, `CEDia`
- `CEDia2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CEProCod`, `CEAno`, `CEMes`
- `CEDia3` (Duplicate): `CMEmpCod`, `CMFilCod`, `CEDiaDtaAux`
- `CEDia4` (Duplicate): `CEAno`, `CEMes`, `CEProCod`
- `CEDia5` (Duplicate): `CEAno`, `CEMes`, `CEDia`, `CEProCod`
- `CEDia6` (Duplicate): `CMEmpCod`, `CEProCod`, `CEAno`, `CEMes`

---

### 📌 CEEmb
- **Descrição:** Cadastro de Embalagens
- **Chave Primária:** `CMEmpCod`, `CEEmbCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEEmbCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CEEmbQtd` | `N/D` | - |
| `CEEmbCUsu` | `N/D` | - |
| `CEEmbCPrg` | `N/D` | - |
| `CEEmbCHor` | `N/D` | - |
| `CEEmbCDta` | `N/D` | - |
| `CEEmbDtaTrs` | `N/D` | - |
| `CEEmbVlrUnt` | `N/D` | - |
| `CEEmbVlrTot` | `N/D` | - |

#### 🗺️ Índices
- `CEEmb1` (Unique): `CMEmpCod`, `CEEmbCod`
- `CEEmb2` (Duplicate): `CMEmpCod`, `CEProCod`

---

### 📌 CEFas
- **Descrição:** Fases do Produto até Entrega Final
- **Chave Primária:** `CMEmpCod`, `CEFasCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEFasCod` | `N/D` | - |
| `CEFasDes` | `N/D` | - |
| `CEFasPrx` | `N/D` | - |
| `CEFasCor` | `N/D` | - |
| `CEFasTipMsg` | `N/D` | - |

#### 🗺️ Índices
- `CEFas1` (Unique): `CMEmpCod`, `CEFasCod`
- `CEFas2` (Duplicate): `CMEmpCod`

---

### 📌 CEFat
- **Descrição:** Tabela Fator Produtos
- **Chave Primária:** `CMEmpCod`, `CEFatCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEFatCod` | `N/D` | - |
| `CEFatDes` | `N/D` | - |
| `CEFatVlr` | `N/D` | - |
| `CEFatVlrPrz` | `N/D` | - |
| `CEFatVlr3` | `N/D` | - |
| `CEFatVlr4` | `N/D` | - |

#### 🗺️ Índices
- `CEFat1` (Unique): `CMEmpCod`, `CEFatCod`
- `CEFat2` (Duplicate): `CMEmpCod`

---

### 📌 CEFaU
- **Descrição:** Configura Usuários nas Fases da Entrega
- **Chave Primária:** `CMEmpCod`, `CEFaUNom`, `CEFasCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEFaUNom` | `N/D` | - |
| `CEFasCod` | `N/D` | - |
| `CEFaUPrg` | `N/D` | - |
| `CEFaUTST` | `N/D` | - |
| `CEFaUUsu` | `N/D` | - |
| `CEFauVol4Fas` | `N/D` | - |
| `CEFauVol3Fas` | `N/D` | - |
| `CEFauVol2Fas` | `N/D` | - |
| `CEFauVol1Fas` | `N/D` | - |
| `CEFauLct4Fas` | `N/D` | - |
| `CEFauLct3Fas` | `N/D` | - |
| `CEFauLct2Fas` | `N/D` | - |
| `CEFauLct1Fas` | `N/D` | - |
| `CEFauLctFasFin` | `N/D` | - |
| `CEFaUTodFil` | `N/D` | - |
| `CEFaUAntFas` | `N/D` | - |
| `CEFaUPrxFas` | `N/D` | - |
| `CEFaUVis` | `N/D` | - |
| `CEFasDes` | `N/D` | - |

#### 🗺️ Índices
- `ICEFaU` (Unique): `CMEmpCod`, `CEFaUNom`, `CEFasCod`
- `CEFaU2` (Duplicate): `CMEmpCod`, `CEFasCod`

---

### 📌 CEGR1
- **Descrição:** Grade de Produtos 01
- **Chave Primária:** `CMEmpCod`, `CEGr1Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEGr1Cod` | `N/D` | - |
| `CEGR1Des` | `N/D` | - |
| `CEGr1Qtd` | `N/D` | - |
| `CEGr1IteQtd` | `N/D` | - |

#### 🗺️ Índices
- `CEGR11` (Unique): `CMEmpCod`, `CEGr1Cod`
- `CEGR12` (Duplicate): `CMEmpCod`
- `CEGR13` (Duplicate): `CMEmpCod`, `CEGR1Des`

---

### 📌 CEGR2
- **Descrição:** Grade de Produtos
- **Chave Primária:** `CMEmpCod`, `CEGr1Cod`, `CEGr2Nro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEGr1Cod` | `N/D` | - |
| `CEGR1Des` | `N/D` | - |
| `CEGr1Qtd` | `N/D` | - |
| `CEGr1IteQtd` | `N/D` | - |
| `CEGr2Nro` | `N/D` | - |
| `CEGr2Qtd` | `N/D` | - |
| `CEGR2Pos` | `N/D` | - |
| `CEGR2Seq` | `N/D` | - |

#### 🗺️ Índices
- `CEGR21` (Unique): `CMEmpCod`, `CEGr1Cod`, `CEGr2Nro`
- `CEGR22` (Duplicate): `CMEmpCod`, `CEGr1Cod`
- `CRGR23` (Duplicate): `CMEmpCod`, `CEGr1Cod`, `CEGr2Qtd`
- `CRGR24` (Duplicate): `CMEmpCod`, `CEGR2Seq`
- `CEGR23` (Duplicate): `CMEmpCod`, `CEGr1Cod`, `CEGr2Qtd`
- `CEGR24` (Duplicate): `CMEmpCod`, `CEGR2Seq`

---

### 📌 CEGrp
- **Descrição:** Grupos de Produtos
- **Chave Primária:** `CMEmpCod`, `CEGrpCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEGrpCod` | `N/D` | - |
| `CMEmpConQtdPecPro` | `N/D` | - |
| `CMEmpUsaPerComFix` | `N/D` | - |
| `CEGrpDes` | `N/D` | - |
| `CEGrpCon` | `N/D` | - |
| `CEGrpCUsu` | `N/D` | - |
| `CEGrpCDta` | `N/D` | - |
| `CEGrpCHor` | `N/D` | - |
| `CEGrpCPrg` | `N/D` | - |
| `CEGrpFlaDel` | `N/D` | - |
| `CEGrpDtaTrs` | `N/D` | - |
| `CEGrpPrcCom` | `N/D` | - |
| `CEGrpPrcVen` | `N/D` | - |
| `CEGrpNroIni` | `N/D` | - |
| `CEGrpNroFin` | `N/D` | - |
| `CEGrpTip` | `N/D` | - |
| `CEGrpCom` | `N/D` | - |
| `CEGrpPrzMed` | `N/D` | - |
| `CMEmpPrzMedGrp` | `N/D` | - |
| `CEGrpNiv` | `N/D` | - |
| `CEGrpDesCom` | `N/D` | - |

#### 🗺️ Índices
- `CEGrp1` (Unique): `CMEmpCod`, `CEGrpCod`
- `ICEGrp` (Duplicate): `CMEmpCod`
- `CEGrp3` (Duplicate): `CMEmpCod`, `CEGrpDes`

---

### 📌 CEHPC
- **Descrição:** CRM Clientes x Produtos
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CEHPCTIP`, `CEHPCCLICOD`, `CEHPCPROCOD`, `CEHPCTST`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CEHPCTIP` | `N/D` | - |
| `CEHPCCLICOD` | `N/D` | - |
| `CEHPCPROCOD` | `N/D` | - |
| `CEHPCTST` | `N/D` | - |
| `CEHPCPRODES` | `N/D` | - |
| `CEHPCCLIDES` | `N/D` | - |
| `CEHPCSLDANT` | `N/D` | - |
| `CEHPCQTD` | `N/D` | - |
| `CEHPCSLDATU` | `N/D` | - |
| `CEHPCHIS` | `N/D` | - |
| `CEHPCFLAG` | `N/D` | - |
| `CEHPCTIPMOV` | `N/D` | - |
| `CEHPCNROSER` | `N/D` | - |
| `CEHPCPerIR` | `N/D` | - |

#### 🗺️ Índices
- `CEHPCA` (Unique): `CMEmpCod`, `CMFilCod`, `CEHPCTIP`, `CEHPCCLICOD`, `CEHPCPROCOD`, `CEHPCTST`
- `CEHPCB` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CEHPCC` (Duplicate): `CEHPCTST`
- `CEHPCD` (Duplicate): `CMEmpCod`, `CMFilCod`, `CEHPCCLICOD`, `CEHPCPROCOD`, `CEHPCTST`

---

### 📌 CEImp
- **Descrição:** Impressoras
- **Chave Primária:** `CMEmpCod`, `CEImpCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEImpCod` | `N/D` | - |
| `CEImpDes` | `N/D` | - |
| `CEImpTip` | `N/D` | - |

#### 🗺️ Índices
- `CEImp1` (Unique): `CMEmpCod`, `CEImpCod`
- `CEImp2` (Duplicate): `CMEmpCod`

---

### 📌 CEInv
- **Descrição:** Diferenças do Estoque
- **Chave Primária:** `CMEmpCod`, `CEInvProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEInvProCod` | `N/D` | - |
| `CEInvQtdEnt` | `N/D` | - |
| `CEInvProDes` | `N/D` | - |
| `CEInvQtdSai` | `N/D` | - |
| `CEInvDif` | `N/D` | - |

#### 🗺️ Índices
- `CEInvA` (Unique): `CMEmpCod`, `CEInvProCod`
- `CEInvB` (Duplicate): `CMEmpCod`

---

### 📌 CEKT1
- **Descrição:** Kit de Produtos 1 Nivel
- **Chave Primária:** `CMEmpCod`, `CEKT1CodOrg`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEKT1CodOrg` | `N/D` | - |
| `CEKT1DesOrg` | `N/D` | - |
| `CEKT1TotCus` | `N/D` | - |
| `CEKT1TotVda` | `N/D` | - |
| `CEKT1Eli` | `N/D` | - |
| `CEKT1PreTabOrg` | `N/D` | - |
| `CEKT1CusOrg` | `N/D` | - |
| `CEKT1TotPrcCP` | `N/D` | - |
| `CEKT1TabPre` | `N/D` | - |
| `CEKT1AtuPreTab` | `N/D` | - |
| `CEKT1PrcCus` | `N/D` | - |
| `CEKT1Qtd` | `N/D` | - |

#### 🗺️ Índices
- `CEKT1A` (Unique): `CMEmpCod`, `CEKT1CodOrg`
- `CEKT1B` (Duplicate): `CMEmpCod`

---

### 📌 CEKT2
- **Descrição:** Kit de Produtos 2  Nivel
- **Chave Primária:** `CMEmpCod`, `CEKT1CodOrg`, `CEKT2CodPro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEKT1CodOrg` | `N/D` | - |
| `CEKT1DesOrg` | `N/D` | - |
| `CEKT1TotCus` | `N/D` | - |
| `CEKT1TotVda` | `N/D` | - |
| `CEKT1Eli` | `N/D` | - |
| `CEKT1PreTabOrg` | `N/D` | - |
| `CEKT1CusOrg` | `N/D` | - |
| `CEKT1TotPrcCP` | `N/D` | - |
| `CEKT1TabPre` | `N/D` | - |
| `CEKT1AtuPreTab` | `N/D` | - |
| `CEKT1PrcCus` | `N/D` | - |
| `CEKT1Qtd` | `N/D` | - |
| `CEKT2CodPro` | `N/D` | - |
| `CEKT2Qtd` | `N/D` | - |
| `CEKT2PreCus` | `N/D` | - |
| `CEKT2PreVda` | `N/D` | - |
| `CEKT2Pre_VdaKit` | `N/D` | - |
| `CEKT2Des` | `N/D` | - |
| `CEKT2DesCom` | `N/D` | - |
| `CEKT2TotCus` | `N/D` | - |
| `CEKT2TotVda` | `N/D` | - |
| `CEKT2PrcCP` | `N/D` | - |
| `CEKt2PQA` | `N/D` | - |
| `CEKT2PrcCus` | `N/D` | - |
| `CEKT2QTDOrg` | `N/D` | - |
| `CEKT2Calc` | `N/D` | - |

#### 🗺️ Índices
- `CEKT2A` (Unique): `CMEmpCod`, `CEKT1CodOrg`, `CEKT2CodPro`
- `CEKT2B` (Duplicate): `CMEmpCod`, `CEKT1CodOrg`

---

### 📌 CELab
- **Descrição:** Laboratórios ( Farmacia )
- **Chave Primária:** `CMEmpCod`, `CEProNomLabFar`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProNomLabFar` | `N/D` | - |
| `CELabPerDes` | `N/D` | - |
| `CELabCUsu` | `N/D` | - |
| `CELabCPrg` | `N/D` | - |
| `CELabCHor` | `N/D` | - |
| `CELabCDta` | `N/D` | - |
| `CELabDtaTrs` | `N/D` | - |
| `CELabFlaDel` | `N/D` | - |

#### 🗺️ Índices
- `CELab1` (Unique): `CMEmpCod`, `CEProNomLabFar`
- `CELab2` (Duplicate): `CMEmpCod`

---

### 📌 CEMes
- **Descrição:** Acumulo Estoque Mensal
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CEProCod`, `CEAno`, `CEMes`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEAno` | `N/D` | - |
| `CEAnoQtdEnt` | `N/D` | - |
| `CEAnoQtdSai` | `N/D` | - |
| `CEAnoQtdVda` | `N/D` | - |
| `CEAnoQtdCom` | `N/D` | - |
| `CEAnoQtd_SaiTrs` | `N/D` | - |
| `CEAnoQtd_EntTrs` | `N/D` | - |
| `CEAnoIND` | `N/D` | - |
| `CEAnoFlaDel` | `N/D` | - |
| `CEAnoDtaTrs` | `N/D` | - |
| `CEAnoVlrLuc` | `N/D` | - |
| `CEAnoVlrCus` | `N/D` | - |
| `CEAnoVlrVda` | `N/D` | - |
| `CEAnoQtdOutEnt` | `N/D` | - |
| `CEAnoQtd_OutSai` | `N/D` | - |
| `CEAnoMrg` | `N/D` | - |
| `CEAnoQtdEVC` | `N/D` | - |
| `CEAnoQtdSCC` | `N/D` | - |
| `CEAnoQtdSTM` | `N/D` | - |
| `CEAnoQtdETM` | `N/D` | - |
| `CEAnoTotEnt` | `N/D` | - |
| `CEAnoTotSai` | `N/D` | - |
| `CEMes` | `N/D` | - |
| `CEMesQtdEnt` | `N/D` | - |
| `CEMesQtdSai` | `N/D` | - |
| `CEMesQtdVda` | `N/D` | - |
| `CEMesQtdOutEnt` | `N/D` | - |
| `CEMesQtd_OutSai` | `N/D` | - |
| `CEMesQtdCom` | `N/D` | - |
| `CEMesQtd_SaiTrs` | `N/D` | - |
| `CEMesQtd_EntTrs` | `N/D` | - |
| `CEMesFlaDel` | `N/D` | - |
| `CEMesDtaTrs` | `N/D` | - |
| `CEMesIND` | `N/D` | - |
| `CEMesVlrLuc` | `N/D` | - |
| `CEMesVlrVda` | `N/D` | - |
| `CEMesVlrCus` | `N/D` | - |
| `CEMesEstIni` | `N/D` | - |
| `CEMesEstFin` | `N/D` | - |
| `CEMesAju` | `N/D` | - |
| `CEMesDtaIni` | `N/D` | - |
| `CEMesDtaFin` | `N/D` | - |
| `CEMesDtaHorPro` | `N/D` | - |
| `CEMesEstVda` | `N/D` | - |
| `CEMesEstCom` | `N/D` | - |
| `CEMesMrg` | `N/D` | - |
| `CEMesQtdEVC` | `N/D` | - |
| `CEMesQtdSCC` | `N/D` | - |
| `CEMesQtdSTM` | `N/D` | - |
| `CEMesQtdETM` | `N/D` | - |
| `CEMesQtdAtu` | `N/D` | - |
| `CEMesTotEnt` | `N/D` | - |
| `CEMesTotSai` | `N/D` | - |
| `CEMesDiaPro` | `N/D` | - |

#### 🗺️ Índices
- `CEMes1` (Unique): `CMEmpCod`, `CMFilCod`, `CEProCod`, `CEAno`, `CEMes`
- `CEMes2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CEProCod`, `CEAno`
- `CEMes3` (Duplicate): `CMEmpCod`, `CMFilCod`, `CEAno`, `CEMes`, `CEMesIND`
- `CEMes4` (Duplicate): `CMEmpCod`, `CEProCod`, `CEAno`, `CEMes`
- `CEMes5` (Duplicate): `CMEmpCod`, `CEAno`, `CEMes`
- `CEMes6` (Duplicate): `CMEmpCod`, `CEAno`, `CEProCod`, `CEMes`

---

### 📌 CEMst
- **Descrição:** Produtos da Master Informática
- **Chave Primária:** `CEMstProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CEMstProCod` | `N/D` | - |
| `CEMstProDes` | `N/D` | - |
| `CEMstProCus` | `N/D` | - |

#### 🗺️ Índices
- `CEMst1` (Unique): `CEMstProCod`
- `CEMst2` (Duplicate): `CEMstProDes`

---

### 📌 CENBM
- **Descrição:** Nomenclatura Brasileira de Medicamentos
- **Chave Primária:** `CENBMSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CENBMSeq` | `N/D` | - |
| `CENBMNBM` | `N/D` | - |
| `CENBMPri1` | `N/D` | - |
| `CENBMPri` | `N/D` | - |

#### 🗺️ Índices
- `CENBM1` (Unique): `CENBMSeq`
- `CENBM2` (Duplicate): `CENBMPri1`
- `CENBM3` (Duplicate): `CENBMSeq`, `CENBMNBM`

---

### 📌 CENCG
- **Descrição:** NCM Geral
- **Chave Primária:** `CENCGCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CENCGCod` | `N/D` | - |
| `CENCGDes` | `N/D` | - |

#### 🗺️ Índices
- `CENCG1` (Unique): `CENCGCod`

---

### 📌 CENCM
- **Descrição:** Nomenclatura Comum Mercosul
- **Chave Primária:** `CENCMCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CENCMCod` | `N/D` | - |
| `CENCMDes` | `N/D` | - |
| `CENCMCCes` | `N/D` | - |

#### 🗺️ Índices
- `CENCM1` (Unique): `CENCMCod`

---

### 📌 CENCU
- **Descrição:** NCM Geral por UF
- **Chave Primária:** `CENCGCod`, `CENCUUF`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CENCGCod` | `N/D` | - |
| `CENCGDes` | `N/D` | - |
| `CENCUUF` | `N/D` | - |
| `CENCUMsg` | `N/D` | - |

#### 🗺️ Índices
- `CENCU1` (Unique): `CENCGCod`, `CENCUUF`
- `CENCU2` (Duplicate): `CENCGCod`

---

### 📌 CENFC
- **Descrição:** Cabeçalho da Nota Fiscal
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CENFCSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CENFCSeq` | `N/D` | - |
| `CMFilNopCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRCliCalcIR` | `N/D` | - |
| `CMFilModImpFis` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CENFCSer` | `N/D` | - |
| `CENFCSSe` | `N/D` | - |
| `CRCliRazSoc` | `N/D` | - |
| `CENFCRazSoc` | `N/D` | - |
| `CENFCPrcICM` | `N/D` | - |
| `CRCliCGC1` | `N/D` | - |
| `CRCliRG` | `N/D` | - |
| `CRCliCPF` | `N/D` | - |
| `CRCliIE1` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `CPCliBai` | `N/D` | - |
| `CPCliCep` | `N/D` | - |
| `CPCliCgc` | `N/D` | - |
| `CPCliCid` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CPCliEnd` | `N/D` | - |
| `CPCliIE` | `N/D` | - |
| `CPCliTel1` | `N/D` | - |
| `CPCliUf` | `N/D` | - |
| `CENFCEmail` | `N/D` | - |
| `CENFCNroNFi` | `N/D` | - |
| `CENFCDTAEMI` | `N/D` | - |
| `CENFCDTASAIENT` | `N/D` | - |
| `CENFCBCISub` | `N/D` | - |
| `CENFCVlrISB` | `N/D` | - |
| `CENFCNopCodAux` | `N/D` | - |
| `CENFCVlrPro` | `N/D` | - |
| `CENFCVlrFrt` | `N/D` | - |
| `CENFCVlrSeg` | `N/D` | - |
| `CENFCVlDsp` | `N/D` | - |
| `CENFCVlrIPI` | `N/D` | - |
| `CENFCVlrOrg` | `N/D` | - |
| `CMTraCod` | `N/D` | - |
| `CMTraIBGE` | `N/D` | - |
| `CENFCIntCod` | `N/D` | - |
| `CENFCOBS1` | `N/D` | - |
| `CENFCObs2` | `N/D` | - |
| `CENFCObs3` | `N/D` | - |
| `CENFCObs4` | `N/D` | - |
| `CENFCPlcVei` | `N/D` | - |
| `CENFCUFVei` | `N/D` | - |
| `CENFCEsp` | `N/D` | - |
| `CENFCPesBrt` | `N/D` | - |
| `CENFCPesLiq` | `N/D` | - |
| `CENFCQtd` | `N/D` | - |
| `CENFCCRFilCod` | `N/D` | - |
| `CENFCCRMovSEq` | `N/D` | - |
| `CENFC_CRMovDta` | `N/D` | - |
| `CENFCVen` | `N/D` | - |
| `CENFCNroPed` | `N/D` | - |
| `CENFCQtdIte` | `N/D` | - |
| `CENFCSts` | `N/D` | - |
| `CMTraCGC` | `N/D` | - |
| `CMTraCid` | `N/D` | - |
| `CMTraEnd` | `N/D` | - |
| `CMTraIEs` | `N/D` | - |
| `CMTraUF` | `N/D` | - |
| `CMTraPlcVei` | `N/D` | - |
| `CMTraUFVei` | `N/D` | - |
| `CMTraMotNom` | `N/D` | - |
| `CMNOpCod` | `N/A(4)` | CMNopCod |
| `CENFCVlrDsc` | `N/D` | - |
| `CENFCVlrAcr` | `N/D` | - |
| `CENFCVlrLiqPro` | `N/D` | - |
| `CMCEPCod` | `N/D` | - |
| `CMCEPDes` | `N/D` | - |
| `CMUFCod` | `N/D` | - |
| `CMTraRazSoc` | `N/D` | - |
| `CRCliBai` | `N/D` | - |
| `CRCliEnd` | `N/D` | - |
| `CENFCUsu` | `N/D` | - |
| `CENFCTipFre` | `N/D` | - |
| `CENFCTME` | `N/D` | - |
| `CENFCOrg` | `N/D` | - |
| `CENFCCNPJ` | `N/D` | - |
| `CENFCIE` | `N/D` | - |
| `CENFCBID` | `N/D` | - |
| `CENFCVID` | `N/D` | - |
| `CENFCISSVlr` | `N/D` | - |
| `CENFCVLRIRRF` | `N/D` | - |
| `CENFCVLRSS` | `N/D` | - |
| `CENFCVlr1Ser` | `N/D` | - |
| `CENFCVlr1Pro` | `N/D` | - |
| `CMFilPerISS` | `N/D` | - |
| `CMFilPerSecSoc` | `N/D` | - |
| `CMFilPerIRRF` | `N/D` | - |
| `CENFCDesIRRF` | `N/D` | - |
| `CENFCLocSer` | `N/D` | - |
| `CENFCLocCob` | `N/D` | - |
| `CENFCConf` | `N/D` | - |
| `CENFCPis` | `N/D` | - |
| `CENFCTxaSis` | `N/D` | - |
| `CENFCArm` | `N/D` | - |
| `CENFCTPe` | `N/D` | - |
| `CENFCD_IM` | `N/D` | - |
| `CENFCD_END` | `N/D` | - |
| `CENFCDEndCom` | `N/D` | - |
| `CENFCD_CEP` | `N/D` | - |
| `CENFCD_IBGE` | `N/D` | - |
| `CENFCD_UF` | `N/D` | - |
| `CENFCD_BAI` | `N/D` | - |
| `CENFCD_PAI` | `N/D` | - |
| `CENFCD_CID` | `N/D` | - |
| `CENFCD_TEL` | `N/D` | - |
| `CENFCD_NRO` | `N/D` | - |
| `CENFCD_CEN` | `N/D` | - |
| `CENFCTSTSAI` | `N/D` | - |
| `CENFCDESCNPJ` | `N/D` | - |
| `CENFCMar` | `N/D` | - |
| `CENFC_Nro` | `N/D` | - |
| `CENFCLINDA` | `N/D` | - |
| `CENFCO_UF` | `N/D` | - |
| `CENFCICMORG` | `N/D` | - |
| `CENFCICMDST` | `N/D` | - |
| `CENFCDtaCan` | `N/D` | - |
| `CENFCMotCan` | `N/D` | - |
| `CENFCFRe` | `N/D` | - |
| `CENFCTSTIdx` | `N/D` | - |
| `CENFCProST` | `N/D` | - |
| `CENFCVlIse` | `N/D` | - |
| `CENFCVlICM` | `N/D` | - |
| `CENFCAliIcms` | `N/D` | - |
| `CENfcModNot` | `N/D` | - |
| `CENFCCSLL` | `N/D` | - |
| `CENFCChvNFE` | `N/D` | - |
| `CENFCChvRefNFE` | `N/D` | - |
| `CENFCProNFE` | `N/D` | - |
| `CENFCProCanNFE` | `N/D` | - |
| `CENFCLotNFE` | `N/D` | - |
| `CENFCProInuNFE` | `N/D` | - |
| `CENFCDtaInuNFE` | `N/D` | - |
| `CENFCRecNFE` | `N/D` | - |
| `CENFCNFE` | `N/D` | - |
| `CENFCTOPICMS` | `N/D` | - |
| `CENFCTOPTip` | `N/D` | - |
| `CENFCTOPST` | `N/D` | - |
| `CENFCTOPRedBC` | `N/D` | - |
| `CMTOPCod` | `N/D` | - |
| `CMTOPDes` | `N/D` | - |
| `CMTOPE_S` | `N/D` | - |
| `CENFCTOPCod` | `N/D` | - |
| `CENFCBCPis` | `N/D` | - |
| `CENFCVTPis` | `N/D` | - |
| `CENFCVTCof` | `N/D` | - |
| `CENFCBCCof` | `N/D` | - |
| `CENFCIPIBas` | `N/D` | - |
| `CENFCInfDscIte` | `N/D` | - |
| `CENFCtipAmb` | `N/D` | - |
| `CENFCRedAcrNot` | `N/D` | - |
| `CENFCTOPSomFre` | `N/D` | - |
| `CENFCVlrDis` | `N/D` | - |
| `CENFCVrApr` | `N/D` | - |
| `CENFCPeApr` | `N/D` | - |
| `CENFCSit` | `N/D` | - |
| `CENFCULEVE` | `N/D` | - |
| `CENFCHorCan` | `N/D` | - |
| `CENFCTOPSIPI` | `N/D` | - |
| `CENFCPerINSS` | `N/D` | - |
| `CENFCVlrINSS` | `N/D` | - |
| `CENFCImpNF` | `N/D` | - |
| `CENFCPerST` | `N/D` | - |
| `CMTOPFinNF` | `N/D` | - |
| `CENFCDeson` | `N/D` | - |
| `CENFCIndIE` | `N/D` | - |
| `CENFCIntMed` | `N/D` | - |
| `CENFCVrFCP` | `N/D` | - |
| `CENFCVrIDes` | `N/D` | - |
| `CENFCVrIRem` | `N/D` | - |
| `CENFCObs87` | `N/D` | - |
| `CENFCMotNom` | `N/D` | - |
| `CENFCObs5` | `N/D` | - |
| `CENFCObs6` | `N/D` | - |
| `CENFCVlrImp` | `N/D` | - |
| `CENFCPerImp` | `N/D` | - |
| `CENFCIndPres` | `N/D` | - |
| `CENFCIdx` | `N/D` | - |
| `CENFCVrSTFCP` | `N/D` | - |
| `CENFCVrRetFCP` | `N/D` | - |
| `CENFCTroco` | `N/D` | - |
| `CENFCVFCP` | `N/D` | - |
| `CENFCIPIDev` | `N/D` | - |
| `CENFCTotEst` | `N/D` | - |
| `CMTopIntEst` | `N/D` | - |
| `CENFCcPais` | `N/D` | - |
| `CENFCnPais` | `N/D` | - |
| `CENFUFsPais` | `N/D` | - |
| `CENFLcsPais` | `N/D` | - |
| `CMTOPICMS` | `N/D` | - |
| `CMTOPST` | `N/D` | - |
| `CMTOPFrt` | `N/D` | - |
| `CMTOPDsc` | `N/D` | - |
| `CMTOPIPI` | `N/D` | - |
| `CMTOPISS` | `N/D` | - |
| `CMTOPDsp` | `N/D` | - |
| `CENFCTotTrib` | `N/D` | - |
| `CENFCIRPis` | `N/D` | - |
| `CENFCIRCof` | `N/D` | - |
| `CENFCIRCSLL` | `N/D` | - |
| `CENFCIRBCIRRF` | `N/D` | - |
| `CENFCIRpIRRF` | `N/D` | - |
| `CENFCIRIRRF` | `N/D` | - |
| `CENFCIRBCPrev` | `N/D` | - |
| `CENFCIRPrev` | `N/D` | - |
| `CENFCIRpPrev` | `N/D` | - |
| `CENFCFlag` | `N/D` | - |
| `CENFCBcoCod` | `N/D` | - |
| `CENFCDtaPgt` | `N/D` | - |
| `CENFCBCIBSCBS` | `N/D` | - |
| `CENFCUFVlrIBS` | `N/D` | - |
| `CENFCMunVlrIBS` | `N/D` | - |
| `CENFCVlrIBS` | `N/D` | - |
| `CENFCVlrCBS` | `N/D` | - |
| `CENFCBCMon` | `N/D` | - |
| `CENFCVlrMon` | `N/D` | - |
| `CENFCHod` | `N/D` | - |
| `CENFCPrcDsc` | `N/D` | - |
| `CMEmpDec` | `N/D` | - |
| `CMFilArrTru` | `N/D` | - |
| `CENFCPrcAcr` | `N/D` | - |
| `CMFilModTelIni` | `N/D` | - |
| `CENFCIte` | `N/D` | - |
| `CENFCTOPDes` | `N/D` | - |
| `CMTopVdaSim` | `N/D` | - |
| `CMTOPVda` | `N/D` | - |
| `CMTOPUSU` | `N/D` | - |
| `CMTOPTST` | `N/D` | - |
| `CMTopTip` | `N/D` | - |
| `CMTOPRedBC` | `N/D` | - |
| `CMTOPPRG` | `N/D` | - |
| `CMTOPPISCOF` | `N/D` | - |
| `CMTOPCSTSER` | `N/D` | - |
| `CMTopCalImpAut` | `N/D` | - |
| `CMTOPEstNeg` | `N/D` | - |
| `CENFCTotImp` | `N/D` | - |
| `CMTOPCmpICMS` | `N/D` | - |
| `CMTOPArrST` | `N/D` | - |
| `CENFCTot_QtdAux` | `N/D` | - |
| `CENFCTotQtd` | `N/D` | - |

#### 🗺️ Índices
- `CENFCA` (Unique): `CMEmpCod`, `CMFilCod`, `CENFCSeq`
- `CENFCF` (Duplicate): `CMNOpCod`
- `CENFCB` (Duplicate): `CMTraCod`
- `CENFC4` (Duplicate): `CMEmpCod`, `CPCliCod`
- `CENFC3` (Duplicate): `CMEmpCod`, `CRCliCod`
- `CENFC5` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CENFCM` (Duplicate): `CMTOPCod`
- `CENFCE` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CMNOpCod`
- `CENFCG` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFCDTAEMI`
- `CENFCH` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFC_CRMovDta`, `CENFCCRMovSEq`, `CENFC_Nro`
- `CENFCI` (Duplicate): `CENFCDtaCan`
- `CENFCJ` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFCNroNFi`
- `CENFCK` (Duplicate): `CENFCTSTIdx`
- `CENFCL` (Duplicate): `CENFCIdx`

---

### 📌 CENFD
- **Descrição:** Duplicatas da Nota Fiscal
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFDCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CENFCSeq` | `N/D` | - |
| `CENFCSts` | `N/D` | - |
| `CENFCVlrOrg` | `N/D` | - |
| `CENFDCod` | `N/D` | - |
| `CENFDDtaVct` | `N/D` | - |
| `CENFDVlr` | `N/D` | - |
| `CENFDNroDupAux` | `N/D` | - |

#### 🗺️ Índices
- `CENFDA` (Unique): `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFDCod`
- `CENFDB` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFCSeq`

---

### 📌 CENFE
- **Descrição:** Distribuição / Manifesto DFe - Eventos
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CENFNNSU`, `CENFNTipEve`, `CENFNSeqEve`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CENFNNSU` | `N/D` | - |
| `CENFNTipo` | `N/D` | - |
| `CENFNChNFe` | `N/D` | - |
| `CENFNTpEve` | `N/D` | - |
| `CENFNDsEve` | `N/D` | - |
| `CENFNDhResp` | `N/D` | - |
| `CENFNSitMan` | `N/D` | - |
| `CENFNVrNF` | `N/D` | - |
| `CENFNNome` | `N/D` | - |
| `CENFNCPFCNPJ` | `N/D` | - |
| `CENFNIE` | `N/D` | - |
| `CENFNDhEmi` | `N/D` | - |
| `CENFNTpNF` | `N/D` | - |
| `CENFNSitNF` | `N/D` | - |
| `CENFNProt` | `N/D` | - |
| `CENFNDtEmi` | `N/D` | - |
| `CENFNNumNF` | `N/D` | - |
| `CENFNDwnNF` | `N/D` | - |
| `CENFNTipEve` | `N/D` | - |
| `CENFNSeqEve` | `N/D` | - |
| `CENFNDhEve` | `N/D` | - |
| `CENFNJust` | `N/D` | - |
| `CENFNStat` | `N/D` | - |
| `CENFNMotivo` | `N/D` | - |
| `CENFNDhReg` | `N/D` | - |

#### 🗺️ Índices
- `CENFE1` (Unique): `CMEmpCod`, `CMFilCod`, `CENFNNSU`, `CENFNTipEve`, `CENFNSeqEve`
- `CENFE2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFNNSU`

---

### 📌 CENFK
- **Descrição:** Nota Fiscal - Formas de Pagamento
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFKDet`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CENFCSeq` | `N/D` | - |
| `CENFCSts` | `N/D` | - |
| `CENFKDet` | `N/D` | - |
| `CENFKInd` | `N/D` | - |
| `CENFKtPag` | `N/D` | - |
| `CENFKvPag` | `N/D` | - |
| `CENFKItCard` | `N/D` | - |
| `CENFKCnpjCard` | `N/D` | - |
| `CENFKBandCard` | `N/D` | - |
| `CENFKAutCard` | `N/D` | - |

#### 🗺️ Índices
- `CENFK1` (Unique): `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFKDet`
- `CENFK2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFCSeq`

---

### 📌 CENFM
- **Descrição:** Mensagens da Nota Fiscal / NFe
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFMSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CENFCSeq` | `N/D` | - |
| `CENFCSts` | `N/D` | - |
| `CENFMSeq` | `N/D` | - |
| `CENFMMsg` | `N/D` | - |
| `CENFMUSU` | `N/D` | - |
| `CENFMTST` | `N/D` | - |
| `CENFMPRG` | `N/D` | - |
| `CENFMOrd` | `N/D` | - |

#### 🗺️ Índices
- `CENFM1` (Unique): `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFMSeq`
- `CENFM2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFCSeq`
- `CENFM3` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFMOrd`

---

### 📌 CENFN
- **Descrição:** Distribuição / Manifesto DFe
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CENFNNSU`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CENFNNSU` | `N/D` | - |
| `CENFNTipo` | `N/D` | - |
| `CENFNChNFe` | `N/D` | - |
| `CENFNTpEve` | `N/D` | - |
| `CENFNDsEve` | `N/D` | - |
| `CENFNDhResp` | `N/D` | - |
| `CENFNSitMan` | `N/D` | - |
| `CENFNVrNF` | `N/D` | - |
| `CENFNNome` | `N/D` | - |
| `CENFNCPFCNPJ` | `N/D` | - |
| `CENFNIE` | `N/D` | - |
| `CENFNDhEmi` | `N/D` | - |
| `CENFNTpNF` | `N/D` | - |
| `CENFNSitNF` | `N/D` | - |
| `CENFNProt` | `N/D` | - |
| `CENFNDtEmi` | `N/D` | - |
| `CENFNNumNF` | `N/D` | - |
| `CENFNDwnNF` | `N/D` | - |

#### 🗺️ Índices
- `CENFN1` (Unique): `CMEmpCod`, `CMFilCod`, `CENFNNSU`
- `CENFN2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CENFO1
- **Descrição:** Carta Correção da Nota Fiscal
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFO1TST`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CENFCSeq` | `N/D` | - |
| `CENFO1TST` | `N/D` | - |
| `CENFO1Obs` | `N/D` | - |
| `CENFCTSTIdx` | `N/D` | - |
| `CENFO1Usu` | `N/D` | - |
| `CENFCNroNFi` | `N/D` | - |
| `CENFCSSe` | `N/D` | - |
| `CENFCSer` | `N/D` | - |
| `CENFCSts` | `N/D` | - |
| `CENFCRazSoc` | `N/D` | - |
| `CENFCDTAEMI` | `N/D` | - |
| `CENFO1Prg` | `N/D` | - |
| `CENFCUSeq` | `N/D` | - |

#### 🗺️ Índices
- `CENFO11` (Unique): `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFO1TST`
- `CENFO12` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFCSeq`

---

### 📌 CENFO2
- **Descrição:** Carta Correção da Nota Fiscal
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFO1TST`, `CENFO2COD`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CENFCSeq` | `N/D` | - |
| `CENFO1TST` | `N/D` | - |
| `CENFO1Obs` | `N/D` | - |
| `CENFCTSTIdx` | `N/D` | - |
| `CENFO1Usu` | `N/D` | - |
| `CENFCNroNFi` | `N/D` | - |
| `CENFCSSe` | `N/D` | - |
| `CENFCSer` | `N/D` | - |
| `CENFCSts` | `N/D` | - |
| `CENFCRazSoc` | `N/D` | - |
| `CENFCDTAEMI` | `N/D` | - |
| `CENFO1Prg` | `N/D` | - |
| `CENFCUSeq` | `N/D` | - |
| `CENFO2COD` | `N/D` | - |
| `CENFO2ObsRed` | `N/D` | - |
| `CENFO2Obs` | `N/D` | - |
| `CENFO2SeqCCe` | `N/D` | - |
| `CENFO2RetCCe` | `N/D` | - |
| `CENFCSeqCCe` | `N/D` | - |
| `CENFCUStCCe` | `N/D` | - |
| `CENFCDhCCe` | `N/D` | - |
| `CENFO2ArqRet` | `N/D` | - |

#### 🗺️ Índices
- `CENFO21` (Unique): `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFO1TST`, `CENFO2COD`
- `CENFO22` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFO1TST`

---

### 📌 CENFP
- **Descrição:** Produtos da Nota Fiscal
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CEProCod`, `CENFPIte`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CENFCSeq` | `N/D` | - |
| `CENFCPrcDsc` | `N/D` | - |
| `CMEmpDec` | `N/D` | - |
| `CMFilArrTru` | `N/D` | - |
| `CENFCPrcAcr` | `N/D` | - |
| `CMFilModImpFis` | `N/D` | - |
| `CMFilModTelIni` | `N/D` | - |
| `CENFCIte` | `N/D` | - |
| `CENFCVlrPro` | `N/D` | - |
| `CENFCVID` | `N/D` | - |
| `CENFCBID` | `N/D` | - |
| `CENFCVlr1Ser` | `N/D` | - |
| `CENFCISSVlr` | `N/D` | - |
| `CENFCTOPCod` | `N/D` | - |
| `CENFCTOPDes` | `N/D` | - |
| `CENFCInfDscIte` | `N/D` | - |
| `CMTOPCod` | `N/D` | - |
| `CMTOPDes` | `N/D` | - |
| `CMTopVdaSim` | `N/D` | - |
| `CMTOPDsc` | `N/D` | - |
| `CMTOPVda` | `N/D` | - |
| `CMTOPUSU` | `N/D` | - |
| `CMTOPTST` | `N/D` | - |
| `CMTopTip` | `N/D` | - |
| `CMTOPST` | `N/D` | - |
| `CMTOPRedBC` | `N/D` | - |
| `CMTOPPRG` | `N/D` | - |
| `CMTOPPISCOF` | `N/D` | - |
| `CMTOPISS` | `N/D` | - |
| `CMTOPIPI` | `N/D` | - |
| `CMTopIntEst` | `N/D` | - |
| `CMTOPICMS` | `N/D` | - |
| `CMTOPFrt` | `N/D` | - |
| `CMTOPE_S` | `N/D` | - |
| `CMTOPDsp` | `N/D` | - |
| `CMTOPCSTSER` | `N/D` | - |
| `CMTopCalImpAut` | `N/D` | - |
| `CMTOPEstNeg` | `N/D` | - |
| `CENFCTotImp` | `N/D` | - |
| `CENFCPerImp` | `N/D` | - |
| `CENFCVlrImp` | `N/D` | - |
| `CENFCTotEst` | `N/D` | - |
| `CMTOPCmpICMS` | `N/D` | - |
| `CENFCSts` | `N/D` | - |
| `CMTOPArrST` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CENFPIte` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CEProDesCom` | `N/D` | - |
| `CEProCST` | `N/D` | - |
| `CEProNCM` | `N/D` | - |
| `CEProOrg` | `N/D` | - |
| `CEProSitTri` | `N/D` | - |
| `CEProPerAliIcm` | `N/D` | - |
| `CEProPre1Tab` | `N/D` | - |
| `CENFPQtd` | `N/D` | - |
| `CENFPPQA` | `N/D` | - |
| `CENFPVlrUnt` | `N/D` | - |
| `CENFPVlrTot` | `N/D` | - |
| `CENFPPrcIcm` | `N/D` | - |
| `CENFPSitTri` | `N/D` | - |
| `CENFPUnd` | `N/D` | - |
| `CENFPTraPro` | `N/D` | - |
| `CENFPVlrICM` | `N/D` | - |
| `CENFPBasICM` | `N/D` | - |
| `CENFPVUD` | `N/D` | - |
| `CENFPVTD` | `N/D` | - |
| `CENFPProDes` | `N/D` | - |
| `CENFPPro_DesAux` | `N/D` | - |
| `CENFPLot` | `N/D` | - |
| `CENFPPrcIPI` | `N/D` | - |
| `CENFPVlrIPI` | `N/D` | - |
| `CENFPIPII` | `N/D` | - |
| `CENFPIPIO` | `N/D` | - |
| `CEProUnd` | `N/D` | - |
| `CENFPQtdAux` | `N/D` | - |
| `CENFPSer` | `N/D` | - |
| `CENFPISSVlr` | `N/D` | - |
| `CENFPISSAlq` | `N/D` | - |
| `CENFPPRBC` | `N/D` | - |
| `CENFPIRRFV` | `N/D` | - |
| `CENFPIRRFP` | `N/D` | - |
| `CENFPBICMSSub` | `N/D` | - |
| `CENFPVICMSSub` | `N/D` | - |
| `CENFPAICMSSub` | `N/D` | - |
| `CENFPOutIcms` | `N/D` | - |
| `CENFPIseIcms` | `N/D` | - |
| `CENFPIPIBas` | `N/D` | - |
| `CENFPVlrDes` | `N/D` | - |
| `CENFPCFOP` | `N/D` | - |
| `CENFPDCFOP` | `N/D` | - |
| `CENFPDP1` | `N/D` | - |
| `CENFPDP2` | `N/D` | - |
| `CENFPDP3` | `N/D` | - |
| `CENFPDP4` | `N/D` | - |
| `CENFPDP5` | `N/D` | - |
| `CENFPAlqPis` | `N/D` | - |
| `CENFPVTPis` | `N/D` | - |
| `CENFPCstPis` | `N/D` | - |
| `CENFPBCPis` | `N/D` | - |
| `CENFPBCCof` | `N/D` | - |
| `CENFPAlqCof` | `N/D` | - |
| `CENFPVTCof` | `N/D` | - |
| `CENFPCSTCof` | `N/D` | - |
| `CENFPIDEPCN` | `N/D` | - |
| `CENFPVlDsp` | `N/D` | - |
| `CENFPCSOSN` | `N/D` | - |
| `CENFPVlrFrt` | `N/D` | - |
| `CENFPVlrSeg` | `N/D` | - |
| `CENFPDec` | `N/D` | - |
| `CENFPPVU` | `N/D` | - |
| `CENFPTabPre` | `N/D` | - |
| `CENFPPrePro` | `N/D` | - |
| `CENFPVICMDisp` | `N/D` | - |
| `CENFPBsApr` | `N/D` | - |
| `CENFPPeApr` | `N/D` | - |
| `CENFPVlApr` | `N/D` | - |
| `CENFPPeIVA` | `N/D` | - |
| `CENFPNCM` | `N/D` | - |
| `CENFPPerImp` | `N/D` | - |
| `CENFPPerIEst` | `N/D` | - |
| `CENFPVlrImp` | `N/D` | - |
| `CENFPObsFis` | `N/D` | - |
| `CENFPObsF1` | `N/D` | - |
| `CENFPObsF2` | `N/D` | - |
| `CENFPObsF3` | `N/D` | - |
| `CENFPObsF4` | `N/D` | - |
| `CENFPVLot` | `N/D` | - |
| `CENFPPerST` | `N/D` | - |
| `CENFPXPed` | `N/D` | - |
| `CENFPnItPe` | `N/D` | - |
| `CENFPVlrIEst` | `N/D` | - |
| `CENFPIdx` | `N/D` | - |
| `CENFPDeson` | `N/D` | - |
| `CENFPMotDe` | `N/D` | - |
| `CENFPPerDif` | `N/D` | - |
| `CENFPVlrDif` | `N/D` | - |
| `CENFPIcmOP` | `N/D` | - |
| `CENFPBasIDes` | `N/D` | - |
| `CENFPAlInt` | `N/D` | - |
| `CENFPAlIest` | `N/D` | - |
| `CENFPPerIDes` | `N/D` | - |
| `CENFPPerFCP` | `N/D` | - |
| `CENFPVrFCP` | `N/D` | - |
| `CENFPVrIDes` | `N/D` | - |
| `CENFPVrIRem` | `N/D` | - |
| `CENFPFCPbST` | `N/D` | - |
| `CENFPFCPpST` | `N/D` | - |
| `CENFPFCPvST` | `N/D` | - |
| `CENFPFCPbRet` | `N/D` | - |
| `CENFPFCPpRet` | `N/D` | - |
| `CENFPFCPvRet` | `N/D` | - |
| `CENFPpST` | `N/D` | - |
| `CENFPBasFCP` | `N/D` | - |
| `CENFPFabLot` | `N/D` | - |
| `CENFPFCPBUFDest` | `N/D` | - |
| `CENFPIPIDev` | `N/D` | - |
| `CENFPPeFCP` | `N/D` | - |
| `CENFPVlrFCP` | `N/D` | - |
| `CENFPGLPPer` | `N/D` | - |
| `CENFPGNnPer` | `N/D` | - |
| `CENFPGNiPer` | `N/D` | - |
| `CENFPGPart` | `N/D` | - |
| `CENFPSTRedBc` | `N/D` | - |
| `CENFPPerDev` | `N/D` | - |
| `CENFPCLFCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CENFPIRBCIRRF` | `N/D` | - |
| `CENFPIRpIRRF` | `N/D` | - |
| `CENFPIRIRRF` | `N/D` | - |
| `CENFPCSTIBSCSB` | `N/D` | - |
| `CENFPBCIBSCBS` | `N/D` | - |
| `CENFPUFAlqIBS` | `N/D` | - |
| `CENFPUFRedIBS` | `N/D` | - |
| `CENFPUFEftIBS` | `N/D` | - |
| `CENFPUFVlrIBS` | `N/D` | - |
| `CENFPMunAlqIBS` | `N/D` | - |
| `CENFPMunRetIBS` | `N/D` | - |
| `CENFPMunEftIBS` | `N/D` | - |
| `CENFPMunVlrIBS` | `N/D` | - |
| `CENFPCBSAlq` | `N/D` | - |
| `CENFPCBSRet` | `N/D` | - |
| `CENFPCBSEft` | `N/D` | - |
| `CENFPCBSVlr` | `N/D` | - |
| `CENFPVTI` | `N/D` | - |
| `CENFPBCMon` | `N/D` | - |
| `CENFPAlqMon` | `N/D` | - |
| `CENFPVlrMon` | `N/D` | - |
| `CENFPcBenef` | `N/D` | - |

#### 🗺️ Índices
- `CENFPA` (Unique): `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CEProCod`, `CENFPIte`
- `CENFPB` (Duplicate): `CMEmpCod`, `CEProCod`
- `CENFPC` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFCSeq`
- `CENFPD` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFPPrcIcm`
- `CENFPE` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFPPrcIcm`, `CENFPCFOP`
- `CENFPF` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFPIdx`
- `CENFPG` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFPIte`

---

### 📌 CENFR
- **Descrição:** Resumo Icms por Natureza Operação da Nota Fiscal
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFRTip`, `CENFRCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CENFCSeq` | `N/D` | - |
| `CENFRTip` | `N/D` | - |
| `CENFRCod` | `N/D` | - |
| `CENFRBas` | `N/D` | - |
| `CENFRVlr` | `N/D` | - |
| `CENFRVlrTotPro` | `N/D` | - |
| `CENFRAlq` | `N/D` | - |

#### 🗺️ Índices
- `CENFR1` (Unique): `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFRTip`, `CENFRCod`
- `CENFR2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFCSeq`
- `CENFR3` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFRVlrTotPro`

---

### 📌 CENFV
- **Descrição:** COO Vinculados à CENFC
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFVSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CENFCSeq` | `N/D` | - |
| `CENFCSts` | `N/D` | - |
| `CENFVSeq` | `N/D` | - |
| `CENFVCOO` | `N/D` | - |

#### 🗺️ Índices
- `CENFV1` (Unique): `CMEmpCod`, `CMFilCod`, `CENFCSeq`, `CENFVSeq`
- `CENFV2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CENFCSeq`

---

### 📌 CEOco
- **Descrição:** Ocorrências do Produto
- **Chave Primária:** `CMEmpCod`, `CEProCod`, `CEOcoTst`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CEOcoTst` | `N/D` | - |
| `CEOcoDes` | `N/D` | - |

#### 🗺️ Índices
- `CEOco1` (Unique): `CMEmpCod`, `CEProCod`, `CEOcoTst`
- `CEOco2` (Duplicate): `CMEmpCod`, `CEProCod`

---

### 📌 CEPAP
- **Descrição:** Parâmetros da Atualização de Preços da Farmácia
- **Chave Primária:** `CEPAPCOD`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CEPAPCOD` | `N/D` | - |
| `CEPAPDTASIM` | `N/D` | - |
| `CEPAPDTAABC` | `N/D` | - |

#### 🗺️ Índices
- `CEPAP1` (Unique): `CEPAPCOD`

---

### 📌 CEPCA
- **Descrição:** Produtos x Características
- **Chave Primária:** `CMEmpCod`, `CEProACod`, `CECA1COD`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProACod` | `N/D` | - |
| `CEProACusUS` | `N/D` | - |
| `CEProACotUS` | `N/D` | - |
| `CEProADatCad` | `N/D` | - |
| `CEProAVlrCom` | `N/D` | - |
| `CEProAPrcCom` | `N/D` | - |
| `CEProAPreTabTem` | `N/D` | - |
| `CEProACodBar` | `N/D` | - |
| `CECA1COD` | `N/D` | - |
| `CECA1DES` | `N/D` | - |
| `CECA1EXINIV2` | `N/D` | - |
| `CECA2COD` | `N/D` | - |
| `CECA2DES` | `N/D` | - |
| `CECA1Sts` | `N/D` | - |

#### 🗺️ Índices
- `CEPCA1` (Unique): `CMEmpCod`, `CEProACod`, `CECA1COD`
- `CEPCA3` (Duplicate): `CMEmpCod`, `CEProACod`
- `CEPCA2` (Duplicate): `CMEmpCod`, `CECA1COD`, `CECA2COD`

---

### 📌 CEPCN
- **Descrição:** Estoque do Produto por Cor e N°
- **Chave Primária:** `CMEmpCod`, `CEProCod`, `CEProFilCod`, `CEPCNNro`, `CEPCNCor`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEProFilCod` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CEProFQtdV1` | `N/D` | - |
| `CEProFQtdAtu` | `N/D` | - |
| `CMEmpGrd` | `N/D` | - |
| `CEProFQtdPCN` | `N/D` | - |
| `CEProFQV1PCN` | `N/D` | - |
| `CEProFIDEPCN` | `N/D` | - |
| `CEPCNNro` | `N/D` | - |
| `CEPCNCor` | `N/D` | - |
| `CEPCNCodBar` | `N/D` | - |
| `CEPCNQtdAtu` | `N/D` | - |
| `CEPCNDes` | `N/D` | - |
| `CEPCNQTDV1` | `N/D` | - |
| `CEPCNIDE` | `N/D` | - |
| `CEPCNCorDesRes` | `N/D` | - |
| `CEPCNRGB1` | `N/D` | - |
| `CEPCNRGB2` | `N/D` | - |
| `CEPCNRGB3` | `N/D` | - |
| `CEPCNCor_Des` | `N/D` | - |
| `CEPCNPrg` | `N/D` | - |
| `CEPCNUsu` | `N/D` | - |
| `CEPCNTst` | `N/D` | - |
| `CEPCNIdx` | `N/D` | - |
| `CEPCNQtdEtq` | `N/D` | - |

#### 🗺️ Índices
- `CEPCN1` (Unique): `CMEmpCod`, `CEProCod`, `CEProFilCod`, `CEPCNNro`, `CEPCNCor`
- `CEPCN2` (Duplicate): `CMEmpCod`, `CEProCod`, `CEProFilCod`
- `CEPCN3` (Duplicate): `CEPCNCodBar`
- `CEPCN4` (Duplicate): `CMEmpCod`, `CEProCod`, `CEPCNNro`
- `CEPCN5` (Duplicate): `CMEmpCod`, `CEProCod`, `CEPCNIDE`
- `CEPCN6` (Duplicate): `CMEmpCod`, `CEProCod`, `CEPCNCor`, `CEPCNNro`

---

### 📌 CEPEC
- **Descrição:** Preços Especiais para o Cliente
- **Chave Primária:** `CMEmpCod`, `CRCliCod`, `CEPecProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRCliPEC` | `N/D` | - |
| `CEPecProCod` | `N/D` | - |
| `CEPecProDes` | `N/D` | - |
| `CEPecVlr` | `N/D` | - |
| `CEPecVlrCen` | `N/D` | - |
| `CEPecDta` | `N/D` | - |
| `CEPecPon` | `N/D` | - |
| `CEPecDstDsc` | `N/D` | - |
| `CEPecPreAtu` | `N/D` | - |

#### 🗺️ Índices
- `CEPEC1` (Unique): `CMEmpCod`, `CRCliCod`, `CEPecProCod`
- `CEPEC2` (Duplicate): `CMEmpCod`, `CRCliCod`

---

### 📌 CEPPr
- **Descrição:** Produtos da Profarma
- **Chave Primária:** `CEPPrCodEan`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CEPPrCodEan` | `N/D` | - |
| `CEPPrCodPro` | `N/D` | - |
| `CEPPrDes` | `N/D` | - |
| `CEPPrVlrCus` | `N/D` | - |
| `CEPPrMon` | `N/D` | - |
| `CEPPrLab` | `N/D` | - |
| `CEPPrDtaUltAtu` | `N/D` | - |
| `CEPPrVlrVda` | `N/D` | - |
| `CEPPrCat` | `N/D` | - |
| `CEPPrSts` | `N/D` | - |

#### 🗺️ Índices
- `CEPPr1` (Unique): `CEPPrCodEan`
- `CEPPr2` (Duplicate): `CEPPrDes`

---

### 📌 CEPRF
- **Descrição:** Produtos x Filial - Somente Consulta
- **Chave Primária:** `CMEmpCod`, `CEPRFCOD`, `CMFilCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEPRFCOD` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CEPRFQTD` | `N/D` | - |
| `CEPRFQtdPed` | `N/D` | - |
| `CEPRFDtaEnt` | `N/D` | - |
| `CEPRFDtaAtu` | `N/D` | - |

#### 🗺️ Índices
- `CEPRF1` (Unique): `CMEmpCod`, `CEPRFCOD`, `CMFilCod`
- `CEPRF2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CEPRG
- **Descrição:** Tabelas Genéricas do Produto
- **Chave Primária:** `CMEmpCod`, `CEProCod`, `CMGenCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CMGenCod` | `N/D` | - |
| `CMGenDes` | `N/D` | - |
| `CEPrgAtivo` | `N/D` | - |
| `CEPrgObsPa` | `N/D` | - |

#### 🗺️ Índices
- `CEPRGA` (Unique): `CMEmpCod`, `CEProCod`, `CMGenCod`
- `CEPRGB` (Duplicate): `CMEmpCod`, `CMGenCod`
- `CEPRGC` (Duplicate): `CMEmpCod`, `CEProCod`

---

### 📌 CEPRI
- **Descrição:** Detalhes Genérico dos Produtos
- **Chave Primária:** `CMEmpCod`, `CEProCod`, `CMGenCod`, `CEPriSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CMGenCod` | `N/D` | - |
| `CMGenDes` | `N/D` | - |
| `CEPrgAtivo` | `N/D` | - |
| `CEPrgObsPa` | `N/D` | - |
| `CEPriSeq` | `N/D` | - |
| `CEPriObs` | `N/D` | - |

#### 🗺️ Índices
- `CEPriA` (Unique): `CMEmpCod`, `CEProCod`, `CMGenCod`, `CEPriSeq`
- `CEPriB` (Duplicate): `CMEmpCod`, `CEProCod`, `CMGenCod`

---

### 📌 CEPrL
- **Descrição:** Lotes do Produto
- **Chave Primária:** `CMEmpCod`, `CEProCod`, `CEProFilCod`, `CEPrLLot`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEProFilCod` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CEProCodMS` | `N/D` | - |
| `CEProFQtdAtu` | `N/D` | - |
| `CEProFTotLot` | `N/D` | - |
| `CEProFQtdInv` | `N/D` | - |
| `CEProFVlrCusInv` | `N/D` | - |
| `CEProFVlrVdaInv` | `N/D` | - |
| `CEPrLLot` | `N/D` | - |
| `CEPrLQtd` | `N/D` | - |
| `CEPrLVct` | `N/D` | - |
| `CEPrLObs` | `N/D` | - |
| `CEPrLCUsu` | `N/D` | - |
| `CEPrLCPrg` | `N/D` | - |
| `CEPrLCTst` | `N/D` | - |
| `CEPrLFab` | `N/D` | - |
| `CEPrLQtdDec` | `N/D` | - |
| `CEPrLSkuDes` | `N/D` | - |
| `CEPrLSkuImg` | `N/D` | - |
| `CEPrLSku` | `N/D` | - |
| `CEPrLImg2Sku` | `N/D` | - |
| `CEPrLImg3Sku` | `N/D` | - |
| `CEPrLImg4Sku` | `N/D` | - |
| `CEPrLImg5Sku` | `N/D` | - |
| `CEPrLImg6Sku` | `N/D` | - |
| `CEPrLEAN` | `N/D` | - |

#### 🗺️ Índices
- `CEPrLA` (Unique): `CMEmpCod`, `CEProCod`, `CEProFilCod`, `CEPrLLot`
- `CEPrLB` (Duplicate): `CMEmpCod`, `CEProCod`, `CEProFilCod`

---

### 📌 CEPro
- **Descrição:** Produtos
- **Chave Primária:** `CMEmpCod`, `CEProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CMEmpCodBar_CodPro` | `N/D` | - |
| `CMEmpPAg` | `N/D` | - |
| `CMEmpModEtqGon` | `N/D` | - |
| `CMEmpCEVct` | `N/D` | - |
| `CMEmpPrxTelCE` | `N/D` | - |
| `CMEmpPerPadIcm` | `N/D` | - |
| `CMEmpGerCodBarAut` | `N/D` | - |
| `CMEmpAbrTelTrs` | `N/D` | - |
| `CMEmpEanQdoGerAut` | `N/D` | - |
| `CEProFab` | `N/D` | - |
| `CEAgrCod` | `N/D` | - |
| `CEProDesCom` | `N/D` | - |
| `CEProFlg` | `N/D` | - |
| `CEGrpCod` | `N/D` | - |
| `CEGrpNiv` | `N/D` | - |
| `CESgrNiv` | `N/D` | - |
| `CESgrCod` | `N/D` | - |
| `CESgrDes` | `N/D` | - |
| `CEGrpDes` | `N/D` | - |
| `CESgrNCM` | `N/D` | - |
| `CEProQtdAtu` | `N/D` | - |
| `CEProQtdV1` | `N/D` | - |
| `CEProQtdUltCom` | `N/D` | - |
| `CEProDta_UltCom` | `N/D` | - |
| `CEProDtaUltVda` | `N/D` | - |
| `CEProDtaCad` | `N/D` | - |
| `CEProDtaPenVda` | `N/D` | - |
| `CEProCDta` | `N/D` | - |
| `CEProCUsu` | `N/D` | - |
| `CEProCHor` | `N/D` | - |
| `CEProCPrg` | `N/D` | - |
| `CEProEstMin` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CEProFlaDel` | `N/D` | - |
| `CEProDtaTrs` | `N/D` | - |
| `CEProEstMax` | `N/D` | - |
| `CEProMrgLuc` | `N/D` | - |
| `CEPro2MrgLuc` | `N/D` | - |
| `CEProQtdPar` | `N/D` | - |
| `CMEmpCEMrgLuc` | `N/D` | - |
| `CMEmpCEQtdPar` | `N/D` | - |
| `CEPro1Cus` | `N/D` | - |
| `CEProPorFar` | `N/D` | - |
| `CEProVigFar` | `N/D` | - |
| `CEProPreVdaFar` | `N/D` | - |
| `CEProPreCusFar` | `N/D` | - |
| `CEProPartFar` | `N/D` | - |
| `CEProDtCadFar` | `N/D` | - |
| `CEProPerDes` | `N/D` | - |
| `CEProReaPro` | `N/D` | - |
| `CEProCodBar` | `N/D` | - |
| `CEProMrg1Atu` | `N/D` | - |
| `CEProMrgGel` | `N/D` | - |
| `CEProPerAumUlt` | `N/D` | - |
| `CEProPer_DecUlt` | `N/D` | - |
| `CEProCor` | `N/D` | - |
| `CEProNro` | `N/D` | - |
| `CEProSimpro` | `N/D` | - |
| `CEProPre1Tab` | `N/D` | - |
| `CEProPre2Tab` | `N/D` | - |
| `CEProPre3Tab` | `N/D` | - |
| `CEProPre4Tab` | `N/D` | - |
| `CEProDta1Tab` | `N/D` | - |
| `CEPro3Cus` | `N/D` | - |
| `CEProCusDol` | `N/D` | - |
| `CEPro2Cus` | `N/D` | - |
| `CEProVlrPar` | `N/D` | - |
| `CEProCusMed` | `N/D` | - |
| `CEProPrcCom` | `N/D` | - |
| `CEProAtuPrePelDis` | `N/D` | - |
| `CEProNomLabFar` | `N/D` | - |
| `CMEmpCEUsaGrpSgr` | `N/D` | - |
| `CEProImpNF` | `N/D` | - |
| `CEProPerRedBasCal` | `N/D` | - |
| `CEProPerAliIcm` | `N/D` | - |
| `CEProAceQtdVda` | `N/D` | - |
| `CEProEnvProBal` | `N/D` | - |
| `CEProTecAceBal` | `N/D` | - |
| `CEProSitTri` | `N/D` | - |
| `CEProDtaIniPro` | `N/D` | - |
| `CEProDtaFinPro` | `N/D` | - |
| `CEProProVis` | `N/D` | - |
| `CEProProCnv` | `N/D` | - |
| `CEProProPrz` | `N/D` | - |
| `CEProGVisPro` | `N/D` | - |
| `CEProGPrzPro` | `N/D` | - |
| `CEProPromQtd` | `N/D` | - |
| `CEProPromVlr` | `N/D` | - |
| `CEProImpLisCom` | `N/D` | - |
| `CEProPre_CusCod` | `N/D` | - |
| `CEProObs` | `N/D` | - |
| `CERepCod` | `N/D` | - |
| `CERepNom` | `N/D` | - |
| `CEProCodFor` | `N/D` | - |
| `CEProDesFor` | `N/D` | - |
| `CEProPreGel` | `N/D` | - |
| `CEProPAg` | `N/D` | - |
| `CEProDta_Inv` | `N/D` | - |
| `CEProMrgInv` | `N/D` | - |
| `CEProUltUsuVda` | `N/D` | - |
| `CEProMonLibFar` | `N/D` | - |
| `CEProPreTabAnt` | `N/D` | - |
| `CEProImpPreVdaEtq` | `N/D` | - |
| `CEProCPF` | `N/D` | - |
| `CEProCPFDes` | `N/D` | - |
| `CEProIdx` | `N/D` | - |
| `CEProCusFin` | `N/D` | - |
| `CEProCusUti` | `N/D` | - |
| `CEProCon` | `N/D` | - |
| `CMEmpAltPreVdaEst` | `N/D` | - |
| `CMEmpCECadMic` | `N/D` | - |
| `CEProLoc` | `N/D` | - |
| `CEProDta2Tab` | `N/D` | - |
| `CEProDta3Tab` | `N/D` | - |
| `CMEmpRef` | `N/D` | - |
| `CEProCST` | `N/D` | - |
| `CEProVct` | `N/D` | - |
| `CEProProCom` | `N/D` | - |
| `CEProNegPos` | `N/D` | - |
| `CEProDesCla` | `N/D` | - |
| `CEProCorNro` | `N/D` | - |
| `CEProPCN` | `N/D` | - |
| `CEPro_PerAliIcmRed` | `N/D` | - |
| `CEProDec` | `N/D` | - |
| `CEProPVU1` | `N/D` | - |
| `CMEmpDec` | `N/D` | - |
| `CEProCusCP` | `N/D` | - |
| `CEProAlqIPI` | `N/D` | - |
| `CEProAlqST` | `N/D` | - |
| `CEProPrcFre` | `N/D` | - |
| `CEProUnd` | `N/D` | - |
| `CEProNroNF` | `N/D` | - |
| `CEProClaDes` | `N/D` | - |
| `CEProMovVlr` | `N/D` | - |
| `CEProPro1Tab` | `N/D` | - |
| `CEProPro2Tab` | `N/D` | - |
| `CEProPro3Tab` | `N/D` | - |
| `CEProPro4Tab` | `N/D` | - |
| `CEProNCMDes` | `N/D` | - |
| `CEProNCM` | `N/D` | - |
| `CEProCCES` | `N/D` | - |
| `CEProQtdOrc` | `N/D` | - |
| `CEProCodAnv` | `N/D` | - |
| `CEProMotAnv` | `N/D` | - |
| `CEProPmcAnv` | `N/D` | - |
| `CEProGerSpd` | `N/D` | - |
| `CEProSebCusVar` | `N/D` | - |
| `CEProSebDspFix` | `N/D` | - |
| `CEProSebMrgLuc` | `N/D` | - |
| `CEProSebPreVda` | `N/D` | - |
| `CEProSebMarUp` | `N/D` | - |
| `CECLFCod` | `N/D` | - |
| `CEProCBenef` | `N/D` | - |
| `CMEmpVlrMaoObr` | `N/D` | - |
| `CEProIndMaoObr` | `N/D` | - |
| `CEProVlrMaoObr` | `N/D` | - |
| `CEProCla` | `N/D` | - |
| `CEProFat` | `N/D` | - |
| `CEProFatDes` | `N/D` | - |
| `CEProFatVlr` | `N/D` | - |
| `CEProPes` | `N/D` | - |
| `CEProQD1` | `N/D` | - |
| `CEProPQD1` | `N/D` | - |
| `CEProPQD2` | `N/D` | - |
| `CEProPQD3` | `N/D` | - |
| `CEProPQA` | `N/D` | - |
| `CEProQD2` | `N/D` | - |
| `CEProQD3` | `N/D` | - |
| `CEProQtdPed` | `N/D` | - |
| `CEProQtdDev` | `N/D` | - |
| `CEProQtdEnt` | `N/D` | - |
| `CEProDtaPrvEnt` | `N/D` | - |
| `CEProPVU2` | `N/D` | - |
| `CEProPVU3` | `N/D` | - |
| `CEProPVU4` | `N/D` | - |
| `CEProQDX` | `N/D` | - |
| `CEProPisCof` | `N/D` | - |
| `CEProNatRec` | `N/D` | - |
| `CEProDNatRec` | `N/D` | - |
| `CEProCSEPis` | `N/D` | - |
| `CEProPeEPis` | `N/D` | - |
| `CEProCSECof` | `N/D` | - |
| `CEProPeECof` | `N/D` | - |
| `CEProAlqPis` | `N/D` | - |
| `CEProAlqCof` | `N/D` | - |
| `CEProDCES` | `N/D` | - |
| `CEProSer` | `N/D` | - |
| `CEProISS` | `N/D` | - |
| `CEProPerDif` | `N/D` | - |
| `CEProCodGen` | `N/D` | - |
| `CEProCSTOut` | `N/D` | - |
| `CEProOrg` | `N/D` | - |
| `CEProANP` | `N/D` | - |
| `CeProClF` | `N/D` | - |
| `CEProPrcIVA` | `N/D` | - |
| `CEProRedPer` | `N/D` | - |
| `CEProRedOpF` | `N/D` | - |
| `CEProLucPC` | `N/D` | - |
| `CEProGPart` | `N/D` | - |
| `CEProUndEmb` | `N/D` | - |
| `CEProAcePreVda` | `N/D` | - |
| `CEProPrzVal` | `N/D` | - |
| `CEProVdaPesUnd` | `N/D` | - |
| `CEProPosAuxTab` | `N/D` | - |
| `CEProPosTab` | `N/D` | - |
| `CEProQtdEmb` | `N/D` | - |
| `CEProBasCodPro` | `N/D` | - |
| `CEProBasDesPro` | `N/D` | - |
| `CEProBasCusPrc` | `N/D` | - |
| `CEProBasVdaPrc` | `N/D` | - |
| `CEProAnoMesUltCom` | `N/D` | - |
| `CEProBasQtd` | `N/D` | - |
| `CEProProPer` | `N/D` | - |
| `CEProBasDiaQtd` | `N/D` | - |
| `CEProVol` | `N/D` | - |
| `CEProCli` | `N/D` | - |
| `CEProCliDes` | `N/D` | - |
| `CEProCodMS` | `N/D` | - |
| `CEProNBM` | `N/D` | - |
| `CEProCPC` | `N/D` | - |
| `CEProCPD` | `N/D` | - |
| `CEProLPD` | `N/D` | - |
| `CEProPrf` | `N/D` | - |
| `CEProFP` | `N/D` | - |
| `CEProFPQV` | `N/D` | - |
| `CEProFPQD` | `N/D` | - |
| `CEProPrcEntIVA` | `N/D` | - |
| `CEProEstZer` | `N/D` | - |
| `CEProLibCon` | `N/D` | - |
| `CEProMon` | `N/D` | - |
| `CEProFabAux` | `N/D` | - |
| `CEProConVas` | `N/D` | - |
| `CEProCreVas` | `N/D` | - |
| `CEProFPVU` | `N/D` | - |
| `CEProFPVT` | `N/D` | - |
| `CEProPis` | `N/D` | - |
| `CEProCof` | `N/D` | - |
| `CEProPrcVisCom` | `N/D` | - |
| `CEProPrcChqCom` | `N/D` | - |
| `CEProPrcCarCom` | `N/D` | - |
| `CEProPrcPrzCom` | `N/D` | - |
| `CEProPrcBolCom` | `N/D` | - |
| `CEProPonFid` | `N/D` | - |
| `CEProGar` | `N/D` | - |
| `CEProFra` | `N/D` | - |
| `CEProTipGar` | `N/D` | - |
| `CEProEstNeg` | `N/D` | - |
| `CEProBayDtBase` | `N/D` | - |
| `CEProBaySdBas` | `N/D` | - |
| `CEProPstDtBase` | `N/D` | - |
| `CEProPstSdBas` | `N/D` | - |
| `CEProPstApBase` | `N/D` | - |
| `CEProPstQEnt` | `N/D` | - |
| `CEProPstQSai` | `N/D` | - |
| `CEProPstAtual` | `N/D` | - |
| `CEProPerBio` | `N/D` | - |
| `CEProPstCnSd` | `N/D` | - |
| `CEProPstDApu` | `N/D` | - |
| `CEProDev` | `N/D` | - |
| `CEProPerPer` | `N/D` | - |
| `CEProConLot` | `N/D` | - |
| `CEProGLPPer` | `N/D` | - |
| `CEProGNnPer` | `N/D` | - |
| `CEProGNiPer` | `N/D` | - |
| `CEProPRedBCST` | `N/D` | - |
| `CEProAltura` | `N/D` | - |
| `CEProLargura` | `N/D` | - |
| `CEProComprimento` | `N/D` | - |
| `CEProPerMonRet` | `N/D` | - |
| `CESgrNCMDes` | `N/D` | - |
| `CEProDtaConFis` | `N/D` | - |
| `CEProUsuConFis` | `N/D` | - |
| `CEProEmtCodBarEtq` | `N/D` | - |
| `CMEmpCusUtl` | `N/D` | - |
| `CEProMrg2Luc` | `N/D` | - |
| `CEProMrg2Atu` | `N/D` | - |
| `CEProMrg3Luc` | `N/D` | - |
| `CEProMrg3Atu` | `N/D` | - |
| `CEProMrg4Atu` | `N/D` | - |
| `CEProMrg4Luc` | `N/D` | - |
| `CEProQtdIni` | `N/D` | - |
| `CEProQtdFin` | `N/D` | - |
| `CEProTmpCodAux` | `N/D` | - |
| `CEProTmpDesAux` | `N/D` | - |
| `CEProTmpPre1Tab` | `N/D` | - |
| `CEProTmp1Cus` | `N/D` | - |
| `CEProTmp_PrcCom` | `N/D` | - |

#### 🗺️ Índices
- `CEPro1` (Unique): `CMEmpCod`, `CEProCod`
- `CEProG` (Duplicate): `CMEmpCod`, `CEAgrCod`
- `CEPro2` (Duplicate): `CMEmpCod`, `CEGrpCod`, `CESgrCod`
- `CEProK` (Duplicate): `CMEmpCod`, `CERepCod`
- `CEProB` (Duplicate): `CMEmpCod`, `CEProNomLabFar`
- `CEProR` (Duplicate): `CMEmpCod`, `CECLFCod`
- `CEPro3` (Duplicate): `CMEmpCod`, `CEProDes`
- `CEPro4` (Duplicate): `CMEmpCod`, `CEGrpCod`, `CESgrCod`, `CEProDes`
- `CEProA` (Duplicate): `CMEmpCod`, `CEProFlg`, `CEProDes`
- `CEProU` (Duplicate): `CMEmpCod`, `CEProCodBar`, `CEProCod`
- `CEProI` (Duplicate): `CMEmpCod`, `CEProFab`
- `CEProJ` (Duplicate): `CMEmpCod`, `CEProTecAceBal`
- `CEProL` (Duplicate): `CMEmpCod`, `CEProBasCodPro`, `CEAgrCod`
- `CEProN` (Duplicate): `CMEmpCod`, `CEGrpCod`, `CESgrCod`, `CEProCod`, `CEAgrCod`
- `CMProM` (Duplicate): `CMEmpCod`, `CEProCPF`, `CEAgrCod`
- `CMProN` (Duplicate): `CEProIdx`
- `CEProO` (Duplicate): `CMEmpCod`, `CEProFlg`, `CEProDesCom`
- `CEProP` (Duplicate): `CEProFlg`, `CERepCod`, `CEProDes`
- `CEProQ` (Duplicate): `CMEmpCod`, `CEProLoc`

---

### 📌 CEProA
- **Descrição:** Dados Auxliares do Produto
- **Chave Primária:** `CMEmpCod`, `CEProACod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProACod` | `N/D` | - |
| `CEProACou` | `N/D` | - |
| `CEProaANro` | `N/D` | - |
| `CEProACor` | `N/D` | - |
| `CEProAGrpCod` | `N/D` | - |
| `CEProAPesAut` | `N/D` | - |
| `CEproADes` | `N/D` | - |
| `CEProAClaTer` | `N/D` | - |
| `CEProATipBasMed` | `N/D` | - |
| `CEProATipUsoMed` | `N/D` | - |
| `CEProAInsUndMed` | `N/D` | - |
| `CEProAUndFar` | `N/D` | - |
| `CEProAMedUndMed` | `N/D` | - |
| `CEProAUsoPro` | `N/D` | - |
| `CEProADtaInv` | `N/D` | - |
| `CEProAQII` | `N/D` | - |
| `CEProAQFI` | `N/D` | - |
| `CEProACst` | `N/D` | - |
| `CEProAPerAliIcm` | `N/D` | - |
| `CEProAUsaFixCst` | `N/D` | - |
| `CEProACusUS` | `N/D` | - |
| `CEProACotUS` | `N/D` | - |
| `CEProADatCad` | `N/D` | - |
| `CEProAVlrCom` | `N/D` | - |
| `CEProAPrcCom` | `N/D` | - |
| `CEProAPreTabTem` | `N/D` | - |
| `CEProACodBar` | `N/D` | - |

#### 🗺️ Índices
- `CEProA1` (Unique): `CMEmpCod`, `CEProACod`
- `CEProA2` (Duplicate): `CMEmpCod`
- `CEProA3` (Duplicate): `CMEmpCod`, `CEProAPreTabTem`

---

### 📌 CEProC
- **Descrição:** Códigos de Barra do Produto
- **Chave Primária:** `CMEmpCod`, `CEProCod`, `CEProCCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CEProCodBar` | `N/D` | - |
| `CMEmpRef` | `N/D` | - |
| `CEProCCod` | `N/D` | - |
| `CEProCAuxCodBar` | `N/D` | - |
| `CEProCFab` | `N/D` | - |

#### 🗺️ Índices
- `CEProC1` (Unique): `CMEmpCod`, `CEProCod`, `CEProCCod`
- `CEProC2` (Duplicate): `CMEmpCod`, `CEProCod`
- `CEProC3` (Duplicate): `CMEmpCod`, `CEProCCod`
- `CEProC4` (Duplicate): `CMEmpCod`, `CEProCFab`

---

### 📌 CEProF
- **Descrição:** Produtos da Filial
- **Chave Primária:** `CMEmpCod`, `CEProCod`, `CEProFilCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEProFilCod` | `N/D` | - |
| `CEProFQtdAtu` | `N/D` | - |
| `CEProFDtaTrs` | `N/D` | - |
| `CEProFEstMin` | `N/D` | - |
| `CEProFCUsu` | `N/D` | - |
| `CEProFCDta` | `N/D` | - |
| `CEProFCPrg` | `N/D` | - |
| `CEProFCodFor` | `N/D` | - |
| `CEProFQtdV1` | `N/D` | - |
| `CEProFDesFor` | `N/D` | - |
| `CEProFDtaIniPro` | `N/D` | - |
| `CEProFGVisPro` | `N/D` | - |
| `CEProFDtaFinPro` | `N/D` | - |
| `CEProFProVis` | `N/D` | - |
| `CEProFGPrzPro` | `N/D` | - |
| `CEProFProCnv` | `N/D` | - |
| `CEProFProPrz` | `N/D` | - |
| `CEProFPQA` | `N/D` | - |
| `CEProFFlg` | `N/D` | - |
| `CEProFPQEstMin` | `N/D` | - |
| `CEProFPQ_EstMax` | `N/D` | - |
| `CEProFEst_Max` | `N/D` | - |
| `CEProFCHor` | `N/D` | - |
| `CEProFQtdOrc` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CEProCodMS` | `N/D` | - |
| `CEProFTotLot` | `N/D` | - |
| `CEProFQtdInv` | `N/D` | - |
| `CEProFVlrCusInv` | `N/D` | - |
| `CEProFVlrVdaInv` | `N/D` | - |
| `CMEmpGrd` | `N/D` | - |
| `CEProFQtdPCN` | `N/D` | - |
| `CEProFQV1PCN` | `N/D` | - |
| `CEProFIDEPCN` | `N/D` | - |
| `CEProFLoc` | `N/D` | - |

#### 🗺️ Índices
- `CEProF1` (Unique): `CMEmpCod`, `CEProCod`, `CEProFilCod`
- `CEProF3` (Duplicate): `CMEmpCod`, `CEProCod`
- `CEProF2` (Duplicate): `CMEmpCod`, `CEProFilCod`
- `CEProF4` (Duplicate): `CMEmpCod`, `CEProFCodFor`

---

### 📌 CEProL
- **Descrição:** Produtos Local
- **Chave Primária:** `CEProLCodBar`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CEProLCodBar` | `N/D` | - |
| `CEProLPre_CusCod` | `N/D` | - |
| `CEProLCod` | `N/D` | - |
| `CEProLPAg` | `N/D` | - |
| `CEProLEnvProBal` | `N/D` | - |
| `CEProLDes` | `N/D` | - |
| `CEProLPre1Tab` | `N/D` | - |
| `CEProLReaPro` | `N/D` | - |
| `CEProLMrgAtu` | `N/D` | - |
| `CEProLQtdAtu` | `N/D` | - |
| `CEProLDtaIniPro` | `N/D` | - |
| `CEProLDtaFinPro` | `N/D` | - |
| `CEProLGVisPro` | `N/D` | - |
| `CEProLProVis` | `N/D` | - |
| `CEProLGPrzPro` | `N/D` | - |
| `CEProLProPrz` | `N/D` | - |
| `CEProLPre2Tab` | `N/D` | - |
| `CEProLPre3Tab` | `N/D` | - |
| `CEProLPreGel` | `N/D` | - |
| `CEProLSitTri` | `N/D` | - |
| `CEProLPerAliIcm` | `N/D` | - |
| `CECGSLPrcDsc` | `N/D` | - |
| `CECGSLPerVda` | `N/D` | - |
| `CESgrLCalDes` | `N/D` | - |
| `CESgrLPerDes` | `N/D` | - |
| `CEProL1Cus` | `N/D` | - |
| `CEProLIndMaoObr` | `N/D` | - |
| `CEProLPrcCom` | `N/D` | - |
| `CEProLGrpCod` | `N/D` | - |
| `CEProLSgrCod` | `N/D` | - |
| `CEProLSgr1CalDes` | `N/D` | - |
| `CEProLSgrPerDes` | `N/D` | - |

#### 🗺️ Índices
- `CEProL1` (Unique): `CEProLCodBar`

---

### 📌 CEProO
- **Descrição:** Observações Adicionais do Produto
- **Chave Primária:** `CMEmpCod`, `CEProOCod`, `CEProOLin`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProOCod` | `N/D` | - |
| `CEProOLin` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CEProOVC` | `N/D` | - |
| `CEProOVC1` | `N/D` | - |
| `CEProOCa` | `N/D` | - |
| `CEProOCa1` | `N/D` | - |
| `CEProOPr` | `N/D` | - |
| `CEProOPr1` | `N/D` | - |
| `CEProOGT` | `N/D` | - |
| `CEProOGT1` | `N/D` | - |
| `CEProOGTR` | `N/D` | - |
| `CEProOGTR1` | `N/D` | - |
| `CEProOGS` | `N/D` | - |
| `CEProOGS1` | `N/D` | - |
| `CEProOCo` | `N/D` | - |
| `CEProOCo1` | `N/D` | - |
| `CEProOFA` | `N/D` | - |
| `CEProOFA1` | `N/D` | - |
| `CEProOCl` | `N/D` | - |
| `CEProOCl1` | `N/D` | - |
| `CEProOFe` | `N/D` | - |
| `CEProOFe1` | `N/D` | - |
| `CEProOSo` | `N/D` | - |
| `CEProOSo1` | `N/D` | - |
| `CEProOCmp1` | `N/D` | - |
| `CEProOCmp2` | `N/D` | - |
| `CEProOCmp3` | `N/D` | - |
| `CEProOCmp4` | `N/D` | - |
| `CEProOCmp5` | `N/D` | - |
| `CEProOCmp6` | `N/D` | - |
| `CEProOL1` | `N/D` | - |
| `CEProOL2` | `N/D` | - |
| `CEProOL3` | `N/D` | - |
| `CEProOUndMed` | `N/D` | - |
| `CEProOObs` | `N/D` | - |
| `CEProOObs1` | `N/D` | - |
| `CEProOObs2` | `N/D` | - |
| `CEProOPriAti` | `N/D` | - |
| `CEProO1PriAti` | `N/D` | - |
| `CEProO2PriAti` | `N/D` | - |
| `CEProOObs3` | `N/D` | - |
| `CEProOObs4` | `N/D` | - |

#### 🗺️ Índices
- `CEProO1` (Unique): `CMEmpCod`, `CEProOCod`, `CEProOLin`
- `CEProO2` (Duplicate): `CMEmpCod`, `CEProOCod`
- `CEProO3` (Duplicate): `CMEmpCod`, `CEProO1PriAti`

---

### 📌 CEProU
- **Descrição:** Cadastro de % IVA por Estado
- **Chave Primária:** `CMEmpCod`, `CEProCod`, `CEProUF`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEProUF` | `N/D` | - |
| `CEProUFDes` | `N/D` | - |
| `CEProIVA` | `N/D` | - |
| `CEProUCFOP` | `N/D` | - |
| `CEProOrigem` | `N/D` | - |
| `CEProUCST` | `N/D` | - |
| `CEProUCSOSN` | `N/D` | - |
| `CEProUPeIcms` | `N/D` | - |
| `CEProUPeApr` | `N/D` | - |
| `CEProUAlInt` | `N/D` | - |
| `CEProUAlIes` | `N/D` | - |

#### 🗺️ Índices
- `CEProU1` (Unique): `CMEmpCod`, `CEProCod`, `CEProUF`
- `CEProU2` (Duplicate): `CMEmpCod`, `CEProCod`

---

### 📌 CEPrU
- **Descrição:** Configurações Fiscais do Produto por Estado
- **Chave Primária:** `CMEmpCod`, `CEProCod`, `CEPrUUF`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEPrUUF` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CEPrUMsg1` | `N/D` | - |
| `CEPrUMsg2` | `N/D` | - |
| `CEPrUMsg3` | `N/D` | - |
| `CEPrUMsg4` | `N/D` | - |
| `CEPrUMsg5` | `N/D` | - |
| `CEPrUPerRedBasCal` | `N/D` | - |
| `CEPrU_PerAliIcmRed` | `N/D` | - |
| `CEPrUUfAlqIcm` | `N/D` | - |

#### 🗺️ Índices
- `CEPrU1` (Unique): `CMEmpCod`, `CEProCod`, `CEPrUUF`
- `CEPrU2` (Duplicate): `CMEmpCod`, `CEProCod`

---

### 📌 CEPRV
- **Descrição:** Produtos x Vendedores Comissão
- **Chave Primária:** `CMEmpCod`, `CEProCod`, `CEPRVUsu`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CEPRVUsu` | `N/D` | - |
| `CEPRVPrc` | `N/D` | - |
| `CEPRVVlr` | `N/D` | - |

#### 🗺️ Índices
- `CEPRV1` (Unique): `CMEmpCod`, `CEProCod`, `CEPRVUsu`
- `CEPRV2` (Duplicate): `CMEmpCod`, `CEProCod`

---

### 📌 CEPxF
- **Descrição:** Tabela de Produto x Fornecedor
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CEPxFDta`, `CEProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CEPxFDta` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CEPxFTip` | `N/D` | - |
| `CEPxFVlr` | `N/D` | - |
| `CEPxFCUsu` | `N/D` | - |
| `CEPxFCPrg` | `N/D` | - |
| `CEPxFDtaTrs` | `N/D` | - |
| `CEPxFFlaDel` | `N/D` | - |
| `CEPxFTipNFi` | `N/D` | - |
| `CEPxFPerDes` | `N/D` | - |
| `CEPxFQtdDiaParPag` | `N/D` | - |
| `CEPxFVlrVis` | `N/D` | - |
| `CEPxFSldAnt` | `N/D` | - |
| `CEPxFQtdEnt` | `N/D` | - |
| `CEPxFSldAtu` | `N/D` | - |
| `CEPxFCusAnt` | `N/D` | - |
| `CEPxFCusAtu` | `N/D` | - |
| `CEPxFVdaAnt` | `N/D` | - |
| `CEPxFVdaAtu` | `N/D` | - |
| `CEPxFTST` | `N/D` | - |
| `CEPxFMovDta` | `N/D` | - |
| `CEPxFMovSeq` | `N/D` | - |
| `CEPxFNroNF` | `N/D` | - |
| `CEPxFObs` | `N/D` | - |

#### 🗺️ Índices
- `CEPxF1` (Unique): `CMEmpCod`, `CMFilCod`, `CEPxFDta`, `CEProCod`
- `CEPxF3` (Duplicate): `CMEmpCod`, `CEProCod`
- `CEPxF4` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CEPxF2` (Duplicate): `CMEmpCod`, `CPCliCod`

---

### 📌 CEPxI
- **Descrição:** Produtos x Impressoras
- **Chave Primária:** `CMEmpCod`, `CEProCod`, `CEImpCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CEImpCod` | `N/D` | - |
| `CEImpDes` | `N/D` | - |

#### 🗺️ Índices
- `CEPxI1` (Unique): `CMEmpCod`, `CEProCod`, `CEImpCod`
- `CEPxI3` (Duplicate): `CMEmpCod`, `CEProCod`
- `CEPxI2` (Duplicate): `CMEmpCod`, `CEImpCod`
- `CEPxI4` (Duplicate): `CMEmpCod`, `CEImpCod`, `CEProCod`

---

### 📌 CERep
- **Descrição:** Representantes
- **Chave Primária:** `CMEmpCod`, `CERepCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CERepCod` | `N/D` | - |
| `CERepNom` | `N/D` | - |
| `CERepObs` | `N/D` | - |

#### 🗺️ Índices
- `CERep1` (Unique): `CMEmpCod`, `CERepCod`
- `CERep2` (Duplicate): `CMEmpCod`

---

### 📌 CERIL
- **Descrição:** Retorno do Inventário Via Leitor
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CERILNomInv`, `CERILProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CERILNomInv` | `N/D` | - |
| `CERILProCod` | `N/D` | - |
| `CERILProDes` | `N/D` | - |
| `CERILQtdCon` | `N/D` | - |
| `CERILEstAtu` | `N/D` | - |
| `CERilDif` | `N/D` | - |
| `CERILTST` | `N/D` | - |
| `CERILSTS` | `N/D` | - |
| `CERILOrg` | `N/D` | - |
| `CERILErr` | `N/D` | - |
| `CERILGrp` | `N/D` | - |
| `CERILSgr` | `N/D` | - |
| `CERILCla` | `N/D` | - |
| `CERILDesErr` | `N/D` | - |

#### 🗺️ Índices
- `CERIL1` (Unique): `CMEmpCod`, `CMFilCod`, `CERILNomInv`, `CERILProCod`
- `CERIL2` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CERIL3` (Duplicate): `CERILTST`
- `CERIL4` (Duplicate): `CMFilCod`, `CERILTST`

---

### 📌 CERPF
- **Descrição:** Produto x Referência do Fornecedor
- **Chave Primária:** `CMEmpCod`, `CPCliCod`, `CERPFRef`, `CERPFCodPro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `CERPFRef` | `N/D` | - |
| `CERPFCodPro` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CERPFDesXML` | `N/D` | - |
| `CERPFDes` | `N/D` | - |
| `CERPFFatCnv` | `N/D` | - |
| `CERPFQtdCnv` | `N/D` | - |
| `CERPFUnCnv` | `N/D` | - |
| `CERPFNCM` | `N/D` | - |
| `CERPFEAN` | `N/D` | - |

#### 🗺️ Índices
- `CERPFA` (Unique): `CMEmpCod`, `CPCliCod`, `CERPFRef`, `CERPFCodPro`
- `CERPFB` (Duplicate): `CMEmpCod`, `CPCliCod`
- `CERPFC` (Duplicate): `CMEmpCod`, `CERPFCodPro`
- `CERPFD` (Duplicate): `CMEmpCod`, `CPCliCod`, `CERPFCodPro`

---

### 📌 CERPS1
- **Descrição:** RPS Gerados
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CERPSTipo`, `CERPSSerie`, `CERPSNum`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CERPSTipo` | `N/D` | - |
| `CERPSSerie` | `N/D` | - |
| `CERPSNum` | `N/D` | - |
| `CERPSStatus` | `N/D` | - |
| `CERPSLotR` | `N/D` | - |
| `CERPSVlr01` | `N/D` | - |
| `CERPSVlr02` | `N/D` | - |
| `CERPSVlr03` | `N/D` | - |
| `CERPSVlr04` | `N/D` | - |
| `CERPSVlr05` | `N/D` | - |
| `CERPSVlr06` | `N/D` | - |
| `CERPSVlr07` | `N/D` | - |
| `CERPSVlr08` | `N/D` | - |
| `CERPSVlr09` | `N/D` | - |
| `CERPSVlr10` | `N/D` | - |
| `CERPSVlr11` | `N/D` | - |
| `CERPSVlr12` | `N/D` | - |
| `CERPSVlr13` | `N/D` | - |
| `CERPSVlr14` | `N/D` | - |
| `CERPSAlq01` | `N/D` | - |
| `CERPSRet01` | `N/D` | - |
| `CERPSRet02` | `N/D` | - |
| `CERPSDtEmi` | `N/D` | - |
| `CERPSHrEmi` | `N/D` | - |
| `CERPSNatOp` | `N/D` | - |
| `CERPSRegime` | `N/D` | - |
| `CERPSOptante` | `N/D` | - |
| `CERPSIncentivo` | `N/D` | - |
| `CERPSItemLS` | `N/D` | - |
| `CERPSCodTrib` | `N/D` | - |
| `CERPSDiscrim` | `N/D` | - |
| `CERPSCodMun` | `N/D` | - |
| `CERPSTTomador` | `N/D` | - |
| `CERPSCTomador` | `N/D` | - |
| `CERPSITomador` | `N/D` | - |
| `CERPSRTomador` | `N/D` | - |
| `CERPSFTomador` | `N/D` | - |
| `CERPSEndTomador` | `N/D` | - |
| `CERPSNumTomador` | `N/D` | - |
| `CERPSCplTomador` | `N/D` | - |
| `CERPSBaiTomador` | `N/D` | - |
| `CERPSMunTomador` | `N/D` | - |
| `CERPSCidTomador` | `N/D` | - |
| `CERPSUFTomador` | `N/D` | - |
| `CERPSCepTomador` | `N/D` | - |
| `CERPSTelTomador` | `N/D` | - |
| `CERPSNumNF` | `N/D` | - |
| `CERPSEmiNF` | `N/D` | - |
| `CERPSCtrNF` | `N/D` | - |
| `CERPSPedCan` | `N/D` | - |
| `CERPSSitu` | `N/D` | - |
| `CERPSPedEmi` | `N/D` | - |
| `CERPSCodCli` | `N/D` | - |
| `CERPSEmailTomador` | `N/D` | - |
| `CERPSSitX` | `N/D` | - |
| `CERPSServX` | `N/D` | - |
| `CERPSCompetencia` | `N/D` | - |
| `CERPSDataEmi` | `N/D` | - |
| `CERPSHoraEmi` | `N/D` | - |
| `CERPSPedImp` | `N/D` | - |
| `CERPSDHNF` | `N/D` | - |
| `CERPSProtL` | `N/D` | - |
| `CERPSPImpAprox` | `N/D` | - |
| `CERPSVImpAprox` | `N/D` | - |
| `CERPSOImpAprox` | `N/D` | - |
| `CERPSAlq02` | `N/D` | - |
| `CERPSAlq03` | `N/D` | - |
| `CERPSAlq04` | `N/D` | - |
| `CERPSVlr15` | `N/D` | - |

#### 🗺️ Índices
- `CERPS1A` (Unique): `CMEmpCod`, `CMFilCod`, `CERPSTipo`, `CERPSSerie`, `CERPSNum`
- `CERPS1B` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CERPS1C` (Duplicate): `CMEmpCod`, `CMFilCod`, `CERPSTipo`, `CERPSSerie`, `CERPSNum`

---

### 📌 CERPS2
- **Descrição:** Lote de RPS
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CERPSLote`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CERPSLote` | `N/D` | - |
| `CERPSEnvio` | `N/D` | - |
| `CERPSDtRec` | `N/D` | - |
| `CERPSProt` | `N/D` | - |
| `CERPSQtde` | `N/D` | - |
| `CERPSSitRet` | `N/D` | - |

#### 🗺️ Índices
- `CERPS2A` (Unique): `CMEmpCod`, `CMFilCod`, `CERPSLote`
- `CERPS2B` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CERPS3
- **Descrição:** Itens do RPS
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CERPSTipo`, `CERPSSerie`, `CERPSNum`, `CERPSItem`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CERPSTipo` | `N/D` | - |
| `CERPSSerie` | `N/D` | - |
| `CERPSNum` | `N/D` | - |
| `CERPSStatus` | `N/D` | - |
| `CERPSLotR` | `N/D` | - |
| `CERPSVlr01` | `N/D` | - |
| `CERPSVlr02` | `N/D` | - |
| `CERPSVlr03` | `N/D` | - |
| `CERPSVlr04` | `N/D` | - |
| `CERPSVlr05` | `N/D` | - |
| `CERPSVlr06` | `N/D` | - |
| `CERPSVlr07` | `N/D` | - |
| `CERPSVlr08` | `N/D` | - |
| `CERPSVlr09` | `N/D` | - |
| `CERPSVlr10` | `N/D` | - |
| `CERPSVlr11` | `N/D` | - |
| `CERPSVlr12` | `N/D` | - |
| `CERPSVlr13` | `N/D` | - |
| `CERPSVlr14` | `N/D` | - |
| `CERPSAlq01` | `N/D` | - |
| `CERPSRet01` | `N/D` | - |
| `CERPSRet02` | `N/D` | - |
| `CERPSDtEmi` | `N/D` | - |
| `CERPSHrEmi` | `N/D` | - |
| `CERPSNatOp` | `N/D` | - |
| `CERPSRegime` | `N/D` | - |
| `CERPSOptante` | `N/D` | - |
| `CERPSIncentivo` | `N/D` | - |
| `CERPSItemLS` | `N/D` | - |
| `CERPSCodTrib` | `N/D` | - |
| `CERPSDiscrim` | `N/D` | - |
| `CERPSCodMun` | `N/D` | - |
| `CERPSTTomador` | `N/D` | - |
| `CERPSCTomador` | `N/D` | - |
| `CERPSITomador` | `N/D` | - |
| `CERPSRTomador` | `N/D` | - |
| `CERPSFTomador` | `N/D` | - |
| `CERPSEndTomador` | `N/D` | - |
| `CERPSNumTomador` | `N/D` | - |
| `CERPSCplTomador` | `N/D` | - |
| `CERPSBaiTomador` | `N/D` | - |
| `CERPSMunTomador` | `N/D` | - |
| `CERPSCidTomador` | `N/D` | - |
| `CERPSUFTomador` | `N/D` | - |
| `CERPSCepTomador` | `N/D` | - |
| `CERPSTelTomador` | `N/D` | - |
| `CERPSNumNF` | `N/D` | - |
| `CERPSEmiNF` | `N/D` | - |
| `CERPSCtrNF` | `N/D` | - |
| `CERPSPedCan` | `N/D` | - |
| `CERPSSitu` | `N/D` | - |
| `CERPSPedEmi` | `N/D` | - |
| `CERPSCodCli` | `N/D` | - |
| `CERPSEmailTomador` | `N/D` | - |
| `CERPSSitX` | `N/D` | - |
| `CERPSServX` | `N/D` | - |
| `CERPSCompetencia` | `N/D` | - |
| `CERPSDataEmi` | `N/D` | - |
| `CERPSHoraEmi` | `N/D` | - |
| `CERPSPedImp` | `N/D` | - |
| `CERPSDHNF` | `N/D` | - |
| `CERPSProtL` | `N/D` | - |
| `CERPSPImpAprox` | `N/D` | - |
| `CERPSVImpAprox` | `N/D` | - |
| `CERPSOImpAprox` | `N/D` | - |
| `CERPSAlq02` | `N/D` | - |
| `CERPSAlq03` | `N/D` | - |
| `CERPSAlq04` | `N/D` | - |
| `CERPSVlr15` | `N/D` | - |
| `CERPSItem` | `N/D` | - |
| `CERPSDescr` | `N/D` | - |
| `CERPSQuant` | `N/D` | - |
| `CERPSUnit` | `N/D` | - |
| `CERPSTotal` | `N/D` | - |

#### 🗺️ Índices
- `CERPS3A` (Unique): `CMEmpCod`, `CMFilCod`, `CERPSTipo`, `CERPSSerie`, `CERPSNum`, `CERPSItem`
- `CERPS3B` (Duplicate): `CMEmpCod`, `CMFilCod`, `CERPSTipo`, `CERPSSerie`, `CERPSNum`

---

### 📌 CERxB
- **Descrição:** Codigo da Rede Total x Codigo
- **Chave Primária:** `CERxBCodRed`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CERxBCodRed` | `N/D` | - |
| `CERxBCodBar` | `N/D` | - |
| `CERxBDesPro` | `N/D` | - |

#### 🗺️ Índices
- `CERxB1` (Unique): `CERxBCodRed`
- `CERxB2` (Duplicate): `CERxBCodBar`

---

### 📌 CESgr
- **Descrição:** Sub-Grupo de Produtos
- **Chave Primária:** `CMEmpCod`, `CEGrpCod`, `CESgrCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEGrpCod` | `N/D` | - |
| `CMEmpConQtdPecPro` | `N/D` | - |
| `CMEmpUsaPerComFix` | `N/D` | - |
| `CEGrpDes` | `N/D` | - |
| `CEGrpCon` | `N/D` | - |
| `CEGrpCUsu` | `N/D` | - |
| `CEGrpCDta` | `N/D` | - |
| `CEGrpCHor` | `N/D` | - |
| `CEGrpCPrg` | `N/D` | - |
| `CEGrpFlaDel` | `N/D` | - |
| `CEGrpDtaTrs` | `N/D` | - |
| `CEGrpPrcCom` | `N/D` | - |
| `CEGrpPrcVen` | `N/D` | - |
| `CEGrpNroIni` | `N/D` | - |
| `CEGrpNroFin` | `N/D` | - |
| `CEGrpTip` | `N/D` | - |
| `CEGrpCom` | `N/D` | - |
| `CEGrpPrzMed` | `N/D` | - |
| `CMEmpPrzMedGrp` | `N/D` | - |
| `CEGrpNiv` | `N/D` | - |
| `CEGrpDesCom` | `N/D` | - |
| `CESgrCod` | `N/D` | - |
| `CESgrDes` | `N/D` | - |
| `CESgrCUsu` | `N/D` | - |
| `CESgrCHor` | `N/D` | - |
| `CESgrCDta` | `N/D` | - |
| `CESgrFlaDel` | `N/D` | - |
| `CESgrDtaTrs` | `N/D` | - |
| `CESgrCalDes` | `N/D` | - |
| `CESgrPerDes` | `N/D` | - |
| `CESgrCPrg` | `N/D` | - |
| `CESgrConQtdPec` | `N/D` | - |
| `CESgrPerAcr` | `N/D` | - |
| `CESgrNCM` | `N/D` | - |
| `CESgrNCMDes` | `N/D` | - |
| `CESgrNiv` | `N/D` | - |
| `CESgrNivCod` | `N/D` | - |
| `CESgrNivDes` | `N/D` | - |
| `CEGrpNivNiv` | `N/D` | - |
| `CESgrNivOrd` | `N/D` | - |
| `CESgrEstMin` | `N/D` | - |

#### 🗺️ Índices
- `CESgr1` (Unique): `CMEmpCod`, `CEGrpCod`, `CESgrCod`
- `CESgr2` (Duplicate): `CMEmpCod`, `CEGrpCod`
- `CESgr3` (Duplicate): `CMEmpCod`, `CESgrDes`
- `CESgr4` (Duplicate): `CMEmpCod`, `CEGrpCod`, `CESgrNivOrd`

---

### 📌 CETGA
- **Descrição:** Total Grupo Anual
- **Chave Primária:** `CMEmpCod`, `CETGAAno`, `CEGrpCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CETGAAno` | `N/D` | - |
| `CEGrpCod` | `N/D` | - |
| `CEGrpDes` | `N/D` | - |
| `CETGAQtdVda` | `N/D` | - |
| `CETGAVlrVda` | `N/D` | - |
| `CETGAVlrCus` | `N/D` | - |
| `CETGAEstAtu` | `N/D` | - |
| `CETGAQtdCom` | `N/D` | - |

#### 🗺️ Índices
- `CETGA1` (Unique): `CMEmpCod`, `CETGAAno`, `CEGrpCod`
- `CETGA2` (Duplicate): `CMEmpCod`, `CEGrpCod`

---

### 📌 CETM1
- **Descrição:** Temp. Vendas do Período
- **Chave Primária:** `CMEmpCod`, `CETM1ProDes`, `CEProCod`, `CETm1NroCxa`, `CETm1IDEPCN`, `CETm1Ite`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CETM1ProDes` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CETm1NroCxa` | `N/D` | - |
| `CETm1IDEPCN` | `N/D` | - |
| `CETm1Ite` | `N/D` | - |
| `CETm1QtdVda` | `N/D` | - |
| `CETm1EstMin` | `N/D` | - |
| `CETm1EstMax` | `N/D` | - |
| `CETm1QtdCom` | `N/D` | - |
| `CETm1EstAtu` | `N/D` | - |
| `CETm1PreCus` | `N/D` | - |
| `CETM1CusFin` | `N/D` | - |
| `CETm1PreVda` | `N/D` | - |
| `CETm1PreGel` | `N/D` | - |
| `CETm1UltUsuVda` | `N/D` | - |
| `CETm1PrcCom` | `N/D` | - |
| `CETm1TotCus` | `N/D` | - |
| `CETm1TotVda` | `N/D` | - |
| `CETm1TotGel` | `N/D` | - |
| `CETM1TotLuc` | `N/D` | - |
| `CETM1CusMed` | `N/D` | - |
| `CETM1VdaMed` | `N/D` | - |
| `CETM1Mrg` | `N/D` | - |
| `CETM1Mrg2` | `N/D` | - |
| `CETM1Fab` | `N/D` | - |
| `CETM1DESPCN` | `N/D` | - |
| `CETM1Cor` | `N/D` | - |
| `CETM1NRO` | `N/D` | - |
| `CETM1Est_Ant` | `N/D` | - |
| `CETM1VVEAnt` | `N/D` | - |
| `CETM1VVEAtu` | `N/D` | - |
| `CETM1VCEAnt` | `N/D` | - |
| `CETM1VCEAtu` | `N/D` | - |
| `CETM1Vlr01` | `N/D` | - |
| `CETM1Vlr02` | `N/D` | - |
| `CETM1Vlr03` | `N/D` | - |
| `CETM1Vlr04` | `N/D` | - |
| `CETM1Vlr05` | `N/D` | - |
| `CETM1Vlr06` | `N/D` | - |
| `CETM1Vlr07` | `N/D` | - |
| `CETM1Vlr08` | `N/D` | - |
| `CETM1Vlr09` | `N/D` | - |
| `CETM1Cha01` | `N/D` | - |
| `CETM1Cha02` | `N/D` | - |
| `CETM1Cha03` | `N/D` | - |
| `CETM1Cha04` | `N/D` | - |
| `CETM1Cha05` | `N/D` | - |
| `CETM1PerPer` | `N/D` | - |
| `CETM1TotPer` | `N/D` | - |
| `CETM1QtdPer` | `N/D` | - |
| `CETM1CusPer` | `N/D` | - |
| `CETM1ClaDes` | `N/D` | - |
| `CETM1VlrAcr` | `N/D` | - |

#### 🗺️ Índices
- `CETM1A` (Unique): `CMEmpCod`, `CETM1ProDes`, `CEProCod`, `CETm1NroCxa`, `CETm1IDEPCN`, `CETm1Ite`
- `CETM1B` (Duplicate): `CMEmpCod`, `CEProCod`
- `CETM1C` (Duplicate): `CMEmpCod`, `CETm1QtdVda`, `CEProCod`

---

### 📌 CETm2
- **Descrição:** Tabela Temporária
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CETm2DesPro`, `CETm2Prg`, `CETM2CodBar`, `CETm2ProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CETm2DesPro` | `N/D` | - |
| `CETm2Prg` | `N/D` | - |
| `CETM2CodBar` | `N/D` | - |
| `CETm2ProCod` | `N/D` | - |
| `CETM2QCA` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CETm2EstAtu` | `N/D` | - |
| `CETm2QtdC` | `N/D` | - |
| `CETm2Pre1` | `N/D` | - |
| `CETm2Pre2` | `N/D` | - |
| `CETm2Pre3` | `N/D` | - |
| `CETm2DiFEs` | `N/D` | - |
| `CETm2QtdVda` | `N/D` | - |
| `CETm2Ent` | `N/D` | - |
| `CETm2Sai` | `N/D` | - |
| `CETm2Com` | `N/D` | - |
| `CETm2Idx` | `N/D` | - |
| `CETm2Cor` | `N/D` | - |
| `CETm2Nro` | `N/D` | - |
| `CETM2PCNIDE` | `N/D` | - |
| `CETM2NomAux` | `N/D` | - |
| `CETM2DesPCN` | `N/D` | - |
| `CETM2Cus` | `N/D` | - |
| `CETM2TotCus` | `N/D` | - |
| `CETM2TotVda` | `N/D` | - |
| `CETM2Vlr02` | `N/D` | - |
| `CETM2CusAux` | `N/D` | - |
| `CETM2VdaAux` | `N/D` | - |
| `CETM2Cha1A` | `N/D` | - |
| `CETM2Vlr01` | `N/D` | - |
| `CETM2Cha1B` | `N/D` | - |
| `CETM2Nro01` | `N/D` | - |
| `CETM2Nro02` | `N/D` | - |
| `CETM2Nro03` | `N/D` | - |
| `CETM2Nro04` | `N/D` | - |
| `CETM2Nro05` | `N/D` | - |
| `CETM2VC01` | `N/D` | - |
| `CETM2VC02` | `N/D` | - |
| `CETM2VC03` | `N/D` | - |
| `CETM2VC04` | `N/D` | - |
| `CETM2VC05` | `N/D` | - |
| `CETM2VC06` | `N/D` | - |
| `CETM2VC07` | `N/D` | - |
| `CETM2VC08` | `N/D` | - |
| `CETM2VC09` | `N/D` | - |
| `CETM2VC10` | `N/D` | - |
| `CETM2VN11` | `N/D` | - |
| `CETM2VN12` | `N/D` | - |
| `CETM2VN13` | `N/D` | - |
| `CETM2VN14` | `N/D` | - |
| `CETM2VN15` | `N/D` | - |
| `CETM2VN16` | `N/D` | - |
| `CETM2VN17` | `N/D` | - |
| `CETM2VN18` | `N/D` | - |
| `CETM2VN19` | `N/D` | - |
| `CETM2VN20` | `N/D` | - |
| `CETM2VV21` | `N/D` | - |
| `CETM2VV22` | `N/D` | - |
| `CETM2VV23` | `N/D` | - |
| `CETM2VV24` | `N/D` | - |
| `CETM2VV25` | `N/D` | - |
| `CETM2VV26` | `N/D` | - |
| `CETM2VV27` | `N/D` | - |
| `CETM2VV28` | `N/D` | - |
| `CETM2VV29` | `N/D` | - |
| `CETM2VV30` | `N/D` | - |
| `CETM2VD31` | `N/D` | - |
| `CETm2VD32` | `N/D` | - |
| `CETM2VD33` | `N/D` | - |
| `CETm2VD34` | `N/D` | - |
| `CETm2VD35` | `N/D` | - |

#### 🗺️ Índices
- `ICETm2` (Unique): `CMEmpCod`, `CMFilCod`, `CETm2DesPro`, `CETm2Prg`, `CETM2CodBar`, `CETm2ProCod`
- `CETM2B` (Duplicate): `CMEmpCod`, `CEProCod`
- `CETM2C` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CETM2D` (Duplicate): `CMEmpCod`, `CMFilCod`, `CETm2DesPro`, `CETm2ProCod`, `CETm2Prg`, `CETM2CodBar`
- `CETM2E` (Duplicate): `CETm2Idx`
- `CETM2F` (Duplicate): `CETm2Prg`, `CETm2Idx`

---

### 📌 CETM21
- **Descrição:** Temp. Totais Gr-Sub-Grp
- **Chave Primária:** `CMEmpCod`, `CETM21CheOut`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CETM21CheOut` | `N/D` | - |
| `CETM21TotVda` | `N/D` | - |
| `CETM21TotCus` | `N/D` | - |

#### 🗺️ Índices
- `CETM211` (Unique): `CMEmpCod`, `CETM21CheOut`
- `CETM212` (Duplicate): `CMEmpCod`

---

### 📌 CETM22
- **Descrição:** Temp. Totais Grupo
- **Chave Primária:** `CMEmpCod`, `CETM21CheOut`, `CEGrpCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CETM21CheOut` | `N/D` | - |
| `CETM21TotVda` | `N/D` | - |
| `CETM21TotCus` | `N/D` | - |
| `CEGrpCod` | `N/D` | - |
| `CETM22TotVda` | `N/D` | - |
| `CETM22TotCus` | `N/D` | - |
| `CETM22PrcVda` | `N/D` | - |
| `CETM22Mrg1` | `N/D` | - |
| `CETM22Mrg2` | `N/D` | - |
| `CETM22TTzVdaGer` | `N/D` | - |
| `CETM22TotQtd` | `N/D` | - |
| `CETM22CPQ` | `N/D` | - |
| `CETM22CPC` | `N/D` | - |
| `CETM22Vis` | `N/D` | - |
| `CETM22Prz` | `N/D` | - |
| `CETM22Car` | `N/D` | - |
| `CETM22Chq` | `N/D` | - |
| `CETM22Fin` | `N/D` | - |
| `CETM22Out` | `N/D` | - |

#### 🗺️ Índices
- `CETM221` (Unique): `CMEmpCod`, `CETM21CheOut`, `CEGrpCod`
- `CETM222` (Duplicate): `CMEmpCod`, `CEGrpCod`
- `CETM223` (Duplicate): `CMEmpCod`, `CETM21CheOut`

---

### 📌 CETM23
- **Descrição:** Temp. Totais Sub-Grupo
- **Chave Primária:** `CMEmpCod`, `CETM21CheOut`, `CEGrpCod`, `CESgrCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CETM21CheOut` | `N/D` | - |
| `CETM21TotVda` | `N/D` | - |
| `CETM21TotCus` | `N/D` | - |
| `CEGrpCod` | `N/D` | - |
| `CETM22TotVda` | `N/D` | - |
| `CETM22TotCus` | `N/D` | - |
| `CETM22PrcVda` | `N/D` | - |
| `CETM22Mrg1` | `N/D` | - |
| `CETM22Mrg2` | `N/D` | - |
| `CETM22TTzVdaGer` | `N/D` | - |
| `CETM22TotQtd` | `N/D` | - |
| `CETM22CPQ` | `N/D` | - |
| `CETM22CPC` | `N/D` | - |
| `CETM22Vis` | `N/D` | - |
| `CETM22Prz` | `N/D` | - |
| `CETM22Car` | `N/D` | - |
| `CETM22Chq` | `N/D` | - |
| `CETM22Fin` | `N/D` | - |
| `CETM22Out` | `N/D` | - |
| `CESgrCod` | `N/D` | - |
| `CETM23TotVda` | `N/D` | - |
| `CETM23TotCus` | `N/D` | - |
| `CETM23PrcVda` | `N/D` | - |
| `CETM23Prc2Vda` | `N/D` | - |
| `CETM23TtzVdaGer` | `N/D` | - |
| `CETM23TtzGrp` | `N/D` | - |
| `CETM23TotQtd` | `N/D` | - |
| `CETM23Mrg1` | `N/D` | - |
| `CETM23Mrg2` | `N/D` | - |
| `CETM23CPQ` | `N/D` | - |
| `CETM23CPC` | `N/D` | - |
| `CETM23Vis` | `N/D` | - |
| `CETM23Prz` | `N/D` | - |
| `CETM23Car` | `N/D` | - |
| `CETM23Chq` | `N/D` | - |
| `CETM23Fin` | `N/D` | - |
| `CETM23Out` | `N/D` | - |

#### 🗺️ Índices
- `CETM231` (Unique): `CMEmpCod`, `CETM21CheOut`, `CEGrpCod`, `CESgrCod`
- `CETM232` (Duplicate): `CMEmpCod`, `CEGrpCod`, `CESgrCod`
- `CETM233` (Duplicate): `CMEmpCod`, `CETM21CheOut`, `CEGrpCod`

---

### 📌 CETM31
- **Descrição:** TCE11D
- **Chave Primária:** `CETM31REF`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CETM31REF` | `N/D` | - |

#### 🗺️ Índices
- `CETM31A` (Unique): `CETM31REF`

---

### 📌 CETM32
- **Descrição:** Temporaria
- **Chave Primária:** `CETM31REF`, `CETM32CrsCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CETM31REF` | `N/D` | - |
| `CETM32CrsCod` | `N/D` | - |

#### 🗺️ Índices
- `CETM32A` (Unique): `CETM31REF`, `CETM32CrsCod`
- `CETM32B` (Duplicate): `CETM31REF`

---

### 📌 CETM33
- **Descrição:** Temporaria
- **Chave Primária:** `CETM31REF`, `CETM32CrsCod`, `CETM33Nro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CETM31REF` | `N/D` | - |
| `CETM32CrsCod` | `N/D` | - |
| `CETM33Nro` | `N/D` | - |
| `CETM33Qtd` | `N/D` | - |

#### 🗺️ Índices
- `CETM33A` (Unique): `CETM31REF`, `CETM32CrsCod`, `CETM33Nro`
- `CETM33B` (Duplicate): `CETM31REF`, `CETM32CrsCod`

---

### 📌 CETM34
- **Descrição:** Temporaria
- **Chave Primária:** `CETM31REF`, `CETM34Nro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CETM31REF` | `N/D` | - |
| `CETM34Nro` | `N/D` | - |
| `CETM34Qtd` | `N/D` | - |

#### 🗺️ Índices
- `CETM34A` (Unique): `CETM31REF`, `CETM34Nro`
- `CETM34B` (Duplicate): `CETM31REF`

---

### 📌 CETM4
- **Descrição:** Temporária Produto Cor/Nº
- **Chave Primária:** `CMEmpCod`, `CEProCod`, `CETM4FilCod`, `CETM4Cor`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CETM4FilCod` | `N/D` | - |
| `CETM4Cor` | `N/D` | - |
| `CETM4CorDes` | `N/D` | - |
| `CETM4RGB1` | `N/D` | - |
| `CETM4RGB2` | `N/D` | - |
| `CETM4RGB3` | `N/D` | - |
| `CETM4Nro01` | `N/D` | - |
| `CETM4Nro02` | `N/D` | - |
| `CETM4Nro03` | `N/D` | - |
| `CETM4Nro04` | `N/D` | - |
| `CETM4Nro05` | `N/D` | - |
| `CETM4Nro06` | `N/D` | - |
| `CETM4Nro07` | `N/D` | - |
| `CETM4Nro08` | `N/D` | - |
| `CETM4Nro09` | `N/D` | - |
| `CETM4Nro10` | `N/D` | - |
| `CETM4Nro11` | `N/D` | - |
| `CETM4Nro12` | `N/D` | - |
| `CETM4Nro13` | `N/D` | - |
| `CETM4Nro14` | `N/D` | - |
| `CETM4Nro15` | `N/D` | - |
| `CETM4Nro16` | `N/D` | - |
| `CETM4Nro17` | `N/D` | - |
| `CETM4Nro18` | `N/D` | - |
| `CETM4Nro19` | `N/D` | - |
| `CETM4Nro20` | `N/D` | - |
| `CETM4Qtd01` | `N/D` | - |
| `CETM4Qtd02` | `N/D` | - |
| `CETM4Qtd03` | `N/D` | - |
| `CETM4Qtd04` | `N/D` | - |
| `CETM4Qtd05` | `N/D` | - |
| `CETM4Qtd06` | `N/D` | - |
| `CETM4Qtd07` | `N/D` | - |
| `CETM4Qtd08` | `N/D` | - |
| `CETM4Qtd09` | `N/D` | - |
| `CETM4Qtd10` | `N/D` | - |
| `CETM4Qtd11` | `N/D` | - |
| `CETM4Qtd12` | `N/D` | - |
| `CETM4Qtd13` | `N/D` | - |
| `CETM4Qtd14` | `N/D` | - |
| `CETM4Qtd15` | `N/D` | - |
| `CETM4Qtd16` | `N/D` | - |
| `CETM4Qtd17` | `N/D` | - |
| `CETM4Qtd18` | `N/D` | - |
| `CETM4Qtd19` | `N/D` | - |
| `CETM4Qtd20` | `N/D` | - |
| `CETM4QtdTot` | `N/D` | - |

#### 🗺️ Índices
- `CETM4A` (Unique): `CMEmpCod`, `CEProCod`, `CETM4FilCod`, `CETM4Cor`
- `CETM4B` (Duplicate): `CMEmpCod`, `CEProCod`
- `CETM4C` (Duplicate): `CMEmpCod`, `CEProCod`, `CETM4Cor`

---

### 📌 CETMP1
- **Descrição:** Tabela Temporaria 01
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CETMP1IdeFor`, `CETMP1ProDes`, `CETMP1ProCod`, `CETMP1Prg`, `CETMP1CUsu`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CETMP1IdeFor` | `N/D` | - |
| `CETMP1ProDes` | `N/D` | - |
| `CETMP1ProCod` | `N/D` | - |
| `CETMP1Prg` | `N/D` | - |
| `CETMP1CUsu` | `N/D` | - |
| `CETMP1UsuUltVda` | `N/D` | - |
| `CETMP1QTD` | `N/D` | - |
| `CETMP1DtaIni` | `N/D` | - |
| `CETMP1DtaFin` | `N/D` | - |
| `CETMP1HorIni` | `N/D` | - |
| `CETMP1HorFin` | `N/D` | - |
| `CETMP1PerDes` | `N/D` | - |
| `CETMP1ProLab` | `N/D` | - |
| `CETMP1Flg` | `N/D` | - |
| `CETMP1EstAtu` | `N/D` | - |
| `CETMP1QtdCom` | `N/D` | - |
| `CETMP1EstMin` | `N/D` | - |
| `CETMP1Est_Max` | `N/D` | - |
| `CETMP1DtaHorPro` | `N/D` | - |
| `CETMP1PreCus` | `N/D` | - |
| `CETMP1PrcCom` | `N/D` | - |
| `CETMP1GrpCod` | `N/D` | - |
| `CETMP1SgrCod` | `N/D` | - |
| `CETMP1Imp` | `N/D` | - |
| `CETMP1CusFin` | `N/D` | - |
| `CETMP1Nro1` | `N/D` | - |
| `CETMP1Nro2` | `N/D` | - |
| `CETMP1Nro3` | `N/D` | - |
| `CETMP1Nro4` | `N/D` | - |
| `CETMP1Nro5` | `N/D` | - |
| `CETMP1CHA1` | `N/D` | - |
| `CETMP1CHA2` | `N/D` | - |
| `CETMP1CHA3` | `N/D` | - |
| `CETMP1CHA4` | `N/D` | - |
| `CETMP1CHA5` | `N/D` | - |
| `CETMP12ProCod` | `N/D` | - |
| `CETMP13ProCod` | `N/D` | - |
| `CETMP1QTD2` | `N/D` | - |
| `CETMP1QTD3` | `N/D` | - |

#### 🗺️ Índices
- `CETMP1A` (Unique): `CMEmpCod`, `CMFilCod`, `CETMP1IdeFor`, `CETMP1ProDes`, `CETMP1ProCod`, `CETMP1Prg`, `CETMP1CUsu`
- `CETMP1B` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CETMP1C` (Duplicate): `CETMP1CHA5`

---

### 📌 CETN1
- **Descrição:** Controle de Tintas CORAL
- **Chave Primária:** `CETNCodTin`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CETNCodTin` | `N/D` | - |
| `CETNDesTin` | `N/D` | - |

#### 🗺️ Índices
- `CETN1A` (Unique): `CETNCodTin`

---

### 📌 CETN2
- **Descrição:** Controle de Tintas CORAL Produtos
- **Chave Primária:** `CETNCodTin`, `CETNCodCom`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CETNCodTin` | `N/D` | - |
| `CETNCodCom` | `N/D` | - |
| `CETNCodLin` | `N/D` | - |
| `CETNDesLin` | `N/D` | - |
| `CETNCodEmb` | `N/D` | - |
| `CETNDesEmb` | `N/D` | - |
| `CETNCodBas` | `N/D` | - |
| `CETNLetBas` | `N/D` | - |
| `CETNDesBas` | `N/D` | - |
| `CETNCodCc1` | `N/D` | - |
| `CETNCodCc2` | `N/D` | - |
| `CETNCodCc3` | `N/D` | - |
| `CETNCodCc4` | `N/D` | - |
| `CETNCodCc5` | `N/D` | - |
| `CETNQtdCc1` | `N/D` | - |
| `CETNQtdCc2` | `N/D` | - |
| `CETNQtdCc3` | `N/D` | - |
| `CETNQtdCc4` | `N/D` | - |
| `CETNQtdCc5` | `N/D` | - |

#### 🗺️ Índices
- `CETN2A` (Unique): `CETNCodTin`, `CETNCodCom`
- `CETN2B` (Duplicate): `CETNCodTin`

---

### 📌 CETP1
- **Descrição:** Configuração Tabelas de Preço
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CETP1Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CETP1Cod` | `N/D` | - |
| `CETP1IDX` | `N/D` | - |

#### 🗺️ Índices
- `CETP1A` (Unique): `CMEmpCod`, `CMFilCod`, `CETP1Cod`
- `CETP1B` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CETP1C` (Duplicate): `CETP1IDX`

---

### 📌 CETP2
- **Descrição:** Configura Tabela de Preço 02
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CETP1Cod`, `CETP2Sit`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CETP1Cod` | `N/D` | - |
| `CETP1IDX` | `N/D` | - |
| `CETP2Sit` | `N/D` | - |
| `CETP2PDV` | `N/D` | - |
| `CETP2PDG` | `N/D` | - |
| `CETP2MaxPar` | `N/D` | - |
| `CETP2PDS` | `N/D` | - |

#### 🗺️ Índices
- `CETP2A` (Unique): `CMEmpCod`, `CMFilCod`, `CETP1Cod`, `CETP2Sit`
- `CETP2B` (Duplicate): `CMEmpCod`, `CMFilCod`, `CETP1Cod`

---

### 📌 CETri
- **Descrição:** Acumulo Estoque Trimestral
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CEAno`, `CETriCod`, `CEProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CEAno` | `N/D` | - |
| `CETriCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CETriQtdEnt` | `N/D` | - |
| `CETriQtdCom` | `N/D` | - |
| `CETriQtd_SaiTrs` | `N/D` | - |
| `CETriQtdSai` | `N/D` | - |
| `CETriQtd_EntTrs` | `N/D` | - |
| `CETriEstIni` | `N/D` | - |
| `CETriEstFin` | `N/D` | - |
| `CETriQtdVda` | `N/D` | - |
| `CETriDtaIni` | `N/D` | - |
| `CETriDtaFin` | `N/D` | - |
| `CETriDesTri` | `N/D` | - |

#### 🗺️ Índices
- `CETri1` (Unique): `CMEmpCod`, `CMFilCod`, `CEAno`, `CETriCod`, `CEProCod`
- `CETri2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CEProCod`, `CEAno`

---

### 📌 CETRS1
- **Descrição:** Sequência das Notas Transferências
- **Chave Primária:** `CMEmpCod`, `CETrs1Dta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CETrs1Dta` | `N/D` | - |
| `CETrs1PrxSeq` | `N/D` | - |
| `CETrs1DtaTrs` | `N/D` | - |
| `CETrs1FlaDel` | `N/D` | - |

#### 🗺️ Índices
- `CETRS1A` (Unique): `CMEmpCod`, `CETrs1Dta`
- `CETRS1B` (Duplicate): `CMEmpCod`

---

### 📌 CETRS2
- **Descrição:** Cabeçalho da Transferência
- **Chave Primária:** `CMEmpCod`, `CETrs2FilOrg`, `CETrs2FilDes`, `CETrs1Dta`, `CETrs2Seq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CETrs2FilOrg` | `N/D` | - |
| `CETrs2FilDes` | `N/D` | - |
| `CETrs1Dta` | `N/D` | - |
| `CETrs2Seq` | `N/D` | - |
| `CETrs2NopCod` | `N/D` | - |
| `CMEmpGrd` | `N/D` | - |
| `CETrs2DtaNF` | `N/D` | - |
| `CETrs2NroNF` | `N/D` | - |
| `CETrs2SerNF` | `N/D` | - |
| `CETrs2NFFO` | `N/D` | - |
| `CETrs2NFFD` | `N/D` | - |
| `CETrs2VlrTot` | `N/D` | - |
| `CETrs2Qtd` | `N/D` | - |
| `CETrs2TotIte` | `N/D` | - |
| `CETrs2Obs` | `N/D` | - |
| `CETrs2CDta` | `N/D` | - |
| `CETrs2CHor` | `N/D` | - |
| `CETrs2CUsu` | `N/D` | - |
| `CETrs2CPrg` | `N/D` | - |
| `CETrs2DtaTrs` | `N/D` | - |
| `CETrs2Sts` | `N/D` | - |
| `CETrs2TipNf` | `N/D` | - |
| `CETrs2EnvArq` | `N/D` | - |
| `CETrs2PEn` | `N/D` | - |
| `CETrs2PSa` | `N/D` | - |
| `CETrs2CusTot` | `N/D` | - |

#### 🗺️ Índices
- `CETRS2A` (Unique): `CMEmpCod`, `CETrs2FilOrg`, `CETrs2FilDes`, `CETrs1Dta`, `CETrs2Seq`
- `CETRS2B` (Duplicate): `CMEmpCod`, `CETrs1Dta`
- `CETRS2C` (Duplicate): `CETrs2Sts`
- `CETRS2D` (Duplicate): `CMEmpCod`, `CETrs1Dta`

---

### 📌 CETRS3
- **Descrição:** Itens da Nota Transferência
- **Chave Primária:** `CMEmpCod`, `CETrs2FilOrg`, `CETrs2FilDes`, `CETrs1Dta`, `CETrs2Seq`, `CETrs3CodCha`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CETrs2FilOrg` | `N/D` | - |
| `CETrs2FilDes` | `N/D` | - |
| `CETrs1Dta` | `N/D` | - |
| `CETrs2Seq` | `N/D` | - |
| `CETrs2NopCod` | `N/D` | - |
| `CMEmpGrd` | `N/D` | - |
| `CETrs2DtaNF` | `N/D` | - |
| `CETrs2NroNF` | `N/D` | - |
| `CETrs2SerNF` | `N/D` | - |
| `CETrs2NFFO` | `N/D` | - |
| `CETrs2NFFD` | `N/D` | - |
| `CETrs2VlrTot` | `N/D` | - |
| `CETrs2Qtd` | `N/D` | - |
| `CETrs2TotIte` | `N/D` | - |
| `CETrs2Obs` | `N/D` | - |
| `CETrs2CDta` | `N/D` | - |
| `CETrs2CHor` | `N/D` | - |
| `CETrs2CUsu` | `N/D` | - |
| `CETrs2CPrg` | `N/D` | - |
| `CETrs2DtaTrs` | `N/D` | - |
| `CETrs2Sts` | `N/D` | - |
| `CETrs2TipNf` | `N/D` | - |
| `CETrs2EnvArq` | `N/D` | - |
| `CETrs2PEn` | `N/D` | - |
| `CETrs2PSa` | `N/D` | - |
| `CETrs2CusTot` | `N/D` | - |
| `CETrs3CodCha` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEProFlg` | `N/D` | - |
| `CEProQtdV1` | `N/D` | - |
| `CEProCusMed` | `N/D` | - |
| `CETrs3Qtd` | `N/D` | - |
| `CETrs3VlrUnt` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CETrs3VlrTot` | `N/D` | - |
| `CETrs3CusUnt` | `N/D` | - |
| `CETrs3CusTot` | `N/D` | - |
| `CETrs3DtaTrs` | `N/D` | - |
| `CETrs3FlaDel` | `N/D` | - |
| `CEProPre1Tab` | `N/D` | - |
| `CEProCusUti` | `N/D` | - |
| `CEProPCN` | `N/D` | - |
| `CETrs3IDEPCN` | `N/D` | - |
| `CETrs3Cor` | `N/D` | - |
| `CETrs3Nro` | `N/D` | - |
| `CEPro1Cus` | `N/D` | - |
| `CETrs3TotQtdTrs4` | `N/D` | - |

#### 🗺️ Índices
- `CETRS3A` (Unique): `CMEmpCod`, `CETrs2FilOrg`, `CETrs2FilDes`, `CETrs1Dta`, `CETrs2Seq`, `CETrs3CodCha`
- `CETRS3B` (Duplicate): `CMEmpCod`, `CEProCod`
- `CETRS3C` (Duplicate): `CMEmpCod`, `CETrs2FilOrg`, `CETrs2FilDes`, `CETrs1Dta`, `CETrs2Seq`

---

### 📌 CETrs4
- **Descrição:** Transferência de Produtos Tratando Cor e N°
- **Chave Primária:** `CMEmpCod`, `CETrs2FilOrg`, `CETrs2FilDes`, `CETrs1Dta`, `CETrs2Seq`, `CETrs3CodCha`, `CETrs4Cor`, `CETrs4Nro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CETrs2FilOrg` | `N/D` | - |
| `CETrs2FilDes` | `N/D` | - |
| `CETrs1Dta` | `N/D` | - |
| `CETrs2Seq` | `N/D` | - |
| `CETrs3CodCha` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CETrs3Qtd` | `N/D` | - |
| `CETrs3TotQtdTrs4` | `N/D` | - |
| `CETrs4Cor` | `N/D` | - |
| `CETrs4Nro` | `N/D` | - |
| `CETrs4DesPcn` | `N/D` | - |
| `CETrs4IDEPCN` | `N/D` | - |
| `CETrs4Qtd` | `N/D` | - |
| `CETrs4EfeLct` | `N/D` | - |
| `CETrs4CodBar` | `N/D` | - |

#### 🗺️ Índices
- `CETRS4A` (Unique): `CMEmpCod`, `CETrs2FilOrg`, `CETrs2FilDes`, `CETrs1Dta`, `CETrs2Seq`, `CETrs3CodCha`, `CETrs4Cor`, `CETrs4Nro`
- `CETRS4B` (Duplicate): `CMEmpCod`, `CETrs2FilOrg`, `CETrs2FilDes`, `CETrs1Dta`, `CETrs2Seq`, `CETrs3CodCha`

---

### 📌 CETSA
- **Descrição:** Total SubGrupo Anual
- **Chave Primária:** `CMEmpCod`, `CETGAAno`, `CEGrpCod`, `CESgrCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CETGAAno` | `N/D` | - |
| `CEGrpCod` | `N/D` | - |
| `CEGrpDes` | `N/D` | - |
| `CETGAQtdVda` | `N/D` | - |
| `CETGAVlrVda` | `N/D` | - |
| `CETGAVlrCus` | `N/D` | - |
| `CETGAEstAtu` | `N/D` | - |
| `CETGAQtdCom` | `N/D` | - |
| `CESgrCod` | `N/D` | - |
| `CESgrDes` | `N/D` | - |
| `CETSAQtdVda` | `N/D` | - |
| `CETSAVlrVda` | `N/D` | - |
| `CETSAVlrCus` | `N/D` | - |
| `CETSAEstAtu` | `N/D` | - |
| `CETSAQtdCom` | `N/D` | - |

#### 🗺️ Índices
- `CETSA1` (Unique): `CMEmpCod`, `CETGAAno`, `CEGrpCod`, `CESgrCod`
- `CETSA2` (Duplicate): `CMEmpCod`, `CEGrpCod`, `CESgrCod`
- `CETSA3` (Duplicate): `CMEmpCod`, `CETGAAno`, `CEGrpCod`

---

### 📌 CETSM
- **Descrição:** Total SubGrupo Mensal
- **Chave Primária:** `CMEmpCod`, `CETGAAno`, `CEGrpCod`, `CESgrCod`, `CETSMMes`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CETGAAno` | `N/D` | - |
| `CEGrpCod` | `N/D` | - |
| `CEGrpDes` | `N/D` | - |
| `CETGAQtdVda` | `N/D` | - |
| `CETGAVlrVda` | `N/D` | - |
| `CETGAVlrCus` | `N/D` | - |
| `CETGAEstAtu` | `N/D` | - |
| `CETGAQtdCom` | `N/D` | - |
| `CESgrCod` | `N/D` | - |
| `CESgrDes` | `N/D` | - |
| `CETSAQtdVda` | `N/D` | - |
| `CETSAVlrVda` | `N/D` | - |
| `CETSAVlrCus` | `N/D` | - |
| `CETSAEstAtu` | `N/D` | - |
| `CETSAQtdCom` | `N/D` | - |
| `CETSMMes` | `N/D` | - |
| `CETSMQtdVda` | `N/D` | - |
| `CETSMVlrVda` | `N/D` | - |
| `CETSMVlrCus` | `N/D` | - |
| `CETSMEstAtu` | `N/D` | - |
| `CETSMQtdCom` | `N/D` | - |

#### 🗺️ Índices
- `CETSM1` (Unique): `CMEmpCod`, `CETGAAno`, `CEGrpCod`, `CESgrCod`, `CETSMMes`
- `CETSM2` (Duplicate): `CMEmpCod`, `CETGAAno`, `CEGrpCod`, `CESgrCod`
- `CETSM3` (Duplicate): `CMEmpCod`, `CETGAAno`, `CETSMMes`

---

### 📌 CEVar
- **Descrição:** Cadastro de Variações
- **Chave Primária:** `CMEmpCod`, `CEVarCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEVarCod` | `N/D` | - |
| `CEVarDes` | `N/D` | - |
| `CEVarVlr` | `N/D` | - |
| `CEVarAtv` | `N/D` | - |

#### 🗺️ Índices
- `CEVarA` (Unique): `CMEmpCod`, `CEVarCod`
- `CEVarB` (Duplicate): `CMEmpCod`

---

### 📌 CEVas
- **Descrição:** Vasilhames
- **Chave Primária:** `CMEmpCod`, `CEVasCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEVasCod` | `N/D` | - |
| `CEVasNom` | `N/D` | - |
| `CEVasCUSU` | `N/D` | - |
| `CEVasCDta` | `N/D` | - |
| `CEVasCPrg` | `N/D` | - |

#### 🗺️ Índices
- `CEVasA` (Unique): `CMEmpCod`, `CEVasCod`
- `CEVasB` (Duplicate): `CMEmpCod`

---

### 📌 CFDes1
- **Descrição:** Controle Horas Desenvolvimento
- **Chave Primária:** `CMEmpCod`, `CFFunCod`, `CFDes1Dta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CFFunCod` | `N/D` | - |
| `CFDes1Dta` | `N/D` | - |
| `CFFunDes` | `N/D` | - |
| `CFDes1TemTot` | `N/D` | - |
| `CFDes1TstFin` | `N/D` | - |
| `CFDes1Err` | `N/D` | - |
| `CFFunSalReg` | `N/D` | - |
| `CFDes1VlrTot` | `N/D` | - |

#### 🗺️ Índices
- `CFDes1A` (Unique): `CMEmpCod`, `CFFunCod`, `CFDes1Dta`
- `CFDes1B` (Duplicate): `CMEmpCod`, `CFFunCod`

---

### 📌 CFDes2
- **Descrição:** Controle Funcionários Desenvolvimento
- **Chave Primária:** `CMEmpCod`, `CFFunCod`, `CFDes1Dta`, `CFDes2TstIni`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CFFunCod` | `N/D` | - |
| `CFDes1Dta` | `N/D` | - |
| `CFFunDes` | `N/D` | - |
| `CFDes1TemTot` | `N/D` | - |
| `CFDes1TstFin` | `N/D` | - |
| `CFDes1Err` | `N/D` | - |
| `CFFunSalReg` | `N/D` | - |
| `CFDes1VlrTot` | `N/D` | - |
| `CFDes2TstIni` | `N/D` | - |
| `CFDes2TstFin` | `N/D` | - |
| `CFDes2TemTot` | `N/D` | - |
| `CFDes2NroCha` | `N/D` | - |
| `CFDes2DesCha` | `N/D` | - |
| `CFDes2Obs` | `N/D` | - |
| `CFDes2VlrHor` | `N/D` | - |
| `CFDes2VlrTot` | `N/D` | - |
| `CFDes2CliCod` | `N/D` | - |
| `CFDes2CliDes` | `N/D` | - |
| `CFDes2TipCod` | `N/D` | - |
| `CFDes2CliVlr` | `N/D` | - |

#### 🗺️ Índices
- `CFDes2A` (Unique): `CMEmpCod`, `CFFunCod`, `CFDes1Dta`, `CFDes2TstIni`
- `CFDes2B` (Duplicate): `CMEmpCod`, `CFFunCod`, `CFDes1Dta`
- `CFDes2C` (Duplicate): `CMEmpCod`, `CFDes2NroCha`, `CFDes1Dta`

---

### 📌 CFFun
- **Descrição:** Funcionarios
- **Chave Primária:** `CMEmpCod`, `CFFunCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CFFunCod` | `N/D` | - |
| `CFFilCod` | `N/D` | - |
| `CFFunAti` | `N/D` | - |
| `CFFunReg` | `N/D` | - |
| `CFFunImpRVa` | `N/D` | - |
| `CFFunDes` | `N/D` | - |
| `CFFunFan` | `N/D` | - |
| `CFFunCDta` | `N/D` | - |
| `CFFunCHor` | `N/D` | - |
| `CFFunCUsu` | `N/D` | - |
| `CFFunEnd` | `N/D` | - |
| `CFFunBai` | `N/D` | - |
| `CFFunCid` | `N/D` | - |
| `CFFunUf` | `N/D` | - |
| `CFFunCep` | `N/D` | - |
| `CFFunTel1` | `N/D` | - |
| `CFFunFax` | `N/D` | - |
| `CFFunTel3` | `N/D` | - |
| `CFFunTel4` | `N/D` | - |
| `CFFunCIC` | `N/D` | - |
| `CFFunRG` | `N/D` | - |
| `CFTipCod` | `N/D` | - |
| `CFTipDes` | `N/D` | - |
| `CFFunRes1` | `N/D` | - |
| `CFFunRes2` | `N/D` | - |
| `CFFunCar1` | `N/D` | - |
| `CFFunCar2` | `N/D` | - |
| `CFFunDtaTrs` | `N/D` | - |
| `CFFunFlaDel` | `N/D` | - |
| `DSDspCod` | `N/D` | - |
| `DSDspDes` | `N/D` | - |
| `CFFunXXX` | `N/D` | - |
| `CFFunForCod` | `N/D` | - |
| `CFFunCliCod` | `N/D` | - |
| `CFFunCliDes` | `N/D` | - |
| `CFFunForDes` | `N/D` | - |
| `CFFunDta_CP` | `N/D` | - |
| `CFFunSeq_CP` | `N/D` | - |
| `CFFunPar_CP` | `N/D` | - |
| `CFFunPon` | `N/D` | - |
| `CFFunCon1` | `N/D` | - |
| `CFFunCon2` | `N/D` | - |
| `CFFunEtqNom` | `N/D` | - |
| `CFFunDtaReg` | `N/D` | - |
| `CFFunDtaEnt` | `N/D` | - |
| `CFFunDtaNsc` | `N/D` | - |
| `CFFunDtaRsc` | `N/D` | - |
| `CFFunSalSem` | `N/D` | - |
| `CFFunSalMes` | `N/D` | - |
| `CFFunSalReg` | `N/D` | - |
| `CFFunObs1` | `N/D` | - |
| `CFFunObs2` | `N/D` | - |
| `CFFunObs3` | `N/D` | - |
| `CFFunObs4` | `N/D` | - |
| `CFFunObs5` | `N/D` | - |
| `CFFunObs6` | `N/D` | - |
| `CFFunObs7` | `N/D` | - |
| `CFFunObs8` | `N/D` | - |
| `CFFunObs9` | `N/D` | - |

#### 🗺️ Índices
- `CFFun1` (Unique): `CMEmpCod`, `CFFunCod`
- `CFFun2` (Duplicate): `CMEmpCod`, `CFTipCod`
- `CFFun5` (Duplicate): `CMEmpCod`, `DSDspCod`
- `CFFun4` (Duplicate): `CMEmpCod`, `CFFilCod`
- `CFFun3` (Duplicate): `CMEmpCod`, `CFFunDes`

---

### 📌 CFFUQ
- **Descrição:** Peças Produzidas pelo Funcionário
- **Chave Primária:** `CMEmpCod`, `CFFunCod`, `CFFuQDta`, `CFFuQSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CFFunCod` | `N/D` | - |
| `CFFuQDta` | `N/D` | - |
| `CFFuQSeq` | `N/D` | - |
| `CFFunAti` | `N/D` | - |
| `CFFunDes` | `N/D` | - |
| `CFFuQ1VlrTot` | `N/D` | - |
| `CFFunFan` | `N/D` | - |
| `CFFuQObs` | `N/D` | - |
| `CFFuQObs1` | `N/D` | - |
| `CFFuQObs2` | `N/D` | - |
| `CFFuQObs3` | `N/D` | - |
| `CFFuQObs5` | `N/D` | - |
| `CFFuQObs4` | `N/D` | - |
| `CFFuQObs7` | `N/D` | - |
| `CFFuQObs6` | `N/D` | - |
| `CFFuQObs8` | `N/D` | - |
| `CFFuqTip` | `N/D` | - |
| `CFFuQObs9` | `N/D` | - |
| `CFFuQDtaVct` | `N/D` | - |
| `CFFuQQtd` | `N/D` | - |
| `CFFuQQtd2` | `N/D` | - |
| `CFFuQQtd1` | `N/D` | - |
| `CFFuQQtd4` | `N/D` | - |
| `CFFuQQtd3` | `N/D` | - |
| `CFFuQQtd7` | `N/D` | - |
| `CFFuQQtd8` | `N/D` | - |
| `CFFuQQtd9` | `N/D` | - |
| `CFFuQQtd6` | `N/D` | - |
| `CFFuQVlrUnt` | `N/D` | - |
| `CFFuQ1VlrUnt` | `N/D` | - |
| `CFFuQQtd5` | `N/D` | - |
| `CFFuQ2VlrUnt` | `N/D` | - |
| `CFFuQ3VlrUnt` | `N/D` | - |
| `CFFuQ4VlrUnt` | `N/D` | - |
| `CFFuQ5VlrUnt` | `N/D` | - |
| `CFFuQ6VlrUnt` | `N/D` | - |
| `CFFuQ8VlrUnt` | `N/D` | - |
| `CFFuQ7VlrUnt` | `N/D` | - |
| `CFFuQ9VlrUnt` | `N/D` | - |
| `CFFuQ2ProCod` | `N/D` | - |
| `CFFuQProCod` | `N/D` | - |
| `CFFuQVlrTot` | `N/D` | - |
| `CFFuQVlr1Tot` | `N/D` | - |
| `CFFuQVlr2Tot` | `N/D` | - |
| `CFFuQVlr3Tot` | `N/D` | - |
| `CFFuQVlr4Tot` | `N/D` | - |
| `CFFuQVlr5Tot` | `N/D` | - |
| `CFFuQVlr6Tot` | `N/D` | - |
| `CFFuQVlr7Tot` | `N/D` | - |
| `CFFuQVlr8Tot` | `N/D` | - |
| `CFFuQVlr9Tot` | `N/D` | - |
| `CFFuqVlrTtz` | `N/D` | - |
| `CFFuQ3ProCod` | `N/D` | - |
| `CFFuQ5ProCod` | `N/D` | - |
| `CFFuQ4ProCod` | `N/D` | - |
| `CFFuQ6ProCod` | `N/D` | - |
| `CFFuQ7ProCod` | `N/D` | - |
| `CFFuQ1ProCod` | `N/D` | - |
| `CFFuQ8ProCod` | `N/D` | - |
| `CFFuQProDes` | `N/D` | - |
| `CFFuQ1ProDes` | `N/D` | - |
| `CFFuQ2ProDes` | `N/D` | - |
| `CFFuQ9ProCod` | `N/D` | - |
| `CFFuQ4ProDes` | `N/D` | - |
| `CFFuQ5ProDes` | `N/D` | - |
| `CFFuQ6ProDes` | `N/D` | - |
| `CFFuQ3ProDes` | `N/D` | - |
| `CFFuQ8ProDes` | `N/D` | - |
| `CFFuQ9ProDes` | `N/D` | - |
| `CFFuQ7ProDes` | `N/D` | - |
| `CFFuqQtdTot` | `N/D` | - |
| `CFFuQSts` | `N/D` | - |
| `CFFuQIdx` | `N/D` | - |

#### 🗺️ Índices
- `CFFUQ1` (Unique): `CMEmpCod`, `CFFunCod`, `CFFuQDta`, `CFFuQSeq`
- `CFFUQ2` (Duplicate): `CMEmpCod`, `CFFunCod`
- `CFFUQ3` (Duplicate): `CFFuQDta`
- `CFFUQ4` (Duplicate): `CFFuQIdx`

---

### 📌 CFMov
- **Descrição:** Movimentacao do Funcionario
- **Chave Primária:** `CMEmpCod`, `CFFunCod`, `CFMovDta`, `CFVDeCod`, `CFMovSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CFFunCod` | `N/D` | - |
| `CFMovDta` | `N/D` | - |
| `CFVDeCod` | `N/D` | - |
| `CFMovSeq` | `N/D` | - |
| `CFFilCod` | `N/D` | - |
| `CMFilTipImp` | `N/D` | - |
| `CMFilDtaValLct` | `N/D` | - |
| `CMFilAltGrpSgrDsp` | `N/D` | - |
| `CFMovVlr` | `N/D` | - |
| `CFMovQtd` | `N/D` | - |
| `CFFunDes` | `N/D` | - |
| `CFVDeD_C` | `N/D` | - |
| `CFVDeDes` | `N/D` | - |
| `CFVDeRec` | `N/D` | - |
| `CFMovCHor` | `N/D` | - |
| `CFMovCDta` | `N/D` | - |
| `CFMovCUsu` | `N/D` | - |
| `CFMovCPrg` | `N/D` | - |
| `CFMovDtaTrs` | `N/D` | - |
| `CFMovFlaDel` | `N/D` | - |
| `CFMovObs` | `N/D` | - |
| `CFMovObsAux` | `N/D` | - |
| `CMFilBcoCof` | `N/D` | - |
| `CMFilFilBcoCof` | `N/D` | - |
| `DSDspCod` | `N/D` | - |
| `DSDspDes` | `N/D` | - |
| `DSGrpCod` | `N/D` | - |
| `DSSgrDes` | `N/D` | - |
| `DSGrpDes` | `N/D` | - |
| `DSSgrCod` | `N/D` | - |
| `CFMovDtaDsp` | `N/D` | - |
| `CFMovSeqDsp` | `N/D` | - |
| `CFMovDspCod` | `N/D` | - |
| `CFMovDspDes` | `N/D` | - |
| `CFMovChqNro` | `N/D` | - |
| `CFMovChqVct` | `N/D` | - |
| `CFMovCxa` | `N/D` | - |
| `CFMovChqBco` | `N/D` | - |
| `CFMovChqDes` | `N/D` | - |
| `CFMovDCx` | `N/D` | - |
| `CFMovCheOut` | `N/D` | - |
| `CFMovFilCod` | `N/D` | - |
| `CFFunSeq_CP` | `N/D` | - |
| `CFFunPar_CP` | `N/D` | - |
| `CFFunDta_CP` | `N/D` | - |
| `CFMovBxa_CP` | `N/D` | - |
| `CFVDeDspDes` | `N/D` | - |
| `CFVdeDspCod` | `N/D` | - |
| `CFMovCCMovSeqLct` | `N/D` | - |
| `CFMovCCx` | `N/D` | - |
| `CFMovGrpDes` | `N/D` | - |
| `CFMovGrpDsp` | `N/D` | - |
| `CFMovSgrDsp` | `N/D` | - |
| `CFMovSgrDes` | `N/D` | - |
| `CFFunForDes` | `N/D` | - |
| `CFFunForCod` | `N/D` | - |
| `CFMovCPMovDta` | `N/D` | - |
| `CFMovCPSeq` | `N/D` | - |

#### 🗺️ Índices
- `CFMov1` (Unique): `CMEmpCod`, `CFFunCod`, `CFMovDta`, `CFVDeCod`, `CFMovSeq`
- `CFMov2` (Duplicate): `CMEmpCod`, `CFVDeCod`
- `CFMov3` (Duplicate): `CMEmpCod`, `CFFunCod`
- `CFMov4` (Duplicate): `CMEmpCod`, `CFMovDta`, `CFVDeCod`, `CFMovSeq`
- `CFMov5` (Duplicate): `CMEmpCod`, `CFMovDta`
- `CFMov6` (Duplicate): `CFMovDCx`
- `CFMov7` (Duplicate): `CFMovCCx`

---

### 📌 CFTip
- **Descrição:** Tipo de Funcionario
- **Chave Primária:** `CMEmpCod`, `CFTipCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CFTipCod` | `N/D` | - |
| `CFTipDes` | `N/D` | - |
| `CFTipCHor` | `N/D` | - |
| `CFTipCUsu` | `N/D` | - |
| `CFTipCDta` | `N/D` | - |
| `CFTipDtaTrs` | `N/D` | - |
| `CFTipFlaDel` | `N/D` | - |

#### 🗺️ Índices
- `CFTip1` (Unique): `CMEmpCod`, `CFTipCod`
- `CFTip2` (Duplicate): `CMEmpCod`
- `CFTip3` (Duplicate): `CMEmpCod`, `CFTipDes`

---

### 📌 CFVDe
- **Descrição:** Codigos Vencimentos\Descontos
- **Chave Primária:** `CMEmpCod`, `CFVDeCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CFVDeCod` | `N/D` | - |
| `CFVDeDes` | `N/D` | - |
| `CFVDeCDta` | `N/D` | - |
| `CFVDeCHor` | `N/D` | - |
| `CFVDeCUsu` | `N/D` | - |
| `CFVDeCPrg` | `N/D` | - |
| `CFVDeD_C` | `N/D` | - |
| `CFVDeRec` | `N/D` | - |
| `CFVDeDesRes` | `N/D` | - |
| `CFVDeDtaTrs` | `N/D` | - |
| `CFVDeFlaDel` | `N/D` | - |
| `CFVdeDspCod` | `N/D` | - |
| `CFVDeDspDes` | `N/D` | - |

#### 🗺️ Índices
- `CFVDe1` (Unique): `CMEmpCod`, `CFVDeCod`
- `CFVDe2` (Duplicate): `CMEmpCod`
- `CFVDe3` (Duplicate): `CMEmpCod`, `CFVDeDes`

---

### 📌 CLHis
- **Descrição:** Histórico Entrada/Saida Clube
- **Chave Primária:** `CLTt1Cod`, `CLTt2Seq`, `CLHisTstEnt`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CLTt1Cod` | `N/D` | - |
| `CLTt2Seq` | `N/D` | - |
| `CLTt2NomDep` | `N/D` | - |
| `CLTt1NomTit` | `N/D` | - |
| `CLHisTstEnt` | `N/D` | - |
| `CLHisTstSai` | `N/D` | - |
| `CLHisDur` | `N/D` | - |
| `CLHisSts` | `N/D` | - |
| `CLHisAceAut` | `N/D` | - |
| `CLHisBarVlr` | `N/D` | - |

#### 🗺️ Índices
- `CLHis1` (Unique): `CLTt1Cod`, `CLTt2Seq`, `CLHisTstEnt`
- `CLHis2` (Duplicate): `CLTt1Cod`, `CLTt2Seq`
- `CLHis3` (Duplicate): `CLTt1Cod`, `CLTt2Seq`, `CLHisSts`
- `CLHis4` (Duplicate): `CLHisSts`

---

### 📌 CLTt1
- **Descrição:** Cadastro Títulos
- **Chave Primária:** `CLTt1Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CLTt1Cod` | `N/D` | - |
| `CLTt1NomTit` | `N/D` | - |
| `CLTt1Sts` | `N/D` | - |
| `CLTt1Tip` | `N/D` | - |
| `CLTt1BarCnt` | `N/D` | - |
| `CLTt1BarDta` | `N/D` | - |
| `CLTt1BarVlr` | `N/D` | - |
| `CLTt1Idx` | `N/D` | - |
| `CLTt1DtaBxa` | `N/D` | - |
| `CLTt1DtaIni` | `N/D` | - |

#### 🗺️ Índices
- `CLTt1A` (Unique): `CLTt1Cod`
- `CLTt1B` (Duplicate): `CLTt1Idx`

---

### 📌 CLTt2
- **Descrição:** Cadastro de Títulos - Dependentes
- **Chave Primária:** `CLTt1Cod`, `CLTt2Seq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CLTt1Cod` | `N/D` | - |
| `CLTt1NomTit` | `N/D` | - |
| `CLTt1Sts` | `N/D` | - |
| `CLTt1Tip` | `N/D` | - |
| `CLTt1BarCnt` | `N/D` | - |
| `CLTt1BarDta` | `N/D` | - |
| `CLTt1BarVlr` | `N/D` | - |
| `CLTt1Idx` | `N/D` | - |
| `CLTt1DtaBxa` | `N/D` | - |
| `CLTt1DtaIni` | `N/D` | - |
| `CLTt2Seq` | `N/D` | - |
| `CLTt2NomDep` | `N/D` | - |
| `CLTt2DtaFinSus` | `N/D` | - |
| `CLTt2DtaIniSus` | `N/D` | - |
| `CLTt2Idx` | `N/D` | - |
| `CLTt2CodCar` | `N/D` | - |
| `CLTt2ColNroCar` | `N/D` | - |
| `CLTt2ColChaCar` | `N/D` | - |
| `CLTt2BarCnt` | `N/D` | - |
| `CLTt2Tip` | `N/D` | - |
| `CLTt2Sts` | `N/D` | - |
| `CLTt2Loc` | `N/D` | - |

#### 🗺️ Índices
- `CLTt2A` (Unique): `CLTt1Cod`, `CLTt2Seq`
- `CLTt2B` (Duplicate): `CLTt1Cod`
- `CLTt2C` (Duplicate): `CLTt2CodCar`
- `CLTt2D` (Duplicate): `CLTt2ColNroCar`

---

### 📌 CLTt3
- **Descrição:** Controle de Suspensão
- **Chave Primária:** `CLTt1Cod`, `CLTt2Seq`, `CLTt3Seq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CLTt1Cod` | `N/D` | - |
| `CLTt2Seq` | `N/D` | - |
| `CLTt2NomDep` | `N/D` | - |
| `CLTt1NomTit` | `N/D` | - |
| `CLTt2DtaFinSus` | `N/D` | - |
| `CLTt2DtaIniSus` | `N/D` | - |
| `CLTt2Sts` | `N/D` | - |
| `CLTt2Loc` | `N/D` | - |
| `CLTt2BarCnt` | `N/D` | - |
| `CLTt2Tip` | `N/D` | - |
| `CLTt3Seq` | `N/D` | - |
| `CLTt3DtaIni` | `N/D` | - |
| `CLTt3DtaFin` | `N/D` | - |
| `CLTt3Mot1` | `N/D` | - |
| `CLTt3Mot2` | `N/D` | - |

#### 🗺️ Índices
- `CLTt3A` (Unique): `CLTt1Cod`, `CLTt2Seq`, `CLTt3Seq`
- `CLTt3B` (Duplicate): `CLTt1Cod`, `CLTt2Seq`

---

### 📌 CMAgA
- **Descrição:** Agendamento Alterações por Usuário
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMAgeUsu`, `CMAgeDta`, `CMAgeHra`, `CMAgeDtHrA`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMAgeUsu` | `N/D` | - |
| `CMAgeDta` | `N/D` | - |
| `CMAgeHra` | `N/D` | - |
| `CMAgeTit` | `N/D` | - |
| `CMAgeTex` | `N/D` | - |
| `CMAgeObs1` | `N/D` | - |
| `CMAgeObs2` | `N/D` | - |
| `CMAgeObs3` | `N/D` | - |
| `CMAgeObs4` | `N/D` | - |
| `CMAgeObs5` | `N/D` | - |
| `CMAgeCDta` | `N/D` | - |
| `CMAgeCHor` | `N/D` | - |
| `CMAgeCPrg` | `N/D` | - |
| `CMAgeCUsu` | `N/D` | - |
| `CMAgeFlg` | `N/D` | - |
| `CMAgeCliCod` | `N/D` | - |
| `CMAgeCliDes` | `N/D` | - |
| `CMAgeCon` | `N/D` | - |
| `CMAgeTip` | `N/D` | - |
| `CMAgeFlgD` | `N/D` | - |
| `CMAgeQReag` | `N/D` | - |
| `CMAgeCPF` | `N/D` | - |
| `CMAgeProfi` | `N/D` | - |
| `CMAgeTel1` | `N/D` | - |
| `CMAgeTel2` | `N/D` | - |
| `CMAgeObsM1` | `N/D` | - |
| `CMAgeObsM2` | `N/D` | - |
| `CMAgeObsM3` | `N/D` | - |
| `CMAgeNomM` | `N/D` | - |
| `CMAgeDtHrA` | `N/D` | - |
| `CMAgeProA` | `N/D` | - |
| `CMAgeUsuA` | `N/D` | - |
| `CMAgACliCod` | `N/D` | - |
| `CMAgACliDes` | `N/D` | - |

#### 🗺️ Índices
- `CMAgA1` (Unique): `CMEmpCod`, `CMFilCod`, `CMAgeUsu`, `CMAgeDta`, `CMAgeHra`, `CMAgeDtHrA`
- `CMAgA2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMAgeUsu`, `CMAgeDta`, `CMAgeHra`

---

### 📌 CMAge
- **Descrição:** Agenda de Compromissos
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMAgeUsu`, `CMAgeDta`, `CMAgeHra`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMAgeUsu` | `N/D` | - |
| `CMAgeDta` | `N/D` | - |
| `CMAgeHra` | `N/D` | - |
| `CMAgeTit` | `N/D` | - |
| `CMAgeHraFin` | `N/D` | - |
| `CMAgeDtaME` | `N/D` | - |
| `CMAgeSeqME` | `N/D` | - |
| `CMAgeTex` | `N/D` | - |
| `CMAgeObs1` | `N/D` | - |
| `CMAgeObs2` | `N/D` | - |
| `CMAgeObs3` | `N/D` | - |
| `CMAgeObs4` | `N/D` | - |
| `CMAgeObs5` | `N/D` | - |
| `CMAgeCDta` | `N/D` | - |
| `CMAgeCHor` | `N/D` | - |
| `CMAgeCPrg` | `N/D` | - |
| `CMAgeCUsu` | `N/D` | - |
| `CMAgeFlg` | `N/D` | - |
| `CMAgeCliCod` | `N/D` | - |
| `CMAgeCliDes` | `N/D` | - |
| `CMAgeCon` | `N/D` | - |
| `CMAgeTip` | `N/D` | - |
| `CMAgeTotHor` | `N/D` | - |
| `CMAgeVlrTot` | `N/D` | - |
| `CMAgeIte` | `N/D` | - |
| `CmAgeTotIte` | `N/D` | - |
| `CMAgeTotQtd` | `N/D` | - |
| `CMAgeDesPac` | `N/D` | - |
| `CMAgeDtaNscPac` | `N/D` | - |
| `CMAgeDtaDepNsc` | `N/D` | - |
| `CMAgeCPFDep` | `N/D` | - |
| `CMAgeFlgD` | `N/D` | - |
| `CMAgeQReag` | `N/D` | - |
| `CMAgeCPF` | `N/D` | - |
| `CMAgeProfi` | `N/D` | - |
| `CMAgeTel1` | `N/D` | - |
| `CMAgeTCad1` | `N/D` | - |
| `CMAgeTel2` | `N/D` | - |
| `CMAgeTCad2` | `N/D` | - |
| `CMAgeTel3` | `N/D` | - |
| `CMAgeTCad3` | `N/D` | - |
| `CMAgeTCadSpc` | `N/D` | - |
| `CMAgeTCadDtaNsc` | `N/D` | - |
| `CMAgeObsM1` | `N/D` | - |
| `CMAgeObsM2` | `N/D` | - |
| `CMAgeObsM3` | `N/D` | - |
| `CMAgeDataC` | `N/D` | - |
| `CMAgeHoraC` | `N/D` | - |
| `CMAgePrior` | `N/D` | - |
| `CMAgePMais` | `N/D` | - |
| `CMAgeDataF` | `N/D` | - |
| `CMAgeHoraF` | `N/D` | - |
| `CMAgeCRTip` | `N/D` | - |
| `CMAgeCRTiD` | `N/D` | - |
| `CMAgeCRTiV` | `N/D` | - |
| `CMAgeCaSUS` | `N/D` | - |
| `CMAgeNomM` | `N/D` | - |
| `CMAgeClSUS` | `N/D` | - |
| `CMAgeCodMo` | `N/D` | - |
| `CMAgeDesMo` | `N/D` | - |
| `CMAgenConf` | `N/D` | - |
| `CMAgenConD` | `N/D` | - |
| `CMAgeCRM` | `N/D` | - |
| `CMAgeMReag` | `N/D` | - |
| `CMAgeOReag` | `N/D` | - |
| `CMAgeDesis` | `N/D` | - |
| `CMAgeDesiM` | `N/D` | - |
| `CMAgeDataD` | `N/D` | - |
| `CMAgeHoraD` | `N/D` | - |
| `CMAgeVrUCo` | `N/D` | - |
| `CMAgeVend` | `N/D` | - |
| `CMAgeUConf` | `N/D` | - |
| `CMAgeUsuInc` | `N/D` | - |
| `CMAgeUsuReag` | `N/D` | - |
| `CMAgeDtaFixLis` | `N/D` | - |
| `CMAgeMedPron` | `N/D` | - |
| `CMAgeIdx` | `N/D` | - |
| `CMAgeQtdGuia` | `N/D` | - |
| `CMAgeNroPr` | `N/D` | - |
| `CMAgeChvReag` | `N/D` | - |
| `CMAgeQueixa` | `N/D` | - |
| `CMAgeVlrPrc` | `N/D` | - |
| `CMAgeDataA` | `N/D` | - |
| `CMAgeHoraA` | `N/D` | - |
| `CMAgeUsuaA` | `N/D` | - |
| `CMAgeTitDep` | `N/D` | - |
| `CMAgeDataR` | `N/D` | - |
| `CMAgeHoraR` | `N/D` | - |
| `CMAgeUsuaR` | `N/D` | - |
| `CMAgeSts` | `N/D` | - |
| `CMAgeVda` | `N/D` | - |
| `CMAgeObsR1` | `N/D` | - |
| `CMAgeObsR2` | `N/D` | - |
| `CMAgeObsR3` | `N/D` | - |
| `CMAgeSin01` | `N/D` | - |
| `CMAgeSin02` | `N/D` | - |
| `CMAgeSin03` | `N/D` | - |
| `CMAgeSin04` | `N/D` | - |
| `CMAgeSin05` | `N/D` | - |
| `CMAgeSin06` | `N/D` | - |
| `CMAgeSin07` | `N/D` | - |
| `CMAgeSin08` | `N/D` | - |
| `CMAgeSin09` | `N/D` | - |
| `CMAgeSadtR` | `N/D` | - |
| `CMAgeSadtP` | `N/D` | - |
| `CMAgeVrCon` | `N/D` | - |
| `CMAgeVrMed` | `N/D` | - |
| `CMAgeVrCli` | `N/D` | - |
| `CMAgeVrDes` | `N/D` | - |
| `CMAgeSeqMo` | `N/D` | - |
| `CMAgeRegUsu` | `N/D` | - |
| `CMAgeDtaHra` | `N/D` | - |
| `CMAgeAnxPrt` | `N/D` | - |
| `CMAgePro01` | `N/D` | - |
| `CMAgePro02` | `N/D` | - |
| `CMAgePro03` | `N/D` | - |
| `CMAgePro04` | `N/D` | - |
| `CMAgePro05` | `N/D` | - |
| `CMAgePro06` | `N/D` | - |
| `CMAgePro07` | `N/D` | - |
| `CMAgePro08` | `N/D` | - |
| `CMAgePro09` | `N/D` | - |
| `CMAgePro10` | `N/D` | - |
| `CMAgeCol01` | `N/D` | - |
| `CMAgeCol02` | `N/D` | - |
| `CMAgeCol03` | `N/D` | - |
| `CMAgeCol04` | `N/D` | - |
| `CMAgeCol05` | `N/D` | - |
| `CMAgeCol06` | `N/D` | - |
| `CMAgeCol07` | `N/D` | - |
| `CMAgeCol08` | `N/D` | - |
| `CMAgeCol09` | `N/D` | - |
| `CMAgeCol10` | `N/D` | - |
| `CMAgeExa01` | `N/D` | - |
| `CMAgeExa02` | `N/D` | - |
| `CMAgeExa03` | `N/D` | - |
| `CMAgeExa04` | `N/D` | - |
| `CMAgeExa05` | `N/D` | - |
| `CMAgeExa06` | `N/D` | - |
| `CMAgeExa07` | `N/D` | - |
| `CMAgeExa08` | `N/D` | - |
| `CMAgeExa09` | `N/D` | - |
| `CMAgeExa10` | `N/D` | - |
| `CMAgeODL01` | `N/D` | - |
| `CMAgeODL02` | `N/D` | - |
| `CMAgeODL03` | `N/D` | - |
| `CMAgeODL04` | `N/D` | - |
| `CMAgeOEL01` | `N/D` | - |
| `CMAgeOEL02` | `N/D` | - |
| `CMAgeOEL03` | `N/D` | - |
| `CMAgeOEL04` | `N/D` | - |
| `CMAgeODP01` | `N/D` | - |
| `CMAgeODP02` | `N/D` | - |
| `CMAgeODP03` | `N/D` | - |
| `CMAgeODP04` | `N/D` | - |
| `CMAgeOEP01` | `N/D` | - |
| `CMAgeOEP02` | `N/D` | - |
| `CMAgeOEP03` | `N/D` | - |
| `CMAgeOEP04` | `N/D` | - |
| `CMAgeAdc` | `N/D` | - |
| `CMAgePre01` | `N/D` | - |
| `CMAgePre02` | `N/D` | - |
| `CMAgeAP` | `N/D` | - |
| `CMAgeTOD01` | `N/D` | - |
| `CMAgeTOD02` | `N/D` | - |
| `CMAgeTOD03` | `N/D` | - |
| `CMAgeTOD04` | `N/D` | - |
| `CMAgeTOD09` | `N/D` | - |
| `CMAgeTOD10` | `N/D` | - |
| `CMAgeTOD11` | `N/D` | - |
| `CMAgeTOD12` | `N/D` | - |
| `CMAgeTOD13` | `N/D` | - |
| `CMAgeTOD14` | `N/D` | - |
| `CMAgeTOD15` | `N/D` | - |
| `CMAgeTOD16` | `N/D` | - |
| `CMAgeTOD17` | `N/D` | - |
| `CMAgeTOD18` | `N/D` | - |
| `CMAgeTOD19` | `N/D` | - |
| `CMAgeTOD20` | `N/D` | - |
| `CMAgeTOD21` | `N/D` | - |
| `CMAgeTOD22` | `N/D` | - |
| `CMAgeTOD23` | `N/D` | - |
| `CMAgeTOD24` | `N/D` | - |
| `CMAgeTOE01` | `N/D` | - |
| `CMAgeTOE02` | `N/D` | - |
| `CMAgeTOE03` | `N/D` | - |
| `CMAgeTOE04` | `N/D` | - |
| `CMAgeTOE09` | `N/D` | - |
| `CMAgeTOE10` | `N/D` | - |
| `CMAgeTOE11` | `N/D` | - |
| `CMAgeTOE12` | `N/D` | - |
| `CMAgeTOE13` | `N/D` | - |
| `CMAgeTOE14` | `N/D` | - |
| `CMAgeTOE15` | `N/D` | - |
| `CMAgeTOE16` | `N/D` | - |
| `CMAgeTOE17` | `N/D` | - |
| `CMAgeTOE18` | `N/D` | - |
| `CMAgeTOE19` | `N/D` | - |
| `CMAgeTOE20` | `N/D` | - |
| `CMAgeTOE21` | `N/D` | - |
| `CMAgeTOE22` | `N/D` | - |
| `CMAgeTOE23` | `N/D` | - |
| `CMAgeTOE24` | `N/D` | - |
| `CMAgeNec01` | `N/D` | - |
| `CMAgeNec02` | `N/D` | - |
| `CMAgeNec03` | `N/D` | - |
| `CMAgeNec04` | `N/D` | - |
| `CMAgeNec05` | `N/D` | - |
| `CMAgeNec06` | `N/D` | - |
| `CMAgeNec07` | `N/D` | - |
| `CMAgeNec08` | `N/D` | - |
| `CMAgeNec09` | `N/D` | - |
| `CMAgeAPA15` | `N/D` | - |
| `CMAgeAPA16` | `N/D` | - |
| `CMAgeAPA17` | `N/D` | - |
| `CMAgeAPA18` | `N/D` | - |
| `CMAgeAPA19` | `N/D` | - |
| `CMAgeAPA20` | `N/D` | - |
| `CMAgeAPA21` | `N/D` | - |
| `CMAgeAPA22` | `N/D` | - |
| `CMAgeAPA23` | `N/D` | - |
| `CMAgeAPA24` | `N/D` | - |
| `CMAgeAPA25` | `N/D` | - |
| `CMAgeAPA26` | `N/D` | - |
| `CMAgeAPA27` | `N/D` | - |
| `CMAgeAPA28` | `N/D` | - |
| `CMAgeAPA29` | `N/D` | - |
| `CMAgeAPA30` | `N/D` | - |
| `CMAgeAPA31` | `N/D` | - |
| `CMAgeAPA32` | `N/D` | - |
| `CMAgeAPA33` | `N/D` | - |
| `CMAgeAPA34` | `N/D` | - |
| `CMAgeAPA35` | `N/D` | - |
| `CMAgeAPA36` | `N/D` | - |
| `CMAgeO1A37` | `N/D` | - |
| `CMAgeO2A37` | `N/D` | - |
| `CMAgeO3A37` | `N/D` | - |
| `CMAgeO4A37` | `N/D` | - |
| `CMAgeAPA39` | `N/D` | - |

#### 🗺️ Índices
- `CMAge1` (Unique): `CMEmpCod`, `CMFilCod`, `CMAgeUsu`, `CMAgeDta`, `CMAgeHra`
- `CMAge2` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CMAge3` (Duplicate): `CMAgeUsu`, `CMAgeDta`, `CMAgeHra`
- `CMAge4` (Duplicate): `CMAgeDta`, `CMAgeHra`
- `CMAge5` (Duplicate): `CMAgeUsu`, `CMAgePrior`
- `CMAge6` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMAgeDataF`, `CMAgeSeqMo`
- `CMAge7` (Duplicate): `CMAgeCRTip`, `CMAgeCliCod`, `CMAgeDataF`
- `CMAge8` (Duplicate): `CMAgeCliCod`, `CMAgeDta`
- `CMAge9` (Duplicate): `CMEmpCod`, `CMAgeCodMo`

---

### 📌 CMAgP
- **Descrição:** Produtos da Agenda de Compromisso
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMAgeUsu`, `CMAgeDta`, `CMAgeHra`, `CMAgPIte`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMAgeUsu` | `N/D` | - |
| `CMAgeDta` | `N/D` | - |
| `CMAgeHra` | `N/D` | - |
| `CMAgeTit` | `N/D` | - |
| `CMAgeCliCod` | `N/D` | - |
| `CMAgeCliDes` | `N/D` | - |
| `CMAgeVlrTot` | `N/D` | - |
| `CMAgeIte` | `N/D` | - |
| `CmAgeTotIte` | `N/D` | - |
| `CMAgeTotQtd` | `N/D` | - |
| `CMAgPIte` | `N/D` | - |
| `CMAgPCodCha` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CEProPre1Tab` | `N/D` | - |
| `CMAgPQtd` | `N/D` | - |
| `CMAgPVlrUnt` | `N/D` | - |
| `CMAgPVlrTot` | `N/D` | - |
| `CMAgPObs` | `N/D` | - |

#### 🗺️ Índices
- `CMAgP1` (Unique): `CMEmpCod`, `CMFilCod`, `CMAgeUsu`, `CMAgeDta`, `CMAgeHra`, `CMAgPIte`
- `CMAgP2` (Duplicate): `CMEmpCod`, `CEProCod`
- `CMAgP3` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMAgeUsu`, `CMAgeDta`, `CMAgeHra`

---

### 📌 CMAgx
- **Descrição:** Atendimento - Exames
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMAgeUsu`, `CMAgeDta`, `CMAgeHra`, `CMAgxSeqEx`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMAgeUsu` | `N/D` | - |
| `CMAgeDta` | `N/D` | - |
| `CMAgeHra` | `N/D` | - |
| `CMAgxSeqEx` | `N/D` | - |
| `CMAgxCodEx` | `N/D` | - |
| `CMAgxDesEx` | `N/D` | - |
| `CMAgxFCod` | `N/D` | - |
| `CMAgxFDes` | `N/D` | - |
| `CMAgxCusto` | `N/D` | - |
| `CMAgxVenda` | `N/D` | - |
| `CMAgxDtaME` | `N/D` | - |
| `CMAgxSeqME` | `N/D` | - |

#### 🗺️ Índices
- `CMAgx1` (Unique): `CMEmpCod`, `CMFilCod`, `CMAgeUsu`, `CMAgeDta`, `CMAgeHra`, `CMAgxSeqEx`
- `CMAgx2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMAgeUsu`, `CMAgeDta`, `CMAgeHra`
- `CMAgx3` (Duplicate): `CMAgxFCod`

---

### 📌 CMAno
- **Descrição:** Totais Ano\Mes - Tipo de Combustível
- **Chave Primária:** `CMEmpCod`, `CMAnoOrg`, `CMAnoFil`, `CMAnoAno`, `CMAnoChv1`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMAnoOrg` | `N/D` | - |
| `CMAnoFil` | `N/D` | - |
| `CMAnoAno` | `N/D` | - |
| `CMAnoChv1` | `N/D` | - |
| `CMAnoQtd1` | `N/D` | - |
| `CMAnoQtd2` | `N/D` | - |
| `CMAnoQtd3` | `N/D` | - |
| `CMAnoQtd4` | `N/D` | - |
| `CMAnoQtd5` | `N/D` | - |
| `CMAnoAno1` | `N/D` | - |
| `CMAnoAno2` | `N/D` | - |
| `CMAnoAno3` | `N/D` | - |
| `CMAnoAno4` | `N/D` | - |
| `CMAnoAno5` | `N/D` | - |
| `CMAnoVlr1` | `N/D` | - |
| `CMAnoVlr2` | `N/D` | - |
| `CMAnoVlr3` | `N/D` | - |
| `CMAnoVlr4` | `N/D` | - |
| `CMAnoVlr5` | `N/D` | - |
| `CMAnoVlr6` | `N/D` | - |
| `CMAnoVlr7` | `N/D` | - |
| `CMAnoVlr8` | `N/D` | - |
| `CMAnoVlr9` | `N/D` | - |
| `CMAnoQ11A` | `N/D` | - |
| `CMAnoQ12A` | `N/D` | - |
| `CMAnoQ13A` | `N/D` | - |
| `CMAnoQ14A` | `N/D` | - |
| `CMAnoQ15A` | `N/D` | - |
| `CMAnoDQ11A` | `N/D` | - |
| `CMAnoDQ12A` | `N/D` | - |
| `CMAnoDQ13A` | `N/D` | - |
| `CMAnoDQ14A` | `N/D` | - |
| `CMAnoDQ15A` | `N/D` | - |
| `CMAnoPQ11A` | `N/D` | - |
| `CMAnoPQ12A` | `N/D` | - |
| `CMAnoPQ13A` | `N/D` | - |
| `CMAnoPQ14A` | `N/D` | - |
| `CMAnoPQ15A` | `N/D` | - |
| `CMAnoDes1` | `N/D` | - |
| `CMAnoDes2` | `N/D` | - |
| `CMAnoDes3` | `N/D` | - |
| `CMAnoDes4` | `N/D` | - |
| `CMAnoQA000` | `N/D` | - |
| `CMAnoQA100` | `N/D` | - |
| `CMAnoQA120` | `N/D` | - |
| `CmAnoQA103` | `N/D` | - |
| `CMAnoQA003` | `N/D` | - |

#### 🗺️ Índices
- `CMAno1` (Unique): `CMEmpCod`, `CMAnoOrg`, `CMAnoFil`, `CMAnoAno`, `CMAnoChv1`
- `CMAno2` (Duplicate): `CMEmpCod`

---

### 📌 CMAud
- **Descrição:** Auditoria
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMAudCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMAudCod` | `N/D` | - |
| `CMAudUsu` | `N/D` | - |
| `CMAudDtaHor` | `N/D` | - |
| `CMAudPrg` | `N/D` | - |
| `CMAudDes1` | `N/D` | - |
| `CMAudDes2` | `N/D` | - |
| `CMAudDes3` | `N/D` | - |
| `CMAudMovDta` | `N/D` | - |
| `CMAudMovSeq` | `N/D` | - |
| `CMAudCliCod` | `N/D` | - |
| `CMAudDtaMov` | `N/D` | - |
| `CMAudOrg` | `N/D` | - |
| `CMAudVlrCus` | `N/D` | - |
| `CMAudVlrVda` | `N/D` | - |
| `CMAudQtdInv` | `N/D` | - |

#### 🗺️ Índices
- `CMAud1` (Unique): `CMEmpCod`, `CMFilCod`, `CMAudCod`
- `CMAud2` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CMAud3` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMAudCod`
- `CMAud4` (Duplicate): `CMAudMovDta`, `CMAudMovSeq`
- `CMAud5` (Duplicate): `CMAudCliCod`
- `CMAud6` (Duplicate): `CMAudDtaMov`

---

### 📌 CMAut
- **Descrição:** Controle Autoridade - Usuários x Programa
- **Chave Primária:** `CMEmpCod`, `CMAutFil`, `CMAutUsu`, `CMAutPrg`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMAutFil` | `N/D` | - |
| `CMAutUsu` | `N/D` | - |
| `CMAutPrg` | `N/D` | - |
| `CMAutNiv` | `N/D` | - |
| `CMAutChcAut` | `N/D` | - |

#### 🗺️ Índices
- `CMAutA` (Unique): `CMEmpCod`, `CMAutFil`, `CMAutUsu`, `CMAutPrg`
- `CMAutB` (Duplicate): `CMEmpCod`
- `CMAutC` (Duplicate): `CMEmpCod`, `CMAutUsu`, `CMAutPrg`, `CMAutFil`
- `CMAutD` (Duplicate): `CMAutPrg`

---

### 📌 CMBen
- **Descrição:** Cadastro Código Beneficio Por Estado
- **Chave Primária:** `CMUFCod`, `CMBenCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMUFCod` | `N/D` | - |
| `CMUFDes` | `N/D` | - |
| `CMBenCod` | `N/D` | - |
| `CMBenDes` | `N/D` | - |
| `CMBenASN` | `N/D` | - |
| `CMBenCST00` | `N/D` | - |
| `CMBenCST10` | `N/D` | - |
| `CMBenCST20` | `N/D` | - |
| `CMBenCST30` | `N/D` | - |
| `CMBenCST40` | `N/D` | - |
| `CMBenCST41` | `N/D` | - |
| `CMBenCST50` | `N/D` | - |
| `CMBenCST51` | `N/D` | - |
| `CMBenCST60` | `N/D` | - |
| `CMBenCST61` | `N/D` | - |
| `CMBenCST70` | `N/D` | - |
| `CMBenCST90` | `N/D` | - |

#### 🗺️ Índices
- `CMBenA` (Unique): `CMUFCod`, `CMBenCod`
- `CMBenB` (Duplicate): `CMUFCod`

---

### 📌 CMCA1
- **Descrição:** Curva ABC Cabeçalho
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMCA1Usu`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMCA1Usu` | `N/D` | - |
| `CMCA1TST` | `N/D` | - |
| `CMCA1DtaIni` | `N/D` | - |
| `CMCA1DtaFin` | `N/D` | - |
| `CMCA1QtdDia` | `N/D` | - |
| `CMCA1Luc` | `N/D` | - |
| `CMCA1Vda` | `N/D` | - |
| `CMCA1PA` | `N/D` | - |
| `CMCA1PB` | `N/D` | - |
| `CMCA1PC` | `N/D` | - |
| `CMCA1Qtd` | `N/D` | - |
| `CMCA1TIt` | `N/D` | - |
| `CMCA1QtdMes` | `N/D` | - |
| `CMCA1QtdAtu` | `N/D` | - |

#### 🗺️ Índices
- `CMCA1A` (Unique): `CMEmpCod`, `CMFilCod`, `CMCA1Usu`
- `CMCA1B` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CMCA2
- **Descrição:** Curva ABC - Produtos
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMCA1Usu`, `CMCA2Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMCA1Usu` | `N/D` | - |
| `CMCA1TST` | `N/D` | - |
| `CMCA1DtaIni` | `N/D` | - |
| `CMCA1DtaFin` | `N/D` | - |
| `CMCA1QtdDia` | `N/D` | - |
| `CMCA1Luc` | `N/D` | - |
| `CMCA1Vda` | `N/D` | - |
| `CMCA1PA` | `N/D` | - |
| `CMCA1PB` | `N/D` | - |
| `CMCA1PC` | `N/D` | - |
| `CMCA1Qtd` | `N/D` | - |
| `CMCA1TIt` | `N/D` | - |
| `CMCA1QtdMes` | `N/D` | - |
| `CMCA1QtdAtu` | `N/D` | - |
| `CMCA2Cod` | `N/D` | - |
| `CMCA2QtdAtu` | `N/D` | - |
| `CMCA2Des` | `N/D` | - |
| `CMCA2Qtd` | `N/D` | - |
| `CMCA2QtdDep` | `N/D` | - |
| `CMCA2Luc` | `N/D` | - |
| `CMCA2Vda` | `N/D` | - |
| `CMCA2MDi` | `N/D` | - |
| `CMCA2MMe` | `N/D` | - |
| `CMCA2QPo` | `N/D` | - |
| `CMCA2LPo` | `N/D` | - |
| `CMCA2VPo` | `N/D` | - |
| `CMCA2QAc` | `N/D` | - |
| `CMCA2VAc` | `N/D` | - |
| `CMCA2LAc` | `N/D` | - |
| `CMCA2QPr` | `N/D` | - |
| `CMCA2LPr` | `N/D` | - |
| `CMCA2VPr` | `N/D` | - |
| `CMCA2QCl` | `N/D` | - |
| `CMCA2LCl` | `N/D` | - |
| `CMCA2VCl` | `N/D` | - |
| `CMCA2QPA` | `N/D` | - |
| `CMCA2QPB` | `N/D` | - |
| `CMCA2QPC` | `N/D` | - |
| `CMCA2LPA` | `N/D` | - |
| `CMCA2LPB` | `N/D` | - |
| `CMCA2LPC` | `N/D` | - |
| `CMCA2VPA` | `N/D` | - |
| `CMCA2VPB` | `N/D` | - |
| `CMCA2VQC` | `N/D` | - |
| `CMCA2DUC` | `N/D` | - |
| `CMCA2DUV` | `N/D` | - |
| `CMCA2QUC` | `N/D` | - |
| `CMCA2IDX` | `N/D` | - |
| `CMCA2FAB` | `N/D` | - |
| `CMCA2Nro` | `N/D` | - |
| `CMCA2Cor` | `N/D` | - |
| `CMCA2PreCus` | `N/D` | - |
| `CMCA2PreTab` | `N/D` | - |
| `CMCA2MrgAtu` | `N/D` | - |
| `CMCA2MrgLuc` | `N/D` | - |
| `CMCA2DtaPro` | `N/D` | - |
| `CMCA2QtdCP` | `N/D` | - |
| `CMCA2VlrCP` | `N/D` | - |
| `CMCA2ForCod` | `N/D` | - |
| `CMCA2GrpCod` | `N/D` | - |
| `CMCA2SgrCod` | `N/D` | - |

#### 🗺️ Índices
- `CMCA2A` (Unique): `CMEmpCod`, `CMFilCod`, `CMCA1Usu`, `CMCA2Cod`
- `CMCA2B` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMCA1Usu`
- `CMCA2C` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMCA1Usu`, `CMCA2Qtd`
- `CMCA2D` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMCA1Usu`, `CMCA2Vda`
- `CMCA2E` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMCA1Usu`, `CMCA2Luc`
- `CMCA2F` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMCA1Usu`, `CMCA2IDX`

---

### 📌 CMCal1
- **Descrição:** Calculadora 1
- **Chave Primária:** `CMCal1CheOut`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMCal1CheOut` | `N/D` | - |
| `CMCal1Tot` | `N/D` | - |
| `CMCal1Obs` | `N/D` | - |
| `CMCal1Seq` | `N/D` | - |

#### 🗺️ Índices
- `CMCal1A` (Unique): `CMCal1CheOut`

---

### 📌 CMCal2
- **Descrição:**  Calculadora 2
- **Chave Primária:** `CMCal1CheOut`, `CMCal2Seq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMCal1CheOut` | `N/D` | - |
| `CMCal1Tot` | `N/D` | - |
| `CMCal1Obs` | `N/D` | - |
| `CMCal1Seq` | `N/D` | - |
| `CMCal2Seq` | `N/D` | - |
| `CMCal2Vlr` | `N/D` | - |

#### 🗺️ Índices
- `CMCal2A` (Unique): `CMCal1CheOut`, `CMCal2Seq`
- `CMCal2B` (Duplicate): `CMCal1CheOut`

---

### 📌 CMCCu
- **Descrição:** Centro de Custo
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMCCuCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMCCuCod` | `N/D` | - |
| `CMCCuDes` | `N/D` | - |
| `CMCCuCUsu` | `N/D` | - |
| `CMCCuCHor` | `N/D` | - |
| `CMCCuCDta` | `N/D` | - |
| `CMCCuCPrg` | `N/D` | - |
| `CMCCuDtaTrs` | `N/D` | - |
| `CMCCuFlaDel` | `N/D` | - |
| `CMCCuSomRat` | `N/D` | - |

#### 🗺️ Índices
- `CMCCu1` (Unique): `CMEmpCod`, `CMFilCod`, `CMCCuCod`
- `CMCCu2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CMCEP
- **Descrição:** C.E.P.
- **Chave Primária:** `CMCEPCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMCEPCod` | `N/D` | - |
| `CMUFCod` | `N/D` | - |
| `CMUFDes` | `N/D` | - |
| `CMCEPDes` | `N/D` | - |
| `CMCEPCUsu` | `N/D` | - |
| `CMCEPCHor` | `N/D` | - |
| `CMCEPCDta` | `N/D` | - |
| `CMCEPCPrg` | `N/D` | - |
| `CMCEPDtaTrs` | `N/D` | - |
| `CMCEPFlaDel` | `N/D` | - |
| `CMCEPDesCom` | `N/D` | - |
| `CMCEPIBGE` | `N/D` | - |

#### 🗺️ Índices
- `CMCEPA` (Unique): `CMCEPCod`
- `CMCEPB` (Duplicate): `CMUFCod`
- `CMCEPC` (Duplicate): `CMCEPDes`

---

### 📌 cmcepl
- **Descrição:** cmcepl
- **Chave Primária:** `CmCepLCod`, `CmCepLLog`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CmCepLCod` | `N/D` | - |
| `CmCepLLog` | `N/D` | - |
| `CmCepLDes` | `N/D` | - |
| `CmCepLBai` | `N/D` | - |
| `CmCepLCid` | `N/D` | - |
| `CmCepLUf` | `N/D` | - |
| `CmCepLPat` | `N/D` | - |

#### 🗺️ Índices
- `CMCEPLA` (Unique): `CmCepLCod`, `CmCepLLog`
- `CMCEPLB` (Duplicate): `CmCepLCid`, `CmCepLDes`

---

### 📌 CMCTe1
- **Descrição:** Cadastro Telefone 01
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMCTe1Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMCTe1Cod` | `N/D` | - |
| `CMCTe1Nom` | `N/D` | - |
| `CMCTe1DtaNsc` | `N/D` | - |
| `CMCTe1DiaNsc` | `N/D` | - |
| `CMCTe1Ida` | `N/D` | - |
| `CMCTe1MesNsc` | `N/D` | - |
| `CMCTe1PrxCod2` | `N/D` | - |
| `CMCTe1EmiRel` | `N/D` | - |

#### 🗺️ Índices
- `CMCTe11` (Unique): `CMEmpCod`, `CMFilCod`, `CMCTe1Cod`
- `CMCTe12` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CMCTe13` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMCTe1Nom`
- `CMCTe14` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMCTe1DiaNsc`, `CMCTe1MesNsc`

---

### 📌 CMCTe2
- **Descrição:** Cadastro Telefone 02
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMCTe1Cod`, `CMCTe2Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMCTe1Cod` | `N/D` | - |
| `CMCTe1Nom` | `N/D` | - |
| `CMCTe1DtaNsc` | `N/D` | - |
| `CMCTe1DiaNsc` | `N/D` | - |
| `CMCTe1Ida` | `N/D` | - |
| `CMCTe1MesNsc` | `N/D` | - |
| `CMCTe1PrxCod2` | `N/D` | - |
| `CMCTe1EmiRel` | `N/D` | - |
| `CMCTe2Cod` | `N/D` | - |
| `CMCTe2Prf` | `N/D` | - |
| `CMCTe2Nro` | `N/D` | - |
| `CMCTe2Des` | `N/D` | - |
| `CMCTe2End` | `N/D` | - |
| `CMCTe2Eml` | `N/D` | - |

#### 🗺️ Índices
- `CMCTe21` (Unique): `CMEmpCod`, `CMFilCod`, `CMCTe1Cod`, `CMCTe2Cod`
- `CMCTe22` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMCTe1Cod`
- `CMCTe23` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMCTe2Nro`

---

### 📌 CMCV1
- **Descrição:** Conversão de Arquivos
- **Chave Primária:** `CMCV1TAB`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMCV1TAB` | `N/D` | - |
| `CMCV1PLA` | `N/D` | - |
| `CMCV1Nom` | `N/D` | - |

#### 🗺️ Índices
- `CMCV1A` (Unique): `CMCV1TAB`

---

### 📌 CMCV2
- **Descrição:** Conversão de Arquivos 2
- **Chave Primária:** `CMCV1TAB`, `CMCV2COD`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMCV1TAB` | `N/D` | - |
| `CMCV1PLA` | `N/D` | - |
| `CMCV1Nom` | `N/D` | - |
| `CMCV2COD` | `N/D` | - |
| `CMCV2DES` | `N/D` | - |
| `CMCV2Tip` | `N/D` | - |
| `CMCV2Tam` | `N/D` | - |
| `CMCV2Pos` | `N/D` | - |
| `CMCV2Def` | `N/D` | - |
| `CMCV2Idx` | `N/D` | - |
| `CMCV2Col` | `N/D` | - |

#### 🗺️ Índices
- `CMCV2A` (Unique): `CMCV1TAB`, `CMCV2COD`
- `CMCV2B` (Duplicate): `CMCV1TAB`

---

### 📌 CMCVG
- **Descrição:** Comissão do Vendedor por Grupo
- **Chave Primária:** `CMEmpCod`, `CMUsuNom`, `CMCVGGrpCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMUsuNom` | `N/D` | - |
| `CMCVGGrpCod` | `N/D` | - |
| `CMCVGGrpDes` | `N/D` | - |
| `CMCVGPerCom` | `N/D` | - |

#### 🗺️ Índices
- `CMCVG1` (Unique): `CMEmpCod`, `CMUsuNom`, `CMCVGGrpCod`
- `CMCVG2` (Duplicate): `CMEmpCod`, `CMUsuNom`

---

### 📌 CmEmp
- **Descrição:** Empresa
- **Chave Primária:** `CMEmpCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMEmpVlrMaoObr` | `N/D` | - |
| `CMEmpBckSai` | `N/D` | - |
| `CMEmpFlaDel` | `N/D` | - |
| `CMEmpDtaTrs` | `N/D` | - |
| `CMEmpBckEnt` | `N/D` | - |
| `CMEmpNomFan` | `N/D` | - |
| `CMEmpSisIde` | `N/D` | - |
| `CMEmpRazSoc` | `N/D` | - |
| `CMEmpEnd` | `N/D` | - |
| `CMEmpBai` | `N/D` | - |
| `CMEmpCep` | `N/D` | - |
| `CMEmpCid` | `N/D` | - |
| `CMEmpUF` | `N/D` | - |
| `CMEmpTel1` | `N/D` | - |
| `CMEmpTel2` | `N/D` | - |
| `CMEmpFax` | `N/D` | - |
| `CMEmpCgc` | `N/D` | - |
| `CMEmpInsEst` | `N/D` | - |
| `CMEmpJrsMes` | `N/D` | - |
| `CMEmpCUsu` | `N/D` | - |
| `CMEmpCHor` | `N/D` | - |
| `CMEmpCDta` | `N/D` | - |
| `CMEmpCPrg` | `N/D` | - |
| `CMEmpSeg` | `N/D` | - |
| `CMEmpCCDtaVal` | `N/D` | - |
| `CMEmpCEPrxPro` | `N/D` | - |
| `CMEmpCFPrxFun` | `N/D` | - |
| `CMEmpCFDta` | `N/D` | - |
| `CMEmpCF1VDDPM` | `N/D` | - |
| `CMEmpCF2VDSS` | `N/D` | - |
| `CMEmpCFVDSM` | `N/D` | - |
| `CMEmpCFVDDMA` | `N/D` | - |
| `CMEmpCP1PrxTipCod` | `N/D` | - |
| `CMEmpCR1PrxTipCod` | `N/D` | - |
| `CMEmpDSDta` | `N/D` | - |
| `CMEmpTemp1` | `N/D` | - |
| `CMEmpCarDes` | `N/D` | - |
| `CMEmpCarJrs` | `N/D` | - |
| `CMEmpDesMes` | `N/D` | - |
| `CMEmpDesVdaVis` | `N/D` | - |
| `CMEmpCEQtdPar` | `N/D` | - |
| `CMEmpCEMrgLuc` | `N/D` | - |
| `CMEmpCRNroRec` | `N/D` | - |
| `CMEmpDtaDia` | `N/D` | - |
| `CMEmpJrsMorMes` | `N/D` | - |
| `CMEmpDtaUltAce` | `N/D` | - |
| `CMEmpMSI` | `N/D` | - |
| `CMEmpProIni` | `N/D` | - |
| `CMEmpSQL` | `N/D` | - |
| `CMEmpVerSis` | `N/D` | - |
| `CMEmpWatUp` | `N/D` | - |
| `CMEmpTstUltDll` | `N/D` | - |
| `CMEmpUltEnvFat` | `N/D` | - |
| `CMEmpMoeCodPad` | `N/D` | - |
| `CMEmpDtaAtuCST` | `N/D` | - |
| `CMEmpBenDtaAtu` | `N/D` | - |
| `CMEmpTokSupTEF` | `N/D` | - |
| `CMEmpCEUsaGrpSgr` | `N/D` | - |
| `CMEmpCRArrCenVda` | `N/D` | - |
| `CMEmpCRComVdaPar` | `N/D` | - |
| `CMEmpCRVenCod` | `N/D` | - |
| `CMEmpUsaPerComFix` | `N/D` | - |
| `CMEmpCRParVdaCre` | `N/D` | - |
| `CMEmpCRUsaCom` | `N/D` | - |
| `CMEmpUsa_MaiUmaFil` | `N/D` | - |
| `CMEmpDtaComPar` | `N/D` | - |
| `CMEmpComCom` | `N/D` | - |
| `CMEMPReorg` | `N/D` | - |
| `CMEMPReAdd` | `N/D` | - |
| `CMEmpTstExe` | `N/D` | - |
| `CMEmpTstPri` | `N/D` | - |
| `CMEmpAPIUsa` | `N/D` | - |
| `CMEmpAPIBlq` | `N/D` | - |
| `CMEmpAPIDtaUltCom` | `N/D` | - |
| `CMEmpCxFecDif` | `N/D` | - |
| `CMEmpCECusMed` | `N/D` | - |
| `CMEmpCodBar_CodPro` | `N/D` | - |
| `CMEmpCPPreVda` | `N/D` | - |
| `CMEmpCRPerAltVdaDepTrc` | `N/D` | - |
| `CMEmpMoeDesPad` | `N/D` | - |
| `CMEmpBaiParDtaRet` | `N/D` | - |
| `CMEmpUsa_CCu` | `N/D` | - |
| `CMEmpUsaSenVdaBxa` | `N/D` | - |
| `CMEmpFazFecMes` | `N/D` | - |
| `CMEmpCR1TCR01B` | `N/D` | - |
| `CMEmpCE_PrxAgr` | `N/D` | - |
| `CMEmpCR2TCR01C` | `N/D` | - |
| `CMEmpCRSenVdaDscSup` | `N/D` | - |
| `CMEmpCRPrcDscBaiPar` | `N/D` | - |
| `CMEmpAcuMovEst` | `N/D` | - |
| `CMEmpCodEan` | `N/D` | - |
| `CMEmpEanQdoGerAut` | `N/D` | - |
| `CMEmpGerCodBarAut` | `N/D` | - |
| `CMEmpConQtdPecPro` | `N/D` | - |
| `CMEmpCntAutCodDsp` | `N/D` | - |
| `CMEmpLctVndSenVda` | `N/D` | - |
| `CMEmpCusUtl` | `N/D` | - |
| `CMEmpAbrTelTrs` | `N/D` | - |
| `CMEmpGruImo` | `N/D` | - |
| `CMEmpSenCanVda` | `N/D` | - |
| `CmEmpAtuTabPre` | `N/D` | - |
| `CMEmpAltPreVdaEst` | `N/D` | - |
| `CMEmpCPUsaProTmp` | `N/D` | - |
| `CMEmpQtdDiaVolDta` | `N/D` | - |
| `CMEmpPrzMedGrp` | `N/D` | - |
| `CMEmpCECadMic` | `N/D` | - |
| `CMEmpCEAtuCusAgr` | `N/D` | - |
| `CMEmpTS` | `N/D` | - |
| `CMEmpBOF` | `N/D` | - |
| `CMEmpPerPadIcm` | `N/D` | - |
| `CMEmpRef` | `N/D` | - |
| `CMEmpModEtqGon` | `N/D` | - |
| `CMEmpCEVct` | `N/D` | - |
| `CMEmpPth1MS` | `N/D` | - |
| `CMEmpPth2MS` | `N/D` | - |
| `CMEmpSenSupPreMen` | `N/D` | - |
| `CMEmpCPLctPro` | `N/D` | - |
| `CMEmpDscVdaCan` | `N/D` | - |
| `CMEmpCRAleDscVda` | `N/D` | - |
| `CMEmpInfLimCre` | `N/D` | - |
| `CMEmpExiFicComCli` | `N/D` | - |
| `CMEmpCliObr` | `N/D` | - |
| `CMEmpCRPrxCli` | `N/D` | - |
| `CMEmpPrxTelCE` | `N/D` | - |
| `CMEmpPAg` | `N/D` | - |
| `CMEmpDes1Tab` | `N/D` | - |
| `CMEmpDes2Tab` | `N/D` | - |
| `CMEmpDes3Tab` | `N/D` | - |
| `CMEmpDes4Tab` | `N/D` | - |
| `CMEmpGrd` | `N/D` | - |
| `CMEmpDec` | `N/D` | - |
| `CMEmpCRDscExc` | `N/D` | - |
| `CMEmpDspSet` | `N/D` | - |
| `CMEmpFecCnvFil` | `N/D` | - |
| `CMEmpPrc1` | `N/D` | - |
| `CMEmpPrc2` | `N/D` | - |

#### 🗺️ Índices
- `CmEmp1` (Unique): `CMEmpCod`
- `CMEmp2` (Duplicate): `CMEmpMoeCodPad`

---

### 📌 CMExA
- **Descrição:** Cadastro de Exames
- **Chave Primária:** `CMEmpCod`, `CMExACod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMExACod` | `N/D` | - |
| `CMExADes` | `N/D` | - |
| `CMExAVenda` | `N/D` | - |
| `CMExAVda2` | `N/D` | - |
| `CMExaFlg` | `N/D` | - |
| `CMExProCod` | `N/D` | - |
| `CMExProDes` | `N/D` | - |

#### 🗺️ Índices
- `CMExA1` (Unique): `CMEmpCod`, `CMExACod`
- `CMExA2` (Duplicate): `CMEmpCod`

---

### 📌 CMExF
- **Descrição:**  T509
- **Chave Primária:** `CMEmpCod`, `CMExACod`, `CMExFCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMExACod` | `N/D` | - |
| `CMExADes` | `N/D` | - |
| `CMExAVenda` | `N/D` | - |
| `CMExAVda2` | `N/D` | - |
| `CMExaFlg` | `N/D` | - |
| `CMExProCod` | `N/D` | - |
| `CMExProDes` | `N/D` | - |
| `CMExFCod` | `N/D` | - |
| `CMExFDes` | `N/D` | - |
| `CMExFCusto` | `N/D` | - |

#### 🗺️ Índices
- `CMExFA` (Unique): `CMEmpCod`, `CMExACod`, `CMExFCod`
- `CMExFB` (Duplicate): `CMEmpCod`, `CMExACod`

---

### 📌 CMEXN
- **Descrição:** Tabela Código EAN (Código de Barras) X NCM
- **Chave Primária:** `CMEXNEAN`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEXNEAN` | `N/D` | - |
| `CMEXNNCM` | `N/D` | - |

#### 🗺️ Índices
- `CMNXE1` (Unique): `CMEXNEAN`

---

### 📌 CMFer
- **Descrição:** Cadastro de Feriados
- **Chave Primária:** `CMFerDta`, `CMFerCEP`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMFerDta` | `N/D` | - |
| `CMFerCEP` | `N/D` | - |
| `CMFerDes` | `N/D` | - |
| `CMFerDtaFix` | `N/D` | - |

#### 🗺️ Índices
- `CMFerA` (Unique): `CMFerDta`, `CMFerCEP`

---

### 📌 CMFIA
- **Descrição:** CMFIL Auxiliar
- **Chave Primária:** `CMEmpCod`, `CMFiACod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFiACod` | `N/D` | - |
| `CMFiAPrxCdx` | `N/D` | - |
| `CMFiAUsaCodAltCli` | `N/D` | - |
| `CMFiADtaGerRTo` | `N/D` | - |
| `CMFiAlRToCod` | `N/D` | - |
| `CMFiARToExtArq` | `N/D` | - |
| `CMFiARToPthArq` | `N/D` | - |
| `CMFiARToTipLay` | `N/D` | - |
| `CMFiARTVerLay` | `N/D` | - |
| `CMFiAImpVdaEtq` | `N/D` | - |
| `CMFiAMosTelQtd` | `N/D` | - |
| `CMFiAAleObsCli` | `N/D` | - |
| `CMFiAFCDI` | `N/D` | - |
| `CMFiAFCDF` | `N/D` | - |
| `CMFiAFCDP` | `N/D` | - |
| `CMFiaFTI` | `N/D` | - |
| `CMFiaBCB` | `N/D` | - |
| `CMFiADscCC` | `N/D` | - |
| `CMFiADscCnv` | `N/D` | - |
| `CMFiADscPrz` | `N/D` | - |
| `CMFiADscVis` | `N/D` | - |
| `CMFiAInfTipVdaAnt` | `N/D` | - |
| `CMFiAArrTru` | `N/D` | - |
| `CMFiAInfMed` | `N/D` | - |
| `CMFiAAleImpRec` | `N/D` | - |
| `CMFiADeiTelUltVda` | `N/D` | - |
| `CMFiASupVda` | `N/D` | - |
| `CMFiAVdaBri` | `N/D` | - |
| `CMFiAQtdIteMsg` | `N/D` | - |
| `CMFiAHVC` | `N/D` | - |
| `CMFiASenCanIte` | `N/D` | - |
| `CMFiAPDCliFor` | `N/D` | - |
| `CMFiACPLctProCom` | `N/D` | - |
| `CMFiACPImpParCom` | `N/D` | - |
| `CMFiAImpEtqCom` | `N/D` | - |
| `CMFIALot` | `N/D` | - |
| `CMFiAPreVisPrz` | `N/D` | - |
| `CMFIAAleVlrVda` | `N/D` | - |
| `CMFIAExiCPFChq` | `N/D` | - |
| `CMFIAPEC` | `N/D` | - |
| `CMFIASenPSC` | `N/D` | - |
| `CMFIAR17IFD` | `N/D` | - |
| `CMFiaPPF` | `N/D` | - |
| `CMFiAQtdMsg` | `N/D` | - |
| `CMFiAQtdBlq` | `N/D` | - |
| `CMFiAAbrGav` | `N/D` | - |
| `CMFiAAltPre` | `N/D` | - |
| `CMFiASCP` | `N/D` | - |
| `CMFiaDesProGer` | `N/D` | - |
| `CMFiaInfNro` | `N/D` | - |
| `CMFiaPerVdaChq` | `N/D` | - |
| `CMFiaEstMin` | `N/D` | - |
| `CMFiaOSR` | `N/D` | - |
| `CMFiaCM1` | `N/D` | - |
| `CMFiaGrvPro` | `N/D` | - |
| `CMFiaMosCodPro` | `N/D` | - |
| `CMFiaVdaVis` | `N/D` | - |
| `CMFiaAltPV` | `N/D` | - |
| `CMFiaAleRepPro` | `N/D` | - |
| `CMFiaPerAcrFecCnt` | `N/D` | - |
| `CMFiaPerDigQtd` | `N/D` | - |
| `CMFiaInfVlrUltCom` | `N/D` | - |
| `CMFiaUsaTX` | `N/D` | - |
| `CMFiaMosPerDscIte` | `N/D` | - |
| `CMFiaAbrTelAltPro` | `N/D` | - |
| `CMFiaLctVen` | `N/D` | - |
| `CMFiaVlrSan` | `N/D` | - |
| `CMFiaDiaVctSis` | `N/D` | - |
| `CMFiaAltVct` | `N/D` | - |
| `CMFiaCRSenVdaDscSup` | `N/D` | - |
| `CMFiaCRAleDscVda` | `N/D` | - |
| `CMFiaCRDscExc` | `N/D` | - |
| `CMFiaCRPrcDscBaiPar` | `N/D` | - |
| `CMFiaCfgDsc` | `N/D` | - |
| `CMFiAObs1FicCli` | `N/D` | - |
| `CMFiAObs2FicCli` | `N/D` | - |
| `CMFiAObs1Car` | `N/D` | - |
| `CMFiAObs2Car` | `N/D` | - |
| `CMFiAObs3Car` | `N/D` | - |
| `CMFiAObs4Car` | `N/D` | - |
| `CMFiAObs1BolBco` | `N/D` | - |
| `CMFiAObs2BolBco` | `N/D` | - |
| `CMFiAObs3BolBco` | `N/D` | - |
| `CMFiAObs4BolBco` | `N/D` | - |
| `CMFiACR01MsgVdaCon` | `N/D` | - |
| `CMFiACR02MsgVdaCon` | `N/D` | - |
| `CMFiACab01` | `N/D` | - |
| `CMFiACab02` | `N/D` | - |
| `CMFiACab03` | `N/D` | - |
| `CMFiACab04` | `N/D` | - |
| `CMFiAObs1Orc` | `N/D` | - |
| `CMFiAObs2Orc` | `N/D` | - |
| `CMFiAObs3Orc` | `N/D` | - |
| `CMFiAObs1_CarCob` | `N/D` | - |
| `CMFiAObs2_CarCob` | `N/D` | - |
| `CMFiAObs3_CarCob` | `N/D` | - |
| `CMFiAMsg01CF` | `N/D` | - |
| `CMFiAMsg02CF` | `N/D` | - |
| `CMFiAMsg03CF` | `N/D` | - |
| `CMFiAMsg04CF` | `N/D` | - |
| `CMFiAMsgGav` | `N/D` | - |
| `CMFiaObs4Orc` | `N/D` | - |
| `CMFiaObs5Orc` | `N/D` | - |
| `CMFiaObs6Orc` | `N/D` | - |
| `CMFiaObs7Orc` | `N/D` | - |
| `CMFiaObs8Orc` | `N/D` | - |
| `CMFiaMsg1NF` | `N/D` | - |
| `CMFiaMsg2NF` | `N/D` | - |
| `CMFiaMsg3NF` | `N/D` | - |
| `CMFiaMsg4NF` | `N/D` | - |
| `CMFiaMsg5NF` | `N/D` | - |
| `CMFiaMsg1CBol` | `N/D` | - |
| `CMFiaMsg2CBol` | `N/D` | - |
| `CMFiaMsg3CBol` | `N/D` | - |
| `CMFiaMsg4CBol` | `N/D` | - |

#### 🗺️ Índices
- `CMFIA1` (Unique): `CMEmpCod`, `CMFiACod`
- `CMFIA2` (Duplicate): `CMEmpCod`

---

### 📌 CMFil
- **Descrição:** Filiais
- **Chave Primária:** `CMEmpCod`, `CMFilCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMFilModBolBco` | `N/D` | - |
| `CMFilRazSoc` | `N/D` | - |
| `CMFilNomFan` | `N/D` | - |
| `CMFilPrcAcrVdaPrz` | `N/D` | - |
| `CMFilEnd` | `N/D` | - |
| `CMFilBai` | `N/D` | - |
| `CMFilCid` | `N/D` | - |
| `CMFilCep` | `N/D` | - |
| `CMFilUF` | `N/D` | - |
| `CMFilTel1` | `N/D` | - |
| `CMFilTel2` | `N/D` | - |
| `CMFilTel3` | `N/D` | - |
| `CMFilWatUp` | `N/D` | - |
| `CMFilFax` | `N/D` | - |
| `CMFilCgc` | `N/D` | - |
| `CMFilCPF` | `N/D` | - |
| `CMFilInsEst` | `N/D` | - |
| `CMFilInsMun` | `N/D` | - |
| `CMFilPerImpCup` | `N/D` | - |
| `CMFilQtdAleCliAtr` | `N/D` | - |
| `CMFilQtdBloCliAtr` | `N/D` | - |
| `CMFilAleFicIncCli` | `N/D` | - |
| `CMFilDtaValLct` | `N/D` | - |
| `CMFilPrxNroNF` | `N/D` | - |
| `CMFilCodMS` | `N/D` | - |
| `CMFilSenDrop` | `N/D` | - |
| `CMFilQtdErrCodMS` | `N/D` | - |
| `CMFilDtaUltAce` | `N/D` | - |
| `CMFilDtaAtuUlt` | `N/D` | - |
| `CMFilMedPgtPar` | `N/D` | - |
| `CMFilNroLinSal` | `N/D` | - |
| `CMFilDtaDia` | `N/D` | - |
| `CMFilNomSin` | `N/D` | - |
| `CMFilVlrNaoBlq` | `N/D` | - |
| `CMFilSisIde` | `N/D` | - |
| `CMFilDspBcoBol` | `N/D` | - |
| `CMFilEMa` | `N/D` | - |
| `CMFilURL` | `N/D` | - |
| `CMFilNPRazSoc` | `N/D` | - |
| `CMFilNPCPF` | `N/D` | - |
| `CMFilEndNro` | `N/D` | - |
| `CMFilNPRG` | `N/D` | - |
| `CMFilEndCom` | `N/D` | - |
| `CMFilCidCom` | `N/D` | - |
| `CMFilN_LicFun` | `N/D` | - |
| `CMFilEMa2` | `N/D` | - |
| `CMFilDtaCer` | `N/D` | - |
| `CMFilNFERazSoc` | `N/D` | - |
| `CMFilPerIE` | `N/D` | - |
| `CMFilCmdBat` | `N/D` | - |
| `CMFilSignAC` | `N/D` | - |
| `CMFIlOrc1PrcMrgLuc` | `N/D` | - |
| `CMFilTipImp` | `N/D` | - |
| `CMFilFar` | `N/D` | - |
| `CMFilCRTipCarRec` | `N/D` | - |
| `CMFilLctCxaUnc` | `N/D` | - |
| `CMFilCEModEtq` | `N/D` | - |
| `CMFilEstFra` | `N/D` | - |
| `CMFIlPthInsSis` | `N/D` | - |
| `CMFilAceQtdVda1Vez` | `N/D` | - |
| `CMFilCRModTelVdaPro` | `N/D` | - |
| `CMFilTipVdaCom` | `N/D` | - |
| `CMFilUsaTelTro` | `N/D` | - |
| `CMFilCRAltPro` | `N/D` | - |
| `CMFilCRInsUpdAtuPreVda` | `N/D` | - |
| `CMFilLimTabMov` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CMFilModTelIni` | `N/D` | - |
| `CMFilMosFotVda` | `N/D` | - |
| `CMFilSNGPC` | `N/D` | - |
| `CMFilVdaEstNeg` | `N/D` | - |
| `CMFilDtaHorUltBck` | `N/D` | - |
| `CMFilImpAss` | `N/D` | - |
| `CMFilKey` | `N/D` | - |
| `CMFilPthBck_C` | `N/D` | - |
| `CMFilPth3Bck` | `N/D` | - |
| `CMFilPth2Bck` | `N/D` | - |
| `CMFilPth1Bck` | `N/D` | - |
| `CMEmpCodBar_CodPro` | `N/D` | - |
| `CMEmpCxFecDif` | `N/D` | - |
| `CMFilAbrCxaUsu` | `N/D` | - |
| `CMFilAceFilEntSai` | `N/D` | - |
| `CMFilAceNroSerPro` | `N/D` | - |
| `CMFilAcrDiaVct` | `N/D` | - |
| `CMFilAcrMicCRMovSeq` | `N/D` | - |
| `CMFilAcuCEPxF` | `N/D` | - |
| `CMFilZerSeqIniDia` | `N/D` | - |
| `CMFilAleVct` | `N/D` | - |
| `CMFilAltCxaAnt` | `N/D` | - |
| `CMFilAltGrpSgrDsp` | `N/D` | - |
| `CMFilAltVlrTabDurVda` | `N/D` | - |
| `CMFilArrTru` | `N/D` | - |
| `CMFilBalMesEst` | `N/D` | - |
| `CMFilBckNFP` | `N/D` | - |
| `CMFilBco_CofBxa` | `N/D` | - |
| `CMFilBcoCof` | `N/D` | - |
| `CMFilFilBcoCof` | `N/D` | - |
| `CMFilBxaCCr` | `N/D` | - |
| `CMFilBxaDsp` | `N/D` | - |
| `CMFilCapAutPesBal` | `N/D` | - |
| `CMFilCE1DesEtq` | `N/D` | - |
| `CMFilCE2DesEtq` | `N/D` | - |
| `CMFilCECorNro` | `N/D` | - |
| `CMFilCEDspCod` | `N/D` | - |
| `CMFilCENFCSEQ` | `N/D` | - |
| `CMFilCepDes` | `N/D` | - |
| `CMFilCEPPe` | `N/D` | - |
| `CMFilCICUltVda` | `N/D` | - |
| `CMFilCISUltVda` | `N/D` | - |
| `CMFilCliCupFis` | `N/D` | - |
| `CMFilCnfESC` | `N/D` | - |
| `CMFilCodCliChqPre` | `N/D` | - |
| `CMFilCodEtqBal` | `N/D` | - |
| `CMFilCom_VdaPrz` | `N/D` | - |
| `CMFilComVda` | `N/D` | - |
| `CMFilConProVda` | `N/D` | - |
| `CMFilCPPrxCli` | `N/D` | - |
| `CMFilCRAcePreVdaCli` | `N/D` | - |
| `CMFilCRNotProImpCar` | `N/D` | - |
| `CMFilCRParVdaNotPro` | `N/D` | - |
| `CMFilCRPerEstParAnt` | `N/D` | - |
| `CMFilCRProImpCar` | `N/D` | - |
| `CMFilCRTICre` | `N/D` | - |
| `CMFilCRTIVis` | `N/D` | - |
| `CMFilCVP` | `N/D` | - |
| `CMFilCVVCom` | `N/D` | - |
| `CMFIlCVVNad` | `N/D` | - |
| `CMFIlCVVSim` | `N/D` | - |
| `CMFilCxaDesTrc` | `N/D` | - |
| `CMFilDesRec` | `N/D` | - |
| `CMFilEtqBalPesVal` | `N/D` | - |
| `CMFilFaiTriIcmProZer` | `N/D` | - |
| `CMFilFec_CnvFecCnt` | `N/D` | - |
| `CMFilFecCnvVdaPar` | `N/D` | - |
| `CMFIlFecCxaDia` | `N/D` | - |
| `CMFilFilBxa` | `N/D` | - |
| `CMFilFilPthArq` | `N/D` | - |
| `CMFilFinAleAni` | `N/D` | - |
| `CMFilFreTra` | `N/D` | - |
| `CMFilICPF` | `N/D` | - |
| `CMFilImp1CodVdaCar` | `N/D` | - |
| `CMFilImp_DetCli` | `N/D` | - |
| `CMFilImpCliFinBol` | `N/D` | - |
| `CMFilImpCNPJ` | `N/D` | - |
| `CMFilImpCodProCar` | `N/D` | - |
| `CMFilImpCxaComDetVda` | `N/D` | - |
| `CMFilImpDesAcrCar` | `N/D` | - |
| `CMFilImpHorCar` | `N/D` | - |
| `CMFilImpNotSemDsc` | `N/D` | - |
| `CMFilImpPrxCab` | `N/D` | - |
| `CMFilImpRecPrz` | `N/D` | - |
| `CMFilImpSer` | `N/D` | - |
| `CMFilImpTipCli` | `N/D` | - |
| `CMFilImpVlrAbe` | `N/D` | - |
| `CMFIlIncCarJrs` | `N/D` | - |
| `CMFIlIndDtaUlt` | `N/D` | - |
| `CMFIlIndQtdDia` | `N/D` | - |
| `CMFilIniAleAni` | `N/D` | - |
| `CMFilIntEtq` | `N/D` | - |
| `CMFilIRE` | `N/D` | - |
| `CMFilLctIteSepJunVda` | `N/D` | - |
| `CMFilLctLot` | `N/D` | - |
| `CMFilLctOutPar` | `N/D` | - |
| `CMFilLctPreCusPro` | `N/D` | - |
| `CMFilLctTrcIniFin` | `N/D` | - |
| `CMFilLojEsc` | `N/D` | - |
| `CMFilMIFAux` | `N/D` | - |
| `CMFilMod_TelOrc` | `N/D` | - |
| `CMFilModBal` | `N/D` | - |
| `CMFilModEtqCli` | `N/D` | - |
| `CMFilModGav` | `N/D` | - |
| `CMFilModImpFis` | `N/D` | - |
| `CMFilModNotPro` | `N/D` | - |
| `CMFilModRelLisPre` | `N/D` | - |
| `CMFilMosCamCxa` | `N/D` | - |
| `CMFilMosParRec33C` | `N/D` | - |
| `CMFilMrgMedPgtPar` | `N/D` | - |
| `CMFILNFECam` | `N/D` | - |
| `CMFilNFEDM` | `N/D` | - |
| `CMFilNFEDTp` | `N/D` | - |
| `CMFilNFEMod` | `N/D` | - |
| `CMFilNom_ImpTro` | `N/D` | - |
| `CMFilNomImp` | `N/D` | - |
| `CMFilNopCod` | `N/D` | - |
| `CMFilNotProDep` | `N/D` | - |
| `CMFilNotVct` | `N/D` | - |
| `CMFilNro_LinAux` | `N/D` | - |
| `CMFilOrc1IndAum` | `N/D` | - |
| `CMFilOutPut` | `N/D` | - |
| `CMFilPerAcrSgr` | `N/D` | - |
| `CMFilPerAltVlrFinVda` | `N/D` | - |
| `CMFilPerDarDscRecPar` | `N/D` | - |
| `CMFilPerDigRefTelVda` | `N/D` | - |
| `CMFilPerDscVdaPrz` | `N/D` | - |
| `CMFilPerFraProEst` | `N/D` | - |
| `CMFilPerIcmSimPau` | `N/D` | - |
| `CMFilPerIRRF` | `N/D` | - |
| `CMFilPerISS` | `N/D` | - |
| `CMFilPerJntVdaCli` | `N/D` | - |
| `CMFilPerLctProVda` | `N/D` | - |
| `CMFilPerSecSoc` | `N/D` | - |
| `CMFilPerZerJrs` | `N/D` | - |
| `CMFilPorSer` | `N/D` | - |
| `CMFilPrcMrg` | `N/D` | - |
| `CMFilPrcPonFid` | `N/D` | - |
| `CMFilPreBal` | `N/D` | - |
| `CMFilProLctPreQtd` | `N/D` | - |
| `CMFilProModTel` | `N/D` | - |
| `CMFilPrxCodBolBco` | `N/D` | - |
| `CMFilPrxOrc` | `N/D` | - |
| `CMFilPthBusPre` | `N/D` | - |
| `CMFilQtdCodBal` | `N/D` | - |
| `CMFilQtdDiaLctAutFunPer` | `N/D` | - |
| `CMFilQtdMesDesCli` | `N/D` | - |
| `CMFilQtdPerValSen` | `N/D` | - |
| `CMFilRecCCr` | `N/D` | - |
| `CMFilRecChq` | `N/D` | - |
| `CMFilRecTrc` | `N/D` | - |
| `CMFilResCxaUnc` | `N/D` | - |
| `CMFilRTeSNGPC` | `N/D` | - |
| `CMFilSaiProNF` | `N/D` | - |
| `CMFilSenRT` | `N/D` | - |
| `CMFilSenSup` | `N/D` | - |
| `CMFilSenUltPro` | `N/D` | - |
| `CMFilSer` | `N/D` | - |
| `CMFilSerCFOP` | `N/D` | - |
| `CMFilSisDev` | `N/D` | - |
| `CMFilSSe` | `N/D` | - |
| `CMFilTelSNGPC` | `N/D` | - |
| `CMFilTipCab` | `N/D` | - |
| `CMFilTMV` | `N/D` | - |
| `CMFilTodProTmp` | `N/D` | - |
| `CMFilTolPthArq` | `N/D` | - |
| `CMFilUsaCPg` | `N/D` | - |
| `CMFilUsaCreBxaPar` | `N/D` | - |
| `CMFilUsaNotPau` | `N/D` | - |
| `CMFilUsaPonFid` | `N/D` | - |
| `CMFilUsaSGrUni` | `N/D` | - |
| `CMFilUsaTabPre` | `N/D` | - |
| `CMFilUsuChe` | `N/D` | - |
| `CMFilVarEtq` | `N/D` | - |
| `CMFilVdaEnc` | `N/D` | - |
| `CMFilVdaPrzQtdRec` | `N/D` | - |
| `CMFilVdaVisQtdRec` | `N/D` | - |
| `CMFilVlrProVda` | `N/D` | - |
| `CMFilVctSisMS` | `N/D` | - |
| `CMFilRec40Prnt` | `N/D` | - |
| `CMFilRec80Prnt` | `N/D` | - |
| `CMFilRomEntPrnt` | `N/D` | - |
| `CMFilPerPix` | `N/D` | - |
| `CMFilVlrBol` | `N/D` | - |
| `CMFilBcoPix` | `N/D` | - |
| `CMFilBcoBol` | `N/D` | - |
| `CMFilPthRec` | `N/D` | - |
| `CMFilPthEnv` | `N/D` | - |
| `CMFilDUESNG` | `N/D` | - |
| `CMFilCGCAux` | `N/D` | - |
| `CMFilNFCEMod` | `N/D` | - |
| `CMFilNFCEDM` | `N/D` | - |
| `CMFilNFCETp` | `N/D` | - |
| `CMEmpTstPri` | `N/D` | - |
| `CMEmpTstExe` | `N/D` | - |
| `CMEMPReorg` | `N/D` | - |

#### 🗺️ Índices
- `CMFil1` (Unique): `CMEmpCod`, `CMFilCod`
- `CMFil2` (Duplicate): `CMEmpCod`
- `CMFil3` (Duplicate): `CMEmpCod`, `CMFilRazSoc`

---

### 📌 CMFt1
- **Descrição:** Controle de Fotos 01
- **Chave Primária:** `CMEmpCod`, `CMFt1Org`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFt1Org` | `N/D` | - |
| `CMFt1Pth` | `N/D` | - |
| `CMFt1Ext` | `N/D` | - |

#### 🗺️ Índices
- `CMFt1A` (Unique): `CMEmpCod`, `CMFt1Org`
- `CmFt1B` (Duplicate): `CMEmpCod`

---

### 📌 CMFt2
- **Descrição:** Controle de Fotos 02
- **Chave Primária:** `CMEmpCod`, `CMFt1Org`, `CMFt2Cod`, `CMFt2Seq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFt1Org` | `N/D` | - |
| `CMFt1Pth` | `N/D` | - |
| `CMFt1Ext` | `N/D` | - |
| `CMFt2Cod` | `N/D` | - |
| `CMFt2Seq` | `N/D` | - |
| `CMFt2Nom` | `N/D` | - |
| `CMFt2Pos` | `N/D` | - |
| `CMFt2Des` | `N/D` | - |
| `CMFt2Usu` | `N/D` | - |
| `CMFt2TST` | `N/D` | - |
| `CMFt2Prg` | `N/D` | - |
| `CMFt2Fot` | `N/D` | - |

#### 🗺️ Índices
- `CMFt2A` (Unique): `CMEmpCod`, `CMFt1Org`, `CMFt2Cod`, `CMFt2Seq`
- `CMFt2B` (Duplicate): `CMEmpCod`, `CMFt1Org`

---

### 📌 CMGen
- **Descrição:** Descrições Genéricas por Tipo
- **Chave Primária:** `CMEmpCod`, `CMGenCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMGenCod` | `N/D` | - |
| `CMGenDes` | `N/D` | - |
| `CMGenTip` | `N/D` | - |
| `CMGenCodRed` | `N/D` | - |
| `CMGenCod01` | `N/D` | - |
| `CMGenCod02` | `N/D` | - |
| `CMGenCod03` | `N/D` | - |
| `CMGenCod04` | `N/D` | - |
| `CMGenCod05` | `N/D` | - |
| `CMGenCod06` | `N/D` | - |
| `CMGenCod07` | `N/D` | - |
| `CMGenCod08` | `N/D` | - |
| `CMGenCod09` | `N/D` | - |
| `CMGenCod10` | `N/D` | - |
| `CMGenCod11` | `N/D` | - |
| `CMGenCod12` | `N/D` | - |
| `CMGenNro01` | `N/D` | - |
| `CMGenNro02` | `N/D` | - |
| `CMGenNro03` | `N/D` | - |
| `CMGenNro04` | `N/D` | - |
| `CMGenNro05` | `N/D` | - |
| `CMGenNro06` | `N/D` | - |
| `CMGenNro07` | `N/D` | - |
| `CMGenNro08` | `N/D` | - |
| `CMGenNro09` | `N/D` | - |
| `CMGenNro10` | `N/D` | - |
| `CMGenNro11` | `N/D` | - |
| `CMGenNro12` | `N/D` | - |
| `CMGenNro13` | `N/D` | - |
| `CMGenNro15` | `N/D` | - |
| `CMGenNro14` | `N/D` | - |
| `CMGenNro16` | `N/D` | - |
| `CMGenNro17` | `N/D` | - |
| `CMGenNro18` | `N/D` | - |
| `CMGenNro19` | `N/D` | - |
| `CMGenNro20` | `N/D` | - |
| `CMGenNro21` | `N/D` | - |
| `CMGenNro22` | `N/D` | - |
| `CMGenNro23` | `N/D` | - |
| `CMGenNro24` | `N/D` | - |
| `CMGenCha01` | `N/D` | - |
| `CMGenCha02` | `N/D` | - |
| `CMGenCha03` | `N/D` | - |
| `CMGenCha04` | `N/D` | - |
| `CMGenCha05` | `N/D` | - |
| `CMGenCha06` | `N/D` | - |
| `CMGenCha07` | `N/D` | - |
| `CMGenCha08` | `N/D` | - |
| `CMGenCha09` | `N/D` | - |
| `CMGenCha10` | `N/D` | - |
| `CMGenCha11` | `N/D` | - |
| `CMGenCha12` | `N/D` | - |
| `CMGenCha13` | `N/D` | - |
| `CMGenCha14` | `N/D` | - |
| `CMGenCha15` | `N/D` | - |
| `CMGenCha16` | `N/D` | - |
| `CMGenCha17` | `N/D` | - |
| `CMGenCha18` | `N/D` | - |
| `CMGenCha19` | `N/D` | - |
| `CMGenCha20` | `N/D` | - |
| `CMGenCha21` | `N/D` | - |
| `CMGenCha22` | `N/D` | - |
| `CMGenCha23` | `N/D` | - |
| `CMGenCha24` | `N/D` | - |
| `CMGenSts01` | `N/D` | - |
| `CMGenSts02` | `N/D` | - |
| `CMGenSts03` | `N/D` | - |
| `CMGenSts04` | `N/D` | - |
| `CMGenSts05` | `N/D` | - |
| `CMGenSts06` | `N/D` | - |
| `CMGenSts07` | `N/D` | - |
| `CMGenSts08` | `N/D` | - |
| `CMGenSts09` | `N/D` | - |
| `CMGenSts10` | `N/D` | - |
| `CMGenSts11` | `N/D` | - |
| `CMGenSts12` | `N/D` | - |
| `CMGenDta01` | `N/D` | - |
| `CMGenDta02` | `N/D` | - |
| `CMGenDta03` | `N/D` | - |
| `CMGenDta04` | `N/D` | - |
| `CMGenDta05` | `N/D` | - |
| `CMGenDta06` | `N/D` | - |
| `CMGenTST01` | `N/D` | - |
| `CMGenTST02` | `N/D` | - |
| `CMGenTST03` | `N/D` | - |
| `CMGenTST04` | `N/D` | - |
| `CMGenTST05` | `N/D` | - |
| `CMGenTST06` | `N/D` | - |
| `CMGenExPro` | `N/D` | - |
| `CMGenJunCod` | `N/D` | - |
| `CMGenJundes` | `N/D` | - |
| `CMGenJunRed` | `N/D` | - |

#### 🗺️ Índices
- `CMGenA` (Unique): `CMEmpCod`, `CMGenCod`
- `CMGenB` (Duplicate): `CMEmpCod`
- `CMGenC` (Duplicate): `CMEmpCod`, `CMGenTip`, `CMGenCod`
- `CMGenD` (Duplicate): `CMEmpCod`, `CMGenTip`, `CMGenDes`
- `CMGenE` (Duplicate): `CMEmpCod`, `CMGenTip`, `CMGenCod`
- `CMGenF` (Duplicate): `CMEmpCod`, `CMGenTip`, `CMGenCodRed`, `CMGenJunCod`

---

### 📌 CMGenO
- **Descrição:** Tabela Genérica Códigos - Detalhes
- **Chave Primária:** `CMEmpCod`, `CMGenCod`, `CMGenSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMGenCod` | `N/D` | - |
| `CMGenDes` | `N/D` | - |
| `CMGenTip` | `N/D` | - |
| `CMGenCodRed` | `N/D` | - |
| `CMGenCod01` | `N/D` | - |
| `CMGenCod02` | `N/D` | - |
| `CMGenCod03` | `N/D` | - |
| `CMGenCod04` | `N/D` | - |
| `CMGenCod05` | `N/D` | - |
| `CMGenCod06` | `N/D` | - |
| `CMGenCod07` | `N/D` | - |
| `CMGenCod08` | `N/D` | - |
| `CMGenCod09` | `N/D` | - |
| `CMGenCod10` | `N/D` | - |
| `CMGenCod11` | `N/D` | - |
| `CMGenCod12` | `N/D` | - |
| `CMGenNro01` | `N/D` | - |
| `CMGenNro02` | `N/D` | - |
| `CMGenNro03` | `N/D` | - |
| `CMGenNro04` | `N/D` | - |
| `CMGenNro05` | `N/D` | - |
| `CMGenNro06` | `N/D` | - |
| `CMGenNro07` | `N/D` | - |
| `CMGenNro08` | `N/D` | - |
| `CMGenNro09` | `N/D` | - |
| `CMGenNro10` | `N/D` | - |
| `CMGenNro11` | `N/D` | - |
| `CMGenNro12` | `N/D` | - |
| `CMGenNro13` | `N/D` | - |
| `CMGenNro15` | `N/D` | - |
| `CMGenNro14` | `N/D` | - |
| `CMGenNro16` | `N/D` | - |
| `CMGenNro17` | `N/D` | - |
| `CMGenNro18` | `N/D` | - |
| `CMGenNro19` | `N/D` | - |
| `CMGenNro20` | `N/D` | - |
| `CMGenNro21` | `N/D` | - |
| `CMGenNro22` | `N/D` | - |
| `CMGenNro23` | `N/D` | - |
| `CMGenNro24` | `N/D` | - |
| `CMGenCha01` | `N/D` | - |
| `CMGenCha02` | `N/D` | - |
| `CMGenCha03` | `N/D` | - |
| `CMGenCha04` | `N/D` | - |
| `CMGenCha05` | `N/D` | - |
| `CMGenCha06` | `N/D` | - |
| `CMGenCha07` | `N/D` | - |
| `CMGenCha08` | `N/D` | - |
| `CMGenCha09` | `N/D` | - |
| `CMGenCha10` | `N/D` | - |
| `CMGenCha11` | `N/D` | - |
| `CMGenCha12` | `N/D` | - |
| `CMGenCha13` | `N/D` | - |
| `CMGenCha14` | `N/D` | - |
| `CMGenCha15` | `N/D` | - |
| `CMGenCha16` | `N/D` | - |
| `CMGenCha17` | `N/D` | - |
| `CMGenCha18` | `N/D` | - |
| `CMGenCha19` | `N/D` | - |
| `CMGenCha20` | `N/D` | - |
| `CMGenCha21` | `N/D` | - |
| `CMGenCha22` | `N/D` | - |
| `CMGenCha23` | `N/D` | - |
| `CMGenCha24` | `N/D` | - |
| `CMGenSts01` | `N/D` | - |
| `CMGenSts02` | `N/D` | - |
| `CMGenSts03` | `N/D` | - |
| `CMGenSts04` | `N/D` | - |
| `CMGenSts05` | `N/D` | - |
| `CMGenSts06` | `N/D` | - |
| `CMGenSts07` | `N/D` | - |
| `CMGenSts08` | `N/D` | - |
| `CMGenSts09` | `N/D` | - |
| `CMGenSts10` | `N/D` | - |
| `CMGenSts11` | `N/D` | - |
| `CMGenSts12` | `N/D` | - |
| `CMGenDta01` | `N/D` | - |
| `CMGenDta02` | `N/D` | - |
| `CMGenDta03` | `N/D` | - |
| `CMGenDta04` | `N/D` | - |
| `CMGenDta05` | `N/D` | - |
| `CMGenDta06` | `N/D` | - |
| `CMGenTST01` | `N/D` | - |
| `CMGenTST02` | `N/D` | - |
| `CMGenTST03` | `N/D` | - |
| `CMGenTST04` | `N/D` | - |
| `CMGenTST05` | `N/D` | - |
| `CMGenTST06` | `N/D` | - |
| `CMGenExPro` | `N/D` | - |
| `CMGenSeq` | `N/D` | - |
| `CMGenObs` | `N/D` | - |
| `CMGenObs1` | `N/D` | - |
| `CMGenOFon` | `N/D` | - |
| `CMGenOTam` | `N/D` | - |
| `CMGenONeg` | `N/D` | - |

#### 🗺️ Índices
- `CMGenOA` (Unique): `CMEmpCod`, `CMGenCod`, `CMGenSeq`
- `CMGenOB` (Duplicate): `CMEmpCod`, `CMGenCod`

---

### 📌 CMGer
- **Descrição:** Tabela Genérica para Usar com SDT
- **Chave Primária:** `CMEmpCod`, `CMGerFil`, `CMGerTab`, `CMGerCmp`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMGerFil` | `N/D` | - |
| `CMGerTab` | `N/D` | - |
| `CMGerCmp` | `N/D` | - |
| `CMGerCnt` | `N/D` | - |

#### 🗺️ Índices
- `CMGer1` (Unique): `CMEmpCod`, `CMGerFil`, `CMGerTab`, `CMGerCmp`
- `CMGer2` (Duplicate): `CMEmpCod`

---

### 📌 CMGR1
- **Descrição:** Controle de Gráficos - Configurações
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMGr1Usu`, `CMGr1Nom`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMGr1Usu` | `N/D` | - |
| `CMGr1Nom` | `N/D` | - |
| `CMGr1Des1` | `N/D` | - |
| `CMGr1Des2` | `N/D` | - |
| `CMGr1MosFai` | `N/D` | - |
| `CMGr1MosVal` | `N/D` | - |
| `CMGr1MosNom` | `N/D` | - |
| `CMGr1CorFai` | `N/D` | - |
| `CMGr1QtdFai` | `N/D` | - |
| `CMGr1IntCor` | `N/D` | - |
| `CMGr1DesX` | `N/D` | - |
| `CMGr1DesY` | `N/D` | - |
| `CMGr1Pth` | `N/D` | - |
| `CMGr1MinY` | `N/D` | - |
| `CMGr1MaxY` | `N/D` | - |
| `CMGr1HorVer` | `N/D` | - |
| `CMGr1Pre` | `N/D` | - |
| `CMGr1VlrTot` | `N/D` | - |
| `CMGr1QtdUsaCal` | `N/D` | - |
| `CMGr1IncTotOut` | `N/D` | - |
| `CMGr1Tam` | `N/D` | - |
| `CMGr1ColTot` | `N/D` | - |
| `CMGR1ColMed` | `N/D` | - |
| `CMGr1VlrMed` | `N/D` | - |
| `CMGr1QtdCMGr2` | `N/D` | - |
| `CMGr1SimMul` | `N/D` | - |

#### 🗺️ Índices
- `CMGR1A` (Unique): `CMEmpCod`, `CMFilCod`, `CMGr1Usu`, `CMGr1Nom`
- `CMGR1B` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CMGR2
- **Descrição:** Controle Gráficos - Valores
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMGr1Usu`, `CMGr1Nom`, `CMGr2Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMGr1Usu` | `N/D` | - |
| `CMGr1Nom` | `N/D` | - |
| `CMGr1Des1` | `N/D` | - |
| `CMGr1Des2` | `N/D` | - |
| `CMGr1MosFai` | `N/D` | - |
| `CMGr1MosVal` | `N/D` | - |
| `CMGr1MosNom` | `N/D` | - |
| `CMGr1CorFai` | `N/D` | - |
| `CMGr1QtdFai` | `N/D` | - |
| `CMGr1IntCor` | `N/D` | - |
| `CMGr1DesX` | `N/D` | - |
| `CMGr1DesY` | `N/D` | - |
| `CMGr1Pth` | `N/D` | - |
| `CMGr1MinY` | `N/D` | - |
| `CMGr1MaxY` | `N/D` | - |
| `CMGr1HorVer` | `N/D` | - |
| `CMGr1Pre` | `N/D` | - |
| `CMGr1VlrTot` | `N/D` | - |
| `CMGr1QtdUsaCal` | `N/D` | - |
| `CMGr1IncTotOut` | `N/D` | - |
| `CMGr1Tam` | `N/D` | - |
| `CMGr1ColTot` | `N/D` | - |
| `CMGR1ColMed` | `N/D` | - |
| `CMGr1VlrMed` | `N/D` | - |
| `CMGr1QtdCMGr2` | `N/D` | - |
| `CMGr1SimMul` | `N/D` | - |
| `CMGr2Cod` | `N/D` | - |
| `CMGr2Des` | `N/D` | - |
| `CMGr2DesCom` | `N/D` | - |
| `CMGr2VlrNro` | `N/D` | - |
| `CMGR2MosGra` | `N/D` | - |
| `CMGr2Per` | `N/D` | - |
| `CMGr2Idx` | `N/D` | - |
| `CMGr2Cor` | `N/D` | - |
| `CMGr2Tip` | `N/D` | - |
| `CMGr2Ser` | `N/D` | - |
| `CMGr2FixCor` | `N/D` | - |

#### 🗺️ Índices
- `CMGR2A` (Unique): `CMEmpCod`, `CMFilCod`, `CMGr1Usu`, `CMGr1Nom`, `CMGr2Cod`
- `CMGR2B` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMGr1Usu`, `CMGr1Nom`
- `CMGR2C` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMGr1Nom`, `CMGr1Usu`, `CMGr2Idx`

---

### 📌 CMGTX
- **Descrição:** Gerar Arquivo Txt
- **Chave Primária:** `CMGTXSEQ`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMGTXSEQ` | `N/D` | - |
| `CMGTX01` | `N/D` | - |
| `CMGTX02` | `N/D` | - |
| `CMGTX03` | `N/D` | - |
| `CMGTX04` | `N/D` | - |
| `CMGTX05` | `N/D` | - |

#### 🗺️ Índices
- `CMGTX1` (Unique): `CMGTXSEQ`

---

### 📌 CMHBc
- **Descrição:** Histórico do Backup
- **Chave Primária:** `CMHBcDta`, `CMHBcHor`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMHBcDta` | `N/D` | - |
| `CMHBcHor` | `N/D` | - |
| `CMHBcDes` | `N/D` | - |

#### 🗺️ Índices
- `CMHBc1` (Unique): `CMHBcDta`, `CMHBcHor`
- `CMHBc2` (Duplicate): `CMHBcDta`, `CMHBcHor`, `CMHBcDes`

---

### 📌 CMHEA
- **Descrição:** Histórico de Envio de Arquivo
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMHEATip`, `CMHEATST`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMHEATip` | `N/D` | - |
| `CMHEATST` | `N/D` | - |
| `CMHEAUSU` | `N/D` | - |
| `CMHEAOBS` | `N/D` | - |
| `CMHEADIN` | `N/D` | - |
| `CMHEADFI` | `N/D` | - |

#### 🗺️ Índices
- `CMHEA1` (Unique): `CMEmpCod`, `CMFilCod`, `CMHEATip`, `CMHEATST`
- `CMHEA2` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CMHEA3` (Duplicate): `CMHEATip`, `CMHEATST`

---

### 📌 CMIdx
- **Descrição:** Tabela Usada para Indexar
- **Chave Primária:** `CMIdxUsu`, `CMIdxCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMIdxUsu` | `N/D` | - |
| `CMIdxCod` | `N/D` | - |

#### 🗺️ Índices
- `CMIdxA` (Unique): `CMIdxUsu`, `CMIdxCod`
- `CMIdxB` (Duplicate): `CMIdxCod`

---

### 📌 CMIFi1
- **Descrição:** Impressora Fiscal 01
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMIFiCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMIFiCod` | `N/D` | - |
| `CMIFi1Dsc` | `N/D` | - |
| `CMIFi1VdaVis` | `N/D` | - |
| `CMIFi1VdaPrz` | `N/D` | - |
| `CMIFi1VdaCCr` | `N/D` | - |
| `CMIFi1VdaFP` | `N/D` | - |
| `CMIFi1FPDes` | `N/D` | - |
| `CMIFi1Vda_Chq` | `N/D` | - |
| `CMIFi1PrxNroCupFis` | `N/D` | - |
| `CMIFI1NroLinSal` | `N/D` | - |
| `CMIFI1VisDes` | `N/D` | - |
| `CMIFI1PrzDes` | `N/D` | - |
| `CMIFI1ChqDes` | `N/D` | - |
| `CMIFI1CCrDes` | `N/D` | - |
| `CMIFI1VdCon` | `N/D` | - |
| `CMIFI1ConDes` | `N/D` | - |
| `CMIFil1NroSerImp` | `N/D` | - |
| `CMIFil1DtRedZ` | `N/D` | - |
| `CMIFil1VrRedZ` | `N/D` | - |

#### 🗺️ Índices
- `CMIFi1A` (Unique): `CMEmpCod`, `CMFilCod`, `CMIFiCod`
- `CMIFi1B` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CMIFi2
- **Descrição:** Impressora Fiscal 2
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMIFiCod`, `CMIFi2PrcIcm`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMIFiCod` | `N/D` | - |
| `CMIFi1Dsc` | `N/D` | - |
| `CMIFi1VdaVis` | `N/D` | - |
| `CMIFi1VdaPrz` | `N/D` | - |
| `CMIFi1VdaCCr` | `N/D` | - |
| `CMIFi1VdaFP` | `N/D` | - |
| `CMIFi1FPDes` | `N/D` | - |
| `CMIFi1Vda_Chq` | `N/D` | - |
| `CMIFi1PrxNroCupFis` | `N/D` | - |
| `CMIFI1NroLinSal` | `N/D` | - |
| `CMIFI1VisDes` | `N/D` | - |
| `CMIFI1PrzDes` | `N/D` | - |
| `CMIFI1ChqDes` | `N/D` | - |
| `CMIFI1CCrDes` | `N/D` | - |
| `CMIFI1VdCon` | `N/D` | - |
| `CMIFI1ConDes` | `N/D` | - |
| `CMIFil1NroSerImp` | `N/D` | - |
| `CMIFil1DtRedZ` | `N/D` | - |
| `CMIFil1VrRedZ` | `N/D` | - |
| `CMIFi2PrcIcm` | `N/D` | - |
| `CMIFi2FaiImpFis` | `N/D` | - |
| `CMIFi2CDta` | `N/D` | - |
| `CMIFi2CHor` | `N/D` | - |
| `CMIFi2CUsu` | `N/D` | - |
| `CMIFi2DtaTrs` | `N/D` | - |
| `CMIFi2FlaDel` | `N/D` | - |

#### 🗺️ Índices
- `CMIFi2A` (Unique): `CMEmpCod`, `CMFilCod`, `CMIFiCod`, `CMIFi2PrcIcm`
- `CMIFi2B` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMIFiCod`

---

### 📌 CMLib
- **Descrição:** TCM02AA
- **Chave Primária:** `CMLibCodMs`, `CMLibDtahra`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMLibCodMs` | `N/D` | - |
| `CMLibDtahra` | `N/D` | - |
| `CMLibEmpCod` | `N/D` | - |
| `CMLibFilCod` | `N/D` | - |
| `CMLibEmpRazSoc` | `N/D` | - |
| `CMLibNomFan` | `N/D` | - |
| `CMLibTel1` | `N/D` | - |
| `CMLibTel2` | `N/D` | - |
| `CMLibUsuNom` | `N/D` | - |
| `CMLibTsLib` | `N/D` | - |
| `CMLibTip` | `N/D` | - |

#### 🗺️ Índices
- `CMLib1` (Unique): `CMLibCodMs`, `CMLibDtahra`

---

### 📌 CMMes
- **Descrição:** Tabela Acumulo Mês
- **Chave Primária:** `CMEmpCod`, `CMAnoOrg`, `CMAnoFil`, `CMAnoAno`, `CMAnoChv1`, `CMMesMes`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMAnoOrg` | `N/D` | - |
| `CMAnoFil` | `N/D` | - |
| `CMAnoAno` | `N/D` | - |
| `CMAnoChv1` | `N/D` | - |
| `CMAnoQtd1` | `N/D` | - |
| `CMAnoQtd2` | `N/D` | - |
| `CMAnoQtd3` | `N/D` | - |
| `CMAnoQtd4` | `N/D` | - |
| `CMAnoQtd5` | `N/D` | - |
| `CMAnoAno1` | `N/D` | - |
| `CMAnoAno2` | `N/D` | - |
| `CMAnoAno3` | `N/D` | - |
| `CMAnoAno4` | `N/D` | - |
| `CMAnoAno5` | `N/D` | - |
| `CMAnoVlr1` | `N/D` | - |
| `CMAnoVlr2` | `N/D` | - |
| `CMAnoVlr3` | `N/D` | - |
| `CMAnoVlr4` | `N/D` | - |
| `CMAnoVlr5` | `N/D` | - |
| `CMAnoVlr6` | `N/D` | - |
| `CMAnoVlr7` | `N/D` | - |
| `CMAnoVlr8` | `N/D` | - |
| `CMAnoVlr9` | `N/D` | - |
| `CMAnoQ11A` | `N/D` | - |
| `CMAnoQ12A` | `N/D` | - |
| `CMAnoQ13A` | `N/D` | - |
| `CMAnoQ14A` | `N/D` | - |
| `CMAnoQ15A` | `N/D` | - |
| `CMAnoDQ11A` | `N/D` | - |
| `CMAnoDQ12A` | `N/D` | - |
| `CMAnoDQ13A` | `N/D` | - |
| `CMAnoDQ14A` | `N/D` | - |
| `CMAnoDQ15A` | `N/D` | - |
| `CMAnoPQ11A` | `N/D` | - |
| `CMAnoPQ12A` | `N/D` | - |
| `CMAnoPQ13A` | `N/D` | - |
| `CMAnoPQ14A` | `N/D` | - |
| `CMAnoPQ15A` | `N/D` | - |
| `CMAnoDes1` | `N/D` | - |
| `CMAnoDes2` | `N/D` | - |
| `CMAnoDes3` | `N/D` | - |
| `CMAnoDes4` | `N/D` | - |
| `CMAnoQA000` | `N/D` | - |
| `CMAnoQA100` | `N/D` | - |
| `CMAnoQA120` | `N/D` | - |
| `CmAnoQA103` | `N/D` | - |
| `CMAnoQA003` | `N/D` | - |
| `CMMesMes` | `N/D` | - |
| `CMMesQtd1` | `N/D` | - |
| `CMMesQtd2` | `N/D` | - |
| `CMMesQtd3` | `N/D` | - |
| `CMMesQtd4` | `N/D` | - |
| `CMMesQtd5` | `N/D` | - |
| `CMMesVlr1` | `N/D` | - |
| `CMMesVlr2` | `N/D` | - |
| `CMMesVlr3` | `N/D` | - |
| `CMMesVlr4` | `N/D` | - |
| `CMMesVlr5` | `N/D` | - |
| `CMMesVlr6` | `N/D` | - |
| `CMMesVlr7` | `N/D` | - |
| `CMMesVlr8` | `N/D` | - |
| `CMMesVlr9` | `N/D` | - |
| `CMMesQ11A` | `N/D` | - |
| `CMMesQ12A` | `N/D` | - |
| `CMMesQ13A` | `N/D` | - |
| `CMMesQ14A` | `N/D` | - |
| `CMMesQ15A` | `N/D` | - |
| `CMMesDQ11A` | `N/D` | - |
| `CMMesDQ12A` | `N/D` | - |
| `CMMesDQ13A` | `N/D` | - |
| `CMMesDQ14A` | `N/D` | - |
| `CMMesDQ15A` | `N/D` | - |
| `CMMesPQ11A` | `N/D` | - |
| `CMMesPQ12A` | `N/D` | - |
| `CMMesPQ13A` | `N/D` | - |
| `CMMesPQ14A` | `N/D` | - |
| `CMMesPQ15A` | `N/D` | - |
| `CMMesQA000` | `N/D` | - |
| `CMMesQA100` | `N/D` | - |
| `CMMesQA120` | `N/D` | - |
| `CMMesQA003` | `N/D` | - |
| `CMMesQA103` | `N/D` | - |

#### 🗺️ Índices
- `CMMes1` (Unique): `CMEmpCod`, `CMAnoOrg`, `CMAnoFil`, `CMAnoAno`, `CMAnoChv1`, `CMMesMes`
- `CMMes2` (Duplicate): `CMEmpCod`, `CMAnoOrg`, `CMAnoFil`, `CMAnoAno`, `CMAnoChv1`

---

### 📌 CMMMS
- **Descrição:** Controla Mensalidades da MSINFOR
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMMMSTip`, `CMMMSQtd`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMMMSTip` | `N/D` | - |
| `CMMMSQtd` | `N/D` | - |
| `CMMMSDta` | `N/D` | - |
| `CMMMSVlr` | `N/D` | - |
| `CMMMSMed` | `N/D` | - |
| `CMMMSVlrAnt` | `N/D` | - |
| `CMMMSVlrDif` | `N/D` | - |
| `CMMMSVlrAum` | `N/D` | - |
| `CMMMSQtdFun` | `N/D` | - |

#### 🗺️ Índices
- `CMMMS1` (Unique): `CMEmpCod`, `CMFilCod`, `CMMMSTip`, `CMMMSQtd`
- `CMMMS2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CMMoe
- **Descrição:** Cadastro Moedas
- **Chave Primária:** `CMMoeCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMMoeCod` | `N/D` | - |
| `CMMoeDes` | `N/D` | - |
| `CMMoeDivMul` | `N/D` | - |
| `CMMoeDtaTrs` | `N/D` | - |
| `CMMoeCDta` | `N/D` | - |
| `CMMoeCUsu` | `N/D` | - |
| `CMMoeCPrg` | `N/D` | - |
| `CMMoeCHor` | `N/D` | - |

#### 🗺️ Índices
- `CMMoeA` (Unique): `CMMoeCod`

---

### 📌 CMMoeD
- **Descrição:** Cadastro Cotação da Moeda Diário
- **Chave Primária:** `CMMoeCod`, `CMMoeDDta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMMoeCod` | `N/D` | - |
| `CMMoeDDta` | `N/D` | - |
| `CMMoeDes` | `N/D` | - |
| `CMMoeDivMul` | `N/D` | - |
| `CMMoeDDtaTrs` | `N/D` | - |
| `CMMoeDVlr` | `N/D` | - |
| `CMMoeDtaTrs` | `N/D` | - |
| `CMMoeCDta` | `N/D` | - |
| `CMMoeCUsu` | `N/D` | - |
| `CMMoeCPrg` | `N/D` | - |
| `CMMoeCHor` | `N/D` | - |

#### 🗺️ Índices
- `CMMoeD1` (Unique): `CMMoeCod`, `CMMoeDDta`
- `CMMoeD2` (Duplicate): `CMMoeCod`

---

### 📌 CMMSA
- **Descrição:** Total Clientes MSINFOR Anual
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMMSAAno`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMMSAAno` | `N/D` | - |
| `CMMSAQtdTot` | `N/D` | - |
| `CMMSAVlrTot` | `N/D` | - |
| `CMMSAQtdNov` | `N/D` | - |
| `CMMSAMedNov` | `N/D` | - |
| `CMMSAVlrNov` | `N/D` | - |
| `CMMSAMedTot` | `N/D` | - |
| `CMMSAQtdPer` | `N/D` | - |
| `CMMSAQtdSal` | `N/D` | - |

#### 🗺️ Índices
- `CMMSA1` (Unique): `CMEmpCod`, `CMFilCod`, `CMMSAAno`
- `CMMSA2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CMMSI
- **Descrição:** Comunicação Entre MSINFOR - Clientes
- **Chave Primária:** `CMMSICOD`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMMSICOD` | `N/D` | - |
| `CMMSIHMS` | `N/D` | - |

#### 🗺️ Índices
- `CMMSIA` (Unique): `CMMSICOD`

---

### 📌 CMMSP
- **Descrição:** Total de Clientes Perdidos no Ano
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMMSAAno`, `CMMSPCli`, `CMMSPDta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMMSAAno` | `N/D` | - |
| `CMMSAQtdTot` | `N/D` | - |
| `CMMSAVlrTot` | `N/D` | - |
| `CMMSAQtdNov` | `N/D` | - |
| `CMMSAMedNov` | `N/D` | - |
| `CMMSAVlrNov` | `N/D` | - |
| `CMMSAMedTot` | `N/D` | - |
| `CMMSAQtdPer` | `N/D` | - |
| `CMMSPCli` | `N/D` | - |
| `CMMSPDta` | `N/D` | - |
| `CMMSPObs` | `N/D` | - |
| `CMMSPDes` | `N/D` | - |

#### 🗺️ Índices
- `CMMSPA` (Unique): `CMEmpCod`, `CMFilCod`, `CMMSAAno`, `CMMSPCli`, `CMMSPDta`
- `CMMSPB` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMMSAAno`

---

### 📌 CMMun
- **Descrição:** Municípios com Código do IBGE
- **Chave Primária:** `CMUFCod`, `CMMunIBGE`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMUFCod` | `N/D` | - |
| `CMMunIBGE` | `N/D` | - |
| `CMMunDes` | `N/D` | - |
| `CMMunCepIni` | `N/D` | - |
| `CMMunCepFin` | `N/D` | - |
| `CMMunUSU` | `N/D` | - |
| `CMMunTST` | `N/D` | - |
| `CMMunPRG` | `N/D` | - |
| `CMMunDesOfi` | `N/D` | - |
| `CMMunDesRec` | `N/D` | - |
| `CMMunCodDNE` | `N/D` | - |

#### 🗺️ Índices
- `CMMun1` (Unique): `CMUFCod`, `CMMunIBGE`
- `CMMun2` (Duplicate): `CMUFCod`
- `CMMun3` (Duplicate): `CMMunCepIni`
- `CMMun4` (Duplicate): `CMMunDes`

---

### 📌 CMNCM
- **Descrição:** NCM - Auxiliar
- **Chave Primária:** `CMNCMNBM`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMNCMNBM` | `N/D` | - |
| `CMNCMNBMDes` | `N/D` | - |
| `CMNCMNCM` | `N/D` | - |
| `CMNCMNCMDes` | `N/D` | - |
| `CMNCMAlNac` | `N/D` | - |
| `CMNCMAlImp` | `N/D` | - |
| `CMNCMAlEst` | `N/D` | - |

#### 🗺️ Índices
- `CMNCM1` (Unique): `CMNCMNBM`
- `CMNCM2` (Duplicate): `CMNCMNCM`

---

### 📌 CMNHD
- **Descrição:** Nro de série dos HD dos micros
- **Chave Primária:** `CMEmpCod`, `CMNHDSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMNHDSeq` | `N/D` | - |
| `CMNHDNro` | `N/D` | - |
| `CMNHDDtaUltAce` | `N/D` | - |
| `CMNHDDes` | `N/D` | - |

#### 🗺️ Índices
- `CMNHD1` (Unique): `CMEmpCod`, `CMNHDSeq`
- `CMNHD2` (Duplicate): `CMEmpCod`

---

### 📌 CMNOP
- **Descrição:** Natureza da Operação CFOP
- **Chave Primária:** `CMNOpCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMNOpCod` | `N/A(4)` | CMNopCod |
| `CMNopDtaTrs` | `N/D` | - |
| `CMNopFlaDel` | `N/D` | - |
| `CMNOpDes` | `N/D` | - |
| `CMNOpCUsu` | `N/D` | - |
| `CMNOpCPrg` | `N/D` | - |
| `CMNOpCHor` | `N/D` | - |
| `CMNOpCDta` | `N/D` | - |
| `CMNOpEnt` | `N/D` | - |
| `CMNopCom` | `N/D` | - |
| `CMNopAtuCus` | `N/D` | - |
| `CMNOpCtbAn` | `N/D` | - |
| `CMNOpCtbDs` | `N/D` | - |

#### 🗺️ Índices
- `CMNOPA` (Unique): `CMNOpCod`

---

### 📌 CMOTE
- **Descrição:** Tabela Operadoras
- **Chave Primária:** `CMOTeCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMOTeCod` | `N/D` | - |
| `CMOTeDes` | `N/D` | - |

#### 🗺️ Índices
- `CMOTE1` (Unique): `CMOTeCod`

---

### 📌 CMPm1
- **Descrição:** Parâmetros da Estação
- **Chave Primária:** `CMPm1NroMic`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMPm1NroMic` | `N/D` | - |
| `CMPm1EmpCod` | `N/D` | - |
| `CMPm1FilCod` | `N/D` | - |
| `CMPm1NomFan` | `N/D` | - |
| `CMPm1V1` | `N/D` | - |
| `CMPm1UsuNom` | `N/D` | - |
| `CMPm1ModImpFis` | `N/D` | - |
| `CMPm1ModGav` | `N/D` | - |
| `CMPm1NroLinSal` | `N/D` | - |
| `CMPm1LimTabMov` | `N/D` | - |
| `CMPm1PorSer` | `N/D` | - |
| `CMPM1CRTipCarRec` | `N/D` | - |
| `CMPM1CRModTelVdaPro` | `N/D` | - |
| `CMPM1PthInsSis` | `N/D` | - |
| `CMPM1GrvZip` | `N/D` | - |
| `CMPM1IMPCOD` | `N/D` | - |
| `CMPM1TipCxa` | `N/D` | - |
| `CMPM1PorCOMBal` | `N/D` | - |
| `CMPM1VlcPor` | `N/D` | - |
| `CMPM1BalPar` | `N/D` | - |
| `CMPM1BalBit` | `N/D` | - |
| `CMPM1VdaFis` | `N/D` | - |
| `CMPM1VdaRec` | `N/D` | - |
| `CMPM1VdaNad` | `N/D` | - |
| `CMPM1PerCPF` | `N/D` | - |
| `CMPM1GavPorSer` | `N/D` | - |
| `CMPM1Gav1Vel` | `N/D` | - |
| `CMPM1Gav2Vel` | `N/D` | - |
| `CMPM1APS` | `N/D` | - |
| `CMPM1DtaCxa` | `N/D` | - |
| `CMPM1GavPrz` | `N/D` | - |
| `CMPM1GavVis` | `N/D` | - |
| `CMPM1GavChe` | `N/D` | - |
| `CMPM1GavCar` | `N/D` | - |
| `CMPM1TipImp` | `N/D` | - |
| `CMPM1TEF` | `N/D` | - |
| `CMPM1ModBal` | `N/D` | - |
| `CMPM1UsuUso` | `N/D` | - |
| `CMPM1TefSt` | `N/D` | - |
| `CMPM1MVend` | `N/D` | - |
| `CMPM1PTHBCKNFP` | `N/D` | - |
| `CMPM1UsuAtu` | `N/D` | - |
| `CMPM1FilaSAT` | `N/D` | - |
| `CMPM1MicSAT` | `N/D` | - |
| `CMPM1PathSAT` | `N/D` | - |
| `CMPM1OpeFisSAT` | `N/D` | - |
| `CMPM1DscFisSAT` | `N/D` | - |
| `CMPM1CerTEF` | `N/D` | - |
| `CMPM1SignAC` | `N/D` | - |
| `CMPM1ALTTEL` | `N/D` | - |
| `CMPM1LARTEL` | `N/D` | - |
| `CMPM1RESMON` | `N/D` | - |
| `CMPM1NFisMod` | `N/D` | - |
| `CMPM1NFisPor` | `N/D` | - |
| `CMPM1NFisVlc` | `N/D` | - |
| `CMPM1SatCodAtiv` | `N/D` | - |
| `CMPM1SatSessao` | `N/D` | - |
| `CMPM1SatModelo` | `N/D` | - |
| `CMPM1CmdBat` | `N/D` | - |
| `CMPM1ScUsa` | `N/D` | - |
| `CMPM1ScCfg` | `N/D` | - |
| `CMPM1ScTm` | `N/D` | - |
| `CMPM1SatVer` | `N/D` | - |
| `CMPM1SatFan` | `N/D` | - |
| `CMPM1ScPth` | `N/D` | - |
| `CMPM1ScIdE` | `N/D` | - |
| `CMPM1ScUsu` | `N/D` | - |
| `CMPM1ScSen` | `N/D` | - |
| `CMPM1ScAvL` | `N/D` | - |
| `CMPM1ScVdDtRe` | `N/D` | - |
| `CMPM1ScVdQtRe` | `N/D` | - |
| `CMPM1ScFcDtRe` | `N/D` | - |
| `CMPM1ScFcQtRe` | `N/D` | - |
| `CMPM1SatPar` | `N/D` | - |
| `CMPM1Spooler` | `N/D` | - |
| `CMPM1Buffer` | `N/D` | - |
| `CMPM1CompU` | `N/D` | - |
| `CMPM1CompN` | `N/D` | - |
| `CMPM1PthM1` | `N/D` | - |
| `CMPM1PthM2` | `N/D` | - |
| `CMPM1PthM3` | `N/D` | - |
| `CMPM1ScMos` | `N/D` | - |
| `CMPM1ScLog` | `N/D` | - |
| `CMPM1ImpSat` | `N/D` | - |
| `CMPM1SatDev` | `N/D` | - |
| `CMPM1TefTm` | `N/D` | - |
| `CMPM1TefRe` | `N/D` | - |
| `CMPM1TefLg` | `N/D` | - |
| `CMPM1TefRq` | `N/D` | - |
| `CMPM1TefRs` | `N/D` | - |
| `CMPM1TefBk` | `N/D` | - |
| `CMPM1TefRd` | `N/D` | - |
| `CMPM1SatPS` | `N/D` | - |
| `CMPM1ScLoc` | `N/D` | - |
| `CMPM1ScPro` | `N/D` | - |
| `CMPM1ScDtF` | `N/D` | - |
| `CMPM1FiSat` | `N/D` | - |
| `CMPM1FrSat` | `N/D` | - |
| `CMPM1MrgEsq` | `N/D` | - |
| `CMPM1PerVda` | `N/D` | - |
| `CMPM1WebTef` | `N/D` | - |
| `CMPM1Bearer` | `N/D` | - |
| `CMPM1UserID` | `N/D` | - |
| `CMPM1LojID` | `N/D` | - |
| `CMPM1CxaID` | `N/D` | - |
| `CMPM1DevID` | `N/D` | - |
| `CMPM1SelBuy` | `N/D` | - |
| `CMPM1ImpGav` | `N/D` | - |
| `CMPM1SupTEF` | `N/D` | - |
| `CMPM1ChvCli` | `N/D` | - |
| `CMPM1IdPOS` | `N/D` | - |
| `CMPM1NomMic` | `N/D` | - |

#### 🗺️ Índices
- `CMPm11` (Unique): `CMPm1NroMic`

---

### 📌 CMPm2
- **Descrição:** Parametros
- **Chave Primária:** `CMPm2Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMPm2Cod` | `N/D` | - |
| `CMPm2EmpCod` | `N/D` | - |
| `CMPm2FilCod` | `N/D` | - |
| `CMPm2UsaMaiUmaEmp` | `N/D` | - |
| `CMPm2Usa_MaiUmaFil` | `N/D` | - |
| `CMPM2UsaFilUsu` | `N/D` | - |
| `CMPM2FilVda` | `N/D` | - |
| `CMPM2VdaFilDep` | `N/D` | - |
| `CMPM2PrxURL` | `N/D` | - |

#### 🗺️ Índices
- `CMPm21` (Unique): `CMPm2Cod`

---

### 📌 CMPMT
- **Descrição:** Parâmetros do Microterminal
- **Chave Primária:** `CMPMTCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMPMTCod` | `N/D` | - |
| `CMPMTDes` | `N/D` | - |
| `CMPMTEndIP` | `N/D` | - |
| `CMPMTPorta` | `N/D` | - |
| `CMPMTPesoB` | `N/D` | - |
| `CMPMTCProA` | `N/D` | - |
| `CMPMTDProA` | `N/D` | - |
| `CMPMTCProB` | `N/D` | - |
| `CMPMTDProB` | `N/D` | - |
| `CMPMTCProC` | `N/D` | - |
| `CMPMTDProC` | `N/D` | - |
| `CMPMTCProD` | `N/D` | - |
| `CMPMTDProD` | `N/D` | - |
| `CMPMTCProE` | `N/D` | - |
| `CMPMTDProE` | `N/D` | - |
| `CMPMTCProF` | `N/D` | - |
| `CMPMTDProF` | `N/D` | - |
| `CMPMTCProG` | `N/D` | - |
| `CMPMTDProG` | `N/D` | - |
| `CMPMTCProH` | `N/D` | - |
| `CMPMTDProH` | `N/D` | - |
| `CMPMTCProI` | `N/D` | - |
| `CMPMTDProI` | `N/D` | - |
| `CMPMTCProJ` | `N/D` | - |
| `CMPMTDProJ` | `N/D` | - |
| `CMPMTCProK` | `N/D` | - |
| `CMPMTDProK` | `N/D` | - |
| `CMPMTCProL` | `N/D` | - |
| `CMPMTDProL` | `N/D` | - |
| `CMPMTCProM` | `N/D` | - |
| `CMPMTDProM` | `N/D` | - |
| `CMPMTCProN` | `N/D` | - |
| `CMPMTDProN` | `N/D` | - |
| `CMPMTCProO` | `N/D` | - |
| `CMPMTDProO` | `N/D` | - |
| `CMPMTCProP` | `N/D` | - |
| `CMPMTDProP` | `N/D` | - |
| `CMPMTCProQ` | `N/D` | - |
| `CMPMTDProQ` | `N/D` | - |
| `CMPMTCProR` | `N/D` | - |
| `CMPMTDProR` | `N/D` | - |
| `CMPMTCProS` | `N/D` | - |
| `CMPMTDProS` | `N/D` | - |
| `CMPMTCProT` | `N/D` | - |
| `CMPMTDProT` | `N/D` | - |
| `CMPMTCProU` | `N/D` | - |
| `CMPMTDProU` | `N/D` | - |
| `CMPMTCProV` | `N/D` | - |
| `CMPMTDProV` | `N/D` | - |
| `CMPMTCProX` | `N/D` | - |
| `CMPMTDProX` | `N/D` | - |
| `CMPMTCProY` | `N/D` | - |
| `CMPMTDProY` | `N/D` | - |
| `CMPMTCProZ` | `N/D` | - |
| `CMPMTDProZ` | `N/D` | - |
| `CMPMTCPrF1` | `N/D` | - |
| `CMPMTDPrF1` | `N/D` | - |
| `CMPMTCPrS1` | `N/D` | - |
| `CMPMTDPrS1` | `N/D` | - |
| `CMPMTCPrF2` | `N/D` | - |
| `CMPMTDPrF2` | `N/D` | - |
| `CMPMTCPrS2` | `N/D` | - |
| `CMPMTDPrS2` | `N/D` | - |
| `CMPMTCPrF3` | `N/D` | - |
| `CMPMTDPrF3` | `N/D` | - |
| `CMPMTCPrS3` | `N/D` | - |
| `CMPMTDPrS3` | `N/D` | - |
| `CMPMTCPrF4` | `N/D` | - |
| `CMPMTDPrF4` | `N/D` | - |
| `CMPMTCPrS4` | `N/D` | - |
| `CMPMTDPrS4` | `N/D` | - |

#### 🗺️ Índices
- `CMPMT1` (Unique): `CMPMTCod`

---

### 📌 CMPNF
- **Descrição:** Parâmentros da NFe
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMPNFCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMFILNFECam` | `N/D` | - |
| `CMFilNFEMod` | `N/D` | - |
| `CMFilNFCEMod` | `N/D` | - |
| `CMFilNFEDM` | `N/D` | - |
| `CMFilNFEDTp` | `N/D` | - |
| `CMFilNFCEDM` | `N/D` | - |
| `CMFilNFCETp` | `N/D` | - |
| `CMPNFCod` | `N/D` | - |
| `CMPNFDsc` | `N/D` | - |
| `CMPNFNota` | `N/D` | - |
| `CMPNFSerie` | `N/D` | - |
| `CMPNFImp` | `N/D` | - |
| `CMPNFSta` | `N/D` | - |
| `CMPNFCop` | `N/D` | - |
| `CMPNFVisImp` | `N/D` | - |

#### 🗺️ Índices
- `CMPNF1` (Unique): `CMEmpCod`, `CMFilCod`, `CMPNFCod`
- `CMPNF2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CMPrD
- **Descrição:** Manutenção da Descrição Programa - MSINFOR
- **Chave Primária:** `CMPrDNom`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMPrDNom` | `N/D` | - |
| `CMPrDDes` | `N/D` | - |
| `CMPrDDesAux` | `N/D` | - |
| `CMPrDSis` | `N/D` | - |

#### 🗺️ Índices
- `CMPrDA` (Unique): `CMPrDNom`

---

### 📌 CMPrF
- **Descrição:** Programas - Parâmetros por Filial
- **Chave Primária:** `CMEmpCod`, `CMPrFFil`, `CMPrgnom`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMPrFFil` | `N/D` | - |
| `CMPrgnom` | `N/D` | - |
| `CMPrFDtaIni` | `N/D` | - |
| `CMPrFDtaFin` | `N/D` | - |
| `CMPrFModRel` | `N/D` | - |
| `CMPrFTST` | `N/D` | - |
| `CMPrFCmp01` | `N/D` | - |
| `CMPrFCmp02` | `N/D` | - |
| `CMPrFCmp03` | `N/D` | - |
| `CMPrFCmp04` | `N/D` | - |
| `CMPrFCmp05` | `N/D` | - |
| `CMPrFCmp06` | `N/D` | - |
| `CMPrFCmp07` | `N/D` | - |
| `CMPrFCmp08` | `N/D` | - |
| `CMPrFCmp09` | `N/D` | - |
| `CMPrFCmp10` | `N/D` | - |
| `CMPrFCmp11` | `N/D` | - |
| `CMPrFCmp12` | `N/D` | - |
| `CMPrFCmp13` | `N/D` | - |
| `CMPrFCmp14` | `N/D` | - |
| `CMPrFCmp15` | `N/D` | - |
| `CMPrFPth01` | `N/D` | - |
| `CMPrFPth02` | `N/D` | - |
| `CMPrFNro01` | `N/D` | - |
| `CMPrFNro02` | `N/D` | - |
| `CMPrFNro03` | `N/D` | - |
| `CMPrFNro04` | `N/D` | - |
| `CMPrFNro05` | `N/D` | - |
| `CMPrFNro06` | `N/D` | - |
| `CMPrFNro07` | `N/D` | - |
| `CMPrFNro08` | `N/D` | - |
| `CMPrFNro09` | `N/D` | - |
| `CMPrFNro10` | `N/D` | - |
| `CMPrFPrinter` | `N/D` | - |
| `CMPrFCmp36` | `N/D` | - |
| `CMPrFCmp37` | `N/D` | - |
| `CMPrFCmp38` | `N/D` | - |
| `CMPrFCmp39` | `N/D` | - |
| `CMPrFCmp40` | `N/D` | - |
| `CMPrFCmp41` | `N/D` | - |
| `CMPrFCmp42` | `N/D` | - |
| `CMPrFCmp43` | `N/D` | - |
| `CMPrFCmp44` | `N/D` | - |
| `CMPrFCmp45` | `N/D` | - |
| `CMPrfCmp46` | `N/D` | - |
| `CMPrFCmp47` | `N/D` | - |
| `CMPrFCmp48` | `N/D` | - |
| `CMPrFCmp49` | `N/D` | - |
| `CMPrFCmp50` | `N/D` | - |
| `CMPrFCmp51` | `N/D` | - |
| `CMPrFCmp52` | `N/D` | - |
| `CMPrFCmp53` | `N/D` | - |
| `CMPrFCmp54` | `N/D` | - |
| `CMPrFCmp55` | `N/D` | - |
| `CMPrFCmp56` | `N/D` | - |
| `CMPrFCmp57` | `N/D` | - |
| `CMPrFCmp58` | `N/D` | - |
| `CMPrFCmp59` | `N/D` | - |
| `CMPrFCmp60` | `N/D` | - |
| `CMPrFCmp61` | `N/D` | - |
| `CMPrFCmp62` | `N/D` | - |
| `CMPrFCmp63` | `N/D` | - |
| `CMPrFCmp64` | `N/D` | - |
| `CMPrFCmp65` | `N/D` | - |
| `CMPrFCmp66` | `N/D` | - |
| `CMPrFCmp67` | `N/D` | - |
| `CMPrFCmp68` | `N/D` | - |
| `CMPrFCmp69` | `N/D` | - |
| `CMPrFCmp70` | `N/D` | - |
| `CMPrFCmp71` | `N/D` | - |
| `CMPrFCmp72` | `N/D` | - |
| `CMPrFCmp73` | `N/D` | - |
| `CMPrFCmp74` | `N/D` | - |
| `CMPrFCmp75` | `N/D` | - |
| `CMPrFCmp76` | `N/D` | - |
| `CMPrFCmp77` | `N/D` | - |
| `CMPrFCmp78` | `N/D` | - |
| `CMPrFCmp79` | `N/D` | - |
| `CMPrFCmp80` | `N/D` | - |

#### 🗺️ Índices
- `CMPrF1` (Unique): `CMEmpCod`, `CMPrFFil`, `CMPrgnom`
- `CmPrF2` (Duplicate): `CMEmpCod`, `CMPrgnom`

---

### 📌 CMPrg
- **Descrição:** Programas
- **Chave Primária:** `CMEmpCod`, `CMPrgnom`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMPrgnom` | `N/D` | - |
| `CMPrgDesBot` | `N/D` | - |
| `CMPrgdes` | `N/D` | - |
| `CMPrgAutNec` | `N/D` | - |
| `CMPrgCUsu` | `N/D` | - |
| `CMPrgCHor` | `N/D` | - |
| `CMPrgCDta` | `N/D` | - |
| `CMPrgCPrg` | `N/D` | - |
| `CMPrgDtaTrs` | `N/D` | - |
| `CMPrgFlaDel` | `N/D` | - |
| `CMPrgCmp01` | `N/D` | - |
| `CMPrgCmp02` | `N/D` | - |
| `CMPrgCmp03` | `N/D` | - |
| `CMPrgCmp04` | `N/D` | - |
| `CMPrgCmp05` | `N/D` | - |
| `CMEmpMoeCodPad` | `N/D` | - |
| `CMPrgCmp06` | `N/D` | - |
| `CMPrgCmp07` | `N/D` | - |
| `CMPrgCmp08` | `N/D` | - |
| `CMPrgCmp09` | `N/D` | - |
| `CMPrgCmp10` | `N/D` | - |
| `CMPrgCmp11` | `N/D` | - |
| `CMPrgCmp12` | `N/D` | - |
| `CMPrgCmp13` | `N/D` | - |
| `CMPrgCmp14` | `N/D` | - |
| `CMPrgCmp15` | `N/D` | - |
| `CMPrgCmp16` | `N/D` | - |
| `CMPrgCmp17` | `N/D` | - |
| `CMPrgCmp18` | `N/D` | - |
| `CMPrgCmp19` | `N/D` | - |
| `CMPrgCmp20` | `N/D` | - |
| `CMPrgCmp21` | `N/D` | - |
| `CMPrgCmp22` | `N/D` | - |
| `CMPrgCmp23` | `N/D` | - |
| `CMPrgCmp24` | `N/D` | - |
| `CMPrgCmp25` | `N/D` | - |
| `CMPrgCmp26` | `N/D` | - |
| `CMPrgCmp27` | `N/D` | - |
| `CMPrgCmp28` | `N/D` | - |
| `CMPrgCmp29` | `N/D` | - |
| `CMPrgCmp30` | `N/D` | - |
| `CMPrgCmp31` | `N/D` | - |
| `CMPrgCmp32` | `N/D` | - |
| `CMPrgCmp33` | `N/D` | - |
| `CMPrgCmp34` | `N/D` | - |
| `CMPrgCmp35` | `N/D` | - |
| `CMPrgLib` | `N/D` | - |
| `CMPrgDesMSI` | `N/D` | - |
| `CMPrgCmp36` | `N/D` | - |
| `CMPrgCmp37` | `N/D` | - |
| `CMPrgCmp38` | `N/D` | - |
| `CMPrgCmp39` | `N/D` | - |
| `CMPrgCmp40` | `N/D` | - |
| `CMPrgCmp41` | `N/D` | - |
| `CMPrgCmp42` | `N/D` | - |
| `CMPrgCmp43` | `N/D` | - |
| `CMPrgCmp44` | `N/D` | - |
| `CMPrgCmp45` | `N/D` | - |
| `CMPrgCmp46` | `N/D` | - |
| `CMPrgCmp47` | `N/D` | - |
| `CMPrgCmp48` | `N/D` | - |
| `CMPrgCmp49` | `N/D` | - |
| `CMPrgCmp50` | `N/D` | - |
| `CMPrgCmp51` | `N/D` | - |
| `CMPrgCmp52` | `N/D` | - |
| `CMPrgCmp53` | `N/D` | - |
| `CMPrgCmp54` | `N/D` | - |
| `CMPrgCmp55` | `N/D` | - |
| `CMPrgCmp56` | `N/D` | - |
| `CMPrgCmp57` | `N/D` | - |
| `CMPrgCmp58` | `N/D` | - |
| `CMPrgCmp59` | `N/D` | - |
| `CMPrgCmp60` | `N/D` | - |

#### 🗺️ Índices
- `CMPrg1` (Unique): `CMEmpCod`, `CMPrgnom`
- `CMPrg2` (Duplicate): `CMEmpCod`

---

### 📌 CMPro
- **Descrição:** Cadastro Profissionais
- **Chave Primária:** `CMProCod`, `CMProTip`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMProCod` | `N/D` | - |
| `CMProTip` | `N/D` | - |
| `CMProDes` | `N/D` | - |
| `CMProUFCons` | `N/D` | - |
| `CMProSts` | `N/D` | - |

#### 🗺️ Índices
- `CMProA` (Unique): `CMProCod`, `CMProTip`

---

### 📌 CMPUL
- **Descrição:** Programas Utilizados Local
- **Chave Primária:** `CMPULCodMs`, `CMPULProNa`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMPULCodMs` | `N/D` | - |
| `CMPULProNa` | `N/D` | - |
| `CMPULQtdeA` | `N/D` | - |

#### 🗺️ Índices
- `CMPUL1` (Unique): `CMPULCodMs`, `CMPULProNa`

---

### 📌 CMTAB
- **Descrição:** Tabelas do Sistema
- **Chave Primária:** `CMTabNom`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMTabNom` | `N/D` | - |
| `CMTabDes` | `N/D` | - |
| `CMTabOpr` | `N/D` | - |

#### 🗺️ Índices
- `CMTAB1` (Unique): `CMTabNom`

---

### 📌 CMTBC
- **Descrição:** Campos das Tabelas
- **Chave Primária:** `CMTBNNom`, `CMTBCNom`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMTBNNom` | `N/D` | - |
| `CMTBNTst` | `N/D` | - |
| `CMTBNTip` | `N/D` | - |
| `CMTBNSts` | `N/D` | - |
| `CMTBCNom` | `N/D` | - |
| `CMTBCTip` | `N/D` | - |
| `CMTBCTam` | `N/D` | - |
| `CMTBCDec` | `N/D` | - |
| `CMTBCNul` | `N/D` | - |
| `CMTBCPK` | `N/D` | - |

#### 🗺️ Índices
- `CMTBCA` (Unique): `CMTBNNom`, `CMTBCNom`
- `CMTBCB` (Duplicate): `CMTBNNom`
- `CMTBC` (Duplicate): `CMTBCPK`, `CMTBCNom`

---

### 📌 CMTBN
- **Descrição:** Grava Nomes Tabelas do Sistema e os Campos - Via Instrução SQL
- **Chave Primária:** `CMTBNNom`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMTBNNom` | `N/D` | - |
| `CMTBNTst` | `N/D` | - |
| `CMTBNTip` | `N/D` | - |
| `CMTBNSts` | `N/D` | - |

#### 🗺️ Índices
- `CMTBNA` (Unique): `CMTBNNom`

---

### 📌 CMTFF
- **Descrição:** Transferência Entre Filiais
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMTFFFil`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMTFFFil` | `N/D` | - |
| `CMTFFSts` | `N/D` | - |

#### 🗺️ Índices
- `CMTFF1` (Unique): `CMEmpCod`, `CMFilCod`, `CMTFFFil`
- `CMTFF2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CMTip
- **Descrição:** Temporaria Tipo Cliente\Fornec
- **Chave Primária:** `CMEmpCod`, `CMTipCod`, `CMTipCF`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMTipCod` | `N/D` | - |
| `CMTipCF` | `N/D` | - |
| `CMTipDes` | `N/D` | - |
| `CMTipCHor` | `N/D` | - |
| `CMTipCUsu` | `N/D` | - |
| `CMTipCDta` | `N/D` | - |
| `CMTipDtaTrs` | `N/D` | - |
| `CMTipFlaDel` | `N/D` | - |

#### 🗺️ Índices
- `CMTip1` (Unique): `CMEmpCod`, `CMTipCod`, `CMTipCF`
- `CMTip2` (Duplicate): `CMEmpCod`
- `CMTip3` (Duplicate): `CMEmpCod`, `CMTipDes`

---

### 📌 CMTM1
- **Descrição:** Temporária Genérica
- **Chave Primária:** `CMTM1CHV1`, `CMTM1CHV2`, `CMTM1CHV3`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMTM1CHV1` | `N/D` | - |
| `CMTM1CHV2` | `N/D` | - |
| `CMTM1CHV3` | `N/D` | - |
| `CMTM1COD1` | `N/D` | - |
| `CMTM1COD2` | `N/D` | - |
| `CMTM1COD3` | `N/D` | - |
| `CMTM1COD4` | `N/D` | - |
| `CMTM1DSC1` | `N/D` | - |
| `CMTM1DSC2` | `N/D` | - |
| `CMTM1DSC3` | `N/D` | - |
| `CMTM1DSC4` | `N/D` | - |

#### 🗺️ Índices
- `CMTM1A` (Unique): `CMTM1CHV1`, `CMTM1CHV2`, `CMTM1CHV3`

---

### 📌 CMTM2
- **Descrição:** Temporária Genérica 02
- **Chave Primária:** `CMTM2CHV01`, `CMTM2CHV02`, `CMTM2CHV03`, `CMTM2CHV04`, `CMTM2CHV05`, `CMTM2CHV06`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMTM2CHV01` | `N/D` | - |
| `CMTM2CHV02` | `N/D` | - |
| `CMTM2CHV03` | `N/D` | - |
| `CMTM2CHV04` | `N/D` | - |
| `CMTM2CHV05` | `N/D` | - |
| `CMTM2CHV06` | `N/D` | - |
| `CMTM2CHV07` | `N/D` | - |
| `CMTM2NRO01` | `N/D` | - |
| `CMTM2NRO02` | `N/D` | - |
| `CMTM2NRO03` | `N/D` | - |
| `CMTM2Usu` | `N/D` | - |
| `CMTM2Fil` | `N/D` | - |
| `CMTM2Emp` | `N/D` | - |
| `CMTM2Prg` | `N/D` | - |
| `CMTM2NRO04` | `N/D` | - |
| `CMTM2NRO05` | `N/D` | - |
| `CMTM2NRO06` | `N/D` | - |
| `CMTM2NRO07` | `N/D` | - |
| `CMTM2NRO08` | `N/D` | - |
| `CMTM2NRO09` | `N/D` | - |
| `CMTM2NRO10` | `N/D` | - |
| `CMTM2NRO11` | `N/D` | - |
| `CMTM2NRO12` | `N/D` | - |
| `CMTM2VLR01` | `N/D` | - |
| `CMTM2VLR02` | `N/D` | - |
| `CMTM2VLR03` | `N/D` | - |
| `CMTM2VLR04` | `N/D` | - |
| `CMTM2VLR05` | `N/D` | - |
| `CMTM2VLR06` | `N/D` | - |
| `CMTM2VLR07` | `N/D` | - |
| `CMTM2VLR08` | `N/D` | - |
| `CMTM2VLR09` | `N/D` | - |
| `CMTM2VLR10` | `N/D` | - |
| `CMTM2VLR11` | `N/D` | - |
| `CMTM2VLR12` | `N/D` | - |
| `CMTM2VLR13` | `N/D` | - |
| `CMTM2VLR14` | `N/D` | - |
| `CMTM2VLR15` | `N/D` | - |
| `CMTM2VLR16` | `N/D` | - |
| `CMTM2VLR17` | `N/D` | - |
| `CMTM2VLR18` | `N/D` | - |
| `CMTM2VLR19` | `N/D` | - |
| `CMTM2VLR20` | `N/D` | - |
| `CMTM2VLR21` | `N/D` | - |
| `CMTM2VLR22` | `N/D` | - |
| `CMTM2VLR23` | `N/D` | - |
| `CMTM2VLR24` | `N/D` | - |
| `CMTM2VLR25` | `N/D` | - |
| `CMTM2CHA01` | `N/D` | - |
| `CMTM2CHA02` | `N/D` | - |
| `CMTM2CHA03` | `N/D` | - |
| `CMTM2CHA04` | `N/D` | - |
| `CMTM2CHA05` | `N/D` | - |
| `CMTM2CHA06` | `N/D` | - |
| `CMTM2CHA07` | `N/D` | - |
| `CMTM2CHA08` | `N/D` | - |
| `CMTM2CHA09` | `N/D` | - |
| `CMTM2CHA10` | `N/D` | - |
| `CMTM2CHA11` | `N/D` | - |
| `CMTM2CHA12` | `N/D` | - |
| `CMTM2DTA01` | `N/D` | - |
| `CMTM2DTA02` | `N/D` | - |
| `CMTM2DTA03` | `N/D` | - |
| `CMTM2DTA04` | `N/D` | - |
| `CMTM2DTA05` | `N/D` | - |

#### 🗺️ Índices
- `CMTM2A` (Unique): `CMTM2CHV01`, `CMTM2CHV02`, `CMTM2CHV03`, `CMTM2CHV04`, `CMTM2CHV05`, `CMTM2CHV06`
- `CMTM2B` (Duplicate): `CMTM2Usu`, `CMTM2Prg`, `CMTM2Emp`, `CMTM2Fil`
- `CMTM2C` (Duplicate): `CMTM2CHV06`

---

### 📌 CMTMS
- **Descrição:** Telefones da MS-Informática
- **Chave Primária:** `CMTMSCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMTMSCod` | `N/D` | - |
| `CMTMSDes` | `N/D` | - |
| `CMTMSSTS` | `N/D` | - |

#### 🗺️ Índices
- `CMTMSA` (Unique): `CMTMSCod`

---

### 📌 CMTOP
- **Descrição:** Natureza Operação Fiscal
- **Chave Primária:** `CMTOPCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMTOPCod` | `N/D` | - |
| `CMTOPDes` | `N/D` | - |
| `CMTOPCSTSER` | `N/D` | - |
| `CMTOPUSU` | `N/D` | - |
| `CMTOPTST` | `N/D` | - |
| `CMTOPPRG` | `N/D` | - |
| `CMTopTip` | `N/D` | - |
| `CMTopIntEst` | `N/D` | - |
| `CMTOPCST00` | `N/D` | - |
| `CMTOPCST10` | `N/D` | - |
| `CMTOPCST20` | `N/D` | - |
| `CMTOPCST30` | `N/D` | - |
| `CMTOPCST40` | `N/D` | - |
| `CMTOPCST41` | `N/D` | - |
| `CMTOPCST50` | `N/D` | - |
| `CMTOPCST51` | `N/D` | - |
| `CMTOPCST60` | `N/D` | - |
| `CMTOPCST61` | `N/D` | - |
| `CMTOPCST70` | `N/D` | - |
| `CMTOPCST90` | `N/D` | - |
| `CMTOPRedBC` | `N/D` | - |
| `CMTOPST` | `N/D` | - |
| `CMTOPObs1` | `N/D` | - |
| `CMTOPObs2` | `N/D` | - |
| `CMTOPObs3` | `N/D` | - |
| `CMTOPObs4` | `N/D` | - |
| `CMTOPObs5` | `N/D` | - |
| `CMTOPObs6` | `N/D` | - |
| `CMTOPICMS` | `N/D` | - |
| `CMTOPIPI` | `N/D` | - |
| `CMTOPPISCOF` | `N/D` | - |
| `CMTOPVda` | `N/D` | - |
| `CMTOPE_S` | `N/D` | - |
| `CMTOP00CSOSN` | `N/D` | - |
| `CMTOP10CSOSN` | `N/D` | - |
| `CMTOP20CSOSN` | `N/D` | - |
| `CMTOP30CSOSN` | `N/D` | - |
| `CMTOP40CSOSN` | `N/D` | - |
| `CMTOP41CSOSN` | `N/D` | - |
| `CMTOP50CSOSN` | `N/D` | - |
| `CMTOP51CSOSN` | `N/D` | - |
| `CMTOP60CSOSN` | `N/D` | - |
| `CMTOP61CSOSN` | `N/D` | - |
| `CMTOP70CSOSN` | `N/D` | - |
| `CMTOP90CSOSN` | `N/D` | - |
| `CMTopCalImpAut` | `N/D` | - |
| `CMTopVdaSim` | `N/D` | - |
| `CMTOPFrt` | `N/D` | - |
| `CMTOPDsp` | `N/D` | - |
| `CMTOPISS` | `N/D` | - |
| `CMTOPDsc` | `N/D` | - |
| `CMTOPSomFre` | `N/D` | - |
| `CMTOPNFOri` | `N/D` | - |
| `CMTopCSTPis` | `N/D` | - |
| `CMTopCSTCof` | `N/D` | - |
| `CMTopPerPis` | `N/D` | - |
| `CMTopPerCof` | `N/D` | - |
| `CMTopCupFis` | `N/D` | - |
| `CMTOPNST00` | `N/D` | - |
| `CMTOPNST10` | `N/D` | - |
| `CMTOPNST20` | `N/D` | - |
| `CMTOPNST30` | `N/D` | - |
| `CMTOPNST40` | `N/D` | - |
| `CMTOPNST41` | `N/D` | - |
| `CMTOPNST50` | `N/D` | - |
| `CMTOPNST51` | `N/D` | - |
| `CMTOPNST60` | `N/D` | - |
| `CMTOPNST61` | `N/D` | - |
| `CMTOPNST70` | `N/D` | - |
| `CMTOPNST90` | `N/D` | - |
| `CMTOPPeR00` | `N/D` | - |
| `CMTOPPeR10` | `N/D` | - |
| `CMTOPPeR20` | `N/D` | - |
| `CMTOPPeR30` | `N/D` | - |
| `CMTOPPeR40` | `N/D` | - |
| `CMTOPPeR41` | `N/D` | - |
| `CMTOPPeR50` | `N/D` | - |
| `CMTOPPeR51` | `N/D` | - |
| `CMTOPPeR60` | `N/D` | - |
| `CMTOPPeR70` | `N/D` | - |
| `CMTOPPeR90` | `N/D` | - |
| `CMTOPPeI00` | `N/D` | - |
| `CMTOPPeI10` | `N/D` | - |
| `CMTOPPeI20` | `N/D` | - |
| `CMTOPPeI30` | `N/D` | - |
| `CMTOPPeI40` | `N/D` | - |
| `CMTOPPeI41` | `N/D` | - |
| `CMTOPPeI50` | `N/D` | - |
| `CMTOPPeI51` | `N/D` | - |
| `CMTOPPeI60` | `N/D` | - |
| `CMTOPPeI61` | `N/D` | - |
| `CMTOPPeI70` | `N/D` | - |
| `CMTOPPeI90` | `N/D` | - |
| `CMTOPIcmDisp` | `N/D` | - |
| `CMTOPDifAl` | `N/D` | - |
| `CMTOPVrUn` | `N/D` | - |
| `CMTOPPeA00` | `N/D` | - |
| `CMTOPPeA10` | `N/D` | - |
| `CMTOPPeA20` | `N/D` | - |
| `CMTOPPeA30` | `N/D` | - |
| `CMTOPPeA40` | `N/D` | - |
| `CMTOPPeA41` | `N/D` | - |
| `CMTOPPeA50` | `N/D` | - |
| `CMTOPPeA51` | `N/D` | - |
| `CMTOPPeA60` | `N/D` | - |
| `CMTOPPeA61` | `N/D` | - |
| `CMTOPPeA70` | `N/D` | - |
| `CMTOPPeA90` | `N/D` | - |
| `CMTOPMsgV` | `N/D` | - |
| `CMTOPCliFor` | `N/D` | - |
| `CMTOPREF` | `N/D` | - |
| `CMTOPEstNeg` | `N/D` | - |
| `CMTOPCFEnt` | `N/D` | - |
| `CMTOPSomIPI` | `N/D` | - |
| `CMTOPCmpICMS` | `N/D` | - |
| `CMTOPAliInt` | `N/D` | - |
| `CMTOPDstICMS` | `N/D` | - |
| `CMTOPUPis` | `N/D` | - |
| `CMTOPUCof` | `N/D` | - |
| `CMTOPFinNF` | `N/D` | - |
| `CMTOPMot20` | `N/D` | - |
| `CMTOPAImob` | `N/D` | - |
| `CMTOPArrST` | `N/D` | - |
| `CMTOPIcmPDest` | `N/D` | - |
| `CMTOPFilCod` | `N/D` | - |
| `CMTOPRegEstSim` | `N/D` | - |
| `CMTOPObs87` | `N/D` | - |
| `CMTOPIncNroCup` | `N/D` | - |
| `CMTOPIndFinal` | `N/D` | - |
| `CMTOPPis00` | `N/D` | - |
| `CMTOPPis10` | `N/D` | - |
| `CMTOPPis20` | `N/D` | - |
| `CMTOPPis30` | `N/D` | - |
| `CMTOPPis40` | `N/D` | - |
| `CMTOPPis41` | `N/D` | - |
| `CMTOPPis50` | `N/D` | - |
| `CMTOPPis51` | `N/D` | - |
| `CMTOPPis60` | `N/D` | - |
| `CMTOPPis61` | `N/D` | - |
| `CMTOPPis70` | `N/D` | - |
| `CMTOPPis90` | `N/D` | - |
| `CMTOPPAl00` | `N/D` | - |
| `CMTOPPAl10` | `N/D` | - |
| `CMTOPPAl20` | `N/D` | - |
| `CMTOPPAl30` | `N/D` | - |
| `CMTOPPAl40` | `N/D` | - |
| `CMTOPPAl41` | `N/D` | - |
| `CMTOPPAl50` | `N/D` | - |
| `CMTOPPAl51` | `N/D` | - |
| `CMTOPPAl60` | `N/D` | - |
| `CMTOPPAl61` | `N/D` | - |
| `CMTOPPAl70` | `N/D` | - |
| `CMTOPPAl90` | `N/D` | - |
| `CMTOPCof00` | `N/D` | - |
| `CMTOPCof10` | `N/D` | - |
| `CMTOPCof20` | `N/D` | - |
| `CMTOPCof30` | `N/D` | - |
| `CMTOPCof40` | `N/D` | - |
| `CMTOPCof41` | `N/D` | - |
| `CMTOPCof50` | `N/D` | - |
| `CMTOPCof51` | `N/D` | - |
| `CMTOPCof60` | `N/D` | - |
| `CMTOPCof61` | `N/D` | - |
| `CMTOPCof70` | `N/D` | - |
| `CMTOPCof90` | `N/D` | - |
| `CMTOPCAl00` | `N/D` | - |
| `CMTOPCAl10` | `N/D` | - |
| `CMTOPCAl20` | `N/D` | - |
| `CMTOPCAl30` | `N/D` | - |
| `CMTOPCAl40` | `N/D` | - |
| `CMTOPCAl41` | `N/D` | - |
| `CMTOPCAl50` | `N/D` | - |
| `CMTOPCAl51` | `N/D` | - |
| `CMTOPCAl60` | `N/D` | - |
| `CMTOPCAl61` | `N/D` | - |
| `CMTOPCAl70` | `N/D` | - |
| `CMTOPCAl90` | `N/D` | - |
| `CMTOPPeFCP` | `N/D` | - |
| `CMTOPMBc20` | `N/D` | - |
| `CMTOPIPICST` | `N/D` | - |
| `CMTOPIndPres` | `N/D` | - |
| `CMTOPAvOpI` | `N/D` | - |
| `CMTOPFS201` | `N/D` | - |
| `CMTOPFS202` | `N/D` | - |
| `CMTOPFC500` | `N/D` | - |
| `CMTOPFR500` | `N/D` | - |
| `CMTOPFS900` | `N/D` | - |
| `CMTOPFC00` | `N/D` | - |
| `CMTOPFC10` | `N/D` | - |
| `CMTOPFS10` | `N/D` | - |
| `CMTOPFC20` | `N/D` | - |
| `CMTOPFS30` | `N/D` | - |
| `CMTOPFC51` | `N/D` | - |
| `CMTOPFR60` | `N/D` | - |
| `CMTOPFC70` | `N/D` | - |
| `CMTOPFS70` | `N/D` | - |
| `CMTOPFC90` | `N/D` | - |
| `CMTOPFS90` | `N/D` | - |
| `CMTOPBProU` | `N/D` | - |
| `CMTOPTotTrib` | `N/D` | - |
| `CMTOPVlrTriApr` | `N/D` | - |
| `CMTOPSelNFCP` | `N/D` | - |
| `CMTOPObsEE` | `N/D` | - |
| `CMTOPPerAliMon` | `N/D` | - |
| `CMTopFrePisCof` | `N/D` | - |
| `CMTopEmpCod` | `N/D` | - |
| `CMTopArrIBS` | `N/D` | - |
| `CMTopArrCBS` | `N/D` | - |
| `CMTopCalcRT` | `N/D` | - |
| `CMTop00cBenef` | `N/D` | - |
| `CMTop10cBenef` | `N/D` | - |
| `CMTop20cBenef` | `N/D` | - |
| `CMTop30cBenef` | `N/D` | - |
| `CMTop40cBenef` | `N/D` | - |
| `CMTop41cBenef` | `N/D` | - |
| `CMTop50cBenef` | `N/D` | - |
| `CMTop51cBenef` | `N/D` | - |
| `CMTop60cBenef` | `N/D` | - |
| `CMTop61cBenef` | `N/D` | - |
| `CMTop70cBenef` | `N/D` | - |
| `CMTop90cBenef` | `N/D` | - |

#### 🗺️ Índices
- `CMTOP1` (Unique): `CMTOPCod`
- `CMTOP2` (Duplicate): `CMTOPDes`

---

### 📌 CMTOPR
- **Descrição:** Classificação Tribuária Por Tipo de Operação (Reforma Tributária)
- **Chave Primária:** `CMTOPCod`, `CMTopRCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMTOPCod` | `N/D` | - |
| `CMTOPDes` | `N/D` | - |
| `CMTOPCSTSER` | `N/D` | - |
| `CMTOPUSU` | `N/D` | - |
| `CMTOPTST` | `N/D` | - |
| `CMTOPPRG` | `N/D` | - |
| `CMTopTip` | `N/D` | - |
| `CMTopIntEst` | `N/D` | - |
| `CMTOPCST00` | `N/D` | - |
| `CMTOPCST10` | `N/D` | - |
| `CMTOPCST20` | `N/D` | - |
| `CMTOPCST30` | `N/D` | - |
| `CMTOPCST40` | `N/D` | - |
| `CMTOPCST41` | `N/D` | - |
| `CMTOPCST50` | `N/D` | - |
| `CMTOPCST51` | `N/D` | - |
| `CMTOPCST60` | `N/D` | - |
| `CMTOPCST61` | `N/D` | - |
| `CMTOPCST70` | `N/D` | - |
| `CMTOPCST90` | `N/D` | - |
| `CMTOPRedBC` | `N/D` | - |
| `CMTOPST` | `N/D` | - |
| `CMTOPObs1` | `N/D` | - |
| `CMTOPObs2` | `N/D` | - |
| `CMTOPObs3` | `N/D` | - |
| `CMTOPObs4` | `N/D` | - |
| `CMTOPObs5` | `N/D` | - |
| `CMTOPObs6` | `N/D` | - |
| `CMTOPICMS` | `N/D` | - |
| `CMTOPIPI` | `N/D` | - |
| `CMTOPPISCOF` | `N/D` | - |
| `CMTOPVda` | `N/D` | - |
| `CMTOPE_S` | `N/D` | - |
| `CMTOP00CSOSN` | `N/D` | - |
| `CMTOP10CSOSN` | `N/D` | - |
| `CMTOP20CSOSN` | `N/D` | - |
| `CMTOP30CSOSN` | `N/D` | - |
| `CMTOP40CSOSN` | `N/D` | - |
| `CMTOP41CSOSN` | `N/D` | - |
| `CMTOP50CSOSN` | `N/D` | - |
| `CMTOP51CSOSN` | `N/D` | - |
| `CMTOP60CSOSN` | `N/D` | - |
| `CMTOP61CSOSN` | `N/D` | - |
| `CMTOP70CSOSN` | `N/D` | - |
| `CMTOP90CSOSN` | `N/D` | - |
| `CMTopCalImpAut` | `N/D` | - |
| `CMTopVdaSim` | `N/D` | - |
| `CMTOPFrt` | `N/D` | - |
| `CMTOPDsp` | `N/D` | - |
| `CMTOPISS` | `N/D` | - |
| `CMTOPDsc` | `N/D` | - |
| `CMTOPSomFre` | `N/D` | - |
| `CMTOPNFOri` | `N/D` | - |
| `CMTopCSTPis` | `N/D` | - |
| `CMTopCSTCof` | `N/D` | - |
| `CMTopPerPis` | `N/D` | - |
| `CMTopPerCof` | `N/D` | - |
| `CMTopCupFis` | `N/D` | - |
| `CMTOPNST00` | `N/D` | - |
| `CMTOPNST10` | `N/D` | - |
| `CMTOPNST20` | `N/D` | - |
| `CMTOPNST30` | `N/D` | - |
| `CMTOPNST40` | `N/D` | - |
| `CMTOPNST41` | `N/D` | - |
| `CMTOPNST50` | `N/D` | - |
| `CMTOPNST51` | `N/D` | - |
| `CMTOPNST60` | `N/D` | - |
| `CMTOPNST61` | `N/D` | - |
| `CMTOPNST70` | `N/D` | - |
| `CMTOPNST90` | `N/D` | - |
| `CMTOPPeR00` | `N/D` | - |
| `CMTOPPeR10` | `N/D` | - |
| `CMTOPPeR20` | `N/D` | - |
| `CMTOPPeR30` | `N/D` | - |
| `CMTOPPeR40` | `N/D` | - |
| `CMTOPPeR41` | `N/D` | - |
| `CMTOPPeR50` | `N/D` | - |
| `CMTOPPeR51` | `N/D` | - |
| `CMTOPPeR60` | `N/D` | - |
| `CMTOPPeR70` | `N/D` | - |
| `CMTOPPeR90` | `N/D` | - |
| `CMTOPPeI00` | `N/D` | - |
| `CMTOPPeI10` | `N/D` | - |
| `CMTOPPeI20` | `N/D` | - |
| `CMTOPPeI30` | `N/D` | - |
| `CMTOPPeI40` | `N/D` | - |
| `CMTOPPeI41` | `N/D` | - |
| `CMTOPPeI50` | `N/D` | - |
| `CMTOPPeI51` | `N/D` | - |
| `CMTOPPeI60` | `N/D` | - |
| `CMTOPPeI61` | `N/D` | - |
| `CMTOPPeI70` | `N/D` | - |
| `CMTOPPeI90` | `N/D` | - |
| `CMTOPIcmDisp` | `N/D` | - |
| `CMTOPDifAl` | `N/D` | - |
| `CMTOPVrUn` | `N/D` | - |
| `CMTOPPeA00` | `N/D` | - |
| `CMTOPPeA10` | `N/D` | - |
| `CMTOPPeA20` | `N/D` | - |
| `CMTOPPeA30` | `N/D` | - |
| `CMTOPPeA40` | `N/D` | - |
| `CMTOPPeA41` | `N/D` | - |
| `CMTOPPeA50` | `N/D` | - |
| `CMTOPPeA51` | `N/D` | - |
| `CMTOPPeA60` | `N/D` | - |
| `CMTOPPeA61` | `N/D` | - |
| `CMTOPPeA70` | `N/D` | - |
| `CMTOPPeA90` | `N/D` | - |
| `CMTOPMsgV` | `N/D` | - |
| `CMTOPCliFor` | `N/D` | - |
| `CMTOPREF` | `N/D` | - |
| `CMTOPEstNeg` | `N/D` | - |
| `CMTOPCFEnt` | `N/D` | - |
| `CMTOPSomIPI` | `N/D` | - |
| `CMTOPCmpICMS` | `N/D` | - |
| `CMTOPAliInt` | `N/D` | - |
| `CMTOPDstICMS` | `N/D` | - |
| `CMTOPUPis` | `N/D` | - |
| `CMTOPUCof` | `N/D` | - |
| `CMTOPFinNF` | `N/D` | - |
| `CMTOPMot20` | `N/D` | - |
| `CMTOPAImob` | `N/D` | - |
| `CMTOPArrST` | `N/D` | - |
| `CMTOPIcmPDest` | `N/D` | - |
| `CMTOPFilCod` | `N/D` | - |
| `CMTOPRegEstSim` | `N/D` | - |
| `CMTOPObs87` | `N/D` | - |
| `CMTOPIncNroCup` | `N/D` | - |
| `CMTOPIndFinal` | `N/D` | - |
| `CMTOPPis00` | `N/D` | - |
| `CMTOPPis10` | `N/D` | - |
| `CMTOPPis20` | `N/D` | - |
| `CMTOPPis30` | `N/D` | - |
| `CMTOPPis40` | `N/D` | - |
| `CMTOPPis41` | `N/D` | - |
| `CMTOPPis50` | `N/D` | - |
| `CMTOPPis51` | `N/D` | - |
| `CMTOPPis60` | `N/D` | - |
| `CMTOPPis61` | `N/D` | - |
| `CMTOPPis70` | `N/D` | - |
| `CMTOPPis90` | `N/D` | - |
| `CMTOPPAl00` | `N/D` | - |
| `CMTOPPAl10` | `N/D` | - |
| `CMTOPPAl20` | `N/D` | - |
| `CMTOPPAl30` | `N/D` | - |
| `CMTOPPAl40` | `N/D` | - |
| `CMTOPPAl41` | `N/D` | - |
| `CMTOPPAl50` | `N/D` | - |
| `CMTOPPAl51` | `N/D` | - |
| `CMTOPPAl60` | `N/D` | - |
| `CMTOPPAl61` | `N/D` | - |
| `CMTOPPAl70` | `N/D` | - |
| `CMTOPPAl90` | `N/D` | - |
| `CMTOPCof00` | `N/D` | - |
| `CMTOPCof10` | `N/D` | - |
| `CMTOPCof20` | `N/D` | - |
| `CMTOPCof30` | `N/D` | - |
| `CMTOPCof40` | `N/D` | - |
| `CMTOPCof41` | `N/D` | - |
| `CMTOPCof50` | `N/D` | - |
| `CMTOPCof51` | `N/D` | - |
| `CMTOPCof60` | `N/D` | - |
| `CMTOPCof61` | `N/D` | - |
| `CMTOPCof70` | `N/D` | - |
| `CMTOPCof90` | `N/D` | - |
| `CMTOPCAl00` | `N/D` | - |
| `CMTOPCAl10` | `N/D` | - |
| `CMTOPCAl20` | `N/D` | - |
| `CMTOPCAl30` | `N/D` | - |
| `CMTOPCAl40` | `N/D` | - |
| `CMTOPCAl41` | `N/D` | - |
| `CMTOPCAl50` | `N/D` | - |
| `CMTOPCAl51` | `N/D` | - |
| `CMTOPCAl60` | `N/D` | - |
| `CMTOPCAl61` | `N/D` | - |
| `CMTOPCAl70` | `N/D` | - |
| `CMTOPCAl90` | `N/D` | - |
| `CMTOPPeFCP` | `N/D` | - |
| `CMTOPMBc20` | `N/D` | - |
| `CMTOPIPICST` | `N/D` | - |
| `CMTOPIndPres` | `N/D` | - |
| `CMTOPAvOpI` | `N/D` | - |
| `CMTOPFS201` | `N/D` | - |
| `CMTOPFS202` | `N/D` | - |
| `CMTOPFC500` | `N/D` | - |
| `CMTOPFR500` | `N/D` | - |
| `CMTOPFS900` | `N/D` | - |
| `CMTOPFC00` | `N/D` | - |
| `CMTOPFC10` | `N/D` | - |
| `CMTOPFS10` | `N/D` | - |
| `CMTOPFC20` | `N/D` | - |
| `CMTOPFS30` | `N/D` | - |
| `CMTOPFC51` | `N/D` | - |
| `CMTOPFR60` | `N/D` | - |
| `CMTOPFC70` | `N/D` | - |
| `CMTOPFS70` | `N/D` | - |
| `CMTOPFC90` | `N/D` | - |
| `CMTOPFS90` | `N/D` | - |
| `CMTOPBProU` | `N/D` | - |
| `CMTOPTotTrib` | `N/D` | - |
| `CMTOPVlrTriApr` | `N/D` | - |
| `CMTOPSelNFCP` | `N/D` | - |
| `CMTOPObsEE` | `N/D` | - |
| `CMTOPPerAliMon` | `N/D` | - |
| `CMTopFrePisCof` | `N/D` | - |
| `CMTopEmpCod` | `N/D` | - |
| `CMTopArrIBS` | `N/D` | - |
| `CMTopArrCBS` | `N/D` | - |
| `CMTopCalcRT` | `N/D` | - |
| `CMTop00cBenef` | `N/D` | - |
| `CMTop10cBenef` | `N/D` | - |
| `CMTop20cBenef` | `N/D` | - |
| `CMTop30cBenef` | `N/D` | - |
| `CMTop40cBenef` | `N/D` | - |
| `CMTop41cBenef` | `N/D` | - |
| `CMTop50cBenef` | `N/D` | - |
| `CMTop51cBenef` | `N/D` | - |
| `CMTop60cBenef` | `N/D` | - |
| `CMTop61cBenef` | `N/D` | - |
| `CMTop70cBenef` | `N/D` | - |
| `CMTop90cBenef` | `N/D` | - |
| `CMTopRCod` | `N/D` | - |
| `CMTopRCodAux` | `N/D` | - |

#### 🗺️ Índices
- `CMTOPR1` (Unique): `CMTOPCod`, `CMTopRCod`
- `CMTOPR2` (Duplicate): `CMTOPCod`

---

### 📌 CMTra
- **Descrição:** Transportadora
- **Chave Primária:** `CMTraCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMTraCod` | `N/D` | - |
| `CMTraRazSoc` | `N/D` | - |
| `CMTraEnd` | `N/D` | - |
| `CMTraCid` | `N/D` | - |
| `CMTraUF` | `N/D` | - |
| `CMTraCGC` | `N/D` | - |
| `CMTraIEs` | `N/D` | - |
| `CMTraTel` | `N/D` | - |
| `CMTraCEP` | `N/D` | - |
| `CMTraCEPL` | `N/D` | - |
| `CMTraNro` | `N/D` | - |
| `CMTraIBGE` | `N/D` | - |
| `CMTraEmail` | `N/D` | - |
| `CMTraTip` | `N/D` | - |
| `CMTraMotNom` | `N/D` | - |
| `CMTraPlcVei` | `N/D` | - |
| `CMTraUFVei` | `N/D` | - |

#### 🗺️ Índices
- `CMTraA` (Unique): `CMTraCod`
- `CMTraB` (Duplicate): `CMTraCod`, `CMTraUF`

---

### 📌 CMTxt
- **Descrição:** Importa Texto Geral
- **Chave Primária:** `CMTxtGer`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMTxtGer` | `N/D` | - |
| `CMTxtAux1` | `N/D` | - |
| `CMTxtAux2` | `N/D` | - |

#### 🗺️ Índices
- `CMTxt1` (Unique): `CMTxtGer`

---

### 📌 CMUAt
- **Descrição:** Últimas Atualizações das Tabel
- **Chave Primária:** `CMUAtNomTab`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMUAtNomTab` | `N/D` | - |
| `CMUAtDta` | `N/D` | - |
| `CMUAtHor` | `N/D` | - |

#### 🗺️ Índices
- `CMUAt1` (Unique): `CMUAtNomTab`
- `CMUAt2` (Duplicate): `CMUAtDta`

---

### 📌 CMUBH
- **Descrição:** Banco de Horas do Usuário
- **Chave Primária:** `CMEmpCod`, `CMUsuNom`, `CMUBHAMe`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMUsuNom` | `N/D` | - |
| `CMUBHAMe` | `N/D` | - |
| `CMUBHSldAnt` | `N/D` | - |
| `CMUBHSldAtu` | `N/D` | - |
| `CMUBHQtdMes` | `N/D` | - |
| `CMUBHQtdPreMes` | `N/D` | - |
| `CMUBHUsu` | `N/D` | - |
| `CMUBHTST` | `N/D` | - |
| `CMUBHPrg` | `N/D` | - |
| `CMUBHSts` | `N/D` | - |
| `CMUBHDif` | `N/D` | - |

#### 🗺️ Índices
- `CMUBH1` (Unique): `CMEmpCod`, `CMUsuNom`, `CMUBHAMe`
- `CMUBH2` (Duplicate): `CMEmpCod`, `CMUsuNom`
- `CMUBH3` (Duplicate): `CMEmpCod`, `CMUsuNom`, `CMUBHAMe`

---

### 📌 CMUF
- **Descrição:** Estados
- **Chave Primária:** `CMUFCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMUFCod` | `N/D` | - |
| `CMUFDes` | `N/D` | - |
| `CMUFAlqIcm` | `N/D` | - |
| `CMUFCUsu` | `N/D` | - |
| `CMUFCHor` | `N/D` | - |
| `CMUFCDta` | `N/D` | - |
| `CMUFCPrg` | `N/D` | - |
| `CMUFDtaTrs` | `N/D` | - |
| `CMUFFlaDel` | `N/D` | - |
| `CMUFPer` | `N/D` | - |
| `CMUFMva` | `N/D` | - |
| `CMUFAlqST2` | `N/D` | - |
| `CMUFAlqST1` | `N/D` | - |
| `CMUFPerIVA` | `N/D` | - |

#### 🗺️ Índices
- `CMUFA` (Unique): `CMUFCod`

---

### 📌 CMUFF
- **Descrição:** Parâmetros da UF por Filial
- **Chave Primária:** `CMUFCod`, `CMUFFilCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMUFCod` | `N/D` | - |
| `CMUFFilCod` | `N/D` | - |
| `CMUFFInscE` | `N/D` | - |

#### 🗺️ Índices
- `CMUFFA` (Unique): `CMUFCod`, `CMUFFilCod`
- `CMUFFB` (Duplicate): `CMUFCod`

---

### 📌 CMUsA
- **Descrição:** Atendimento Realizado pelos Usuários
- **Chave Primária:** `CMEmpCod`, `CMUsuNom`, `CMUsHDta`, `CMUsAEnt`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMUsuNom` | `N/D` | - |
| `CMUsHDta` | `N/D` | - |
| `CMUsAEnt` | `N/D` | - |
| `CMUsHObs` | `N/D` | - |
| `CMUsuVlrHor` | `N/D` | - |
| `CMUsASai` | `N/D` | - |
| `CMUsACliCod` | `N/D` | - |
| `CMUsACliDes` | `N/D` | - |
| `CMUsAObs1` | `N/D` | - |
| `CMUsAObs2` | `N/D` | - |
| `CMUsAObs3` | `N/D` | - |
| `CMUsAObs4` | `N/D` | - |
| `CMUsAObs5` | `N/D` | - |
| `CMUsAQtd` | `N/D` | - |
| `CMUsATip` | `N/D` | - |
| `CMUsAVlrHor` | `N/D` | - |
| `CMUsAVltTot` | `N/D` | - |

#### 🗺️ Índices
- `CMUsA1` (Unique): `CMEmpCod`, `CMUsuNom`, `CMUsHDta`, `CMUsAEnt`
- `CMUsA2` (Duplicate): `CMEmpCod`, `CMUsuNom`, `CMUsHDta`
- `CMUsA3` (Duplicate): `CMEmpCod`, `CMUsACliCod`, `CMUsHDta`

---

### 📌 CMUsC
- **Descrição:** Configura Preço Consulta Por Usuário \ Convênio
- **Chave Primária:** `CMEmpCod`, `CMUsuNom`, `CMUsCCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMUsuNom` | `N/D` | - |
| `CMUsCCod` | `N/D` | - |
| `CMUsCDes` | `N/D` | - |
| `CMUsCVrCon` | `N/D` | - |

#### 🗺️ Índices
- `CMUsC1` (Unique): `CMEmpCod`, `CMUsuNom`, `CMUsCCod`
- `CMUsC2` (Duplicate): `CMEmpCod`, `CMUsuNom`

---

### 📌 CMUsF
- **Descrição:** Usuário - Filiais Que Possui Acesso
- **Chave Primária:** `CMUsuNom`, `CMUsuEmp`, `CMUsuFil`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMUsuNom` | `N/D` | - |
| `CMUsuEmp` | `N/D` | - |
| `CMUsuFil` | `N/D` | - |
| `CMUsuEntPrg` | `N/D` | - |

#### 🗺️ Índices
- `CMUsF1` (Unique): `CMUsuNom`, `CMUsuEmp`, `CMUsuFil`

---

### 📌 CMUsH
- **Descrição:** Horários dos Funcionários
- **Chave Primária:** `CMEmpCod`, `CMUsuNom`, `CMUsHDta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMUsuNom` | `N/D` | - |
| `CMUsHDta` | `N/D` | - |
| `CMUsuSen` | `N/D` | - |
| `CMUsHSai1` | `N/D` | - |
| `CMUsHS1OK` | `N/D` | - |
| `CMUsHEnt1` | `N/D` | - |
| `CMUsHE1OK` | `N/D` | - |
| `CMUsHAts1` | `N/D` | - |
| `CMUsHCid1` | `N/D` | - |
| `CMUsHFal1` | `N/D` | - |
| `CMUsHQtd1` | `N/D` | - |
| `CMUsHEnt2` | `N/D` | - |
| `CMUsHE2OK` | `N/D` | - |
| `CMUsHAts2` | `N/D` | - |
| `CMUsHCid2` | `N/D` | - |
| `CMUsHFal2` | `N/D` | - |
| `CMUsHSai2` | `N/D` | - |
| `CMUsHS2OK` | `N/D` | - |
| `CMUsHQtd2` | `N/D` | - |
| `CMUsHSai3` | `N/D` | - |
| `CMUsHS3OK` | `N/D` | - |
| `CMUsHEnt3` | `N/D` | - |
| `CMUsHE3OK` | `N/D` | - |
| `CMUsHAts3` | `N/D` | - |
| `CMUsHCid3` | `N/D` | - |
| `CMUsHFal3` | `N/D` | - |
| `CMUsHEnt4` | `N/D` | - |
| `CMUsHE4OK` | `N/D` | - |
| `CMUsHSai4` | `N/D` | - |
| `CMUsHS4OK` | `N/D` | - |
| `CMUsHAts4` | `N/D` | - |
| `CMUsHCid4` | `N/D` | - |
| `CMUsHFal4` | `N/D` | - |
| `CMUsHQtd4` | `N/D` | - |
| `CMUsHQtd3` | `N/D` | - |
| `CMUsHQtdDia` | `N/D` | - |
| `CMUsHQtdMes` | `N/D` | - |
| `CMUsHObs` | `N/D` | - |
| `CMUsHDesDia` | `N/D` | - |
| `CMUsHQtdPre` | `N/D` | - |

#### 🗺️ Índices
- `CMUsH1` (Unique): `CMEmpCod`, `CMUsuNom`, `CMUsHDta`
- `CMUsH2` (Duplicate): `CMEmpCod`, `CMUsuNom`
- `CMUsH3` (Duplicate): `CMUsHDta`

---

### 📌 CMUsM
- **Descrição:** Metas de Vendas por Vendedor
- **Chave Primária:** `CMEmpCod`, `CMUsuNom`, `CMUsMAMe`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMUsuNom` | `N/D` | - |
| `CMUsMAMe` | `N/D` | - |
| `CMUsMVlrCom` | `N/D` | - |
| `CMUsMDifPreTab` | `N/D` | - |
| `CMUsMDifRR` | `N/D` | - |
| `CMUsMDifTrc` | `N/D` | - |
| `CMUsMVVOut` | `N/D` | - |
| `CMUsMVVFin` | `N/D` | - |
| `CMUsMVVCar` | `N/D` | - |
| `CMUsMVVChq` | `N/D` | - |
| `CMUsMVVPrz` | `N/D` | - |
| `CMUsMVVVis` | `N/D` | - |
| `CMUsMQtdPec` | `N/D` | - |
| `CMUsMQtdVda` | `N/D` | - |
| `CMUsMIdx` | `N/D` | - |
| `CMUsMMg5` | `N/D` | - |
| `CMUsMMg4` | `N/D` | - |
| `CMUsMMg3` | `N/D` | - |
| `CMUsMMg2` | `N/D` | - |
| `CMUsMMg1` | `N/D` | - |
| `CMUsMMedDia` | `N/D` | - |
| `CMUsMPrjVda` | `N/D` | - |
| `CMUsMQDU` | `N/D` | - |
| `CMUsMQDF` | `N/D` | - |
| `CMUsMQDT` | `N/D` | - |
| `CMUsMVlrCus` | `N/D` | - |
| `CMUsMVlrVda` | `N/D` | - |
| `CMUsMVl5` | `N/D` | - |
| `CMUsMVl4` | `N/D` | - |
| `CMUsMVl3` | `N/D` | - |
| `CMUsMVl2` | `N/D` | - |
| `CMUsMVl1` | `N/D` | - |

#### 🗺️ Índices
- `CmUsM1` (Unique): `CMEmpCod`, `CMUsuNom`, `CMUsMAMe`
- `CmUsM2` (Duplicate): `CMEmpCod`, `CMUsuNom`
- `CMUsM3` (Duplicate): `CMEmpCod`, `CMUsMAMe`, `CMUsMIdx`

---

### 📌 CMUSP
- **Descrição:** Histórico de Acesso de Programas
- **Chave Primária:** `CMEmpCod`, `CMUsuNom`, `CMUSPPrg`, `CMUSPTST`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMUsuNom` | `N/D` | - |
| `CMUSPPrg` | `N/D` | - |
| `CMUSPTST` | `N/D` | - |
| `CMUSPEMP` | `N/D` | - |
| `CMUSPFIL` | `N/D` | - |
| `CMUSPDES` | `N/D` | - |
| `CMUSPDESBOT` | `N/D` | - |
| `CMUSPDESALE` | `N/D` | - |
| `CMUSPObs1` | `N/D` | - |
| `CMUSPObs2` | `N/D` | - |
| `CMUSPObs3` | `N/D` | - |
| `CMUSPObs4` | `N/D` | - |
| `CMUSPObs5` | `N/D` | - |
| `CMUSUSTS` | `N/D` | - |
| `CMUSPSegPrg` | `N/D` | - |
| `CMUSPAud` | `N/D` | - |

#### 🗺️ Índices
- `CMUSP1` (Unique): `CMEmpCod`, `CMUsuNom`, `CMUSPPrg`, `CMUSPTST`
- `CMUSP2` (Duplicate): `CMEmpCod`, `CMUsuNom`
- `CMUSP3` (Duplicate): `CMUSPTST`

---

### 📌 CmUsu
- **Descrição:** Usuarios
- **Chave Primária:** `CMEmpCod`, `CMUsuNom`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMUsuNom` | `N/D` | - |
| `CMUsuPerCom` | `N/D` | - |
| `CMUsuAut` | `N/D` | - |
| `CMUsuNComp` | `N/D` | - |
| `CMUsuNomCom` | `N/D` | - |
| `CMUsuCRM` | `N/D` | - |
| `CMUsuEspec` | `N/D` | - |
| `CMUsuCPF` | `N/D` | - |
| `CMUsuVrCon` | `N/D` | - |
| `CMUsuCodFo` | `N/D` | - |
| `CMUsuCodPro` | `N/D` | - |
| `CMUsuCodMerc` | `N/D` | - |
| `CMUsuDesMerc` | `N/D` | - |
| `CMUsuDesPro` | `N/D` | - |
| `CMUsuDesFo` | `N/D` | - |
| `CMUsuChcAut` | `N/D` | - |
| `CMUsuSen` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMUsuVen` | `N/D` | - |
| `CMUsuCUsu` | `N/D` | - |
| `CMUsuCHor` | `N/D` | - |
| `CMUsuCDta` | `N/D` | - |
| `CMUsuDtaTrs` | `N/D` | - |
| `CMUsuFlaDel` | `N/D` | - |
| `CMUsuCodVen` | `N/D` | - |
| `CMUsuSomCxa` | `N/D` | - |
| `CMUsuCheOut` | `N/D` | - |
| `CMUsuAuxCheOut` | `N/D` | - |
| `CMUsuVerOutFil` | `N/D` | - |
| `CMUsuAceCus` | `N/D` | - |
| `CMUsuTipCom` | `N/D` | - |
| `CMUsuFun` | `N/D` | - |
| `CMUsuPrxSeqVda` | `N/D` | - |
| `CMUsuCri` | `N/D` | - |
| `CMUsuSenCri` | `N/D` | - |
| `CMUsuFPSen` | `N/D` | - |
| `CMUsuNroMic` | `N/D` | - |
| `CMUsuCntHor` | `N/D` | - |
| `CMUsuManLimHor` | `N/D` | - |
| `CMUsuTarLimHor` | `N/D` | - |
| `CMusuNoiLimHor` | `N/D` | - |
| `CMusuH04LimHor` | `N/D` | - |
| `CMUsuManMHE` | `N/D` | - |
| `CMUsuTarMHE` | `N/D` | - |
| `CMUsuNoiMHE` | `N/D` | - |
| `CMUsuH04MHE` | `N/D` | - |
| `CMUsuCodCon` | `N/D` | - |
| `CMUsuVlrHor` | `N/D` | - |
| `CMUsuModNF` | `N/D` | - |
| `CMUsuInt` | `N/D` | - |
| `CMUsuEnd` | `N/D` | - |
| `CMUsuNroCas` | `N/D` | - |
| `CMUsuBai` | `N/D` | - |
| `CMUsuCid` | `N/D` | - |
| `CMUsuCEP` | `N/D` | - |
| `CMUsuTel1` | `N/D` | - |
| `CMUsuTel2` | `N/D` | - |
| `CMUsuDiaNsc` | `N/D` | - |
| `CMUsuMesNsc` | `N/D` | - |
| `CMUsuFunCod` | `N/D` | - |
| `CMUsuFunDes` | `N/D` | - |
| `CMUsuIdx` | `N/D` | - |
| `CMUsuEma` | `N/D` | - |
| `CMUsuPerDsc` | `N/D` | - |
| `CMUsuVlrRec` | `N/D` | - |

#### 🗺️ Índices
- `CMUsu1` (Unique): `CMEmpCod`, `CMUsuNom`
- `CMUsu2` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CMUsu3` (Duplicate): `CMEmpCod`, `CMUsuIdx`

---

### 📌 CMVD1
- **Descrição:** Cadastros de Vencimentos/Descontos VD
- **Chave Primária:** `CMVD1Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMVD1Cod` | `N/D` | - |
| `CMVD1Des` | `N/D` | - |

#### 🗺️ Índices
- `CMVD1A` (Unique): `CMVD1Cod`

---

### 📌 CMVen
- **Descrição:** Vencimentos
- **Chave Primária:** `CMEmpCod`, `CMVenSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMVenSeq` | `N/D` | - |
| `CMVenDta` | `N/D` | - |
| `CMVenObs` | `N/D` | - |
| `CMVenVlr` | `N/D` | - |
| `CMVenSal` | `N/D` | - |
| `CMVenTip` | `N/D` | - |
| `CMVenNroChq` | `N/D` | - |
| `CMVenNroBco` | `N/D` | - |
| `CMVenBcoDes` | `N/D` | - |
| `CMVenNroNf` | `N/D` | - |
| `CMVenNomFor` | `N/D` | - |
| `CMVenCodFor` | `N/D` | - |
| `CMVenDtaLctCp` | `N/D` | - |
| `CMVenSeqLctCp` | `N/D` | - |
| `CMVenNroParCp` | `N/D` | - |
| `CMVenTelCli` | `N/D` | - |
| `CMVenDtaTrs` | `N/D` | - |
| `CMVenFlaDel` | `N/D` | - |
| `CMVenCCrCod` | `N/D` | - |
| `CMVenCCrDes` | `N/D` | - |
| `CMVenCCSeqLct` | `N/D` | - |
| `CMVenFil` | `N/D` | - |

#### 🗺️ Índices
- `CMVen1` (Unique): `CMEmpCod`, `CMVenSeq`
- `CMVen2` (Duplicate): `CMEmpCod`

---

### 📌 CMWht
- **Descrição:** Controle Mensagens WhatsApp
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CMWhtSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMWhtSeq` | `N/D` | - |
| `CMWhtDtaInc` | `N/D` | - |
| `CMWhtCodPac` | `N/D` | - |
| `CMWhtDesPac` | `N/D` | - |
| `CMWhtMsg` | `N/D` | - |
| `CMWhtCmp` | `N/D` | - |
| `CMWhtTel01` | `N/D` | - |
| `CMWhtTel02` | `N/D` | - |
| `CMWhtTel03` | `N/D` | - |
| `CMWhtDtaVda` | `N/D` | - |
| `CMWhtSeqVda` | `N/D` | - |
| `CMWhtSts` | `N/D` | - |
| `CMWhtExtBol` | `N/D` | - |
| `CMWhtDirBol` | `N/D` | - |
| `CMWhtID` | `N/D` | - |
| `CMWhtTip` | `N/D` | - |

#### 🗺️ Índices
- `CMWhtA` (Unique): `CMEmpCod`, `CMFilCod`, `CMWhtSeq`
- `CMWhtB` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CMWhtC` (Duplicate): `CMWhtSeq`
- `CMWhtD` (Duplicate): `CMWhtID`
- `CMWhtE` (Duplicate): `CMEmpCod`, `CMFilCod`, `CMWhtCodPac`, `CMWhtDtaVda`, `CMWhtSeqVda`

---

### 📌 CMXML
- **Descrição:** Controla Arquivos XML
- **Chave Primária:** `CMXmlNom`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMXmlNom` | `N/D` | - |
| `CMXMLTip` | `N/D` | - |
| `CMXMLAno` | `N/D` | - |
| `CMXMLMes` | `N/D` | - |
| `CMXMLCan` | `N/D` | - |
| `CMXmlObs` | `N/D` | - |
| `CMXMLVlr` | `N/D` | - |
| `CMXMLDtaEmi` | `N/D` | - |
| `CMXMLNro` | `N/D` | - |
| `CMXMLEmp` | `N/D` | - |
| `CMXMLFil` | `N/D` | - |
| `CMXMLDocCli` | `N/D` | - |
| `CMXMLCNPJEmi` | `N/D` | - |
| `CMXmlCon` | `N/D` | - |
| `CMXmlCnf` | `N/D` | - |
| `CMXmlMovDta` | `N/D` | - |
| `CMXMLMovSeq` | `N/D` | - |
| `CMXMLMovVlr` | `N/D` | - |
| `CMXmlOrg` | `N/D` | - |
| `CMXmlArqVlr` | `N/D` | - |
| `CMXmlArqDifVlr` | `N/D` | - |
| `CMXmlVdaDifVlr` | `N/D` | - |

#### 🗺️ Índices
- `CMXMLA` (Unique): `CMXmlNom`
- `CMXMLB` (Duplicate): `CMXMLAno`, `CMXMLMes`, `CMXMLNro`
- `CMXmlC` (Duplicate): `CMXMLAno`, `CMXMLMes`, `CMXmlNom`
- `CMXmlD` (Duplicate): `CMXmlMovDta`, `CMXMLMovSeq`

---

### 📌 CMXMLI
- **Descrição:** Controle Arquivos Por Imposto
- **Chave Primária:** `CMXmlNom`, `CMXmlImp`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMXmlNom` | `N/D` | - |
| `CMXMLTip` | `N/D` | - |
| `CMXMLAno` | `N/D` | - |
| `CMXMLMes` | `N/D` | - |
| `CMXMLCan` | `N/D` | - |
| `CMXmlObs` | `N/D` | - |
| `CMXMLVlr` | `N/D` | - |
| `CMXMLDtaEmi` | `N/D` | - |
| `CMXMLNro` | `N/D` | - |
| `CMXMLEmp` | `N/D` | - |
| `CMXMLFil` | `N/D` | - |
| `CMXMLDocCli` | `N/D` | - |
| `CMXMLCNPJEmi` | `N/D` | - |
| `CMXmlCon` | `N/D` | - |
| `CMXmlCnf` | `N/D` | - |
| `CMXmlMovDta` | `N/D` | - |
| `CMXMLMovSeq` | `N/D` | - |
| `CMXMLMovVlr` | `N/D` | - |
| `CMXmlOrg` | `N/D` | - |
| `CMXmlArqVlr` | `N/D` | - |
| `CMXmlArqDifVlr` | `N/D` | - |
| `CMXmlVdaDifVlr` | `N/D` | - |
| `CMXmlImp` | `N/D` | - |
| `CMXmlIVlrImp` | `N/D` | - |

#### 🗺️ Índices
- `CMXMLIA` (Unique): `CMXmlNom`, `CMXmlImp`
- `CMXMLIB` (Duplicate): `CMXmlNom`

---

### 📌 COLUNAS
- **Descrição:** Colunas
- **Chave Primária:** `object_id`, `Colunanome`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `object_id` | `N/D` | - |
| `Colunanome` | `N/D` | - |

#### 🗺️ Índices
- `IColunas` (Unique): `object_id`, `Colunanome`
- `IColunas1` (Duplicate): `object_id`

---

### 📌 CPCCr
- **Descrição:** Cadastro Cartões de Crédito
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPCCrCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPCCrCod` | `N/D` | - |
| `CPCCrDes` | `N/D` | - |
| `CPCCrCHor` | `N/D` | - |
| `CPCCrCUsu` | `N/D` | - |
| `CPCCrCPrg` | `N/D` | - |
| `CPCCrCDta` | `N/D` | - |
| `CPCCrBcoDebAut` | `N/D` | - |
| `CPCCrTip` | `N/D` | - |

#### 🗺️ Índices
- `CPCCr1` (Unique): `CMEmpCod`, `CMFilCod`, `CPCCrCod`
- `CPCCr2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CPCLI
- **Descrição:** Cadastro Fornecedor
- **Chave Primária:** `CMEmpCod`, `CPCliCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CPCliFan` | `N/D` | - |
| `CPCliCDta` | `N/D` | - |
| `CPCliCHor` | `N/D` | - |
| `CPCliCUsu` | `N/D` | - |
| `CPCliEnd` | `N/D` | - |
| `CPTipProRvd` | `N/D` | - |
| `CPCliCEn` | `N/D` | - |
| `CPCliEMa` | `N/D` | - |
| `CPCliNroCas` | `N/D` | - |
| `CPCliObs` | `N/D` | - |
| `CPCliBai` | `N/D` | - |
| `CPCliCid` | `N/D` | - |
| `CPCliUf` | `N/D` | - |
| `CPCliCep` | `N/D` | - |
| `CPCliTel1` | `N/D` | - |
| `CPCliFax` | `N/D` | - |
| `CPCliTel3` | `N/D` | - |
| `CPCliTel4` | `N/D` | - |
| `CPCliCgc` | `N/D` | - |
| `CPCliIE` | `N/D` | - |
| `CPTipCod` | `N/D` | - |
| `CPTipDes` | `N/D` | - |
| `CPCliAge` | `N/D` | - |
| `CPCliDtaTrs` | `N/D` | - |
| `CPCliFlaDel` | `N/D` | - |
| `CPCliCon1` | `N/D` | - |
| `CPCliCon2` | `N/D` | - |
| `CPCliEtqNom` | `N/D` | - |
| `CPCliImpEtq` | `N/D` | - |
| `CPCliSen` | `N/D` | - |
| `CPCliWeb` | `N/D` | - |
| `DSDspCod` | `N/D` | - |
| `DSDspDes` | `N/D` | - |
| `CPCliDesRes` | `N/D` | - |
| `CPCliFil` | `N/D` | - |
| `CPCLiCodAux` | `N/D` | - |
| `CPCliFun` | `N/D` | - |
| `CPCliRelCodCli` | `N/D` | - |
| `CPCliVlrCreAbe` | `N/D` | - |
| `CPCliModNf` | `N/D` | - |
| `CPCliSts` | `N/D` | - |
| `CPCliCPF` | `N/D` | - |
| `CPCliRazSoc` | `N/D` | - |
| `CPCliIdx` | `N/D` | - |
| `CPCliDesCli` | `N/D` | - |
| `CPCliPer01` | `N/D` | - |
| `CPCliPer02` | `N/D` | - |
| `CPCliPer03` | `N/D` | - |

#### 🗺️ Índices
- `CPCLI1` (Unique): `CMEmpCod`, `CPCliCod`
- `CPCLI4` (Duplicate): `CMEmpCod`, `CPTipCod`
- `CPCLI3` (Duplicate): `CMEmpCod`, `DSDspCod`
- `CPCLI5` (Duplicate): `CMEmpCod`, `CPCliDes`
- `CPCli6` (Duplicate): `CPCliIdx`

---

### 📌 CPCR1
- **Descrição:** Controle Requisições - Ótica
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPCliCod`, `CPCR1Dta`, `CPCR1Org`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `CPCR1Dta` | `N/D` | - |
| `CPCR1Org` | `N/D` | - |
| `CPCR1TotReq` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CPCR1VlrFor` | `N/D` | - |
| `CPCR1VlrCal` | `N/D` | - |
| `CPCR1VlrDif` | `N/D` | - |
| `CPCR1QtdPro` | `N/D` | - |
| `CPCR1IDX` | `N/D` | - |

#### 🗺️ Índices
- `CPCR1A` (Unique): `CMEmpCod`, `CMFilCod`, `CPCliCod`, `CPCR1Dta`, `CPCR1Org`
- `CPCR1B` (Duplicate): `CMEmpCod`, `CPCliCod`
- `CPCR1C` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CPCR1D` (Duplicate): `CPCliCod`, `CPCR1Dta`
- `CPCR1E` (Duplicate): `CPCR1Dta`
- `CPCR1F` (Duplicate): `CPCR1IDX`

---

### 📌 CPCR2
- **Descrição:** Controle Requisições - Ótica
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPCliCod`, `CPCR1Dta`, `CPCR1Org`, `CPCR2NroReq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `CPCR1Dta` | `N/D` | - |
| `CPCR1Org` | `N/D` | - |
| `CPCR1TotReq` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CPCR1VlrFor` | `N/D` | - |
| `CPCR1VlrCal` | `N/D` | - |
| `CPCR1VlrDif` | `N/D` | - |
| `CPCR1QtdPro` | `N/D` | - |
| `CPCR1IDX` | `N/D` | - |
| `CPCR2NroReq` | `N/D` | - |
| `CPCR2VlrFor` | `N/D` | - |
| `CPCR2VlrCal` | `N/D` | - |
| `CPCR2VlrDif` | `N/D` | - |
| `CPCR2UsuReq` | `N/D` | - |
| `CPCR2UsuCP` | `N/D` | - |
| `CPCR2TstReq` | `N/D` | - |
| `CPCR2TstCP` | `N/D` | - |
| `CPCR2UsuSup` | `N/D` | - |
| `CPCR2Sts` | `N/D` | - |
| `CPCR2NroNF` | `N/D` | - |
| `CPCR2DtaNF` | `N/D` | - |
| `CPCR2SerNf` | `N/D` | - |
| `CPCR2MovDta` | `N/D` | - |
| `CPCR2MovSeq` | `N/D` | - |
| `CPCR2MovFil` | `N/D` | - |

#### 🗺️ Índices
- `CPCR2A` (Unique): `CMEmpCod`, `CMFilCod`, `CPCliCod`, `CPCR1Dta`, `CPCR1Org`, `CPCR2NroReq`
- `CPCR2B` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPCliCod`, `CPCR1Dta`, `CPCR1Org`
- `CPCR2C` (Duplicate): `CPCR2NroReq`
- `CPCR2D` (Duplicate): `CPCR1Dta`

---

### 📌 CPCR3
- **Descrição:** Controle Requisições - Ótica
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPCliCod`, `CPCR1Dta`, `CPCR1Org`, `CPCR2NroReq`, `CPCR3Ite`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `CPCR1Dta` | `N/D` | - |
| `CPCR1Org` | `N/D` | - |
| `CPCR1TotReq` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CPCR1VlrFor` | `N/D` | - |
| `CPCR1VlrCal` | `N/D` | - |
| `CPCR1VlrDif` | `N/D` | - |
| `CPCR1QtdPro` | `N/D` | - |
| `CPCR2NroReq` | `N/D` | - |
| `CPCR2VlrFor` | `N/D` | - |
| `CPCR2VlrCal` | `N/D` | - |
| `CPCR2VlrDif` | `N/D` | - |
| `CPCR2UsuReq` | `N/D` | - |
| `CPCR2UsuCP` | `N/D` | - |
| `CPCR2TstReq` | `N/D` | - |
| `CPCR2TstCP` | `N/D` | - |
| `CPCR2UsuSup` | `N/D` | - |
| `CPCR3Ite` | `N/D` | - |
| `CPCR3CodPro` | `N/D` | - |
| `CPCR3QtdFor` | `N/D` | - |
| `CPCR3VlrCus` | `N/D` | - |
| `CPCR3VlrVda` | `N/D` | - |
| `CPCR3TotCus` | `N/D` | - |
| `CPCR3TotVda` | `N/D` | - |
| `CPCR3QtdOrg` | `N/D` | - |
| `CPCR3VlrFor` | `N/D` | - |
| `CPCR3VlrCal` | `N/D` | - |
| `CPCR3ProDes` | `N/D` | - |

#### 🗺️ Índices
- `CPCR3A` (Unique): `CMEmpCod`, `CMFilCod`, `CPCliCod`, `CPCR1Dta`, `CPCR1Org`, `CPCR2NroReq`, `CPCR3Ite`
- `CPCR3B` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPCliCod`, `CPCR1Dta`, `CPCR1Org`, `CPCR2NroReq`
- `CPCR3C` (Duplicate): `CPCR2NroReq`
- `CPCR3D` (Duplicate): `CPCR1Dta`

---

### 📌 CPCXP
- **Descrição:** Fornecedor x CFOP
- **Chave Primária:** `CMEmpCod`, `CPCliCod`, `CPCliCFOPO`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `CPCliCFOPO` | `N/D` | - |
| `CPCliCFOPD` | `N/D` | - |

#### 🗺️ Índices
- `CPCXP1` (Unique): `CMEmpCod`, `CPCliCod`, `CPCliCFOPO`
- `CPCXP2` (Duplicate): `CMEmpCod`, `CPCliCod`

---

### 📌 CPDevC
- **Descrição:** Cabeçalho Devolução de Produtos da Nota -
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPDevCTST`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPMovDta` | `N/D` | - |
| `CPMovSeq` | `N/D` | - |
| `CPMov2VlrTot` | `N/D` | - |
| `CPMov2CodCliFor` | `N/D` | - |
| `CPMov2DesCliFor` | `N/D` | - |
| `CPMov2Flag` | `N/D` | - |
| `CPMov2TotCus` | `N/D` | - |
| `CPMov2CMPrgnom` | `N/D` | - |
| `CPMov2TotQtd` | `N/D` | - |
| `CPMov2DevVlrTot` | `N/D` | - |
| `CPMov2DevQtd` | `N/D` | - |
| `CPDevCTST` | `N/D` | - |
| `CPDevCDevQtd` | `N/D` | - |
| `CPDevCDevVlrTot` | `N/D` | - |
| `CPDevCObs1` | `N/D` | - |
| `CPDevCObs2` | `N/D` | - |
| `CPDevCUSU` | `N/D` | - |
| `CPDevCSts` | `N/D` | - |
| `CPDevCCanTST` | `N/D` | - |
| `CPDevCCanUsu` | `N/D` | - |
| `CPDevCVlrCre` | `N/D` | - |

#### 🗺️ Índices
- `CPDevC1` (Unique): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPDevCTST`
- `CPDevC2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`
- `CPDevC3` (Duplicate): `CPDevCTST`

---

### 📌 CPDevP
- **Descrição:** Devolução de Produtos da Nota - Produtos
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPDevCTST`, `CPMov4Ite`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPMovDta` | `N/D` | - |
| `CPMovSeq` | `N/D` | - |
| `CPMov2VlrTot` | `N/D` | - |
| `CPMov2CodCliFor` | `N/D` | - |
| `CPMov2DesCliFor` | `N/D` | - |
| `CPMov2Flag` | `N/D` | - |
| `CPMov2TotCus` | `N/D` | - |
| `CPMov2CMPrgnom` | `N/D` | - |
| `CPMov2TotQtd` | `N/D` | - |
| `CPMov2DevVlrTot` | `N/D` | - |
| `CPMov2DevQtd` | `N/D` | - |
| `CPDevCTST` | `N/D` | - |
| `CPDevCDevQtd` | `N/D` | - |
| `CPDevCDevVlrTot` | `N/D` | - |
| `CPDevCObs1` | `N/D` | - |
| `CPDevCObs2` | `N/D` | - |
| `CPDevCUSU` | `N/D` | - |
| `CPDevCSts` | `N/D` | - |
| `CPDevCCanTST` | `N/D` | - |
| `CPDevCCanUsu` | `N/D` | - |
| `CPDevCVlrCre` | `N/D` | - |
| `CPMov4Ite` | `N/D` | - |
| `CPMov4CodCha` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CPMov4ProDes` | `N/D` | - |
| `CPMov4ProQtd` | `N/D` | - |
| `CPMov4CusPro` | `N/D` | - |
| `CPDevPQtd` | `N/D` | - |
| `CPDevPVlrTot` | `N/D` | - |
| `CPDevPVlrUnt` | `N/D` | - |
| `CPDevPQtdTot` | `N/D` | - |

#### 🗺️ Índices
- `CPDevP1` (Unique): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPDevCTST`, `CPMov4Ite`
- `CPDevP2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMov4Ite`
- `CPDevP3` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPDevCTST`

---

### 📌 CPGF1
- **Descrição:** Grupos de Fornecedores
- **Chave Primária:** `CMEmpCod`, `CPGF1Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CPGF1Cod` | `N/D` | - |
| `CPGF1Des` | `N/D` | - |
| `CPGF1STS` | `N/D` | - |

#### 🗺️ Índices
- `CPGF1A` (Unique): `CMEmpCod`, `CPGF1Cod`
- `CPGF1B` (Duplicate): `CMEmpCod`

---

### 📌 CPGF2
- **Descrição:** Grupo de Fornecedores
- **Chave Primária:** `CMEmpCod`, `CPGF1Cod`, `CPGF2Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CPGF1Cod` | `N/D` | - |
| `CPGF1Des` | `N/D` | - |
| `CPGF1STS` | `N/D` | - |
| `CPGF2Cod` | `N/D` | - |
| `CPGF2Des` | `N/D` | - |
| `CPGF2STS` | `N/D` | - |

#### 🗺️ Índices
- `CPGF2A` (Unique): `CMEmpCod`, `CPGF1Cod`, `CPGF2Cod`
- `CPGF2B` (Duplicate): `CMEmpCod`, `CPGF1Cod`

---

### 📌 CPMov1
- **Descrição:** Sequencia das Compras
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPMovDta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPMovDta` | `N/D` | - |
| `CPMov1AuxSeq` | `N/D` | - |
| `CPMov1PrxChq` | `N/D` | - |

#### 🗺️ Índices
- `CPMov11` (Unique): `CMEmpCod`, `CMFilCod`, `CPMovDta`
- `CPMov12` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CPMov2
- **Descrição:** Cabecalho das compras
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPMovDta` | `N/D` | - |
| `CPMovSeq` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CMFilAltGrpSgrDsp` | `N/D` | - |
| `CMFilBcoCof` | `N/D` | - |
| `CMFilAceFilEntSai` | `N/D` | - |
| `CPMov2GrpDsp` | `N/D` | - |
| `CPMov2Grp_Des` | `N/D` | - |
| `CPMov2SgrDsp` | `N/D` | - |
| `CPMov2Sgr_Des` | `N/D` | - |
| `CPMov2TotQtd` | `N/D` | - |
| `CPMov2VlDup` | `N/D` | - |
| `CPMov2TotCus` | `N/D` | - |
| `CPMov2Fil` | `N/D` | - |
| `CPMov2VlrTot` | `N/D` | - |
| `CPMov2VlrIpi` | `N/D` | - |
| `CPMov2VlIcm` | `N/D` | - |
| `CPMov2BCIcm` | `N/D` | - |
| `CPMov2CDta` | `N/D` | - |
| `CPMov2CHor` | `N/D` | - |
| `CPMov2CUsu` | `N/D` | - |
| `CPMov2CPrg` | `N/D` | - |
| `CPMov2NroNFi` | `N/D` | - |
| `CPMov2FIPI` | `N/D` | - |
| `CPMov2SerNFi` | `N/D` | - |
| `CPMov2DtaNFi` | `N/D` | - |
| `CPMov2DtaSPD` | `N/D` | - |
| `CPMov2Obs` | `N/D` | - |
| `CPMov2Obs3` | `N/D` | - |
| `CPMov2Obs2` | `N/D` | - |
| `CPMov2CodCliFor` | `N/D` | - |
| `DSDspCod` | `N/D` | - |
| `CPCliSts` | `N/D` | - |
| `CPMov2DesCliFor` | `N/D` | - |
| `CPMov2NOpCod` | `N/D` | - |
| `CPMov2NOpDes` | `N/D` | - |
| `CPMov2Flag` | `N/D` | - |
| `CPMov2NroPar` | `N/D` | - |
| `CPMov2BcoCod` | `N/D` | - |
| `CPMov2EfeLct` | `N/D` | - |
| `CPMov2PerAcrFin` | `N/D` | - |
| `CPMov2PerDesFin` | `N/D` | - |
| `CPMov2VlrAbe` | `N/D` | - |
| `CPMov2CCuCod` | `N/D` | - |
| `CMEmpUsa_CCu` | `N/D` | - |
| `CPMov2DspCod` | `N/D` | - |
| `CPMov2DspDes` | `N/D` | - |
| `CPMov2TotDscPar` | `N/D` | - |
| `CPMov2TotAcrPar` | `N/D` | - |
| `CPMov2TotVlrPag` | `N/D` | - |
| `CPMov2MedDiaPgt` | `N/D` | - |
| `CPMov2_PerDesPad` | `N/D` | - |
| `CPMov2CCrCod` | `N/D` | - |
| `CPCCrBcoDebAut` | `N/D` | - |
| `CPMov1AuxSeq` | `N/D` | - |
| `CPMov2Per2DesSobTodIte` | `N/D` | - |
| `CPMov2Per3AcrSobTodIte` | `N/D` | - |
| `CPMov2AtuPrcVda` | `N/D` | - |
| `CPMov2UsaCusFinPreVda` | `N/D` | - |
| `CPMov2DtaPed` | `N/D` | - |
| `CPMov2SeqPed` | `N/D` | - |
| `CPMov2VlrFre` | `N/D` | - |
| `CPMov2VlDes` | `N/D` | - |
| `CPMov2FilDsp` | `N/D` | - |
| `CPMov2FilNomFan` | `N/D` | - |
| `CPMov2VlrDifVlr` | `N/D` | - |
| `CPMov2VlrV1` | `N/D` | - |
| `CPMov2ModNF` | `N/D` | - |
| `CPMov2VlIse` | `N/D` | - |
| `CPMov2VlrOut` | `N/D` | - |
| `CPMov2AliIcm` | `N/D` | - |
| `CPMov2Sit` | `N/D` | - |
| `CpMov2IcmRet` | `N/D` | - |
| `CPMov2VlDsp` | `N/D` | - |
| `CPMov2IcmSub` | `N/D` | - |
| `CPMov2CodAnt` | `N/D` | - |
| `CPMov2FilFat` | `N/D` | - |
| `CPMov2ProVda` | `N/D` | - |
| `CPMov2Vlr_IsePisCof` | `N/D` | - |
| `CPMov2VlrPro` | `N/D` | - |
| `CPMov2TrtDsc` | `N/D` | - |
| `CPMov2TrtAcr` | `N/D` | - |
| `CPMov2TrtFrt` | `N/D` | - |
| `CPMov2TrtSeg` | `N/D` | - |
| `CPMov2VlrSeg` | `N/D` | - |
| `CPMov2FVlrFin` | `N/D` | - |
| `CPMov2CliDes` | `N/D` | - |
| `CPMov2CliCod` | `N/D` | - |
| `CPMov2ImpXML` | `N/D` | - |
| `CPMov2NFe` | `N/D` | - |
| `CPMov2VctPriPar` | `N/D` | - |
| `CPMov2VlPriPar` | `N/D` | - |
| `CPMov2Idx` | `N/D` | - |
| `CPCliModNf` | `N/D` | - |
| `CPMov2_FilEntCod` | `N/D` | - |
| `CPMov2FilEntDes` | `N/D` | - |
| `CPMov2TerDep` | `N/D` | - |
| `CPMov2Per_AcrCusFin` | `N/D` | - |
| `CPMov2Vl_AcrCusFin` | `N/D` | - |
| `CPMov2Aprv` | `N/D` | - |
| `CPMov2IcmD` | `N/D` | - |
| `CPMov2DtSped` | `N/D` | - |
| `CPMov2LctAutDsp` | `N/D` | - |
| `CPMov2vSTFCP` | `N/D` | - |
| `CPMov2TotFinCus` | `N/D` | - |
| `CPMov2VTPis` | `N/D` | - |
| `CPMov2VTCof` | `N/D` | - |
| `CPMov2TpPed` | `N/D` | - |
| `CPMov2TCL` | `N/D` | - |
| `CPMov2FVST` | `N/D` | - |
| `CPMov2FVICM` | `N/D` | - |
| `CPMov2FSeg` | `N/D` | - |
| `CPMov2FFrt` | `N/D` | - |
| `CPMov2FDsp` | `N/D` | - |
| `CPMov2FDsc` | `N/D` | - |
| `CPMov2FBST` | `N/D` | - |
| `CPMov2FBICM` | `N/D` | - |
| `CPMov2EfeDev` | `N/D` | - |
| `CPMov2DevVlrTot` | `N/D` | - |
| `CPMov2DevQtd` | `N/D` | - |
| `CPMov2PrxIte` | `N/D` | - |
| `CPMov2PreMed` | `N/D` | - |
| `CPMov2Ped` | `N/D` | - |
| `CPMov2Cus_CusDes` | `N/D` | - |
| `CPMov2DtaTrs` | `N/D` | - |
| `CPMov2TST` | `N/D` | - |
| `CPMov2AudVlr` | `N/D` | - |
| `CPCCrTip` | `N/D` | - |
| `CPMov2CMPrgnom` | `N/D` | - |
| `CPMov2TotReq` | `N/D` | - |
| `CMFilLojEsc` | `N/D` | - |
| `CMEmpCEVct` | `N/D` | - |
| `CMFilSNGPC` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CMFilAceNroSerPro` | `N/D` | - |
| `CMEmpCPLctPro` | `N/D` | - |
| `CMFilUsaTabPre` | `N/D` | - |
| `CMFilEstFra` | `N/D` | - |
| `CMFilCECorNro` | `N/D` | - |
| `CMFilPrcAcrVdaPrz` | `N/D` | - |
| `CMEmpCPPreVda` | `N/D` | - |
| `CMEmpCEUsaGrpSgr` | `N/D` | - |
| `CMEmpDec` | `N/D` | - |
| `CMFilArrTru` | `N/D` | - |
| `CMFilPerIcmSimPau` | `N/D` | - |
| `CPMov2FFCPST` | `N/D` | - |
| `CPMov2CodPed` | `N/D` | - |

#### 🗺️ Índices
- `CPMov21` (Unique): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`
- `CPMov23` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMovDta`
- `CPMov2D` (Duplicate): `CMEmpCod`, `CPMov2CodCliFor`
- `CPMov27` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMov2BcoCod`
- `CPMov26` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMov2CCuCod`
- `CPMov28` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMov2CCrCod`
- `CPMov24` (Duplicate): `CMEmpCod`, `CPMov2EfeLct`
- `CPMov25` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMov2DtaNFi`, `CPMov2NroNFi`
- `CPMov2A` (Duplicate): `CPMov2TST`
- `CPMov2B` (Duplicate): `CPMov2Ped`
- `CPMov2C` (Duplicate): `CMEmpCod`, `CPMov2CodCliFor`, `CPMovDta`
- `CPMov2E` (Duplicate): `CPMov2Idx`
- `CPMov2F` (Duplicate): `CPMov2NFe`

---

### 📌 CPMov3
- **Descrição:** Parcelas da Compra
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMov3Par`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPMovDta` | `N/D` | - |
| `CPMovSeq` | `N/D` | - |
| `CPMov2NroPar` | `N/D` | - |
| `CMFilBcoCof` | `N/D` | - |
| `CPMov2_PerDesPad` | `N/D` | - |
| `CPMov2Vlr_IsePisCof` | `N/D` | - |
| `CPMov2VlrOut` | `N/D` | - |
| `CPMov2VlrDifVlr` | `N/D` | - |
| `CPMov2VlrAbe` | `N/D` | - |
| `CPMov2VlIse` | `N/D` | - |
| `CPMov2VlDup` | `N/D` | - |
| `CPMov2UsaCusFinPreVda` | `N/D` | - |
| `CPMov2TotVlrPag` | `N/D` | - |
| `CPMov2TotQtd` | `N/D` | - |
| `CPMov2TotFinCus` | `N/D` | - |
| `CPMov2TotDscPar` | `N/D` | - |
| `CPMov2TotCus` | `N/D` | - |
| `CMFilAltGrpSgrDsp` | `N/D` | - |
| `CPMov2VlrPro` | `N/D` | - |
| `CPMov2FVlrFin` | `N/D` | - |
| `CPMov2TrtSeg` | `N/D` | - |
| `CPMov2TrtFrt` | `N/D` | - |
| `CPMov2TrtDsc` | `N/D` | - |
| `CPMov2TrtAcr` | `N/D` | - |
| `CPMov2TotAcrPar` | `N/D` | - |
| `CPMov2VTPis` | `N/D` | - |
| `CPMov2VTCof` | `N/D` | - |
| `CPMov2VlrSeg` | `N/D` | - |
| `CPMov2VctPriPar` | `N/D` | - |
| `CPMov2TpPed` | `N/D` | - |
| `CPMov2TCL` | `N/D` | - |
| `CPMov2NFe` | `N/D` | - |
| `CPMov2ImpXML` | `N/D` | - |
| `CPMov2Idx` | `N/D` | - |
| `CPMov2FVST` | `N/D` | - |
| `CPMov2FVICM` | `N/D` | - |
| `CPMov2FSeg` | `N/D` | - |
| `CPMov2FFrt` | `N/D` | - |
| `CPMov2FDsp` | `N/D` | - |
| `CPMov2FDsc` | `N/D` | - |
| `CPMov2FBST` | `N/D` | - |
| `CPMov2FBICM` | `N/D` | - |
| `CPMov2EfeDev` | `N/D` | - |
| `CPMov2DevVlrTot` | `N/D` | - |
| `CPMov2DevQtd` | `N/D` | - |
| `CPMov2Sit` | `N/D` | - |
| `CPMov2Sgr_Des` | `N/D` | - |
| `CPMov2SgrDsp` | `N/D` | - |
| `CPMov2SeqPed` | `N/D` | - |
| `CPMov2PrxIte` | `N/D` | - |
| `CPMov2ProVda` | `N/D` | - |
| `CPMov2PreMed` | `N/D` | - |
| `CPMov2PerDesFin` | `N/D` | - |
| `CPMov2PerAcrFin` | `N/D` | - |
| `CPMov2Per3AcrSobTodIte` | `N/D` | - |
| `CPMov2Per2DesSobTodIte` | `N/D` | - |
| `CPMov2Ped` | `N/D` | - |
| `CPMov2ModNF` | `N/D` | - |
| `CPMov2MedDiaPgt` | `N/D` | - |
| `CPMov2IcmSub` | `N/D` | - |
| `CpMov2IcmRet` | `N/D` | - |
| `CPMov2Grp_Des` | `N/D` | - |
| `CPMov2GrpDsp` | `N/D` | - |
| `CPMov2FilNomFan` | `N/D` | - |
| `CPMov2FilFat` | `N/D` | - |
| `CPMov2FilDsp` | `N/D` | - |
| `CPMov2EfeLct` | `N/D` | - |
| `CPMov2DtaPed` | `N/D` | - |
| `CPMov2DspDes` | `N/D` | - |
| `CPMov2DspCod` | `N/D` | - |
| `CPMov2VlDsp` | `N/D` | - |
| `CPMov2Cus_CusDes` | `N/D` | - |
| `CPMov2CodAnt` | `N/D` | - |
| `CPMov2BCIcm` | `N/D` | - |
| `CPMov2AtuPrcVda` | `N/D` | - |
| `CPMov2AliIcm` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CPMov2Flag` | `N/D` | - |
| `CPMov2Fil` | `N/D` | - |
| `CPMov2VlrTot` | `N/D` | - |
| `CPMov2VlrIpi` | `N/D` | - |
| `CPMov2FIPI` | `N/D` | - |
| `CPMov2VlrFre` | `N/D` | - |
| `CPMov2VlDes` | `N/D` | - |
| `CPMov2VlIcm` | `N/D` | - |
| `CPMov2CDta` | `N/D` | - |
| `CPMov2CHor` | `N/D` | - |
| `CPMov2CUsu` | `N/D` | - |
| `CPMov2CPrg` | `N/D` | - |
| `CPMov2NroNFi` | `N/D` | - |
| `CPMov2SerNFi` | `N/D` | - |
| `CPMov2DtaNFi` | `N/D` | - |
| `CPMov2Obs` | `N/D` | - |
| `CPMov2Obs2` | `N/D` | - |
| `CPMov2Obs3` | `N/D` | - |
| `CPMov2CodCliFor` | `N/D` | - |
| `CPMov2DesCliFor` | `N/D` | - |
| `CPMov2DtaTrs` | `N/D` | - |
| `CPMov2TST` | `N/D` | - |
| `CPCliModNf` | `N/D` | - |
| `CPMov2NOpCod` | `N/D` | - |
| `CPMov2NOpDes` | `N/D` | - |
| `CPMov2BcoCod` | `N/D` | - |
| `CPMov2CCuCod` | `N/D` | - |
| `CMEmpUsa_CCu` | `N/D` | - |
| `CPMov2CCrCod` | `N/D` | - |
| `CPCCrBcoDebAut` | `N/D` | - |
| `CPMov2VlrV1` | `N/D` | - |
| `CPMov2CliCod` | `N/D` | - |
| `CPMov2CliDes` | `N/D` | - |
| `CPMov2Aprv` | `N/D` | - |
| `CPMov2IcmD` | `N/D` | - |
| `CPMov2AudVlr` | `N/D` | - |
| `CPMov2DtSped` | `N/D` | - |
| `CPMov2vSTFCP` | `N/D` | - |
| `CPMov3Par` | `N/D` | - |
| `CPMov3CodCliFor` | `N/D` | - |
| `CPMov3CCSeqLct` | `N/D` | - |
| `CPMov3VlrOrg` | `N/D` | - |
| `CPMov3VlrAcr` | `N/D` | - |
| `CPMov3VlrDes` | `N/D` | - |
| `CPMov3DtaVct` | `N/D` | - |
| `CPMov3DtaPgt` | `N/D` | - |
| `CPMov3Obs` | `N/D` | - |
| `CPMov3Flag` | `N/D` | - |
| `CPMov3CDta` | `N/D` | - |
| `CPMov3CUsu` | `N/D` | - |
| `CPMov3CHor` | `N/D` | - |
| `CPMov3DtaTrs` | `N/D` | - |
| `CPMov3Chq` | `N/D` | - |
| `CPMov3BcoCod` | `N/D` | - |
| `CPMov3CCuCod` | `N/D` | - |
| `CPMov3CCuDes` | `N/D` | - |
| `CPMov3DspCod` | `N/D` | - |
| `CPMov3DspDes` | `N/D` | - |
| `CPMov3CPrg` | `N/D` | - |
| `CPMov3FlgCCrCod` | `N/D` | - |
| `CPMov3SaiDinCxa` | `N/D` | - |
| `CPMov3VlrV1` | `N/D` | - |
| `CPMov3CCrCod` | `N/D` | - |
| `CPMov3CheOut` | `N/D` | - |
| `CPMov3DOV` | `N/D` | - |
| `CPMov3NroBol` | `N/D` | - |
| `CPMov3AudVlr` | `N/D` | - |
| `CPMov3AudJus` | `N/D` | - |
| `CPMov3AudTst` | `N/D` | - |
| `CPMov3AudUsu` | `N/D` | - |
| `CMFilFilBcoCof` | `N/D` | - |
| `CPMov2LctAutDsp` | `N/D` | - |
| `CPMov3Sit` | `N/D` | - |
| `CPMov3DtaLctDsp` | `N/D` | - |
| `CPMov3SeqLctDsp` | `N/D` | - |
| `CPMov3FilNomFan` | `N/D` | - |
| `CPMov3FilDsp` | `N/D` | - |
| `CPMov3VlrChqTer` | `N/D` | - |
| `CPMov3VlrBxaPar` | `N/D` | - |
| `CPMov3Idx` | `N/D` | - |
| `CPCCrTip` | `N/D` | - |
| `CPMov3Vlr_Abe` | `N/D` | - |
| `CPMov3FlaDel` | `N/D` | - |
| `CPMov3VlrPag` | `N/D` | - |
| `CPMov3DCx` | `N/D` | - |
| `CPMov3Rec` | `N/D` | - |
| `CPMov3CCx` | `N/D` | - |
| `CPMov3DtPrePgt` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CPMov3DPr` | `N/D` | - |

#### 🗺️ Índices
- `CPMov31` (Unique): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMov3Par`
- `CPMov32` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`
- `CPMov39` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMov3CCrCod`
- `CPMov33` (Duplicate): `CMEmpCod`, `CPMov3DtaVct`
- `CPMov34` (Duplicate): `CMEmpCod`, `CPMov3DtaPgt`
- `CPMov35` (Duplicate): `CMEmpCod`, `CPMov3Flag`, `CPMov3CodCliFor`, `CPMov3DtaVct`
- `CPMov36` (Duplicate): `CMEmpCod`, `CPMov3Flag`, `CPMov3DtaVct`
- `CPMov37` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMov3BcoCod`, `CPMov3Chq`
- `CPMov38` (Duplicate): `CMEmpCod`, `CPMov3FlgCCrCod`
- `CPMov3A` (Duplicate): `CPMov3DCx`
- `CPMov3B` (Duplicate): `CPMov3CCx`
- `CPMov3C` (Duplicate): `CPMov3DtPrePgt`
- `CPMov3D` (Duplicate): `CPMov3Idx`
- `CPMov3E` (Duplicate): `CPMov3AudTst`

---

### 📌 CPMov4
- **Descrição:** Produtos da Compra
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMov4Ite`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPMovDta` | `N/D` | - |
| `CPMovSeq` | `N/D` | - |
| `CPMov2VlrTot` | `N/D` | - |
| `CPMov2CodCliFor` | `N/D` | - |
| `CPMov2DesCliFor` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CPMov2Flag` | `N/D` | - |
| `CPMov2TotCus` | `N/D` | - |
| `CPMov2CMPrgnom` | `N/D` | - |
| `CPMov2TotQtd` | `N/D` | - |
| `CPMov2DevVlrTot` | `N/D` | - |
| `CPMov2DevQtd` | `N/D` | - |
| `CPMov2CUsu` | `N/D` | - |
| `CPMov2CCrCod` | `N/D` | - |
| `CPMov2BcoCod` | `N/D` | - |
| `CPMov2CCuCod` | `N/D` | - |
| `CPMov2PrxIte` | `N/D` | - |
| `CPMov4Ite` | `N/D` | - |
| `CPMov4CodCha` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CPMov4ProDes` | `N/D` | - |
| `CPMov4ProQtd` | `N/D` | - |
| `CPMov4CusPro` | `N/D` | - |
| `CPMov4EstApoEnt` | `N/D` | - |
| `CPMov4NovPreVda` | `N/D` | - |
| `CPMov4NroSerPro` | `N/D` | - |
| `CPMov4CusFin` | `N/D` | - |
| `CPMov4TotCus` | `N/D` | - |
| `CPMov4MrgTel` | `N/D` | - |
| `CMFilLojEsc` | `N/D` | - |
| `CMEmpCEVct` | `N/D` | - |
| `CMFilSNGPC` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CMFilAceNroSerPro` | `N/D` | - |
| `CMEmpCPLctPro` | `N/D` | - |
| `CPMov2VlrFre` | `N/D` | - |
| `CPMov2VlDes` | `N/D` | - |
| `CMFilUsaTabPre` | `N/D` | - |
| `CPMov2NOpCod` | `N/D` | - |
| `CPMov2PreMed` | `N/D` | - |
| `CPMov2TotFinCus` | `N/D` | - |
| `CPMov2_PerDesPad` | `N/D` | - |
| `CPMov2Cus_CusDes` | `N/D` | - |
| `CPMov2Per2DesSobTodIte` | `N/D` | - |
| `CPMov2Per3AcrSobTodIte` | `N/D` | - |
| `CPMov2UsaCusFinPreVda` | `N/D` | - |
| `CPMov2ImpXML` | `N/D` | - |
| `CPMov2NroNFi` | `N/D` | - |
| `CMFilAceFilEntSai` | `N/D` | - |
| `CMFilEstFra` | `N/D` | - |
| `CMFilCECorNro` | `N/D` | - |
| `CPMov2VlrDifVlr` | `N/D` | - |
| `CMFilPrcAcrVdaPrz` | `N/D` | - |
| `CPMov2VlrIpi` | `N/D` | - |
| `CPMov2FIPI` | `N/D` | - |
| `CMEmpCPPreVda` | `N/D` | - |
| `CMEmpCEUsaGrpSgr` | `N/D` | - |
| `CPMov4PerDes` | `N/D` | - |
| `CPMov4TotFinCus` | `N/D` | - |
| `CPMov4ProPre1Tab` | `N/D` | - |
| `CPMov4Pro1QtdPar` | `N/D` | - |
| `CPMov4Pro2VlrPar` | `N/D` | - |
| `CPMov4DtaTrs` | `N/D` | - |
| `CPMov4FlaDel` | `N/D` | - |
| `CPMov4QtdEtq` | `N/D` | - |
| `CPMov4EfeLct` | `N/D` | - |
| `CPMov4CusHorEnt` | `N/D` | - |
| `CPMov4Ref` | `N/D` | - |
| `CPMov4PreGel` | `N/D` | - |
| `CPMov4Lot` | `N/D` | - |
| `CPMov4VlrIpi` | `N/D` | - |
| `CPMov4VlrUntIpi` | `N/D` | - |
| `CPMov4Vct` | `N/D` | - |
| `CPMov4VlICM` | `N/D` | - |
| `CPMov4VlrDsc` | `N/D` | - |
| `CPMov4CST` | `N/D` | - |
| `CPMov4CFOP` | `N/D` | - |
| `CPMov4BasIcm` | `N/D` | - |
| `CPMov4BasSubIcm` | `N/D` | - |
| `CPMov4AliIcms` | `N/D` | - |
| `CPMov4Mrg` | `N/D` | - |
| `CPMov4NCM` | `N/D` | - |
| `CPMov4NCMDes` | `N/D` | - |
| `CPMov4Vlr_ICMSub` | `N/D` | - |
| `CPMov4CusLiq` | `N/D` | - |
| `CPMov4VlrFre` | `N/D` | - |
| `CPMov4AlqIPI` | `N/D` | - |
| `CPMov4VlDsp` | `N/D` | - |
| `CPMov4VlrSeg` | `N/D` | - |
| `CPMov4DevQtd` | `N/D` | - |
| `CPMov4CusAntLiq` | `N/D` | - |
| `CPMov4TnqCod` | `N/D` | - |
| `CPMov4FabLot` | `N/D` | - |
| `CPMov4CodFor` | `N/D` | - |
| `CMEmpDec` | `N/D` | - |
| `CMFilArrTru` | `N/D` | - |
| `CPMov2SerNFi` | `N/D` | - |
| `CMFilPerIcmSimPau` | `N/D` | - |
| `CPMov2DtaNFi` | `N/D` | - |
| `CPMov2TrtDsc` | `N/D` | - |
| `CPMov2AliIcm` | `N/D` | - |
| `CpMov2IcmRet` | `N/D` | - |
| `CPMov2IcmSub` | `N/D` | - |
| `CPMov2VlIcm` | `N/D` | - |
| `CPMov2VlrOut` | `N/D` | - |
| `CPMov2BCIcm` | `N/D` | - |
| `CPMov2VlDsp` | `N/D` | - |
| `CPMov2FFrt` | `N/D` | - |
| `CPMov2FDsp` | `N/D` | - |
| `CPMov2FDsc` | `N/D` | - |
| `CPMov2FBST` | `N/D` | - |
| `CPMov2FVST` | `N/D` | - |
| `CPMov2FBICM` | `N/D` | - |
| `CPMov2FVICM` | `N/D` | - |
| `CPMov2FSeg` | `N/D` | - |
| `CPMov2VlrSeg` | `N/D` | - |
| `CPMov2VlrPro` | `N/D` | - |
| `CPMov2TCL` | `N/D` | - |
| `CPMov2VTPis` | `N/D` | - |
| `CPMov2VTCof` | `N/D` | - |
| `CPMov2Per_AcrCusFin` | `N/D` | - |
| `CPMov2Vl_AcrCusFin` | `N/D` | - |
| `CPMov2FFCPST` | `N/D` | - |
| `CPMov2vSTFCP` | `N/D` | - |
| `CPMov4Bas_IPI` | `N/D` | - |
| `CPMov4_QtdNFE` | `N/D` | - |
| `CPMov4_VUnNFE` | `N/D` | - |
| `CPMov4_VToNFE` | `N/D` | - |
| `CPMov4DifVlrTot` | `N/D` | - |
| `CPMov4AlqST` | `N/D` | - |
| `CPMov4Und` | `N/D` | - |
| `CPMov4Ind` | `N/D` | - |
| `CPMov4VUnDsc` | `N/D` | - |
| `CPMov4TCL` | `N/D` | - |
| `CPMov4DesNFE` | `N/D` | - |
| `CPMov4BCPis` | `N/D` | - |
| `CPMov4BCCof` | `N/D` | - |
| `CPMov4AlqPis` | `N/D` | - |
| `CPMov4AliCof` | `N/D` | - |
| `CPMov4ModICM` | `N/D` | - |
| `CPMov4ModST` | `N/D` | - |
| `CPMov4CSTIpi` | `N/D` | - |
| `CPMov4VUPis` | `N/D` | - |
| `CPMov4CstPis` | `N/D` | - |
| `CPMov4CstCof` | `N/D` | - |
| `CPMov4VUCof` | `N/D` | - |
| `CPMov4VTPis` | `N/D` | - |
| `CPMov4VTCof` | `N/D` | - |
| `CPMov4IDEPCN` | `N/D` | - |
| `CPMov4PQA` | `N/D` | - |
| `CPMov4CnvQtd` | `N/D` | - |
| `CPMov4CnvFat` | `N/D` | - |
| `CPMov4PerRedICM` | `N/D` | - |
| `CPMov4UndNFe` | `N/D` | - |
| `CPMov4CnvUnd` | `N/D` | - |
| `CPMov4CusDifICM` | `N/D` | - |
| `CPMov4P_DifICM` | `N/D` | - |
| `CPMov4CSOSN` | `N/D` | - |
| `CPMov4PCrSN` | `N/D` | - |
| `CPMov4VCrSN` | `N/D` | - |
| `CPMov4PrcFre` | `N/D` | - |
| `CPMov4MrgAtu` | `N/D` | - |
| `CPMov4DifICMUnit` | `N/D` | - |
| `CPMov4Per_AcrCusFin` | `N/D` | - |
| `CPMov4Vl_AcrCusFin` | `N/D` | - |
| `CPMov4CusEst` | `N/D` | - |
| `CPMov4_Pro1Cus` | `N/D` | - |
| `CPMov4ProCusFin` | `N/D` | - |
| `CPMov4IcmD` | `N/D` | - |
| `CPMov4vSTFCP` | `N/D` | - |
| `CPMov2VlrV1` | `N/D` | - |
| `CPMov2VlrAbe` | `N/D` | - |
| `CPMov2Vlr_IsePisCof` | `N/D` | - |
| `CPMov2TotVlrPag` | `N/D` | - |
| `CPMov2TotDscPar` | `N/D` | - |
| `CPMov2TotAcrPar` | `N/D` | - |
| `CPMov2VlIse` | `N/D` | - |
| `CPMov2VlDup` | `N/D` | - |
| `CPMov2FVlrFin` | `N/D` | - |
| `CPMov2Fil` | `N/D` | - |
| `CPMov4bFCP` | `N/D` | - |
| `CPMov4pFCP` | `N/D` | - |
| `CPMov4vFCP` | `N/D` | - |
| `CPMov4bSTFCP` | `N/D` | - |
| `CPMov4pSTFCP` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CPMov4bRetFCP` | `N/D` | - |
| `CPMov4pRetFCP` | `N/D` | - |
| `CPMov4vRetFCP` | `N/D` | - |
| `CPMov4QLotes` | `N/D` | - |
| `CPMov2CDta` | `N/D` | - |
| `CPMov2CHor` | `N/D` | - |
| `CPMov2CPrg` | `N/D` | - |
| `CPMov2Obs` | `N/D` | - |
| `CPMov2Obs3` | `N/D` | - |
| `CPMov2Obs2` | `N/D` | - |
| `CPMov2EfeLct` | `N/D` | - |
| `CPMov2Ped` | `N/D` | - |
| `CPMov2TpPed` | `N/D` | - |
| `CPMov2EfeDev` | `N/D` | - |
| `CPMov2VctPriPar` | `N/D` | - |
| `CPMov2NroPar` | `N/D` | - |
| `CPMov2CodPed` | `N/D` | - |
| `CPMov4QtdPed` | `N/D` | - |
| `CPMov4QtdCan` | `N/D` | - |
| `CPMov4EstKIT` | `N/D` | - |
| `CPMov4ObsCan` | `N/D` | - |
| `CPMov2ProVda` | `N/D` | - |
| `CPMov4T_CPMovG` | `N/D` | - |

#### 🗺️ Índices
- `CPMov4A` (Unique): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMov4Ite`
- `CPMov4B` (Duplicate): `CMEmpCod`, `CEProCod`
- `CPMov4C` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`
- `CPMov4D` (Duplicate): `CPMov4NroSerPro`
- `CPMov4E` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CEProCod`
- `CPMov4F` (Duplicate): `CPMovDta`, `CPMov4ProDes`
- `CPMov4G` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMov4AliIcms`
- `CPMov4H` (Duplicate): `CEProCod`, `CPMovDta`
- `CPMov4I` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMov4CFOP`, `CPMov4Ite`

---

### 📌 CPMovG
- **Descrição:** Lançamento Contas a Pagar por Grade
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMov4Ite`, `CPMovGNro`, `CPMovGCor`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPMovDta` | `N/D` | - |
| `CPMovSeq` | `N/D` | - |
| `CPMov4Ite` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CPMov4T_CPMovG` | `N/D` | - |
| `CPMovGNro` | `N/D` | - |
| `CPMovGCor` | `N/D` | - |
| `CPMovGCodBar` | `N/D` | - |
| `CPMovGQtdAtu` | `N/D` | - |
| `CPMovGCorDes` | `N/D` | - |
| `CPMovGSts` | `N/D` | - |
| `CPMovGProCod` | `N/D` | - |
| `CPMovGDesPCN` | `N/D` | - |
| `CPMovGIDE` | `N/D` | - |

#### 🗺️ Índices
- `CPMovG1` (Unique): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMov4Ite`, `CPMovGNro`, `CPMovGCor`
- `CPMovG2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMov4Ite`

---

### 📌 CPMovI
- **Descrição:** Impostos da Nota
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMovIOrg`, `CPMovICod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPMovDta` | `N/D` | - |
| `CPMovSeq` | `N/D` | - |
| `CPMov2VlrTot` | `N/D` | - |
| `CPMov2CodCliFor` | `N/D` | - |
| `CPMov2DesCliFor` | `N/D` | - |
| `CPMov2VlrV1` | `N/D` | - |
| `CPMovIOrg` | `N/D` | - |
| `CPMovICod` | `N/D` | - |
| `CPMovIVlr` | `N/D` | - |
| `CPMovIAux1` | `N/D` | - |
| `CPMovIAux2` | `N/D` | - |
| `CPMovIAux3` | `N/D` | - |
| `CPMovICST` | `N/D` | - |
| `CPMovIPI1` | `N/D` | - |
| `CPMovIPI2` | `N/D` | - |
| `CPMovIPI3` | `N/D` | - |
| `CPMovIPI4` | `N/D` | - |
| `CPMovIPI5` | `N/D` | - |
| `CPMovIBI1` | `N/D` | - |
| `CPMovIBI2` | `N/D` | - |
| `CPMovIBI3` | `N/D` | - |
| `CPMovIBI4` | `N/D` | - |
| `CPMovIBI5` | `N/D` | - |
| `CPMovIVI1` | `N/D` | - |
| `CPMovIVI2` | `N/D` | - |
| `CPMovIVI3` | `N/D` | - |
| `CPMovIVI4` | `N/D` | - |
| `CPMovIVI5` | `N/D` | - |
| `CPMovIPer` | `N/D` | - |

#### 🗺️ Índices
- `CPMovI1` (Unique): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMovIOrg`, `CPMovICod`
- `CPMovI2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`

---

### 📌 CPMovL
- **Descrição:** Cadastro Produtos Compra - Lotes
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMov4Ite`, `CPMovLNum`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPMovDta` | `N/D` | - |
| `CPMovSeq` | `N/D` | - |
| `CPMov4Ite` | `N/D` | - |
| `CPMov4QLotes` | `N/D` | - |
| `CPMovLNum` | `N/D` | - |
| `CPMovLFab` | `N/D` | - |
| `CPMovLVal` | `N/D` | - |
| `CPMovLQtd` | `N/D` | - |
| `CPMovLCdx` | `N/D` | - |

#### 🗺️ Índices
- `CPMovL1` (Unique): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMov4Ite`, `CPMovLNum`
- `CPMovL2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMov4Ite`

---

### 📌 CPMovR
- **Descrição:** Requisições da Nota
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMovRReq`, `CPMovRPro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPMovDta` | `N/D` | - |
| `CPMovSeq` | `N/D` | - |
| `CPMov2CodCliFor` | `N/D` | - |
| `CPMov2DesCliFor` | `N/D` | - |
| `CPMov2TotReq` | `N/D` | - |
| `CPMov2TotQtd` | `N/D` | - |
| `CPMov2FVlrFin` | `N/D` | - |
| `CPMovRReq` | `N/D` | - |
| `CPMovRPro` | `N/D` | - |
| `CPMovRDtaVda` | `N/D` | - |
| `CPMovRFilVda` | `N/D` | - |
| `CPMovRSeqVda` | `N/D` | - |
| `CPMovRTST` | `N/D` | - |
| `CPMovRPrg` | `N/D` | - |
| `CPMovRUsu` | `N/D` | - |
| `CPMovRQtd` | `N/D` | - |
| `CPMovRObs` | `N/D` | - |

#### 🗺️ Índices
- `CPMovR1` (Unique): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`, `CPMovRReq`, `CPMovRPro`
- `CPMovR2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPMovDta`, `CPMovSeq`
- `CPMovR3` (Duplicate): `CPMovRReq`

---

### 📌 CPTip
- **Descrição:** Tipo de Fornecedor
- **Chave Primária:** `CMEmpCod`, `CPTipCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CPTipCod` | `N/D` | - |
| `CPTipDes` | `N/D` | - |
| `CPTipDtaTrs` | `N/D` | - |
| `CPTipCHor` | `N/D` | - |
| `CPTipCUsu` | `N/D` | - |
| `CPTipCDta` | `N/D` | - |
| `CPTipFlaDel` | `N/D` | - |
| `CPTipProRvd` | `N/D` | - |
| `CPTipCPrg` | `N/D` | - |

#### 🗺️ Índices
- `CPTip1` (Unique): `CMEmpCod`, `CPTipCod`
- `CPTip2` (Duplicate): `CMEmpCod`
- `CPTip3` (Duplicate): `CMEmpCod`, `CPTipDes`

---

### 📌 CPTmp1
- **Descrição:** Temporária
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPTmp1Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPTmp1Cod` | `N/D` | - |
| `CPTmp1Dta` | `N/D` | - |
| `CPTmp1Org` | `N/D` | - |
| `CPTmp1NroNFi` | `N/D` | - |
| `CPTmp1SerNFi` | `N/D` | - |
| `CPTmp1Vlr` | `N/D` | - |
| `CPTmp1DesCliFor` | `N/D` | - |
| `CPTmp1Obs` | `N/D` | - |
| `CPTmp1x` | `N/D` | - |

#### 🗺️ Índices
- `CPTmp5` (Unique): `CMEmpCod`, `CMFilCod`, `CPTmp1Cod`
- `CPTmp2` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CPTmp3` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPTmp1Dta`, `CPTmp1Org`

---

### 📌 CPTPF
- **Descrição:** Tabela de Preço do Fornecedor
- **Chave Primária:** `CMEmpCod`, `CPCliCod`, `CMFilCod`, `CPTPFProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CPCliPer01` | `N/D` | - |
| `CPCliPer02` | `N/D` | - |
| `CPCliPer03` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPTPFProCod` | `N/D` | - |
| `CPTPFProDes` | `N/D` | - |
| `CPTPFVlr` | `N/D` | - |
| `CPTPFCUsu` | `N/D` | - |
| `CPTPFCDta` | `N/D` | - |
| `CPTPFCHor` | `N/D` | - |
| `CPTPFCPrg` | `N/D` | - |
| `CPTPFDtaTrs` | `N/D` | - |
| `CPTPFFlaDel` | `N/D` | - |
| `CPTPFVlr01` | `N/D` | - |
| `CPTPFVlr02` | `N/D` | - |
| `CPTPFVlr03` | `N/D` | - |

#### 🗺️ Índices
- `CPTPF1` (Unique): `CMEmpCod`, `CPCliCod`, `CMFilCod`, `CPTPFProCod`
- `CPTPF3` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CPTPF4` (Duplicate): `CMEmpCod`, `CPCliCod`
- `CPTPF2` (Duplicate): `CMEmpCod`, `CPTPFProCod`

---

### 📌 CRCCr
- **Descrição:** Cartao de Crédito
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRCCrCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRCCrCod` | `N/D` | - |
| `CRCCrDes` | `N/D` | - |
| `CRCCrCHor` | `N/D` | - |
| `CRCCrCUsu` | `N/D` | - |
| `CRCCrCPrg` | `N/D` | - |
| `CRCCrCDta` | `N/D` | - |
| `CRCCr_PerDesVdaPrz` | `N/D` | - |
| `CRCCrPerDesVdaVis` | `N/D` | - |
| `CRCCrTip` | `N/D` | - |
| `CRCCrQtdDiaPriVct` | `N/D` | - |
| `CRCCrPerPar` | `N/D` | - |
| `CRCCrBcoFil` | `N/D` | - |
| `CRCCrBcoCod` | `N/D` | - |
| `CRCCrBcoDes` | `N/D` | - |
| `CRCCrDspCod` | `N/D` | - |
| `CRCCrDspDes` | `N/D` | - |
| `CRCCrDesRes` | `N/D` | - |
| `CRCCrMaxPar` | `N/D` | - |
| `CRCCrSts` | `N/D` | - |
| `CRCCrLctParFec` | `N/D` | - |
| `CRCCrNroVlrCon` | `N/D` | - |
| `CRCCrQtdIniPar` | `N/D` | - |
| `CRCCrQtdFinPar` | `N/D` | - |

#### 🗺️ Índices
- `CRCCr1` (Unique): `CMEmpCod`, `CMFilCod`, `CRCCrCod`
- `CRCCr2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CRCCV
- **Descrição:** Controle Contra Vale
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRCCVCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRCCVCod` | `N/D` | - |
| `CRCCVCOL` | `N/D` | - |
| `CRCCVUSU` | `N/D` | - |
| `CRCCVTST` | `N/D` | - |
| `CRCCVPRG` | `N/D` | - |
| `CRCCVVlr` | `N/D` | - |
| `CRCCVObs` | `N/D` | - |
| `CRCCVDCx` | `N/D` | - |
| `CRCCVDtaLct` | `N/D` | - |
| `CRCCVDtaBxa` | `N/D` | - |
| `CRCCVDIdx` | `N/D` | - |
| `CRCCVCOB` | `N/D` | - |
| `CRCCVORG` | `N/D` | - |
| `CRCCVProCod` | `N/D` | - |
| `CRCCVProDes` | `N/D` | - |
| `CRCCVPro1Qtd` | `N/D` | - |
| `CRCCVForPgt` | `N/D` | - |
| `CRCCVCliCod` | `N/D` | - |
| `CRCCVCliDes` | `N/D` | - |
| `CRCCVPro2Qtd` | `N/D` | - |
| `CRCCVPro3Qtd` | `N/D` | - |
| `CRCCVPro4Qtd` | `N/D` | - |
| `CRCCVUsuBxa` | `N/D` | - |
| `CRCCVCon1Vas` | `N/D` | - |
| `CRCCVCon2Vas` | `N/D` | - |
| `CRCCVCon3Vas` | `N/D` | - |
| `CRCCVCon4Vas` | `N/D` | - |
| `CRCCVNroAux` | `N/D` | - |
| `CRCCVSalVas` | `N/D` | - |
| `CRCCVBxa1Qtd` | `N/D` | - |
| `CRCCVBxa2Qtd` | `N/D` | - |
| `CRCCVBxa3Qtd` | `N/D` | - |
| `CRCCVBxa4Qtd` | `N/D` | - |
| `CRCCVSal1Qtd` | `N/D` | - |
| `CRCCVSal2Qtd` | `N/D` | - |
| `CRCCVSal3Qtd` | `N/D` | - |
| `CRCCVSal4Qtd` | `N/D` | - |
| `xxx` | `N/D` | - |

#### 🗺️ Índices
- `CRCCV1` (Unique): `CMEmpCod`, `CMFilCod`, `CRCCVCod`
- `CRCCV2` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CRCCV3` (Duplicate): `CRCCVDtaLct`
- `CRCCV4` (Duplicate): `CRCCVDtaBxa`
- `CRCCV5` (Duplicate): `CRCCVDIdx`
- `CRCCV6` (Duplicate): `CRCCVCliCod`

---

### 📌 CRCen
- **Descrição:** Endereços do Cliente
- **Chave Primária:** `CMEmpCod`, `CRCliCod`, `CRCEnTip`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRCEnTip` | `N/D` | - |
| `CRCenObs` | `N/D` | - |
| `CRCEnEnd` | `N/D` | - |
| `CRCenNro` | `N/D` | - |
| `CRCEnBai` | `N/D` | - |
| `CRCEnCid` | `N/D` | - |
| `CRCEnCEP` | `N/D` | - |
| `CRCenCom` | `N/D` | - |
| `CRCEnUF` | `N/D` | - |
| `CRCEnTst` | `N/D` | - |
| `CRCEnUsu` | `N/D` | - |
| `CRCEnPrg` | `N/D` | - |

#### 🗺️ Índices
- `CRCen1` (Unique): `CMEmpCod`, `CRCliCod`, `CRCEnTip`
- `CRCen2` (Duplicate): `CMEmpCod`, `CRCliCod`

---

### 📌 CRChA
- **Descrição:** Cheques Avulsos
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRChACod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRChACod` | `N/D` | - |
| `CRChAVlr` | `N/D` | - |
| `CRChaCnfVlr` | `N/D` | - |
| `CRChADtaVct` | `N/D` | - |
| `CRChaCnfDtaVct` | `N/D` | - |
| `CRChaDiaPrz` | `N/D` | - |
| `CRChADtaBai` | `N/D` | - |
| `CRChANom` | `N/D` | - |
| `CRChACodBco` | `N/D` | - |
| `CRChANroChq` | `N/D` | - |
| `CRChADesChq` | `N/D` | - |
| `CRChACodCta` | `N/D` | - |
| `CRChAObs` | `N/D` | - |
| `CRChADtaLct` | `N/D` | - |
| `CRChACheOut` | `N/D` | - |
| `CRChASts` | `N/D` | - |
| `CRChACodCli` | `N/D` | - |
| `CRChADesCli` | `N/D` | - |
| `CRChAAge` | `N/D` | - |
| `CRChACpfCli` | `N/D` | - |
| `CRChADCx` | `N/D` | - |
| `CRChAVlrTrc` | `N/D` | - |
| `CRChAOrg` | `N/D` | - |
| `CRChABcoCof` | `N/D` | - |
| `CMFilBcoCof` | `N/D` | - |
| `CRChACpfNro` | `N/D` | - |
| `CRChAFilPgt` | `N/D` | - |
| `CRChACPFil` | `N/D` | - |
| `CRChaCPDta` | `N/D` | - |
| `CRChaCPSeq` | `N/D` | - |
| `CRChaCPPar` | `N/D` | - |
| `CRChaCPCli` | `N/D` | - |
| `CRChACCx` | `N/D` | - |
| `CRChaCRMov6Seq` | `N/D` | - |
| `CRChaCTst` | `N/D` | - |
| `CRChaCUsu` | `N/D` | - |
| `CRChAFilMovOrg` | `N/D` | - |
| `CRChADtaMovOrg` | `N/D` | - |
| `CRChASeqMovOrg` | `N/D` | - |
| `CRChAParOrg` | `N/D` | - |
| `CRChAQtdPar` | `N/D` | - |
| `CMEmpJrsMes` | `N/D` | - |
| `CRChAVlrDsc` | `N/D` | - |
| `CRChAVlrAcr` | `N/D` | - |
| `CRChAQtdDiaDsc` | `N/D` | - |
| `CRChATxaDsc` | `N/D` | - |
| `CRChAVlrApoDsc` | `N/D` | - |
| `CRChaX` | `N/D` | - |
| `CRChaIdx` | `N/D` | - |
| `CRChaCPrg` | `N/D` | - |

#### 🗺️ Índices
- `CRChA1` (Unique): `CMEmpCod`, `CMFilCod`, `CRChACod`
- `CRChA2` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CRChA3` (Duplicate): `CRChANroChq`, `CRChACodBco`
- `CRChA4` (Duplicate): `CRChADtaVct`
- `CRChA5` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRChACod`
- `CRChA6` (Duplicate): `CRChADtaLct`
- `CRChA7` (Duplicate): `CMEmpCod`, `CRChACodCli`, `CRChADtaVct`
- `CRChA8` (Duplicate): `CRChADtaBai`
- `CRChA9` (Duplicate): `CRChACpfNro`, `CRChADtaLct`, `CMFilCod`
- `CRChAA` (Duplicate): `CRChADCx`
- `CRChAB` (Duplicate): `CRChaCPDta`
- `CRChAC` (Duplicate): `CRChACCx`
- `CRChAD` (Duplicate): `CRChaIdx`

---

### 📌 CRCla
- **Descrição:** Cadastro de Associados Sindicato
- **Chave Primária:** `CMEmpCod`, `CRClaCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRClaCod` | `N/D` | - |
| `CRClaMat` | `N/D` | - |
| `CRClaFil` | `N/D` | - |
| `CRClaNom` | `N/D` | - |
| `CRClaDtaNas` | `N/D` | - |
| `CRClaIda` | `N/D` | - |
| `CRClaNat` | `N/D` | - |
| `CRClaCid` | `N/D` | - |
| `CRClaEst` | `N/D` | - |
| `CRClaNac` | `N/D` | - |
| `CRClaEstCil` | `N/D` | - |
| `CRClaEndCli` | `N/D` | - |
| `CRClaNumCli` | `N/D` | - |
| `CRClaBaiCli` | `N/D` | - |
| `CRClaPai` | `N/D` | - |
| `CRClaMae` | `N/D` | - |
| `CRClaFir` | `N/D` | - |
| `CRClaEndFir` | `N/D` | - |
| `CRClaNumFir` | `N/D` | - |
| `CRClaBaiFir` | `N/D` | - |
| `CRClaCTPS` | `N/D` | - |
| `CRClaDECTPS` | `N/D` | - |
| `CRClaUFCTPS` | `N/D` | - |
| `CRClaSer` | `N/D` | - |
| `CRClaPro` | `N/D` | - |
| `CRClaDatFir` | `N/D` | - |
| `CRClaDatSin` | `N/D` | - |
| `CRCLANomPat` | `N/D` | - |
| `CRCLANomFaz` | `N/D` | - |
| `CRCLACidFaz` | `N/D` | - |
| `CRCLACar` | `N/D` | - |
| `CRCLARem` | `N/D` | - |
| `CRCLACartRes` | `N/D` | - |
| `CRCLASerRes` | `N/D` | - |
| `CRCLAOut` | `N/D` | - |
| `CRCLAObs` | `N/D` | - |
| `CRCLANumPro` | `N/D` | - |
| `CRCLAENDC` | `N/D` | - |
| `CRCLAEndCo` | `N/D` | - |
| `CRCLATe` | `N/D` | - |
| `CRCLAZon` | `N/D` | - |
| `CRCLAMen` | `N/D` | - |
| `CRCLATel1` | `N/D` | - |
| `CRCLATel2` | `N/D` | - |
| `CRCLATel3` | `N/D` | - |
| `CRCLABol` | `N/D` | - |
| `CRCLACidFir` | `N/D` | - |
| `CRCLARG` | `N/D` | - |
| `CRCLARGOriEmi` | `N/D` | - |
| `CRClaDERG` | `N/D` | - |
| `CRCLACPF` | `N/D` | - |
| `CRClADtaFic` | `N/D` | - |
| `CRClAUsiCod` | `N/D` | - |
| `CRClAChp` | `N/D` | - |
| `CRClaCEP` | `N/D` | - |
| `CRCLASex` | `N/D` | - |
| `CRClaMenSoc` | `N/D` | - |
| `CRClaConFed` | `N/D` | - |
| `CRClaConAss` | `N/D` | - |
| `CRClaConSin` | `N/D` | - |
| `SDUsiCod` | `N/D` | - |
| `SDUsiNomEmp` | `N/D` | - |
| `CRClaSoc` | `N/D` | - |

#### 🗺️ Índices
- `CRCla1` (Unique): `CMEmpCod`, `CRClaCod`
- `CRCla2` (Duplicate): `CMEmpCod`, `SDUsiCod`
- `CRCla3` (Duplicate): `CMEmpCod`, `CRClaNom`

---

### 📌 CRCLD
- **Descrição:** Dados do Cliente
- **Chave Primária:** `CMEmpCod`, `CRCliCod`, `CRCLDIte`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRCLDIte` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRCLDSts` | `N/D` | - |
| `CRCLDCon` | `N/D` | - |
| `CRCLDPgt02` | `N/D` | - |
| `CRCLDVct02` | `N/D` | - |
| `CRCLDVct01` | `N/D` | - |
| `CRCLDPgt01` | `N/D` | - |
| `CRCLDVlr02` | `N/D` | - |
| `CRCLDVlr01` | `N/D` | - |
| `CRCLDAux` | `N/D` | - |
| `CRCLDUSU` | `N/D` | - |
| `CRCLDTST` | `N/D` | - |
| `CRCLDOBS2` | `N/D` | - |
| `CRCLDOBS1` | `N/D` | - |
| `CRCLDOBS` | `N/D` | - |
| `CRCldCodFil` | `N/D` | - |
| `CRClDDes` | `N/D` | - |
| `CRClDDtaNsc` | `N/D` | - |
| `CRClDSerAno` | `N/D` | - |
| `CRClDNat` | `N/D` | - |
| `CRClDTipSan` | `N/D` | - |
| `CRClDCod` | `N/D` | - |
| `CRClDLog` | `N/D` | - |
| `CRClDEnd` | `N/D` | - |
| `CRClDNroCas` | `N/D` | - |
| `CRClDBai` | `N/D` | - |
| `CRClDTelAln` | `N/D` | - |
| `CRClDPai` | `N/D` | - |
| `CRClDRGPai` | `N/D` | - |
| `CRClDCPFPai` | `N/D` | - |
| `CRClDPaiEstCiv` | `N/D` | - |
| `CRClDPai01Tel` | `N/D` | - |
| `CRClDPai02Tel` | `N/D` | - |
| `CRClDProPai` | `N/D` | - |
| `CRClDMae` | `N/D` | - |
| `CRClDRGMae` | `N/D` | - |
| `CRClDCPFMae` | `N/D` | - |
| `CRClDMaeEstCiv` | `N/D` | - |
| `CRClDMae01Tel` | `N/D` | - |
| `CRClDMae02Tel` | `N/D` | - |
| `CRClDProMae` | `N/D` | - |
| `CRClDNom01` | `N/D` | - |
| `CRClDTel01` | `N/D` | - |
| `CRClDPar01` | `N/D` | - |
| `CRClDNom02` | `N/D` | - |
| `CRClDTel02` | `N/D` | - |
| `CRClDPar02` | `N/D` | - |
| `CRClDNom03` | `N/D` | - |
| `CRClDTel03` | `N/D` | - |
| `CRClDPar03` | `N/D` | - |
| `CRClDNom04` | `N/D` | - |
| `CRClDTel04` | `N/D` | - |
| `CRClDPar04` | `N/D` | - |
| `CRClDRac` | `N/D` | - |
| `CRClDCheBol` | `N/D` | - |
| `CRClDChe01` | `N/D` | - |
| `CRClDQua01` | `N/D` | - |
| `CRClDChe02` | `N/D` | - |
| `CRClDChe03` | `N/D` | - |
| `CRClDChe04` | `N/D` | - |
| `CRClDChe05` | `N/D` | - |
| `CRClDChe06` | `N/D` | - |
| `CRClDQua06` | `N/D` | - |
| `CRClDChe07` | `N/D` | - |
| `CRClDQua07` | `N/D` | - |
| `CRClDChe08` | `N/D` | - |
| `CRClDChe09` | `N/D` | - |
| `CRClDChe10` | `N/D` | - |
| `CRClDChe11` | `N/D` | - |
| `CRClDQua11` | `N/D` | - |
| `CRClDChe12` | `N/D` | - |
| `CRClDObsA` | `N/D` | - |
| `CRClDObsB` | `N/D` | - |
| `CRClDObsC` | `N/D` | - |
| `CRClDObsD` | `N/D` | - |
| `CRClDResFin` | `N/D` | - |

#### 🗺️ Índices
- `CRCLD1` (Unique): `CMEmpCod`, `CRCliCod`, `CRCLDIte`
- `CRCLD2` (Duplicate): `CMEmpCod`, `CRCliCod`
- `CRCLD3` (Duplicate): `CRCLDIte`, `CRCLDSts`

---

### 📌 CRClG1
- **Descrição:** Gastos Cliente 01 - VD
- **Chave Primária:** `CMEmpCod`, `CRCliCod`, `CRCLG1AnoMes`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRCLG1AnoMes` | `N/D` | - |
| `CRClG1Tot` | `N/D` | - |

#### 🗺️ Índices
- `CRClG1A` (Unique): `CMEmpCod`, `CRCliCod`, `CRCLG1AnoMes`
- `CRClG1B` (Duplicate): `CMEmpCod`, `CRCliCod`

---

### 📌 CRClG2
- **Descrição:** Gastos Cliente 02 - VD
- **Chave Primária:** `CMEmpCod`, `CRCliCod`, `CRCLG1AnoMes`, `CRClG2VD`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRCLG1AnoMes` | `N/D` | - |
| `CRClG1Tot` | `N/D` | - |
| `CRClG2VD` | `N/D` | - |
| `CRClG2VDDes` | `N/D` | - |
| `CRClG2Vlr` | `N/D` | - |
| `CRClG2Tst` | `N/D` | - |
| `CRClG2Prg` | `N/D` | - |
| `CRClG2Usu` | `N/D` | - |
| `CRClGVlrAbe` | `N/D` | - |
| `CRClGVlrLim` | `N/D` | - |
| `CRClGVlrSal` | `N/D` | - |

#### 🗺️ Índices
- `CRClG2A` (Unique): `CMEmpCod`, `CRCliCod`, `CRCLG1AnoMes`, `CRClG2VD`
- `CRClG2B` (Duplicate): `CMEmpCod`, `CRCliCod`, `CRCLG1AnoMes`

---

### 📌 CRCli
- **Descrição:** Cadastro de Clientes
- **Chave Primária:** `CMEmpCod`, `CRCliCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRCliPEC` | `N/D` | - |
| `CRCliVlrTA` | `N/D` | - |
| `CRCliVlrPA` | `N/D` | - |
| `CRCliVlrBA` | `N/D` | - |
| `CRCliDPA` | `N/D` | - |
| `CRCliSalCre` | `N/D` | - |
| `CRCliPonFid` | `N/D` | - |
| `CRCliDUV` | `N/D` | - |
| `CRCliCGC1` | `N/D` | - |
| `CMEmpInfLimCre` | `N/D` | - |
| `CMEmpExiFicComCli` | `N/D` | - |
| `CRCliDtaNsc` | `N/D` | - |
| `CRCliImpEtq` | `N/D` | - |
| `CRCliComE` | `N/D` | - |
| `CRCliIE1` | `N/D` | - |
| `CRCliFan` | `N/D` | - |
| `CRCliEnd` | `N/D` | - |
| `CRCliBai` | `N/D` | - |
| `CMCEPCod` | `N/D` | - |
| `CRCliLog` | `N/D` | - |
| `CMCEPDes` | `N/D` | - |
| `CMUFCod` | `N/D` | - |
| `CRCliEndC` | `N/D` | - |
| `CRCliBaiC` | `N/D` | - |
| `CRCliCidC` | `N/D` | - |
| `CRCliCepC` | `N/D` | - |
| `CRCliLogC` | `N/D` | - |
| `CRCliUfC` | `N/D` | - |
| `CRCliTel1` | `N/D` | - |
| `CRCliTel2` | `N/D` | - |
| `CRCliFax` | `N/D` | - |
| `CRCliTel3` | `N/D` | - |
| `CRCliTel4` | `N/D` | - |
| `CRCliCPF` | `N/D` | - |
| `CRCliRG` | `N/D` | - |
| `CRCliRGDtaEmi` | `N/D` | - |
| `CRTipCod` | `N/D` | - |
| `CRTipDes` | `N/D` | - |
| `CRCliAge` | `N/D` | - |
| `CRCliCon` | `N/D` | - |
| `CRCliDtUlt` | `N/D` | - |
| `CRCliCDta` | `N/D` | - |
| `CRCliCHor` | `N/D` | - |
| `CRCliCUsu` | `N/D` | - |
| `CRCliDtaImpEtq` | `N/D` | - |
| `CRCliHorImpEtq` | `N/D` | - |
| `CRCliDtaTrs` | `N/D` | - |
| `CRCliFlaDel` | `N/D` | - |
| `CRCliMesNsc` | `N/D` | - |
| `CRCliDiaNsc` | `N/D` | - |
| `CMEmpCR1TCR01B` | `N/D` | - |
| `CMEmpCR2TCR01C` | `N/D` | - |
| `CRCliLimCre` | `N/D` | - |
| `CRCliEmiCobMes` | `N/D` | - |
| `CRCliDtaUltCom` | `N/D` | - |
| `CRCliDtaPenCom` | `N/D` | - |
| `CRCliEtqNom` | `N/D` | - |
| `CRCliNroFra` | `N/D` | - |
| `CMEmpUsaSenVdaBxa` | `N/D` | - |
| `CRCliRgOrgEmi` | `N/D` | - |
| `CRCliIda` | `N/D` | - |
| `CRCliRazSoc` | `N/D` | - |
| `CRCliProPro` | `N/D` | - |
| `CRCliFlg` | `N/D` | - |
| `CRCliVdaVis` | `N/D` | - |
| `CRCliEMa` | `N/D` | - |
| `CRCliEma2` | `N/D` | - |
| `CRCliVen` | `N/D` | - |
| `CRCliCodEmpCon` | `N/D` | - |
| `CRCliCP` | `N/D` | - |
| `CRCliDUMov` | `N/D` | - |
| `CRCliMesCli` | `N/D` | - |
| `CRCliVdaSomCre` | `N/D` | - |
| `CRCliNroCas` | `N/D` | - |
| `CRCliEndCom` | `N/D` | - |
| `CRCliCom` | `N/D` | - |
| `CRCliUFRG` | `N/D` | - |
| `CRCliFisJur` | `N/D` | - |
| `CMEmpCliObr` | `N/D` | - |
| `CRCliDPP` | `N/D` | - |
| `CRCliDPPMes` | `N/D` | - |
| `CRCliFilCod` | `N/D` | - |
| `CRCliCEP` | `N/D` | - |
| `CRCliCEPCom` | `N/D` | - |
| `CRCliCPFCGC` | `N/D` | - |
| `CRCliAuxCPFCGC` | `N/D` | - |
| `CRCliPerDsc` | `N/D` | - |
| `CRCliAti` | `N/D` | - |
| `CRCliTrbDes` | `N/D` | - |
| `CRCliSexo` | `N/D` | - |
| `CRCliAno` | `N/D` | - |
| `CRCliVctPar` | `N/D` | - |
| `CRTipSts` | `N/D` | - |
| `CRCliCRCP1Cod` | `N/D` | - |
| `CRCliPerST` | `N/D` | - |
| `CRCliIndIE` | `N/D` | - |
| `CRCliTipBol` | `N/D` | - |
| `CRCliTipRecEsp` | `N/D` | - |
| `CRCliKHSts` | `N/D` | - |
| `CRCliCepE` | `N/D` | - |
| `CRCliLogE` | `N/D` | - |
| `CRCliEndE` | `N/D` | - |
| `CrCliNroE` | `N/D` | - |
| `CRCliBaiE` | `N/D` | - |
| `CRCliCidE` | `N/D` | - |
| `CRCliUFE` | `N/D` | - |
| `CRCliTel1E` | `N/D` | - |
| `CRCliTel2E` | `N/D` | - |
| `CRCliTel3E` | `N/D` | - |
| `CRCliObs1` | `N/D` | - |
| `CRCliCaSUS` | `N/D` | - |
| `CRCliCalcIR` | `N/D` | - |
| `CRCliQrBri` | `N/D` | - |
| `CRCliPerRet` | `N/D` | - |
| `CRCliVlrAtuMen` | `N/D` | - |
| `CRCliDiaVctBol` | `N/D` | - |
| `CRCliObs2` | `N/D` | - |
| `CRCliTrbTel` | `N/D` | - |
| `CRCliTrbCargo` | `N/D` | - |
| `CRCliTrbPeriodo` | `N/D` | - |
| `CRCliTrbSal` | `N/D` | - |
| `CRCliTrbNomEnc` | `N/D` | - |
| `CRCliTrbCDes` | `N/D` | - |
| `CRCliTrbCTempo` | `N/D` | - |
| `CRCliTrbCSal` | `N/D` | - |
| `CRCliTrbCCargo` | `N/D` | - |
| `CRCliTrbCEnc` | `N/D` | - |
| `CRCliTrbEmpAnt` | `N/D` | - |
| `CRCliConj` | `N/D` | - |
| `CRCliConjNsc` | `N/D` | - |
| `CRCliCon1` | `N/D` | - |
| `CRCliCon2` | `N/D` | - |
| `CRCliLimMes` | `N/D` | - |
| `CRCliAutCnv` | `N/D` | - |
| `CRCliDtaAdm` | `N/D` | - |
| `CRCliIdx` | `N/D` | - |
| `CRCLICRG` | `N/D` | - |
| `CRCliCCPF` | `N/D` | - |
| `CRCliCETr` | `N/D` | - |
| `CRCLiAut` | `N/D` | - |
| `CRCliTrbEnd` | `N/D` | - |
| `CRCliPerLimCre` | `N/D` | - |
| `CRCliTipCasa` | `N/D` | - |
| `CRCliVlrAlu` | `N/D` | - |
| `CRCliOutRend` | `N/D` | - |
| `CRCliSpc` | `N/D` | - |
| `CRCliSpcDta` | `N/D` | - |
| `CRCliSpcNom` | `N/D` | - |
| `CRCliTelChq` | `N/D` | - |
| `CRCliAvalista` | `N/D` | - |
| `CRCliAvalCic` | `N/D` | - |
| `CRCliRefCom` | `N/D` | - |
| `CRCliTemEnd` | `N/D` | - |
| `CRCliLocNsc` | `N/D` | - |
| `CRCliEstCiv` | `N/D` | - |
| `CRCliPai` | `N/D` | - |
| `CRCliMae` | `N/D` | - |
| `CRCliFecMes` | `N/D` | - |
| `CRCliFecDia` | `N/D` | - |
| `CRCliFecBolDia` | `N/D` | - |
| `CRCliIRRF` | `N/D` | - |
| `CRCliRefBco` | `N/D` | - |
| `CRCliDtaVctLic` | `N/D` | - |
| `CRCliImpTotAbe` | `N/D` | - |
| `CRCliLibCon` | `N/D` | - |
| `CRCliNF` | `N/D` | - |
| `CRCliDtaCas` | `N/D` | - |
| `CRCliUsuCta` | `N/D` | - |
| `CRCliQPP` | `N/D` | - |
| `CRCliVPP` | `N/D` | - |
| `CRCliVlrCreAbe` | `N/D` | - |
| `CRCliObs3` | `N/D` | - |
| `CRCliObs4` | `N/D` | - |
| `CRCliDtaInsPro` | `N/D` | - |
| `CRCliDta_UltAum` | `N/D` | - |
| `CRCliVlrUltMen` | `N/D` | - |
| `CRCliDtaBolUlt` | `N/D` | - |
| `CMEmpPrc1` | `N/D` | - |
| `CMEmpPrc2` | `N/D` | - |
| `CRCliVlrIns` | `N/D` | - |
| `CRCliDtaPgtIns` | `N/D` | - |
| `CRCliQtdMicIns` | `N/D` | - |
| `CRCliPrcQtdSalMin` | `N/D` | - |
| `CRCliQtdPadDiaLib` | `N/D` | - |
| `CRCliVlrS1` | `N/D` | - |
| `CRCliVlrS2` | `N/D` | - |
| `CRCliVlrSF` | `N/D` | - |
| `CRCliPAm` | `N/D` | - |
| `CRCliVAm` | `N/D` | - |
| `CRCliVAA` | `N/D` | - |
| `CRCLiPAA` | `N/D` | - |
| `CRCliDtaPriBolEmi` | `N/D` | - |
| `CRCliDtaLibUlt` | `N/D` | - |
| `CRCliQtdDiaLib` | `N/D` | - |
| `CRCliLibInt` | `N/D` | - |
| `CRCliPrxVctSis` | `N/D` | - |
| `CRCliDUP` | `N/D` | - |
| `CRCLIDLP` | `N/D` | - |
| `CRCLICPC` | `N/D` | - |
| `CRCliRelFac` | `N/D` | - |
| `CRCliRelWat` | `N/D` | - |
| `CRCliRelSky` | `N/D` | - |
| `CRCliSenDrop` | `N/D` | - |
| `CRCliCPE` | `N/D` | - |
| `CRCliTel1C` | `N/D` | - |
| `CRCliTel2C` | `N/D` | - |
| `CRCliTel3C` | `N/D` | - |

#### 🗺️ Índices
- `CRCliA` (Unique): `CMEmpCod`, `CRCliCod`
- `CRCliD` (Duplicate): `CMCEPCod`
- `CRCliE` (Duplicate): `CMEmpCod`, `CRTipCod`
- `CRCli1` (Duplicate): `CMEmpCod`, `CRCliDes`
- `CRCli2` (Duplicate): `CRCliMesCli`
- `CRCli3` (Duplicate): `CMEmpCod`, `CRCliDtaImpEtq`, `CRCliDes`
- `CRCli4` (Duplicate): `CMEmpCod`, `CRCliSpc`
- `CRCli5` (Duplicate): `CRCliCodEmpCon`
- `CRCli6` (Duplicate): `CMEmpCod`, `CRCliMesNsc`, `CRCliDiaNsc`
- `CRCli7` (Duplicate): `CRCliAuxCPFCGC`
- `CRCli8` (Duplicate): `CRCliDtaImpEtq`, `CRCliBai`, `CRCliDes`
- `CRCli9` (Duplicate): `CRCliIdx`

---

### 📌 CRCliC
- **Descrição:** Características do Cliente
- **Chave Primária:** `CMEmpCod`, `CRCliCod`, `CRCrtCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRCliQPP` | `N/D` | - |
| `CRCliVPP` | `N/D` | - |
| `CRCrtCod` | `N/D` | - |
| `CRCrtDes` | `N/D` | - |
| `CRCliCSenAce` | `N/D` | - |
| `CRCLiCUsuAce` | `N/D` | - |
| `CRCliCObs` | `N/D` | - |

#### 🗺️ Índices
- `CRCliC1` (Unique): `CMEmpCod`, `CRCliCod`, `CRCrtCod`
- `CRCliC2` (Duplicate): `CMEmpCod`, `CRCliCod`
- `CRCliC3` (Duplicate): `CMEmpCod`, `CRCrtCod`

---

### 📌 CRCLO
- **Descrição:** Observações Gerais do Cliente
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRCliCod`, `CRClODta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRClODta` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRClODtaSol` | `N/D` | - |
| `CRClODes` | `N/D` | - |
| `CRCloDes1` | `N/D` | - |
| `CRClODes2` | `N/D` | - |
| `CRClODes3` | `N/D` | - |
| `CRClODes4` | `N/D` | - |
| `CRCloDes5` | `N/D` | - |
| `CRCloDes6` | `N/D` | - |
| `CRCloDes7` | `N/D` | - |
| `CRCloDes8` | `N/D` | - |
| `CRClODesRes` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CRClOMosDes` | `N/D` | - |
| `CRClOQtdDiaLib` | `N/D` | - |
| `CRClOSts` | `N/D` | - |
| `CRClODtaPrxAvi` | `N/D` | - |
| `CRTipCod` | `N/D` | - |
| `CRTipDes` | `N/D` | - |
| `CRCLOUSU` | `N/D` | - |
| `CRCloUsuSol` | `N/D` | - |
| `CRClOTip` | `N/D` | - |
| `CRClOTec` | `N/D` | - |
| `CRClOPri` | `N/D` | - |
| `CRClOLnk01` | `N/D` | - |
| `CRCloLnk02` | `N/D` | - |
| `CRCloIdx` | `N/D` | - |
| `CRCloDtaCli` | `N/D` | - |
| `CRCloAviTec` | `N/D` | - |
| `CRCloUsuResAtu` | `N/D` | - |
| `CRCloPgm` | `N/D` | - |
| `CRCloPrgDes` | `N/D` | - |
| `CRCliVlrAtuMen` | `N/D` | - |
| `CRCliDPA` | `N/D` | - |
| `CRCloEnd` | `N/D` | - |
| `CRCloTel` | `N/D` | - |
| `CRCloDtaLct` | `N/D` | - |
| `CRCloNroLct` | `N/D` | - |
| `CRCloVlrHor` | `N/D` | - |
| `CRCloDur` | `N/D` | - |
| `CRCloAgeUsu` | `N/D` | - |
| `CRCloAgeDta` | `N/D` | - |
| `CRCloAgeHra` | `N/D` | - |

#### 🗺️ Índices
- `CRCLO1` (Unique): `CMEmpCod`, `CMFilCod`, `CRCliCod`, `CRClODta`
- `CRCLO2` (Duplicate): `CMEmpCod`, `CRCliCod`
- `CRCLO3` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CRCLO4` (Duplicate): `CMEmpCod`, `CRClODtaPrxAvi`
- `CRCLO5` (Duplicate): `CMEmpCod`, `CRCliCod`, `CRClODta`
- `CRCLO6` (Duplicate): `CRCloDtaLct`
- `CRCLO7` (Duplicate): `CMEmpCod`, `CRClODtaSol`, `CRClODtaPrxAvi`
- `CRClO8` (Duplicate): `CRCloIdx`
- `CRCLo9` (Duplicate): `CRCloDtaCli`
- `CRCLOA` (Duplicate): `CRCloDtaLct`

---

### 📌 CRClr
- **Descrição:** Receituário Médito
- **Chave Primária:** `CMEmpCod`, `CRClrMovFil`, `CRClrMovDta`, `CRClrMovSeq`, `CRClRSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRClrMovFil` | `N/D` | - |
| `CRClrMovDta` | `N/D` | - |
| `CRClrMovSeq` | `N/D` | - |
| `CRClRSeq` | `N/D` | - |
| `CRClRIte1` | `N/D` | - |
| `CRClRIte2` | `N/D` | - |
| `CRClRIte3` | `N/D` | - |
| `CRClRIte4` | `N/D` | - |
| `CRClRDta` | `N/D` | - |
| `CRClRPro1Cod` | `N/D` | - |
| `CRClaNom` | `N/D` | - |
| `CRClrCliNom` | `N/D` | - |
| `CRClr1ProDes` | `N/D` | - |
| `CRClr2ProDes` | `N/D` | - |
| `CRClr3ProDes` | `N/D` | - |
| `CRClr4ProDes` | `N/D` | - |
| `CRClaCod` | `N/D` | - |
| `CRClRLte` | `N/D` | - |
| `CRClRCiODL` | `N/D` | - |
| `CRClREsOdL` | `N/D` | - |
| `CRClREiOEL` | `N/D` | - |
| `CRClREiODL` | `N/D` | - |
| `CRClRDPODL` | `N/D` | - |
| `CRClREsOeL` | `N/D` | - |
| `CRClRCiOEL` | `N/D` | - |
| `CRClREsOdP` | `N/D` | - |
| `CRClREiODP` | `N/D` | - |
| `CRClRCIODP` | `N/D` | - |
| `CRClRDPOEL` | `N/D` | - |
| `CRClRDPODP` | `N/D` | - |
| `CRClREsOEP` | `N/D` | - |
| `CRClREiOEP` | `N/D` | - |
| `CRClRCIOEP` | `N/D` | - |
| `CRCLrAdc` | `N/D` | - |
| `CRClRDPOEP` | `N/D` | - |
| `CRClRFil` | `N/D` | - |
| `CRClaUsu` | `N/D` | - |
| `CRClaDtaCon` | `N/D` | - |
| `CRClaHraCon` | `N/D` | - |
| `CRClRAlt` | `N/D` | - |
| `CRClRAdc2` | `N/D` | - |
| `CRClRObs` | `N/D` | - |
| `CRClRAlt2` | `N/D` | - |
| `CRClRObs1` | `N/D` | - |
| `CRClrCliCod` | `N/D` | - |
| `CRClRCliDes` | `N/D` | - |
| `CRClrPro1Des` | `N/D` | - |
| `CRClrPro2Des` | `N/D` | - |
| `CRClrPro3Des` | `N/D` | - |
| `CRClrPro4Des` | `N/D` | - |
| `CRClrFor1Cod` | `N/D` | - |
| `CRClrFor2Cod` | `N/D` | - |
| `CRClrFor3Cod` | `N/D` | - |
| `CRClrFor4Cod` | `N/D` | - |
| `CRClrPro2Cod` | `N/D` | - |
| `CRClrPro3Cod` | `N/D` | - |
| `CRClrPro4Cod` | `N/D` | - |
| `CRClrIdx` | `N/D` | - |
| `CRClRQtdImp` | `N/D` | - |
| `CRClr1ProQtd` | `N/D` | - |
| `CRClr2ProQtd` | `N/D` | - |
| `CRClr3ProQtd` | `N/D` | - |
| `CRClr4ProQtd` | `N/D` | - |
| `CRClrTST` | `N/D` | - |
| `CRClrFasCod` | `N/D` | - |
| `CRClrFas_Cor` | `N/D` | - |
| `CRClrFasDes` | `N/D` | - |
| `CRClrDPrEnt` | `N/D` | - |
| `CRClrMed` | `N/D` | - |
| `CRClrMedTip` | `N/D` | - |
| `CRClrMedNom` | `N/D` | - |
| `CRClrEnvMed` | `N/D` | - |
| `CRClrTSTAltFas` | `N/D` | - |
| `CRClrStsCP` | `Character(1)` | CRClrStsCP |
| `CRClrSts1CP` | `N/D` | - |
| `CRClrSts2CP` | `N/D` | - |
| `CRClrSts3CP` | `N/D` | - |
| `CRClrSts4CP` | `N/D` | - |
| `CRClrObs3` | `N/D` | - |
| `CRClrObs4` | `N/D` | - |
| `CRClrDtaCP` | `N/D` | - |
| `CRClrP_A` | `N/D` | - |
| `CRClrP_A2` | `N/D` | - |
| `CRClrD_M` | `N/D` | - |
| `CRClrD_M2` | `N/D` | - |
| `CRClrTAr` | `N/D` | - |
| `CRClrFor1Des` | `N/D` | - |
| `CRClrFor2Des` | `N/D` | - |
| `CRClrFor3Des` | `N/D` | - |
| `CRClrFor4Des` | `N/D` | - |
| `CRClrDV` | `N/D` | - |
| `CRClrDV2` | `N/D` | - |
| `CRClrTstA_P` | `N/D` | - |
| `CRClrTstP_F` | `N/D` | - |
| `CRClrUsuA_P` | `N/D` | - |
| `CRClrUsuP_F` | `N/D` | - |
| `CRClr1ForCod` | `N/D` | - |
| `CRClr2ForCod` | `N/D` | - |
| `CRClr3ForCod` | `N/D` | - |
| `CRClr4ForCod` | `N/D` | - |
| `CRClrForCod` | `N/D` | - |
| `CRClrForDes` | `N/D` | - |
| `CRClrVlrReq` | `N/D` | - |
| `CRClrVlrFor` | `N/D` | - |
| `CRClrVlrDif` | `N/D` | - |
| `CRClrNroNF` | `N/D` | - |
| `CRClrSerNF` | `N/D` | - |
| `CRClrDtaNF` | `N/D` | - |
| `CRClrVend` | `N/D` | - |
| `CRClrJEP` | `N/D` | - |
| `CRClrPEP` | `N/D` | - |
| `CRClrJND` | `N/D` | - |
| `CRClrJNE` | `N/D` | - |
| `CRClrPND` | `N/D` | - |
| `CRClrPNE` | `N/D` | - |
| `CRClrJCD` | `N/D` | - |
| `CRClrJCE` | `N/D` | - |
| `CRClrPCD` | `N/D` | - |
| `CRClrPCE` | `N/D` | - |
| `CRClrJTD` | `N/D` | - |
| `CRClrJTE` | `N/D` | - |
| `CRClrPTD` | `N/D` | - |
| `CRClrPTE` | `N/D` | - |
| `CRClrCol` | `N/D` | - |
| `CRClrDPrMon` | `N/D` | - |
| `CRClrSit` | `N/D` | - |
| `CRClrBcoCod` | `N/D` | - |
| `CRClrPro1Qtd` | `N/D` | - |
| `CRClrPro2Qtd` | `N/D` | - |
| `CRClrPro3Qtd` | `N/D` | - |
| `CRClrPro4Qtd` | `N/D` | - |

#### 🗺️ Índices
- `CRClrA` (Unique): `CMEmpCod`, `CRClrMovFil`, `CRClrMovDta`, `CRClrMovSeq`, `CRClRSeq`
- `CRClrB` (Duplicate): `CMEmpCod`, `CRClaCod`
- `CRClrC` (Duplicate): `CMEmpCod`, `CRClrCliCod`
- `CRClrD` (Duplicate): `CMEmpCod`, `CRClRSeq`
- `CRClrE` (Duplicate): `CRClrFasCod`
- `CRClrF` (Duplicate): `CRClrTST`
- `CRClrG` (Duplicate): `CRClrTSTAltFas`
- `CRClrH` (Duplicate): `CRClrStsCP`, `CRClRSeq`
- `CRClrI` (Duplicate): `CRClrMovDta`
- `CRClrJ` (Duplicate): `CRClrDtaCP`, `CRClrStsCP`
- `CRClrK` (Duplicate): `CRClrStsCP`, `CRClrMovDta`
- `CRClrL` (Duplicate): `CRClrTstA_P`
- `CRClrM` (Duplicate): `CRClrTstP_F`

---

### 📌 CRClT
- **Descrição:** Telefones/Senhas do Cliente
- **Chave Primária:** `CMEmpCod`, `CRCliCod`, `CRCltSeq`, `CMOTeCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRCliCGC1` | `N/D` | - |
| `CRCltSeq` | `N/D` | - |
| `CMOTeCod` | `N/D` | - |
| `CRCltTel` | `N/D` | - |
| `CMOTeDes` | `N/D` | - |
| `CRCltObs` | `N/D` | - |
| `CRCltCNPJ` | `N/D` | - |
| `CRCltNrSerie` | `N/D` | - |
| `CRCltNrSeg` | `N/D` | - |
| `CRCltMac` | `N/D` | - |
| `CRCltCodAt` | `N/D` | - |
| `CRCltChvVin` | `N/D` | - |
| `CRCltSts` | `N/D` | - |

#### 🗺️ Índices
- `CRClT1` (Unique): `CMEmpCod`, `CRCliCod`, `CRCltSeq`, `CMOTeCod`
- `CRClT2` (Duplicate): `CMOTeCod`
- `CRClT3` (Duplicate): `CMEmpCod`, `CRCliCod`

---

### 📌 CRClV
- **Descrição:** Cadastro Clientes x Veículos
- **Chave Primária:** `CMEmpCod`, `CRCliCod`, `CRClVSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRClVSeq` | `N/D` | - |
| `CRVeiPlc` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRVeiCil` | `N/D` | - |
| `CRVeiMar` | `N/D` | - |
| `CRVeiKM` | `N/D` | - |
| `CRVeiAno` | `N/D` | - |
| `CRVeiCor` | `N/D` | - |
| `CRVeiChas` | `N/D` | - |
| `CRVeiMedCom` | `N/D` | - |
| `CRVeiDes` | `N/D` | - |
| `CRClVNom` | `N/D` | - |
| `CRClVDtaNsc` | `N/D` | - |
| `CRClVRac` | `N/D` | - |
| `CRClVPed` | `N/D` | - |

#### 🗺️ Índices
- `CRClV1` (Unique): `CMEmpCod`, `CRCliCod`, `CRClVSeq`
- `CRClV2` (Duplicate): `CRVeiPlc`
- `CRClV3` (Duplicate): `CMEmpCod`, `CRCliCod`

---

### 📌 CRClVH
- **Descrição:** Histórico Movimentos Veículos/Animais
- **Chave Primária:** `CMEmpCod`, `CRCliCod`, `CRClVSeq`, `CRClVHTST`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRClVSeq` | `N/D` | - |
| `CRClVHTST` | `N/D` | - |
| `CRClVHUSU` | `N/D` | - |
| `CRClVHPRG` | `N/D` | - |
| `CRClVHObs1` | `N/D` | - |
| `CRClVHObs2` | `N/D` | - |
| `CRClVHObs3` | `N/D` | - |
| `CRClVNom` | `N/D` | - |
| `CRClVDtaNsc` | `N/D` | - |
| `CRClVRac` | `N/D` | - |
| `CRClVPed` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRVeiPlc` | `N/D` | - |
| `CRVeiDes` | `N/D` | - |
| `CRVeiMar` | `N/D` | - |
| `CRVeiCor` | `N/D` | - |
| `CRClVHDtaMov` | `N/D` | - |
| `CRClVHSeqMov` | `N/D` | - |
| `CRClVHFilMov` | `N/D` | - |

#### 🗺️ Índices
- `CRClVH1` (Unique): `CMEmpCod`, `CRCliCod`, `CRClVSeq`, `CRClVHTST`
- `CRClVH2` (Duplicate): `CMEmpCod`, `CRCliCod`, `CRClVSeq`
- `CRClVH3` (Duplicate): `CMEmpCod`, `CRCliCod`, `CRClVSeq`, `CRClVHTST`

---

### 📌 CRCM1
- **Descrição:** Controle Cartão Magnético
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRCM1Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRCM1Cod` | `N/D` | - |
| `CRCM1Prg` | `N/D` | - |
| `CRCM1Usu` | `N/D` | - |
| `CRCM1TST` | `N/D` | - |
| `CRCM1Des` | `N/D` | - |
| `CRCM1CliCod` | `N/D` | - |
| `CRCM1CliDes` | `N/D` | - |
| `CRCM1Sts` | `N/D` | - |
| `CRCM1Apt` | `N/D` | - |
| `CRCM1CodAlt` | `N/D` | - |

#### 🗺️ Índices
- `CRCM1A` (Unique): `CMEmpCod`, `CMFilCod`, `CRCM1Cod`
- `CRCM1B` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CRCM1C` (Duplicate): `CRCM1CodAlt`

---

### 📌 CRCP1
- **Descrição:** Condições de Pagamento
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRCP1Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRCP1Cod` | `N/D` | - |
| `CRCP1Des` | `N/D` | - |
| `CRCP1QtdPar` | `N/D` | - |
| `CRCP1PrcJrs` | `N/D` | - |
| `CRCP1TipJrs` | `N/D` | - |
| `CRCP1ExiSen` | `N/D` | - |
| `CRCP1Aux` | `N/D` | - |
| `CRCP1AltVct` | `N/D` | - |
| `CPCP1PerDesc` | `N/D` | - |

#### 🗺️ Índices
- `CRCP1A` (Unique): `CMEmpCod`, `CMFilCod`, `CRCP1Cod`
- `CRCP1B` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CRCP2
- **Descrição:** Condições de Pagamento
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRCP1Cod`, `CRCP2Par`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRCP1Cod` | `N/D` | - |
| `CRCP1Des` | `N/D` | - |
| `CRCP1QtdPar` | `N/D` | - |
| `CRCP1PrcJrs` | `N/D` | - |
| `CRCP1TipJrs` | `N/D` | - |
| `CRCP1ExiSen` | `N/D` | - |
| `CRCP1Aux` | `N/D` | - |
| `CRCP1AltVct` | `N/D` | - |
| `CPCP1PerDesc` | `N/D` | - |
| `CRCP2Par` | `N/D` | - |
| `CRCP2QtdDia` | `N/D` | - |

#### 🗺️ Índices
- `CRCP2A` (Unique): `CMEmpCod`, `CMFilCod`, `CRCP1Cod`, `CRCP2Par`
- `CRCP2B` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRCP1Cod`

---

### 📌 CRCre1
- **Descrição:** Controla Crédito Cliente 01
- **Chave Primária:** `CMEmpCod`, `CRCliCod`, `CRCre1Dta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRCre1Dta` | `N/D` | - |
| `CRCre1AuxSeq` | `N/D` | - |
| `CRCre1CDta` | `N/D` | - |
| `CRCre1CHor` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRCre1CUsu` | `N/D` | - |
| `CRCre1CPrg` | `N/D` | - |
| `CRCre1DtaTrs` | `N/D` | - |
| `CRCre1FlaDel` | `N/D` | - |
| `CRCliLimCre` | `N/D` | - |
| `CRCliVlrCreAbe` | `N/D` | - |
| `CRCre1FilCod` | `N/D` | - |

#### 🗺️ Índices
- `CRCre1A` (Unique): `CMEmpCod`, `CRCliCod`, `CRCre1Dta`
- `CRCre1B` (Duplicate): `CMEmpCod`, `CRCliCod`
- `CRCre1C` (Duplicate): `CMEmpCod`, `CRCre1Dta`

---

### 📌 CRCre2
- **Descrição:** Controla Crédito Cliente 02
- **Chave Primária:** `CMEmpCod`, `CRCliCod`, `CRCre1Dta`, `CRCre2Seq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRCre1Dta` | `N/D` | - |
| `CRCre1AuxSeq` | `N/D` | - |
| `CRCre1CDta` | `N/D` | - |
| `CRCre1CHor` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRCre1CUsu` | `N/D` | - |
| `CRCre1CPrg` | `N/D` | - |
| `CRCre1DtaTrs` | `N/D` | - |
| `CRCre1FlaDel` | `N/D` | - |
| `CRCliLimCre` | `N/D` | - |
| `CRCliVlrCreAbe` | `N/D` | - |
| `CRCre1FilCod` | `N/D` | - |
| `CRCre2Seq` | `N/D` | - |
| `CRCre2CUsu` | `N/D` | - |
| `CRCre2CHor` | `N/D` | - |
| `CRCre2CDta` | `N/D` | - |
| `CRCre2CPrg` | `N/D` | - |
| `CRCre2DtaTrs` | `N/D` | - |
| `CRCre2FlaDel` | `N/D` | - |
| `CRCre2DtaMovOrg` | `N/D` | - |
| `CRCre2SeqMovOrg` | `N/D` | - |
| `CRCre2ParMovOrg` | `N/D` | - |
| `CRCre2CreDeb` | `N/D` | - |
| `CRCre2Vlr` | `N/D` | - |
| `CRCre2SalApoMov` | `N/D` | - |
| `CRCre2Obs1` | `N/D` | - |
| `CRCre2Obs2` | `N/D` | - |
| `CRCre2Obs3` | `N/D` | - |
| `CRCre2CheOut` | `N/D` | - |
| `CRCre2Mov5Org` | `N/D` | - |
| `CRCre2Cxa` | `N/D` | - |
| `CRCre2DCx` | `N/D` | - |
| `CRCre2FilCod` | `N/D` | - |
| `CRCre2Org` | `N/D` | - |
| `CRCre2CPCliCod` | `N/D` | - |
| `CRCre2ForFan` | `N/D` | - |
| `CRCre2ForRaz` | `N/D` | - |
| `CRCre2CCx` | `N/D` | - |
| `CRCre2Mov6Seq` | `N/D` | - |
| `CRCre2Tst` | `N/D` | - |

#### 🗺️ Índices
- `CRCre2A` (Unique): `CMEmpCod`, `CRCliCod`, `CRCre1Dta`, `CRCre2Seq`
- `CRCre2B` (Duplicate): `CMEmpCod`, `CRCliCod`, `CRCre1Dta`
- `CRCre2C` (Duplicate): `CMEmpCod`, `CRCliCod`, `CRCre1Dta`, `CRCre2Seq`
- `CRCre2D` (Duplicate): `CRCre2DCx`
- `CRCre2E` (Duplicate): `CMEmpCod`, `CRCre1Dta`
- `CRCre2F` (Duplicate): `CRCre2CCx`

---

### 📌 CRCrt
- **Descrição:** Características
- **Chave Primária:** `CMEmpCod`, `CRCrtCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCrtCod` | `N/D` | - |
| `CRCrtDes` | `N/D` | - |
| `CRCrtCHor` | `N/D` | - |
| `CRCrtCUsu` | `N/D` | - |
| `CRCrtCPrg` | `N/D` | - |
| `CRCrtCDta` | `N/D` | - |

#### 🗺️ Índices
- `CRCrt1` (Unique): `CMEmpCod`, `CRCrtCod`
- `CRCrt2` (Duplicate): `CMEmpCod`

---

### 📌 CRCxP
- **Descrição:** Produtos Periódicos
- **Chave Primária:** `CMEmpCod`, `CRCliCod`, `CRCxPProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRCxPProCod` | `N/D` | - |
| `CRCxPDtaVct` | `N/D` | - |
| `CRCXPQtdDia` | `N/D` | - |
| `CRCxPDtaUltCom` | `N/D` | - |
| `CRCxPProPer` | `N/D` | - |
| `CRCxPFilCod` | `N/D` | - |
| `CRCxPProDes` | `N/D` | - |

#### 🗺️ Índices
- `CRCxP1` (Unique): `CMEmpCod`, `CRCliCod`, `CRCxPProCod`
- `CRCxP2` (Duplicate): `CMEmpCod`, `CRCliCod`
- `CRCxP3` (Duplicate): `CMEmpCod`, `CRCxPDtaVct`

---

### 📌 CRDep
- **Descrição:** Dependentes
- **Chave Primária:** `CMEmpCod`, `CRCliCod`, `CRDepNom`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRDepNom` | `N/D` | - |
| `CRDepCDta` | `N/D` | - |
| `CRDepCHor` | `N/D` | - |
| `CRDepCUsu` | `N/D` | - |
| `CRDepDiaNsc` | `N/D` | - |
| `CRDepMesNsc` | `N/D` | - |
| `CRDepDtaNsc` | `N/D` | - |
| `CRDepDtaTrs` | `N/D` | - |
| `CRDepTip` | `N/D` | - |
| `CRDepEmiEtqAni` | `N/D` | - |
| `CRDepIda` | `N/D` | - |
| `CRDepDtaHorEtq` | `N/D` | - |
| `CRDepCPF` | `N/D` | - |
| `CRDepRG` | `N/D` | - |
| `CRDepEnd` | `N/D` | - |
| `CRDepBai` | `N/D` | - |
| `CRDepNroCas` | `N/D` | - |
| `CRDepCEP` | `N/D` | - |
| `CRDepCid` | `N/D` | - |
| `CRDepUF` | `N/D` | - |
| `CRDepCom` | `N/D` | - |
| `CRDepTel1` | `N/D` | - |
| `CRDepTel2` | `N/D` | - |
| `CRDepDtaUltCom` | `N/D` | - |
| `CRDepFilCod` | `N/D` | - |
| `CRDepSexo` | `N/D` | - |
| `CRDepCLTt2Seq` | `N/D` | - |
| `CRDepCod` | `N/D` | - |
| `CRCliSexo` | `N/D` | - |
| `CRCliDtaNsc` | `N/D` | - |
| `CRCliTel2` | `N/D` | - |
| `CRCliTel1` | `N/D` | - |

#### 🗺️ Índices
- `CRDep1` (Unique): `CMEmpCod`, `CRCliCod`, `CRDepNom`
- `CRDep2` (Duplicate): `CMEmpCod`, `CRCliCod`
- `CRDep3` (Duplicate): `CMEmpCod`, `CRDepMesNsc`, `CRDepDiaNsc`
- `CRDep4` (Duplicate): `CRDepNom`

---

### 📌 CRDepC
- **Descrição:** Características do Dependente
- **Chave Primária:** `CMEmpCod`, `CRCliCod`, `CRDepNom`, `CRDepCrt`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRDepNom` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRDepDiaNsc` | `N/D` | - |
| `CRDepDtaNsc` | `N/D` | - |
| `CRDepEmiEtqAni` | `N/D` | - |
| `CRDepIda` | `N/D` | - |
| `CRDepTip` | `N/D` | - |
| `CRDepCrt` | `N/D` | - |
| `CRDepCrtDes` | `N/D` | - |

#### 🗺️ Índices
- `CRDepC1` (Unique): `CMEmpCod`, `CRCliCod`, `CRDepNom`, `CRDepCrt`
- `CRDepC2` (Duplicate): `CMEmpCod`, `CRCliCod`, `CRDepNom`

---

### 📌 CREnc1
- **Descrição:** Tabela Encomendas \ Entregas 1
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CREnc1Dta`, `CREnc1Hra`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CREnc1Dta` | `N/D` | - |
| `CREnc1Hra` | `N/D` | - |
| `CREnc1Tot` | `N/D` | - |
| `CREnc1Obs1` | `N/D` | - |
| `CREnc1Obs2` | `N/D` | - |
| `CREnc1CliDes` | `N/D` | - |
| `CREnc1CliTel` | `N/D` | - |
| `CREnc1Tip` | `N/D` | - |
| `CREnc1CHor` | `N/D` | - |
| `CREnc1CPrg` | `N/D` | - |
| `CREnc1CDta` | `N/D` | - |
| `CREnc1CUsu` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CPCliCod` | `N/D` | - |

#### 🗺️ Índices
- `CREnc11` (Unique): `CMEmpCod`, `CMFilCod`, `CREnc1Dta`, `CREnc1Hra`
- `CREnc12` (Duplicate): `CMEmpCod`, `CPCliCod`
- `CREnc13` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CREnc2
- **Descrição:** Tabela Encomendas \ Entregas 2
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CREnc1Dta`, `CREnc1Hra`, `CREnc2ProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CREnc1Dta` | `N/D` | - |
| `CREnc1Hra` | `N/D` | - |
| `CREnc1Tot` | `N/D` | - |
| `CREnc1Obs1` | `N/D` | - |
| `CREnc1Obs2` | `N/D` | - |
| `CREnc1CliDes` | `N/D` | - |
| `CREnc1CliTel` | `N/D` | - |
| `CREnc1Tip` | `N/D` | - |
| `CREnc1CHor` | `N/D` | - |
| `CREnc1CPrg` | `N/D` | - |
| `CREnc1CDta` | `N/D` | - |
| `CREnc1CUsu` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `CREnc2ProCod` | `N/D` | - |
| `CREnc2ProDes` | `N/D` | - |
| `CREnc2PreTab` | `N/D` | - |
| `CREnc2PreCus` | `N/D` | - |
| `CREnc2TotPro` | `N/D` | - |
| `CREnc2Qtd` | `N/D` | - |

#### 🗺️ Índices
- `CREnc21` (Unique): `CMEmpCod`, `CMFilCod`, `CREnc1Dta`, `CREnc1Hra`, `CREnc2ProCod`
- `CREnc22` (Duplicate): `CMEmpCod`, `CMFilCod`, `CREnc1Dta`, `CREnc1Hra`

---

### 📌 CRFPC
- **Descrição:** Cabeçalho Venda Farmácia Popular
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRFPCCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRFPCCod` | `N/D` | - |
| `CRFPCUsu` | `N/D` | - |
| `CRFPCPrg` | `N/D` | - |
| `CRFPCTST` | `N/D` | - |
| `CRFPCCPF` | `N/D` | - |
| `CRFPCCRM` | `N/D` | - |
| `CRFPCDesPrf` | `N/D` | - |
| `CRFPCUFP` | `N/D` | - |
| `CRFPCDtaRec` | `N/D` | - |
| `CRFPCCPA` | `N/D` | - |
| `CRFPCCAu` | `N/D` | - |
| `CRFPCCCa` | `N/D` | - |
| `CRFPCNNF` | `N/D` | - |
| `CRFPCCliDes` | `N/D` | - |
| `CRFPCCliCod` | `N/D` | - |
| `CRFPCSts` | `N/D` | - |
| `CRFPCForPgt` | `N/D` | - |
| `CRFPCDta` | `N/D` | - |
| `CRFPCSeq` | `N/D` | - |
| `CRFPCVlrCli` | `N/D` | - |
| `CRFPCVlrGov` | `N/D` | - |
| `CRFPCIdx` | `N/D` | - |

#### 🗺️ Índices
- `CRFPC1` (Unique): `CMEmpCod`, `CMFilCod`, `CRFPCCod`
- `CRFPC2` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CRFPC3` (Duplicate): `CRFPCDta`, `CRFPCSeq`
- `CRFPC4` (Duplicate): `CRFPCIdx`

---

### 📌 CRFPM
- **Descrição:** Mercadorias da Farmácia Popular
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRFPCCod`, `CEProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRFPCCod` | `N/D` | - |
| `CRFPCUsu` | `N/D` | - |
| `CRFPCPrg` | `N/D` | - |
| `CRFPCTST` | `N/D` | - |
| `CRFPCCPF` | `N/D` | - |
| `CRFPCCRM` | `N/D` | - |
| `CRFPCDesPrf` | `N/D` | - |
| `CRFPCUFP` | `N/D` | - |
| `CRFPCDtaRec` | `N/D` | - |
| `CRFPCCPA` | `N/D` | - |
| `CRFPCCAu` | `N/D` | - |
| `CRFPCCCa` | `N/D` | - |
| `CRFPCNNF` | `N/D` | - |
| `CRFPCCliDes` | `N/D` | - |
| `CRFPCCliCod` | `N/D` | - |
| `CRFPCSts` | `N/D` | - |
| `CRFPCForPgt` | `N/D` | - |
| `CRFPCDta` | `N/D` | - |
| `CRFPCSeq` | `N/D` | - |
| `CRFPCVlrCli` | `N/D` | - |
| `CRFPCVlrGov` | `N/D` | - |
| `CRFPCIdx` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CRFPMQtdSol` | `N/D` | - |
| `CRFPMQtdApr` | `N/D` | - |
| `CRFPMQtdDia` | `N/D` | - |
| `CRFPMPreVda` | `N/D` | - |
| `CRFPMVlrGov` | `N/D` | - |
| `CRFPMVlrCli` | `N/D` | - |
| `CRFPMQtdCxa` | `N/D` | - |

#### 🗺️ Índices
- `CRFPM1` (Unique): `CMEmpCod`, `CMFilCod`, `CRFPCCod`, `CEProCod`
- `CRFPM2` (Duplicate): `CMEmpCod`, `CEProCod`
- `CRFPM3` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRFPCCod`

---

### 📌 CRFPP
- **Descrição:** Parâmetros da Farmácia Popular
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRFPPCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRFPPCod` | `N/D` | - |
| `CRFPPLog` | `N/D` | - |
| `CRFPPSen` | `N/D` | - |
| `CRFPPCNPJ` | `N/D` | - |
| `CRFPPPCS` | `N/D` | - |
| `CRFPPUsu` | `N/D` | - |
| `CRFPPPrg` | `N/D` | - |
| `CRFPPTST` | `N/D` | - |
| `CRFPPVer` | `N/D` | - |

#### 🗺️ Índices
- `CRFPP1` (Unique): `CMEmpCod`, `CMFilCod`, `CRFPPCod`
- `CRFPP2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CRFPV
- **Descrição:** Dados do Cupom Fiscal Vinculado da Farmácia Popular
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRFPCCod`, `CRFPVSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRFPCCod` | `N/D` | - |
| `CRFPVSeq` | `N/D` | - |
| `CRFPVObs` | `N/D` | - |

#### 🗺️ Índices
- `CRFPV1` (Unique): `CMEmpCod`, `CMFilCod`, `CRFPCCod`, `CRFPVSeq`
- `CRFPV2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRFPCCod`

---

### 📌 CRHCL1
- **Descrição:** Histórico Comercial do Cliente
- **Chave Primária:** `CMEmpCod`, `CRHCl1CliCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRHCl1CliCod` | `N/D` | - |
| `CRHCl1CliDes` | `N/D` | - |
| `CRHCl1TotAbe` | `N/D` | - |
| `CRHCl1TotFec` | `N/D` | - |
| `CRHCl1TotCan` | `N/D` | - |
| `CRHCl1_TotAtr` | `N/D` | - |
| `CRHCl1DtaMaiAtr` | `N/D` | - |
| `CRHCl1DtaUltCom` | `N/D` | - |
| `CRHCl1DtaPriCom` | `N/D` | - |
| `CRHCl1MedPgt` | `N/D` | - |
| `CRHCl1DiaMaiAtr` | `N/D` | - |
| `CRHCl1TotGerAbeFec` | `N/D` | - |
| `CRHCL1FilCod` | `N/D` | - |

#### 🗺️ Índices
- `CRHCL1A` (Unique): `CMEmpCod`, `CRHCl1CliCod`
- `CRHCL1B` (Duplicate): `CMEmpCod`, `CRHCl1CliCod`
- `CRHCL1C` (Duplicate): `CMEmpCod`, `CRHCl1CliDes`

---

### 📌 CRHCL2
- **Descrição:** Histórico Comercial do Cliente 02
- **Chave Primária:** `CMEmpCod`, `CRHCl1CliCod`, `CRHCl2AnoMes`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRHCl1CliCod` | `N/D` | - |
| `CRHCl1CliDes` | `N/D` | - |
| `CRHCl1TotAbe` | `N/D` | - |
| `CRHCl1TotFec` | `N/D` | - |
| `CRHCl1TotCan` | `N/D` | - |
| `CRHCl1_TotAtr` | `N/D` | - |
| `CRHCl1DtaMaiAtr` | `N/D` | - |
| `CRHCl1DtaUltCom` | `N/D` | - |
| `CRHCl1DtaPriCom` | `N/D` | - |
| `CRHCl1MedPgt` | `N/D` | - |
| `CRHCl1DiaMaiAtr` | `N/D` | - |
| `CRHCl1TotGerAbeFec` | `N/D` | - |
| `CRHCL1FilCod` | `N/D` | - |
| `CRHCl2AnoMes` | `N/D` | - |
| `CRHCl2_TotAbe` | `N/D` | - |
| `CRHCl2TotFec` | `N/D` | - |
| `CRHCl2TotCan` | `N/D` | - |
| `CRHCl2TotAtr` | `N/D` | - |

#### 🗺️ Índices
- `CRHCL2A` (Unique): `CMEmpCod`, `CRHCl1CliCod`, `CRHCl2AnoMes`
- `CRHCL2B` (Duplicate): `CMEmpCod`, `CRHCl1CliCod`

---

### 📌 CRHRB
- **Descrição:** Histórico Retorno de Boletos
- **Chave Primária:** `CRHRBCod`, `CRHRBBco`, `CRHRBAge`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CRHRBCod` | `N/D` | - |
| `CRHRBBco` | `N/D` | - |
| `CRHRBAge` | `N/D` | - |
| `CRHRBVlr` | `N/D` | - |
| `CRHRBTstImp` | `N/D` | - |
| `CRHRBSts` | `N/D` | - |
| `CRHRBDTV` | `N/D` | - |
| `CRHRBDTP` | `N/D` | - |
| `CRHRBTBX` | `N/D` | - |
| `CRHRBQTD` | `N/D` | - |
| `CRHRBDig` | `N/D` | - |
| `CRHRBUsuImp` | `N/D` | - |
| `CRHRBTxt` | `N/D` | - |
| `CRHRBTxt1` | `N/D` | - |
| `CRHRBTxt2` | `N/D` | - |
| `CRHRBNomArq` | `N/D` | - |
| `CRHRBJrs` | `N/D` | - |
| `CRHRBTar` | `N/D` | - |
| `CRHRBMul` | `N/D` | - |
| `CRHRBCli` | `N/D` | - |

#### 🗺️ Índices
- `CRHRB1` (Unique): `CRHRBCod`, `CRHRBBco`, `CRHRBAge`
- `CRHRB2` (Duplicate): `CRHRBDTP`
- `CRHRB3` (Duplicate): `CRHRBTstImp`

---

### 📌 CRHVC
- **Descrição:** Histórico Cancelamento Venda e Itens
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRHVCTST`, `CRHVCCHEOUT`, `CRHVCUSU`, `CRHVCProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRHVCTST` | `N/D` | - |
| `CRHVCCHEOUT` | `N/D` | - |
| `CRHVCUSU` | `N/D` | - |
| `CRHVCProCod` | `N/D` | - |
| `CRHVCQtd` | `N/D` | - |
| `CRHVCDta` | `N/D` | - |
| `CRHVCVlrUnt` | `N/D` | - |
| `CRHVCVlrTot` | `N/D` | - |

#### 🗺️ Índices
- `CRHVC1` (Unique): `CMEmpCod`, `CMFilCod`, `CRHVCTST`, `CRHVCCHEOUT`, `CRHVCUSU`, `CRHVCProCod`
- `CRHVC2` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CRHVC3` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRHVCDta`, `CRHVCCHEOUT`

---

### 📌 CRIRR
- **Descrição:** Tabela Cliente x Produto Retenção Imposto de Renda
- **Chave Primária:** `CMEmpCod`, `CRIRRFilCod`, `CRIRRCliCod`, `CEProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRIRRFilCod` | `N/D` | - |
| `CRIRRCliCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CRIRRPerRet` | `N/D` | - |
| `CRIRRRetVlr` | `N/D` | - |
| `CRIRRDtaInc` | `N/D` | - |

#### 🗺️ Índices
- `CRIRRA` (Unique): `CMEmpCod`, `CRIRRFilCod`, `CRIRRCliCod`, `CEProCod`
- `CRIRRB` (Duplicate): `CMEmpCod`, `CEProCod`

---

### 📌 CRLic
- **Descrição:** TCR24A
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRLicDta`, `CRLicNroEdi`, `CRLicTip`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRLicDta` | `N/D` | - |
| `CRLicNroEdi` | `N/D` | - |
| `CRLicTip` | `N/D` | - |
| `CRLicOrg` | `N/D` | - |
| `CRLicEmp` | `N/D` | - |
| `CRLicPrzEnt` | `N/D` | - |
| `CRLicDtaEnt` | `N/D` | - |
| `CRLicPrzPag` | `N/D` | - |
| `CRLicRecPag` | `N/D` | - |
| `CRLicPagPar` | `N/D` | - |
| `CRLicVlr` | `N/D` | - |
| `CRLicVlrRec` | `N/D` | - |
| `CRLicVlrARec` | `N/D` | - |

#### 🗺️ Índices
- `CRLicA` (Unique): `CMEmpCod`, `CMFilCod`, `CRLicDta`, `CRLicNroEdi`, `CRLicTip`
- `CRLicB` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CRLMT
- **Descrição:** Lançamentos Provenientes de Microterminal
- **Chave Primária:** `CRLMTID`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CRLMTID` | `N/D` | - |
| `CRLMTCoMic` | `N/D` | - |
| `CRLMTOpe` | `N/D` | - |
| `CRLMTEmpCod` | `N/D` | - |
| `CRLMTFilCod` | `N/D` | - |
| `CRLMTProCod` | `N/D` | - |
| `CRLMTProDes` | `N/D` | - |
| `CRLMTProCus` | `N/D` | - |
| `CRLMTProVen` | `N/D` | - |
| `CRLMTQuant` | `N/D` | - |
| `CRLMTComan` | `N/D` | - |
| `CRLMTData` | `N/D` | - |
| `CRLMTHora` | `N/D` | - |
| `CRLMTStatus` | `N/D` | - |
| `CRLMTInteg` | `N/D` | - |

#### 🗺️ Índices
- `CRLMT1` (Unique): `CRLMTID`

---

### 📌 CRMov1
- **Descrição:** Sequencia Diaria das Vendas
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRMovDta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRMovDta` | `N/D` | - |
| `CRMov1AuxSeq` | `N/D` | - |
| `CRMov1DtaTrs` | `N/D` | - |
| `CRMov1FlaDel` | `N/D` | - |
| `CRMov1QP1` | `N/D` | - |
| `CRMov1QPL` | `N/D` | - |
| `CRMov1QPF` | `N/D` | - |
| `CRMov1QPD` | `N/D` | - |
| `CRMov1QPA` | `N/D` | - |
| `CRMov1HPP` | `N/D` | - |
| `CRMov1ScEnv` | `N/D` | - |

#### 🗺️ Índices
- `CRMov11` (Unique): `CMEmpCod`, `CMFilCod`, `CRMovDta`
- `CRMov12` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CRMov2
- **Descrição:** Cabecalho das vendas
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRMovDta` | `N/D` | - |
| `CRMovSeq` | `N/D` | - |
| `CMFilTMV` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CMFilPrxCodBolBco` | `N/D` | - |
| `CMFilDspBcoBol` | `N/D` | - |
| `CMEmpCRUsaCom` | `N/D` | - |
| `CMEmpUsa_CCu` | `N/D` | - |
| `CRMov2CnfMS` | `N/D` | - |
| `CRMov2Enc` | `N/D` | - |
| `CRMov2CenTip` | `N/D` | - |
| `CRMov2FiSat` | `N/D` | - |
| `CRMov2ScaQtdTen` | `N/D` | - |
| `CRMov2ScaSts` | `N/D` | - |
| `CRMov2ScaTipEnv` | `N/D` | - |
| `CRMov2ScaAplDsc` | `N/D` | - |
| `CRMov2ScaMsgErr` | `N/D` | - |
| `CRMov2VenOrg` | `N/D` | - |
| `CRMov2RPSN` | `N/D` | - |
| `CRMov2RPSS` | `N/D` | - |
| `CRMov2RPST` | `N/D` | - |
| `CRMov2RPS` | `N/D` | - |
| `CRMov2CQR2Ass` | `N/D` | - |
| `CRMov2CQR1Ass` | `N/D` | - |
| `CRMov2CQRCode` | `N/D` | - |
| `CRMov2QR2Ass` | `N/D` | - |
| `CRMov2QR1Ass` | `N/D` | - |
| `CRMov2VrAprox` | `N/D` | - |
| `CRMov2QRCode` | `N/D` | - |
| `CRMov2SitFila` | `N/D` | - |
| `CRMov2FilaSAT` | `N/D` | - |
| `CRMov2MicSAT` | `N/D` | - |
| `CRMov2SerCancSAT` | `N/D` | - |
| `CRMov2ExcSAT` | `N/D` | - |
| `CRMov2ArqCanSAT` | `N/D` | - |
| `CRMov2ChCancSAT` | `N/D` | - |
| `CRMov2ModImpFiSAT` | `N/D` | - |
| `CRMov2ArqSAT` | `N/D` | - |
| `CRMov2ExtSAT` | `N/D` | - |
| `CRMov2SerSAT` | `N/D` | - |
| `CRMov2DhCancSAT` | `N/D` | - |
| `CRMov2DhEmiSAT` | `N/D` | - |
| `CRMov2SitSAT` | `N/D` | - |
| `CRMov2ChaveSAT` | `N/D` | - |
| `CRMov2VlValPre` | `N/D` | - |
| `CRMov2DspExt` | `N/D` | - |
| `CRMov2TrcOrg` | `N/D` | - |
| `CRMov2OrcDtaHor` | `N/D` | - |
| `CRMov2VDV` | `N/D` | - |
| `CRMov2X` | `N/D` | - |
| `CRMov2BcoDes` | `N/D` | - |
| `CRMov2BcoCod` | `N/D` | - |
| `CRMov2VlrRes` | `N/D` | - |
| `CRMov2CCV` | `N/D` | - |
| `CRMov2ChaCod` | `N/D` | - |
| `CRMov2TMVCod` | `N/D` | - |
| `CRMov2ImpNotPro` | `N/D` | - |
| `CRMov2ComVda` | `N/D` | - |
| `CRMov2MedPgtPar` | `N/D` | - |
| `CRCliTipBol` | `N/D` | - |
| `CRMov2Mrg` | `N/D` | - |
| `CRMov2CV2` | `N/D` | - |
| `CRMov2CV1` | `N/D` | - |
| `CRMov2Per_ComFix` | `N/D` | - |
| `CRMov2VlComFixVen` | `N/D` | - |
| `CRMov2ResOutVda` | `N/D` | - |
| `CRMov2Com` | `N/D` | - |
| `CRMov2ConVlrAbe` | `N/D` | - |
| `CRMov2TipCod` | `N/D` | - |
| `CRMov2DtaEnvCon` | `N/D` | - |
| `CRMov2CotSeq` | `N/D` | - |
| `CRMov2CotDtaHorLct` | `N/D` | - |
| `CRMov2DspVia` | `N/D` | - |
| `CRMov2VlrEntPag` | `N/D` | - |
| `CRMov2VlrTrc` | `N/D` | - |
| `CRMov2CheOut` | `N/D` | - |
| `CRMov2VlrVdaLiq` | `N/D` | - |
| `CRMov2VlrUsaCre` | `N/D` | - |
| `CRMov2MotCan` | `N/D` | - |
| `CRCCrCod` | `N/D` | - |
| `CRMov2LctHstCli` | `N/D` | - |
| `CRMov2PerComGer` | `N/D` | - |
| `CRMov2VlrLiqDesCom` | `N/D` | - |
| `CRMov2TotVlrDesCom` | `N/D` | - |
| `CRMov2CCuCod` | `N/D` | - |
| `CRMov2VdaCon` | `N/D` | - |
| `CRMov2ImpConFar` | `N/D` | - |
| `CRMov2CanCxa_CreCli` | `N/D` | - |
| `CRMov2SaiOutLoj` | `N/D` | - |
| `CRMov2NOpDes` | `N/D` | - |
| `CRMov2NOpCod` | `N/D` | - |
| `CRMov2FlaDel` | `N/D` | - |
| `CRMov2DtaTrs` | `N/D` | - |
| `CRMov2NroPar` | `N/D` | - |
| `CRMov2Vlr1Com` | `N/D` | - |
| `CRMov2VlrProd` | `N/D` | - |
| `CRMov2VlrDesc` | `N/D` | - |
| `CRMov2VlrAberto` | `N/D` | - |
| `CRMov2VlAcre` | `N/D` | - |
| `CRMov2PrxNroPar` | `N/D` | - |
| `CRMov2PerDesc` | `N/D` | - |
| `CRMov2PerAcre` | `N/D` | - |
| `CRMov2Obs2` | `N/D` | - |
| `CRMov2Obs1` | `N/D` | - |
| `CRMov2Flag` | `N/D` | - |
| `CRMov2DesCliFor` | `N/D` | - |
| `CRCliVlrAtuMen` | `N/D` | - |
| `CRCliDtaBolUlt` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRMov2CodCliFor` | `N/D` | - |
| `CRMov2Sit` | `N/D` | - |
| `CRMov2Obs` | `N/D` | - |
| `CRMov2DtaNf` | `N/D` | - |
| `CRMov2SerNf` | `N/D` | - |
| `CRMov2NroCoo` | `N/D` | - |
| `CRMov2CPrg` | `N/D` | - |
| `CRMov2CUsu` | `N/D` | - |
| `CRMov2CHor` | `N/D` | - |
| `CRMov2CDta` | `N/D` | - |
| `CRMov2Icm` | `N/D` | - |
| `CRMov2VlrIpi` | `N/D` | - |
| `CRMov2VlrCPr` | `N/D` | - |
| `CRMov2VlrOrg` | `N/D` | - |
| `CRTipCod` | `N/D` | - |
| `CRMov2Fil` | `N/D` | - |
| `CRMov2DtaCan` | `N/D` | - |
| `CRMov2Vend` | `N/D` | - |
| `CRMov2SenBai` | `N/D` | - |
| `CRMov2SeqAux` | `N/D` | - |
| `CMTraCod` | `N/D` | - |
| `CRMov2VTF` | `N/D` | - |
| `CRMov2VDF` | `N/D` | - |
| `CRMov2PixVlr` | `N/D` | - |
| `CRMov2DtaRen` | `N/D` | - |
| `CRMov2DirRem` | `N/D` | - |
| `CRMov2DirBol` | `N/D` | - |
| `CRMov2ExtBol` | `N/D` | - |
| `CRMov2RecBol` | `N/D` | - |
| `CRMov2ModNF` | `N/D` | - |
| `CRMov2IMKDtaMov` | `N/D` | - |
| `CRMov2IMKSeqMov` | `N/D` | - |
| `CRMov2POS` | `N/D` | - |
| `CMFilModBolBco` | `N/D` | - |
| `CMFilComVda` | `N/D` | - |
| `CMEmpCRPerAltVdaDepTrc` | `N/D` | - |
| `CMEmpJrsMorMes` | `N/D` | - |
| `CRMov2Idx` | `N/D` | - |
| `CRMov2Idx2` | `N/D` | - |
| `CRCCrPerDesVdaVis` | `N/D` | - |
| `CRMov2VlrJrsMor` | `N/D` | - |
| `CRMov2AltVdaMan` | `N/D` | - |
| `CRMov2CRMMed` | `N/D` | - |
| `CRMov2DstDup` | `N/D` | - |
| `CRMov2VAF` | `N/D` | - |
| `CRMov2DspCod` | `N/D` | - |
| `CRMov2GrpCod` | `N/D` | - |
| `CRMov2SgrCod` | `N/D` | - |
| `CRMov2DesSit` | `N/D` | - |
| `CRMov2PgtMS` | `N/D` | - |
| `CRCCr_PerDesVdaPrz` | `N/D` | - |
| `CRMov2AudVlr` | `N/D` | - |
| `CRMov2AudQtd` | `N/D` | - |
| `CRMov2AudDta` | `N/D` | - |
| `CRMov2Ven2` | `N/D` | - |
| `CRMov2CodVD` | `N/D` | - |
| `CRMov2FasCod` | `N/D` | - |
| `CRMov2Fas_Cor` | `N/D` | - |
| `CRMov2FasDes` | `N/D` | - |
| `CRMov2NroDup` | `N/D` | - |
| `CRMov2PonFid` | `N/D` | - |
| `CRMov2EntReb` | `N/D` | - |
| `CRMov2VrTImp` | `N/D` | - |
| `CRMov2VrTEst` | `N/D` | - |
| `CRMov2PerImp` | `N/D` | - |
| `CRMov2VrAImp` | `N/D` | - |
| `CRMov2ObsImp` | `N/D` | - |
| `CRMov2CB1DtaEnv` | `N/D` | - |
| `CRMov2CB2DtaRet` | `N/D` | - |
| `CRMov2CB3DtaBol` | `N/D` | - |
| `CRMov2CBSeqRem` | `N/D` | - |
| `CRMov2TstVda` | `N/D` | - |
| `CRMov2GenV100` | `N/D` | - |
| `CRMov2NroNF` | `N/D` | - |
| `CRMov2Vlr_Dev` | `N/D` | - |
| `CRMov2TtzVlrOrgJnt` | `N/D` | - |
| `CRMov2PgtCom` | `N/D` | - |
| `CRMov2Vlr3Com` | `N/D` | - |
| `CRMov2GerGrpSgr` | `N/D` | - |
| `CRMov2CmpGen1` | `N/D` | - |
| `CRMov2CliNroFra` | `N/D` | - |
| `CRMov2CRCCrDes` | `N/D` | - |
| `CRMov2_CRCCrTip` | `N/D` | - |
| `CRMov2QtdDev` | `N/D` | - |
| `CRMov2Qtd` | `N/D` | - |
| `CRMov2NFiFrt` | `N/D` | - |
| `CRMov2NFiDsp` | `N/D` | - |
| `CRMov2NFiSeg` | `N/D` | - |
| `CRMov2NFiTipFrt` | `N/D` | - |
| `CRMov2NFiEGB` | `N/D` | - |
| `CRMov2NroMic` | `N/D` | - |
| `CRMov2DtEnt` | `N/D` | - |
| `CRMov2Tab` | `N/D` | - |
| `CRMov2DesTab` | `N/D` | - |
| `CRMov2VCC` | `N/D` | - |
| `CRMov2VSE` | `N/D` | - |
| `CRMov2VEC` | `N/D` | - |
| `CRMov2SNG` | `N/D` | - |
| `CRMov2TotCusPro` | `N/D` | - |
| `CRMov2CPF` | `N/D` | - |
| `CRMov2PVC` | `N/D` | - |
| `CRMov2PVO` | `N/D` | - |
| `CRMov2PVE` | `N/D` | - |
| `CRMov2DCx` | `N/D` | - |
| `CRMov2Med` | `N/D` | - |
| `CRMov2MedTip` | `N/D` | - |
| `CRMov2Ent` | `N/D` | - |
| `CRMov2PlcVei` | `N/D` | - |
| `CRMov2MrgVda` | `N/D` | - |
| `CRMov2Mrg2Vda` | `N/D` | - |
| `CRMov2FPD` | `N/D` | - |
| `CRMov2DPrEnt` | `N/D` | - |
| `CRMov2VlLuc` | `N/D` | - |
| `CRMov2UsuEnt` | `N/D` | - |
| `CRMov2DCxCan` | `N/D` | - |
| `CRMov2SeqLctVen` | `N/D` | - |
| `CRMov2DtaIni` | `N/D` | - |
| `CRMov2DtaFin` | `N/D` | - |
| `CRMov2FPCCod` | `N/D` | - |
| `CRMov2VlAMov3` | `N/D` | - |
| `CRMov2EntBxa` | `N/D` | - |
| `CRMov2EntTST` | `N/D` | - |
| `CRMov2Txa_IDE` | `N/D` | - |
| `CRMov2TxaIND` | `N/D` | - |
| `CRMov2TxaTAC` | `N/D` | - |
| `CRMov2BAFE` | `N/D` | - |
| `CRMov2VAFE` | `N/D` | - |
| `CRMov2VAFA` | `N/D` | - |
| `CRMov2CRClrSeq` | `N/D` | - |
| `CRMov2CRCP1Cod` | `N/D` | - |
| `CRMov2UsuCon` | `N/D` | - |
| `CRMov2EntFut` | `N/D` | - |
| `CRMov2TSTCan` | `N/D` | - |
| `CRMov2Uus_Can` | `N/D` | - |
| `CRMov2V_Rat` | `N/D` | - |
| `CRMov2CCx` | `N/D` | - |
| `CRMov2MonDtaPre` | `N/D` | - |
| `CRMov2MonUsu` | `N/D` | - |
| `CRMov2MonCxa` | `N/D` | - |
| `CRMov2DifVlr` | `N/D` | - |
| `CRMov2Com2` | `N/D` | - |
| `CRMov2VAV` | `N/D` | - |
| `CRMov2Vol` | `N/D` | - |
| `CMTraRazSoc` | `N/D` | - |
| `CRMov2Pes` | `N/D` | - |
| `CRMov2DUP` | `N/D` | - |
| `CRMov2CCrPar` | `N/D` | - |
| `CRMov2VlDscLiqVda` | `N/D` | - |
| `CRMov2Dtx2Com` | `N/D` | - |
| `CRMov2Dta2Com` | `N/D` | - |
| `CRMov2Per3Com` | `N/D` | - |
| `CRMov2Vlr2Com` | `N/D` | - |
| `CMFilPrcAcrVdaPrz` | `N/D` | - |
| `CMFilUsaTabPre` | `N/D` | - |

#### 🗺️ Índices
- `CRMov22` (Unique): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`
- `CRMov2J` (Duplicate): `CMTraCod`
- `CRMov23` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMovDta`
- `CRMov2B` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRCCrCod`
- `CRMov2O` (Duplicate): `CMEmpCod`, `CRMov2CodCliFor`
- `CRMov24` (Duplicate): `CMEmpCod`, `CRMov2DtaCan`
- `CRMov25` (Duplicate): `CMEmpCod`, `CRMov2Flag`
- `CRMov26` (Duplicate): `CMEmpCod`, `CRMov2CodCliFor`, `CRMov2Flag`, `CRMovDta`
- `CRMov27` (Duplicate): `CMEmpCod`, `CRMov2DtaNf`, `CRMov2NroCoo`
- `CRMov28` (Duplicate): `CMEmpCod`, `CRMov2VdaCon`
- `CRMov29` (Duplicate): `CMEmpCod`, `CRMov2CodCliFor`, `CRMovDta`
- `CRMov2A` (Duplicate): `CMEmpCod`, `CRMovDta`, `CRMovSeq`
- `CRMov2D` (Duplicate): `CRMovDta`, `CRMov2CheOut`, `CRMovSeq`, `CMEmpCod`
- `CRMov2E` (Duplicate): `CMEmpCod`, `CRMov2DstDup`
- `CRMov2F` (Duplicate): `CRMov2ComVda`, `CRMov2CDta`, `CRMov2CHor`, `CMEmpCod`
- `CRMov2H` (Duplicate): `CRMov2Idx`, `CRMov2Idx2`
- `CRMov2I` (Duplicate): `CRMov2DCx`
- `CRMov2K` (Duplicate): `CRMov2Ent`, `CRMov2DtEnt`
- `CRMov2L` (Duplicate): `CRMov2DtaEnvCon`, `CRMov2CodCliFor`
- `CRMov2M` (Duplicate): `CRMov2DCxCan`
- `CRMov2N` (Duplicate): `CRMov2SeqLctVen`
- `CRMov2P` (Duplicate): `CRMov2FasCod`
- `CRMov2Q` (Duplicate): `CRMov2CCx`
- `CRMov2R` (Duplicate): `CRMov2MicSAT`, `CRMov2SitFila`, `CRMovDta`, `CRMovSeq`
- `CRMov2T` (Duplicate): `CRMov2NroDup`

---

### 📌 CRMov3
- **Descrição:** Parcelas das Vendas
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMov3Par`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRMovDta` | `N/D` | - |
| `CRMovSeq` | `N/D` | - |
| `CMFilModBolBco` | `N/D` | - |
| `CMFilComVda` | `N/D` | - |
| `CMEmpUsa_CCu` | `N/D` | - |
| `CMEmpCRPerAltVdaDepTrc` | `N/D` | - |
| `CMEmpJrsMorMes` | `N/D` | - |
| `CRMov2NOpCod` | `N/D` | - |
| `CRMov2NOpDes` | `N/D` | - |
| `CRMov2Vend` | `N/D` | - |
| `CRMov2Fil` | `N/D` | - |
| `CRMov2Idx` | `N/D` | - |
| `CRMov2Idx2` | `N/D` | - |
| `CRMov2VlrOrg` | `N/D` | - |
| `CRMov2VlrIpi` | `N/D` | - |
| `CRMov2Icm` | `N/D` | - |
| `CRMov2CDta` | `N/D` | - |
| `CRMov2CHor` | `N/D` | - |
| `CRMov2CUsu` | `N/D` | - |
| `CRMov2CPrg` | `N/D` | - |
| `CRMov2NroCoo` | `N/D` | - |
| `CRMov2SerNf` | `N/D` | - |
| `CRMov2DtaNf` | `N/D` | - |
| `CRMov2Obs` | `N/D` | - |
| `CRMov2Sit` | `N/D` | - |
| `CRMov2CodCliFor` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `CRMov2DesCliFor` | `N/D` | - |
| `CRMov2DtaTrs` | `N/D` | - |
| `CRMov2SaiOutLoj` | `N/D` | - |
| `CRMov2VlrAberto` | `N/D` | - |
| `CRMov2CCuCod` | `N/D` | - |
| `CRMov2NroPar` | `N/D` | - |
| `CRCCrCod` | `N/D` | - |
| `CRCCrPerDesVdaVis` | `N/D` | - |
| `CRMov2Flag` | `N/D` | - |
| `CRMov2VlrJrsMor` | `N/D` | - |
| `CRMov2VlrUsaCre` | `N/D` | - |
| `CRMov2VlrVdaLiq` | `N/D` | - |
| `CRMov2CheOut` | `N/D` | - |
| `CRMov2AltVdaMan` | `N/D` | - |
| `CRMov2CRMMed` | `N/D` | - |
| `CRMov2ComVda` | `N/D` | - |
| `CRMov2DstDup` | `N/D` | - |
| `CRMov2VlAcre` | `N/D` | - |
| `CRMov2ResOutVda` | `N/D` | - |
| `CRMov2VAF` | `N/D` | - |
| `CRMov2DspCod` | `N/D` | - |
| `CRMov2GrpCod` | `N/D` | - |
| `CRMov2SgrCod` | `N/D` | - |
| `CRMov2DesSit` | `N/D` | - |
| `CRMov2PgtMS` | `N/D` | - |
| `CRMov2Per_ComFix` | `N/D` | - |
| `CRCCr_PerDesVdaPrz` | `N/D` | - |
| `CRMov2AudVlr` | `N/D` | - |
| `CRMov2AudQtd` | `N/D` | - |
| `CRMov2AudDta` | `N/D` | - |
| `CRMov2Ven2` | `N/D` | - |
| `CRMov2CodVD` | `N/D` | - |
| `CRMov2FasCod` | `N/D` | - |
| `CRMov2Fas_Cor` | `N/D` | - |
| `CRMov2FasDes` | `N/D` | - |
| `CRMov2NroDup` | `N/D` | - |
| `CRMov2PonFid` | `N/D` | - |
| `CRMov2EntReb` | `N/D` | - |
| `CRMov2VrTImp` | `N/D` | - |
| `CRMov2VrTEst` | `N/D` | - |
| `CRMov2PerImp` | `N/D` | - |
| `CRMov2VrAImp` | `N/D` | - |
| `CRMov2ObsImp` | `N/D` | - |
| `CRMov2CB1DtaEnv` | `N/D` | - |
| `CRMov2CB2DtaRet` | `N/D` | - |
| `CRMov2CB3DtaBol` | `N/D` | - |
| `CRMov2CBSeqRem` | `N/D` | - |
| `CRMov2TstVda` | `N/D` | - |
| `CRMov2GenV100` | `N/D` | - |
| `CRMov3Par` | `N/D` | - |
| `CRMov3NDB` | `N/D` | - |
| `CRMov3DCx` | `N/D` | - |
| `CRMov3CV1` | `N/D` | - |
| `CRMov3CV2` | `N/D` | - |
| `CRMov3AudVlr` | `N/D` | - |
| `CRMov3AudDta` | `N/D` | - |
| `CRMov3AudPgt` | `N/D` | - |
| `CRMov3Vl2Com` | `N/D` | - |
| `CRMov3VlrMov5` | `N/D` | - |
| `CRMov3VDB` | `N/D` | - |
| `CRMov3VlrLiq` | `N/D` | - |
| `CRMov3VAF` | `N/D` | - |
| `CRMov3Vl_Liq` | `N/D` | - |
| `CRMov3_VlrOrgJrs` | `N/D` | - |
| `CRMov3VlrJrs` | `N/D` | - |
| `CRMov3DiaAtr` | `N/D` | - |
| `CRMov3NroDup` | `N/D` | - |
| `CRMov3DifDiaPgt` | `N/D` | - |
| `CRMov3CCx` | `N/D` | - |
| `CRMov3CCr_Div` | `N/D` | - |
| `CRMov3JrsCRMov5` | `N/D` | - |
| `CRMov3CB1DtaEnv` | `N/D` | - |
| `CRMov3CB2DtaRet` | `N/D` | - |
| `CRMov3CB3DtaBol` | `N/D` | - |
| `CRMov3CBSeqRem` | `N/D` | - |
| `CRMov3Flag` | `N/D` | - |
| `CRMov3Obs` | `N/D` | - |
| `CRMov3CDta` | `N/D` | - |
| `CRMov3CUsu` | `N/D` | - |
| `CRMov3CHor` | `N/D` | - |
| `CRMov3CPrg` | `N/D` | - |
| `CRMov3PrxCod5` | `N/D` | - |
| `CRMov3DtaTrs` | `N/D` | - |
| `CRMov3VlrCom` | `N/D` | - |
| `CRMov3FlgCCr` | `N/D` | - |
| `CRMov3VLrRecCCr` | `N/D` | - |
| `CRMov3DtaCCrPgt` | `N/D` | - |
| `CRMov3LctHstCli` | `N/D` | - |
| `CRMov3CheOut` | `N/D` | - |
| `CRMov3CodBolBco` | `N/D` | - |
| `CRMov3Vlr_ComFixVen` | `N/D` | - |
| `CRMov3CCrCod` | `N/D` | - |
| `CRMov3Idx` | `N/D` | - |
| `CRMov3VlrDspBco` | `N/D` | - |
| `CRMov3DtaEnvCon` | `N/D` | - |
| `CRMov3BxaBco` | `N/D` | - |
| `CRMov3VlrOrg` | `N/D` | - |
| `CRMov3VlAberto` | `N/D` | - |
| `CRMov3DtaVcto` | `N/D` | - |
| `CRMov3DtaPgto` | `N/D` | - |
| `CRMov3CodCliFor` | `N/D` | - |
| `CRMov3UsuCob` | `N/D` | - |
| `CRMov3BolDV` | `N/D` | - |
| `CRMov3BolAge` | `N/D` | - |
| `CRMov3BolCed` | `N/D` | - |
| `CRMov3NroFinCar` | `N/D` | - |
| `CRMov3PerCCrDes` | `N/D` | - |
| `CRMov3Dbg1` | `N/D` | - |
| `CRMov3BasNN` | `N/D` | - |
| `CRMov3PixVlr` | `N/D` | - |
| `CRMov3SeuNro` | `N/D` | - |
| `CRMov3ExtBol` | `N/D` | - |
| `CRMov3DirBol` | `N/D` | - |
| `CRMov3StsBco` | `N/D` | - |
| `CRMov3IdPgtMP` | `N/D` | - |
| `CRMov3UnPay` | `N/D` | - |
| `CRMov3IdPay` | `N/D` | - |
| `CRMov3NSU` | `N/D` | - |
| `CRMov3AutCod` | `N/D` | - |
| `CRMov3IdOrd` | `N/D` | - |
| `CRMov2NroNF` | `N/D` | - |
| `CRMov2Vlr_Dev` | `N/D` | - |
| `CRMov3Vl1Com` | `N/D` | - |
| `CRMov3RCC` | `N/D` | - |
| `CRMov3VCC` | `N/D` | - |
| `CMEmpCRUsaCom` | `N/D` | - |
| `CRMov2SenBai` | `N/D` | - |
| `CRMov2DtaCan` | `N/D` | - |
| `CRMov2VlrCPr` | `N/D` | - |
| `CRMov2Obs1` | `N/D` | - |
| `CRMov2Obs2` | `N/D` | - |
| `CRMov2PerAcre` | `N/D` | - |
| `CRMov2PerDesc` | `N/D` | - |
| `CRMov2PrxNroPar` | `N/D` | - |
| `CRMov2VlrDesc` | `N/D` | - |
| `CRMov2VlrProd` | `N/D` | - |
| `CRMov2Vlr1Com` | `N/D` | - |
| `CRMov2FlaDel` | `N/D` | - |
| `CRMov2CanCxa_CreCli` | `N/D` | - |
| `CRMov2Qtd` | `N/D` | - |
| `CRMov2NFiFrt` | `N/D` | - |
| `CRMov2NFiDsp` | `N/D` | - |
| `CRMov2NFiSeg` | `N/D` | - |
| `CRMov2NFiTipFrt` | `N/D` | - |
| `CRMov2NFiEGB` | `N/D` | - |
| `CRMov2NroMic` | `N/D` | - |
| `CRMov2DtEnt` | `N/D` | - |
| `CRMov2Tab` | `N/D` | - |
| `CRMov2DesTab` | `N/D` | - |
| `CRMov2VCC` | `N/D` | - |
| `CRMov2VSE` | `N/D` | - |
| `CRMov2VEC` | `N/D` | - |
| `CRMov2SNG` | `N/D` | - |
| `CRMov2TotCusPro` | `N/D` | - |
| `CRMov2CPF` | `N/D` | - |
| `CRMov2PVC` | `N/D` | - |
| `CRMov2PVO` | `N/D` | - |
| `CRMov2PVE` | `N/D` | - |
| `CRMov2DCx` | `N/D` | - |
| `CRMov2Med` | `N/D` | - |
| `CRMov2MedTip` | `N/D` | - |
| `CRMov2Ent` | `N/D` | - |
| `CRMov2PlcVei` | `N/D` | - |
| `CRMov2MrgVda` | `N/D` | - |
| `CRMov2Mrg2Vda` | `N/D` | - |
| `CRMov2FPD` | `N/D` | - |
| `CRMov2DPrEnt` | `N/D` | - |
| `CRMov2VlLuc` | `N/D` | - |
| `CRMov2UsuEnt` | `N/D` | - |
| `CRMov2DCxCan` | `N/D` | - |
| `CRMov2SeqLctVen` | `N/D` | - |
| `CRMov2DtaIni` | `N/D` | - |
| `CRMov2DtaFin` | `N/D` | - |
| `CRMov2FPCCod` | `N/D` | - |
| `CRMov2VlAMov3` | `N/D` | - |
| `CRMov2EntBxa` | `N/D` | - |
| `CRMov2EntTST` | `N/D` | - |
| `CRMov2Txa_IDE` | `N/D` | - |
| `CRMov2TxaIND` | `N/D` | - |
| `CRMov2TxaTAC` | `N/D` | - |
| `CRMov2BAFE` | `N/D` | - |
| `CRMov2VAFE` | `N/D` | - |
| `CRMov2VAFA` | `N/D` | - |
| `CRMov2CRClrSeq` | `N/D` | - |
| `CRMov2CRCP1Cod` | `N/D` | - |
| `CRMov2UsuCon` | `N/D` | - |
| `CRMov2EntFut` | `N/D` | - |
| `CRMov2TSTCan` | `N/D` | - |
| `CRMov2Uus_Can` | `N/D` | - |
| `CRMov2V_Rat` | `N/D` | - |
| `CRMov2CCx` | `N/D` | - |
| `CRMov2MonDtaPre` | `N/D` | - |
| `CRMov2MonUsu` | `N/D` | - |
| `CRMov2MonCxa` | `N/D` | - |
| `CRMov3DtaOrgVcto` | `N/D` | - |
| `CRMov3SenBai` | `N/D` | - |
| `CRMov3FlaDel` | `N/D` | - |
| `CRMov3ChqPre` | `N/D` | - |
| `CRMov3Sit` | `N/D` | - |
| `CRMov3KHFlag` | `N/D` | - |
| `CRMov2DifVlr` | `N/D` | - |
| `CRMov2Com2` | `N/D` | - |
| `CRCliTipBol` | `N/D` | - |
| `CRMov3SPC` | `N/D` | - |
| `CRMov3CCV` | `N/D` | - |
| `CRMov3VDC` | `N/D` | - |
| `CRMov3VAC` | `N/D` | - |
| `CRMov3VlrEntPag` | `N/D` | - |
| `CRMov3ConVlrAbe` | `N/D` | - |
| `CRMov3VlrTrc` | `N/D` | - |
| `CRMov3AuxBxaPar` | `N/D` | - |
| `CRMov3FunPer` | `N/D` | - |
| `CRMov3ChqNro` | `N/D` | - |
| `CRMov3AgeCod` | `N/D` | - |
| `CRMov3BcoCod` | `N/D` | - |
| `CRMov3VlrBol` | `N/D` | - |
| `CRMov2DUP` | `N/D` | - |
| `CRMov2CCrPar` | `N/D` | - |
| `CRMov3CCrDes` | `N/D` | - |
| `CRMov3FilPgt` | `N/D` | - |
| `CRMov3CCrPar` | `N/D` | - |
| `CRMov2VlDscLiqVda` | `N/D` | - |
| `CRMov2Dtx2Com` | `N/D` | - |
| `CRMov2Dta2Com` | `N/D` | - |
| `CRMov2Per3Com` | `N/D` | - |
| `CRMov2Vlr3Com` | `N/D` | - |
| `CRMov2Vlr2Com` | `N/D` | - |
| `CRMov2PgtCom` | `N/D` | - |
| `CRMov3Dta2Com` | `N/D` | - |

#### 🗺️ Índices
- `CRMov32` (Unique): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMov3Par`
- `CRMov33` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`
- `CRMov34` (Duplicate): `CMEmpCod`, `CRMov3CodCliFor`, `CRMov3Flag`, `CRMovDta`, `CRMovSeq`, `CRMov3Par`
- `CRMov35` (Duplicate): `CMEmpCod`, `CRMov3DtaVcto`, `CRMov3CodBolBco`
- `CRMov36` (Duplicate): `CMEmpCod`, `CRMov3Flag`, `CRMov3DtaVcto`
- `CRMov37` (Duplicate): `CMEmpCod`, `CRMov3DtaPgto`
- `CRMov38` (Duplicate): `CMEmpCod`, `CRMov3CodCliFor`, `CRMov3Flag`, `CRMov3DtaVcto`
- `CRMov31` (Duplicate): `CMEmpCod`, `CRMov3FlgCCr`, `CRMov3DtaVcto`
- `CRMov39` (Duplicate): `CRMov3CodBolBco`
- `CRMov3A` (Duplicate): `CRMov3AuxBxaPar`
- `CRMov3B` (Duplicate): `CRMov3Idx`
- `CRMov3C` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMov3Flag`, `CRMov3DtaVcto`
- `CRMov3D` (Duplicate): `CMEmpCod`, `CRMov3DtaCCrPgt`
- `CRMov3E` (Duplicate): `CRMov3DCx`
- `CRMOV3F` (Duplicate): `CRMov3DtaEnvCon`, `CRMov3CodCliFor`
- `CRmov3G` (Duplicate): `CRMov3CCx`

---

### 📌 CRMov4
- **Descrição:** Produtos da Venda
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov4Ite`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRMovDta` | `N/D` | - |
| `CRMov2CodCliFor` | `N/D` | - |
| `CRMov2QtdDev` | `N/D` | - |
| `CRMov2Com` | `N/D` | - |
| `CRMov2VlrProd` | `N/D` | - |
| `CRMovSeq` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CRMov4Ite` | `N/D` | - |
| `CRMov4Pro_Des` | `N/D` | - |
| `CRMov4ProDesCom` | `N/D` | - |
| `CRMov4VlrUntCor` | `N/D` | - |
| `CRMov4Qtd` | `N/D` | - |
| `CRMov4VlrTotCor` | `N/D` | - |
| `CRMov4CusPro` | `N/D` | - |
| `CRMov4FlaDel` | `N/D` | - |
| `CRMov4DtaTrs` | `N/D` | - |
| `CRMov4VlrAtoVda` | `N/D` | - |
| `CRMov4VlrDes` | `N/D` | - |
| `CRMov4PerDes` | `N/D` | - |
| `CRMov4TotCusPro` | `N/D` | - |
| `CRMov4PreTabAtoVda` | `N/D` | - |
| `CRMov4FilSai` | `N/D` | - |
| `CRMov4TmpCodAux` | `N/D` | - |
| `CRMov4TmpDesAux` | `N/D` | - |
| `CRMov4TmpPre1Tab` | `N/D` | - |
| `CRMov4Tmp_DifReaPre` | `N/D` | - |
| `CRMov4Tmp1Cus` | `N/D` | - |
| `CRMov4TmpReaPro` | `N/D` | - |
| `CRMov4CheOut` | `N/D` | - |
| `CRMov4ProPro` | `N/D` | - |
| `CRMov4PreVdaCli` | `N/D` | - |
| `CRMov4QtdEtq` | `N/D` | - |
| `CRMov4PrcCom` | `N/D` | - |
| `CRMov4QtdDev` | `N/D` | - |
| `CRMov4Vlr_TotDev` | `N/D` | - |
| `CRMov4Com` | `N/D` | - |
| `CRMov4SldLev_Dev` | `N/D` | - |
| `CRMov4QtdOrg` | `N/D` | - |
| `CRMov4TotPreTab` | `N/D` | - |
| `CRMov4DtaUltPreVda` | `N/D` | - |
| `CRMov4TSt` | `N/D` | - |
| `CRMov4VlrLiq` | `N/D` | - |
| `CRMov4ModTelVdaPro` | `N/D` | - |
| `CRMov4TipPre` | `N/D` | - |
| `CRMov4ProCom` | `N/D` | - |
| `CRMov4OrgCom` | `N/D` | - |
| `CRMov4VUL` | `N/D` | - |
| `CRMov4AlqPis` | `N/D` | - |
| `CRMov4BCPis` | `N/D` | - |
| `CRMov4CSTPis` | `N/D` | - |
| `CRMov4VTPis` | `N/D` | - |
| `CRMov4AlqCof` | `N/D` | - |
| `CRMov4BCCof` | `N/D` | - |
| `CRMov4CstCof` | `N/D` | - |
| `CRMov4VTCof` | `N/D` | - |
| `CRMov4BCIpi` | `N/D` | - |
| `CRMov4VTIpi` | `N/D` | - |
| `CRMov4AlqIpi` | `N/D` | - |
| `CRMov4PVU` | `N/D` | - |
| `CRMov4Dec` | `N/D` | - |
| `CRMov4NCM` | `N/D` | - |
| `CRMov4PerImp` | `N/D` | - |
| `CRMov4VrImp` | `N/D` | - |
| `CRMov4PeIE` | `N/D` | - |
| `CRMov4VrIF` | `N/D` | - |
| `CRMov4VrIE` | `N/D` | - |
| `CRMov4CFOP` | `N/D` | - |
| `CRMov4CSOSN` | `N/D` | - |
| `CRMov4AlICMS` | `N/D` | - |
| `CRMov4CSTIcms` | `N/D` | - |
| `CRMov4VDSc` | `N/D` | - |
| `CRMov4VASc` | `N/D` | - |
| `CRMov4FlSc` | `N/D` | - |
| `CRMov4UsSc` | `N/D` | - |
| `CRMov4PgSc` | `N/D` | - |
| `CRMov4TotVdaCli` | `N/D` | - |
| `CRMov4Regis` | `N/D` | - |
| `CRMov4VUF` | `N/D` | - |
| `CRMov4VTF` | `N/D` | - |
| `CRMov4VDF` | `N/D` | - |
| `CRMov4VTI` | `N/D` | - |
| `CRMov4PECDscCen` | `N/D` | - |
| `CRMov4PerAcr` | `N/D` | - |
| `CRMov4VlAcr` | `N/D` | - |
| `CRMov4DspExt` | `N/D` | - |
| `CRMov4Prc2Com` | `N/D` | - |
| `CRMov4Com2` | `N/D` | - |
| `CRMov4Org2Com` | `N/D` | - |
| `CRMov4VU2Com` | `N/D` | - |
| `CRMOV4VlrCom` | `N/D` | - |
| `CRMov4VlUsaCre` | `N/D` | - |
| `CRMov4Ven2` | `N/D` | - |
| `CRMov4Ven` | `N/D` | - |
| `CRMov4VAF` | `N/D` | - |
| `CRMov4VlDscLiqVda` | `N/D` | - |
| `CRMov4ArrTru` | `N/D` | - |
| `CRMov2DifVlr` | `N/D` | - |
| `CRMov2Com2` | `N/D` | - |
| `CRMov4Dev` | `N/D` | - |
| `CRMov4DtaEnt` | `N/D` | - |
| `CRMov4Ent` | `N/D` | - |
| `CRMov4Lot` | `N/D` | - |
| `CRMov4LotVct` | `N/D` | - |
| `CRMov4PQA` | `N/D` | - |
| `CRMov4Cor` | `N/D` | - |
| `CRMov4CorAux` | `N/D` | - |
| `CRMov4GrpCod` | `N/D` | - |
| `CRMov4SgrCod` | `N/D` | - |
| `CRMov4BasIcm` | `N/D` | - |
| `CRMov4SitTrib` | `N/D` | - |
| `CRMov4VlrICMS` | `N/D` | - |
| `CRMov4IDEPCN` | `N/D` | - |
| `CRMov4DesPCN` | `N/D` | - |
| `CRMov4Nro` | `N/D` | - |
| `CRMov4DifVlr` | `N/D` | - |
| `CRMov4PonFid` | `N/D` | - |
| `CRMov4Gar` | `N/D` | - |
| `CRMov4GarVct` | `N/D` | - |
| `CRMov4VDV` | `N/D` | - |
| `CRMov4MrgVda` | `N/D` | - |
| `CRMov4DepCod` | `N/D` | - |
| `CRMov4DepNom` | `N/D` | - |
| `CRMov4FabLot` | `N/D` | - |
| `CRMov4Enc` | `N/D` | - |
| `CRMov2EntFut` | `N/D` | - |
| `CRMov4Q_Ent` | `N/D` | - |
| `CRMov4FasCod` | `N/D` | - |
| `CRMov4FasDes` | `N/D` | - |
| `CRMov4Fas_Cor` | `N/D` | - |
| `CRMov2DesCliFor` | `N/D` | - |
| `CRMov7TotCus` | `N/D` | - |
| `CRMov7Qtd` | `N/D` | - |
| `CRMov7TotVda` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CEProPAg` | `N/D` | - |
| `CMFilPrcAcrVdaPrz` | `N/D` | - |
| `CMFilUsaTabPre` | `N/D` | - |
| `CEProPre1Tab` | `N/D` | - |

#### 🗺️ Índices
- `CRMov41` (Unique): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov4Ite`
- `CRMov42` (Duplicate): `CMEmpCod`, `CEProCod`
- `CRMov43` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`
- `CRMov44` (Duplicate): `CMEmpCod`, `CMFilCod`, `CEProCod`, `CRMovDta`
- `CRMov45` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMov4Pro_Des`
- `CRMov46` (Duplicate): `CRMov4Ent`, `CRMov4DtaEnt`
- `CRMov47` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMov4Ite`, `CEProCod`
- `CRMov48` (Duplicate): `CEProCod`, `CRMovDta`
- `CRMov49` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMov4GrpCod`, `CRMov4SgrCod`, `CRMovDta`
- `CRMov4A` (Duplicate): `CRMov4FasCod`
- `CRMov4B` (Duplicate): `CRMov4Dev`, `CRMovDta`
- `CRMov4C` (Duplicate): `CRMov4FlSc`, `CRMov4PgSc`

---

### 📌 CRMov5
- **Descrição:** Histórico de Baixas e Cheque P
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMov3Par`, `CRMov5Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRMovDta` | `N/D` | - |
| `CRMovSeq` | `N/D` | - |
| `CRMov2CodCliFor` | `N/D` | - |
| `CRMov3Par` | `N/D` | - |
| `CRMov5Cod` | `N/D` | - |
| `CRMov5Obs` | `N/D` | - |
| `CRMov2DifVlr` | `N/D` | - |
| `CRMov2Com2` | `N/D` | - |
| `CRMov5DtaMov` | `N/D` | - |
| `CRMov5DtaPgto` | `N/D` | - |
| `CRMov5VlrOrg` | `N/D` | - |
| `CRMov5VlrAcr` | `N/D` | - |
| `CRMov5VlrDes` | `N/D` | - |
| `CRMov5VlrTot` | `N/D` | - |
| `CRMov5Flag` | `N/D` | - |
| `CRMov5Bco` | `N/D` | - |
| `CRMov5Age` | `N/D` | - |
| `CRMov5VlrCre` | `N/D` | - |
| `CRMov5Chq` | `N/D` | - |
| `CRMov5TipBai` | `N/D` | - |
| `CRMov5CUsu` | `N/D` | - |
| `CRMov5CDta` | `N/D` | - |
| `CRMov5CHor` | `N/D` | - |
| `CRMov5Est` | `N/D` | - |
| `CRMov5CodEst` | `N/D` | - |
| `CRMov5CPrg` | `N/D` | - |
| `CRMov5FlaDel` | `N/D` | - |
| `CRMov5DtaTrs` | `N/D` | - |
| `CRMov5Idx` | `N/D` | - |
| `CRMov5BxaBco` | `N/D` | - |
| `CRMov5DCx` | `N/D` | - |
| `CRMov5AcrVlrDevSerCob` | `N/D` | - |
| `CRMov5BaiCRMov3` | `N/D` | - |
| `CRMov5CCV` | `N/D` | - |
| `CRMov5CheOut` | `N/D` | - |
| `CRMov5ChqDtaDes` | `N/D` | - |
| `CRMov5ChqFlgDes` | `N/D` | - |
| `CRMov5ChqJrsPag` | `N/D` | - |
| `CRMov5ChqObs` | `N/D` | - |
| `CRMov5ChqVlrRec` | `N/D` | - |
| `CRMov5CodCtaChq` | `N/D` | - |
| `CRMov5CRChACod` | `N/D` | - |
| `CRMov5CRMov6` | `N/D` | - |
| `CRMov5DesVlrDevSerCob` | `N/D` | - |
| `CRMov5DifDias` | `N/D` | - |
| `CRMov5DtaVct` | `N/D` | - |
| `CRMov5FilPgt` | `N/D` | - |
| `CRMov5LctHstCli` | `N/D` | - |
| `CRMov5ModBxa` | `N/D` | - |
| `CRMov5QtdDiaAtr` | `N/D` | - |
| `CRMov5SenBai` | `N/D` | - |
| `CRMov5Vlr_Trc` | `N/D` | - |
| `CRMov5CCx` | `N/D` | - |
| `CRMov5SPC` | `N/D` | - |
| `CRMov5VlAberto` | `N/D` | - |

#### 🗺️ Índices
- `CRMov51` (Unique): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMov3Par`, `CRMov5Cod`
- `CRMov52` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMov3Par`
- `CRMov53` (Duplicate): `CMEmpCod`, `CRMov5DtaPgto`
- `CRMov54` (Duplicate): `CMEmpCod`, `CRMov5DtaMov`
- `CRMov55` (Duplicate): `CMEmpCod`, `CRMov5Bco`, `CRMov5Chq`
- `CRMov56` (Duplicate): `CMEmpCod`, `CRMov5Idx`, `CRMov5DtaPgto`
- `CRMov57` (Duplicate): `CRMov5DCx`
- `CRMov58` (Duplicate): `CRMov5CCx`

---

### 📌 CRMov6
- **Descrição:** Resumo das Baixas Parcelas
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRMov6Seq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRMov6Seq` | `N/D` | - |
| `CRMov6Cxa` | `N/D` | - |
| `CRMov6Hor` | `N/D` | - |
| `CRMov6DtaLct` | `N/D` | - |
| `CRMov6CUsu` | `N/D` | - |
| `CRMov6DesCli` | `N/D` | - |
| `CRMov6VLrEntCxa` | `N/D` | - |
| `CRMov6VLrDes` | `N/D` | - |
| `CRMov6VlrAcr` | `N/D` | - |
| `CRMov6TotAcr` | `N/D` | - |
| `CRMov6TotComJrs` | `N/D` | - |
| `CRMov6VlrTot` | `N/D` | - |
| `CRMov6VlrRes` | `N/D` | - |
| `CRMov6Obs` | `N/D` | - |
| `CRMov6Est` | `N/D` | - |
| `CRMov6EstTst` | `N/D` | - |
| `CRMov6OrgLct` | `N/D` | - |
| `CRMov6CheOut` | `N/D` | - |
| `CRMov6Vlr_Trc` | `N/D` | - |
| `CRMov6VlEntPag` | `N/D` | - |
| `CRMov6CRChACod` | `N/D` | - |
| `CRMov6CliCod` | `N/D` | - |
| `CRMov6DtaPgt` | `N/D` | - |
| `CRMov6Sit` | `N/D` | - |
| `CRMov6CCrCod` | `N/D` | - |
| `CRMov6CCrDtaVct` | `N/D` | - |
| `CRMov6CCrPgtDta` | `N/D` | - |
| `CRMov6CCrFlg` | `N/D` | - |
| `CRMov6CCRVlrRec` | `N/D` | - |
| `CRMov6CCr_PrcDsc` | `N/D` | - |
| `CRMov6DCx` | `N/D` | - |
| `CRMov6FilPgt` | `N/D` | - |
| `CRMov6RCC` | `N/D` | - |
| `CRMov6CCx` | `N/D` | - |
| `CRMov6MovDta` | `N/D` | - |
| `CRMov6SeqVda` | `N/D` | - |
| `CRMov6ParVda` | `N/D` | - |
| `CRMov6ObsBxaCar` | `N/D` | - |
| `CRMov6TSTPOCF1` | `N/D` | - |
| `CRMov6CPrg` | `N/D` | - |
| `CRMov6TstLct` | `N/D` | - |
| `CRMov6Idx` | `N/D` | - |
| `CRMov6PerCCrDes` | `N/D` | - |
| `CRMov6PixVlr` | `N/D` | - |

#### 🗺️ Índices
- `CRMov61` (Unique): `CMEmpCod`, `CMFilCod`, `CRMov6Seq`
- `CRMov62` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CRMov63` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMov6Seq`
- `CRMov64` (Duplicate): `CMEmpCod`, `CRMov6DtaLct`
- `CRMov65` (Duplicate): `CMEmpCod`, `CRMov6CliCod`, `CRMov6DtaLct`, `CRMov6CCrCod`
- `CRMov66` (Duplicate): `CMEmpCod`, `CRMov6CCrCod`, `CRMov6CCrFlg`, `CRMov6CCrPgtDta`
- `CRMov67` (Duplicate): `CRMov6DCx`
- `CRMov68` (Duplicate): `CRMov6CCx`
- `CRMov69` (Duplicate): `CRMov6Idx`

---

### 📌 CRMov7
- **Descrição:** Número Série do Produto
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov7Item`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRMovDta` | `N/D` | - |
| `CRMovSeq` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CRMov7Item` | `N/D` | - |
| `CRMov7NroSerPro` | `N/D` | - |
| `CRMov2CodCliFor` | `N/D` | - |
| `CRMov2DesCliFor` | `N/D` | - |
| `CRMov7CheOut` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CRMov7Idx` | `N/D` | - |
| `CRMov7Obs` | `N/D` | - |
| `CRMov7QtdMon` | `N/D` | - |
| `CRMov7DP1` | `N/D` | - |
| `CRMov7DP2` | `N/D` | - |
| `CRMov7DP3` | `N/D` | - |
| `CRMov7DP5` | `N/D` | - |
| `CRMov7DP4` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CRMov7Obs2` | `N/D` | - |
| `CRMov7DtaPreMon` | `N/D` | - |
| `CRMov7Obs1` | `N/D` | - |
| `CRMov7Obs3` | `N/D` | - |
| `CRMov7DtaMon` | `N/D` | - |
| `CRMov7Obs4` | `N/D` | - |
| `CRMov7MonUsu` | `N/D` | - |
| `CRMov7MonVlr` | `N/D` | - |
| `CRMov7Mon` | `N/D` | - |

#### 🗺️ Índices
- `CRMov71` (Unique): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov7Item`
- `CRMov72` (Duplicate): `CMEmpCod`, `CEProCod`
- `CRMov73` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`
- `CRMov74` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMov7NroSerPro`
- `CRMov75` (Duplicate): `CRMov7Mon`, `CRMov7DtaPreMon`
- `CRMov76` (Duplicate): `CRMov7Mon`, `CRMov7DtaMon`
- `CRMov77` (Duplicate): `CRMov7Idx`

---

### 📌 CRmov8
- **Descrição:** Resumo das Vendas Juntadas
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMov8DtaOrg`, `CRMov8SeqOrg`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRMovDta` | `N/D` | - |
| `CRMovSeq` | `N/D` | - |
| `CRMov2CodCliFor` | `N/D` | - |
| `CRMov2TtzVlrOrgJnt` | `N/D` | - |
| `CRMov8DtaOrg` | `N/D` | - |
| `CRMov8SeqOrg` | `N/D` | - |
| `CRMov8VlrOrg` | `N/D` | - |
| `CRMov8DtaIni` | `N/D` | - |
| `CRMov8DtaFin` | `N/D` | - |
| `CRMov8NroNf` | `N/D` | - |
| `CMFilModImpFis` | `N/D` | - |
| `CRMov8UFE` | `N/D` | - |
| `CRMov8CidE` | `N/D` | - |
| `CRMov8LogE` | `N/D` | - |
| `CRMov8CEPE` | `N/D` | - |
| `CRMov8BaiE` | `N/D` | - |
| `CRMov8NroE` | `N/D` | - |
| `CRMov8EndE` | `N/D` | - |
| `CRMov8VlrLibFin` | `N/D` | - |
| `CRMov8NroConFin` | `N/D` | - |
| `CRMov8ImpCupVin` | `N/D` | - |
| `CRMov8HorSai` | `N/D` | - |
| `CRMov8DtaSai` | `N/D` | - |
| `CRMov8PrgCha` | `N/D` | - |
| `CRMov8OS10` | `N/D` | - |
| `CRMov8OSa9` | `N/D` | - |
| `CRMov8OSa8` | `N/D` | - |
| `CRMov8OSa7` | `N/D` | - |
| `CRMov8OSa6` | `N/D` | - |
| `CRMov8OSa5` | `N/D` | - |
| `CRMov8OSa4` | `N/D` | - |
| `CRMov8OSa3` | `N/D` | - |
| `CRMov8OSa2` | `N/D` | - |
| `CRMov8OSa1` | `N/D` | - |
| `CRMov8Obs9` | `N/D` | - |
| `CRMov8Obs8` | `N/D` | - |
| `CRMov8Obs7` | `N/D` | - |
| `CRMov8Obs6` | `N/D` | - |
| `CRMov8Obs5` | `N/D` | - |
| `CRMov8Obs4` | `N/D` | - |
| `CRMov8Obs3` | `N/D` | - |
| `CRMov8Obs2` | `N/D` | - |
| `CRMov8Obs1` | `N/D` | - |
| `CRMov8BcoCod` | `N/D` | - |
| `CRMov8BcoAge` | `N/D` | - |
| `CRMov8Bco_Cta` | `N/D` | - |
| `CRMov2PgtCom` | `N/D` | - |
| `CRMov2Vlr3Com` | `N/D` | - |
| `CRMov2Vlr1Com` | `N/D` | - |
| `CRMov2DesCliFor` | `N/D` | - |
| `CRMov2Idx` | `N/D` | - |
| `CRMov2Idx2` | `N/D` | - |
| `CRMov2VlrOrg` | `N/D` | - |
| `CRMov2VlrAberto` | `N/D` | - |
| `CRMov2Flag` | `N/D` | - |
| `CRMov2GerGrpSgr` | `N/D` | - |
| `CRMov2CmpGen1` | `N/D` | - |
| `CRMov2CliNroFra` | `N/D` | - |
| `CRMov2CRCCrDes` | `N/D` | - |
| `CRMov2_CRCCrTip` | `N/D` | - |
| `CRMov8VlrCom` | `N/D` | - |
| `CRMov8VctCom` | `N/D` | - |
| `CRMov8PgtCom` | `N/D` | - |
| `CRMov8StsCom` | `N/D` | - |
| `CRMov8ObsCom` | `N/D` | - |
| `CRMov2Obs` | `N/D` | - |
| `CRMov2Obs2` | `N/D` | - |
| `CRMov2Obs1` | `N/D` | - |

#### 🗺️ Índices
- `CRMov8A` (Unique): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMov8DtaOrg`, `CRMov8SeqOrg`
- `CRMov8B` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`
- `CRMov8C` (Duplicate): `CRMov8VctCom`
- `CRMov8D` (Duplicate): `CRMov8StsCom`, `CRMov8VctCom`
- `CRMov8E` (Duplicate): `CRMov8StsCom`, `CRMov8PgtCom`

---

### 📌 CRMov9
- **Descrição:** Level1
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov4Ite`, `CRMov9CodPro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRMovDta` | `N/D` | - |
| `CRMovSeq` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CRMov4Ite` | `N/D` | - |
| `CRMov2CodCliFor` | `N/D` | - |
| `CRMov2DesCliFor` | `N/D` | - |
| `CRMov4Qtd` | `N/D` | - |
| `CRMov4VlrDes` | `N/D` | - |
| `CRMov4VlrTotCor` | `N/D` | - |
| `CRMov7TotCus` | `N/D` | - |
| `CRMov7Qtd` | `N/D` | - |
| `CRMov7TotVda` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `CRMov4VlrLiq` | `N/D` | - |
| `CRMov4VlrUntCor` | `N/D` | - |
| `CEProPAg` | `N/D` | - |
| `CRMov9CodPro` | `N/D` | - |
| `CRMov9ProDes` | `N/D` | - |
| `CRMov9Cus` | `N/D` | - |
| `CRMov9TotVda` | `N/D` | - |
| `CRMov9TotCus` | `N/D` | - |
| `CRMov9Vda` | `N/D` | - |
| `CRMov9Tip` | `N/D` | - |
| `CRMov9MovEst` | `N/D` | - |
| `CRMov9Qtd` | `N/D` | - |
| `CRMov9PQA` | `N/D` | - |
| `CRMov9Obs` | `N/D` | - |

#### 🗺️ Índices
- `CRMov9A` (Unique): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov4Ite`, `CRMov9CodPro`
- `CRMov9B` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov4Ite`

---

### 📌 CRMovA
- **Descrição:** Dados Adicionais da Venda\Produto
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMovATip`, `CRMovADtaLct`, `CRMovASeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRMovDta` | `N/D` | - |
| `CRMovSeq` | `N/D` | - |
| `CRMovATip` | `N/D` | - |
| `CRMovADtaLct` | `N/D` | - |
| `CRMovASeq` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CRMov2DesCliFor` | `N/D` | - |
| `CRMov2CodCliFor` | `N/D` | - |
| `CRMovAObs1` | `N/D` | - |
| `CRMovAObs2` | `N/D` | - |
| `CRMovATST` | `N/D` | - |
| `CRMovAObs3` | `N/D` | - |
| `CRMovAObs4` | `N/D` | - |
| `CRMovAObs6` | `N/D` | - |
| `CRMovAObs5` | `N/D` | - |
| `CRMovAObs7` | `N/D` | - |
| `CRMovAObs8` | `N/D` | - |
| `CRMovAObs9` | `N/D` | - |
| `CRMovASts` | `N/D` | - |
| `CRMovAUsu2` | `N/D` | - |
| `CRMovAUsu3` | `N/D` | - |
| `CRMovAUsuAbe` | `N/D` | - |
| `CRMovAUsu1` | `N/D` | - |
| `CRMovAUsuBxa` | `N/D` | - |
| `CRMovAProDes` | `N/D` | - |
| `CRMovAVlr1` | `N/D` | - |
| `CRMovADtaBxa` | `N/D` | - |
| `CRMovADtaPrvEnt` | `N/D` | - |
| `CRMovAVlr2` | `N/D` | - |
| `CRMovAVlr5` | `N/D` | - |
| `CRMovAVlr3` | `N/D` | - |
| `CRMovADta1` | `N/D` | - |
| `CRMovADta2` | `N/D` | - |
| `CRMovAVlr4` | `N/D` | - |
| `CRMovADtaIdx` | `N/D` | - |
| `CRMovADta3` | `N/D` | - |
| `CRMovAProCod` | `N/D` | - |
| `CRMovACod` | `N/D` | - |
| `CRMovAHis` | `N/D` | - |
| `CRMovAVlr6` | `N/D` | - |
| `CRMovAVlr7` | `N/D` | - |
| `CRMovAVlr8` | `N/D` | - |
| `CRMovAVlr9` | `N/D` | - |

#### 🗺️ Índices
- `CRMovA1` (Unique): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMovATip`, `CRMovADtaLct`, `CRMovASeq`
- `CRMovA2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`
- `CRMovA3` (Duplicate): `CRMovATip`, `CRMovASts`, `CRMovADtaLct`
- `CRMovA4` (Duplicate): `CRMovAProCod`
- `CRMovA5` (Duplicate): `CRMovATip`, `CRMovASts`, `CRMovADtaIdx`
- `CRMovA6` (Duplicate): `CRMovATip`, `CRMovADtaIdx`, `CRMovASts`
- `CRMovA7` (Duplicate): `CRMovACod`

---

### 📌 CRMovE
- **Descrição:** Controle Entregas Parcial
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov4Ite`, `CRMovESeq`, `CRMovEDta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRMovDta` | `N/D` | - |
| `CRMovSeq` | `N/D` | - |
| `CRMov2CodCliFor` | `N/D` | - |
| `CRMov2DesCliFor` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CRMov4Ite` | `N/D` | - |
| `CRMov4Pro_Des` | `N/D` | - |
| `CRMov4Qtd` | `N/D` | - |
| `CRMov4Q_Ent` | `N/D` | - |
| `CRMovESeq` | `N/D` | - |
| `CRMovEDta` | `N/D` | - |
| `CRMovEFasLen` | `N/D` | - |
| `CRMovEFasDst` | `N/D` | - |
| `CRMovEFasOrg` | `N/D` | - |
| `CRMovEUltLctDia` | `N/D` | - |
| `CRMovEDPrEnt` | `N/D` | - |
| `CRMovEPQA` | `N/D` | - |
| `CRMovEIdx` | `N/D` | - |
| `CRMovEObs` | `N/D` | - |
| `CRMovEPrg` | `N/D` | - |
| `CRMovETST` | `N/D` | - |
| `CRMovEUsu` | `N/D` | - |
| `CRMovEQtd` | `N/D` | - |

#### 🗺️ Índices
- `ICRMovE` (Unique): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov4Ite`, `CRMovESeq`, `CRMovEDta`
- `CRMovE2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov4Ite`
- `CRMovE3` (Duplicate): `CRMovETST`
- `CRMove4` (Duplicate): `CRMovEDta`

---

### 📌 CRMovG
- **Descrição:** Tabela Genéricas das CRMovs CRMovG
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMovGChv`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRMovDta` | `N/D` | - |
| `CRMovSeq` | `N/D` | - |
| `CRMovGChv` | `N/D` | - |
| `CRMovGCon` | `N/D` | - |
| `CRMovGDta` | `N/D` | - |
| `CRMovGVlr` | `N/D` | - |
| `CRMovGNro` | `N/D` | - |
| `CRMovGCha` | `N/D` | - |
| `CRMovGPrg` | `N/D` | - |

#### 🗺️ Índices
- `CRMovGA` (Unique): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CRMovGChv`
- `CRMovGB` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`
- `CRMovGC` (Duplicate): `CMEmpCod`, `CRMovGChv`, `CRMovGCha`
- `CRMovGD` (Duplicate): `CMEmpCod`, `CRMovGChv`, `CRMovGDta`

---

### 📌 CRMovH
- **Descrição:** Histórico Movimentações Fases Óticas
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRMovHDta`, `CRMovHSeq`, `CRMovHCod`, `CRMovHDtaE`, `CRMovHSeqE`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRMovHDta` | `N/D` | - |
| `CRMovHSeq` | `N/D` | - |
| `CRMovHCod` | `N/D` | - |
| `CRMovHDtaE` | `N/D` | - |
| `CRMovHSeqE` | `N/D` | - |
| `CRMovHQtd` | `N/D` | - |
| `CRMovHUsu` | `N/D` | - |
| `CRMovHTST` | `N/D` | - |
| `CRMovHPrg` | `N/D` | - |
| `CRMovHObs` | `N/D` | - |
| `CRMovHIdx` | `N/D` | - |
| `CRMovHUltL` | `N/D` | - |
| `CRMovHFasO` | `N/D` | - |
| `CRMovHFasD` | `N/D` | - |
| `CRMovHFasL` | `N/D` | - |

#### 🗺️ Índices
- `CRMovH1` (Unique): `CMEmpCod`, `CMFilCod`, `CRMovHDta`, `CRMovHSeq`, `CRMovHCod`, `CRMovHDtaE`, `CRMovHSeqE`
- `CRMovH2` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CRMovH3` (Duplicate): `CRMovHTST`
- `CRMovH4` (Duplicate): `CRMovHDtaE`

---

### 📌 CRMovR
- **Descrição:** Level1
- **Chave Primária:** `CRMovTCtr`, `CRMovRTipo`, `CRMovRSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CRMovTCtr` | `N/D` | - |
| `CRMovTEmp` | `N/D` | - |
| `CRMovTFil` | `N/D` | - |
| `CRMovTData` | `N/D` | - |
| `CRMovTSeq` | `N/D` | - |
| `CRMovTTrn` | `N/D` | - |
| `CRMovTSit` | `N/D` | - |
| `CRMovTValor` | `N/D` | - |
| `CRMovTNumDoc` | `N/D` | - |
| `CRMovTDtHr` | `N/D` | - |
| `CRMovTRede` | `N/D` | - |
| `CRMovTOperacao` | `N/D` | - |
| `CRMovTCartao` | `N/D` | - |
| `CRMovTParc` | `N/D` | - |
| `CRMovTDtCp` | `N/D` | - |
| `CRMovTHrCp` | `N/D` | - |
| `CRMovTAuCp` | `N/D` | - |
| `CRMovTNSU` | `N/D` | - |
| `CRMovTCCtr` | `N/D` | - |
| `CRMovTConf` | `N/D` | - |
| `CRMovTCErro` | `N/D` | - |
| `CRMovTDErro` | `N/D` | - |
| `CRMovTCert` | `N/D` | - |
| `CRMovTQtdPar` | `N/D` | - |
| `CRMovTTroco` | `N/D` | - |
| `CRMovTDesconto` | `N/D` | - |
| `CRMovTOriginal` | `N/D` | - |
| `CRMovTMomC` | `N/D` | - |
| `CRMovTSitC` | `N/D` | - |
| `CRMovTNroMic` | `N/D` | - |
| `CRMovTReqCnf` | `N/D` | - |
| `CRMovTCanCtr` | `N/D` | - |
| `CRMovRTipo` | `N/D` | - |
| `CRMovRSeq` | `N/D` | - |
| `CRMovRTexto` | `N/D` | - |

#### 🗺️ Índices
- `CRMovR1` (Unique): `CRMovTCtr`, `CRMovRTipo`, `CRMovRSeq`
- `CRMovR2` (Duplicate): `CRMovTCtr`

---

### 📌 CRMovT
- **Descrição:** Controle de Emissão de TEF
- **Chave Primária:** `CRMovTCtr`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CRMovTCtr` | `N/D` | - |
| `CRMovTEmp` | `N/D` | - |
| `CRMovTFil` | `N/D` | - |
| `CRMovTData` | `N/D` | - |
| `CRMovTSeq` | `N/D` | - |
| `CRMovTTrn` | `N/D` | - |
| `CRMovTSit` | `N/D` | - |
| `CRMovTValor` | `N/D` | - |
| `CRMovTNumDoc` | `N/D` | - |
| `CRMovTDtHr` | `N/D` | - |
| `CRMovTRede` | `N/D` | - |
| `CRMovTOperacao` | `N/D` | - |
| `CRMovTCartao` | `N/D` | - |
| `CRMovTParc` | `N/D` | - |
| `CRMovTDtCp` | `N/D` | - |
| `CRMovTHrCp` | `N/D` | - |
| `CRMovTAuCp` | `N/D` | - |
| `CRMovTNSU` | `N/D` | - |
| `CRMovTCCtr` | `N/D` | - |
| `CRMovTConf` | `N/D` | - |
| `CRMovTCErro` | `N/D` | - |
| `CRMovTDErro` | `N/D` | - |
| `CRMovTCert` | `N/D` | - |
| `CRMovTQtdPar` | `N/D` | - |
| `CRMovTTroco` | `N/D` | - |
| `CRMovTDesconto` | `N/D` | - |
| `CRMovTOriginal` | `N/D` | - |
| `CRMovTMomC` | `N/D` | - |
| `CRMovTSitC` | `N/D` | - |
| `CRMovTNroMic` | `N/D` | - |
| `CRMovTReqCnf` | `N/D` | - |
| `CRMovTCanCtr` | `N/D` | - |

#### 🗺️ Índices
- `CRMovT1` (Unique): `CRMovTCtr`
- `CRMovT2` (Duplicate): `CRMovTCtr`
- `CRMovT3` (Duplicate): `CRMovTEmp`, `CRMovTFil`, `CRMovTData`, `CRMovTSeq`, `CRMovTCtr`
- `CRMovT4` (Duplicate): `CRMovTNroMic`, `CRMovTCtr`

---

### 📌 CROrc1
- **Descrição:** Orçamento 01
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CROrcDtaHor` | `N/D` | - |
| `CROrc1Cli` | `N/D` | - |
| `CROrc1Tel` | `N/D` | - |
| `CROrc1Set` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CROrc1CliCod` | `N/D` | - |
| `CROrc1Obs` | `N/D` | - |
| `CROrc1TotCus` | `N/D` | - |
| `CROrc1TotProDol` | `N/D` | - |
| `CROrc1Qtd` | `N/D` | - |
| `CMFIlOrc1PrcMrgLuc` | `N/D` | - |
| `CROrc1Tip` | `N/D` | - |
| `CROrc1Sts` | `N/D` | - |
| `CROrc1Eqp` | `N/D` | - |
| `CROrc1Tec` | `N/D` | - |
| `CROrc1End` | `N/D` | - |
| `CROrc1Cod` | `N/D` | - |
| `CROrc1Gar` | `N/D` | - |
| `CROrc1Ite` | `N/D` | - |
| `CROrc1Mrg1` | `N/D` | - |
| `CROrc1VlrLuc` | `N/D` | - |
| `CROrc1Cha1` | `N/D` | - |
| `CROrc1Cha2` | `N/D` | - |
| `CROrc1Cha3` | `N/D` | - |
| `CROrc1CliDes` | `N/D` | - |
| `CROrc1DtaPrvVda` | `N/D` | - |
| `CROrc1DiaPrxVda` | `N/D` | - |
| `CROrc1IndAum` | `N/D` | - |
| `CROrc1TabPre` | `N/D` | - |
| `CROrc1CotDol` | `N/D` | - |
| `CROrc1PrcMrgLuc` | `N/D` | - |
| `CROrc1Ven` | `N/D` | - |
| `CROrc1Ven2` | `N/D` | - |
| `CROrc1CM1` | `N/D` | - |
| `CMFilUsaTabPre` | `N/D` | - |
| `CMEmpDes1Tab` | `N/D` | - |
| `CMEmpDes2Tab` | `N/D` | - |
| `CMEmpDes3Tab` | `N/D` | - |
| `CMEmpDes4Tab` | `N/D` | - |
| `CMEmpDec` | `N/D` | - |
| `CROrc1TtCusOrg` | `N/D` | - |
| `CMEmpVlrMaoObr` | `N/D` | - |
| `CMFilOrc1IndAum` | `N/D` | - |
| `CROrc1DtaVda` | `N/D` | - |
| `CMFilPrcAcrVdaPrz` | `N/D` | - |
| `CROrc1TotDscPro` | `N/D` | - |
| `CROrc1Mrg2` | `N/D` | - |
| `CROrc1VlrFin` | `N/D` | - |
| `CrOrc1NF` | `N/D` | - |
| `CROrc1Plc` | `N/D` | - |
| `CROrc1Vei` | `N/D` | - |
| `CROrc1VlrMO` | `N/D` | - |
| `CROrc1DscMO` | `N/D` | - |
| `CROrc1VlrPec` | `N/D` | - |
| `CROrc1DscPec` | `N/D` | - |
| `CROrc1Val` | `N/D` | - |
| `CROrc1Rec` | `N/D` | - |
| `CROrc1Frota` | `N/D` | - |
| `CROrc1Obs1` | `N/D` | - |
| `CROrc1Obs2` | `N/D` | - |
| `CROrc1Obs3` | `N/D` | - |
| `CROrc1Obs4` | `N/D` | - |
| `CROrc1Obs5` | `N/D` | - |
| `CROrc1Obs6` | `N/D` | - |
| `CROrc1Obs7` | `N/D` | - |
| `CROrc1Obs8` | `N/D` | - |
| `CROrc1Obs9` | `N/D` | - |
| `CROrc1Tot2Cus` | `N/D` | - |
| `CROrc1KM` | `N/D` | - |
| `CEGR1Des` | `N/D` | - |
| `CEGr1Cod` | `N/D` | - |
| `CROrc1VlrCom` | `N/D` | - |
| `CROrc1TotSemDscPro` | `N/D` | - |
| `CROrc1VlrDsc` | `N/D` | - |
| `CROrc1CP1` | `N/D` | - |
| `CROrc1CP2` | `N/D` | - |
| `CROrc1CP3` | `N/D` | - |
| `CROrc1CP4` | `N/D` | - |
| `CROrc1DtaRetCli` | `N/D` | - |
| `CROrc1DtaEntPrv` | `N/D` | - |
| `CROrc1BxaKitOrc` | `N/D` | - |
| `CROrc1Pes` | `N/D` | - |
| `CROrc1GD01` | `N/D` | - |
| `CROrc1GD02` | `N/D` | - |
| `CROrc1GD03` | `N/D` | - |
| `CROrc1GD04` | `N/D` | - |
| `CROrc1GD05` | `N/D` | - |
| `CROrc1GD06` | `N/D` | - |
| `CROrc1GD07` | `N/D` | - |
| `CROrc1GD08` | `N/D` | - |
| `CROrc1GD09` | `N/D` | - |
| `CROrc1GD10` | `N/D` | - |
| `CROrc1GD11` | `N/D` | - |
| `CROrc1GD12` | `N/D` | - |
| `CROrc1GD13` | `N/D` | - |
| `CROrc1GD14` | `N/D` | - |
| `CROrc1GD15` | `N/D` | - |
| `CROrc1GD16` | `N/D` | - |
| `CROrc1GD17` | `N/D` | - |
| `CROrc1GD18` | `N/D` | - |
| `CROrc1GD19` | `N/D` | - |
| `CROrc1GD20` | `N/D` | - |
| `CROrc1GD21` | `N/D` | - |
| `CROrc1GD22` | `N/D` | - |
| `CROrc1GD23` | `N/D` | - |
| `CROrc1GD24` | `N/D` | - |
| `CROrc1GD25` | `N/D` | - |
| `CROrc1QtdPar` | `N/D` | - |
| `CROrc1Tot_DscFin` | `N/D` | - |
| `CROrc1TotGerDsc` | `N/D` | - |
| `CROrc1UsuSep` | `N/D` | - |
| `CROrc1UsuCon` | `N/D` | - |
| `CROrc1Frt` | `N/D` | - |
| `CROrc1TraCod` | `N/D` | - |
| `CROrc1TraRazSoc` | `N/D` | - |
| `CROrc1Vol` | `N/D` | - |
| `CROrc1Tra` | `N/D` | - |
| `CROrc1Bco` | `N/D` | - |
| `CROrc1Sit` | `N/D` | - |
| `CROrc1Fal` | `N/D` | - |
| `CROrc1Mot` | `N/D` | - |
| `CROrc1DtaDes` | `N/D` | - |
| `CROrc1QtdVda` | `N/D` | - |
| `CROrc1TotTabAtoVda` | `N/D` | - |
| `CROrc1Dta` | `N/D` | - |
| `CROrc1VlrAcr` | `N/D` | - |
| `CROrc1Cel` | `N/D` | - |
| `CROrc1AutCod` | `N/D` | - |
| `CROrc1AutDes` | `N/D` | - |
| `CROrc1TotAlt` | `N/D` | - |
| `CROrc1TotLar` | `N/D` | - |
| `CRORc1AreaTot` | `N/D` | - |
| `CROrc1StsSer` | `N/D` | - |
| `CROrc1StsPgt` | `N/D` | - |
| `CROrc1VlrTer` | `N/D` | - |
| `CROrc1Idx` | `N/D` | - |

#### 🗺️ Índices
- `CROrc1A` (Unique): `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`
- `CROrc1B` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CROrc1F` (Duplicate): `CMEmpCod`, `CEGr1Cod`
- `CROrc1C` (Duplicate): `CROrc1Sts`, `CROrcDtaHor`
- `CROrc1D` (Duplicate): `CROrc1Plc`, `CROrcDtaHor`
- `CROrc1E` (Duplicate): `CROrc1CM1`
- `CROrc1G` (Duplicate): `CROrc1Idx`
- `CROrc1H` (Duplicate): `CROrc1StsPgt`, `CROrc1Sts`
- `CROrc1I` (Duplicate): `CROrc1StsSer`, `CROrc1Sts`
- `CROrc1J` (Duplicate): `CROrc1Cod`
- `CROrc1K` (Duplicate): `CMEmpCod`, `CROrc1CliCod`

---

### 📌 CROrc2
- **Descrição:** Itens Orçamento
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`, `CROrc2Ite`, `CROrc2ProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CROrcDtaHor` | `N/D` | - |
| `CROrc1Cli` | `N/D` | - |
| `CROrc1Tel` | `N/D` | - |
| `CROrc1Set` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CROrc1CliCod` | `N/D` | - |
| `CROrc1Obs` | `N/D` | - |
| `CROrc1TotCus` | `N/D` | - |
| `CROrc1TotProDol` | `N/D` | - |
| `CROrc1Qtd` | `N/D` | - |
| `CMFIlOrc1PrcMrgLuc` | `N/D` | - |
| `CROrc1Tip` | `N/D` | - |
| `CROrc1Sts` | `N/D` | - |
| `CROrc1Eqp` | `N/D` | - |
| `CROrc1Tec` | `N/D` | - |
| `CROrc1End` | `N/D` | - |
| `CROrc1Cod` | `N/D` | - |
| `CROrc1Gar` | `N/D` | - |
| `CROrc1Ite` | `N/D` | - |
| `CROrc1Mrg1` | `N/D` | - |
| `CROrc1VlrLuc` | `N/D` | - |
| `CROrc1Cha1` | `N/D` | - |
| `CROrc1Cha2` | `N/D` | - |
| `CROrc1Cha3` | `N/D` | - |
| `CROrc1CliDes` | `N/D` | - |
| `CROrc1DtaPrvVda` | `N/D` | - |
| `CROrc1DiaPrxVda` | `N/D` | - |
| `CROrc1IndAum` | `N/D` | - |
| `CROrc1TabPre` | `N/D` | - |
| `CROrc1CotDol` | `N/D` | - |
| `CROrc1PrcMrgLuc` | `N/D` | - |
| `CROrc1Ven` | `N/D` | - |
| `CROrc1Ven2` | `N/D` | - |
| `CROrc1CM1` | `N/D` | - |
| `CROrc2Ite` | `N/D` | - |
| `CROrc2ProCod` | `N/D` | - |
| `CROrc2Aux` | `N/D` | - |
| `CROrc2ProDes` | `N/D` | - |
| `CROrc2Qtd` | `N/D` | - |
| `CROrc2PrcDsc` | `N/D` | - |
| `CROrc2Pro1Cus` | `N/D` | - |
| `CROrc2TotCusPro` | `N/D` | - |
| `CROrc2Pre1Tab` | `N/D` | - |
| `CROrc2TotPro` | `N/D` | - |
| `CROrc2CusOrg` | `N/D` | - |
| `CROrc2PrcMrgLuc` | `N/D` | - |
| `CROrc2OrgPre1Tab` | `N/D` | - |
| `CROrc2ProEst` | `N/D` | - |
| `CROrc2VlrDsc` | `N/D` | - |
| `CROrc2PreTabAtoVda` | `N/D` | - |
| `CROrc2DesComPro` | `N/D` | - |
| `CROrc2QtdCar` | `N/D` | - |
| `CRorc2Lar` | `N/D` | - |
| `CROrc2QG01` | `N/D` | - |
| `CROrc2Lot` | `N/D` | - |
| `CROrc2LotVct` | `N/D` | - |
| `CROrc2Tip1Tec` | `N/D` | - |
| `CROrc2EstAtu` | `N/D` | - |
| `CROrc2EstSep` | `N/D` | - |
| `CROrc2SalEst` | `N/D` | - |
| `CROrc2VlrCom` | `N/D` | - |
| `CROrc2Ref` | `N/D` | - |
| `CROrc2ProPro` | `N/D` | - |
| `CROrc2Cor` | `N/D` | - |
| `CROrc2Obs1` | `N/D` | - |
| `CROrc2Obs2` | `N/D` | - |
| `CMFilUsaTabPre` | `N/D` | - |
| `CMEmpDes1Tab` | `N/D` | - |
| `CMEmpDes2Tab` | `N/D` | - |
| `CMEmpDes3Tab` | `N/D` | - |
| `CMEmpDes4Tab` | `N/D` | - |
| `CMEmpDec` | `N/D` | - |
| `CROrc1TtCusOrg` | `N/D` | - |
| `CMEmpVlrMaoObr` | `N/D` | - |
| `CMFilOrc1IndAum` | `N/D` | - |
| `CROrc1DtaVda` | `N/D` | - |
| `CMFilPrcAcrVdaPrz` | `N/D` | - |
| `CROrc1TotDscPro` | `N/D` | - |
| `CROrc1Mrg2` | `N/D` | - |
| `CROrc1VlrFin` | `N/D` | - |
| `CrOrc1NF` | `N/D` | - |
| `CROrc2NCM` | `N/D` | - |
| `CROrc2TotDsc` | `N/D` | - |
| `CROrc2PVU` | `N/D` | - |
| `CROrc2Idx` | `N/D` | - |
| `CROrc2Sts` | `N/D` | - |
| `CROrc2Mrg1LucRea` | `N/D` | - |
| `CROrc2Mrg2LucRea` | `N/D` | - |
| `CROrc2Mrg3LucRea` | `N/D` | - |
| `CROrc2Mrg4LucRea` | `N/D` | - |
| `CROrc2Alt` | `N/D` | - |
| `CROrc2AltXLar` | `N/D` | - |
| `CROrc2Tot_CusOrg` | `N/D` | - |
| `CROrc2QtdPec` | `N/D` | - |
| `CROrc2Fas` | `N/D` | - |
| `CROrc1Plc` | `N/D` | - |
| `CROrc1Vei` | `N/D` | - |
| `CROrc1VlrMO` | `N/D` | - |
| `CROrc1DscMO` | `N/D` | - |
| `CROrc1VlrPec` | `N/D` | - |
| `CROrc1DscPec` | `N/D` | - |
| `CROrc1Val` | `N/D` | - |
| `CROrc1Rec` | `N/D` | - |
| `CROrc1Frota` | `N/D` | - |
| `CROrc1Obs1` | `N/D` | - |
| `CROrc1Obs2` | `N/D` | - |
| `CROrc1Obs3` | `N/D` | - |
| `CROrc1Obs4` | `N/D` | - |
| `CROrc1Obs5` | `N/D` | - |
| `CROrc1Obs6` | `N/D` | - |
| `CROrc1Obs7` | `N/D` | - |
| `CROrc1Obs8` | `N/D` | - |
| `CROrc1Obs9` | `N/D` | - |
| `CROrc2Ven` | `N/D` | - |
| `CROrc2PQA` | `N/D` | - |
| `CROrc2TMO` | `N/D` | - |
| `CROrc2TipLoc` | `N/D` | - |
| `CROrc1Tot2Cus` | `N/D` | - |
| `CROrc1KM` | `N/D` | - |
| `CROrc2DscCus` | `N/D` | - |
| `CROrc2Vda` | `N/D` | - |
| `CEGR1Des` | `N/D` | - |
| `CEGr1Cod` | `N/D` | - |
| `CROrc1VlrCom` | `N/D` | - |
| `CROrc1TotSemDscPro` | `N/D` | - |
| `CROrc1VlrDsc` | `N/D` | - |
| `CROrc1CP1` | `N/D` | - |
| `CROrc1CP2` | `N/D` | - |
| `CROrc1CP3` | `N/D` | - |
| `CROrc1CP4` | `N/D` | - |
| `CROrc1DtaRetCli` | `N/D` | - |
| `CROrc1DtaEntPrv` | `N/D` | - |
| `CROrc1BxaKitOrc` | `N/D` | - |
| `CROrc1Pes` | `N/D` | - |
| `CRORc2Tec` | `N/D` | - |
| `CROrc2Sil1` | `N/D` | - |
| `CRORC2Cor1` | `N/D` | - |
| `CROrc2Sil2` | `N/D` | - |
| `CRORC2Cor2` | `N/D` | - |
| `CROrc2Sil3` | `N/D` | - |
| `CRORC2Cor3` | `N/D` | - |
| `CROrc2Sil4` | `N/D` | - |
| `CRORC2Cor4` | `N/D` | - |
| `CROrc2Bor` | `N/D` | - |
| `CROrc2CorB` | `N/D` | - |
| `CROrc2ForCod` | `N/D` | - |
| `CROrc2ForDes` | `N/D` | - |
| `CROrc2PrcCom` | `N/D` | - |
| `CROrc2TipTec` | `N/D` | - |
| `CROrc2Tip2Tec` | `N/D` | - |
| `CROrc2BxaKitOrc` | `N/D` | - |
| `CROrc2IDEPCN` | `N/D` | - |
| `CROrc1GD01` | `N/D` | - |
| `CROrc1GD02` | `N/D` | - |
| `CROrc1GD03` | `N/D` | - |
| `CROrc1GD04` | `N/D` | - |
| `CROrc1GD05` | `N/D` | - |
| `CROrc1GD06` | `N/D` | - |
| `CROrc1GD07` | `N/D` | - |
| `CROrc1GD08` | `N/D` | - |
| `CROrc1GD09` | `N/D` | - |
| `CROrc1GD10` | `N/D` | - |
| `CROrc1GD11` | `N/D` | - |
| `CROrc1GD12` | `N/D` | - |
| `CROrc1GD13` | `N/D` | - |
| `CROrc1GD14` | `N/D` | - |
| `CROrc1GD15` | `N/D` | - |
| `CROrc1GD16` | `N/D` | - |
| `CROrc1GD17` | `N/D` | - |
| `CROrc1GD18` | `N/D` | - |
| `CROrc1GD19` | `N/D` | - |
| `CROrc1GD25` | `N/D` | - |
| `CROrc1GD24` | `N/D` | - |
| `CROrc1GD23` | `N/D` | - |
| `CROrc1GD22` | `N/D` | - |
| `CROrc1GD21` | `N/D` | - |
| `CROrc1GD20` | `N/D` | - |
| `CROrc2QGT` | `N/D` | - |
| `CROrc2QG25` | `N/D` | - |
| `CROrc2QG24` | `N/D` | - |
| `CROrc2QG23` | `N/D` | - |
| `CROrc2QG22` | `N/D` | - |
| `CROrc2QG21` | `N/D` | - |
| `CROrc2QG20` | `N/D` | - |
| `CROrc2QG19` | `N/D` | - |
| `CROrc2QG18` | `N/D` | - |
| `CROrc2QG17` | `N/D` | - |
| `CROrc2QG16` | `N/D` | - |
| `CROrc2QG15` | `N/D` | - |
| `CROrc2QG14` | `N/D` | - |
| `CROrc2QG13` | `N/D` | - |
| `CROrc2QG12` | `N/D` | - |
| `CROrc2QG11` | `N/D` | - |
| `CROrc2QG10` | `N/D` | - |
| `CROrc2QG09` | `N/D` | - |
| `CROrc2QG08` | `N/D` | - |
| `CROrc2QG07` | `N/D` | - |
| `CROrc2QG06` | `N/D` | - |
| `CROrc2QG05` | `N/D` | - |
| `CROrc2QG04` | `N/D` | - |
| `CROrc2QG03` | `N/D` | - |
| `CROrc2QG02` | `N/D` | - |
| `CROrc2Cus5` | `N/D` | - |
| `CROrc2Vda5` | `N/D` | - |
| `CROrc1TotTabAtoVda` | `N/D` | - |
| `CROrc1Dta` | `N/D` | - |
| `CROrc1VlrAcr` | `N/D` | - |
| `CROrc1Tot_DscFin` | `N/D` | - |
| `CROrc2TotTabAtoVda` | `N/D` | - |
| `CROrc2Ser1` | `N/D` | - |
| `CROrc2Ser2` | `N/D` | - |
| `CROrc2Ser3` | `N/D` | - |
| `CROrc2Ser4` | `N/D` | - |
| `CROrc2Ser5` | `N/D` | - |
| `CROrc2Ser6` | `N/D` | - |
| `CROrc1Cel` | `N/D` | - |
| `CROrc1AutCod` | `N/D` | - |
| `CROrc1AutDes` | `N/D` | - |
| `CROrc1Mot` | `N/D` | - |
| `CROrc1TotAlt` | `N/D` | - |
| `CROrc1TotLar` | `N/D` | - |
| `CRORc1AreaTot` | `N/D` | - |
| `CROrc2Esp` | `N/D` | - |
| `CROrc2Kit` | `N/D` | - |
| `CROrc1StsSer` | `N/D` | - |
| `CROrc1StsPgt` | `N/D` | - |
| `CROrc1VlrTer` | `N/D` | - |
| `CROrc1Idx` | `N/D` | - |
| `CROrc2MrgLucRea` | `N/D` | - |
| `CROrc2VlrTer` | `N/D` | - |
| `CROrc2VlrLuc` | `N/D` | - |

#### 🗺️ Índices
- `CRORC2A` (Unique): `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`, `CROrc2Ite`, `CROrc2ProCod`
- `CRORC2B` (Duplicate): `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`
- `CRORC2C` (Duplicate): `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`, `CROrc2ProCod`
- `CRORC2D` (Duplicate): `CROrc2Idx`
- `CRORC2E` (Duplicate): `CROrc2Sts`, `CROrc2ProCod`

---

### 📌 CROrc3
- **Descrição:** CROrc3
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`, `CROrc2Ite`, `CROrc2ProCod`, `CROrc3Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CROrcDtaHor` | `N/D` | - |
| `CROrc2Ite` | `N/D` | - |
| `CROrc2ProCod` | `N/D` | - |
| `CROrc3Cod` | `N/D` | - |
| `CROrc3DR1` | `N/D` | - |
| `CROrc3DR2` | `N/D` | - |
| `CROrc2ProDes` | `N/D` | - |
| `CROrc3DR3` | `N/D` | - |
| `CROrc3DR4` | `N/D` | - |
| `CROrc3DR5` | `N/D` | - |
| `CROrc3DC1` | `N/D` | - |
| `CROrc3DC2` | `N/D` | - |
| `CROrc3DC3` | `N/D` | - |
| `CROrc3DC4` | `N/D` | - |
| `CROrc3DC5` | `N/D` | - |
| `CROrc3NroSer` | `N/D` | - |
| `CROrc3Pat` | `N/D` | - |
| `CROrc3Mod` | `N/D` | - |
| `CROrc3Mar` | `N/D` | - |
| `CROrc3TipEqp` | `N/D` | - |
| `CROrc3IdeCon` | `N/D` | - |
| `CROrc3NFC` | `N/D` | - |
| `CROrc3DNC` | `N/D` | - |
| `CROrc3LojCom` | `N/D` | - |
| `CROrc3NroCer` | `N/D` | - |
| `CROrc3Sen` | `N/D` | - |
| `CROrc3OSExt` | `N/D` | - |
| `CROrc3Obs1` | `N/D` | - |
| `CROrc3Obs2` | `N/D` | - |
| `CROrc3Obs3` | `N/D` | - |
| `CROrc3Obs4` | `N/D` | - |
| `CROrc3Obs5` | `N/D` | - |
| `CROrc3Ace1` | `N/D` | - |
| `CROrc3Ace2` | `N/D` | - |
| `CROrc3Ace3` | `N/D` | - |
| `CROrc3Ace4` | `N/D` | - |
| `CROrc3Ace5` | `N/D` | - |
| `CROrc3NomRec` | `N/D` | - |
| `CROrc3DtaPro` | `N/D` | - |
| `CROrc3HorPro` | `N/D` | - |
| `CROrc3TipPro` | `N/D` | - |
| `CROrc3DtaEnt` | `N/D` | - |
| `CROrc3HorEnt` | `N/D` | - |
| `CROrc1Cli` | `N/D` | - |
| `CROrc3SE1` | `N/D` | - |
| `CROrc3SE2` | `N/D` | - |
| `CROrc3SE3` | `N/D` | - |
| `CROrc3SE4` | `N/D` | - |
| `CROrc3SE5` | `N/D` | - |
| `CROrc3Idx` | `N/D` | - |
| `CROrc3SE6` | `N/D` | - |
| `CROrc3SE7` | `N/D` | - |
| `CROrc3SE8` | `N/D` | - |
| `CROrc3SE9` | `N/D` | - |
| `CROrc3Txt0` | `N/D` | - |
| `CROrc3Txt1` | `N/D` | - |
| `CROrc3Txt2` | `N/D` | - |
| `CROrc3Txt3` | `N/D` | - |
| `CROrc3Txt4` | `N/D` | - |
| `CROrc3Txt5` | `N/D` | - |
| `CROrc3Txt6` | `N/D` | - |
| `CROrc3Txt7` | `N/D` | - |
| `CROrc3Txt8` | `N/D` | - |
| `CROrc3Txt9` | `N/D` | - |
| `CROrc3Cha0` | `N/D` | - |
| `CROrc3Cha1` | `N/D` | - |
| `CROrc3Cha2` | `N/D` | - |
| `CROrc3Cha3` | `N/D` | - |
| `CROrc3Cha4` | `N/D` | - |
| `CROrc3Cha5` | `N/D` | - |
| `CROrc3Cha6` | `N/D` | - |
| `CROrc3Cha7` | `N/D` | - |
| `CROrc3Cha8` | `N/D` | - |
| `CROrc3Cha9` | `N/D` | - |
| `CROrc3Nro` | `N/D` | - |

#### 🗺️ Índices
- `CROrc3A` (Unique): `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`, `CROrc2Ite`, `CROrc2ProCod`, `CROrc3Cod`
- `CROrc3B` (Duplicate): `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`, `CROrc2Ite`, `CROrc2ProCod`
- `CROrc3C` (Duplicate): `CROrc3DtaPro`
- `CROrc3D` (Duplicate): `CROrc3DtaEnt`

---

### 📌 CROrc4
- **Descrição:** Apontamentos do Orçamento
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`, `CROrc4Nom`, `CROrc4TSTLct`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CROrcDtaHor` | `N/D` | - |
| `CROrc4Nom` | `N/D` | - |
| `CROrc4TSTLct` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CROrc1Cli` | `N/D` | - |
| `CROrc1CliCod` | `N/D` | - |
| `CROrc1Obs` | `N/D` | - |
| `CROrc1Sts` | `N/D` | - |
| `CROrc1Eqp` | `N/D` | - |
| `CROrc1Tec` | `N/D` | - |
| `CROrc1Cod` | `N/D` | - |
| `CROrc1Plc` | `N/D` | - |
| `CROrc1Vei` | `N/D` | - |
| `CROrc1Rec` | `N/D` | - |
| `CROrc4TstIni` | `N/D` | - |
| `CROrc4TSTFin` | `N/D` | - |
| `CROrc4HorTra` | `N/D` | - |
| `CROrc4Obs1` | `N/D` | - |
| `CROrc4Obs3` | `N/D` | - |
| `CROrc1Tip` | `N/D` | - |
| `CROrc4Obs2` | `N/D` | - |

#### 🗺️ Índices
- `CROrc4A` (Unique): `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`, `CROrc4Nom`, `CROrc4TSTLct`
- `CROrc4B` (Duplicate): `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`

---

### 📌 CROrc5
- **Descrição:** Detalhes do Orçamento
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`, `CROrc2Ite`, `CROrc2ProCod`, `CROrc5ProKitCod`, `CROrc5Tip`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CROrcDtaHor` | `N/D` | - |
| `CROrc2Ite` | `N/D` | - |
| `CROrc2ProCod` | `N/D` | - |
| `CROrc5ProKitCod` | `N/D` | - |
| `CROrc5Tip` | `N/D` | - |
| `CROrc5Obs1` | `N/D` | - |
| `CROrc5Obs2` | `N/D` | - |
| `CROrc2ProDes` | `N/D` | - |
| `CROrc5Obs3` | `N/D` | - |
| `CROrc5Obs4` | `N/D` | - |
| `CROrc5Obs5` | `N/D` | - |
| `CROrc5Obs6` | `N/D` | - |
| `CROrc5Obs7` | `N/D` | - |
| `CROrc5Obs8` | `N/D` | - |
| `CROrc5Obs9` | `N/D` | - |
| `CROrc5PrgCha` | `N/D` | - |
| `CROrc5DtaSai` | `N/D` | - |
| `CROrc5HorSai` | `N/D` | - |
| `CROrc5Dta1` | `N/D` | - |
| `CROrc5Dta2` | `N/D` | - |
| `CROrc5Dta3` | `N/D` | - |
| `CROrc5Dta4` | `N/D` | - |
| `CROrc5Vlr1` | `N/D` | - |
| `CROrc5Vl2` | `N/D` | - |
| `CROrc5Vlr3` | `N/D` | - |
| `CROrc5Vlr4` | `N/D` | - |
| `CROrc5Vlr5` | `N/D` | - |
| `CROrc5USU` | `N/D` | - |
| `CROrc5TST` | `N/D` | - |
| `CROrc5Qtd` | `N/D` | - |
| `CROrc5SalQtd` | `N/D` | - |
| `CROrc5PQA` | `N/D` | - |
| `CROrc5CusUnt` | `N/D` | - |
| `CROrc5VdaUnt` | `N/D` | - |
| `CROrc5CusTot` | `N/D` | - |
| `CROrc5VdaTot` | `N/D` | - |
| `CROrc5KitDesPro` | `N/D` | - |
| `CROrc5Sts` | `N/D` | - |
| `CROrc2Cus5` | `N/D` | - |
| `CROrc2Vda5` | `N/D` | - |
| `CROrc5Fon` | `N/D` | - |
| `CROrc5Tam` | `N/D` | - |
| `CROrc5Neg` | `N/D` | - |
| `CROrc5GenCod` | `N/D` | - |

#### 🗺️ Índices
- `CROrc5A` (Unique): `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`, `CROrc2Ite`, `CROrc2ProCod`, `CROrc5ProKitCod`, `CROrc5Tip`
- `CROrc5B` (Duplicate): `CMEmpCod`, `CMFilCod`, `CROrcDtaHor`, `CROrc2Ite`, `CROrc2ProCod`

---

### 📌 CROrcF
- **Descrição:** Fases
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CROrcFCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CROrcFCod` | `N/D` | - |
| `CROrcFDes` | `N/D` | - |

#### 🗺️ Índices
- `CROrcF1` (Unique): `CMEmpCod`, `CMFilCod`, `CROrcFCod`
- `CROrcF2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CROrcT
- **Descrição:** Descrição do Tipo do Status do Orçamento
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CROrcTCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CROrcTCod` | `N/D` | - |
| `CROrcTDes` | `N/D` | - |
| `CROrcTExc` | `N/D` | - |
| `CROrcTDesOrg` | `N/D` | - |

#### 🗺️ Índices
- `CROrcT1` (Unique): `CMEmpCod`, `CMFilCod`, `CROrcTCod`
- `CROrcT2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CROtc
- **Descrição:** Cadastro de Ótica
- **Chave Primária:** `CMEmpCod`, `CROtcCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CROtcCod` | `N/D` | - |
| `CROtcDes` | `N/D` | - |

#### 🗺️ Índices
- `CROtc1` (Unique): `CMEmpCod`, `CROtcCod`
- `CROtc2` (Duplicate): `CMEmpCod`

---

### 📌 CRPtm2
- **Descrição:** Pedidos Temporários 02
- **Chave Primária:** `CMEmpCod`, `CRPTmCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRPTmCod` | `N/D` | - |
| `CRPTm2VlrPro` | `N/D` | - |
| `CRPtm2AuxVlrPro` | `N/D` | - |
| `CRPtm2DspVia` | `N/D` | - |
| `CRPtm2PrxItem` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CMEmpInfLimCre` | `N/D` | - |
| `CRPtm2QtdDiaPriVct` | `N/D` | - |
| `CMFilPerDscVdaPrz` | `N/D` | - |
| `CRPtm2VlrCreCli` | `N/D` | - |
| `CRPtm2VlrVdaAbe` | `N/D` | - |
| `CRPTm2Vend` | `N/D` | - |
| `CRPTm2Obs1` | `N/D` | - |
| `CRPTm2Obs2` | `N/D` | - |
| `CRPTm2VlrFinal` | `N/D` | - |
| `CRPTm2VlrDesc` | `N/D` | - |
| `CRPTm2VlrAcre` | `N/D` | - |
| `CRPTm2PerAcre` | `N/D` | - |
| `CRPTm2PerDesc` | `N/D` | - |
| `CRPTm2NroPar` | `N/D` | - |
| `CRPTm2NroNf` | `N/D` | - |
| `CRPTm2SerNf` | `N/D` | - |
| `CRPTm2DtaNf` | `N/D` | - |
| `CRPTm2Vct1Par` | `N/D` | - |
| `CRPTm2Vlr1Par` | `N/D` | - |
| `CRPTm2Nop1CodAux` | `N/D` | - |
| `CRPTm2NopCod` | `N/D` | - |
| `CMEmpCRUsaCom` | `N/D` | - |
| `CMEmpCRNroRec` | `N/D` | - |
| `CRPTm2NroRec` | `N/D` | - |
| `CRPTm2CodCli` | `N/D` | - |
| `CMEmpDesVdaVis` | `N/D` | - |
| `CRPTm2DesCli` | `N/D` | - |
| `CRPtm2CCuCod` | `N/D` | - |
| `CRPtm2CRMMed` | `N/D` | - |
| `CMEmpUsa_CCu` | `N/D` | - |
| `CMEmpUsaSenVdaBxa` | `N/D` | - |
| `CRPtm2CUsu` | `N/D` | - |
| `CRPtm2CCrCod` | `N/D` | - |
| `CRPtm2Vlr_DesCom` | `N/D` | - |
| `CRPtm2CodBco` | `N/D` | - |
| `CRPtm2NroCta` | `N/D` | - |
| `CRPtm2ChqIni` | `N/D` | - |
| `CMEmpCRArrCenVda` | `N/D` | - |
| `CMEmpCRSenVdaDscSup` | `N/D` | - |
| `CMFilPerAltVlrFinVda` | `N/D` | - |
| `CRPtm2NFiFrt` | `N/D` | - |
| `CRPtm2NFiDsp` | `N/D` | - |
| `CRptm2NFiSeg` | `N/D` | - |
| `CRPTm2NopDes` | `N/D` | - |
| `CMEmpLctVndSenVda` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CMFilAcrDiaVct` | `N/D` | - |
| `CRPtm2MedPgtPar` | `N/D` | - |
| `CRPtm2TotDiaPar` | `N/D` | - |
| `CMEmpCRVenCod` | `N/D` | - |
| `CMFilVdaPrzQtdRec` | `N/D` | - |
| `CMFilVdaVisQtdRec` | `N/D` | - |
| `CRPtm2TotQtd` | `N/D` | - |
| `CRPtm2Com` | `N/D` | - |
| `CRPtm2Des` | `N/D` | - |
| `CRMov2TotIte` | `N/D` | - |

#### 🗺️ Índices
- `CRPTm21` (Unique): `CMEmpCod`, `CRPTmCod`
- `CRPtm23` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CRPtm3
- **Descrição:** Pedidos Temporários 03
- **Chave Primária:** `CMEmpCod`, `CRPTmCod`, `CRPtm3NroPar`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRPTmCod` | `N/D` | - |
| `CRPtm2CodBco` | `N/D` | - |
| `CRPtm2NroCta` | `N/D` | - |
| `CRPtm2ChqIni` | `N/D` | - |
| `CRPtm2MedPgtPar` | `N/D` | - |
| `CRPtm2TotDiaPar` | `N/D` | - |
| `CRPTm2NroPar` | `N/D` | - |
| `CRPTm2VlrFinal` | `N/D` | - |
| `CRPtm3NroPar` | `N/D` | - |
| `CRPtm3DtaVcto` | `N/D` | - |
| `CRPtm3Vlr` | `N/D` | - |
| `CRPtm3NroBco` | `N/D` | - |
| `CRPtm3NroChq` | `N/D` | - |
| `CRPtm3MedPgtPar` | `N/D` | - |

#### 🗺️ Índices
- `CRPTm31` (Unique): `CMEmpCod`, `CRPTmCod`, `CRPtm3NroPar`
- `CRPTm32` (Duplicate): `CMEmpCod`, `CRPTmCod`

---

### 📌 CRPTM4
- **Descrição:** Pedidos Temporários 04
- **Chave Primária:** `CMEmpCod`, `CRPTmCod`, `CRPtm4IteAux`, `CEProCod`, `CRPtm4Item`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRPTmCod` | `N/D` | - |
| `CRPTm2VlrPro` | `N/D` | - |
| `CRPtm2AuxVlrPro` | `N/D` | - |
| `CRPtm2DspVia` | `N/D` | - |
| `CRPtm2PrxItem` | `N/D` | - |
| `CRPtm4IteAux` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CRPtm4Item` | `N/D` | - |
| `CRPTm4Qtd` | `N/D` | - |
| `CRPTm4VlrPro` | `N/D` | - |
| `CRPtm4MrgPro` | `N/D` | - |
| `CRPtm4CusPro` | `N/D` | - |
| `CRPtm4ProDesRes` | `N/D` | - |
| `CRPtm4Pro_Des` | `N/D` | - |
| `CRPtm4PerDes` | `N/D` | - |
| `CRPtm4VlrDes` | `N/D` | - |
| `CRPtm4Pro` | `N/D` | - |
| `CRPtm4ProCor` | `N/D` | - |
| `CRPtm4ProNro` | `N/D` | - |
| `CRPTm4VlrUnt` | `N/D` | - |
| `CRPtm4ReaPro` | `N/D` | - |
| `CRPtm4QtdCEProF` | `N/D` | - |
| `CRPtm4AceQtd` | `N/D` | - |
| `CRPtm4AcePreVda` | `N/D` | - |
| `CRPtm4FilSai` | `N/D` | - |
| `CRPtm4PreTabAtoVda` | `N/D` | - |
| `CRPtm4NroSerPro` | `N/D` | - |
| `CRPtm4PreVdaCli` | `N/D` | - |
| `CRPtm4VU2` | `N/D` | - |
| `CRPtm4PT2` | `N/D` | - |
| `CRPtm2TotQtd` | `N/D` | - |
| `CRPTm2DesCli` | `N/D` | - |
| `CRPTm2CodCli` | `N/D` | - |
| `CMEmpCRSenVdaDscSup` | `N/D` | - |
| `CRPtm4PerCom` | `N/D` | - |
| `CRPtm4QtdAux` | `N/D` | - |
| `CRPtm2Com` | `N/D` | - |
| `CRPtm2Des` | `N/D` | - |
| `CRMov2TotIte` | `N/D` | - |
| `CRPtm4Com` | `N/D` | - |
| `CRPtm4Des` | `N/D` | - |

#### 🗺️ Índices
- `CRPTM41` (Unique): `CMEmpCod`, `CRPTmCod`, `CRPtm4IteAux`, `CEProCod`, `CRPtm4Item`
- `CRPTM42` (Duplicate): `CMEmpCod`, `CEProCod`
- `CRPTM43` (Duplicate): `CMEmpCod`, `CRPTmCod`

---

### 📌 CRPVC
- **Descrição:** Produtos Última Venda Condicio
- **Chave Primária:** `CRPVCNroCxa`, `CRPVCProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CRPVCNroCxa` | `N/D` | - |
| `CRPVCProCod` | `N/D` | - |
| `CRPVCProDes` | `N/D` | - |
| `CRPVCQtd` | `N/D` | - |
| `CRPVCSts` | `N/D` | - |
| `CRPVCCliDes` | `N/D` | - |

#### 🗺️ Índices
- `CRPVC1` (Unique): `CRPVCNroCxa`, `CRPVCProCod`
- `CRPVC2` (Duplicate): `CRPVCSts`

---

### 📌 CRRBB1
- **Descrição:** Retorno Tit. B.Brasil
- **Chave Primária:** `CRRBB1Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CRRBB1Cod` | `N/D` | - |
| `CRRBB1Dig` | `N/D` | - |
| `CRRBB1Vlr` | `N/D` | - |
| `CRRBBDtaImp` | `N/D` | - |
| `CRRBBSts` | `N/D` | - |
| `CRRBB1DTV` | `N/D` | - |
| `CRRBB1DTP` | `N/D` | - |
| `CRRBB1TBX` | `N/D` | - |
| `CRRBB1QTD` | `N/D` | - |
| `CRRBB1JrsVlr` | `N/D` | - |
| `CRRBB1TarVlr` | `N/D` | - |
| `CRRBB1MulVlr` | `N/D` | - |

#### 🗺️ Índices
- `CRRBB1A` (Unique): `CRRBB1Cod`

---

### 📌 CRRCxA
- **Descrição:** Regime Caixa Anual
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRRCxAno`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRRCxAno` | `N/D` | - |
| `CRRCxAQtdPec` | `N/D` | - |
| `CRRCxAVlrTotVda` | `N/D` | - |
| `CRRCxACUsu` | `N/D` | - |
| `CRRCxACHor` | `N/D` | - |
| `CRRCxACPrg` | `N/D` | - |
| `CRRCxACDta` | `N/D` | - |
| `CRRCxADtaTrs` | `N/D` | - |
| `CRRCxAFlaDel` | `N/D` | - |
| `CRRCxAQtdMesTrb` | `N/D` | - |
| `CRRCxAMedVlrMes` | `N/D` | - |
| `CRRCxAMedQtdMes` | `N/D` | - |

#### 🗺️ Índices
- `CRRCxA1` (Unique): `CMEmpCod`, `CMFilCod`, `CRRCxAno`
- `CRRCxA2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CRRCxD
- **Descrição:** Regime Caixa Diário
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRRCxAno`, `CRRCxMes`, `CRRCxDia`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRRCxAno` | `N/D` | - |
| `CRRCxMes` | `N/D` | - |
| `CRRCxACUsu` | `N/D` | - |
| `CRRCxACHor` | `N/D` | - |
| `CRRCxACPrg` | `N/D` | - |
| `CRRCxACDta` | `N/D` | - |
| `CRRCxADtaTrs` | `N/D` | - |
| `CRRCxAFlaDel` | `N/D` | - |
| `CRRCxMQtdPec` | `N/D` | - |
| `CRRCxMVlrTotVda` | `N/D` | - |
| `CRRCxMDtaTrs` | `N/D` | - |
| `CRRCxMFlaDel` | `N/D` | - |
| `CRRCxMMesTrb` | `N/D` | - |
| `CRRCxMQtdDiaTrb` | `N/D` | - |
| `CRRCxMMedVlrDia` | `N/D` | - |
| `CRRCxMMedQtdDia` | `N/D` | - |
| `CRRCxDia` | `N/D` | - |
| `CRRCxDDta` | `N/D` | - |
| `CRRCxDQtdPec` | `N/D` | - |
| `CRRCxDVlrTotVda` | `N/D` | - |
| `CRRCxDDtaTrs` | `N/D` | - |
| `CRRCxDObs` | `N/D` | - |
| `CRRCxDDiaTrb` | `N/D` | - |
| `CRRCxDFlaDel` | `N/D` | - |

#### 🗺️ Índices
- `CRRCxD1` (Unique): `CMEmpCod`, `CMFilCod`, `CRRCxAno`, `CRRCxMes`, `CRRCxDia`
- `CRRCxD2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRRCxAno`, `CRRCxMes`

---

### 📌 CRRCxM
- **Descrição:** Regime Caixa Mensal
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRRCxAno`, `CRRCxMes`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRRCxAno` | `N/D` | - |
| `CRRCxMes` | `N/D` | - |
| `CRRCxACUsu` | `N/D` | - |
| `CRRCxACHor` | `N/D` | - |
| `CRRCxACPrg` | `N/D` | - |
| `CRRCxACDta` | `N/D` | - |
| `CRRCxADtaTrs` | `N/D` | - |
| `CRRCxAFlaDel` | `N/D` | - |
| `CRRCxMQtdPec` | `N/D` | - |
| `CRRCxMVlrTotVda` | `N/D` | - |
| `CRRCxMDtaTrs` | `N/D` | - |
| `CRRCxMFlaDel` | `N/D` | - |
| `CRRCxMMesTrb` | `N/D` | - |
| `CRRCxMQtdDiaTrb` | `N/D` | - |
| `CRRCxMMedVlrDia` | `N/D` | - |
| `CRRCxMMedQtdDia` | `N/D` | - |
| `CRRCxAQtdPec` | `N/D` | - |
| `CRRCxAVlrTotVda` | `N/D` | - |
| `CRRCxAQtdMesTrb` | `N/D` | - |
| `CRRCxAMedVlrMes` | `N/D` | - |
| `CRRCxAMedQtdMes` | `N/D` | - |

#### 🗺️ Índices
- `CRRCxM1` (Unique): `CMEmpCod`, `CMFilCod`, `CRRCxAno`, `CRRCxMes`
- `CRRCxM2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRRCxAno`
- `CRRCxM3` (Duplicate): `CMEmpCod`, `CRRCxMes`, `CRRCxAno`, `CMFilCod`

---

### 📌 CRRTo
- **Descrição:** Tabela Movimento Rede Total
- **Chave Primária:** `CRRToCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CRRToCod` | `N/D` | - |

#### 🗺️ Índices
- `CRRTo1` (Unique): `CRRToCod`

---

### 📌 CRSin01
- **Descrição:** Cadastro Registro Fiscal 60M
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRSinNroImp`, `CRSinDataM`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRSinNroImp` | `N/D` | - |
| `CRSinDataM` | `N/D` | - |
| `CRSinSeFaM` | `N/D` | - |
| `CRSinNroOrdSeq` | `N/D` | - |
| `CRSinModDocFis` | `N/D` | - |
| `CRSinCOpeIni` | `N/D` | - |
| `CRSinConOpeFin` | `N/D` | - |
| `CRSinConRedZ` | `N/D` | - |
| `CRSinReiOpe` | `N/D` | - |
| `CRSinVlrVenBru` | `N/D` | - |
| `CRSinVlrTotGer` | `N/D` | - |

#### 🗺️ Índices
- `CRSin01A` (Unique): `CMEmpCod`, `CMFilCod`, `CRSinNroImp`, `CRSinDataM`
- `CRSin01B` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CRSin02
- **Descrição:** Cadastro Registro Fiscal 60A
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRSinNroImp`, `CRSinDataA`, `CRSinASitTrib`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRSinNroImp` | `N/D` | - |
| `CRSinDataA` | `N/D` | - |
| `CRSinASitTrib` | `N/D` | - |
| `CRSinAAcuTotPar` | `N/D` | - |
| `CRSinSeFaA` | `N/D` | - |

#### 🗺️ Índices
- `CRSin02A` (Unique): `CMEmpCod`, `CMFilCod`, `CRSinNroImp`, `CRSinDataA`, `CRSinASitTrib`
- `CRSin02B` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CRSin03
- **Descrição:** Cadastro Registro Fiscal 60I
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRSinNroImp`, `CRSinDataI`, `CRSinModDI`, `CRSinNumCOO`, `CRSinNumItem`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRSinNroImp` | `N/D` | - |
| `CRSinDataI` | `N/D` | - |
| `CRSinModDI` | `N/D` | - |
| `CRSinNumCOO` | `N/D` | - |
| `CRSinNumItem` | `N/D` | - |
| `CRSinCodPro` | `N/D` | - |
| `CRSinQuant` | `N/D` | - |
| `CRSinVrLiqPro` | `N/D` | - |
| `CRSinBaseICMSPro` | `N/D` | - |
| `CRSinSitTribAliqPro` | `N/D` | - |
| `CRSinVlrICMSPro` | `N/D` | - |
| `CRSinSeFaI` | `N/D` | - |

#### 🗺️ Índices
- `CRSin03A` (Unique): `CMEmpCod`, `CMFilCod`, `CRSinNroImp`, `CRSinDataI`, `CRSinModDI`, `CRSinNumCOO`, `CRSinNumItem`
- `CRSin03B` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CRSin03C` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRSinModDI`, `CRSinNumCOO`, `CRSinNumItem`

---

### 📌 CRSin04
- **Descrição:** Cadastro Registro Fiscal 60D
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRSinNroImp`, `CRSinDataD`, `CRSinDCodPro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRSinNroImp` | `N/D` | - |
| `CRSinDataD` | `N/D` | - |
| `CRSinDCodPro` | `N/D` | - |
| `CRSinDQuant` | `N/D` | - |
| `CRSinDVlrLiq` | `N/D` | - |
| `CRSinDBasICMS` | `N/D` | - |
| `CRSinDSitTribAliq` | `N/D` | - |
| `CRSinDVlrICMS` | `N/D` | - |
| `CRSinSeFaD` | `N/D` | - |

#### 🗺️ Índices
- `CRSin04A` (Unique): `CMEmpCod`, `CMFilCod`, `CRSinNroImp`, `CRSinDataD`, `CRSinDCodPro`
- `CRSin04B` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CRSin05
- **Descrição:** Cadastro Registro Fiscal 60R
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRSinNroImp`, `CRSinDataR`, `CRSinMesAno`, `CRSinRCodPro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRSinNroImp` | `N/D` | - |
| `CRSinDataR` | `N/D` | - |
| `CRSinMesAno` | `N/D` | - |
| `CRSinRCodPro` | `N/D` | - |
| `CRSinRQuant` | `N/D` | - |
| `CRSinRVrLiq` | `N/D` | - |
| `CRSinRBaseICMS` | `N/D` | - |
| `CRSinRSitTribAliq` | `N/D` | - |
| `CRSinSeFaR` | `N/D` | - |

#### 🗺️ Índices
- `CRSin05A` (Unique): `CMEmpCod`, `CMFilCod`, `CRSinNroImp`, `CRSinDataR`, `CRSinMesAno`, `CRSinRCodPro`
- `CRSin05B` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CRSin06
- **Descrição:** Temporária - Soma COO
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRSinModDT`, `CRSinNumT`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRSinModDT` | `N/D` | - |
| `CRSinNumT` | `N/D` | - |
| `CRSinVrCTB` | `N/D` | - |
| `CRSinVrBsICMS` | `N/D` | - |

#### 🗺️ Índices
- `ICRSin06` (Unique): `CMEmpCod`, `CMFilCod`, `CRSinModDT`, `CRSinNumT`
- `ICRSin061` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CRSNG
- **Descrição:** Sistema Nacional de Gerenciamento de Produto Controlado
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov4Ite`, `CRSNGAux`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRMovDta` | `N/D` | - |
| `CRMovSeq` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CRMov4Ite` | `N/D` | - |
| `CRSNGAux` | `N/D` | - |
| `CMFilSenRT` | `N/D` | - |
| `CRMov2CodCliFor` | `N/D` | - |
| `CRMov2DesCliFor` | `N/D` | - |
| `CRMov4Pro_Des` | `N/D` | - |
| `CMProCod` | `N/D` | - |
| `CMProTip` | `N/D` | - |
| `CRSNGDTp` | `N/D` | - |
| `CMProDes` | `N/D` | - |
| `CRSNGDNr` | `N/D` | - |
| `CRSNGDOE` | `N/D` | - |
| `CRSNGDUE` | `N/D` | - |
| `CRSNGNroRec` | `N/D` | - |
| `CRSNGDtaPres` | `N/D` | - |
| `CRMov4Qtd` | `N/D` | - |
| `CRSNGRec` | `N/D` | - |
| `CRSNGLot` | `N/D` | - |
| `CEProPrf` | `N/D` | - |
| `CEProCon` | `N/D` | - |
| `CRSNGMEs` | `N/D` | - |
| `CRSNGCRT` | `N/D` | - |
| `CRSNGDesCli` | `N/D` | - |
| `CRSNGSenRT` | `N/D` | - |
| `CRSNGClaTer` | `N/D` | - |
| `CRSNGTipBasMed` | `N/D` | - |
| `CRSNGTipUsoMed` | `N/D` | - |
| `CRSNGInsUndMed` | `N/D` | - |
| `CRSNGUndFar` | `N/D` | - |
| `CRSNGMedUndMed` | `N/D` | - |
| `CRSNGPacNom` | `N/D` | - |
| `CRSNGPacIda` | `N/D` | - |
| `CRSNGPacSex` | `N/D` | - |
| `CRSNGPacUndIda` | `N/D` | - |
| `CRSNGPacCID` | `N/D` | - |
| `CMProSts` | `N/D` | - |
| `CRSNGInfLotVda` | `N/D` | - |
| `CRSNGFixCmp` | `N/D` | - |
| `CRSNGUsoPro` | `N/D` | - |

#### 🗺️ Índices
- `CRSNG1` (Unique): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov4Ite`, `CRSNGAux`
- `CRSNG2` (Duplicate): `CMProCod`, `CMProTip`
- `CRSNG3` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRMovDta`, `CRMovSeq`, `CEProCod`, `CRMov4Ite`

---

### 📌 CRTip
- **Descrição:** Tipo de Cliente
- **Chave Primária:** `CMEmpCod`, `CRTipCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRTipCod` | `N/D` | - |
| `CRTipDes` | `N/D` | - |
| `CRTipCPrg` | `N/D` | - |
| `CRTipCHor` | `N/D` | - |
| `CRTipCDta` | `N/D` | - |
| `CRTipDtaTrs` | `N/D` | - |
| `CRTipFlaDel` | `N/D` | - |
| `CRTipPerDes` | `N/D` | - |
| `CRTipPer_DesVis` | `N/D` | - |
| `CRTipPerPrzPar` | `N/D` | - |
| `CRTipTipRec` | `N/D` | - |
| `CRTipSts` | `N/D` | - |
| `CRTipDscPro` | `N/D` | - |
| `CRTipDesRes` | `N/D` | - |
| `CRTipRazSoc` | `N/D` | - |
| `CRTipCGC` | `N/D` | - |
| `CRTipIE` | `N/D` | - |
| `CRTipEnd` | `N/D` | - |
| `CRTipCid` | `N/D` | - |
| `CRTipUF` | `N/D` | - |
| `CRTipCon` | `N/D` | - |
| `CRTipTel` | `N/D` | - |
| `CRTipObs` | `N/D` | - |
| `CRTipVrCon` | `N/D` | - |
| `CRTipReCxa` | `N/D` | - |
| `CRTipVlrTo` | `N/D` | - |
| `CRTipPorPro` | `N/D` | - |
| `CRTipCUsu` | `N/D` | - |

#### 🗺️ Índices
- `CRTip1` (Unique): `CMEmpCod`, `CRTipCod`
- `CRTip2` (Duplicate): `CMEmpCod`
- `CRTip3` (Duplicate): `CMEmpCod`, `CRTipDes`

---

### 📌 CRTipH
- **Descrição:** Histório Clientes nos Convênios
- **Chave Primária:** `CMEmpCod`, `CRTipCod`, `CRTipHDta`, `CRTipHCodCli`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRTipCod` | `N/D` | - |
| `CRTipHDta` | `N/D` | - |
| `CRTipHCodCli` | `N/D` | - |
| `CRTipHSts` | `N/D` | - |
| `CRTipHVlr` | `N/D` | - |

#### 🗺️ Índices
- `CRTipH1` (Unique): `CMEmpCod`, `CRTipCod`, `CRTipHDta`, `CRTipHCodCli`
- `CRTipH2` (Duplicate): `CMEmpCod`, `CRTipCod`

---

### 📌 CRTipV
- **Descrição:** Convênio - Valores
- **Chave Primária:** `CMEmpCod`, `CRTipCod`, `CRTipVDta`, `CRTipVCodCli`, `CRTipVPar`, `CRTipVFil`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRTipCod` | `N/D` | - |
| `CRTipVDta` | `N/D` | - |
| `CRTipVCodCli` | `N/D` | - |
| `CRTipVPar` | `N/D` | - |
| `CRTipVFil` | `N/D` | - |
| `CRTipVVlr` | `N/D` | - |
| `CRTipVFlg` | `N/D` | - |
| `CRTipVDtaPgt` | `N/D` | - |
| `CRTipVDtaVct` | `N/D` | - |
| `CRTipVObs` | `N/D` | - |
| `CRTipVDtaOrg` | `N/D` | - |
| `CRTipVLctMan` | `N/D` | - |
| `CRTipDes` | `N/D` | - |
| `CRTipCPrg` | `N/D` | - |
| `CRTipCHor` | `N/D` | - |
| `CRTipCDta` | `N/D` | - |
| `CRTipDtaTrs` | `N/D` | - |
| `CRTipFlaDel` | `N/D` | - |
| `CRTipPerDes` | `N/D` | - |
| `CRTipVVlrDsc` | `N/D` | - |
| `CRTipVVlrAcr` | `N/D` | - |
| `CRTipVVlrPag` | `N/D` | - |
| `CRTipVVlrSal` | `N/D` | - |
| `CRTipVVlrOrg` | `N/D` | - |
| `CRTipVCheOut` | `N/D` | - |
| `CRTipVDifDia` | `N/D` | - |
| `CMEmpJrsMes` | `N/D` | - |
| `CRTipVDCx` | `N/D` | - |
| `CRTipVCodBolBco` | `N/D` | - |
| `CRTipVDesCli` | `N/D` | - |
| `CRTipVFilRec` | `N/D` | - |
| `CRTipVFilFec` | `N/D` | - |
| `CRTipVUsuRec` | `N/D` | - |
| `CRTipVUsuFec` | `N/D` | - |
| `CRTipVTSTRec` | `N/D` | - |
| `CRTipVTSTFec` | `N/D` | - |
| `CMEmpJrsMorMes` | `N/D` | - |
| `CRTipVDPA` | `N/D` | - |
| `CRTipVCodVD` | `N/D` | - |
| `CRTipVCPrg` | `N/D` | - |
| `CRTipVFecMov3` | `N/D` | - |
| `CRTipVNroFec` | `N/D` | - |
| `CRTipVCCx` | `N/D` | - |
| `CRTipVVlPagAtoVda` | `N/D` | - |
| `CRTipVTotPag` | `N/D` | - |

#### 🗺️ Índices
- `CRTipVA` (Unique): `CMEmpCod`, `CRTipCod`, `CRTipVDta`, `CRTipVCodCli`, `CRTipVPar`, `CRTipVFil`
- `CRTipVB` (Duplicate): `CMEmpCod`, `CRTipCod`
- `CRTipVC` (Duplicate): `CRTipVDCx`
- `CRTipVD` (Duplicate): `CRTipVDtaPgt`
- `CRTipVE` (Duplicate): `CRTipVCodBolBco`
- `CRTipVF` (Duplicate): `CMEmpCod`, `CRTipVDesCli`
- `CRTipVG` (Duplicate): `CMEmpCod`, `CRTipVCodCli`, `CRTipVDtaVct`
- `CRTipVH` (Duplicate): `CRTipVFlg`
- `CRTipVI` (Duplicate): `CMEmpCod`, `CRTipCod`, `CRTipVNroFec`
- `CRTipVJ` (Duplicate): `CRTipVCCx`

---

### 📌 CRTM1
- **Descrição:** Temporária Extrato Cliente
- **Chave Primária:** `CMEmpCod`, `CRCliCod`, `CRTm1Dta`, `CRTm1Tip`, `CRTm1SeqLct`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `CRTm1Dta` | `N/D` | - |
| `CRTm1Tip` | `N/D` | - |
| `CRTm1SeqLct` | `N/D` | - |
| `CRTm1Vlr` | `N/D` | - |
| `CRTm1Sld` | `N/D` | - |
| `CRTm1Seq` | `N/D` | - |
| `CRTm1SeqImp` | `N/D` | - |
| `CRTm1Vlr01` | `N/D` | - |
| `CRTm1Vlr02` | `N/D` | - |
| `CRTm1Vlr03` | `N/D` | - |
| `CRTm1Vlr04` | `N/D` | - |
| `CRTm1Vlr05` | `N/D` | - |
| `CRTm1Vlr06` | `N/D` | - |
| `CRTm1Cha01` | `N/D` | - |
| `CRTm1Cha02` | `N/D` | - |
| `CRTm1Cha03` | `N/D` | - |
| `CRTm1Cha04` | `N/D` | - |
| `CRTm1Cha05` | `N/D` | - |
| `CRTm1Cha06` | `N/D` | - |
| `CRTm1Tst` | `N/D` | - |

#### 🗺️ Índices
- `CRTM1A` (Unique): `CMEmpCod`, `CRCliCod`, `CRTm1Dta`, `CRTm1Tip`, `CRTm1SeqLct`
- `CRTM1B` (Duplicate): `CMEmpCod`, `CRCliCod`
- `CRTM1C` (Duplicate): `CMEmpCod`, `CRCliCod`, `CRTm1Dta`, `CRTm1SeqImp`
- `CRTM1D` (Duplicate): `CMEmpCod`, `CRCliCod`, `CRTm1SeqImp`
- `CRTM1E` (Duplicate): `CMEmpCod`, `CRCliCod`, `CRTm1Dta`, `CRTm1Tip`
- `CRTM1F` (Duplicate): `CMEmpCod`, `CRCliCod`, `CRTm1Tst`
- `CRTM1G` (Duplicate): `CMEmpCod`, `CRCliCod`, `CRTm1SeqLct`

---

### 📌 CRTM2
- **Descrição:** Temporária Recebimentos com Cartão de Crédito
- **Chave Primária:** `CRTM2Seq`, `CRTM2CheOut`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CRTM2Seq` | `N/D` | - |
| `CRTM2CheOut` | `N/D` | - |
| `CRTM2Nom` | `N/D` | - |
| `CRTM2Vlr` | `N/D` | - |
| `CRTM2DtaLct` | `N/D` | - |
| `CRTM2DtaVct` | `N/D` | - |
| `CRTM2CCRCod` | `N/D` | - |
| `CRTM2CCRDes` | `N/D` | - |
| `CRTM2VlrAcr` | `N/D` | - |
| `CRTM2VlrDsc` | `N/D` | - |

#### 🗺️ Índices
- `CRTM2A` (Unique): `CRTM2Seq`, `CRTM2CheOut`

---

### 📌 CRTMV
- **Descrição:** Tipo do Motivo da Venda
- **Chave Primária:** `CMEmpCod`, `CRTMVCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRTMVCod` | `N/D` | - |
| `CRTMVDes` | `N/D` | - |
| `CRTMVSts` | `N/D` | - |
| `CRTMVCts` | `N/D` | - |

#### 🗺️ Índices
- `CRTMV1` (Unique): `CMEmpCod`, `CRTMVCod`
- `CRTMV2` (Duplicate): `CMEmpCod`

---

### 📌 CRTrc1
- **Descrição:** Troca Mercadoria 1
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRTrc1Dta`, `CRTrc1Hor`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRTrc1Dta` | `N/D` | - |
| `CRTrc1Hor` | `N/D` | - |
| `CMEmpUsaSenVdaBxa` | `N/D` | - |
| `CMFilUsaTabPre` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CRTrc1Usu` | `N/D` | - |
| `CRTrc1CPrg` | `N/D` | - |
| `CRTrc1CDta` | `N/D` | - |
| `CMFilVdaEstNeg` | `N/D` | - |
| `CRTrc1CHor` | `N/D` | - |
| `CRTrc1CUsu` | `N/D` | - |
| `CRTrc1Obs` | `N/D` | - |
| `CRTrc1VlrFin` | `N/D` | - |
| `CRTrc1VlrOrgFin` | `N/D` | - |
| `CRTrc1EftLct` | `N/D` | - |
| `CRTrc1MovDta` | `N/D` | - |
| `CRTrc1MovSeq` | `N/D` | - |
| `CRTrc1CliCod` | `N/D` | - |
| `CRTrc1CliDes` | `N/D` | - |
| `CRTrc1Dif` | `N/D` | - |
| `CRTrc1PerAcr` | `N/D` | - |
| `CRTrc1PerDes` | `N/D` | - |
| `CRTrc1Item` | `N/D` | - |
| `CRTrc1CheOut` | `N/D` | - |
| `CRTrc1Ven` | `N/D` | - |
| `CRTrc1VdaVis` | `N/D` | - |
| `CRTrc1PerComVen` | `N/D` | - |
| `CMEmpUsa_MaiUmaFil` | `N/D` | - |
| `CRTrc1DCx` | `N/D` | - |
| `CRTrc1Mov_Sit` | `N/D` | - |
| `CRTrc1CCV` | `N/D` | - |
| `CRTrc1PrxSeqVen` | `N/D` | - |
| `CRTrc1CdxCodCli` | `N/D` | - |
| `CRTrc1CdxDesCli` | `N/D` | - |
| `CRTrc1CRDtaNov` | `N/D` | - |
| `CRTrc1CRSeqNov` | `N/D` | - |
| `CRTrc1Opr` | `N/D` | - |
| `CRTrc1Cxa` | `N/D` | - |
| `CRTrc1ComVlr` | `N/D` | - |
| `CRTrc1ProKit` | `N/D` | - |
| `CRTrc1IteKit` | `N/D` | - |
| `CRTrc1CCx` | `N/D` | - |
| `CRTrc1CliAux` | `N/D` | - |
| `CRTrc1Tst` | `N/D` | - |

#### 🗺️ Índices
- `CRTrc11` (Unique): `CMEmpCod`, `CMFilCod`, `CRTrc1Dta`, `CRTrc1Hor`
- `CRTrc12` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CRTrc13` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRTrc1Ven`, `CRTrc1Dta`
- `CRTrc14` (Duplicate): `CRTrc1DCx`
- `CRTrc15` (Duplicate): `CMEmpCod`, `CRTrc1CliCod`, `CRTrc1Dta`
- `CRTrc16` (Duplicate): `CRTrc1CRDtaNov`, `CRTrc1CRSeqNov`
- `CRTrc17` (Duplicate): `CRTrc1CCx`
- `CRTrc18` (Duplicate): `CRTrc1CliAux`

---

### 📌 CRTrc2
- **Descrição:** Troca Mercadoria 2
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CRTrc1Dta`, `CRTrc1Hor`, `CRTrc2Item`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRTrc1Dta` | `N/D` | - |
| `CRTrc1Hor` | `N/D` | - |
| `CMEmpUsaSenVdaBxa` | `N/D` | - |
| `CMFilUsaTabPre` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CRTrc1Usu` | `N/D` | - |
| `CRTrc1CPrg` | `N/D` | - |
| `CRTrc1CDta` | `N/D` | - |
| `CMFilVdaEstNeg` | `N/D` | - |
| `CRTrc1CHor` | `N/D` | - |
| `CRTrc1CUsu` | `N/D` | - |
| `CRTrc1Obs` | `N/D` | - |
| `CRTrc1VlrFin` | `N/D` | - |
| `CRTrc1VlrOrgFin` | `N/D` | - |
| `CRTrc1EftLct` | `N/D` | - |
| `CRTrc1MovDta` | `N/D` | - |
| `CRTrc1MovSeq` | `N/D` | - |
| `CRTrc1CliCod` | `N/D` | - |
| `CRTrc1CliDes` | `N/D` | - |
| `CRTrc1Dif` | `N/D` | - |
| `CRTrc1PerAcr` | `N/D` | - |
| `CRTrc1PerDes` | `N/D` | - |
| `CRTrc1Item` | `N/D` | - |
| `CRTrc1CheOut` | `N/D` | - |
| `CRTrc1Ven` | `N/D` | - |
| `CRTrc1VdaVis` | `N/D` | - |
| `CRTrc1PerComVen` | `N/D` | - |
| `CMEmpUsa_MaiUmaFil` | `N/D` | - |
| `CRTrc1DCx` | `N/D` | - |
| `CRTrc1Mov_Sit` | `N/D` | - |
| `CRTrc1CCV` | `N/D` | - |
| `CRTrc1PrxSeqVen` | `N/D` | - |
| `CRTrc1CdxCodCli` | `N/D` | - |
| `CRTrc1CdxDesCli` | `N/D` | - |
| `CRTrc1CRDtaNov` | `N/D` | - |
| `CRTrc1CRSeqNov` | `N/D` | - |
| `CRTrc1Opr` | `N/D` | - |
| `CRTrc1Cxa` | `N/D` | - |
| `CRTrc1ComVlr` | `N/D` | - |
| `CRTrc1ProKit` | `N/D` | - |
| `CRTrc1IteKit` | `N/D` | - |
| `CRTrc1CCx` | `N/D` | - |
| `CRTrc1CliAux` | `N/D` | - |
| `CRTrc1Tst` | `N/D` | - |
| `CRTrc2Item` | `N/D` | - |
| `CRTrc2CodCha` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CRTrc2EntSai` | `N/D` | - |
| `CRTrc2ProDes` | `N/D` | - |
| `CRTrc2PreTab` | `N/D` | - |
| `CRTrc2QtdOrgVda` | `N/D` | - |
| `CRTrc2Qtd` | `N/D` | - |
| `CRTrc2CusPro` | `N/D` | - |
| `CRTrc2OrgPreTab` | `N/D` | - |
| `CRTrc2VlrTot` | `N/D` | - |
| `CRTrc2VlrOrgTot` | `N/D` | - |
| `CRTrc2ProVda` | `N/D` | - |
| `CRTrc2CheOut` | `N/D` | - |
| `CRTrc2FilSai` | `N/D` | - |
| `CRTrc2Lot` | `N/D` | - |
| `CRTrc2PrcDsc` | `N/D` | - |
| `CRTrc2Cor` | `N/D` | - |
| `CRTrc2Nro` | `N/D` | - |
| `CRTrc2IDEPCN` | `N/D` | - |
| `CRTrc2DesPCN` | `N/D` | - |
| `CRTrc2TrcCus` | `N/D` | - |
| `CRTrc2TrcVda` | `N/D` | - |
| `CRTrc2ComVlr` | `N/D` | - |
| `CRTrc2ComPrc` | `N/D` | - |
| `CRTrc2ComOrg` | `N/D` | - |
| `CRTrc2ProPro` | `N/D` | - |
| `CRTrc2QtdSal` | `N/D` | - |
| `CRTrc2Ent` | `N/D` | - |
| `CRTrc2PerCal` | `N/D` | - |

#### 🗺️ Índices
- `CRTrc21` (Unique): `CMEmpCod`, `CMFilCod`, `CRTrc1Dta`, `CRTrc1Hor`, `CRTrc2Item`
- `CRTrc22` (Duplicate): `CMEmpCod`, `CEProCod`
- `CRTrc23` (Duplicate): `CMEmpCod`, `CMFilCod`, `CRTrc1Dta`, `CRTrc1Hor`

---

### 📌 CRTX1
- **Descrição:** Taxas Financeiras
- **Chave Primária:** `CMEmpCod`, `CRTX1Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRTX1Cod` | `N/D` | - |
| `CRTX1Des` | `N/D` | - |
| `CRTX1Sts` | `N/D` | - |

#### 🗺️ Índices
- `CRTX1A` (Unique): `CMEmpCod`, `CRTX1Cod`
- `CRTX1B` (Duplicate): `CMEmpCod`

---

### 📌 CRTX2
- **Descrição:** Tabela de Taxas
- **Chave Primária:** `CMEmpCod`, `CRTX1Cod`, `CRTX2Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRTX1Cod` | `N/D` | - |
| `CRTX2Cod` | `N/D` | - |
| `CRTX1Des` | `N/D` | - |
| `CRTX1Sts` | `N/D` | - |
| `CRTX2Des` | `N/D` | - |
| `CRTX2TAC` | `N/D` | - |
| `CRTX2Sts` | `N/D` | - |
| `CRTX2DiaCar` | `N/D` | - |

#### 🗺️ Índices
- `CRTX2A` (Unique): `CMEmpCod`, `CRTX1Cod`, `CRTX2Cod`
- `CRTX2B` (Duplicate): `CMEmpCod`, `CRTX1Cod`

---

### 📌 CRTX3
- **Descrição:** Tabela de Taxas
- **Chave Primária:** `CMEmpCod`, `CRTX1Cod`, `CRTX2Cod`, `CRTX3Cod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRTX1Cod` | `N/D` | - |
| `CRTX2Cod` | `N/D` | - |
| `CRTX1Des` | `N/D` | - |
| `CRTX1Sts` | `N/D` | - |
| `CRTX2Des` | `N/D` | - |
| `CRTX2TAC` | `N/D` | - |
| `CRTX2Sts` | `N/D` | - |
| `CRTX2DiaCar` | `N/D` | - |
| `CRTX3Cod` | `N/D` | - |
| `CRTX3Ind` | `N/D` | - |
| `CRTX3IDE` | `N/D` | - |
| `CRTX3QPa` | `N/D` | - |
| `CRTX3Per` | `N/D` | - |

#### 🗺️ Índices
- `CRTX3A` (Unique): `CMEmpCod`, `CRTX1Cod`, `CRTX2Cod`, `CRTX3Cod`
- `CRTX3B` (Duplicate): `CMEmpCod`, `CRTX1Cod`, `CRTX2Cod`

---

### 📌 CRVCT
- **Descrição:** Vencimentos do Cliente
- **Chave Primária:** `CMEmpCod`, `CRVCTCliCod`, `CRVctSeqLct`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRVCTCliCod` | `N/D` | - |
| `CRVctSeqLct` | `N/D` | - |
| `CRVCTVct` | `N/D` | - |
| `CRVCTMovDta` | `N/D` | - |
| `CRVCTMovSeq` | `N/D` | - |
| `CRVCTMovPar` | `N/D` | - |
| `CRVCTNroBol` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CRVCTVlrOrg` | `N/D` | - |
| `CRVCTVlrAbe` | `N/D` | - |
| `CRVCTCliDes` | `N/D` | - |
| `CRVCTTip` | `N/D` | - |

#### 🗺️ Índices
- `CRVCT1` (Unique): `CMEmpCod`, `CRVCTCliCod`, `CRVctSeqLct`
- `CRVCT2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CRVEI
- **Descrição:** Cadastro veiculos
- **Chave Primária:** `CRVeiPlc`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CRVeiPlc` | `N/D` | - |
| `CRVeiMar` | `N/D` | - |
| `CRVeiCil` | `N/D` | - |
| `CRVeiKM` | `N/D` | - |
| `CRVeiAno` | `N/D` | - |
| `CRVeiCor` | `N/D` | - |
| `CRVeiChas` | `N/D` | - |
| `CRVeiMedCom` | `N/D` | - |
| `CRVeiDes` | `N/D` | - |
| `CRVeiPro` | `N/D` | - |
| `CRVeiCPF_CNPJ` | `N/D` | - |
| `CRVeiEnd` | `N/D` | - |
| `CRVeiEndNro` | `N/D` | - |
| `CRVeiBai` | `N/D` | - |
| `CRVeiCliCod` | `N/D` | - |
| `CRVeiCliDes` | `N/D` | - |
| `CRVeiCep` | `N/D` | - |
| `CRVeiLog` | `N/D` | - |
| `CRVeiCid` | `N/D` | - |
| `CRVeiUF` | `N/D` | - |
| `CRVeiTel1` | `N/D` | - |
| `CRVeiTel2` | `N/D` | - |
| `CRVeiTel3` | `N/D` | - |
| `CRVeiMod` | `N/D` | - |
| `CRVeiPneu` | `N/D` | - |
| `CRVeiRen` | `N/D` | - |
| `CRVeiCoeW` | `N/D` | - |
| `CRVeiTacMar` | `N/D` | - |
| `CRVeiTacMod` | `N/D` | - |
| `CRVeiTacSer` | `N/D` | - |
| `CRVeiTac8ConK` | `N/D` | - |
| `CRVeiTac1SelPlaCol` | `N/D` | - |
| `CRVeiTac2AdeCol` | `N/D` | - |
| `CRVeiTac3RetSelPla` | `N/D` | - |
| `CRVeiTac4RetAde` | `N/D` | - |
| `CRVeiTacDtaSer` | `N/D` | - |
| `CRVeiTac5NroOS` | `N/D` | - |
| `CRVeiTac6NroNF` | `N/D` | - |
| `CRVeiTac7Res` | `N/D` | - |
| `CRVeiCadSerInm` | `N/D` | - |
| `CRVeiFrota` | `N/D` | - |
| `CRVeiDtaAle` | `N/D` | - |

#### 🗺️ Índices
- `CRVEI1` (Unique): `CRVeiPlc`
- `CRVei2` (Duplicate): `CRVeiCadSerInm`

---

### 📌 CRVeiH
- **Descrição:** Histórico Abastecimentos Veículos
- **Chave Primária:** `CRVeiPlc`, `CRVeiHTST`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CRVeiPlc` | `N/D` | - |
| `CRVeiHTST` | `N/D` | - |
| `CRVeiMar` | `N/D` | - |
| `CRVeiDes` | `N/D` | - |
| `CRVeiCil` | `N/D` | - |
| `CRVeiKM` | `N/D` | - |
| `CRVeiAno` | `N/D` | - |
| `CRVeiCor` | `N/D` | - |
| `CRVeiChas` | `N/D` | - |
| `CRVeiHKIn` | `N/D` | - |
| `CRVeiHKFi` | `N/D` | - |
| `CRVeiMedCom` | `N/D` | - |
| `CRVeiHDifKM` | `N/D` | - |
| `CRVeiHQtd` | `N/D` | - |
| `CRVeiHLoc` | `N/D` | - |
| `CRVeiHMed` | `N/D` | - |
| `CRVeiHUsu` | `N/D` | - |
| `CRVeiHPrg` | `N/D` | - |
| `CRVeiHVlr` | `N/D` | - |
| `CRVeiHVlrLit` | `N/D` | - |
| `CRVeiHUltTST` | `N/D` | - |
| `CRVeiHKDi` | `N/D` | - |
| `CRVeiHDifDia` | `N/D` | - |
| `CRVeiHIdx` | `N/D` | - |
| `CRVeiHPesEnt` | `N/D` | - |
| `CRVeiHPesSai` | `N/D` | - |
| `CRVeiHPesDif` | `N/D` | - |
| `CRVeiHPesIDta` | `N/D` | - |
| `CRVeiHPesFlg` | `N/D` | - |
| `CRVeiCliCod` | `N/D` | - |
| `CRVeiCliDes` | `N/D` | - |
| `CRVeiHPesObs` | `N/D` | - |
| `CRVeiHPesProCod` | `N/D` | - |
| `CRVeiHPes_ProDes` | `N/D` | - |
| `CRVeiHVlrUni` | `N/D` | - |
| `CRVeiHiPicVlrUn` | `N/D` | - |
| `CRVeiHVlrTot` | `N/D` | - |
| `CRVeiHPicVlrTot` | `N/D` | - |
| `CRVeiHPes1EmpMov` | `N/D` | - |
| `CRVeiHPes2FilMov` | `N/D` | - |
| `CRVeiHPes3DtaMov` | `N/D` | - |
| `CRVeiHPes4SeqMov` | `N/D` | - |
| `CRVeiHPesNroNF` | `N/D` | - |
| `CRVeiHDHEnt` | `N/D` | - |
| `CRVeiHDHSai` | `N/D` | - |
| `CRVeiHCliCod` | `N/D` | - |
| `CRVeiHCliDes` | `N/D` | - |
| `CRVeiHQtdTon` | `N/D` | - |
| `CRVeiHUniTon` | `N/D` | - |
| `CRVeiHPicUniTon` | `N/D` | - |

#### 🗺️ Índices
- `CRVeiH1` (Unique): `CRVeiPlc`, `CRVeiHTST`
- `CRVeiH2` (Duplicate): `CRVeiPlc`
- `CRVeiH3` (Duplicate): `CRVeiHTST`
- `CRVeiH4` (Duplicate): `CRVeiHIdx`
- `CRVeiH5` (Duplicate): `CRVeiHPesFlg`, `CRVeiHPesIDta`
- `CRVeiH6` (Duplicate): `CRVeiHPesIDta`

---

### 📌 CRVen
- **Descrição:** Vendedores para Dinamic Combo Box
- **Chave Primária:** `CRVenNom`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CRVenNom` | `N/D` | - |

#### 🗺️ Índices
- `CRVen1` (Unique): `CRVenNom`

---

### 📌 CT01A
- **Descrição:** Dados da NFP - Cupom E14
- **Chave Primária:** `CT01ImpFis`, `CT01NumCCF`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CT01ImpFis` | `N/D` | - |
| `CT01NumCCF` | `N/D` | - |
| `CT01DtEmi` | `N/D` | - |
| `CT01NumCOO` | `N/D` | - |
| `CT01VrTDoc` | `N/D` | - |
| `CT01VrTPis` | `N/D` | - |
| `CT01VrTCof` | `N/D` | - |
| `CT01CodAdq` | `N/D` | - |
| `CT01NomAdq` | `N/D` | - |
| `CT01DocCan` | `N/D` | - |
| `CT01EquipA` | `N/D` | - |
| `CT01NumSeA` | `N/D` | - |
| `CT01NumUsA` | `N/D` | - |

#### 🗺️ Índices
- `CT01A1` (Unique): `CT01ImpFis`, `CT01NumCCF`

---

### 📌 CT01B
- **Descrição:** Dados da NFP - Produtos E15
- **Chave Primária:** `CT01ImpFis`, `CT01NumCCF`, `CT01Item`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CT01ImpFis` | `N/D` | - |
| `CT01NumCCF` | `N/D` | - |
| `CT01Item` | `N/D` | - |
| `CT01CodPro` | `N/D` | - |
| `CT01DesPro` | `N/D` | - |
| `CT01EmpCod` | `N/D` | - |
| `CT01ProCod` | `N/D` | - |
| `CT01ProDes` | `N/D` | - |
| `CT01ProUnd` | `N/D` | - |
| `CT01ProNat` | `N/D` | - |
| `CT01CSTPis` | `N/D` | - |
| `CT01CSTCof` | `N/D` | - |
| `CT01BsPis` | `N/D` | - |
| `CT01AlPis` | `N/D` | - |
| `CT01VrPis` | `N/D` | - |
| `CT01BsCof` | `N/D` | - |
| `CT01AlCof` | `N/D` | - |
| `CT01VrCof` | `N/D` | - |
| `CT01Qtd` | `N/D` | - |
| `CT01VrUn` | `N/D` | - |
| `CT01VrTot` | `N/D` | - |
| `CT01QtdCan` | `N/D` | - |
| `CT01Un` | `N/D` | - |
| `CT01IndCan` | `N/D` | - |
| `CT01CSTIcm` | `N/D` | - |
| `CT01TotTri` | `N/D` | - |
| `CT01AlIcm` | `N/D` | - |
| `CT01EquipB` | `N/D` | - |
| `CT01NumSeB` | `N/D` | - |
| `CT01NumUsB` | `N/D` | - |
| `CT01ProCsP` | `N/D` | - |
| `CT01ProCsC` | `N/D` | - |

#### 🗺️ Índices
- `CT01B1` (Unique): `CT01ImpFis`, `CT01NumCCF`, `CT01Item`
- `CT01B2` (Duplicate): `CT01ImpFis`, `CT01NumCCF`

---

### 📌 CT02A
- **Descrição:** Dados da NFP - Relação de Reduções Z
- **Chave Primária:** `CT02ImpFis`, `CT02NumCRZ`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CT02ImpFis` | `N/D` | - |
| `CT02NumCRZ` | `N/D` | - |
| `CT02COOCRZ` | `N/D` | - |
| `CT02CROCRZ` | `N/D` | - |
| `CT02DtMov` | `N/D` | - |
| `CT02DtEmi` | `N/D` | - |
| `CT02HrEmi` | `N/D` | - |
| `CT02VBruta` | `N/D` | - |
| `CT02DescIS` | `N/D` | - |
| `CT02EquipA` | `N/D` | - |
| `CT02NumSeA` | `N/D` | - |
| `CT02NumUsA` | `N/D` | - |
| `CT02PriCOO` | `N/D` | - |
| `CT02UltCOO` | `N/D` | - |
| `CT02VrAnt` | `N/D` | - |
| `CT02VrTot` | `N/D` | - |
| `CT02VrAtu` | `N/D` | - |

#### 🗺️ Índices
- `CT02A1` (Unique): `CT02ImpFis`, `CT02NumCRZ`
- `CT02A2` (Duplicate): `CT02ImpFis`, `CT02DtMov`
- `CT02A3` (Duplicate): `CT02ImpFis`, `CT02DtMov`

---

### 📌 CT02B
- **Descrição:** Dados da NFP - Totais de Tributação da Redução Z
- **Chave Primária:** `CT02ImpFis`, `CT02NumCRZ`, `CT02TotTri`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CT02ImpFis` | `N/D` | - |
| `CT02NumCRZ` | `N/D` | - |
| `CT02TotTri` | `N/D` | - |
| `CT02VrTri` | `N/D` | - |
| `CT02EquipB` | `N/D` | - |
| `CT02NumSeB` | `N/D` | - |
| `CT02NumUsB` | `N/D` | - |

#### 🗺️ Índices
- `CT02B1` (Unique): `CT02ImpFis`, `CT02NumCRZ`, `CT02TotTri`
- `CT02B2` (Duplicate): `CT02ImpFis`, `CT02NumCRZ`

---

### 📌 CT03A
- **Descrição:** SPED - Participantes (Registro 0150)
- **Chave Primária:** `CMEmpCod`, `CT03TipPar`, `CT03CodPar`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CT03TipPar` | `N/D` | - |
| `CT03CodPar` | `N/D` | - |
| `CT03NomPar` | `N/D` | - |
| `CT03CodTXT` | `N/D` | - |
| `CT03ModNF` | `N/D` | - |

#### 🗺️ Índices
- `CT03A1` (Unique): `CMEmpCod`, `CT03TipPar`, `CT03CodPar`
- `CT03A2` (Duplicate): `CMEmpCod`

---

### 📌 CT03B
- **Descrição:** SPED - Produtos (Registro 0200)
- **Chave Primária:** `CMEmpCod`, `CT03CodPro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CT03CodPro` | `N/D` | - |
| `CT03DesPro` | `N/D` | - |
| `CT03CodPrT` | `N/D` | - |

#### 🗺️ Índices
- `CT03B1` (Unique): `CMEmpCod`, `CT03CodPro`
- `CT03B2` (Duplicate): `CMEmpCod`

---

### 📌 CT03C
- **Descrição:** SPED - Agrupamento Bloco M (CST)
- **Chave Primária:** `CT03TipoPC`, `CT03CST`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CT03TipoPC` | `N/D` | - |
| `CT03CST` | `N/D` | - |
| `CT03BsCST` | `N/D` | - |

#### 🗺️ Índices
- `CT03C1` (Unique): `CT03TipoPC`, `CT03CST`

---

### 📌 CT03D
- **Descrição:** SPED - Agrupamento Bloco M (Nat. Rec.)
- **Chave Primária:** `CT03TipoPC`, `CT03CST`, `CT03NatRec`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CT03TipoPC` | `N/D` | - |
| `CT03CST` | `N/D` | - |
| `CT03NatRec` | `N/D` | - |
| `CT03BsNat` | `N/D` | - |

#### 🗺️ Índices
- `CT03D1` (Unique): `CT03TipoPC`, `CT03CST`, `CT03NatRec`
- `CT03D2` (Duplicate): `CT03TipoPC`, `CT03CST`

---

### 📌 CT03E
- **Descrição:** SPED - Erros durante a validação
- **Chave Primária:** `CT03SeqErr`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CT03SeqErr` | `N/D` | - |
| `CT03DscErr` | `N/D` | - |

#### 🗺️ Índices
- `CT03E1` (Unique): `CT03SeqErr`

---

### 📌 CT03F
- **Descrição:** SPED - Temporária para Geração do Arquivo Texto
- **Chave Primária:** `CT03SeqArq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CT03SeqArq` | `N/D` | - |
| `CT03Txt01` | `N/D` | - |
| `CT03Txt02` | `N/D` | - |
| `CT03Txt03` | `N/D` | - |
| `CT03Txt04` | `N/D` | - |
| `CT03Txt05` | `N/D` | - |
| `CT03Txt06` | `N/D` | - |
| `CT03Txt07` | `N/D` | - |
| `CT03Txt08` | `N/D` | - |
| `CT03Txt09` | `N/D` | - |
| `CT03Txt10` | `N/D` | - |

#### 🗺️ Índices
- `CT03F1` (Unique): `CT03SeqArq`

---

### 📌 CT04A
- **Descrição:** SPED - Importação do MFD 1
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CT04Ano`, `CT04Mes`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CT04Ano` | `N/D` | - |
| `CT04Mes` | `N/D` | - |
| `CT04Ser01` | `N/D` | - |
| `CT04Ser02` | `N/D` | - |
| `CT04Ser03` | `N/D` | - |
| `CT04Ser04` | `N/D` | - |
| `CT04Ser05` | `N/D` | - |
| `CT04Ser06` | `N/D` | - |
| `CT04Ser07` | `N/D` | - |
| `CT04Ser08` | `N/D` | - |
| `CT04Ser09` | `N/D` | - |
| `CT04Ser10` | `N/D` | - |
| `CT04Mod01` | `N/D` | - |
| `CT04Mod02` | `N/D` | - |
| `CT04Mod03` | `N/D` | - |
| `CT04Mod04` | `N/D` | - |
| `CT04Mod05` | `N/D` | - |
| `CT04Mod06` | `N/D` | - |
| `CT04Mod07` | `N/D` | - |
| `CT04Mod08` | `N/D` | - |
| `CT04Mod09` | `N/D` | - |
| `CT04Mod10` | `N/D` | - |
| `CT04Arq01` | `N/D` | - |
| `CT04Arq02` | `N/D` | - |
| `CT04Arq03` | `N/D` | - |
| `CT04Arq04` | `N/D` | - |
| `CT04Arq05` | `N/D` | - |
| `CT04Arq06` | `N/D` | - |
| `CT04Arq07` | `N/D` | - |
| `CT04Arq08` | `N/D` | - |
| `CT04Arq09` | `N/D` | - |
| `CT04Arq10` | `N/D` | - |
| `CT04LimTbl` | `N/D` | - |

#### 🗺️ Índices
- `CT04A1` (Unique): `CMEmpCod`, `CMFilCod`, `CT04Ano`, `CT04Mes`
- `CT04A2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CT04B
- **Descrição:** SPED - Importação do MFD 2
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CT04Ano`, `CT04Mes`, `CT04Equip`, `CT04SeqTxt`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CT04Ano` | `N/D` | - |
| `CT04Mes` | `N/D` | - |
| `CT04Equip` | `N/D` | - |
| `CT04SeqTxt` | `N/D` | - |
| `CT04LinTxt` | `N/D` | - |

#### 🗺️ Índices
- `CT04B1` (Unique): `CMEmpCod`, `CMFilCod`, `CT04Ano`, `CT04Mes`, `CT04Equip`, `CT04SeqTxt`
- `CT04B2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CT04Ano`, `CT04Mes`

---

### 📌 CT04C
- **Descrição:** SPED - Importação do MFD 3
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CT04Ano`, `CT04Mes`, `CT04Equip`, `CT04Data`, `CT04CodPro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CT04Ano` | `N/D` | - |
| `CT04Mes` | `N/D` | - |
| `CT04Equip` | `N/D` | - |
| `CT04Data` | `N/D` | - |
| `CT04CodPro` | `N/D` | - |
| `CT04VrAcu` | `N/D` | - |

#### 🗺️ Índices
- `CT04C1` (Unique): `CMEmpCod`, `CMFilCod`, `CT04Ano`, `CT04Mes`, `CT04Equip`, `CT04Data`, `CT04CodPro`
- `CT04C2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CT04Ano`, `CT04Mes`

---

### 📌 CT04D
- **Descrição:** SPED - Importação do MFD 4
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CT04Ano`, `CT04Mes`, `CT04Equip`, `CT04Data`, `CT04COO`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CT04Ano` | `N/D` | - |
| `CT04Mes` | `N/D` | - |
| `CT04Equip` | `N/D` | - |
| `CT04Data` | `N/D` | - |
| `CT04COO` | `N/D` | - |
| `CT04VrDoc` | `N/D` | - |
| `CT04VrCan` | `N/D` | - |

#### 🗺️ Índices
- `CT04D1` (Unique): `CMEmpCod`, `CMFilCod`, `CT04Ano`, `CT04Mes`, `CT04Equip`, `CT04Data`, `CT04COO`
- `CT04D2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CT04Ano`, `CT04Mes`

---

### 📌 CT05A
- **Descrição:** Dados do Contador
- **Chave Primária:** `CT05EmpCod`, `CT05FilCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CT05EmpCod` | `N/D` | - |
| `CT05FilCod` | `N/D` | - |
| `CT05Nome` | `N/D` | - |
| `CT05CPF` | `N/D` | - |
| `CT05CRC` | `N/D` | - |
| `CT05CNPJ` | `N/D` | - |
| `CT05CEP` | `N/D` | - |
| `CT05Endere` | `N/D` | - |
| `CT05Numend` | `N/D` | - |
| `CT05Compl` | `N/D` | - |
| `CT05Bairro` | `N/D` | - |
| `CT05Fone` | `N/D` | - |
| `CT05Fax` | `N/D` | - |
| `CT05Email` | `N/D` | - |
| `CT05IBGE` | `N/D` | - |
| `CT05CPIS04` | `N/D` | - |
| `CT05DPIS04` | `N/D` | - |
| `CT05CPIS05` | `N/D` | - |
| `CT05DPIS05` | `N/D` | - |
| `CT05CPIS06` | `N/D` | - |
| `CT05DPIS06` | `N/D` | - |
| `CT05CPIS07` | `N/D` | - |
| `CT05DPIS07` | `N/D` | - |
| `CT05CPIS08` | `N/D` | - |
| `CT05DPIS08` | `N/D` | - |
| `CT05CPIS09` | `N/D` | - |
| `CT05DPIS09` | `N/D` | - |
| `CT05CCOF04` | `N/D` | - |
| `CT05DCOF04` | `N/D` | - |
| `CT05CCOF05` | `N/D` | - |
| `CT05DCOF05` | `N/D` | - |
| `CT05CCOF06` | `N/D` | - |
| `CT05DCOF06` | `N/D` | - |
| `CT05CCOF07` | `N/D` | - |
| `CT05DCOF07` | `N/D` | - |
| `CT05CCOF08` | `N/D` | - |
| `CT05DCOF08` | `N/D` | - |
| `CT05CCOF09` | `N/D` | - |
| `CT05DCOF09` | `N/D` | - |

#### 🗺️ Índices
- `CT05A1` (Unique): `CT05EmpCod`, `CT05FilCod`

---

### 📌 CT05C
- **Descrição:** Parâmetros SPED - PIS/COFINS
- **Chave Primária:** `CT05EmpCod`, `CT05FilCod`, `CT05TipoPC`, `CT05CSTPC`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CT05EmpCod` | `N/D` | - |
| `CT05FilCod` | `N/D` | - |
| `CT05TipoPC` | `N/D` | - |
| `CT05CSTPC` | `N/D` | - |

#### 🗺️ Índices
- `CT05C1` (Unique): `CT05EmpCod`, `CT05FilCod`, `CT05TipoPC`, `CT05CSTPC`
- `CT05C2` (Duplicate): `CT05EmpCod`, `CT05FilCod`

---

### 📌 CT05D
- **Descrição:** Parâmetros SPED - PIS/COFINS Natureza da Receita
- **Chave Primária:** `CT05EmpCod`, `CT05FilCod`, `CT05TipoPC`, `CT05CSTPC`, `CT05NatRec`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CT05EmpCod` | `N/D` | - |
| `CT05FilCod` | `N/D` | - |
| `CT05TipoPC` | `N/D` | - |
| `CT05CSTPC` | `N/D` | - |
| `CT05NatRec` | `N/D` | - |
| `CT05CodCtb` | `N/D` | - |
| `CT05DscCtb` | `N/D` | - |

#### 🗺️ Índices
- `CT05D1` (Unique): `CT05EmpCod`, `CT05FilCod`, `CT05TipoPC`, `CT05CSTPC`, `CT05NatRec`
- `CT05D2` (Duplicate): `CT05EmpCod`, `CT05FilCod`, `CT05TipoPC`, `CT05CSTPC`

---

### 📌 CT06A
- **Descrição:** SPED - Contas Contábeis
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CT06CodCtb`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CT06CodCtb` | `N/D` | - |
| `CT06DesCtb` | `N/D` | - |
| `CT06CodRFB` | `N/D` | - |
| `CT06NatCtb` | `N/D` | - |

#### 🗺️ Índices
- `CT06A1` (Unique): `CMEmpCod`, `CMFilCod`, `CT06CodCtb`
- `CT06A2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CT07A
- **Descrição:** SPED - Histórico Qtde Estoque (Bloco H)
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CEProCod`, `CT07ADta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CT07ADta` | `N/D` | - |
| `CT07ASal` | `N/D` | - |
| `CT07AVlrUnt` | `N/D` | - |
| `CT07AVlrTot` | `N/D` | - |

#### 🗺️ Índices
- `CT07A1` (Unique): `CMEmpCod`, `CMFilCod`, `CEProCod`, `CT07ADta`
- `CT07A2` (Duplicate): `CMEmpCod`, `CEProCod`
- `CT07A3` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 CxCxa
- **Descrição:** Caixa
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CxCxaDta`, `CxCxaCheOut`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CxCxaDta` | `N/D` | - |
| `CxCxaCheOut` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CMFilImpPrxCab` | `N/D` | - |
| `CMFilRecChq` | `N/D` | - |
| `CMFIlFecCxaDia` | `N/D` | - |
| `CMFilMosCamCxa` | `N/D` | - |
| `CxCxaTrcIni` | `N/D` | - |
| `CxCxaTrcFim` | `N/D` | - |
| `CxCxaSaiOut` | `N/D` | - |
| `CxCxaEntOut` | `N/D` | - |
| `CMFilBcoCof` | `N/D` | - |
| `CMFilFilBcoCof` | `N/D` | - |
| `CxCxaDepDia` | `N/D` | - |
| `CxCxaDepPrxDia` | `N/D` | - |
| `CxCxaDepCfrDia` | `N/D` | - |
| `CxCxaVlrDsp` | `N/D` | - |
| `CxCxaTotBri` | `N/D` | - |
| `CxCxaBAFE` | `N/D` | - |
| `CxCxaVlrFim` | `N/D` | - |
| `CxCxaTotVis` | `N/D` | - |
| `CxCxaTotRPa` | `N/D` | - |
| `CxCxaTotVda` | `N/D` | - |
| `CxCxaTotCVd` | `N/D` | - |
| `CxCxaTotEst` | `N/D` | - |
| `CxCxaDinDevCli` | `N/D` | - |
| `CxCxaTotChq` | `N/D` | - |
| `CxCxaCUsu` | `N/D` | - |
| `CxCxaCHor` | `N/D` | - |
| `CxCxaCDta` | `N/D` | - |
| `CxCxaCPrg` | `N/D` | - |
| `CxCxaFlag` | `N/D` | - |
| `CxCxaDtaTrs` | `N/D` | - |
| `CxCxaFlaDel` | `N/D` | - |
| `CxCxaEntCreCli` | `N/D` | - |
| `CXCxaEntManCreCli` | `N/D` | - |
| `CxCxaSaiCreCli` | `N/D` | - |
| `CxCxaVlrTrcMer` | `N/D` | - |
| `CxCxaTotDesRecPar` | `N/D` | - |
| `CXCxaTotAcrRecPar` | `N/D` | - |
| `CxCxaVlrRegCxa` | `N/D` | - |
| `CxCxaTotCCr` | `N/D` | - |
| `CxCxaTotCreUsaVda` | `N/D` | - |
| `CxCxaVlr_RecCon` | `N/D` | - |
| `CxCxaTotRecCCr` | `N/D` | - |
| `CMFilImpCxaComDetVda` | `N/D` | - |
| `CxCxaAbrLoj` | `N/D` | - |
| `CXCxaTotCDe` | `N/D` | - |
| `CXCxaTot1Cre` | `N/D` | - |
| `CXCxaTot2CreLiq` | `N/D` | - |
| `CxCxaDscRecCCr` | `N/D` | - |
| `CxCxaPgtFun` | `N/D` | - |
| `CMFilLctCxaUnc` | `N/D` | - |
| `CMFilAltCxaAnt` | `N/D` | - |
| `CXCxaRecBol` | `N/D` | - |
| `CXCxaVlrCCr` | `N/D` | - |
| `CXCxaVlChq` | `N/D` | - |
| `CMFilRecCCr` | `N/D` | - |
| `CXCxaPVV` | `N/D` | - |
| `CXCxaDCx` | `N/D` | - |
| `CXCxaPQP` | `N/D` | - |
| `CXCxaTotCP` | `N/D` | - |
| `CXCxaAcrVdaVis` | `N/D` | - |
| `CXCxaVlrChqTrc` | `N/D` | - |
| `CXCxaVlRec` | `N/D` | - |
| `CXCxaBcoDia` | `N/D` | - |
| `CXCxaBcoPrxDia` | `N/D` | - |
| `CxCxaBcoCfrDia` | `N/D` | - |
| `CXCxaFilBcoDia` | `N/D` | - |
| `CXCxaFilPrxDiaBco` | `N/D` | - |
| `CxCxaFilCfrDiaBco` | `N/D` | - |
| `CxCxaVlrAcr` | `N/D` | - |
| `CXCxaVlrCanIte` | `N/D` | - |
| `CXCxaCCV` | `N/D` | - |
| `CXCxaCCVD` | `N/D` | - |
| `CXCxaVlrDev` | `N/D` | - |
| `CXCxaUSU` | `N/D` | - |
| `CXCxaRecOutFil` | `N/D` | - |
| `CXCxaRecChqDev` | `N/D` | - |
| `CxCxaPgt_FunNaoCxa` | `N/D` | - |
| `CxCxaMovCxa` | `N/D` | - |
| `CxCxaVlrVdaBB` | `N/D` | - |
| `CxCxaTotBBCxa` | `N/D` | - |
| `CxCxaCreAnt` | `N/D` | - |
| `CxCxaCreAtu` | `N/D` | - |
| `CxCxaCreSld` | `N/D` | - |
| `CxCxaCrePgt` | `N/D` | - |
| `CxCxaCreNov` | `N/D` | - |
| `CxCxaCreDif` | `N/D` | - |
| `CXCxaCreCanAbe` | `N/D` | - |
| `CXCxaCECdx3` | `N/D` | - |
| `CXCxaCMAud` | `N/D` | - |
| `CXCxaTrcAntFin` | `N/D` | - |
| `CXCxaCEDia` | `N/D` | - |
| `CXCxaCCx` | `N/D` | - |
| `CXCxaPCC` | `N/D` | - |
| `CXCxaPCD` | `N/D` | - |
| `CXCxaPCP` | `N/D` | - |
| `CXCxaVLrV1` | `N/D` | - |
| `CXCxaDtaFin` | `N/D` | - |
| `CXCxaTstFin` | `N/D` | - |
| `CXCxaCCVlr` | `N/D` | - |
| `CXCxaCCBco` | `N/D` | - |
| `CXCxaRecParTrs` | `N/D` | - |
| `CxCxaTotFin` | `N/D` | - |
| `CxCxaObs1` | `N/D` | - |
| `CxCxaObs2` | `N/D` | - |
| `CxCxaObs3` | `N/D` | - |
| `CxCxaAudTI` | `N/D` | - |
| `CxCxaAudTF` | `N/D` | - |
| `CxCxaAudVF` | `N/D` | - |
| `CxCxaAudOK` | `N/D` | - |
| `CXCxaTstSan` | `N/D` | - |
| `CxCxaCCDepDia` | `N/D` | - |
| `CxCxaCCPrxDia` | `N/D` | - |
| `CXCxaDscPixCCr` | `N/D` | - |
| `CXCxaScaMsgErr` | `N/D` | - |
| `CxCxaObs4` | `N/D` | - |
| `CxCxaObs5` | `N/D` | - |
| `CxCxaObs6` | `N/D` | - |
| `CxCxaObs7` | `N/D` | - |
| `CxCxaObs8` | `N/D` | - |
| `CxCxaObs9` | `N/D` | - |
| `CxCxaSeq` | `N/D` | - |
| `CMFilCnfESC` | `N/D` | - |
| `CXCxaPgtBco` | `N/D` | - |

#### 🗺️ Índices
- `CxCxa2` (Unique): `CMEmpCod`, `CMFilCod`, `CxCxaDta`, `CxCxaCheOut`
- `CxCxa3` (Duplicate): `CMEmpCod`, `CMFilCod`
- `CxCxa4` (Duplicate): `CMEmpCod`, `CxCxaFlag`
- `CXCxa5` (Duplicate): `CXCxaDCx`
- `CXCxa6` (Duplicate): `CXCxaCCx`

---

### 📌 CxCxa1
- **Descrição:** Sangria do Caixa
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CxCxaDta`, `CxCxaCheOut`, `CxCxa1Seq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CxCxaDta` | `N/D` | - |
| `CxCxaCheOut` | `N/D` | - |
| `CxCxaSeq` | `N/D` | - |
| `CMFilBcoCof` | `N/D` | - |
| `CMFilFilBcoCof` | `N/D` | - |
| `CMFilAltCxaAnt` | `N/D` | - |
| `CMFilCnfESC` | `N/D` | - |
| `CXCxaPgtBco` | `N/D` | - |
| `CxCxaEntOut` | `N/D` | - |
| `CxCxaSaiOut` | `N/D` | - |
| `CxCxaFlag` | `N/D` | - |
| `CxCxa1Seq` | `N/D` | - |
| `CxCxa1Hor` | `N/D` | - |
| `CxCxa1Vlr` | `N/D` | - |
| `CxCxa1Obs` | `N/D` | - |
| `CxCxa1EntSai` | `N/D` | - |
| `CxCxa1UsuNom` | `N/D` | - |
| `CxCxa1CnfESC` | `N/D` | - |
| `CxCxa1DCx` | `N/D` | - |
| `CXCxa1CRDta` | `N/D` | - |
| `CXCxa1CRSeq` | `N/D` | - |
| `CxCxa1CRIte` | `N/D` | - |
| `CXCxa1BcoCod` | `N/D` | - |
| `CXCxa1LctCC` | `N/D` | - |
| `CXCxa1Tip` | `N/D` | - |
| `CxCxa1CCx` | `N/D` | - |

#### 🗺️ Índices
- `CxCxa11` (Unique): `CMEmpCod`, `CMFilCod`, `CxCxaDta`, `CxCxaCheOut`, `CxCxa1Seq`
- `CxCxa12` (Duplicate): `CMEmpCod`, `CMFilCod`, `CxCxaDta`, `CxCxaCheOut`
- `CxCxa13` (Duplicate): `CxCxa1DCx`
- `CxCxa14` (Duplicate): `CxCxa1CCx`

---

### 📌 CXCxC
- **Descrição:** Detalhes Recebimento do Cartão
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CxCxaDta`, `CxCxaCheOut`, `CXCxCSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CxCxaDta` | `N/D` | - |
| `CxCxaCheOut` | `N/D` | - |
| `CXCxCSeq` | `N/D` | - |
| `CXCxCNom` | `N/D` | - |
| `CXCxCVlr` | `N/D` | - |
| `CXCxCDCx` | `N/D` | - |
| `CXCxCCCRCod` | `N/D` | - |
| `CXCxCFilMov` | `N/D` | - |
| `CXCxCDtaMov` | `N/D` | - |
| `CXCxCSeqMov` | `N/D` | - |
| `CXCxCPrg` | `N/D` | - |
| `CXCxCCCRDes` | `N/D` | - |
| `CXCxCTip` | `N/D` | - |

#### 🗺️ Índices
- `CXCxC1` (Unique): `CMEmpCod`, `CMFilCod`, `CxCxaDta`, `CxCxaCheOut`, `CXCxCSeq`
- `CXCxC2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CxCxaDta`, `CxCxaCheOut`
- `CXCxC3` (Duplicate): `CXCxCDCx`

---

### 📌 CXCXD
- **Descrição:** Detalhes dos Movimentos
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CxCxaDta`, `CxCxaCheOut`, `CXCxDSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CxCxaDta` | `N/D` | - |
| `CxCxaCheOut` | `N/D` | - |
| `CXCxDSeq` | `N/D` | - |
| `CXCxDObs` | `N/D` | - |
| `CXCxDOrg` | `N/D` | - |
| `CXCxDVlr` | `N/D` | - |
| `CXCxDDC` | `N/D` | - |
| `CXCxDVlrOrg` | `N/D` | - |
| `CXCxDVlrDsc` | `N/D` | - |
| `CXCxDVlrAcr` | `N/D` | - |

#### 🗺️ Índices
- `CXCXD1` (Unique): `CMEmpCod`, `CMFilCod`, `CxCxaDta`, `CxCxaCheOut`, `CXCxDSeq`
- `CXCXD2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CxCxaDta`, `CxCxaCheOut`

---

### 📌 DSCta
- **Descrição:** Plano de Contas
- **Chave Primária:** `CMEmpCod`, `DSCtaNiv01`, `DSCtaNiv02`, `DSCtaNiv03`, `DSCtaNiv04`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `DSCtaNiv01` | `N/D` | - |
| `DSCtaNiv02` | `N/D` | - |
| `DSCtaNiv03` | `N/D` | - |
| `DSCtaNiv04` | `N/D` | - |
| `DSCtaDes` | `N/D` | - |
| `DSCtaCla` | `N/D` | - |
| `DSCtaAceLct` | `N/D` | - |
| `DSCtaRecDsp` | `N/D` | - |
| `DSCtaPrg` | `N/D` | - |
| `DSCtaUsu` | `N/D` | - |
| `DSCtaTST` | `N/D` | - |
| `DSCtaNivGer` | `N/D` | - |

#### 🗺️ Índices
- `DSCta1` (Unique): `CMEmpCod`, `DSCtaNiv01`, `DSCtaNiv02`, `DSCtaNiv03`, `DSCtaNiv04`
- `DSCta2` (Duplicate): `CMEmpCod`
- `DSCta3` (Duplicate): `CMEmpCod`, `DSCtaCla`

---

### 📌 DSDSA
- **Descrição:** Despesa x Setor de Aplicação
- **Chave Primária:** `CMEmpCod`, `DSDspCod`, `DSDSACod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `DSDspCod` | `N/D` | - |
| `DSDSACod` | `N/D` | - |
| `DSDspDes` | `N/D` | - |
| `CMEmpDspSet` | `N/D` | - |
| `DSDSADES` | `N/D` | - |
| `DSDSACPRG` | `N/D` | - |
| `DSDSACTST` | `N/D` | - |
| `DSDSACUSU` | `N/D` | - |

#### 🗺️ Índices
- `DSDSAA` (Unique): `CMEmpCod`, `DSDspCod`, `DSDSACod`
- `DSDSAB` (Duplicate): `CMEmpCod`, `DSDspCod`

---

### 📌 DSDsp
- **Descrição:** Despesas
- **Chave Primária:** `CMEmpCod`, `DSDspCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `DSDspCod` | `N/D` | - |
| `DSDspIde` | `N/D` | - |
| `DSDspDes` | `N/D` | - |
| `DSGrpCod` | `N/D` | - |
| `DSGrpDes` | `N/D` | - |
| `DSDspFixVar` | `N/D` | - |
| `DSDspCHor` | `N/D` | - |
| `DSDspCDta` | `N/D` | - |
| `DSDspCUsu` | `N/D` | - |
| `DSDspCPrg` | `N/D` | - |
| `DSDspFlaDel` | `N/D` | - |
| `DSDspDtaTrs` | `N/D` | - |
| `DSSgrCod` | `N/D` | - |
| `DSSgrDes` | `N/D` | - |
| `DSDspVlrFix` | `N/D` | - |
| `CMEmpDspSet` | `N/D` | - |
| `DSDspQtdFix` | `N/D` | - |
| `CMEmpUsa_CCu` | `N/D` | - |
| `DSDspRecDsp` | `N/D` | - |
| `DSDspDiaVctDsp` | `N/D` | - |
| `DSDspDRE` | `N/D` | - |
| `DSCtaNiv01` | `N/D` | - |
| `DSCtaNiv02` | `N/D` | - |
| `DSCtaNiv03` | `N/D` | - |
| `DSCtaNiv04` | `N/D` | - |
| `DSCtaCla` | `N/D` | - |
| `DSCtaAceLct` | `N/D` | - |
| `DSCtaRecDsp` | `N/D` | - |
| `DSCtaDes` | `N/D` | - |
| `DSDspSetCod` | `N/D` | - |
| `DSDspSetDes` | `N/D` | - |
| `DSDspFil` | `N/D` | - |
| `DSDspFilNom` | `N/D` | - |
| `DSDspTipDre` | `N/D` | - |
| `DSDspTotPrc` | `N/D` | - |

#### 🗺️ Índices
- `DSDsp1` (Unique): `CMEmpCod`, `DSDspCod`
- `DSDsp2` (Duplicate): `CMEmpCod`, `DSGrpCod`, `DSSgrCod`
- `DSDsp7` (Duplicate): `CMEmpCod`, `DSCtaNiv01`, `DSCtaNiv02`, `DSCtaNiv03`, `DSCtaNiv04`
- `DSDsp3` (Duplicate): `CMEmpCod`, `DSDspDes`
- `DSDsp4` (Duplicate): `CMEmpCod`, `DSDspCod`
- `DSDsp5` (Duplicate): `CMEmpCod`, `DSGrpCod`

---

### 📌 DSDsR
- **Descrição:** Rateio de Despesa por Filial
- **Chave Primária:** `CMEmpCod`, `DSDspCod`, `DSDsRFil`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `DSDspCod` | `N/D` | - |
| `DSDspDes` | `N/D` | - |
| `DSDspTotPrc` | `N/D` | - |
| `DSDsRFil` | `N/D` | - |
| `DSDsRPrc` | `N/D` | - |
| `DSDsRCUsu` | `N/D` | - |
| `DSDsRCTst` | `N/D` | - |
| `DSDsRCPrg` | `N/D` | - |

#### 🗺️ Índices
- `DSDsR1` (Unique): `CMEmpCod`, `DSDspCod`, `DSDsRFil`
- `DSDsR2` (Duplicate): `CMEmpCod`, `DSDspCod`

---

### 📌 DSEmp
- **Descrição:** Empresa
- **Chave Primária:** `DSEmpCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `DSEmpCod` | `N/D` | - |
| `DSEmpAnoAtu` | `N/D` | - |
| `DSEmpMesAtu` | `N/D` | - |

#### 🗺️ Índices
- `DSEmp1` (Unique): `DSEmpCod`

---

### 📌 DSFAn
- **Descrição:** Parametros Anual
- **Chave Primária:** `DSEmpCod`, `DSFilCod`, `DSFAnAno`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `DSEmpCod` | `N/D` | - |
| `DSFilCod` | `N/D` | - |
| `DSFilDes` | `N/D` | - |
| `DSFAnAno` | `N/D` | - |
| `DSFAnVlrVda` | `N/D` | - |
| `DSFAnMetVda` | `N/D` | - |
| `DSFAnPrcRea` | `N/D` | - |
| `DSRAnCUsu` | `N/D` | - |
| `DSRAnCPrg` | `N/D` | - |
| `DSRAnTst` | `N/D` | - |

#### 🗺️ Índices
- `DSFAn1` (Unique): `DSEmpCod`, `DSFilCod`, `DSFAnAno`
- `DSFAn2` (Duplicate): `DSEmpCod`, `DSFilCod`

---

### 📌 DSFil
- **Descrição:** Filiais
- **Chave Primária:** `DSEmpCod`, `DSFilCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `DSEmpCod` | `N/D` | - |
| `DSEmpAnoAtu` | `N/D` | - |
| `DSEmpMesAtu` | `N/D` | - |
| `DSFilCod` | `N/D` | - |
| `DSFilDes` | `N/D` | - |
| `DSFilCUsu` | `N/D` | - |
| `DSFilCDta` | `N/D` | - |
| `DSFilCPrg` | `N/D` | - |

#### 🗺️ Índices
- `DSFil1` (Unique): `DSEmpCod`, `DSFilCod`
- `DSFil2` (Duplicate): `DSEmpCod`

---

### 📌 DSFMe
- **Descrição:** Resultado Mensal
- **Chave Primária:** `DSEmpCod`, `DSFilCod`, `DSFAnAno`, `DSFMeMes`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `DSEmpCod` | `N/D` | - |
| `DSFilCod` | `N/D` | - |
| `DSFilDes` | `N/D` | - |
| `DSFAnAno` | `N/D` | - |
| `DSFAnVlrVda` | `N/D` | - |
| `DSFAnMetVda` | `N/D` | - |
| `DSFAnPrcRea` | `N/D` | - |
| `DSRAnCUsu` | `N/D` | - |
| `DSRAnCPrg` | `N/D` | - |
| `DSRAnTst` | `N/D` | - |
| `DSFMeMes` | `N/D` | - |
| `DSFMeQtdDiaUte` | `N/D` | - |
| `DSFMeMetDiaVda` | `N/D` | - |
| `DSFMeMetVda` | `N/D` | - |
| `DSFMeCUsu` | `N/D` | - |
| `DSFMeCPrg` | `N/D` | - |
| `DSFMeCDta` | `N/D` | - |
| `DSFMEVlrVda` | `N/D` | - |
| `DSFMeDiaTra` | `N/D` | - |
| `DSFMeDiaAux` | `N/D` | - |
| `DSFMePrcRea` | `N/D` | - |
| `DSFMEPrcPro` | `N/D` | - |
| `DSFMePrdDif` | `N/D` | - |

#### 🗺️ Índices
- `DSFMe1` (Unique): `DSEmpCod`, `DSFilCod`, `DSFAnAno`, `DSFMeMes`
- `DSFMe2` (Duplicate): `DSEmpCod`, `DSFilCod`, `DSFAnAno`

---

### 📌 DSGrp
- **Descrição:** Grupo de Despesas
- **Chave Primária:** `CMEmpCod`, `DSGrpCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `DSGrpCod` | `N/D` | - |
| `DSGrpDes` | `N/D` | - |
| `DSGrpCHor` | `N/D` | - |
| `DSGrpCDta` | `N/D` | - |
| `DSGrpCUsu` | `N/D` | - |
| `DSGrpCPrg` | `N/D` | - |
| `DSGrpPrxSgr` | `N/D` | - |
| `DSGrpFlaDel` | `N/D` | - |
| `DSGrpDtaTrs` | `N/D` | - |

#### 🗺️ Índices
- `DSGrp1` (Unique): `CMEmpCod`, `DSGrpCod`
- `DSGrp2` (Duplicate): `CMEmpCod`
- `DSGrp3` (Duplicate): `CMEmpCod`, `DSGrpDes`
- `DSGrp4` (Duplicate): `CMEmpCod`, `DSGrpCod`

---

### 📌 DSLMG
- **Descrição:** Limite Mensal de Gasto da Despesa Saindo do Caixa
- **Chave Primária:** `CMEmpCod`, `DSDspCod`, `DSFilCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `DSDspCod` | `N/D` | - |
| `DSDspDes` | `N/D` | - |
| `DSFilCod` | `N/D` | - |
| `DSLMGVlr` | `N/D` | - |

#### 🗺️ Índices
- `DSLMG1` (Unique): `CMEmpCod`, `DSDspCod`, `DSFilCod`
- `DSLMG2` (Duplicate): `CMEmpCod`, `DSDspCod`

---

### 📌 DSMov1
- **Descrição:** Movimento Despesa 01
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `DSMov2Dta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `DSMov2Dta` | `N/D` | - |
| `CMFilDtaValLct` | `N/D` | - |
| `DSMov1AuxSeq` | `N/D` | - |
| `DSMov1DtaTrs` | `N/D` | - |
| `DSMov1FlaDel` | `N/D` | - |

#### 🗺️ Índices
- `DSMov11` (Unique): `CMEmpCod`, `CMFilCod`, `DSMov2Dta`
- `DSMov12` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 DSMov2
- **Descrição:** Movimento Despesa 02
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `DSMov2Dta`, `DSMov2Seq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `DSMov2Dta` | `N/D` | - |
| `DSMov2Seq` | `N/D` | - |
| `CMFilDtaValLct` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `CMFilBcoCof` | `N/D` | - |
| `CMFilFilBcoCof` | `N/D` | - |
| `CMEmpDspSet` | `N/D` | - |
| `CMFilAltGrpSgrDsp` | `N/D` | - |
| `CMEmpUsa_CCu` | `N/D` | - |
| `CMFilBxaDsp` | `N/D` | - |
| `CMEmpMoeCodPad` | `N/D` | - |
| `DSMov1FlaDel` | `N/D` | - |
| `DSDspDes` | `N/D` | - |
| `DSDspRecDsp` | `N/D` | - |
| `DSDspFixVar` | `N/D` | - |
| `DSDspSetDes` | `N/D` | - |
| `DSDspSetCod` | `N/D` | - |
| `DSGrpCod` | `N/D` | - |
| `DSGrpDes` | `N/D` | - |
| `DSMov2GrpCod` | `N/D` | - |
| `DSSgrCod` | `N/D` | - |
| `DSSgrDes` | `N/D` | - |
| `DSMov2VeiPlc` | `N/D` | - |
| `DSMov2VeiDes` | `N/D` | - |
| `DSMov2Qtd` | `N/D` | - |
| `DSMov2Vlr` | `N/D` | - |
| `DSMov2VlrMoe` | `N/D` | - |
| `DSMov2CHor` | `N/D` | - |
| `DSMov2CDta` | `N/D` | - |
| `DSMov2CUsu` | `N/D` | - |
| `DSMov2CPrg` | `N/D` | - |
| `DSMov2Obs` | `N/D` | - |
| `DSMov2DtaTrs` | `N/D` | - |
| `DSMov2FlaDel` | `N/D` | - |
| `DSMov2BcoCod` | `N/D` | - |
| `DSMov2NroChq` | `N/D` | - |
| `DSMov2Cxa` | `N/D` | - |
| `DSMov2DtaVctChq` | `N/D` | - |
| `DSMov2CCuCod` | `N/D` | - |
| `DSMov2CCuDes` | `N/D` | - |
| `DSMov2OrgCPCR` | `N/D` | - |
| `DSMov2OrgMovDta` | `N/D` | - |
| `DSMov2Org_MovSeq` | `N/D` | - |
| `DSMov2OrgNroPar` | `N/D` | - |
| `DSMov2PerRatCC` | `N/D` | - |
| `DSMov2CheOut` | `N/D` | - |
| `DSMov2CCMovSeqLct` | `N/D` | - |
| `DSMov2ForCod` | `N/D` | - |
| `DSMov2ForDes` | `N/D` | - |
| `DSMov2SgrCod` | `N/D` | - |
| `DSMov2SgrDes` | `N/D` | - |
| `DSMov2GrpDes` | `N/D` | - |
| `DSMov2DCx` | `N/D` | - |
| `DSDspDRE` | `N/D` | - |
| `DSMov2TSTVeiH` | `N/D` | - |
| `DSMov2IDX` | `N/D` | - |
| `DSMov2Sts` | `N/D` | - |
| `DSMov2DtaPgt` | `N/D` | - |
| `DSMov2ObsPgt` | `N/D` | - |
| `DSSetDes` | `N/D` | - |
| `DSSetCod` | `N/D` | - |
| `DSSetVeiPlc` | `N/D` | - |
| `DsSetVeiDes` | `N/D` | - |
| `DSMov2Org1CRMov5Cod` | `N/D` | - |
| `DSMov2ObsDet` | `N/D` | - |
| `DSMov2DtaNF` | `N/D` | - |
| `DSMov2NroNF` | `N/D` | - |
| `DSMov2Saf` | `N/D` | - |
| `DSMov2TSTLct` | `N/D` | - |
| `DSSgrVeiPlc` | `N/D` | - |
| `DSSgrVeiDes` | `N/D` | - |
| `DSMov2CCx` | `N/D` | - |
| `DSDspIde` | `N/D` | - |
| `DSDspFil` | `N/D` | - |
| `DSDspFilNom` | `N/D` | - |
| `DSMov2DspDta` | `N/D` | - |
| `DSDspCod` | `N/D` | - |
| `DSMov2PrcRat` | `N/D` | - |
| `DSMov2SQtd` | `N/D` | - |
| `DSMov2SVlr` | `N/D` | - |

#### 🗺️ Índices
- `DSMov21` (Unique): `CMEmpCod`, `CMFilCod`, `DSMov2Dta`, `DSMov2Seq`
- `DSMov23` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSMov2Dta`
- `DSMov22` (Duplicate): `CMEmpCod`, `DSDspCod`
- `DSMov2A` (Duplicate): `CMEmpCod`, `DSSetCod`
- `DSMov24` (Duplicate): `CMEmpCod`, `DSMov2DspDta`
- `DSMov25` (Duplicate): `CMEmpCod`, `DSMov2Dta`
- `DSMov26` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSMov2OrgMovDta`, `DSMov2Org_MovSeq`
- `DSMov27` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSMov2OrgCPCR`, `DSMov2OrgMovDta`, `DSMov2Org_MovSeq`, `DSMov2OrgNroPar`, `DSMov2Org1CRMov5Cod`
- `DSMov28` (Duplicate): `DSMov2DCx`
- `DSMov29` (Duplicate): `DSMov2IDX`
- `DSMov2B` (Duplicate): `DSMov2TSTLct`
- `DSMov2C` (Duplicate): `DSMov2CCx`

---

### 📌 DSMovS
- **Descrição:** Detalhamento do Lançamento por Setor de Aplicação
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `DSMov2Dta`, `DSMov2Seq`, `DSMovSSetCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `DSMov2Dta` | `N/D` | - |
| `DSMov2Seq` | `N/D` | - |
| `DSMov2SQtd` | `N/D` | - |
| `DSMov2SVlr` | `N/D` | - |
| `DSMov2Vlr` | `N/D` | - |
| `DSMov2Qtd` | `N/D` | - |
| `DSDspCod` | `N/D` | - |
| `DSDspDes` | `N/D` | - |
| `DSMovSSetCod` | `N/D` | - |
| `DSMovSSetDes` | `N/D` | - |
| `DSMovSVlr` | `N/D` | - |
| `DSMovSQtd` | `N/D` | - |
| `DSMovSObs` | `N/D` | - |
| `DSMovSVlrMoe` | `N/D` | - |

#### 🗺️ Índices
- `DSMovS1` (Unique): `CMEmpCod`, `CMFilCod`, `DSMov2Dta`, `DSMov2Seq`, `DSMovSSetCod`
- `DSMovS2` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSMov2Dta`, `DSMov2Seq`

---

### 📌 DSRAn
- **Descrição:** Resultado Anual
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `DSRAnAno`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `DSRAnAno` | `N/D` | - |
| `DSRAnVl_VdaBrt` | `N/D` | - |
| `DSRAnVl_CusBrt` | `N/D` | - |
| `DSRAnVlrVdaLiq` | `N/D` | - |
| `CMEmpMoeCodPad` | `N/D` | - |
| `DSRAnVlrCusLiq` | `N/D` | - |
| `DSRAnResBrt` | `N/D` | - |
| `DSRAnMrgBrt` | `N/D` | - |
| `DSRAnVlrDsp` | `N/D` | - |
| `DSRAnDspFix` | `N/D` | - |
| `DSRAnDspVar` | `N/D` | - |
| `DSRAnDspInv` | `N/D` | - |
| `DSRAnResLiq` | `N/D` | - |
| `DSRAnPerSobVda` | `N/D` | - |
| `DSRAnVlrEst` | `N/D` | - |
| `DSRAnVlrCRe` | `N/D` | - |
| `DSRAnVlrCPg` | `N/D` | - |
| `DSRAnResFin` | `N/D` | - |
| `DSRAnSalBco` | `N/D` | - |
| `DSRAnVlrChqAbe` | `N/D` | - |
| `DSRAnDtaTrs` | `N/D` | - |
| `DSRAnFlaDel` | `N/D` | - |
| `DSRAnVlr_VdaCan` | `N/D` | - |
| `DSRAnVlr_CusCan` | `N/D` | - |
| `DSRAnVlrCCr` | `N/D` | - |
| `DSRAnVlrPreChqCR` | `N/D` | - |
| `DSRAnVlrRecCCr` | `N/D` | - |
| `DSRAnVlr_ProVda` | `N/D` | - |
| `DSRanProCus` | `N/D` | - |
| `DSRanProLuc` | `N/D` | - |
| `DSRAnVlrDesCom` | `N/D` | - |
| `DSRAnVlrAcrCom` | `N/D` | - |
| `DSRAnVlr_AbeCom` | `N/D` | - |
| `DSRAnRecCon` | `N/D` | - |
| `DSRAnVlrPgtCP` | `N/D` | - |
| `DSRAnDtaHorUltPro` | `N/D` | - |
| `DSRAnRecCrd` | `N/D` | - |
| `DSRAnLucDif` | `N/D` | - |
| `DSRAnLuc01` | `N/D` | - |
| `DSRAnLuc02` | `N/D` | - |

#### 🗺️ Índices
- `DSRAn1` (Unique): `CMEmpCod`, `CMFilCod`, `DSRAnAno`
- `DSRAn2` (Duplicate): `CMEmpCod`, `CMFilCod`
- `DSRAn3` (Duplicate): `CMEmpCod`, `DSRAnAno`

---

### 📌 DSRFA
- **Descrição:** Resultado por Fornecedor Anual
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPCliCod`, `DSRFAANO`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `DSRFAANO` | `N/D` | - |
| `DSRFAVlrVda` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `DSRFAVlrCom` | `N/D` | - |
| `DSRFAQtdCom` | `N/D` | - |
| `DSRFAQtdVda` | `N/D` | - |
| `DSRFACusVda` | `N/D` | - |

#### 🗺️ Índices
- `DSRFA1` (Unique): `CMEmpCod`, `CMFilCod`, `CPCliCod`, `DSRFAANO`
- `DSRFA2` (Duplicate): `CMEmpCod`, `CPCliCod`
- `DSRFA3` (Duplicate): `CMEmpCod`, `CMFilCod`
- `DSRFA4` (Duplicate): `DSRFAANO`

---

### 📌 DSRFD
- **Descrição:** Resultado do Fornecedor Detalhado
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPCliCod`, `DSRFAANO`, `DSRFMMES`, `DSRFDCOD`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `DSRFAANO` | `N/D` | - |
| `DSRFMMES` | `N/D` | - |
| `DSRFMVlrVda` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `DSRFMVlrCom` | `N/D` | - |
| `DSRFMQtdEst` | `N/D` | - |
| `DSRFMVlrEst` | `N/D` | - |
| `DSRFMQtdCom` | `N/D` | - |
| `DSRFMQtdVda` | `N/D` | - |
| `DSRFMCusVda` | `N/D` | - |
| `DSRFMMrgLuc` | `N/D` | - |
| `DSRFMDtaIni` | `N/D` | - |
| `DSRFMDtaFin` | `N/D` | - |
| `DSRFMVen` | `N/D` | - |
| `DSRFMLuc` | `N/D` | - |
| `DSRFMVdaCus` | `N/D` | - |
| `DSRFMVdaVlr` | `N/D` | - |
| `DSFRMMrgVda` | `N/D` | - |
| `DSRFDCOD` | `N/D` | - |
| `DSRFDDES` | `N/D` | - |
| `DSRFDQtdCom` | `N/D` | - |
| `DSRFDQtdVda` | `N/D` | - |
| `DSRFDQtdEst` | `N/D` | - |
| `DSRFDQTD01` | `N/D` | - |
| `DSRFDQTD02` | `N/D` | - |
| `DSRFDQTD03` | `N/D` | - |
| `DSRFDQTD04` | `N/D` | - |
| `DSRFDQTD05` | `N/D` | - |
| `DSRFDQTD06` | `N/D` | - |
| `DSRFDQTD07` | `N/D` | - |
| `DSRFDQTD08` | `N/D` | - |
| `DSRFDQTD09` | `N/D` | - |
| `DSRFDQTD99` | `N/D` | - |
| `DSRFDFab` | `N/D` | - |
| `DSRFDQtdEmpEst` | `N/D` | - |
| `DSRFDGrpCod` | `N/D` | - |
| `DSRFDSgrCod` | `N/D` | - |
| `DSRFDGrpDes` | `N/D` | - |
| `DSRFDSgrDes` | `N/D` | - |
| `DSRFDIDX` | `N/D` | - |
| `DSRFDCusUnt` | `N/D` | - |
| `DSRFDVdaUnt` | `N/D` | - |
| `DSRFDMrgUnt` | `N/D` | - |
| `DSRFDCusTot` | `N/D` | - |
| `DSRFDVdaTot` | `N/D` | - |
| `DSRFDLuc` | `N/D` | - |
| `DSFRDVdaCus` | `N/D` | - |
| `DSFRDVdaVlr` | `N/D` | - |
| `DSRFDMrgVda` | `N/D` | - |
| `DSRFAVlrVda` | `N/D` | - |
| `DSRFAVlrCom` | `N/D` | - |
| `DSRFAQtdCom` | `N/D` | - |
| `DSRFAQtdVda` | `N/D` | - |
| `DSRFACusVda` | `N/D` | - |

#### 🗺️ Índices
- `DSRFDA` (Unique): `CMEmpCod`, `CMFilCod`, `CPCliCod`, `DSRFAANO`, `DSRFMMES`, `DSRFDCOD`
- `DSRFDB` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPCliCod`, `DSRFAANO`, `DSRFMMES`
- `DSRFDC` (Duplicate): `DSRFDIDX`
- `DSRFDD` (Duplicate): `DSRFAANO`, `DSRFMMES`

---

### 📌 DSRFM
- **Descrição:** Resultado por Fornecedor Mensal
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `CPCliCod`, `DSRFAANO`, `DSRFMMES`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `CPCliCod` | `N/D` | - |
| `DSRFAANO` | `N/D` | - |
| `DSRFMMES` | `N/D` | - |
| `DSRFMVlrVda` | `N/D` | - |
| `CPCliDes` | `N/D` | - |
| `DSRFMVlrCom` | `N/D` | - |
| `DSRFMQtdEst` | `N/D` | - |
| `DSRFMVlrEst` | `N/D` | - |
| `DSRFMQtdCom` | `N/D` | - |
| `DSRFMQtdVda` | `N/D` | - |
| `DSRFMCusVda` | `N/D` | - |
| `DSRFMMrgLuc` | `N/D` | - |
| `DSRFMDtaIni` | `N/D` | - |
| `DSRFMDtaFin` | `N/D` | - |
| `DSRFMVen` | `N/D` | - |
| `DSRFMLuc` | `N/D` | - |
| `DSRFMVdaCus` | `N/D` | - |
| `DSRFMVdaVlr` | `N/D` | - |
| `DSFRMMrgVda` | `N/D` | - |
| `DSRFAVlrVda` | `N/D` | - |
| `DSRFAVlrCom` | `N/D` | - |
| `DSRFAQtdCom` | `N/D` | - |
| `DSRFAQtdVda` | `N/D` | - |
| `DSRFACusVda` | `N/D` | - |

#### 🗺️ Índices
- `DSRFM1` (Unique): `CMEmpCod`, `CMFilCod`, `CPCliCod`, `DSRFAANO`, `DSRFMMES`
- `DSRFM2` (Duplicate): `CMEmpCod`, `CMFilCod`, `CPCliCod`, `DSRFAANO`
- `DSRFM3` (Duplicate): `DSRFAANO`, `DSRFMMES`

---

### 📌 DSRMC
- **Descrição:** Resultado mensal por Cartão
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`, `DSRMCCCrCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `DSRAnAno` | `N/D` | - |
| `DSRAnVl_VdaBrt` | `N/D` | - |
| `DSRAnVl_CusBrt` | `N/D` | - |
| `DSRAnVlrVdaLiq` | `N/D` | - |
| `CMEmpMoeCodPad` | `N/D` | - |
| `DSRAnVlrCusLiq` | `N/D` | - |
| `DSRAnResBrt` | `N/D` | - |
| `DSRAnMrgBrt` | `N/D` | - |
| `DSRAnVlrDsp` | `N/D` | - |
| `DSRAnDspFix` | `N/D` | - |
| `DSRAnDspVar` | `N/D` | - |
| `DSRAnDspInv` | `N/D` | - |
| `DSRAnResLiq` | `N/D` | - |
| `DSRAnPerSobVda` | `N/D` | - |
| `DSRAnVlrEst` | `N/D` | - |
| `DSRAnVlrCRe` | `N/D` | - |
| `DSRAnVlrCPg` | `N/D` | - |
| `DSRAnResFin` | `N/D` | - |
| `DSRAnSalBco` | `N/D` | - |
| `DSRAnVlrChqAbe` | `N/D` | - |
| `DSRAnDtaTrs` | `N/D` | - |
| `DSRAnFlaDel` | `N/D` | - |
| `DSRAnVlr_VdaCan` | `N/D` | - |
| `DSRAnVlr_CusCan` | `N/D` | - |
| `DSRAnVlrCCr` | `N/D` | - |
| `DSRAnVlrPreChqCR` | `N/D` | - |
| `DSRAnVlrRecCCr` | `N/D` | - |
| `DSRAnVlr_ProVda` | `N/D` | - |
| `DSRanProCus` | `N/D` | - |
| `DSRanProLuc` | `N/D` | - |
| `DSRAnVlrDesCom` | `N/D` | - |
| `DSRAnVlrAcrCom` | `N/D` | - |
| `DSRAnVlr_AbeCom` | `N/D` | - |
| `DSRAnRecCon` | `N/D` | - |
| `DSRAnVlrPgtCP` | `N/D` | - |
| `DSRAnDtaHorUltPro` | `N/D` | - |
| `DSRAnRecCrd` | `N/D` | - |
| `DSRAnLucDif` | `N/D` | - |
| `DSRAnLuc01` | `N/D` | - |
| `DSRAnLuc02` | `N/D` | - |
| `DSRMeMes` | `N/D` | - |
| `DSRMeDta` | `N/D` | - |
| `DSRMeCDta` | `N/D` | - |
| `DSRMeCHor` | `N/D` | - |
| `DSRMeCUsu` | `N/D` | - |
| `DSRMeCPrg` | `N/D` | - |
| `DSRMeVl_VdaBrt` | `N/D` | - |
| `DSRMeVl_CusBrt` | `N/D` | - |
| `DSRMeVlrVdaLiq` | `N/D` | - |
| `DSRMeVlrCusLiq` | `N/D` | - |
| `DSRMeResBrt` | `N/D` | - |
| `DSRMeMrgBrt` | `N/D` | - |
| `DSRMeVlrDsp` | `N/D` | - |
| `DSRMeDspFix` | `N/D` | - |
| `DSRMeDspVar` | `N/D` | - |
| `DSRMeDspInv` | `N/D` | - |
| `DSRMeResLiq` | `N/D` | - |
| `DSRMePerSobVda` | `N/D` | - |
| `DSRMeVlrEst` | `N/D` | - |
| `DSRMeVlr_EstCon` | `N/D` | - |
| `DSRMeVlrCRe` | `N/D` | - |
| `DSRMeVlrCPg` | `N/D` | - |
| `DSRMeVlrCCrPag` | `N/D` | - |
| `DSRMeVlrPreChqCR` | `N/D` | - |
| `DSRMeVlrChqAbeCC` | `N/D` | - |
| `DSRMeSalBco` | `N/D` | - |
| `DSRMeDtaTrs` | `N/D` | - |
| `DSRMeFlaDel` | `N/D` | - |
| `DSRMeResFin` | `N/D` | - |
| `DSRMeMoeCod` | `N/D` | - |
| `DSRMeVlr_VdaCan` | `N/D` | - |
| `DSRMeVlr_CusCan` | `N/D` | - |
| `DSRMeSts` | `N/D` | - |
| `DSRMeVlrRecCCr` | `N/D` | - |
| `DSRMeTotRec` | `N/D` | - |
| `DSRMeTotPag` | `N/D` | - |
| `DSRMeVlrParRec` | `N/D` | - |
| `DSRMeVlrJrsRecCre` | `N/D` | - |
| `DSRMeVlr_DscRecCre` | `N/D` | - |
| `DSRMeVlrCom` | `N/D` | - |
| `DSRMeVdaVis` | `N/D` | - |
| `DSRMeCusVis` | `N/D` | - |
| `DSRMePrcVis` | `N/D` | - |
| `DSRMeVdaCre` | `N/D` | - |
| `DSRMeCusCusCre` | `N/D` | - |
| `DSRMePrcCre` | `N/D` | - |
| `DSRMeVdaChqPre` | `N/D` | - |
| `DSRMeCusChqPre` | `N/D` | - |
| `DSRMePrcChqPre` | `N/D` | - |
| `DSRMeVdaCarCre` | `N/D` | - |
| `DSRMeCusCarCre` | `N/D` | - |
| `DSRMePrcCarCre` | `N/D` | - |
| `DSRMePrcFin` | `N/D` | - |
| `DSRMeVdaOut` | `N/D` | - |
| `DSRMeCusOut` | `N/D` | - |
| `DSRMePrcOut` | `N/D` | - |
| `DSRMeRCrAdi` | `N/D` | - |
| `DSRMeRCr0030Dia` | `N/D` | - |
| `DSRMeRCr3160Dia` | `N/D` | - |
| `DSRMeRCr6190Dia` | `N/D` | - |
| `DSRMeRCr91120Dia` | `N/D` | - |
| `DSRMeRCrMai120Dia` | `N/D` | - |
| `DSRMeRCrFunPer` | `N/D` | - |
| `DSRMeVlrFunPer` | `N/D` | - |
| `DSRMePAV0_10Dia` | `N/D` | - |
| `DSRMePAV1120Dia` | `N/D` | - |
| `DSRMePAV2130Dia` | `N/D` | - |
| `DSRMePAV3145Dia` | `N/D` | - |
| `DSRMePAV4660Dia` | `N/D` | - |
| `DSRMePAV0060Dia` | `N/D` | - |
| `DSRMePAV61120Dia` | `N/D` | - |
| `DSRMePAVMai120Dia` | `N/D` | - |
| `DSRMePAVTot` | `N/D` | - |
| `DSRMePAVPrc` | `N/D` | - |
| `DSRMePAA0_10Dia` | `N/D` | - |
| `DSRMePAA1120Dia` | `N/D` | - |
| `DSRMePAA2130Dia` | `N/D` | - |
| `DSRMePAA3145Dia` | `N/D` | - |
| `DSRMePAA4660Dia` | `N/D` | - |
| `DSRMePAA0060Dia` | `N/D` | - |
| `DSRMePAA61120Dia` | `N/D` | - |
| `DSRMePAAMai120Dia` | `N/D` | - |
| `DSRMePAATot` | `N/D` | - |
| `DSRMePAAPrc` | `N/D` | - |
| `DSRMeDifCreTrc` | `N/D` | - |
| `DSRMeDifEstTrc` | `N/D` | - |
| `DSRMeVlr_ProVda` | `N/D` | - |
| `DSRMEProCus` | `N/D` | - |
| `DSRMeProLuc` | `N/D` | - |
| `DSRMeVlrDesCom` | `N/D` | - |
| `DSRMeVlr_AbeCom` | `N/D` | - |
| `DSRMeRecCon` | `N/D` | - |
| `DSRMeVlrAcrCom` | `N/D` | - |
| `DSRMeDVP` | `N/D` | - |
| `DSRMeDVV` | `N/D` | - |
| `DSRMeDVC` | `N/D` | - |
| `DSRMeDVCPre` | `N/D` | - |
| `DSRMeTotDes` | `N/D` | - |
| `DSRMeVlrSemDscVda` | `N/D` | - |
| `DSRMeVrComDscVda` | `N/D` | - |
| `DSRMeVlrPgtCP` | `N/D` | - |
| `DSRMeVVCD` | `N/D` | - |
| `DSRMeCVCD` | `N/D` | - |
| `DSRMeVVSD` | `N/D` | - |
| `DSRMeCVSD` | `N/D` | - |
| `DSRMeVPCD` | `N/D` | - |
| `DSRMeCPCD` | `N/D` | - |
| `DSRMeVPSD` | `N/D` | - |
| `DSRMeCPSD` | `N/D` | - |
| `DSRMeVCCD` | `N/D` | - |
| `DSRMeCCCD` | `N/D` | - |
| `DSRMeVCSD` | `N/D` | - |
| `DSRMeCCSD` | `N/D` | - |
| `DSRMeVCQCD` | `N/D` | - |
| `DSRMeCCQCD` | `N/D` | - |
| `DSRMeVCQSD` | `N/D` | - |
| `DSRMeCCQSD` | `N/D` | - |
| `DSRMeVVP` | `N/D` | - |
| `DSRMeCVP` | `N/D` | - |
| `DSRMeVPP` | `N/D` | - |
| `DSRMeCPP` | `N/D` | - |
| `DSRMeVCP` | `N/D` | - |
| `DSRMeCCP` | `N/D` | - |
| `DSRMeVChP` | `N/D` | - |
| `DSRMeCChP` | `N/D` | - |
| `DSRMeVdaFin` | `N/D` | - |
| `DSRMeVlrMrg` | `N/D` | - |
| `DSRMeVlrMet` | `N/D` | - |
| `DSRMePrcMet` | `N/D` | - |
| `DSRMeQtdDiaTrb` | `N/D` | - |
| `DSRMeQtd_DiaUteMes` | `N/D` | - |
| `DSRMeVlr_MetPro` | `N/D` | - |
| `DSRMeDifVdaMet` | `N/D` | - |
| `DSRMePrcDspSobVda` | `N/D` | - |
| `DSRMeRCr0110Dia` | `N/D` | - |
| `DSRMeRCr1120Dia` | `N/D` | - |
| `DSRMeRCr2130Dia` | `N/D` | - |
| `DSRMERCr3045Dia` | `N/D` | - |
| `DSRMeRecChq` | `N/D` | - |
| `DSRMeRecCCr` | `N/D` | - |
| `DSRMeRecCrd` | `N/D` | - |
| `DSRMeChqPreMes` | `N/D` | - |
| `DSRMeVlrRct` | `N/D` | - |
| `DSRMeVlCPBco` | `N/D` | - |
| `DSRMeVlCPDin` | `N/D` | - |
| `DSRMeSalAntBco` | `N/D` | - |
| `DSRMeDifSalBco` | `N/D` | - |
| `DSRMeVlrAFP` | `N/D` | - |
| `DSRMEVlrFFP` | `N/D` | - |
| `DSRMESldIni` | `N/D` | - |
| `DSRMESldFin` | `N/D` | - |
| `DSRMEDspTot` | `N/D` | - |
| `DSRMERecTot` | `N/D` | - |
| `DSRMELucDif` | `N/D` | - |
| `DSRMELuc02` | `N/D` | - |
| `DSRMELuc01` | `N/D` | - |
| `DSRMCCCrCod` | `N/D` | - |
| `DSRMCVlrVda` | `N/D` | - |

#### 🗺️ Índices
- `DSRMC1` (Unique): `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`, `DSRMCCCrCod`
- `DSRMC2` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`

---

### 📌 DSRMD
- **Descrição:** Vendas Diárias
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`, `DSRMDDia`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `DSRAnAno` | `N/D` | - |
| `DSRAnVl_VdaBrt` | `N/D` | - |
| `DSRAnVl_CusBrt` | `N/D` | - |
| `DSRAnVlrVdaLiq` | `N/D` | - |
| `CMEmpMoeCodPad` | `N/D` | - |
| `DSRAnVlrCusLiq` | `N/D` | - |
| `DSRAnResBrt` | `N/D` | - |
| `DSRAnMrgBrt` | `N/D` | - |
| `DSRAnVlrDsp` | `N/D` | - |
| `DSRAnDspFix` | `N/D` | - |
| `DSRAnDspVar` | `N/D` | - |
| `DSRAnDspInv` | `N/D` | - |
| `DSRAnResLiq` | `N/D` | - |
| `DSRAnPerSobVda` | `N/D` | - |
| `DSRAnVlrEst` | `N/D` | - |
| `DSRAnVlrCRe` | `N/D` | - |
| `DSRAnVlrCPg` | `N/D` | - |
| `DSRAnResFin` | `N/D` | - |
| `DSRAnSalBco` | `N/D` | - |
| `DSRAnVlrChqAbe` | `N/D` | - |
| `DSRAnDtaTrs` | `N/D` | - |
| `DSRAnFlaDel` | `N/D` | - |
| `DSRAnVlr_VdaCan` | `N/D` | - |
| `DSRAnVlr_CusCan` | `N/D` | - |
| `DSRAnVlrCCr` | `N/D` | - |
| `DSRAnVlrPreChqCR` | `N/D` | - |
| `DSRAnVlrRecCCr` | `N/D` | - |
| `DSRAnVlr_ProVda` | `N/D` | - |
| `DSRanProCus` | `N/D` | - |
| `DSRanProLuc` | `N/D` | - |
| `DSRAnVlrDesCom` | `N/D` | - |
| `DSRAnVlrAcrCom` | `N/D` | - |
| `DSRAnVlr_AbeCom` | `N/D` | - |
| `DSRAnRecCon` | `N/D` | - |
| `DSRAnVlrPgtCP` | `N/D` | - |
| `DSRAnDtaHorUltPro` | `N/D` | - |
| `DSRAnRecCrd` | `N/D` | - |
| `DSRAnLucDif` | `N/D` | - |
| `DSRAnLuc01` | `N/D` | - |
| `DSRAnLuc02` | `N/D` | - |
| `DSRMeMes` | `N/D` | - |
| `DSRMeDta` | `N/D` | - |
| `DSRMeCDta` | `N/D` | - |
| `DSRMeCHor` | `N/D` | - |
| `DSRMeCUsu` | `N/D` | - |
| `DSRMeCPrg` | `N/D` | - |
| `DSRMeVl_VdaBrt` | `N/D` | - |
| `DSRMeVl_CusBrt` | `N/D` | - |
| `DSRMeVlrVdaLiq` | `N/D` | - |
| `DSRMeVlrCusLiq` | `N/D` | - |
| `DSRMeResBrt` | `N/D` | - |
| `DSRMeMrgBrt` | `N/D` | - |
| `DSRMeVlrDsp` | `N/D` | - |
| `DSRMeDspFix` | `N/D` | - |
| `DSRMeDspVar` | `N/D` | - |
| `DSRMeDspInv` | `N/D` | - |
| `DSRMeResLiq` | `N/D` | - |
| `DSRMePerSobVda` | `N/D` | - |
| `DSRMeVlrEst` | `N/D` | - |
| `DSRMeVlr_EstCon` | `N/D` | - |
| `DSRMeVlrCRe` | `N/D` | - |
| `DSRMeVlrCPg` | `N/D` | - |
| `DSRMeVlrCCrPag` | `N/D` | - |
| `DSRMeVlrPreChqCR` | `N/D` | - |
| `DSRMeVlrChqAbeCC` | `N/D` | - |
| `DSRMeSalBco` | `N/D` | - |
| `DSRMeDtaTrs` | `N/D` | - |
| `DSRMeFlaDel` | `N/D` | - |
| `DSRMeResFin` | `N/D` | - |
| `DSRMeMoeCod` | `N/D` | - |
| `DSRMeVlr_VdaCan` | `N/D` | - |
| `DSRMeVlr_CusCan` | `N/D` | - |
| `DSRMeSts` | `N/D` | - |
| `DSRMeVlrRecCCr` | `N/D` | - |
| `DSRMeTotRec` | `N/D` | - |
| `DSRMeTotPag` | `N/D` | - |
| `DSRMeVlrParRec` | `N/D` | - |
| `DSRMeVlrJrsRecCre` | `N/D` | - |
| `DSRMeVlr_DscRecCre` | `N/D` | - |
| `DSRMeVlrCom` | `N/D` | - |
| `DSRMeVdaVis` | `N/D` | - |
| `DSRMeCusVis` | `N/D` | - |
| `DSRMePrcVis` | `N/D` | - |
| `DSRMeVdaCre` | `N/D` | - |
| `DSRMeCusCusCre` | `N/D` | - |
| `DSRMePrcCre` | `N/D` | - |
| `DSRMeVdaChqPre` | `N/D` | - |
| `DSRMeCusChqPre` | `N/D` | - |
| `DSRMePrcChqPre` | `N/D` | - |
| `DSRMeVdaCarCre` | `N/D` | - |
| `DSRMeCusCarCre` | `N/D` | - |
| `DSRMePrcCarCre` | `N/D` | - |
| `DSRMePrcFin` | `N/D` | - |
| `DSRMeVdaOut` | `N/D` | - |
| `DSRMeCusOut` | `N/D` | - |
| `DSRMePrcOut` | `N/D` | - |
| `DSRMeRCrAdi` | `N/D` | - |
| `DSRMeRCr0030Dia` | `N/D` | - |
| `DSRMeRCr3160Dia` | `N/D` | - |
| `DSRMeRCr6190Dia` | `N/D` | - |
| `DSRMeRCr91120Dia` | `N/D` | - |
| `DSRMeRCrMai120Dia` | `N/D` | - |
| `DSRMeRCrFunPer` | `N/D` | - |
| `DSRMeVlrFunPer` | `N/D` | - |
| `DSRMePAV0_10Dia` | `N/D` | - |
| `DSRMePAV1120Dia` | `N/D` | - |
| `DSRMePAV2130Dia` | `N/D` | - |
| `DSRMePAV3145Dia` | `N/D` | - |
| `DSRMePAV4660Dia` | `N/D` | - |
| `DSRMePAV0060Dia` | `N/D` | - |
| `DSRMePAV61120Dia` | `N/D` | - |
| `DSRMePAVMai120Dia` | `N/D` | - |
| `DSRMePAVTot` | `N/D` | - |
| `DSRMePAVPrc` | `N/D` | - |
| `DSRMePAA0_10Dia` | `N/D` | - |
| `DSRMePAA1120Dia` | `N/D` | - |
| `DSRMePAA2130Dia` | `N/D` | - |
| `DSRMePAA3145Dia` | `N/D` | - |
| `DSRMePAA4660Dia` | `N/D` | - |
| `DSRMePAA0060Dia` | `N/D` | - |
| `DSRMePAA61120Dia` | `N/D` | - |
| `DSRMePAAMai120Dia` | `N/D` | - |
| `DSRMePAATot` | `N/D` | - |
| `DSRMePAAPrc` | `N/D` | - |
| `DSRMeDifCreTrc` | `N/D` | - |
| `DSRMeDifEstTrc` | `N/D` | - |
| `DSRMeVlr_ProVda` | `N/D` | - |
| `DSRMEProCus` | `N/D` | - |
| `DSRMeProLuc` | `N/D` | - |
| `DSRMeVlrDesCom` | `N/D` | - |
| `DSRMeVlr_AbeCom` | `N/D` | - |
| `DSRMeRecCon` | `N/D` | - |
| `DSRMeVlrAcrCom` | `N/D` | - |
| `DSRMeDVP` | `N/D` | - |
| `DSRMeDVV` | `N/D` | - |
| `DSRMeDVC` | `N/D` | - |
| `DSRMeDVCPre` | `N/D` | - |
| `DSRMeTotDes` | `N/D` | - |
| `DSRMeVlrSemDscVda` | `N/D` | - |
| `DSRMeVrComDscVda` | `N/D` | - |
| `DSRMeVlrPgtCP` | `N/D` | - |
| `DSRMeVVCD` | `N/D` | - |
| `DSRMeCVCD` | `N/D` | - |
| `DSRMeVVSD` | `N/D` | - |
| `DSRMeCVSD` | `N/D` | - |
| `DSRMeVPCD` | `N/D` | - |
| `DSRMeCPCD` | `N/D` | - |
| `DSRMeVPSD` | `N/D` | - |
| `DSRMeCPSD` | `N/D` | - |
| `DSRMeVCCD` | `N/D` | - |
| `DSRMeCCCD` | `N/D` | - |
| `DSRMeVCSD` | `N/D` | - |
| `DSRMeCCSD` | `N/D` | - |
| `DSRMeVCQCD` | `N/D` | - |
| `DSRMeCCQCD` | `N/D` | - |
| `DSRMeVCQSD` | `N/D` | - |
| `DSRMeCCQSD` | `N/D` | - |
| `DSRMeVVP` | `N/D` | - |
| `DSRMeCVP` | `N/D` | - |
| `DSRMeVPP` | `N/D` | - |
| `DSRMeCPP` | `N/D` | - |
| `DSRMeVCP` | `N/D` | - |
| `DSRMeCCP` | `N/D` | - |
| `DSRMeVChP` | `N/D` | - |
| `DSRMeCChP` | `N/D` | - |
| `DSRMeVdaFin` | `N/D` | - |
| `DSRMeVlrMrg` | `N/D` | - |
| `DSRMeVlrMet` | `N/D` | - |
| `DSRMePrcMet` | `N/D` | - |
| `DSRMeQtdDiaTrb` | `N/D` | - |
| `DSRMeQtd_DiaUteMes` | `N/D` | - |
| `DSRMeVlr_MetPro` | `N/D` | - |
| `DSRMeDifVdaMet` | `N/D` | - |
| `DSRMePrcDspSobVda` | `N/D` | - |
| `DSRMeRCr0110Dia` | `N/D` | - |
| `DSRMeRCr1120Dia` | `N/D` | - |
| `DSRMeRCr2130Dia` | `N/D` | - |
| `DSRMERCr3045Dia` | `N/D` | - |
| `DSRMeRecChq` | `N/D` | - |
| `DSRMeRecCCr` | `N/D` | - |
| `DSRMeRecCrd` | `N/D` | - |
| `DSRMeChqPreMes` | `N/D` | - |
| `DSRMeVlrRct` | `N/D` | - |
| `DSRMeVlCPBco` | `N/D` | - |
| `DSRMeVlCPDin` | `N/D` | - |
| `DSRMeSalAntBco` | `N/D` | - |
| `DSRMeDifSalBco` | `N/D` | - |
| `DSRMeVlrAFP` | `N/D` | - |
| `DSRMEVlrFFP` | `N/D` | - |
| `DSRMESldIni` | `N/D` | - |
| `DSRMESldFin` | `N/D` | - |
| `DSRMEDspTot` | `N/D` | - |
| `DSRMERecTot` | `N/D` | - |
| `DSRMELucDif` | `N/D` | - |
| `DSRMELuc02` | `N/D` | - |
| `DSRMELuc01` | `N/D` | - |
| `DSRMDDia` | `N/D` | - |
| `DSRMDVlrVda` | `N/D` | - |
| `DSRMDVlrCus` | `N/D` | - |
| `DSRMDQtd` | `N/D` | - |
| `DSRMDMrg1` | `N/D` | - |
| `DSRMDVdaQtd` | `N/D` | - |

#### 🗺️ Índices
- `DSRMD1` (Unique): `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`, `DSRMDDia`
- `DSRMD2` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`

---

### 📌 DSRMe
- **Descrição:** Resultado Mensal
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `DSRAnAno` | `N/D` | - |
| `DSRAnVl_VdaBrt` | `N/D` | - |
| `DSRAnVl_CusBrt` | `N/D` | - |
| `DSRAnVlrVdaLiq` | `N/D` | - |
| `CMEmpMoeCodPad` | `N/D` | - |
| `DSRAnVlrCusLiq` | `N/D` | - |
| `DSRAnResBrt` | `N/D` | - |
| `DSRAnMrgBrt` | `N/D` | - |
| `DSRAnVlrDsp` | `N/D` | - |
| `DSRAnDspFix` | `N/D` | - |
| `DSRAnDspVar` | `N/D` | - |
| `DSRAnDspInv` | `N/D` | - |
| `DSRAnResLiq` | `N/D` | - |
| `DSRAnPerSobVda` | `N/D` | - |
| `DSRAnVlrEst` | `N/D` | - |
| `DSRAnVlrCRe` | `N/D` | - |
| `DSRAnVlrCPg` | `N/D` | - |
| `DSRAnResFin` | `N/D` | - |
| `DSRAnSalBco` | `N/D` | - |
| `DSRAnVlrChqAbe` | `N/D` | - |
| `DSRAnDtaTrs` | `N/D` | - |
| `DSRAnFlaDel` | `N/D` | - |
| `DSRAnVlr_VdaCan` | `N/D` | - |
| `DSRAnVlr_CusCan` | `N/D` | - |
| `DSRAnVlrCCr` | `N/D` | - |
| `DSRAnVlrPreChqCR` | `N/D` | - |
| `DSRAnVlrRecCCr` | `N/D` | - |
| `DSRAnVlr_ProVda` | `N/D` | - |
| `DSRanProCus` | `N/D` | - |
| `DSRanProLuc` | `N/D` | - |
| `DSRAnVlrDesCom` | `N/D` | - |
| `DSRAnVlrAcrCom` | `N/D` | - |
| `DSRAnVlr_AbeCom` | `N/D` | - |
| `DSRAnRecCon` | `N/D` | - |
| `DSRAnVlrPgtCP` | `N/D` | - |
| `DSRAnDtaHorUltPro` | `N/D` | - |
| `DSRAnRecCrd` | `N/D` | - |
| `DSRAnLucDif` | `N/D` | - |
| `DSRAnLuc01` | `N/D` | - |
| `DSRAnLuc02` | `N/D` | - |
| `DSRMeMes` | `N/D` | - |
| `DSRMeDta` | `N/D` | - |
| `DSRMeCDta` | `N/D` | - |
| `DSRMeCHor` | `N/D` | - |
| `DSRMeCUsu` | `N/D` | - |
| `DSRMeCPrg` | `N/D` | - |
| `DSRMeVl_VdaBrt` | `N/D` | - |
| `DSRMeVl_CusBrt` | `N/D` | - |
| `DSRMeVlrVdaLiq` | `N/D` | - |
| `DSRMeVlrCusLiq` | `N/D` | - |
| `DSRMeResBrt` | `N/D` | - |
| `DSRMeMrgBrt` | `N/D` | - |
| `DSRMeVlrDsp` | `N/D` | - |
| `DSRMeDspFix` | `N/D` | - |
| `DSRMeDspVar` | `N/D` | - |
| `DSRMeDspInv` | `N/D` | - |
| `DSRMeResLiq` | `N/D` | - |
| `DSRMePerSobVda` | `N/D` | - |
| `DSRMeVlrEst` | `N/D` | - |
| `DSRMeVlr_EstCon` | `N/D` | - |
| `DSRMeVlrCRe` | `N/D` | - |
| `DSRMeVlrCPg` | `N/D` | - |
| `DSRMeVlrCCrPag` | `N/D` | - |
| `DSRMeVlrPreChqCR` | `N/D` | - |
| `DSRMeVlrChqAbeCC` | `N/D` | - |
| `DSRMeSalBco` | `N/D` | - |
| `DSRMeDtaTrs` | `N/D` | - |
| `DSRMeFlaDel` | `N/D` | - |
| `DSRMeResFin` | `N/D` | - |
| `DSRMeMoeCod` | `N/D` | - |
| `DSRMeVlr_VdaCan` | `N/D` | - |
| `DSRMeVlr_CusCan` | `N/D` | - |
| `DSRMeSts` | `N/D` | - |
| `DSRMeVlrRecCCr` | `N/D` | - |
| `DSRMeTotRec` | `N/D` | - |
| `DSRMeTotPag` | `N/D` | - |
| `DSRMeVlrParRec` | `N/D` | - |
| `DSRMeVlrJrsRecCre` | `N/D` | - |
| `DSRMeVlr_DscRecCre` | `N/D` | - |
| `DSRMeVlrCom` | `N/D` | - |
| `DSRMeVdaVis` | `N/D` | - |
| `DSRMeCusVis` | `N/D` | - |
| `DSRMePrcVis` | `N/D` | - |
| `DSRMeVdaCre` | `N/D` | - |
| `DSRMeCusCusCre` | `N/D` | - |
| `DSRMePrcCre` | `N/D` | - |
| `DSRMeVdaChqPre` | `N/D` | - |
| `DSRMeCusChqPre` | `N/D` | - |
| `DSRMePrcChqPre` | `N/D` | - |
| `DSRMeVdaCarCre` | `N/D` | - |
| `DSRMeCusCarCre` | `N/D` | - |
| `DSRMePrcCarCre` | `N/D` | - |
| `DSRMePrcFin` | `N/D` | - |
| `DSRMeVdaOut` | `N/D` | - |
| `DSRMeCusOut` | `N/D` | - |
| `DSRMePrcOut` | `N/D` | - |
| `DSRMeRCrAdi` | `N/D` | - |
| `DSRMeRCr0030Dia` | `N/D` | - |
| `DSRMeRCr3160Dia` | `N/D` | - |
| `DSRMeRCr6190Dia` | `N/D` | - |
| `DSRMeRCr91120Dia` | `N/D` | - |
| `DSRMeRCrMai120Dia` | `N/D` | - |
| `DSRMeRCrFunPer` | `N/D` | - |
| `DSRMeVlrFunPer` | `N/D` | - |
| `DSRMePAV0_10Dia` | `N/D` | - |
| `DSRMePAV1120Dia` | `N/D` | - |
| `DSRMePAV2130Dia` | `N/D` | - |
| `DSRMePAV3145Dia` | `N/D` | - |
| `DSRMePAV4660Dia` | `N/D` | - |
| `DSRMePAV0060Dia` | `N/D` | - |
| `DSRMePAV61120Dia` | `N/D` | - |
| `DSRMePAVMai120Dia` | `N/D` | - |
| `DSRMePAVTot` | `N/D` | - |
| `DSRMePAVPrc` | `N/D` | - |
| `DSRMePAA0_10Dia` | `N/D` | - |
| `DSRMePAA1120Dia` | `N/D` | - |
| `DSRMePAA2130Dia` | `N/D` | - |
| `DSRMePAA3145Dia` | `N/D` | - |
| `DSRMePAA4660Dia` | `N/D` | - |
| `DSRMePAA0060Dia` | `N/D` | - |
| `DSRMePAA61120Dia` | `N/D` | - |
| `DSRMePAAMai120Dia` | `N/D` | - |
| `DSRMePAATot` | `N/D` | - |
| `DSRMePAAPrc` | `N/D` | - |
| `DSRMeDifCreTrc` | `N/D` | - |
| `DSRMeDifEstTrc` | `N/D` | - |
| `DSRMeVlr_ProVda` | `N/D` | - |
| `DSRMEProCus` | `N/D` | - |
| `DSRMeProLuc` | `N/D` | - |
| `DSRMeVlrDesCom` | `N/D` | - |
| `DSRMeVlr_AbeCom` | `N/D` | - |
| `DSRMeRecCon` | `N/D` | - |
| `DSRMeVlrAcrCom` | `N/D` | - |
| `DSRMeDVP` | `N/D` | - |
| `DSRMeDVV` | `N/D` | - |
| `DSRMeDVC` | `N/D` | - |
| `DSRMeDVCPre` | `N/D` | - |
| `DSRMeTotDes` | `N/D` | - |
| `DSRMeVlrSemDscVda` | `N/D` | - |
| `DSRMeVrComDscVda` | `N/D` | - |
| `DSRMeVlrPgtCP` | `N/D` | - |
| `DSRMeVVCD` | `N/D` | - |
| `DSRMeCVCD` | `N/D` | - |
| `DSRMeVVSD` | `N/D` | - |
| `DSRMeCVSD` | `N/D` | - |
| `DSRMeVPCD` | `N/D` | - |
| `DSRMeCPCD` | `N/D` | - |
| `DSRMeVPSD` | `N/D` | - |
| `DSRMeCPSD` | `N/D` | - |
| `DSRMeVCCD` | `N/D` | - |
| `DSRMeCCCD` | `N/D` | - |
| `DSRMeVCSD` | `N/D` | - |
| `DSRMeCCSD` | `N/D` | - |
| `DSRMeVCQCD` | `N/D` | - |
| `DSRMeCCQCD` | `N/D` | - |
| `DSRMeVCQSD` | `N/D` | - |
| `DSRMeCCQSD` | `N/D` | - |
| `DSRMeVVP` | `N/D` | - |
| `DSRMeCVP` | `N/D` | - |
| `DSRMeVPP` | `N/D` | - |
| `DSRMeCPP` | `N/D` | - |
| `DSRMeVCP` | `N/D` | - |
| `DSRMeCCP` | `N/D` | - |
| `DSRMeVChP` | `N/D` | - |
| `DSRMeCChP` | `N/D` | - |
| `DSRMeVdaFin` | `N/D` | - |
| `DSRMeVlrMrg` | `N/D` | - |
| `DSRMeVlrMet` | `N/D` | - |
| `DSRMePrcMet` | `N/D` | - |
| `DSRMeQtdDiaTrb` | `N/D` | - |
| `DSRMeQtd_DiaUteMes` | `N/D` | - |
| `DSRMeVlr_MetPro` | `N/D` | - |
| `DSRMeDifVdaMet` | `N/D` | - |
| `DSRMePrcDspSobVda` | `N/D` | - |
| `DSRMeRCr0110Dia` | `N/D` | - |
| `DSRMeRCr1120Dia` | `N/D` | - |
| `DSRMeRCr2130Dia` | `N/D` | - |
| `DSRMERCr3045Dia` | `N/D` | - |
| `DSRMeRecChq` | `N/D` | - |
| `DSRMeRecCCr` | `N/D` | - |
| `DSRMeRecCrd` | `N/D` | - |
| `DSRMeChqPreMes` | `N/D` | - |
| `DSRMeVlrRct` | `N/D` | - |
| `DSRMeVlCPBco` | `N/D` | - |
| `DSRMeVlCPDin` | `N/D` | - |
| `DSRMeSalAntBco` | `N/D` | - |
| `DSRMeDifSalBco` | `N/D` | - |
| `DSRMeVlrAFP` | `N/D` | - |
| `DSRMEVlrFFP` | `N/D` | - |
| `DSRMESldIni` | `N/D` | - |
| `DSRMESldFin` | `N/D` | - |
| `DSRMEDspTot` | `N/D` | - |
| `DSRMERecTot` | `N/D` | - |
| `DSRMELucDif` | `N/D` | - |
| `DSRMELuc02` | `N/D` | - |
| `DSRMELuc01` | `N/D` | - |
| `DSRMeVlrLiqDsp` | `N/D` | - |
| `DSRMeVlCof` | `N/D` | - |
| `DSRMeVlrCxa` | `N/D` | - |
| `DSRMeVlRet` | `N/D` | - |
| `DSRMeVlrAju` | `N/D` | - |
| `DSRMeVlrAntBal` | `N/D` | - |
| `DSRMeVlrAtuBal` | `N/D` | - |
| `DSRMeVlrDifBal` | `N/D` | - |
| `DSRMeQtdCom` | `N/D` | - |
| `DSRMEQtdVen` | `N/D` | - |
| `DSRMeVlrEntCof` | `N/D` | - |
| `DSRMeDspDir` | `N/D` | - |
| `DSRMEOutCre` | `N/D` | - |
| `DSRMEOutDeb` | `N/D` | - |
| `DSRMECCrBan` | `N/D` | - |
| `DSRMEPOLNC` | `N/D` | - |
| `DSRMEPOVNC` | `N/D` | - |
| `DSRMEPOCNC` | `N/D` | - |
| `DSRMEPOORe` | `N/D` | - |
| `DSRMeVdaDeb` | `N/D` | - |
| `DSRMeVdaPix` | `N/D` | - |
| `DSRMeTotCar` | `N/D` | - |
| `DSRMeObs1` | `N/D` | - |
| `DSRMeObs2` | `N/D` | - |
| `DSRMeObs3` | `N/D` | - |
| `DSRMeObs4` | `N/D` | - |
| `DSRMeObs5` | `N/D` | - |
| `DSRMeDtaIni` | `N/D` | - |
| `DSRMeDtaFin` | `N/D` | - |

#### 🗺️ Índices
- `DSRMe1` (Unique): `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`
- `DSRMe2` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSRAnAno`
- `DSRMe3` (Duplicate): `CMEmpCod`, `DSRAnAno`, `DSRMeMes`
- `DSRMe6` (Duplicate): `CMEmpCod`, `DSRMeMes`, `DSRAnAno`

---

### 📌 DSRMG
- **Descrição:** Resultado Mensal por Grupo
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`, `DSRMGCodGrp`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `DSRAnAno` | `N/D` | - |
| `DSRMeMes` | `N/D` | - |
| `DSRMGCodGrp` | `N/D` | - |
| `DSRMGVlrVda` | `N/D` | - |
| `DSRMGVlrCus` | `N/D` | - |
| `DSRMGPerVda` | `N/D` | - |
| `DSRMGMrg1` | `N/D` | - |
| `DSRMGMrg2` | `N/D` | - |
| `DSRMGChqVlr` | `N/D` | - |
| `DSRMGChqCus` | `N/D` | - |
| `DSRMGChq1Mrg` | `N/D` | - |
| `DSRMGChq2Mrg` | `N/D` | - |
| `DSRMGVisVlr` | `N/D` | - |
| `DSRMGVisCus` | `N/D` | - |
| `DSRMGVis1Mrg` | `N/D` | - |
| `DSRMGVis2Mrg` | `N/D` | - |
| `DSRMGPrzVlr` | `N/D` | - |
| `DSRMGPrzCus` | `N/D` | - |
| `DSRMGPrz1Mrg` | `N/D` | - |
| `DSRMGPrz2Mrg` | `N/D` | - |
| `DSRMGCarVlr` | `N/D` | - |
| `DSRMGCarCus` | `N/D` | - |
| `DSRMGCar1Mrg` | `N/D` | - |
| `DSRMGCar2Mrg` | `N/D` | - |
| `DSRMGPerChq` | `N/D` | - |
| `DSRMGPerVis` | `N/D` | - |
| `DSRMGPerPrz` | `N/D` | - |
| `DSRMGPerCar` | `N/D` | - |
| `DSRMGPerFin` | `N/D` | - |
| `DSRMGFinVlr` | `N/D` | - |
| `DSRMGFinCus` | `N/D` | - |
| `DSRMGFin1Mrg` | `N/D` | - |
| `DSRMGFin2Mrg` | `N/D` | - |
| `DSRMGPerOut` | `N/D` | - |
| `DSRMGOutVlr` | `N/D` | - |
| `DSRMGOutCus` | `N/D` | - |
| `DSRMGOut1Mrg` | `N/D` | - |
| `DSRMGOut2Mrg` | `N/D` | - |
| `DSRMGQtd` | `N/D` | - |

#### 🗺️ Índices
- `DSRMG1` (Unique): `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`, `DSRMGCodGrp`
- `DSRMG2` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`

---

### 📌 DSRMS
- **Descrição:** Resultado Mensal por Subgrupo
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`, `DSRMGCodGrp`, `DSRMSCodSgr`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `DSRAnAno` | `N/D` | - |
| `DSRMeMes` | `N/D` | - |
| `DSRMGCodGrp` | `N/D` | - |
| `DSRMGVlrVda` | `N/D` | - |
| `DSRMGVlrCus` | `N/D` | - |
| `DSRMGPerVda` | `N/D` | - |
| `DSRMGMrg1` | `N/D` | - |
| `DSRMGMrg2` | `N/D` | - |
| `DSRMGChqVlr` | `N/D` | - |
| `DSRMGChqCus` | `N/D` | - |
| `DSRMGChq1Mrg` | `N/D` | - |
| `DSRMGChq2Mrg` | `N/D` | - |
| `DSRMGVisVlr` | `N/D` | - |
| `DSRMGVisCus` | `N/D` | - |
| `DSRMGVis1Mrg` | `N/D` | - |
| `DSRMGVis2Mrg` | `N/D` | - |
| `DSRMGPrzVlr` | `N/D` | - |
| `DSRMGPrzCus` | `N/D` | - |
| `DSRMGPrz1Mrg` | `N/D` | - |
| `DSRMGPrz2Mrg` | `N/D` | - |
| `DSRMGCarVlr` | `N/D` | - |
| `DSRMGCarCus` | `N/D` | - |
| `DSRMGCar1Mrg` | `N/D` | - |
| `DSRMGCar2Mrg` | `N/D` | - |
| `DSRMGPerChq` | `N/D` | - |
| `DSRMGPerVis` | `N/D` | - |
| `DSRMGPerPrz` | `N/D` | - |
| `DSRMGPerCar` | `N/D` | - |
| `DSRMGPerFin` | `N/D` | - |
| `DSRMGFinVlr` | `N/D` | - |
| `DSRMGFinCus` | `N/D` | - |
| `DSRMGFin1Mrg` | `N/D` | - |
| `DSRMGFin2Mrg` | `N/D` | - |
| `DSRMGPerOut` | `N/D` | - |
| `DSRMGOutVlr` | `N/D` | - |
| `DSRMGOutCus` | `N/D` | - |
| `DSRMGOut1Mrg` | `N/D` | - |
| `DSRMGOut2Mrg` | `N/D` | - |
| `DSRMGQtd` | `N/D` | - |
| `DSRMSCodSgr` | `N/D` | - |
| `DSRMSVlrVda` | `N/D` | - |
| `DSRMSVlrCus` | `N/D` | - |
| `DSRMSPerVda` | `N/D` | - |
| `DSRMSPerGrp` | `N/D` | - |
| `DSRMSMrg1` | `N/D` | - |
| `DSRMSMrg2` | `N/D` | - |
| `DSRMSChqVlr` | `N/D` | - |
| `DSRMSChqCus` | `N/D` | - |
| `DSRMSChq1Mrg` | `N/D` | - |
| `DSRMSChq2Mrg` | `N/D` | - |
| `DSRMSVisVlr` | `N/D` | - |
| `DSRMSVisCus` | `N/D` | - |
| `DSRMSVis1Mrg` | `N/D` | - |
| `DSRMSVis2Mrg` | `N/D` | - |
| `DSRMSPrzVlr` | `N/D` | - |
| `DSRMSPrzCus` | `N/D` | - |
| `DSRMSPrz1Mrg` | `N/D` | - |
| `DSRMSPrz2Mrg` | `N/D` | - |
| `DSRMSCarVlr` | `N/D` | - |
| `DSRMSCarCus` | `N/D` | - |
| `DSRMSCar1Mrg` | `N/D` | - |
| `DSRMSCar2Mrg` | `N/D` | - |
| `DSRMSPerChq` | `N/D` | - |
| `DSRMSPerCar` | `N/D` | - |
| `DSRMSPerVis` | `N/D` | - |
| `DSRMSPerPrz` | `N/D` | - |
| `DSRMSPerFin` | `N/D` | - |
| `DSRMSPerOut` | `N/D` | - |
| `DSRMSFinVlr` | `N/D` | - |
| `DSRMSFinCus` | `N/D` | - |
| `DSRMSFin1Mrg` | `N/D` | - |
| `DSRMSFin2Mrg` | `N/D` | - |
| `DSRMSOutVlr` | `N/D` | - |
| `DSRMSOutCus` | `N/D` | - |
| `DSRMSOut1Mrg` | `N/D` | - |
| `DSRMSOut2Mrg` | `N/D` | - |
| `DSRMSQtd` | `N/D` | - |

#### 🗺️ Índices
- `DSRMS1` (Unique): `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`, `DSRMGCodGrp`, `DSRMSCodSgr`
- `DSRMS2` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSRAnAno`, `DSRMeMes`, `DSRMGCodGrp`

---

### 📌 DSRS1
- **Descrição:** Histórico Resumo  Grupo/SubGrupo/Despesa
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `DSRS1ANO`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `DSRS1ANO` | `N/D` | - |
| `DSRS1REC` | `N/D` | - |
| `DSRS1DSP` | `N/D` | - |
| `DSRS1Dif` | `N/D` | - |

#### 🗺️ Índices
- `DSRS1A` (Unique): `CMEmpCod`, `CMFilCod`, `DSRS1ANO`
- `DSRS1B` (Duplicate): `CMEmpCod`, `CMFilCod`
- `DSRS1C` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSRS1ANO`

---

### 📌 DSRS2
- **Descrição:** Resumo despesas por Ano\Mês
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `DSRS1ANO`, `DSRS2Mes`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `DSRS1ANO` | `N/D` | - |
| `DSRS1REC` | `N/D` | - |
| `DSRS1DSP` | `N/D` | - |
| `DSRS1Dif` | `N/D` | - |
| `DSRS2Mes` | `N/D` | - |
| `DSRS2Rec` | `N/D` | - |
| `DSRS2Dsp` | `N/D` | - |
| `DSRS2Dif` | `N/D` | - |

#### 🗺️ Índices
- `DSRS2A` (Unique): `CMEmpCod`, `CMFilCod`, `DSRS1ANO`, `DSRS2Mes`
- `DSRS2B` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSRS1ANO`

---

### 📌 DSRS3
- **Descrição:** Resumo despesas por Ano\Mês\Grupo
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `DSRS1ANO`, `DSRS2Mes`, `DSRS3GrpCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `DSRS1ANO` | `N/D` | - |
| `DSRS1REC` | `N/D` | - |
| `DSRS1DSP` | `N/D` | - |
| `DSRS1Dif` | `N/D` | - |
| `DSRS2Mes` | `N/D` | - |
| `DSRS2Rec` | `N/D` | - |
| `DSRS2Dsp` | `N/D` | - |
| `DSRS2Dif` | `N/D` | - |
| `DSRS3GrpCod` | `N/D` | - |
| `DSRS3GrpDes` | `N/D` | - |
| `DSRS3Rec` | `N/D` | - |
| `DSRS3Dsp` | `N/D` | - |
| `DSRS3Dif` | `N/D` | - |

#### 🗺️ Índices
- `DSRS3A` (Unique): `CMEmpCod`, `CMFilCod`, `DSRS1ANO`, `DSRS2Mes`, `DSRS3GrpCod`
- `DSRS3B` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSRS1ANO`, `DSRS2Mes`
- `DSRS3C` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSRS3GrpCod`, `DSRS1ANO`, `DSRS2Mes`

---

### 📌 DSRS4
- **Descrição:** Resumo despesas por Ano\Mês\Grupo\SubGrupo
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `DSRS1ANO`, `DSRS2Mes`, `DSRS3GrpCod`, `DSRS4SgrCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `DSRS1ANO` | `N/D` | - |
| `DSRS1REC` | `N/D` | - |
| `DSRS1DSP` | `N/D` | - |
| `DSRS1Dif` | `N/D` | - |
| `DSRS2Mes` | `N/D` | - |
| `DSRS2Rec` | `N/D` | - |
| `DSRS2Dsp` | `N/D` | - |
| `DSRS2Dif` | `N/D` | - |
| `DSRS3GrpCod` | `N/D` | - |
| `DSRS3GrpDes` | `N/D` | - |
| `DSRS3Rec` | `N/D` | - |
| `DSRS3Dsp` | `N/D` | - |
| `DSRS3Dif` | `N/D` | - |
| `DSRS4SgrCod` | `N/D` | - |
| `DSRS4SgrDes` | `N/D` | - |
| `DSRS4Rec` | `N/D` | - |
| `DSRS4Dsp` | `N/D` | - |
| `DSRS4Dif` | `N/D` | - |

#### 🗺️ Índices
- `DSRS4A` (Unique): `CMEmpCod`, `CMFilCod`, `DSRS1ANO`, `DSRS2Mes`, `DSRS3GrpCod`, `DSRS4SgrCod`
- `DSRS4B` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSRS1ANO`, `DSRS2Mes`, `DSRS3GrpCod`
- `DSRS4C` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSRS3GrpCod`, `DSRS4SgrCod`, `DSRS1ANO`, `DSRS2Mes`

---

### 📌 DSRS5
- **Descrição:** Resumo despesas por Ano\Mês\Grupo\SubGrupo\despesa
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `DSRS1ANO`, `DSRS2Mes`, `DSRS3GrpCod`, `DSRS4SgrCod`, `DSRS5DspCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `DSRS1ANO` | `N/D` | - |
| `DSRS1REC` | `N/D` | - |
| `DSRS1DSP` | `N/D` | - |
| `DSRS1Dif` | `N/D` | - |
| `DSRS2Mes` | `N/D` | - |
| `DSRS2Rec` | `N/D` | - |
| `DSRS2Dsp` | `N/D` | - |
| `DSRS2Dif` | `N/D` | - |
| `DSRS3GrpCod` | `N/D` | - |
| `DSRS3GrpDes` | `N/D` | - |
| `DSRS3Rec` | `N/D` | - |
| `DSRS3Dsp` | `N/D` | - |
| `DSRS3Dif` | `N/D` | - |
| `DSRS4SgrCod` | `N/D` | - |
| `DSRS4SgrDes` | `N/D` | - |
| `DSRS4Rec` | `N/D` | - |
| `DSRS4Dsp` | `N/D` | - |
| `DSRS4Dif` | `N/D` | - |
| `DSRS5DspCod` | `N/D` | - |
| `DSRS5DspDes` | `N/D` | - |
| `DSRS5Rec` | `N/D` | - |
| `DSRS5Dsp` | `N/D` | - |
| `DSRS5DtaIni` | `N/D` | - |
| `DSRS5Dif` | `N/D` | - |

#### 🗺️ Índices
- `DSRS5A` (Unique): `CMEmpCod`, `CMFilCod`, `DSRS1ANO`, `DSRS2Mes`, `DSRS3GrpCod`, `DSRS4SgrCod`, `DSRS5DspCod`
- `DSRS5B` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSRS1ANO`, `DSRS2Mes`, `DSRS3GrpCod`, `DSRS4SgrCod`
- `DSRS5C` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSRS5DtaIni`
- `DSRS5D` (Duplicate): `CMEmpCod`, `CMFilCod`, `DSRS5DspCod`, `DSRS1ANO`, `DSRS2Mes`

---

### 📌 DSSet
- **Descrição:** Setor de Aplicação
- **Chave Primária:** `CMEmpCod`, `DSSetCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `DSSetCod` | `N/D` | - |
| `DSSetDes` | `N/D` | - |
| `DSSetCUsu` | `N/D` | - |
| `DSSetCTst` | `N/D` | - |
| `DSSetCPrg` | `N/D` | - |
| `CMEmpDspSet` | `N/D` | - |
| `DSSetVeiPlc` | `N/D` | - |
| `DsSetVeiDes` | `N/D` | - |

#### 🗺️ Índices
- `DSSetA` (Unique): `CMEmpCod`, `DSSetCod`
- `DSSetB` (Duplicate): `CMEmpCod`
- `DSSetC` (Duplicate): `DSSetDes`

---

### 📌 DSSgr
- **Descrição:** Sub-Grupo de Despesa
- **Chave Primária:** `CMEmpCod`, `DSGrpCod`, `DSSgrCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `DSGrpCod` | `N/D` | - |
| `DSGrpDes` | `N/D` | - |
| `DSGrpCHor` | `N/D` | - |
| `DSGrpCDta` | `N/D` | - |
| `DSGrpCUsu` | `N/D` | - |
| `DSGrpCPrg` | `N/D` | - |
| `DSGrpPrxSgr` | `N/D` | - |
| `DSGrpFlaDel` | `N/D` | - |
| `DSGrpDtaTrs` | `N/D` | - |
| `DSSgrCod` | `N/D` | - |
| `DSSgrPerDes` | `N/D` | - |
| `DSSgrFlaDel` | `N/D` | - |
| `DSSgrDtaTrs` | `N/D` | - |
| `DSSgrDes` | `N/D` | - |
| `DSSgrIde` | `N/D` | - |
| `DSSgrVlr` | `N/D` | - |
| `DSSgrVeiPlc` | `N/D` | - |
| `DSSgrVeiDes` | `N/D` | - |

#### 🗺️ Índices
- `DSSgr1` (Unique): `CMEmpCod`, `DSGrpCod`, `DSSgrCod`
- `DSSgr2` (Duplicate): `CMEmpCod`, `DSGrpCod`
- `DSSgr3` (Duplicate): `DSSgrIde`

---

### 📌 FCMov1
- **Descrição:** Fluxo de Caixa 01
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `FCMovDta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `FCMovDta` | `N/D` | - |
| `FCMov1AuxSeq` | `N/D` | - |
| `FCMov1SalFim` | `N/D` | - |
| `FCMov1SalIni` | `N/D` | - |
| `FCMov1DtaTrs` | `N/D` | - |
| `FCMov1FlaDel` | `N/D` | - |
| `FCMov1DebDia` | `N/D` | - |
| `FCMov1CreDia` | `N/D` | - |

#### 🗺️ Índices
- `FCMov11` (Unique): `CMEmpCod`, `CMFilCod`, `FCMovDta`
- `FCMov12` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 FCMov2
- **Descrição:** Fluxo de Caixa 02
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `FCMovDta`, `FCMovSeq`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `FCMovDta` | `N/D` | - |
| `FCMovSeq` | `N/D` | - |
| `FCMov2VlrTot` | `N/D` | - |
| `FCMov2NroPar` | `N/D` | - |
| `FCMov2CDta` | `N/D` | - |
| `FCMov2CHor` | `N/D` | - |
| `FCMov2CUsu` | `N/D` | - |
| `FCMov2CPrg` | `N/D` | - |
| `FCMov2NroNf` | `N/D` | - |
| `FCMov2SerNf` | `N/D` | - |
| `FCMov2DtaNf` | `N/D` | - |
| `FCMov2TipNf` | `N/D` | - |
| `FCMov2Obs` | `N/D` | - |
| `FCMov2Sit` | `N/D` | - |
| `FCMov2CodCliFor` | `N/D` | - |
| `FCMov2DesCliFor` | `N/D` | - |
| `FCMov2DebCre` | `N/D` | - |
| `FCMov2DtaTrs` | `N/D` | - |
| `FCMov2FlaDel` | `N/D` | - |
| `FCMov2Obs2` | `N/D` | - |
| `FCMov2OrgCod` | `N/D` | - |
| `FCMov2OrgDta` | `N/D` | - |
| `FCMov2OrgSeq` | `N/D` | - |
| `FCMov2OrgAux` | `N/D` | - |

#### 🗺️ Índices
- `FCMov21` (Unique): `CMEmpCod`, `CMFilCod`, `FCMovDta`, `FCMovSeq`
- `FCMov22` (Duplicate): `CMEmpCod`, `CMFilCod`, `FCMovDta`

---

### 📌 FCSAn
- **Descrição:** Saldo do Fluxo Caixa Anual
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `FCSAn`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `FCSAn` | `N/D` | - |
| `FCSAnCHor` | `N/D` | - |
| `FCSAnCUsu` | `N/D` | - |
| `FCSAnCDta` | `N/D` | - |
| `FCSAnCPrg` | `N/D` | - |
| `FCSAnEntVlr` | `N/D` | - |
| `FCSAnSaiVlr` | `N/D` | - |
| `FCSAnSalAtu` | `N/D` | - |
| `FCSAnAntSal` | `N/D` | - |

#### 🗺️ Índices
- `FCSAn1` (Unique): `CMEmpCod`, `CMFilCod`, `FCSAn`
- `FCSAn2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 FCSMe
- **Descrição:** Saldo do Fluxo de Caixa Mensal
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `FCSAn`, `FCSMe`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `FCSAn` | `N/D` | - |
| `FCSAnCHor` | `N/D` | - |
| `FCSAnCUsu` | `N/D` | - |
| `FCSAnCDta` | `N/D` | - |
| `FCSAnCPrg` | `N/D` | - |
| `FCSAnEntVlr` | `N/D` | - |
| `FCSAnSaiVlr` | `N/D` | - |
| `FCSAnSalAtu` | `N/D` | - |
| `FCSAnAntSal` | `N/D` | - |
| `FCSMe` | `N/D` | - |
| `FCSMeDta` | `N/D` | - |
| `FCSMeEntVlr` | `N/D` | - |
| `FCSMeSaiVlr` | `N/D` | - |
| `FCSMeSalAtu` | `N/D` | - |
| `FCSMeAntSal` | `N/D` | - |
| `FCSMeCDta` | `N/D` | - |
| `FCSMeCHor` | `N/D` | - |
| `FCSMeCUsu` | `N/D` | - |
| `FCSMeCPrg` | `N/D` | - |

#### 🗺️ Índices
- `FCSMe1` (Unique): `CMEmpCod`, `CMFilCod`, `FCSAn`, `FCSMe`
- `FCSMe2` (Duplicate): `CMEmpCod`, `CMFilCod`, `FCSAn`

---

### 📌 HTApt
- **Descrição:** Cadastro de Quartos
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `HTAptCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `HTAptCod` | `N/D` | - |
| `HTAptDes` | `N/D` | - |
| `HTAptUsu` | `N/D` | - |
| `HTAptTST` | `N/D` | - |
| `HTAptPrg` | `N/D` | - |
| `HTAptVlrInd` | `N/D` | - |
| `HTAptVlrApt` | `N/D` | - |
| `HTAptSts` | `N/D` | - |
| `HTAptDtaIni` | `N/D` | - |
| `HTAptDtaFin` | `N/D` | - |
| `HTAptDesRes` | `N/D` | - |

#### 🗺️ Índices
- `HTApt1` (Unique): `CMEmpCod`, `CMFilCod`, `HTAptCod`
- `HTApt2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 HTDAp
- **Descrição:** Movimento das Diárias dos Quartos
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `HTAptCod`, `HTDApDta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `HTAptCod` | `N/D` | - |
| `HTDApDta` | `N/D` | - |
| `HTAptDes` | `N/D` | - |
| `HTDApCodCli` | `N/D` | - |
| `HTDApDesCli` | `N/D` | - |
| `HTDApCliMan` | `N/D` | - |
| `HTDApDesMan` | `N/D` | - |
| `HTDApVlrApt` | `N/D` | - |
| `HTDApUsu` | `N/D` | - |
| `HTDApTST` | `N/D` | - |
| `HTDApPrg` | `N/D` | - |
| `HTDApSts` | `N/D` | - |
| `HTDApObs` | `N/D` | - |
| `HTDApQtdApt` | `N/D` | - |
| `HTDApQtdJan` | `N/D` | - |
| `HTDApQtdAlm` | `N/D` | - |
| `HTDApVlrInd` | `N/D` | - |
| `HTAptVlrInd` | `N/D` | - |
| `HTAptVlrApt` | `N/D` | - |
| `HTDApVlrCob` | `N/D` | - |
| `HTDApCalAut` | `N/D` | - |
| `HTDApVlrDes` | `N/D` | - |
| `HTDApMovDta` | `N/D` | - |
| `HTDApMovSeq` | `N/D` | - |
| `HTDApQtdDia` | `N/D` | - |
| `HTDApDtaFin` | `N/D` | - |
| `HTDApCnfEnt` | `N/D` | - |
| `HTDApStsPgt` | `N/D` | - |
| `HTDApDtaIni` | `N/D` | - |
| `HTDApUsuRes` | `N/D` | - |
| `HTDApTstRes` | `N/D` | - |
| `HTDapTotVlr` | `N/D` | - |
| `CMFilCli` | `N/D` | - |
| `HTDApObs2` | `N/D` | - |
| `HTDApObs3` | `N/D` | - |
| `HTDApTel` | `N/D` | - |
| `HTDApQtdPar` | `N/D` | - |
| `HTDapVctPriPar` | `N/D` | - |
| `HTDapDesDta` | `N/D` | - |
| `HTDAp1HosCod` | `N/D` | - |
| `HTDAp1HosNom` | `N/D` | - |
| `HTDAp2HosCod` | `N/D` | - |
| `HTDAp3HosCod` | `N/D` | - |
| `HTDAp4HosCod` | `N/D` | - |
| `HTDAp5HosCod` | `N/D` | - |
| `HTDAp6HosCod` | `N/D` | - |
| `HTDAp2HosNom` | `N/D` | - |
| `HTDAp3HosNom` | `N/D` | - |
| `HTDAp4HosNom` | `N/D` | - |
| `HTDAp5HosNom` | `N/D` | - |
| `HTDAp6HosNom` | `N/D` | - |
| `HTDap1VlrHos` | `N/D` | - |
| `HTDap2VlrHos` | `N/D` | - |
| `HTDap3VlrHos` | `N/D` | - |
| `HTDap4VlrHos` | `N/D` | - |
| `HTDap5VlrHos` | `N/D` | - |
| `HTDap6VlrHos` | `N/D` | - |
| `HTDapVlrTotHos` | `N/D` | - |
| `HTDapTotPar` | `N/D` | - |

#### 🗺️ Índices
- `HTDAp1` (Unique): `CMEmpCod`, `CMFilCod`, `HTAptCod`, `HTDApDta`
- `HTDAp2` (Duplicate): `CMEmpCod`, `CMFilCod`, `HTAptCod`
- `HTDAp3` (Duplicate): `HTDApSts`, `HTDApDta`
- `HTDAp4` (Duplicate): `HTDApDta`
- `HTDAp5` (Duplicate): `HTDApMovDta`, `HTDApMovSeq`

---

### 📌 HTDAV
- **Descrição:** Vencimento das Parcelas do Aluguel
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `HTAptCod`, `HTDApDta`, `HTDAVPar`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `HTAptCod` | `N/D` | - |
| `HTDApDta` | `N/D` | - |
| `HTAptDes` | `N/D` | - |
| `HTDApCodCli` | `N/D` | - |
| `HTDApDesCli` | `N/D` | - |
| `HTDApVlrCob` | `N/D` | - |
| `HTDApQtdDia` | `N/D` | - |
| `HTDApDtaFin` | `N/D` | - |
| `HTDApQtdPar` | `N/D` | - |
| `HTDapVctPriPar` | `N/D` | - |
| `HTDapDesDta` | `N/D` | - |
| `HTDapTotVlr` | `N/D` | - |
| `HTDapTotPar` | `N/D` | - |
| `HTDAVPar` | `N/D` | - |
| `HTDAVVct` | `N/D` | - |
| `HTDAVVlr` | `N/D` | - |

#### 🗺️ Índices
- `HTDAV1` (Unique): `CMEmpCod`, `CMFilCod`, `HTAptCod`, `HTDApDta`, `HTDAVPar`
- `HTDAV2` (Duplicate): `CMEmpCod`, `CMFilCod`, `HTAptCod`, `HTDApDta`

---

### 📌 HTPrm
- **Descrição:** Parâmetros do Hotel
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `HTPrmCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `HTPrmCod` | `N/D` | - |
| `HTPrmTST` | `N/D` | - |
| `HTPrmUSU` | `N/D` | - |
| `HTPrmPRG` | `N/D` | - |
| `HTPrmProCod` | `N/D` | - |
| `HTPrmProDes` | `N/D` | - |

#### 🗺️ Índices
- `HTPrm1` (Unique): `CMEmpCod`, `CMFilCod`, `HTPrmCod`
- `HTPrm2` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 IRMov2
- **Descrição:** Tabela de Pedidos da Irroba
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `IRMov2Id`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `IRMov2Id` | `N/D` | - |
| `IRMov2Data` | `N/D` | - |
| `IRMov2Total` | `N/D` | - |
| `IRMov2VlrDesc` | `N/D` | - |
| `IRMov2PerDesc` | `N/D` | - |
| `IRMov2Frt` | `N/D` | - |
| `IRMov2CStatus` | `N/D` | - |
| `IRMov2DStatus` | `N/D` | - |
| `IRMov2CliId` | `N/D` | - |
| `IRMov2TipCli` | `N/D` | - |
| `IRMov2FName` | `N/D` | - |
| `IRMov2LName` | `N/D` | - |
| `IRMov2ChvNfe` | `N/D` | - |
| `IRMov2EmiCNPJ` | `N/D` | - |
| `IRMov2NroNF` | `N/D` | - |
| `IRMov2XML1` | `N/D` | - |
| `IRMov2XML2` | `N/D` | - |
| `IRMov2XML3` | `N/D` | - |
| `IRMov2XML4` | `N/D` | - |
| `IRMov2XML5` | `N/D` | - |
| `IRMov2InvSts` | `N/D` | - |
| `IREmpCod` | `N/D` | - |
| `IRFilCod` | `N/D` | - |
| `IRMovDta` | `N/D` | - |
| `IRMovSeq` | `N/D` | - |
| `IRMov2CgcCpf` | `N/D` | - |
| `IRMov2RgIE` | `N/D` | - |
| `IRMov2Ema` | `N/D` | - |
| `IRMov2Tel1` | `N/D` | - |
| `IRMov2Tel2` | `N/D` | - |
| `IRMov2PEnd` | `N/D` | - |
| `IRMov2PNro` | `N/D` | - |
| `IRMov2PBai` | `N/D` | - |
| `IRMov2PCom` | `N/D` | - |
| `IRMov2PCid` | `N/D` | - |
| `IRMov2PCEP` | `N/D` | - |
| `IRMov2PZnId` | `N/D` | - |
| `IRMov2SEnd` | `N/D` | - |
| `IRMov2SNro` | `N/D` | - |
| `IRMov2SBai` | `N/D` | - |
| `IRMov2SCom` | `N/D` | - |
| `IRMov2SCid` | `N/D` | - |
| `IRMov2SCEP` | `N/D` | - |
| `IRMov2SZnId` | `N/D` | - |
| `IRMov2RetErro` | `N/D` | - |
| `IRMov2StsEnt` | `N/D` | - |

#### 🗺️ Índices
- `IRMov2A` (Unique): `CMEmpCod`, `CMFilCod`, `IRMov2Id`
- `IRMov2B` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 IRMov4
- **Descrição:** Itens de Pedido da Irroba
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `IRMov2Id`, `IRMov4Id`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `IRMov2Id` | `N/D` | - |
| `IRMov2Data` | `N/D` | - |
| `IRMov2Total` | `N/D` | - |
| `IRMov2VlrDesc` | `N/D` | - |
| `IRMov2PerDesc` | `N/D` | - |
| `IRMov2Frt` | `N/D` | - |
| `IRMov2CStatus` | `N/D` | - |
| `IRMov2DStatus` | `N/D` | - |
| `IRMov2CliId` | `N/D` | - |
| `IRMov2TipCli` | `N/D` | - |
| `IRMov2FName` | `N/D` | - |
| `IRMov2LName` | `N/D` | - |
| `IRMov2ChvNfe` | `N/D` | - |
| `IRMov2EmiCNPJ` | `N/D` | - |
| `IRMov2NroNF` | `N/D` | - |
| `IRMov2XML1` | `N/D` | - |
| `IRMov2XML2` | `N/D` | - |
| `IRMov2XML3` | `N/D` | - |
| `IRMov2XML4` | `N/D` | - |
| `IRMov2XML5` | `N/D` | - |
| `IRMov2InvSts` | `N/D` | - |
| `IREmpCod` | `N/D` | - |
| `IRFilCod` | `N/D` | - |
| `IRMovDta` | `N/D` | - |
| `IRMovSeq` | `N/D` | - |
| `IRMov2CgcCpf` | `N/D` | - |
| `IRMov2RgIE` | `N/D` | - |
| `IRMov2Ema` | `N/D` | - |
| `IRMov2Tel1` | `N/D` | - |
| `IRMov2Tel2` | `N/D` | - |
| `IRMov2PEnd` | `N/D` | - |
| `IRMov2PNro` | `N/D` | - |
| `IRMov2PBai` | `N/D` | - |
| `IRMov2PCom` | `N/D` | - |
| `IRMov2PCid` | `N/D` | - |
| `IRMov2PCEP` | `N/D` | - |
| `IRMov2PZnId` | `N/D` | - |
| `IRMov2SEnd` | `N/D` | - |
| `IRMov2SNro` | `N/D` | - |
| `IRMov2SBai` | `N/D` | - |
| `IRMov2SCom` | `N/D` | - |
| `IRMov2SCid` | `N/D` | - |
| `IRMov2SCEP` | `N/D` | - |
| `IRMov2SZnId` | `N/D` | - |
| `IRMov2RetErro` | `N/D` | - |
| `IRMov2StsEnt` | `N/D` | - |
| `IRMov4Id` | `N/D` | - |
| `IRMov4Qtd` | `N/D` | - |
| `IRMov4VrU` | `N/D` | - |
| `IRMov4CodPro` | `N/D` | - |
| `IRMov4DscPro` | `N/D` | - |

#### 🗺️ Índices
- `IRMov4A` (Unique): `CMEmpCod`, `CMFilCod`, `IRMov2Id`, `IRMov4Id`
- `IRMov4B` (Duplicate): `CMEmpCod`, `CMFilCod`, `IRMov2Id`

---

### 📌 KHClH
- **Descrição:** KHCl H
- **Chave Primária:** `KHEmpEmp`, `KHCliCod`, `KHClHTstLc`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `KHEmpEmp` | `N/D` | - |
| `KHCliCod` | `N/D` | - |
| `KHClHTstLc` | `N/D` | - |
| `KHClHTamBc` | `N/D` | - |
| `KHClHNFE` | `N/D` | - |
| `KHClHSat` | `N/D` | - |
| `KHClHVlrVd` | `N/D` | - |
| `KHClHDtaEx` | `N/D` | - |
| `KHClHVlrCu` | `N/D` | - |
| `KHClHObs` | `N/D` | - |
| `KHClHTipSi` | `N/D` | - |
| `KHClHTipLc` | `N/A(3)` | Tipos Lançamentos KHClH |
| `KHClHModRe` | `N/D` | - |
| `KHClHTef` | `N/D` | - |
| `KHClHSca` | `N/D` | - |
| `KHClHYan` | `N/D` | - |
| `KHClHUsu` | `N/D` | - |
| `KHClHPrg` | `N/D` | - |
| `KHClHUltTs` | `N/D` | - |
| `KHClHNroHD` | `N/D` | - |
| `KHFunNom` | `N/D` | - |
| `KHClHTst70` | `N/D` | - |
| `KHClHTst71` | `N/D` | - |
| `KHClHTst72` | `N/D` | - |
| `KHClHTst73` | `N/D` | - |
| `KHClHTst74` | `N/D` | - |
| `KHClHCha75` | `N/D` | - |
| `KHClHCha76` | `N/D` | - |
| `KHClHCha77` | `N/D` | - |
| `KHClHCha78` | `N/D` | - |
| `KHClHCha79` | `N/D` | - |
| `KHClHCha80` | `N/D` | - |
| `KHClHCha81` | `N/D` | - |
| `KHClHCha82` | `N/D` | - |
| `KHClHCha83` | `N/D` | - |
| `KHClHCha84` | `N/D` | - |
| `KHClHNro50` | `N/D` | - |
| `KHClHNro51` | `N/D` | - |
| `KHClHNro52` | `N/D` | - |
| `KHClHNro53` | `N/D` | - |
| `KHClHNro54` | `N/D` | - |
| `KHClHVlr55` | `N/D` | - |
| `KHClHVlr56` | `N/D` | - |
| `KHClHVlr57` | `N/D` | - |
| `KHClHVlr58` | `N/D` | - |
| `KHClHVlr59` | `N/D` | - |
| `KHClHVlr60` | `N/D` | - |
| `KHClHVlr61` | `N/D` | - |
| `KHClHVlr62` | `N/D` | - |
| `KHClHVlr63` | `N/D` | - |
| `KHClHVlr64` | `N/D` | - |
| `KHClHVar65` | `N/D` | - |
| `KHClHVar66` | `N/D` | - |
| `KHClHVar67` | `N/D` | - |
| `KHClHVar68` | `N/D` | - |
| `KHClHVar69` | `N/D` | - |

#### 🗺️ Índices
- `KHClH1` (Unique): `KHEmpEmp`, `KHCliCod`, `KHClHTstLc`
- `KHClH3` (Duplicate): `KHEmpEmp`, `KHCliCod`
- `KHClH4` (Duplicate): `KHEmpEmp`, `KHFunNom`
- `KHClH2` (Duplicate): `KHEmpEmp`, `KHCliCod`, `KHClHTstLc`
- `KHClH5` (Duplicate): `KHEmpEmp`, `KHFunNom`, `KHClHTstLc`
- `KHClH6` (Duplicate): `KHEmpEmp`, `KHClHTstLc`
- `KHClH7` (Duplicate): `KHEmpEmp`, `KHCliCod`, `KHClHTipLc`

---

### 📌 KHCli
- **Descrição:** KHCli
- **Chave Primária:** `KHEmpEmp`, `KHCliCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `KHEmpEmp` | `N/D` | - |
| `KHCliCod` | `N/D` | - |
| `KHCliRazSo` | `N/D` | - |
| `KHCliCnpj` | `N/D` | - |
| `KHCliTel` | `N/D` | - |
| `KHCliSts` | `N/D` | - |
| `KHCliDtaAt` | `N/D` | - |
| `KHCliMSRaz` | `N/D` | - |
| `KHCliMSCnp` | `N/D` | - |
| `KHCliFan` | `N/D` | - |
| `KHCliMSFan` | `N/D` | - |
| `KHCliLog` | `N/D` | - |
| `KHCliBckEr` | `N/D` | - |
| `KHCliBckDt` | `N/D` | - |
| `KHCliVlrMe` | `N/D` | - |
| `KHCliTipCo` | `N/D` | - |
| `KHCliCid` | `N/D` | - |
| `KHCliDtaFe` | `N/D` | - |
| `KHCliCha01` | `N/D` | - |
| `KHCliCha02` | `N/D` | - |
| `KHCliCha03` | `N/D` | - |
| `KHCliNro01` | `N/D` | - |
| `KHCliNro02` | `N/D` | - |
| `KHCliNro03` | `N/D` | - |
| `KHCliTst01` | `N/D` | - |
| `KHCliTst02` | `N/D` | - |
| `KHCliTst03` | `N/D` | - |
| `KHCliVar01` | `N/D` | - |
| `KHCliVar02` | `N/D` | - |
| `KHCliVar03` | `N/D` | - |
| `KHCliVlr01` | `N/D` | - |
| `KHCliVlr02` | `N/D` | - |
| `KHCliVlr03` | `N/D` | - |

#### 🗺️ Índices
- `KHCli1` (Unique): `KHEmpEmp`, `KHCliCod`
- `KHCli2` (Duplicate): `KHEmpEmp`

---

### 📌 KHEmp
- **Descrição:** Empresas KingHost
- **Chave Primária:** `KHEmpEmp`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `KHEmpEmp` | `N/D` | - |
| `KHEmpDBB` | `N/D` | - |
| `KHEmpDBM` | `N/D` | - |
| `KHEmpQtdCli` | `N/D` | - |
| `KHEmpDUP` | `N/D` | - |

#### 🗺️ Índices
- `KHEmp1` (Unique): `KHEmpEmp`

---

### 📌 KHFun
- **Descrição:** Funcionários da MSINFOR
- **Chave Primária:** `KHEmpEmp`, `KHFunNom`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `KHEmpEmp` | `N/D` | - |
| `KHFunNom` | `N/D` | - |
| `KHFunSen` | `N/D` | - |
| `KHFunObs` | `N/D` | - |

#### 🗺️ Índices
- `KHFun1` (Unique): `KHEmpEmp`, `KHFunNom`
- `IKHFun` (Duplicate): `KHEmpEmp`

---

### 📌 KHHAP
- **Descrição:** Histórico Acesso programa
- **Chave Primária:** `KHEmpEmp`, `KHCliCod`, `KHHAPPrg`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `KHEmpEmp` | `N/D` | - |
| `KHCliCod` | `N/D` | - |
| `KHHAPPrg` | `N/D` | - |
| `KHHAPDta` | `N/D` | - |
| `KHHAPQtd` | `N/D` | - |

#### 🗺️ Índices
- `IKHHAP` (Unique): `KHEmpEmp`, `KHCliCod`, `KHHAPPrg`
- `IKHHAP1` (Duplicate): `KHEmpEmp`, `KHCliCod`

---

### 📌 KHPar
- **Descrição:** KHPar
- **Chave Primária:** `KHEmpEmp`, `KHCliCod`, `KHParDta`, `KHParSeq`, `KHParPar`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `KHEmpEmp` | `N/D` | - |
| `KHCliCod` | `N/D` | - |
| `KHParDta` | `N/D` | - |
| `KHParSeq` | `N/D` | - |
| `KHParPar` | `N/D` | - |
| `KHParVlrAb` | `N/D` | - |
| `KHParVlrOr` | `N/D` | - |
| `KHParPgt` | `N/D` | - |
| `KHParVct` | `N/D` | - |
| `KHParSts` | `N/D` | - |
| `KHParPerMul` | `N/D` | - |
| `KHParPerJrs` | `N/D` | - |
| `KHParVlrMul` | `N/D` | - |
| `KHParVlrJrs` | `N/D` | - |
| `KHParVlrTot` | `N/D` | - |
| `KHParDiaAtr` | `N/D` | - |
| `KHParBxaJr` | `N/D` | - |
| `KHParBxaMu` | `N/D` | - |
| `KHParBxaTo` | `N/D` | - |
| `KHParUsuBx` | `N/D` | - |
| `KHParTst01` | `N/D` | - |
| `KHParTst02` | `N/D` | - |
| `KHParTst03` | `N/D` | - |
| `KHParCha01` | `N/D` | - |
| `KHParCha02` | `N/D` | - |
| `KHParCha03` | `N/D` | - |
| `KHParVlr01` | `N/D` | - |
| `KHParVlr02` | `N/D` | - |
| `KHParVlr03` | `N/D` | - |
| `KHParNro01` | `N/D` | - |
| `KHParNro02` | `N/D` | - |
| `KHParNro03` | `N/D` | - |
| `KHParVar01` | `N/D` | - |
| `KHParVar02` | `N/D` | - |
| `KHParVar03` | `N/D` | - |

#### 🗺️ Índices
- `PRIMARY` (Unique): `KHEmpEmp`, `KHCliCod`, `KHParDta`, `KHParSeq`, `KHParPar`
- `KHPar2` (Duplicate): `KHEmpEmp`, `KHCliCod`
- `KHPar3` (Duplicate): `KHEmpEmp`, `KHCliCod`, `KHParVct`
- `KHPAR4` (Duplicate): `KHEmpEmp`, `KHParSts`, `KHParVct`

---

### 📌 PDPCR
- **Descrição:** % q Cada Recebedor de Comissão
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `PDRprCod`, `PDRCoCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `PDRprCod` | `N/D` | - |
| `PDRprNom` | `N/D` | - |
| `PDRprTotPrcCom` | `N/D` | - |
| `PDRprSts` | `N/D` | - |
| `PDRCoCod` | `N/D` | - |
| `PDRCoNom` | `N/D` | - |
| `PDPCRPrc` | `N/D` | - |

#### 🗺️ Índices
- `PDPCRA` (Unique): `CMEmpCod`, `CMFilCod`, `PDRprCod`, `PDRCoCod`
- `PDPCRC` (Duplicate): `CMEmpCod`, `CMFilCod`, `PDRprCod`
- `PDPCRB` (Duplicate): `CMEmpCod`, `CMFilCod`, `PDRCoCod`

---

### 📌 PDPDB
- **Descrição:** Baixa Pedidos
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `PDPDCNro`, `PDPDiItem`, `PDPDNNro`, `PDPDBNroNot`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `PDPDCNro` | `N/D` | - |
| `PDRprCod` | `N/D` | - |
| `PDRepCod` | `N/D` | - |
| `PDPDCCliCod` | `N/D` | - |
| `PDPDCCliDes` | `N/D` | - |
| `PDRepNom` | `N/D` | - |
| `PDRprNom` | `N/D` | - |
| `PDPDCDta` | `N/D` | - |
| `PDPDCSts` | `N/D` | - |
| `PDPDCVlr` | `N/D` | - |
| `PDPDCQtd` | `N/D` | - |
| `PDPDCQtdSld` | `N/D` | - |
| `PDPDCQtdCan` | `N/D` | - |
| `PDPDCQtdEnt` | `N/D` | - |
| `PDPDiItem` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `PDPDIDif` | `N/D` | - |
| `PDPDIDtaPrvEnt` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `PDPDIDes` | `N/D` | - |
| `CEProPre1Tab` | `N/D` | - |
| `PDPDIQtd` | `N/D` | - |
| `PDPDIVlrUnt` | `N/D` | - |
| `PDPDIVLrTot` | `N/D` | - |
| `PDPDIQtdSld` | `N/D` | - |
| `PDPDIQtdCan` | `N/D` | - |
| `PDPDIQtdEnt` | `N/D` | - |
| `PDPDNNro` | `N/D` | - |
| `PDPDNQtd` | `N/D` | - |
| `PDPDNQtdSld` | `N/D` | - |
| `PDPDNQtdCan` | `N/D` | - |
| `PDPDNQtdEnt` | `N/D` | - |
| `PDPDNVlrUnt` | `N/D` | - |
| `PDPDNVlrTot` | `N/D` | - |
| `PDPDBNroNot` | `N/D` | - |
| `PDPDBDta` | `N/D` | - |
| `PDPDBQtdEnt` | `N/D` | - |
| `PDPDBQtdCan` | `N/D` | - |

#### 🗺️ Índices
- `PDPDBA` (Unique): `CMEmpCod`, `CMFilCod`, `PDPDCNro`, `PDPDiItem`, `PDPDNNro`, `PDPDBNroNot`
- `PDPDBB` (Duplicate): `CMEmpCod`, `CMFilCod`, `PDPDCNro`, `PDPDiItem`, `PDPDNNro`

---

### 📌 PDPDC
- **Descrição:** Cabecalho Pedidos
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `PDPDCNro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `PDPDCNro` | `N/D` | - |
| `PDRprCod` | `N/D` | - |
| `PDRepCod` | `N/D` | - |
| `PDPDCCliCod` | `N/D` | - |
| `PDPDCCliDes` | `N/D` | - |
| `PDRepNom` | `N/D` | - |
| `PDRprNom` | `N/D` | - |
| `PDPDCDta` | `N/D` | - |
| `PDPDCSts` | `N/D` | - |
| `PDPDCLocEnt` | `N/D` | - |
| `PDPDCTipEmb` | `N/D` | - |
| `PDPDCPrzPgt` | `N/D` | - |
| `PDPDCCifFob` | `N/D` | - |
| `PDPDCDiv` | `N/D` | - |
| `CMTraCod` | `N/D` | - |
| `CMTraRazSoc` | `N/D` | - |
| `PDPDCVlr` | `N/D` | - |
| `PDPDCQtd` | `N/D` | - |
| `PDPDCQtdSld` | `N/D` | - |
| `PDPDCQtdCan` | `N/D` | - |
| `PDPDCQtdEnt` | `N/D` | - |
| `PDPDCObs1` | `N/D` | - |
| `PDPDCObs2` | `N/D` | - |

#### 🗺️ Índices
- `PDPDC1` (Unique): `CMEmpCod`, `CMFilCod`, `PDPDCNro`
- `PDPDC2` (Duplicate): `CMTraCod`
- `PDPDC3` (Duplicate): `CMEmpCod`, `CMFilCod`, `PDRepCod`
- `PDPDC4` (Duplicate): `CMEmpCod`, `CMFilCod`, `PDRprCod`

---

### 📌 PDPDI
- **Descrição:** Itens Pedido
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `PDPDCNro`, `PDPDiItem`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `PDPDCNro` | `N/D` | - |
| `PDRprCod` | `N/D` | - |
| `PDRepCod` | `N/D` | - |
| `PDPDCCliCod` | `N/D` | - |
| `PDPDCCliDes` | `N/D` | - |
| `PDRepNom` | `N/D` | - |
| `PDRprNom` | `N/D` | - |
| `PDPDCDta` | `N/D` | - |
| `PDPDCSts` | `N/D` | - |
| `PDPDCLocEnt` | `N/D` | - |
| `PDPDCTipEmb` | `N/D` | - |
| `PDPDCPrzPgt` | `N/D` | - |
| `PDPDCCifFob` | `N/D` | - |
| `PDPDCDiv` | `N/D` | - |
| `CMTraCod` | `N/D` | - |
| `CMTraRazSoc` | `N/D` | - |
| `PDPDCVlr` | `N/D` | - |
| `PDPDCQtd` | `N/D` | - |
| `PDPDCQtdSld` | `N/D` | - |
| `PDPDCQtdCan` | `N/D` | - |
| `PDPDCQtdEnt` | `N/D` | - |
| `PDPDCObs1` | `N/D` | - |
| `PDPDCObs2` | `N/D` | - |
| `PDPDiItem` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `PDPDIDif` | `N/D` | - |
| `PDPDIDtaPrvEnt` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `PDPDIDes` | `N/D` | - |
| `CEProPre1Tab` | `N/D` | - |
| `PDPDICorApr` | `N/D` | - |
| `PDPDIQtd` | `N/D` | - |
| `PDPDIVlrUnt` | `N/D` | - |
| `PDPDIVLrTot` | `N/D` | - |
| `PDPDIQtdSld` | `N/D` | - |
| `PDPDIQtdCan` | `N/D` | - |
| `PDPDIQtdEnt` | `N/D` | - |

#### 🗺️ Índices
- `PDPDIA` (Unique): `CMEmpCod`, `CMFilCod`, `PDPDCNro`, `PDPDiItem`
- `PDPDIB` (Duplicate): `CMEmpCod`, `CEProCod`
- `PDPDIC` (Duplicate): `CMEmpCod`, `CMFilCod`, `PDPDCNro`

---

### 📌 PDPDN
- **Descrição:** Pedido por Numeração
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `PDPDCNro`, `PDPDiItem`, `PDPDNNro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `PDPDCNro` | `N/D` | - |
| `PDRprCod` | `N/D` | - |
| `PDRepCod` | `N/D` | - |
| `PDPDCCliCod` | `N/D` | - |
| `PDPDCCliDes` | `N/D` | - |
| `PDRepNom` | `N/D` | - |
| `PDRprNom` | `N/D` | - |
| `PDPDCDta` | `N/D` | - |
| `PDPDCSts` | `N/D` | - |
| `PDPDCLocEnt` | `N/D` | - |
| `PDPDCTipEmb` | `N/D` | - |
| `PDPDCPrzPgt` | `N/D` | - |
| `PDPDCCifFob` | `N/D` | - |
| `PDPDCDiv` | `N/D` | - |
| `CMTraCod` | `N/D` | - |
| `CMTraRazSoc` | `N/D` | - |
| `PDPDCVlr` | `N/D` | - |
| `PDPDCQtd` | `N/D` | - |
| `PDPDCQtdSld` | `N/D` | - |
| `PDPDCQtdCan` | `N/D` | - |
| `PDPDCQtdEnt` | `N/D` | - |
| `PDPDCObs1` | `N/D` | - |
| `PDPDCObs2` | `N/D` | - |
| `PDPDiItem` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `PDPDIDif` | `N/D` | - |
| `PDPDIDtaPrvEnt` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `PDPDIDes` | `N/D` | - |
| `CEProPre1Tab` | `N/D` | - |
| `PDPDICorApr` | `N/D` | - |
| `PDPDIQtd` | `N/D` | - |
| `PDPDIVlrUnt` | `N/D` | - |
| `PDPDIVLrTot` | `N/D` | - |
| `PDPDIQtdSld` | `N/D` | - |
| `PDPDIQtdCan` | `N/D` | - |
| `PDPDIQtdEnt` | `N/D` | - |
| `PDPDNNro` | `N/D` | - |
| `PDPDNQtd` | `N/D` | - |
| `PDPDNQtdSld` | `N/D` | - |
| `PDPDNQtdCan` | `N/D` | - |
| `PDPDNQtdEnt` | `N/D` | - |
| `PDPDNVlrUnt` | `N/D` | - |
| `PDPDNVlrTot` | `N/D` | - |

#### 🗺️ Índices
- `PDPDNA` (Unique): `CMEmpCod`, `CMFilCod`, `PDPDCNro`, `PDPDiItem`, `PDPDNNro`
- `PDPDNB` (Duplicate): `CMEmpCod`, `CMFilCod`, `PDPDCNro`, `PDPDiItem`

---

### 📌 PDRCo
- **Descrição:** Recebedores de Comissão
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `PDRCoCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `PDRCoCod` | `N/D` | - |
| `PDRCoNom` | `N/D` | - |

#### 🗺️ Índices
- `PRRCoA` (Unique): `CMEmpCod`, `CMFilCod`, `PDRCoCod`
- `PRRCoB` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 PDRep
- **Descrição:** Representantes
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `PDRepCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `PDRepCod` | `N/D` | - |
| `PDRepNom` | `N/D` | - |
| `PDRepSts` | `N/D` | - |

#### 🗺️ Índices
- `PDRepA` (Unique): `CMEmpCod`, `CMFilCod`, `PDRepCod`
- `PDRepB` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 PDRpr
- **Descrição:** Representadas
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `PDRprCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `PDRprCod` | `N/D` | - |
| `PDRprNom` | `N/D` | - |
| `PDRprTotPrcCom` | `N/D` | - |
| `PDRprSts` | `N/D` | - |

#### 🗺️ Índices
- `PDRprA` (Unique): `CMEmpCod`, `CMFilCod`, `PDRprCod`
- `PDRprB` (Duplicate): `CMEmpCod`, `CMFilCod`
- `PDRprC` (Duplicate): `PDRprNom`

---

### 📌 POBIT
- **Descrição:** Bicos - Intervenção Técnica
- **Chave Primária:** `POEmpCod`, `POBomCod`, `POBITNroInt`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `POBomCod` | `N/D` | - |
| `POBomDes` | `N/D` | - |
| `POBITNroInt` | `N/D` | - |
| `POBITDta` | `N/D` | - |
| `POBITMot` | `N/D` | - |
| `POBITNom` | `N/D` | - |
| `POBITCNPJ` | `N/D` | - |
| `POBITCPF` | `N/D` | - |

#### 🗺️ Índices
- `POBIT1` (Unique): `POEmpCod`, `POBomCod`, `POBITNroInt`
- `POBIT2` (Duplicate): `POEmpCod`, `POBomCod`

---

### 📌 POBom
- **Descrição:** Cadastro Bombas
- **Chave Primária:** `POEmpCod`, `POBomCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `POBomCod` | `N/D` | - |
| `POBomDes` | `N/D` | - |
| `POBomVlrUnt` | `N/D` | - |
| `POTCoCod` | `N/D` | - |
| `POBomTnqCod` | `N/D` | - |
| `POBomTnqDes` | `N/D` | - |
| `PoBomDesLMC` | `N/D` | - |
| `POBomCusUnt` | `N/D` | - |
| `POBomCanal` | `N/D` | - |
| `POBomCodPro` | `N/D` | - |
| `POBomDesPro` | `N/D` | - |
| `POBomEncer` | `N/D` | - |
| `POBomAtuEn` | `N/D` | - |
| `POBomSomar` | `N/D` | - |
| `POBomSts` | `N/D` | - |
| `POBomDtaSom` | `N/D` | - |
| `POBomLucMed` | `N/D` | - |

#### 🗺️ Índices
- `POBom1` (Unique): `POEmpCod`, `POBomCod`
- `POBom3` (Duplicate): `POEmpCod`
- `POBom2` (Duplicate): `POTCoCod`

---

### 📌 POBxB
- **Descrição:** Bombas x Bicos
- **Chave Primária:** `POEmpCod`, `POMBoCod`, `POBomCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `POMBoCod` | `N/D` | - |
| `POMBoDes` | `N/D` | - |
| `POMBoNroSer` | `N/D` | - |
| `POMBoNomFab` | `N/D` | - |
| `POMBoModBom` | `N/D` | - |
| `POMBoIdeMed` | `N/D` | - |
| `POBomCod` | `N/D` | - |
| `POBomDes` | `N/D` | - |
| `POBxBSts` | `N/D` | - |

#### 🗺️ Índices
- `POBxB1` (Unique): `POEmpCod`, `POMBoCod`, `POBomCod`
- `POBxB2` (Duplicate): `POEmpCod`, `POBomCod`
- `POBxB3` (Duplicate): `POEmpCod`, `POMBoCod`

---

### 📌 POCF1
- **Descrição:** Movimento POCF1
- **Chave Primária:** `POEmpCod`, `POCF1Tst`, `POCF1Regis`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `POCF1Tst` | `N/D` | - |
| `POCF1Regis` | `N/D` | - |
| `POCF1VlrCxa` | `N/D` | - |
| `POCF1Usu` | `N/D` | - |
| `POCF1VlrMov` | `N/D` | - |
| `POCF1VlrDsc` | `N/D` | - |
| `POCF1VlrAcr` | `N/D` | - |
| `POCF1VlrSal` | `N/D` | - |
| `POCF1TipMov` | `Character(1)` | Tipo Movimentos Caixa Frentista |
| `POCF1DesTipMov` | `N/D` | - |
| `POCF1Sts` | `N/D` | - |
| `POCF1TstFec` | `N/D` | - |
| `POCF1Obs` | `N/D` | - |
| `POCF1FilCod` | `N/D` | - |
| `POCF1DtaMov` | `N/D` | - |
| `POCF1SeqMov` | `N/D` | - |
| `POCF1IteMov` | `N/D` | - |
| `POCF1Prg` | `N/D` | - |
| `POCF1Bic` | `N/D` | - |
| `POCF1BomCod` | `N/D` | - |
| `POCF1ProCod` | `N/D` | - |
| `POCF1Qtd` | `N/D` | - |
| `POCF1VelIni` | `N/D` | - |
| `POCF1VelFin` | `N/D` | - |
| `POCF1VlrUnt` | `N/D` | - |
| `POCF1VlrBom` | `N/D` | - |
| `POCF1Idx` | `N/D` | - |
| `POCF1TstCon` | `N/D` | - |
| `POCF1Can` | `N/D` | - |
| `POCF1TstCan` | `N/D` | - |
| `POCF1UsuCan` | `N/D` | - |
| `POCF1Canal` | `N/D` | - |
| `POCF1DataA` | `N/D` | - |
| `POCF1HoraA` | `N/D` | - |
| `POCF1PUBom` | `N/D` | - |
| `POCF1ProDes` | `N/D` | - |
| `POCF1TipOrg` | `N/D` | - |
| `POCF1CusUnt` | `N/D` | - |
| `POCF1CusTot` | `N/D` | - |
| `POCF1VlrLuc` | `N/D` | - |
| `POCF1DCx` | `N/D` | - |
| `POCF1Mrg` | `N/D` | - |
| `POCF1VlrCCr` | `N/D` | - |
| `POCF1TipCCr` | `N/D` | - |
| `POCF1CarCnv` | `N/D` | - |
| `POCF1PECDscCen` | `N/D` | - |
| `POCF1VUF` | `N/D` | - |
| `POCF1VTF` | `N/D` | - |
| `POCF1NroNf` | `N/D` | - |
| `POCF1VDF` | `N/D` | - |
| `POCF1LibGer` | `N/D` | - |
| `POCF1VDFFak` | `N/D` | - |

#### 🗺️ Índices
- `POCF1A` (Unique): `POEmpCod`, `POCF1Tst`, `POCF1Regis`
- `POCF1B` (Duplicate): `POEmpCod`
- `POCF1C` (Duplicate): `POCF1Sts`, `POCF1TstFec`
- `POCF1D` (Duplicate): `POCF1Usu`, `POCF1Sts`, `POCF1Tst`
- `POCF1E` (Duplicate): `POCF1Idx`
- `POCF1F` (Duplicate): `POCF1Sts`, `POCF1Usu`, `POCF1TstCon`
- `POCF1G` (Duplicate): `POCF1DtaMov`, `POCF1SeqMov`
- `POCF1H` (Duplicate): `POCF1DCx`
- `POCF1I` (Duplicate): `POCF1Tst`, `POCF1Regis`

---

### 📌 POCF2
- **Descrição:** Resumo Caixa por Frentista
- **Chave Primária:** `POEmpCod`, `POCF2Usu`, `POCF2Tst`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `POCF2Usu` | `N/D` | - |
| `POCF2Tst` | `N/D` | - |
| `POCF2Prg` | `N/D` | - |
| `POCF2Sts` | `N/D` | - |
| `POCF2VlrFin` | `N/D` | - |
| `POCF2VlrMan` | `N/D` | - |
| `POCF2VlrDif` | `N/D` | - |
| `POCF2Idx` | `N/D` | - |
| `POCF2TSTFec` | `N/D` | - |
| `POCF2UsuFec` | `N/D` | - |
| `POCF2ImpCxa` | `N/D` | - |
| `POCF2VlrCof` | `N/D` | - |
| `POCF2VlrBom` | `N/D` | - |
| `POCF2VlrDes` | `N/D` | - |
| `POCF2DscPEC` | `N/D` | - |
| `POCF2CofVlrRea` | `N/D` | - |
| `POCF2Msg1` | `N/D` | - |
| `POCF2Msg2` | `N/D` | - |
| `POCF2Msg3` | `N/D` | - |
| `POCF2Msg4` | `N/D` | - |
| `POCF2Msg5` | `N/D` | - |
| `POCF2DCx` | `N/D` | - |
| `POCF2VlrRec` | `N/D` | - |
| `POCF2VlrBrtRec` | `N/D` | - |
| `POCF2RecCar` | `N/D` | - |
| `POCF2LucCom` | `N/D` | - |
| `POCF2Vlr1Can` | `N/D` | - |
| `POCF2VlrDsp` | `N/D` | - |
| `POCF2VlrCCr` | `N/D` | - |
| `POCF2VlrCLj` | `N/D` | - |
| `POCF2VlrCDe` | `N/D` | - |
| `POCF2VlrTip1` | `N/D` | - |
| `POCF2TotCar` | `N/D` | - |
| `POCF2VlrPix` | `N/D` | - |
| `POCF2CarPix` | `N/D` | - |
| `POCF2Vlr2Can` | `N/D` | - |
| `POCF2DifCof` | `N/D` | - |
| `POCF2Qtd2` | `N/D` | - |
| `POCF2Qtd5` | `N/D` | - |
| `POCF2Qtd10` | `N/D` | - |
| `POCF2Qtd20` | `N/D` | - |
| `POCF2Qtd50` | `N/D` | - |
| `POCF2Qt100` | `N/D` | - |
| `POCF2VlrChq` | `N/D` | - |
| `POCF2VlrMoe` | `N/D` | - |
| `POCF2Vlr2` | `N/D` | - |
| `POCF2Vlr5` | `N/D` | - |
| `POCF2Vlr10` | `N/D` | - |
| `POCF2Vlr20` | `N/D` | - |
| `POCF2Vlr50` | `N/D` | - |
| `POCF2Vl100` | `N/D` | - |
| `POCF2Vlr999` | `N/D` | - |

#### 🗺️ Índices
- `POCF2A` (Unique): `POEmpCod`, `POCF2Usu`, `POCF2Tst`
- `POCF2B` (Duplicate): `POEmpCod`
- `POCF2C` (Duplicate): `POCF2Idx`
- `POCF2D` (Duplicate): `POCF2Sts`, `POCF2Tst`
- `POCF2E` (Duplicate): `POCF2DCx`

---

### 📌 POCF3
- **Descrição:** Resumo dos Movimentos do Caixa do Frentista
- **Chave Primária:** `POEmpCod`, `POCF2Usu`, `POCF2Tst`, `POCF3TipMov`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `POCF2Usu` | `N/D` | - |
| `POCF2Tst` | `N/D` | - |
| `POCF2Prg` | `N/D` | - |
| `POCF2Sts` | `N/D` | - |
| `POCF2VlrFin` | `N/D` | - |
| `POCF2VlrMan` | `N/D` | - |
| `POCF2VlrDif` | `N/D` | - |
| `POCF2Idx` | `N/D` | - |
| `POCF2TSTFec` | `N/D` | - |
| `POCF2UsuFec` | `N/D` | - |
| `POCF2ImpCxa` | `N/D` | - |
| `POCF2VlrCof` | `N/D` | - |
| `POCF2VlrBom` | `N/D` | - |
| `POCF2VlrDes` | `N/D` | - |
| `POCF2DscPEC` | `N/D` | - |
| `POCF2CofVlrRea` | `N/D` | - |
| `POCF2Msg1` | `N/D` | - |
| `POCF2Msg2` | `N/D` | - |
| `POCF2Msg3` | `N/D` | - |
| `POCF2Msg4` | `N/D` | - |
| `POCF2Msg5` | `N/D` | - |
| `POCF2DCx` | `N/D` | - |
| `POCF2VlrRec` | `N/D` | - |
| `POCF2VlrBrtRec` | `N/D` | - |
| `POCF2RecCar` | `N/D` | - |
| `POCF2LucCom` | `N/D` | - |
| `POCF2Vlr1Can` | `N/D` | - |
| `POCF2VlrDsp` | `N/D` | - |
| `POCF2VlrCCr` | `N/D` | - |
| `POCF2VlrCLj` | `N/D` | - |
| `POCF2VlrCDe` | `N/D` | - |
| `POCF2VlrTip1` | `N/D` | - |
| `POCF2TotCar` | `N/D` | - |
| `POCF2VlrPix` | `N/D` | - |
| `POCF2CarPix` | `N/D` | - |
| `POCF2Vlr2Can` | `N/D` | - |
| `POCF3TipMov` | `N/D` | - |
| `POCF3VlrFin` | `N/D` | - |

#### 🗺️ Índices
- `POCF3A` (Unique): `POEmpCod`, `POCF2Usu`, `POCF2Tst`, `POCF3TipMov`
- `POCF3B` (Duplicate): `POEmpCod`, `POCF2Usu`, `POCF2Tst`
- `POCF3C` (Duplicate): `POCF2Tst`

---

### 📌 POCF4
- **Descrição:** Movimento POCF4 Gravado pelo Programa .Net
- **Chave Primária:** `POEmpCod`, `POCF4Tst`, `POCF4Regis`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `POCF4Tst` | `N/D` | - |
| `POCF4Regis` | `N/D` | - |
| `POCF4VlrCxa` | `N/D` | - |
| `POCF4Usu` | `N/D` | - |
| `POCF4VlrMov` | `N/D` | - |
| `POCF4VlrDsc` | `N/D` | - |
| `POCF4VlrAcr` | `N/D` | - |
| `POCF4VlrSal` | `N/D` | - |
| `POCF4TipMov` | `N/D` | - |
| `POCF4Sts` | `N/D` | - |
| `POCF4TstFec` | `N/D` | - |
| `POCF4Obs` | `N/D` | - |
| `POCF4FilCod` | `N/D` | - |
| `POCF4DtaMov` | `N/D` | - |
| `POCF4SeqMov` | `N/D` | - |
| `POCF4Prg` | `N/D` | - |
| `POCF4Bic` | `N/D` | - |
| `POCF4BomCod` | `N/D` | - |
| `POCF4ProCod` | `N/D` | - |
| `POCF4Qtd` | `N/D` | - |
| `POCF4VelIni` | `N/D` | - |
| `POCF4VelFin` | `N/D` | - |
| `POCF4VlrUnt` | `N/D` | - |
| `POCF4VlrBom` | `N/D` | - |
| `POCF4Idx` | `N/D` | - |
| `POCF4TstCon` | `N/D` | - |
| `POCF4Can` | `N/D` | - |
| `POCF4TstCan` | `N/D` | - |
| `POCF4UsuCan` | `N/D` | - |
| `POCF4Canal` | `N/D` | - |
| `POCF4DataA` | `N/D` | - |
| `POCF4HoraA` | `N/D` | - |
| `POCF4PUBom` | `N/D` | - |
| `POCF4ProDes` | `N/D` | - |
| `POCF4TipOrg` | `N/D` | - |
| `POCF4CusUnt` | `N/D` | - |
| `POCF4CusTot` | `N/D` | - |
| `POCF4VlrLuc` | `N/D` | - |
| `POCF4DCx` | `N/D` | - |
| `POCF4Mrg` | `N/D` | - |

#### 🗺️ Índices
- `POCF4A` (Unique): `POEmpCod`, `POCF4Tst`, `POCF4Regis`
- `POCF4B` (Duplicate): `POEmpCod`
- `POCF4C` (Duplicate): `POCF4Sts`
- `POCF4D` (Duplicate): `POCF4TstFec`

---

### 📌 POCxa1
- **Descrição:** Caixa01
- **Chave Primária:** `POEmpCod`, `PODtaMov`, `POCxaPer`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `PODtaMov` | `N/D` | - |
| `POCxaPer` | `N/D` | - |
| `POCxa1DinCxa` | `N/D` | - |
| `POCxa1Prz` | `N/D` | - |
| `POCxa1CarCre` | `N/D` | - |
| `POCxa1CarDeb` | `N/D` | - |
| `POCxa1CarTot` | `N/D` | - |
| `POCxa1Pix` | `N/D` | - |
| `POCxa1CorPrz` | `N/D` | - |
| `POCxa1Req` | `N/D` | - |
| `POCxa1Lub` | `N/D` | - |
| `POCxa1Tot1` | `N/D` | - |
| `POCxa1TotCom` | `N/D` | - |
| `POCxa1TrcAnt` | `N/D` | - |
| `POCxa1Cad` | `N/D` | - |
| `POCxa1Tot2` | `N/D` | - |
| `POCxa1DscPEC` | `N/D` | - |
| `POCxa1Dif` | `N/D` | - |
| `POCxa1DCx` | `N/D` | - |
| `POCxa1TPAn` | `N/D` | - |
| `POCxa1TRP` | `N/D` | - |
| `POCxa1TPAt` | `N/D` | - |
| `POCxa1Pre` | `N/D` | - |
| `POCxa1VlrRec` | `N/D` | - |
| `POCxa1VlrEnt` | `N/D` | - |
| `POCxa1VlrSai` | `N/D` | - |
| `POCxa1VlrVis` | `N/D` | - |
| `POCxa1ChqCxa` | `N/D` | - |
| `POCxa1VlrDsc` | `N/D` | - |
| `POCxa1VDR` | `N/D` | - |
| `POCxa1VDV` | `N/D` | - |
| `POCxa1DspVlr` | `N/D` | - |
| `POCxa1TrsLojCon` | `N/D` | - |
| `POCxa1VlrCan` | `N/D` | - |
| `POCxa1PrzCxa` | `N/D` | - |
| `POCxa1TotRec` | `N/D` | - |
| `POCxa1CofVlrRea` | `N/D` | - |
| `POCxa1Vlr_Cof` | `N/D` | - |
| `POCxa1DifCof` | `N/D` | - |
| `POCxa1RecCar` | `N/D` | - |
| `POCxa1RecRes` | `N/D` | - |
| `POCxa1RecTotRes` | `N/D` | - |
| `POCXa1LucCom` | `N/D` | - |
| `POCXa1LucOut` | `N/D` | - |
| `POCxa1LucTot` | `N/D` | - |
| `POCxa1DspDir` | `N/D` | - |
| `POCxa1DspTot` | `N/D` | - |
| `POCxa1Msg1` | `N/D` | - |
| `POCxa1Msg2` | `N/D` | - |
| `POCxa1Msg3` | `N/D` | - |
| `POCxa1Msg4` | `N/D` | - |
| `POCxa1Msg5` | `N/D` | - |
| `POCxa1VlrBol` | `N/D` | - |
| `POCxa1VlrPgtBol` | `N/D` | - |
| `POCxa1VlBom` | `N/D` | - |
| `POCxa1DifRec` | `N/D` | - |
| `POCxa1QtdCom` | `N/D` | - |
| `POCxa1BM_QTD` | `N/D` | - |
| `POCxa1BM_VLR` | `N/D` | - |
| `POCxa1BM_LUC` | `N/D` | - |
| `POCxa1PrzDir` | `N/D` | - |
| `POCxa1Qt2` | `N/D` | - |
| `POCxa1Qt5` | `N/D` | - |
| `POCxa1Qt10` | `N/D` | - |
| `POCxa1Qt20` | `N/D` | - |
| `POCxa1Qt50` | `N/D` | - |
| `POCxa1Qt_100` | `N/D` | - |
| `POCxa1Vl2` | `N/D` | - |
| `POCxa1Vl5` | `N/D` | - |
| `POCxa1Vl10` | `N/D` | - |
| `POCxa1Vl20` | `N/D` | - |
| `POCxa1Vl50` | `N/D` | - |
| `POCxa1Vl_100` | `N/D` | - |
| `POCxa1Vl999` | `N/D` | - |
| `POCxa1VlMoe` | `N/D` | - |
| `POCxa1VlChq` | `N/D` | - |
| `POCxa1DifDinCxa` | `N/D` | - |
| `POCxa1VFF` | `N/D` | - |
| `POCxa1Tot3` | `N/D` | - |
| `POCxa1Dif3` | `N/D` | - |
| `POCxa1VlDsp` | `N/D` | - |

#### 🗺️ Índices
- `POCxa11` (Unique): `POEmpCod`, `PODtaMov`, `POCxaPer`
- `POCxa12` (Duplicate): `POEmpCod`
- `POCxa13` (Duplicate): `POCxa1DCx`

---

### 📌 POCxa2
- **Descrição:** Caixa 2 - Somar Vendas por Tipo de Combustível
- **Chave Primária:** `POEmpCod`, `PODtaMov`, `POCxaPer`, `POTCoCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `PODtaMov` | `N/D` | - |
| `POCxaPer` | `N/D` | - |
| `POCxa1DinCxa` | `N/D` | - |
| `POCxa1Prz` | `N/D` | - |
| `POCxa1CarCre` | `N/D` | - |
| `POCxa1CarDeb` | `N/D` | - |
| `POCxa1CarTot` | `N/D` | - |
| `POCxa1Pix` | `N/D` | - |
| `POCxa1CorPrz` | `N/D` | - |
| `POCxa1Req` | `N/D` | - |
| `POCxa1Lub` | `N/D` | - |
| `POCxa1Tot1` | `N/D` | - |
| `POCxa1TotCom` | `N/D` | - |
| `POCxa1TrcAnt` | `N/D` | - |
| `POCxa1Cad` | `N/D` | - |
| `POCxa1Tot2` | `N/D` | - |
| `POCxa1DscPEC` | `N/D` | - |
| `POCxa1Dif` | `N/D` | - |
| `POCxa1DCx` | `N/D` | - |
| `POCxa1TPAn` | `N/D` | - |
| `POCxa1TRP` | `N/D` | - |
| `POCxa1TPAt` | `N/D` | - |
| `POCxa1Pre` | `N/D` | - |
| `POCxa1VlrRec` | `N/D` | - |
| `POCxa1VlrEnt` | `N/D` | - |
| `POCxa1VlrSai` | `N/D` | - |
| `POCxa1VlrVis` | `N/D` | - |
| `POCxa1ChqCxa` | `N/D` | - |
| `POCxa1VlrDsc` | `N/D` | - |
| `POCxa1VDR` | `N/D` | - |
| `POCxa1VDV` | `N/D` | - |
| `POCxa1DspVlr` | `N/D` | - |
| `POCxa1TrsLojCon` | `N/D` | - |
| `POCxa1VlrCan` | `N/D` | - |
| `POCxa1PrzCxa` | `N/D` | - |
| `POCxa1TotRec` | `N/D` | - |
| `POCxa1CofVlrRea` | `N/D` | - |
| `POCxa1Vlr_Cof` | `N/D` | - |
| `POCxa1DifCof` | `N/D` | - |
| `POCxa1RecCar` | `N/D` | - |
| `POCxa1RecRes` | `N/D` | - |
| `POCxa1RecTotRes` | `N/D` | - |
| `POCXa1LucCom` | `N/D` | - |
| `POCXa1LucOut` | `N/D` | - |
| `POCxa1LucTot` | `N/D` | - |
| `POCxa1DspDir` | `N/D` | - |
| `POCxa1DspTot` | `N/D` | - |
| `POCxa1Msg1` | `N/D` | - |
| `POCxa1Msg2` | `N/D` | - |
| `POCxa1Msg3` | `N/D` | - |
| `POCxa1Msg4` | `N/D` | - |
| `POCxa1Msg5` | `N/D` | - |
| `POCxa1VlrBol` | `N/D` | - |
| `POCxa1VlrPgtBol` | `N/D` | - |
| `POCxa1VlBom` | `N/D` | - |
| `POCxa1DifRec` | `N/D` | - |
| `POCxa1QtdCom` | `N/D` | - |
| `POCxa1BM_QTD` | `N/D` | - |
| `POCxa1BM_VLR` | `N/D` | - |
| `POCxa1BM_LUC` | `N/D` | - |
| `POCxa1PrzDir` | `N/D` | - |
| `POCxa1Qt2` | `N/D` | - |
| `POCxa1Qt5` | `N/D` | - |
| `POCxa1Qt10` | `N/D` | - |
| `POCxa1Qt20` | `N/D` | - |
| `POCxa1Qt50` | `N/D` | - |
| `POCxa1Qt_100` | `N/D` | - |
| `POCxa1Vl2` | `N/D` | - |
| `POCxa1Vl5` | `N/D` | - |
| `POCxa1Vl10` | `N/D` | - |
| `POCxa1Vl20` | `N/D` | - |
| `POCxa1Vl50` | `N/D` | - |
| `POCxa1Vl_100` | `N/D` | - |
| `POCxa1Vl999` | `N/D` | - |
| `POCxa1VlMoe` | `N/D` | - |
| `POCxa1VlChq` | `N/D` | - |
| `POTCoCod` | `N/D` | - |
| `POTCoDes` | `N/D` | - |
| `POCxa2Qtd` | `N/D` | - |
| `POCxa2Vlr` | `N/D` | - |
| `POCxa2MDM1Atu` | `N/D` | - |
| `POCxa2MDM2Ant` | `N/D` | - |
| `POCxa2MDA1Atu` | `N/D` | - |
| `POCxa2MDA2Ant` | `N/D` | - |
| `POCxa2QDM` | `N/D` | - |
| `POCxa2QDA` | `N/D` | - |
| `POCxa2QLM1Atu` | `N/D` | - |
| `POCxa2QLA1Atu` | `N/D` | - |
| `POCxa2QLM2Ant` | `N/D` | - |
| `POCxa2QLA2Ant` | `N/D` | - |
| `POCxa2DtaMovAnt` | `N/D` | - |
| `POCxa2DtaIniAno` | `N/D` | - |
| `POCxa2VlrUnt` | `N/D` | - |
| `POCxa2CusUnt` | `N/D` | - |
| `POCxa2MrgAtu` | `N/D` | - |
| `POCxa2DMM` | `N/D` | - |
| `POCxa2DMA` | `N/D` | - |
| `POCxa2DQM` | `N/D` | - |
| `POCxa2DQA` | `N/D` | - |
| `POCxa2CusTot` | `N/D` | - |
| `POCxa2LucTot` | `N/D` | - |

#### 🗺️ Índices
- `POCxa21` (Unique): `POEmpCod`, `PODtaMov`, `POCxaPer`, `POTCoCod`
- `POCxa22` (Duplicate): `POTCoCod`
- `POCxa23` (Duplicate): `POEmpCod`, `PODtaMov`, `POCxaPer`
- `POCxa24` (Duplicate): `POEmpCod`, `POTCoCod`, `PODtaMov`

---

### 📌 POEmp
- **Descrição:** Empresas
- **Chave Primária:** `POEmpCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `POEmpDes` | `N/D` | - |
| `POEmpDtaUso` | `N/D` | - |
| `POEmpPer` | `N/D` | - |
| `POEmpRazSoc` | `N/D` | - |
| `PoEmpEnd` | `N/D` | - |
| `POEmpCGC` | `N/D` | - |
| `POEmpI_E` | `N/D` | - |
| `POEmpQtdPer` | `N/D` | - |
| `POEmpVlrVal` | `N/D` | - |

#### 🗺️ Índices
- `POEmp1` (Unique): `POEmpCod`

---

### 📌 POENF
- **Descrição:** Entrada de Notas Fiscais
- **Chave Primária:** `POEmpCod`, `PODtaMov`, `POTnqCod`, `POForCod`, `POForNNF`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `PODtaMov` | `N/D` | - |
| `POTnqCod` | `N/D` | - |
| `POForCod` | `N/D` | - |
| `POForNNF` | `N/D` | - |
| `POForDNF` | `N/D` | - |
| `POENFQtd` | `N/D` | - |
| `POTnqDes` | `N/D` | - |
| `POENFVlrTot` | `N/D` | - |
| `POENFVlrUnt` | `N/D` | - |
| `POENFObs` | `N/D` | - |
| `POENFSts` | `N/D` | - |
| `POENFDtaPgt` | `N/D` | - |
| `POENFOrg` | `N/D` | - |
| `POENFNFE` | `N/D` | - |
| `POENFBCO` | `N/D` | - |
| `POENFCHQ` | `N/D` | - |

#### 🗺️ Índices
- `POENF1` (Unique): `POEmpCod`, `PODtaMov`, `POTnqCod`, `POForCod`, `POForNNF`
- `POEnF3` (Duplicate): `POEmpCod`, `PODtaMov`, `POTnqCod`
- `POENF2` (Duplicate): `POForCod`
- `POENF4` (Duplicate): `POENFSts`, `POENFDtaPgt`, `POENFBCO`, `POENFCHQ`, `POENFQtd`
- `POENF5` (Duplicate): `POENFNFE`

---

### 📌 POFor
- **Descrição:** Fornecedores
- **Chave Primária:** `POForCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POForCod` | `N/D` | - |
| `POForDes` | `N/D` | - |

#### 🗺️ Índices
- `POFor1` (Unique): `POForCod`

---

### 📌 POLac
- **Descrição:** Lacre das Bombas
- **Chave Primária:** `POEmpCod`, `POMBoCod`, `POLacNro`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `POMBoCod` | `N/D` | - |
| `POMBoDes` | `N/D` | - |
| `POLacNro` | `N/D` | - |
| `POLacDta` | `N/D` | - |

#### 🗺️ Índices
- `POLac1` (Unique): `POEmpCod`, `POMBoCod`, `POLacNro`
- `POLac2` (Duplicate): `POEmpCod`, `POMBoCod`

---

### 📌 POLMC1
- **Descrição:** LMC
- **Chave Primária:** `POEmpCod`, `PODtaMov`, `POTnqCod`, `POBomCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `PODtaMov` | `N/D` | - |
| `POTnqCod` | `N/D` | - |
| `POLMC2Vda` | `N/D` | - |
| `POBomCod` | `N/D` | - |
| `POBomDes` | `N/D` | - |
| `POLMC1Fin` | `N/D` | - |
| `POLMC1Ini` | `N/D` | - |
| `POLMC1Qtd` | `N/D` | - |
| `POLMC1Afe` | `N/D` | - |

#### 🗺️ Índices
- `POLMC11` (Unique): `POEmpCod`, `PODtaMov`, `POTnqCod`, `POBomCod`
- `POLMC12` (Duplicate): `POEmpCod`, `POBomCod`
- `POLMC13` (Duplicate): `POEmpCod`, `PODtaMov`, `POTnqCod`

---

### 📌 POLMC2
- **Descrição:** Estoque dos Tanques LMC
- **Chave Primária:** `POEmpCod`, `PODtaMov`, `POTnqCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `PODtaMov` | `N/D` | - |
| `POTnqCod` | `N/D` | - |
| `POTnqDes` | `N/D` | - |
| `POLMC2EIn` | `N/D` | - |
| `POLMC2EFi` | `N/D` | - |
| `POLMC2Vda` | `N/D` | - |
| `POLMC2EntNF` | `N/D` | - |
| `POLMC2E_S` | `N/D` | - |
| `POLMC2Obs` | `N/D` | - |
| `POLMC2CusUnt` | `N/D` | - |
| `POLMC2CusTot` | `N/D` | - |
| `POTnqCusUnt` | `N/D` | - |
| `POLMC2EEs` | `N/D` | - |
| `POLMC2EPe` | `N/D` | - |
| `POLMC2EGa` | `N/D` | - |
| `POLMC2EDi` | `N/D` | - |
| `POLMC2VlrUnt` | `N/D` | - |
| `POLMC2VUF` | `N/D` | - |
| `POLMC2VlrTot` | `N/D` | - |
| `POLMC2EmiLMC` | `N/D` | - |
| `POLMC2TrsQtd` | `N/D` | - |
| `POLMC2TrsTnq` | `N/D` | - |
| `POLMC2TrsCom` | `N/D` | - |
| `POLMC2TrsLMCTnq` | `N/D` | - |
| `POTnqTipCom` | `N/D` | - |
| `POTnqDesLMC` | `N/D` | - |
| `POTnqQtd` | `N/D` | - |
| `POLMC2CusEnc` | `N/D` | - |
| `POLMC2QtdEnc` | `N/D` | - |

#### 🗺️ Índices
- `POLMC21` (Unique): `POEmpCod`, `PODtaMov`, `POTnqCod`
- `POLMC22` (Duplicate): `POEmpCod`, `POTnqCod`

---

### 📌 POLMC3
- **Descrição:** Movimento por Tipo Combustível - LMC
- **Chave Primária:** `POEmpCod`, `PODtaMov`, `POLMC3TCoCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `PODtaMov` | `N/D` | - |
| `POLMC3TCoCod` | `N/D` | - |
| `POLMC3TCoDes` | `N/D` | - |
| `POLMC3Ein` | `N/D` | - |
| `POLMC3Efi` | `N/D` | - |
| `POLMC3EDi` | `N/D` | - |
| `POLMC3Vda` | `N/D` | - |
| `POLMC3EntNF` | `N/D` | - |
| `POLMC3E_S` | `N/D` | - |
| `POLMC3Obs` | `N/D` | - |
| `POLMC3EEs` | `N/D` | - |
| `POLMC3EPe` | `N/D` | - |
| `POLMC3EGa` | `N/D` | - |

#### 🗺️ Índices
- `POLMC31` (Unique): `POEmpCod`, `PODtaMov`, `POLMC3TCoCod`
- `POLMC32` (Duplicate): `POEmpCod`
- `POLMC33` (Duplicate): `POEmpCod`, `POLMC3TCoCod`, `PODtaMov`

---

### 📌 POLvr
- **Descrição:** Livros do LMC
- **Chave Primária:** `POEmpCod`, `POLvrCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `POLvrCod` | `N/D` | - |
| `POLvrDes` | `N/D` | - |
| `POLvrDtaIni` | `N/D` | - |

#### 🗺️ Índices
- `POLvr1` (Unique): `POEmpCod`, `POLvrCod`
- `POLvr2` (Duplicate): `POEmpCod`

---

### 📌 POMBo
- **Descrição:** Cadastro das Bombas
- **Chave Primária:** `POEmpCod`, `POMBoCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `POMBoCod` | `N/D` | - |
| `POMBoDes` | `N/D` | - |
| `POMBoNroSer` | `N/D` | - |
| `POMBoNomFab` | `N/D` | - |
| `POMBoModBom` | `N/D` | - |
| `POMBoIdeMed` | `N/D` | - |

#### 🗺️ Índices
- `POMBo1` (Unique): `POEmpCod`, `POMBoCod`
- `POMBo2` (Duplicate): `POEmpCod`

---

### 📌 POPer
- **Descrição:** Períodos
- **Chave Primária:** `POEmpCod`, `POPerCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `POEmpQtdPer` | `N/D` | - |
| `POPerCod` | `N/D` | - |
| `POPerDes` | `N/D` | - |

#### 🗺️ Índices
- `POPer1` (Unique): `POEmpCod`, `POPerCod`
- `POPer2` (Duplicate): `POEmpCod`

---

### 📌 POTCo
- **Descrição:** Tipos de Combustíveis
- **Chave Primária:** `POTCoCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POTCoCod` | `N/D` | - |
| `POTCoDes` | `N/D` | - |
| `POTCoProCod` | `N/D` | - |
| `POTCoProDes` | `N/D` | - |
| `POTCoProUnd` | `N/D` | - |

#### 🗺️ Índices
- `POTCo1` (Unique): `POTCoCod`

---

### 📌 POTCV
- **Descrição:** TOTAL COMPRAS/VENDAS
- **Chave Primária:** `POEmpCod`, `POTCMAn`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `POTCMAn` | `N/D` | - |
| `POTCMAno` | `N/D` | - |
| `POTCMMes` | `N/D` | - |
| `POTCFVlrIni` | `N/D` | - |
| `POTCFVlrFin` | `N/D` | - |
| `POTCFVlrDif` | `N/D` | - |
| `POTCFVlrEnt` | `N/D` | - |
| `POTCFCreDeb` | `N/D` | - |
| `POTCFQEDie` | `N/D` | - |
| `POTCFQES10` | `N/D` | - |
| `POTCFQEGas` | `N/D` | - |
| `POTCFQEEta` | `N/D` | - |
| `POTCFVEDie` | `N/D` | - |
| `POTCFVES10` | `N/D` | - |
| `POTCFVEEta` | `N/D` | - |
| `POTCFVEGas` | `N/D` | - |
| `POTCFQSDie` | `N/D` | - |
| `POTCFQSS10` | `N/D` | - |
| `POTCFQSGas` | `N/D` | - |
| `POTCFQSEta` | `N/D` | - |
| `POTCFVSDie` | `N/D` | - |
| `POTCFVSS10` | `N/D` | - |
| `POTCFVSEta` | `N/D` | - |
| `POTCFVSGas` | `N/D` | - |
| `POTCFCDQDie` | `N/D` | - |
| `POTCFCDQS10` | `N/D` | - |
| `POTCFCDQGas` | `N/D` | - |
| `POTCFCDQEta` | `N/D` | - |
| `POTCFCDVDie` | `N/D` | - |
| `POTCFCDVS10` | `N/D` | - |
| `POTCFCDVGas` | `N/D` | - |
| `POTCFCDVEta` | `N/D` | - |
| `POTCFQET` | `N/D` | - |
| `POTCFVET` | `N/D` | - |
| `POTCFQST` | `N/D` | - |
| `POTCFVST` | `N/D` | - |

#### 🗺️ Índices
- `POTCV1` (Unique): `POEmpCod`, `POTCMAn`
- `POTCV2` (Duplicate): `POEmpCod`

---

### 📌 POTnq
- **Descrição:** Tanques
- **Chave Primária:** `POEmpCod`, `POTnqCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `POTnqCod` | `N/D` | - |
| `POTnqDes` | `N/D` | - |
| `POTnqDesLMC` | `N/D` | - |
| `POLvrCod` | `N/D` | - |
| `POLvrDes` | `N/D` | - |
| `POTnqTipCom` | `N/D` | - |
| `POTnqCusUnt` | `N/D` | - |
| `POTnqConSpd` | `N/D` | - |
| `POTnqQtd` | `N/D` | - |

#### 🗺️ Índices
- `POTnq1` (Unique): `POEmpCod`, `POTnqCod`
- `POTnq2` (Duplicate): `POEmpCod`, `POLvrCod`

---

### 📌 POVal
- **Descrição:** Controle de Vales
- **Chave Primária:** `POEmpCod`, `POValCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `POEmpVlrVal` | `N/D` | - |
| `POValCod` | `N/D` | - |
| `POValVlr` | `N/D` | - |
| `POValUsu` | `N/D` | - |
| `POValTST` | `N/D` | - |
| `POValCreDeb` | `N/D` | - |
| `POValCli` | `N/D` | - |
| `POValAlt` | `N/D` | - |
| `POValDel` | `N/D` | - |
| `POValVlrAnt` | `N/D` | - |
| `POValDif` | `N/D` | - |
| `POValDtaLct` | `N/D` | - |
| `POValTstBxa` | `N/D` | - |
| `POValUsuBxa` | `N/D` | - |
| `POValSts` | `N/D` | - |
| `POValCodOrg` | `N/D` | - |

#### 🗺️ Índices
- `POVal1` (Unique): `POEmpCod`, `POValCod`
- `POVal2` (Duplicate): `POEmpCod`
- `POVal3` (Duplicate): `POValCli`
- `POVal4` (Duplicate): `POEmpCod`, `POValCod`
- `POVal5` (Duplicate): `POValDtaLct`
- `POVal6` (Duplicate): `POValSts`

---

### 📌 POVel1
- **Descrição:** Velocímetro 01
- **Chave Primária:** `POEmpCod`, `PODtaMov`, `POVel1Per`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `PODtaMov` | `N/D` | - |
| `POVel1Per` | `N/D` | - |
| `POVel1Qtd` | `N/D` | - |
| `POVel1Vlr` | `N/D` | - |

#### 🗺️ Índices
- `POVel11` (Unique): `POEmpCod`, `PODtaMov`, `POVel1Per`
- `POVel12` (Duplicate): `POEmpCod`

---

### 📌 POVel2
- **Descrição:** Velocimetro 02
- **Chave Primária:** `POEmpCod`, `PODtaMov`, `POVel1Per`, `POBomCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `POEmpCod` | `N/D` | - |
| `PODtaMov` | `N/D` | - |
| `POVel1Per` | `N/D` | - |
| `POVel1Qtd` | `N/D` | - |
| `POVel1Vlr` | `N/D` | - |
| `POBomCod` | `N/D` | - |
| `POBomDes` | `N/D` | - |
| `POBomVlrUnt` | `N/D` | - |
| `POVel2Ini` | `N/D` | - |
| `POVel2Fin` | `N/D` | - |
| `POVel2Qtd` | `N/D` | - |
| `POVel2Afe` | `N/D` | - |
| `POVel2VlrTot` | `N/D` | - |
| `POVel2LQM` | `N/D` | - |
| `POVel2VlrUnt` | `N/D` | - |
| `POVel2CusUnt` | `N/D` | - |
| `POVel2CusTot` | `N/D` | - |
| `POVel2LucTot` | `N/D` | - |

#### 🗺️ Índices
- `POVel21` (Unique): `POEmpCod`, `PODtaMov`, `POVel1Per`, `POBomCod`
- `POVel22` (Duplicate): `POEmpCod`, `POBomCod`
- `POVel23` (Duplicate): `POEmpCod`, `PODtaMov`, `POVel1Per`

---

### 📌 Precos
- **Descrição:** Precos do Simpro
- **Chave Primária:** `CD_Cliente`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CD_Cliente` | `N/D` | - |
| `Nome_Prod` | `N/D` | - |
| `Nome_Lab` | `N/D` | - |
| `Preco_Prod` | `N/D` | - |
| `Data_Vig` | `N/D` | - |
| `Identif` | `N/D` | - |
| `Preco_Fabr` | `N/D` | - |
| `Nome_35Pos` | `N/D` | - |
| `AbcFarma` | `N/D` | - |

#### 🗺️ Índices
- `Preco1` (Unique): `CD_Cliente`
- `Preco2` (Duplicate): `Nome_Prod`
- `Preco3` (Duplicate): `Nome_35Pos`

---

### 📌 SANF1
- **Descrição:** Cab. Nota Sagra
- **Chave Primária:** `SANF1Ini`, `SANF1NroPed`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `SANF1Ini` | `N/D` | - |
| `SANF1NroPed` | `N/D` | - |
| `SANF1PedCli` | `N/D` | - |
| `SANF1NroNFi` | `N/D` | - |
| `SACliCod` | `N/D` | - |
| `SANF1DtaEmi` | `N/D` | - |
| `SANF1DtaVct` | `N/D` | - |
| `SANF1TotNot` | `N/D` | - |

#### 🗺️ Índices
- `SANF11` (Unique): `SANF1Ini`, `SANF1NroPed`

---

### 📌 SANF2
- **Descrição:** Produtos Nota SAGRA
- **Chave Primária:** `SANF1Ini`, `SANF1NroPed`, `SAProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `SANF1Ini` | `N/D` | - |
| `SANF1NroPed` | `N/D` | - |
| `SANF1PedCli` | `N/D` | - |
| `SANF1NroNFi` | `N/D` | - |
| `SACliCod` | `N/D` | - |
| `SANF1DtaEmi` | `N/D` | - |
| `SANF1DtaVct` | `N/D` | - |
| `SANF1TotNot` | `N/D` | - |
| `SAProCod` | `N/D` | - |
| `SANF2Qtd` | `N/D` | - |
| `SANF2Cus` | `N/D` | - |
| `SANF2PerDes` | `N/D` | - |
| `SANF2IntOk` | `N/D` | - |
| `SANF2TotPro` | `N/D` | - |
| `SANF2CodBar` | `N/D` | - |
| `SANF2DesPro` | `N/D` | - |

#### 🗺️ Índices
- `SANF21` (Unique): `SANF1Ini`, `SANF1NroPed`, `SAProCod`
- `SANF22` (Duplicate): `SAProCod`
- `SANF23` (Duplicate): `SANF1Ini`, `SANF1NroPed`

---

### 📌 SAPro
- **Descrição:** Produtos da SAGRA
- **Chave Primária:** `SAProCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `SAProCod` | `N/D` | - |
| `SAProDes` | `N/D` | - |
| `SAProPreVda` | `N/D` | - |
| `SAProPerDes` | `N/D` | - |
| `SAForCod` | `N/D` | - |
| `SAProPor` | `N/D` | - |
| `SAProEstDis` | `N/D` | - |
| `SAProCodBar` | `N/D` | - |

#### 🗺️ Índices
- `SAPro1` (Unique): `SAProCod`
- `SAPro2` (Duplicate): `SAProCodBar`

---

### 📌 SDMA1
- **Descrição:** Movimento do Associado
- **Chave Primária:** `CMEmpCod`, `CRCliCod`, `SDMA1Dta`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CRCliCod` | `N/D` | - |
| `SDMA1Dta` | `N/D` | - |
| `SDMA1Ano` | `N/D` | - |
| `SDMA1Mes` | `N/D` | - |
| `CRCliDes` | `N/D` | - |
| `SDMA1VlrCab` | `N/D` | - |
| `SDMA1VlrRem` | `N/D` | - |
| `SDMA1VlrDes` | `N/D` | - |
| `SDMA1VlrAss` | `N/D` | - |
| `SDMA1VlrCur` | `N/D` | - |
| `SDMA1VlrOut` | `N/D` | - |
| `SDMA1VlrCon` | `N/D` | - |
| `SDMA1TST` | `N/D` | - |
| `SDMA1USU` | `N/D` | - |
| `SDMA1PRG` | `N/D` | - |
| `SDMA1Obs1` | `N/D` | - |
| `SDMA1Obs2` | `N/D` | - |
| `SDMA1Obs3` | `N/D` | - |

#### 🗺️ Índices
- `SDMA1A` (Unique): `CMEmpCod`, `CRCliCod`, `SDMA1Dta`
- `SDMA1B` (Duplicate): `CMEmpCod`, `CRCliCod`
- `SDMV1C` (Duplicate): `CMEmpCod`, `SDMA1Dta`
- `SDMV1D` (Duplicate): `CMEmpCod`, `SDMA1Dta`

---

### 📌 SDMV1
- **Descrição:** SDMV1
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `SDMV1AME`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `SDMV1AME` | `N/D` | - |
| `SDMV1Aux` | `N/D` | - |

#### 🗺️ Índices
- `SDMV11` (Unique): `CMEmpCod`, `CMFilCod`, `SDMV1AME`
- `SDMV12` (Duplicate): `CMEmpCod`, `CMFilCod`

---

### 📌 SDMV2
- **Descrição:** SDMV2
- **Chave Primária:** `CMEmpCod`, `CMFilCod`, `SDMV1AME`, `CRClaCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CMFilCod` | `N/D` | - |
| `SDMV1AME` | `N/D` | - |
| `SDMV1Aux` | `N/D` | - |
| `CRClaCod` | `N/D` | - |
| `CRClaNom` | `N/D` | - |
| `SDMVDeb` | `N/D` | - |
| `SDMVCre` | `N/D` | - |
| `SDMVDif` | `N/D` | - |

#### 🗺️ Índices
- `SDMV22` (Unique): `CMEmpCod`, `CMFilCod`, `SDMV1AME`, `CRClaCod`
- `SDMV21` (Duplicate): `CMEmpCod`, `CRClaCod`
- `SDMV23` (Duplicate): `CMEmpCod`, `CMFilCod`, `SDMV1AME`

---

### 📌 SDPOB
- **Descrição:** Observações do Produto do Sindicato
- **Chave Primária:** `CMEmpCod`, `CEProCod`, `SDPOB`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `CEProCod` | `N/D` | - |
| `CEProDes` | `N/D` | - |
| `SDPOB` | `N/D` | - |

#### 🗺️ Índices
- `SDPOB1` (Unique): `CMEmpCod`, `CEProCod`, `SDPOB`
- `SDPOB2` (Duplicate): `CMEmpCod`, `CEProCod`

---

### 📌 SDUsi
- **Descrição:** Cadastro de Usinas
- **Chave Primária:** `CMEmpCod`, `SDUsiCod`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `CMEmpCod` | `N/D` | - |
| `SDUsiCod` | `N/D` | - |
| `SDUsiNomEmp` | `N/D` | - |
| `SDUsiNomPro` | `N/D` | - |
| `SDUsiCNPJ` | `N/D` | - |
| `SDUsiCPF` | `N/D` | - |
| `SDUsiCidPro` | `N/D` | - |
| `SDUsiNroFun` | `N/D` | - |
| `SDUsiEndCor` | `N/D` | - |
| `SDUsiComCor` | `N/D` | - |
| `SDUsiCidCor` | `N/D` | - |
| `SDUsiEstCor` | `N/D` | - |
| `SDUsiBaiCor` | `N/D` | - |
| `SDUsiCEPCor` | `N/D` | - |
| `SDUsiEmaCor` | `N/D` | - |
| `SDUsiEscDes` | `N/D` | - |
| `SDUsiEscNomCon` | `N/D` | - |
| `SDUsiEscTelCon1` | `N/D` | - |
| `SDUsiEscFax` | `N/D` | - |
| `SDUsiCont` | `N/D` | - |
| `SDUsiProTip` | `N/D` | - |
| `SDUsiSet` | `N/D` | - |
| `SDUsuFil` | `N/D` | - |

#### 🗺️ Índices
- `SDUsi1` (Unique): `CMEmpCod`, `SDUsiCod`
- `SDUsi2` (Duplicate): `CMEmpCod`
- `SDUsi3` (Duplicate): `CMEmpCod`, `SDUsiNomEmp`

---

### 📌 TABELAS
- **Descrição:** TABELAS
- **Chave Primária:** `object_id`

#### 📄 Colunas / Campos
| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| `object_id` | `N/D` | - |
| `Name` | `N/D` | - |

#### 🗺️ Índices
- `ITABELAS` (Unique): `object_id`

---

