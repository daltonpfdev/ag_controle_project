# Controle de Motoristas e Veículos

Este projeto Django é um CRUD (Create, Read, Update, Delete) para o controle de motoristas, veículos e saídas de veículos. Ele permite que você gerencie informações sobre motoristas, veículos e registros de saída de veículos associados aos motoristas.

## Funcionalidades

- Cadastro de motoristas com nome, telefone e número de CNH.
- Cadastro de veículos com placa, marca, tipo de veículo e quilometragem para troca de óleo.
- Registro de saídas de veículos, incluindo data e hora de saída, quilometragem de saída, destino, data e hora de retorno, quilometragem de retorno e quilometragem percorrida.
- Controle de disponibilidade de veículos, garantindo que um veículo só possa ser utilizado se estiver disponível.
- Interface amigável para visualização e gerenciamento dos registros de controle.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git

2. Entrar no arquivo de ambiente virtual (venv):

   ```bash
   .\venv\Scripts\activate

3. Verificar as bibliotecas necessárias para a execução do Projeto com o comando:

   -Comando para verificar as bibliotecas
      ```bash
         pip list
      
4. Lista de bibliotecas python necessárias para o Projeto:

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

2. Configuração do arquivo settings.py para o Banco de Dados Sqlite3
   ```markdown
   DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
       }
   }




   
   

   
