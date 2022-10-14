__________________________________________________________________________________
### Request Data Tweets in Twitter API:

##### Pré-requisitos:
- Baixe e instale o Python 3.7 ou superior para o seu sistema operacional. É necessário que você adicione o Python ao seu PATH, pois o conector do MySQL exige isso.

- Abra um prompt de comando ou shell do bash e verifique sua versão do Python, executando python -V com a opção V em maiúscula.

- O instalador do pacote pip está incluído nas versões mais recentes do Python. Executando pip install -U pip, atualize o pip para a versão mais recente.

- Se o pip não estiver instalado, você poderá baixá-lo e instalá-lo com get-pip.py. Para obter mais informações, confira Instalação.

- PostgressSQL

##### Linux
1. ###### Rode os seguintes comandos:
- $ _sudo apt update_
- $ _sudo apt install postgresql postgresql-contrib_
- $ _pip install pandas_
- $ _pip install psycopg2_

2. ###### Faça o login como usuário postgressSQL:
- $ _sudo -i -u postgres_
- $ _psql_
- $ _\q_
- $ _exit_
#### Criando banco de dados e usuário
1. ###### Faça o login como usuário postgressSQL e abrir psql CLI:
- $ _sudo -u postgres psql_
2. ###### Crie um banco de dados com o seguinte comando contendo o respectivo nome:
- $ _create database products;_
3. ###### Crie um novo usuário com uma senha com o seguinte comando:
- $ _create user username with encrypted password 'password';_
4. ###### Por fim, dê ao usuário todos os privilégios no banco de dados:
- $ _grant all privileges on database products to username;_

#### Rodando o projeto
1. ###### Esteja no diretorio **raiz** do projeto(obs: No mesmo nivel do arquivo main.py).

2. ###### Por fim apenas execute o arquivo main.py:
- $ _python main.py_

___________________________________________________________________________________

### Considerações finais:
Com isso sera feito o processamento do arquivo AppleStore.csv, requisitando os dados na API do Twitter e por fim gerando um JSON, CSV file e gravando as informações no banco de dados(PostgressSQL).