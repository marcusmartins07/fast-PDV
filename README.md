<h1 align="center" style="font-weight: bold;">Fast PDV</h1>

Foco na aprendizagem de vue.js e Django Rest API para desenvolver solução prática e rápida.
Frontend construido em Vue devido a sintaxe e estrura fácil de entender, praticidade para administrar requisições e alocação de dados.
Backend em Django devido a conhecimento prévio do framework e pela curiosidade do funcionamento de uma API REST com autenticação JWT

## Técnologias Utilizadas

<!--- # "Verify icons availability here https://github.com/tandpfun/skill-icons" -->

[![My Skills](https://skillicons.dev/icons?i=django,vuejs,docker,vite,nginx,bootstrap)](https://skillicons.dev)


Executando o projeto localmente (sem Docker)

Pré-requisitos:
Certifique-se de que as seguintes ferramentas estão instaladas em seu sistema:

Python 3.9+
Node.js 16+
Git

Clone o repósitorio: `git clone https://github.com/marcusmartins07/fast-pdv.git`

Executar backend (API):

1. **Crie e ative um ambiente virtual**: `python -m venv` `venv\Scripts\activate`
2. **Instale as blibiotecas necessárias**: `pip install -r requirements.txt`
3. **Realize as migrações e insira os dados iniciais**: `python manage.py makemigrations`
`python manage.py migrate`
`python manage.py shell < usuarios/bd_backup.py`
4. **Inicie o servidor**`python manage.py runserver`


Passos para rodar o frontend (Vue.js)

1. **Em um novo terminal chegue até diretório do frontend**: `cd ../fast_pdv`
2. **Instale as dependências**: `npm install`
3. **Inicie o servidor**: `npm run dev`


## Executando projeto com docker

1. **Configurar caminho relativo dos arquivos em docker-compose.yml**: `C:/Users/Meu-Computador/Downloads/fast-pdv-main/fast-pdv-main/API_Fast_PDV` e `C:/Users/Meu-Computador/Downloads/fast-pdv-main/fast-pdv-main/fast_pdv`
2. **Executar o projeto uma primeira vez**: `docker-compose up --build`
3. **Ajustar migrações alimentação das tabelas no Dockerfile da API**: `CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]`
4. **Executar novamente!**


Licença

Este software está disponível sob as seguintes licenças:

- [MIT](https://rem.mit-license.org)
