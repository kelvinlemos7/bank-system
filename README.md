# 🏦 Bank System API

<div align="center">

**[🇧🇷 Português](#-bank-system-api-pt-br) | [🇺🇸 English](#-bank-system-api-en)**

</div>

---

# 🏦 Bank System API (PT-BR)

Uma API REST estruturada para simulação de operações bancárias, com foco em boas práticas de arquitetura backend.

> Projeto focado em **boas práticas**, **organização**, **clareza de regras de negócio** e **evolução futura**.

---

## 🚀 Funcionalidades

### 👤 Usuários
* Criar usuário
* Listar usuários

### 💳 Contas
* Criar conta bancária
* Listar contas

### 💸 Transações
* Depósito
* Saque
* Transferência entre contas
* Validações de saldo
* Validação de conta de destino

---

## 🧱 Arquitetura do Projeto

O projeto segue uma arquitetura em camadas bem definida:
```
src/
├── controllers/      # Camada HTTP (orquestra requests e responses)
├── services/         # Regras de negócio
├── repositories/     # Acesso ao banco de dados
├── models/           # Models SQLAlchemy
├── schemas/          # Schemas Pydantic
├── routes/           # Definição das rotas
├── utils/            # Enums, erros, validações e handlers de exceção
├── database.py       # Conexão com o banco
└── app.py            # Inicialização da aplicação
```

### 🔁 Fluxo de uma requisição
```
Route → Controller → Service → Repository → Database
```

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12**
* **FastAPI**
* **SQLAlchemy**
* **Pydantic**
* **MySQL**
* **Uvicorn**

---

## ▶️ Como Rodar o Projeto

### 1️⃣ Clone o repositório
```bash
git clone <url-do-repositorio>
cd bank-system
```

### 2️⃣ Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure o ambiente

```bash
cp .env.example .env
```

Ajuste a `DATABASE_URL` conforme seu ambiente (host `db` é usado dentro do Docker).

### 5️⃣ Rode a aplicação

```bash
uvicorn src.app:app --reload
```
ou
```bash
$env:PYTHONPATH = "src"; uvicorn src.app:app --reload
```

### 6️⃣ Acesse a documentação

* Swagger UI: 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* OpenAPI JSON: 👉 [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

## 🚀 Como rodar com Docker
```bash
cp .env.example .env
docker-compose up --build
```

Acesse: http://localhost:8000/docs

---

## 📌 Endpoints Principais

### 👤 Usuários

| Método | Rota         | Descrição      |
| ------ | ------------ | -------------- |
| GET    | `/api/users` | Lista usuários |
| POST   | `/api/users` | Cria usuário   |

### 💳 Contas

| Método | Rota            | Descrição    |
| ------ | --------------- | ------------ |
| GET    | `/api/accounts` | Lista contas |
| POST   | `/api/accounts` | Cria conta   |

### 💸 Transações

| Método | Rota                                                   | Descrição          |
| ------ | ------------------------------------------------------ | ------------------ |
| POST   | `/api/transactions`                                    | Cria transação     |
| GET    | `/api/transactions/accounts/{account_id}/transactions` | Histórico da conta |

---

## 🔐 Regras de Negócio

* ❌ Saques e transferências não podem exceder o saldo
* ❌ Transferências exigem conta de destino válida
* ❌ Transferência para a própria conta não é permitida
* ✅ Depósitos aumentam o saldo
* ✅ Transferências debitam origem e creditam destino
* ✅ Saldo inicial de conta não pode ser negativo

---

## ⚠️ Tratamento de erros

Erros de negócio retornam códigos HTTP específicos em vez de `500`:

| Erro                              | Código | Quando ocorre                          |
| --------------------------------- | ------ | -------------------------------------- |
| `DuplicateUserError`              | `409`  | Email já cadastrado                    |
| `AccountNotFoundError`            | `404`  | Conta (ou destino) não encontrada      |
| `UserNotFoundError`               | `404`  | Usuário não encontrado                 |
| `InsufficientBalanceError`        | `400`  | Saldo insuficiente para saque/transferência |
| `InvalidValueError`               | `422`  | Valor inválido (zero/negativo)         |
| `InvalidEmailError` / `InvalidNameError` | `422` | Campos inválidos               |

---

## 📈 Próximas Evoluções (Ideias)

* Histórico de transações com paginação
* Extrato com saldo após cada transação
* Autenticação (JWT)
* Testes automatizados
* Banco PostgreSQL

---

## 🧠 Objetivo do Projeto

Este projeto foi criado com foco em **aprendizado real de backend**, organização de código, leitura profissional e preparação para sistemas maiores.

---

## 🧑‍💻 Autor

**Kelvin Kauan**

---
---

# 🏦 Bank System API (EN)

A structured REST API for simulating banking operations, focused on backend architecture best practices.

> Project focused on **best practices**, **organization**, **clear business rules**, and **future scalability**.

---

## 🚀 Features

### 👤 Users
* Create user
* List users

### 💳 Accounts
* Create bank account
* List accounts

### 💸 Transactions
* Deposit
* Withdrawal
* Transfer between accounts
* Balance validation
* Destination account validation

---

## 🧱 Project Architecture

The project follows a well-defined layered architecture:
```
src/
├── controllers/      # HTTP layer (orchestrates requests and responses)
├── services/         # Business rules
├── repositories/     # Database access
├── models/           # SQLAlchemy models
├── schemas/          # Pydantic schemas
├── routes/           # Route definitions
├── utils/            # Enums, errors, and validations
├── database.py       # Database connection
└── app.py            # Application entrypoint
```

### 🔁 Request Flow
```
Route → Controller → Service → Repository → Database
```

---

## 🛠️ Tech Stack

* **Python 3.12**
* **FastAPI**
* **SQLAlchemy**
* **Pydantic**
* **MySQL**
* **Uvicorn**

---

## ▶️ How to Run

### 1️⃣ Clone the repository
```bash
git clone <repository-url>
cd bank-system
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure the environment

```bash
cp .env.example .env
```

Adjust the `DATABASE_URL` to your environment (host `db` is used inside Docker).

### 5️⃣ Start the application
```bash
uvicorn src.app:app --reload
```
or
```bash
$env:PYTHONPATH = "src"; uvicorn src.app:app --reload
```

### 6️⃣ Access the docs
* Swagger UI: 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* OpenAPI JSON: 👉 [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

## 🚀 Running with Docker
```bash
cp .env.example .env
docker-compose up --build
```

Access: http://localhost:8000/docs

---

## 📌 Main Endpoints

### 👤 Users

| Method | Route        | Description  |
| ------ | ------------ | ------------ |
| GET    | `/api/users` | List users   |
| POST   | `/api/users` | Create user  |

### 💳 Accounts

| Method | Route           | Description     |
| ------ | --------------- | --------------- |
| GET    | `/api/accounts` | List accounts   |
| POST   | `/api/accounts` | Create account  |

### 💸 Transactions

| Method | Route                                                  | Description             |
| ------ | ------------------------------------------------------ | ----------------------- |
| POST   | `/api/transactions`                                    | Create transaction      |
| GET    | `/api/transactions/accounts/{account_id}/transactions` | Account history         |

---

## 🔐 Business Rules

* ❌ Withdrawals and transfers cannot exceed the available balance
* ❌ Transfers require a valid destination account
* ❌ Transfer to the same account is not allowed
* ✅ Deposits increase the account balance
* ✅ Transfers debit the source and credit the destination
* ✅ Initial account balance cannot be negative

---

## ⚠️ Error Handling

Business errors return specific HTTP codes instead of `500`:

| Error                             | Code | When it happens                             |
| --------------------------------- | ---- | ------------------------------------------- |
| `DuplicateUserError`              | `409` | Email already registered                    |
| `AccountNotFoundError`            | `404` | Account (or destination) not found          |
| `UserNotFoundError`               | `404` | User not found                              |
| `InsufficientBalanceError`        | `400` | Insufficient balance for withdrawal/transfer |
| `InvalidValueError`               | `422` | Invalid amount (zero/negative)              |
| `InvalidEmailError` / `InvalidNameError` | `422` | Invalid fields                    |

---

## 📈 Planned Improvements

* Paginated transaction history
* Balance snapshot after each transaction
* Authentication (JWT)
* Automated tests
* PostgreSQL support

---

## 🧠 Project Goal

This project was built with a focus on **real backend learning** — clean code organization, professional readability, and preparation for larger systems.

---

## 🧑‍💻 Author

**Kelvin Kauan**
