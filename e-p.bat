@echo off
echo [E-P] Reiniciando aplicacao...
taskkill /F /FI "WINDOWTITLE eq SIL_IA_WIN*" /T > nul 2>&1
start "" python SIL_IA_WIN.py
echo [E-P] Aplicacao iniciada.
