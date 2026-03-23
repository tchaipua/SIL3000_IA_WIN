@echo off
echo [GIT] Inicializando repositorio...
git init

echo [GIT] Forcando identidade GitHub...
git config user.email "tchaipua@github.com"
git config user.name "tchaipua"

echo [GIT] Adicionando arquivos...
git add .

echo [GIT] Efetuando Commit...
git commit -m "Inicializando Dashboard de Vendas e Produto"

echo [GIT] Mudando branch para main...
git branch -M main

echo [GIT] Adicionando remote Github...
git remote add origin https://github.com/tchaipua/SIL3000_IA_WIN.git

echo [GIT] Subindo para o Github...
git push -u origin main -f

echo [GIT] Processo Concluido!
