# Esse script adiciona uma função ao seu arquivo bashrc para executar o main.py no terminal em qualquer pasta
# execute pycli em qualquer terminal e sera executado o python script


# Obtém o diretório atual do script bash.sh
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Verifica se a função já está no .bashrc
if ! grep -qF "pycli() {" ~/.bashrc; then
    # Constrói o caminho relativo para o main.py a partir do diretório do script
    script="$script_dir/main.py"

    # Adiciona a função pycli ao final do .bashrc
    echo -e "\npycli() {\n  python \"$script\"\n}" >> ~/.bashrc

    # Atualiza o .bashrc
    source ~/.bashrc
fi