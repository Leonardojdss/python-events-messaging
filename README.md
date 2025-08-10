# Python Events Messaging - Sistema de Processamento de Eventos com AWS

![Arquitetura](arquitetura.png)

## 📋 Visão Geral

Este projeto implementa um sistema de processamento de eventos para registro de novos clientes utilizando os serviços AWS SNS (Simple Notification Service), SQS (Simple Queue Service), Lambda Functions e Aurora PostgreSQL Serverless V2. O sistema é construído em Python com arquitetura orientada a eventos e deployment via AWS SAM (Serverless Application Model).

## 🏗️ Arquitetura

O sistema segue o padrão de arquitetura orientada a eventos com os seguintes componentes:

- **AWS SNS**: Tópico para notificações de novos clientes
- **AWS SQS**: Fila para recebimento das mensagens do SNS
- **AWS Lambda**: Função para processamento das mensagens
- **Aurora PostgreSQL Serverless V2**: Banco de dados para persistência dos dados
- **AWS SAM**: Framework para deployment e gerenciamento da infraestrutura

### Fluxo de Dados

1. Uma mensagem é publicada no tópico SNS `NewClientNotification`
2. O SNS entrega a mensagem para a fila SQS `NewClientFunctionSQS`
3. A Lambda Function `RegisterNewClientFunction` é triggered pela fila SQS
4. A função processa os dados e persiste no banco Aurora PostgreSQL

## 📁 Estrutura do Projeto

```
python-events-messaging/
├── arquitetura.png                 # Diagrama da arquitetura
├── README.md                       # Documentação do projeto
├── template.yml                    # Template SAM para infraestrutura
├── samconfig.toml                  # Configurações do SAM CLI
├── local_test.py                   # Script para testes locais
├── env/                           # Ambiente virtual Python
└── ms_management_client/          # Módulo principal da aplicação
    ├── src/
    │   ├── app.py                 # Handler principal da Lambda
    │   ├── requirements.txt       # Dependências Python
    │   ├── infra/
    │   │   └── connection_postgresql.py  # Classe de conexão com PostgreSQL
    │   └── model/
    │       └── model.py           # Modelos SQLAlchemy
    └── tests/                     # Testes automatizados
        ├── test_app.py
        ├── infra/
        │   └── test_connection_postgresql.py
        └── model/
            └── test_model.py
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**: Linguagem principal
- **AWS Lambda**: Computação serverless
- **AWS SNS/SQS**: Mensageria
- **Aurora PostgreSQL Serverless V2**: Banco de dados
- **AWS SAM**: Framework de deployment
- **SQLAlchemy**: ORM para Python
- **psycopg2**: Driver PostgreSQL
- **python-dotenv**: Gerenciamento de variáveis de ambiente

## 🗄️ Modelo de Dados

### Tabela `costumers`

```sql
CREATE TABLE costumers (
    id SERIAL PRIMARY KEY,
    name_costumer VARCHAR(256) NOT NULL,
    email VARCHAR(256) NOT NULL,
    phone VARCHAR(256) NOT NULL
);
```

## 📨 Formato das Mensagens

### Mensagem de Entrada (JSON)

```json
{
  "name_costumer": "Leonardo",
  "email": "leonardo@example.com",
  "phone": "+5511999999999"
}
```
```json
{
  "name_costumer": "Leonardo",
  "email": "leonardo@example.com",
  "phone": "+5511999999999"
}
```

### Evento SQS Completo

```json
{
  "Records": [
    {
      "messageId": "6ab313ff-412c-4acd-86be-8b834166ab71",
      "receiptHandle": "AQEB4IJR81NS96isrghYgAs5auZR6PkuNaxG3obXakcXHOdXgkDMF/dfyboY76uKmZ23ynhSLScgkDM1SEzYudVjMtL4K0BK5UheHJno/678Gh22+WnnDSuqklIckWXdZYRbTAP7+MmLDmSkwBNGkedsxPUO0UxEFoZ0ToE5Lb5CYLEjJCgdqzt+RGOxsqMyjxdDb7COgCIAupdiLr34xsefX/oc7N/lfLiZGM3vYmYsjqqp/7i96cH/C1eQ/AFlZj83FKKnw0nKF3Ifh8OiM/4IqY/tcBR98G2n7shnPqG5wviU+mbWOTiJiwxMMLx4DWIlkkhdk/oHawT531oHjRLSGpBh6a8QMg0iXdWGOWqvPAhAJbqRgBsf5kzpOPA5+1Lq1t08s2AzuA9I0btOyYfMjA==",
      "body": "{\n  \"name_costumer\": \"Leonardo\",\n  \"email\": \"leonardo@example.com\",\n  \"phone\": \"+5511999999999\"\n}",
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1754815469280",
        "SenderId": "AIDAIT2UOQQY3AUEKVGXU",
        "ApproximateFirstReceiveTimestamp": "1754815469289"
      },
      "messageAttributes": {},
      "md5OfBody": "c86aae3d17e2f4f6a52e35c3c5962df2",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-1:154133135350:NewClientFunctionSQS",
      "awsRegion": "us-east-1"
    }
  ]
}
```

## 🚀 Como Executar

### Pré-requisitos

1. **AWS CLI** configurado com credenciais adequadas
2. **SAM CLI** instalado
3. **Python 3.12** instalado
4. **Docker** para builds locais

### Configuração do Ambiente

1. Clone o repositório:
```bash
git clone <repository-url>
cd python-events-messaging
```

2. Ative o ambiente virtual:
```bash
source env/bin/activate
```

3. Instale as dependências:
```bash
pip install -r ms_management_client/src/requirements.txt
```

4. Configure as variáveis de ambiente no arquivo `.env`:
```env
DB_HOST=your-aurora-endpoint
DB_PORT=5432
DB_NAME=your-database-name
DB_USER=your-username
DB_PASSWORD=your-password
```

### Deploy na AWS

1. Build da aplicação:
```bash
sam build
```

2. Deploy:
```bash
sam deploy --guided
```

### Teste Local

Execute o script de teste local:
```bash
python local_test.py
```