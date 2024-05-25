# Como instalar Python em 2024 + Pyenv, PIP, VENV, PIPX e Poetry
### https://www.youtube.com/watch?v=9LYqtLuD7z4&ab_channel=LucianoGalv%C3%A3oFilho

## Instalação do pyenv

- https://github.com/pyenv-win/pyenv-win

power shell:

*>Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"*

*>Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser*

*verificar as variáveis de ambiente e criar se necessário as variáveis solicitdadas através do caminho específico do pyenv Ex. PYENV PYENV_HOME PYENV_ROOT em C:\Users\Residencial\.pyenv\pyenv-win\ e no PATH adicionar C:\Users\Residencial\.pyenv\pyenv-win\bin e C:\Users\Residencial\.pyenv\pyenv-win\shims*

## Configuração do pyenv

Para verificar as versões python instaladas
>pyenv versions

para instalar uma versão python
>pyenv install 3.12.1

para definir uma versão default
>pyenv global 3.12.1

definindo a versão local, dentro da pasta do projeto
>pyenv local 3.12.1

## PIP e Venv

>pip list (ver a lista de pacotes instalados)

>pip uninstall package (para remover pacotes)

>pip freeze (lista de bibliotecas instaladas)

>pip freeze | grep -v "^-e" | xargs pip uninstall -y (remove todas as bibliotecas)

dentro da pasta do projeto, criamos uma ambiente virtual

>python -m venv .venv
>source .venv/Scripts/activate
>pip install package
>deactivate (para sair do ambiente virtual)


## PIPX

ambiente virtual por usuário

>pip install pipx

>pipx install poetry
>pipx install ipython

## ipython -i

adicionan no PATH o caminho do arquivo executável do ipython

entra no compilador python com uma interface grafica mais amigável

>ipython -i

## Poetry

Organiza as dependencias de bibliotecas

>poetry config virtualenvs.in-project true (para que o poetry controle tambem os ambientes virtuais)

>poetry new nome_do_projeto (ele cria uma pasta com o nome do projeto e todas as configurações)

dentro da pasta do projeto
>pyenv local 3.12.1

>poetry env use 3.12.1 (poetry cria o ambiente virtual dentro de .venv)

>poetry add package (instala um pacote e todas as dependencias)

>poetry remove package (remove pacote e dependências)
