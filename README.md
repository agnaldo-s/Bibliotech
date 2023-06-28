# BiblioTec - Sistema de Gerenciamento de Livros

O BiblioTec é um sistema desenvolvido como desafio para a disciplina de Desenvolvimento para Desktop, ministrada pelo professor Titione Falácio de Amorim. O objetivo do sistema é fornecer um ambiente para gerenciamento de livros, permitindo adicionar, editar, pesquisar e remover livros de uma biblioteca.

### Programadores
- Agnaldo da Silva
- Ana Carolina Schmitz da Silva
- Caique Lacerda Martel
- Chrystian Souza Silveira Meyer


## Requisitos do Sistema

Certifique-se de ter os seguintes requisitos instalados em seu ambiente:

- Python (versão 3.10)
- PySide6
- SQLAlchemy==1.3.10

## Conversão de Arquivos .ui para Python
Para converter um arquivo .ui gerado no Qt Designer para um arquivo Python correspondente, utilizamos o comando pyside6-uic da seguinte forma:
```bash
pyside6-uic arquivo-de-entrada.ui -o ui/arquivo-de-saida.py
```
Onde:

- arquivo-de-entrada.ui é o caminho para o arquivo .ui que desejamos converter.
- ui/arquivo-de-saida.py é o caminho e o nome do arquivo Python que será gerado.
Esse comando realizará a conversão e criará um arquivo Python que poderá ser importado em nosso projeto para a criação da interface.

## Configurando o Ambiente Virtual (venv)
### Windows
1. Abra o prompt de comando.

2. Navegue até a pasta do seu projeto utilizando o comando cd.

3. Crie um novo ambiente virtual com o seguinte comando:

```bash
python3.10 -m venv .venv
```
4. Ative o ambiente virtual executando o seguinte comando:
```bash
.venv\Scripts\activate
```

### Linux
1. Abra um terminal.

2. Navegue até a pasta do seu projeto utilizando o comando cd.

3. Crie um novo ambiente virtual com o seguinte comando:
```bash
python3.10 -m venv .venv
```
4. Ative o ambiente virtual executando o seguinte comando:
```bash
source .venv/bin/activate
```
#### Erro Linux
Se ocorrer o erro:
```bash
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: wayland, wayland-egl, minimal, minimalegl, vkkhrdisplay, eglfs, vnc, xcb, offscreen, linuxfb.
```
Execute o comando:
```bash
sudo apt install libxcb-cursor0
```

### Instalando as Dependências
Após ativar o ambiente virtual, você pode instalar as dependências listadas no arquivo requirements.txt usando o comando pip.

Certifique-se de estar no diretório do seu projeto, onde o arquivo requirements.txt está localizado.

Execute o seguinte comando no terminal:
```bash
pip install -r requirements.txt
```
Isso irá ler o arquivo requirements.txt e instalar todas as dependências listadas no ambiente virtual.

Após a instalação, você estará pronto para executar o seu projeto com as dependências corretamente configuradas.

## Executando o Sistema
Após instalar as dependências, você pode executar o sistema BiblioTec. Certifique-se de estar no diretório do projeto no terminal ou prompt de comando e de que as dependências foram instaladas corretamente.

Execute o seguinte comando para iniciar o sistema:
```bash
python main.py
```
Isso iniciará a aplicação BiblioTec e abrirá a interface do usuário. A partir daí, você poderá interagir com o sistema, adicionar e gerenciar os livros da biblioteca.

## Contribuição
Se você deseja contribuir com o projeto BiblioTec, fique à vontade para abrir problemas ou enviar pull requests para revisão.
