# ag_controle_project
CRUD em python utilizando o Framework Django com banco de dados MySql

Controle de Motoristas e Veículos
Este projeto Django é um CRUD (Create, Read, Update, Delete) para o controle de motoristas, veículos e saídas de veículos. Ele permite que você gerencie informações sobre motoristas, veículos e registros de saída de veículos associados aos motoristas.

Funcionalidades
Cadastro de motoristas com nome, telefone e número de CNH.
Cadastro de veículos com placa, marca, tipo de veículo e quilometragem para troca de óleo.
Registro de saídas de veículos, incluindo data e hora de saída, quilometragem de saída, destino, data e hora de retorno, quilometragem de retorno e quilometragem percorrida.
Controle de disponibilidade de veículos, garantindo que um veículo só possa ser utilizado se estiver disponível.
Interface amigável para visualização e gerenciamento dos registros de controle.

Instalação

Clone o repositório:
git clone https://github.com/seu-usuario/nome-do-repositorio.git

Instale as dependências:
pip install -r requirements.txt

Execute as migrações do Django:
python manage.py migrate

Inicie o servidor de desenvolvimento:
python manage.py runserver

Acesse o projeto em http://localhost:8000/

Uso
Acesse a página de administração em http://localhost:8000/admin/.
Faça login com as credenciais de superusuário criadas durante a instalação.
Gerencie os registros de motoristas, veículos e saídas de veículos.
Contribuição
Sinta-se à vontade para abrir problemas (issues) e enviar pull requests com melhorias.
Para grandes mudanças, por favor, abra uma issue primeiro para discutir o que você gostaria de mudar.
Licença
Este projeto está licenciado sob a MIT License.
