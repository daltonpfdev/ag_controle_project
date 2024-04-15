# Controle de Motoristas e Veículos

Este projeto Django é um CRUD (Create, Read, Update, Delete) para o controle de motoristas, veículos e saídas de veículos. Ele permite que você gerencie informações sobre motoristas, veículos e registros de saída de veículos associados aos motoristas.

## Funcionalidades

- Cadastro de motoristas com nome, telefone e número de CNH.
- Cadastro de veículos com placa, marca, tipo de veículo e quilometragem para troca de óleo.
- Registro de saídas de veículos, incluindo data e hora de saída, quilometragem de saída, destino, data e hora de retorno, quilometragem de retorno e quilometragem percorrida.
- Controle de disponibilidade de veículos, garantindo que um veículo só possa ser utilizado se estiver disponível.
- Interface amigável para visualização e gerenciamento dos registros de controle.

## Preparação do Terreno

1. IDE

   Este projeto foi programado inteiramente na IDE Visual Studio Code, então é recomendável que utlização do Projeto seja na IDE que o projeto foi projetado.

2. Instalação do Python

   Este é um projeto desenvolvido na Linguagem de Programação Python (mais especificamente na versão 3.12.3), então é necessário baixar e instalar o Python. É recomendado que seja baixado no site oficial do Python:
   ```markdown
   https://www.python.org/

3. Variavel de Ambiente

   Para que seja possível rodar um programa feito em Python, é necessário adicionar o caminho da instação para as suas Variáveis de Ambiente:

   - Abra o "Painel de Controle".
   - Clique em "Sistema e Segurança" e depois em "Sistema".
   - No painel esquerdo, clique em "Configurações avançadas do sistema".
   - Na janela de Propriedades do Sistema, clique em "Variáveis de Ambiente".
   - Na seção "Variáveis de Sistema", encontre a variável "PATH" e selecione-a, então clique em "Editar...".
   - Na janela de Edição de Variável de Sistema, clique em "Novo" e adicione o diretório do executável do Python ao PATH.
   - Para encontrar o caminho da instalação do seu Python, abra o CMD e digite o comando:
     
      ```bash
      where python
      
   - Clique em "OK" em todas as janelas para salvar as alterações.
   - Para a confirmar a configuração da Variavel de Ambiente, abra o CMD novamente e digite o comando:
     
      ```bash
      python --version
      
   - Caso aparecer: Python 3.12.3 (ou a versão instalada), está correto! Caso der erro, refaça novamente o procedimento.

4. Permissão para executar Scripts no Sistema Operacional Windows

   Caso o Sistema Operacional utlizado para executar o Projeto for o Windows e nunca foi executado nenhum tipo de Script, é provável que não seja possível executar o projeto. Em caso de erro de permissões:

   - Abrir o Windows PowerShell como Administrador.
   - Digitar o comando:

      ```bash
      Set-ExecutionPolicy RemoteSigned

   - Irá aparecer um texto informando se é desejável alterar as permissões, digite a letra "a" e pressione "Enter".
   - Pronto, é possivel e executar um Script no Sistema Operacional Windows
   
## Instalação do Projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/daltonpfdev/ag_controle_project.git

2. Entrar no arquivo de ambiente virtual (venv):

   ```bash
   .\venv\Scripts\activate

3. Verificar as bibliotecas necessárias para a execução do Projeto com o comando:

   - Comando para verificar as bibliotecas
     
      ```bash
      pip list
      
   - Bibliotecas
      - Dango
      - crispy-bootstrap
      - mysqlclient
      - validate-docbr
      
5. Instalações das Bibliotecas:

   - Django
     
       ```bash
       pip install django
      
   - crispy-bootstrap5
     
        ```bash
        pip install crispy-bootstrap5
      
   - mysqlclient
     
        ```bash
        pip install mysqlclient
        
   - validate-docbr
     
      ```bash
      pip install validate-docbr

## Configuração do Banco de Dados

Este projeto foi planejado para funcionar com o Banco de Dados Mysql. Verifique se seu Mysql WorkBench está na localhost com a Porta: 3306
Porem, caso preferirem, estou disponibilizando o arquivo db.sqlite3 que pode ser utilizado como Banco de Dados desse Projeto.
Aqui está ambas configurações:

1. Configuração do arquivo settings.py para o Banco de Dados MySql:
   ```markdown
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'app_controle',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': 3306,
       }
   }

1.1. No MySql WorkBench, crie uma nova Schema chamada "app_controle" e configure os campos "USER" e "PASSWORD" de acordo com a configuração do MySql WorkBench

2. Configuração do arquivo settings.py para o Banco de Dados Sqlite3
   ```markdown
   DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
       }
   }
   
4. Atualize as tabelas a partir dos Modelos de models.py do Projeto
   
   ```bash
   python manage.py makemigrations

6. Criação das tabelas a partir dos Modelos de models.py do Projeto
   
   ```bash
   python manage.py migrate

## Iniciar o Projeto

1. Para iniciar o Projeto na sua localhost:
   
   ```bash
   python manage.py runserver

3. Acesse o projeto em:
   
   ```markdown
   http://localhost:8000/
   
## Como Usar

Quando o projeto for iniciado, você será direcionado para a página de Registros das Saídas e, como não tem nenhum registro de nada, irá aparecer 2 botões: "Cadastrar Motorista" e "Cadastrar Veículo". Após os cadastros, na página inicial irá aparecer o Botão: "Realizar Nova Saída", onde irá aparcecer um formulário onde poderá ser escolhido um veículo e um motorista e dados adicionais que precisam ou não ser adicionadas. Feito o registro, é possivel visualizar o registro, editar o registro, excluir o registro e concluir o registro. Uma vez concluido, o veículo volta a ser disponível para ser feito uma nova saída.
