#!/usr/bin/fish

# Verifica se o venv existe e ativa
if test -f "venv/bin/activate.fish"
    source venv/bin/activate.fish
    
    # Executa o script
    python tomatextor.py $argv
    
    deactivate
else
    echo "Erro: Ambiente virtual não encontrado. Execute a instalação primeiro."
end