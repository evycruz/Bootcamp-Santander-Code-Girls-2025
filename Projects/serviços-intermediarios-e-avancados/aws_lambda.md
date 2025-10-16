# AWS Lambda

O **AWS Lambda** é um serviço de **computação serverless** da AWS que permite executar código **sem precisar gerenciar servidores**, cobrando apenas pelo tempo de execução e recursos utilizados.

---

## Conceito de AWS Lambda

- **Serverless:** você não precisa provisionar ou gerenciar servidores.  
- **Execução sob demanda:** o código é executado apenas quando acionado por eventos.  
- **Escalabilidade automática:** o Lambda ajusta a quantidade de instâncias conforme a demanda.  
- **Integração nativa com AWS:** funciona com S3, DynamoDB, API Gateway, CloudWatch, SNS, SQS, entre outros.

---

## Principais Componentes

- **Funções (Lambda Functions):** unidades de código que realizam tarefas específicas.  
- **Eventos (Triggers):** gatilhos que disparam a execução da função, como upload em S3 ou atualização em DynamoDB.  
- **Runtime:** ambiente de execução do código, suportando várias linguagens como Python, Node.js, Java, Go e .NET.  
- **Execution Role:** permissões atribuídas à função para acessar outros serviços AWS.  
- **Layers:** pacotes adicionais de bibliotecas e dependências compartilhadas entre funções.  

---

## Benefícios

- **Custo sob demanda:** paga apenas pelo tempo em que o código é executado e pela memória utilizada.  
- **Escalabilidade automática:** suporta desde poucas requisições até milhões simultâneas.  
- **Redução de complexidade:** elimina necessidade de gerenciar infraestrutura.  
- **Integração com AWS:** conecta-se facilmente a diversos serviços AWS para criar arquiteturas completas.  
- **Manutenção simplificada:** atualizações e patches de infraestrutura são gerenciados pela AWS.

---

## Casos de Uso Comuns

- Processamento de arquivos e imagens em S3.  
- APIs serverless usando API Gateway + Lambda.  
- Processamento de eventos de streams do DynamoDB ou Kinesis.  
- Automação de tarefas administrativas e workflows.  
- Notificações e integração de eventos com SNS/SQS.

---
