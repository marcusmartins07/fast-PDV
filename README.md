# Fast PDV

**Foco na aprendizagem de Vue.js e Django REST API para desenvolver uma solução prática e rápida.**  
O frontend foi construído em **Vue.js** devido à sua sintaxe simples e estrutura fácil de entender, oferecendo praticidade para gerenciar requisições e dados.  
O backend foi desenvolvido em **Django** por conhecimento prévio no framework e curiosidade em explorar o funcionamento de uma API REST com autenticação JWT.

---

## 🛠️ Tecnologias Utilizadas

[![My Skills](https://skillicons.dev/icons?i=django,vuejs,docker,vite,nginx,bootstrap)](https://skillicons.dev)

---

## ⚙️ Pré-requisitos

Certifique-se de que as seguintes ferramentas estão instaladas no seu sistema:

- **Python 3.9+**
- **Node.js 16+**
- **Git**

Clone o repositório em sua máquina local:  
```bash
git clone https://github.com/marcusmartins07/fast-pdv.git
```

---

## 🖥️ Executando o Projeto Localmente (Sem Docker)

### **Backend (API)**

1. **Crie e ative um ambiente virtual**:  
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Instale as bibliotecas necessárias**:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Realize as migrações e insira os dados iniciais**:  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py shell < usuarios/bd_backup.py
   ```

4. **Inicie o servidor**:  
   ```bash
   python manage.py runserver
   ```

---

### **Frontend (Vue.js)**

1. **Em um novo terminal, navegue até o diretório do frontend**:  
   ```bash
   cd fast_pdv
   ```

2. **Instale as dependências**:  
   ```bash
   npm install
   ```

3. **Inicie o servidor de desenvolvimento**:  
   ```bash
   npm run dev
   ```

---

## 🐳 Executando o Projeto com Docker

1. **Configure os caminhos relativos no arquivo `docker-compose.yml`**:  
   Atualize os caminhos para apontar para os diretórios locais:  
   - Backend: `C:/Users/Seu-Usuario/fast-pdv-main/API_Fast_PDV`  
   - Frontend: `C:/Users/Seu-Usuario/fast-pdv-main/fast_pdv`

2. **Execute o projeto pela primeira vez**:  
   ```bash
   docker-compose up --build
   ```

3. **Ajuste as migrações e a inserção de dados no Dockerfile da API**:  
   Atualize o comando final para:  
   ```bash
   CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]
   ```

4. **Reinicie o contêiner**:  
   ```bash
   docker-compose up --build
   ```

---

## 📜 Licença

Este software está disponível sob a licença [MIT](https://rem.mit-license.org).
